from rest_framework import viewsets
from rest_framework.response import Response
from django.db.models import Q
from django.contrib.postgres.search import SearchVector

from rest_framework.permissions import IsAuthenticated

from relatorios.models import *
from relatorios.serializers import *
import re
import datetime

class SearchViewset(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)
    def list(self, request, search):
        return checktype(search)

def checktype(_search_field):
    search_field = _search_field.lower()

    if(bool(re.match("^[a-zA-Z]{3}[0-9]", search_field))):
        # CTB167664-4
        query = CTE.objects.filter(NR_CONTROLE__icontains=search_field)
        try:
            return cte_search(query)
        except:
            return Response(status=404)

    elif(len(search_field) == 6 or len(search_field) == 44):
        query = CTE.objects.filter(NR_DACTE__icontains=search_field)
        try:
            return cte_search(query)
        except:
            return Response(status=404)

    elif(bool(re.match("[0-3][0-9][-][0-1][0-9][-][0-9][0-9]", search_field)) or bool(re.match("[0-3][0-9][-][0-1][0-9][-][2][0][0-9][0-9]", search_field)) or bool(re.match("[0-3][0-9][-][0-1][0-9]", search_field))):
        return date(search_field)

    elif(bool(re.search("remetente|rem", search_field))):
        
        term = re.sub("\s", "", re.sub("remetente|rem", "", search_field), 1)
        query = CTE.objects.filter(REMETENTE__icontains=term)
        try:
            return cte_search(query)
        except:
            return Response(status=404)

    elif(bool(re.search("destinatario|dest|des", search_field))):
        term = re.sub("\s", "", re.sub("destinatario|dest|des", "", search_field), 1)
        query = CTE.objects.filter(DESTINATARIO__icontains=term)
        try:
            return cte_search(query)
        except:
            return Response(status=404)

    elif(bool(re.search("nfe|nota|nf", search_field))):
        term = re.sub('\s', '', re.sub("nfe|nota|nf", '', search_field))
        try:
            int(term)
            query = CTE.objects.filter(NFE__icontains=term)
            return cte_search(query)
        except:
            return Response(status=500)

    elif(bool(re.search("relatorio|rel", search_field))):
        term = int(re.sub('\s', '', re.sub("relatorio|rel", '', search_field)))
        try:
            query = ENTREGA.objects.get(pk=term)
            return return_rel(query, many=False)
        except:
            return Response(status=404)

    else:
        try:
            query = ENTREGA.objects.get(pk=int(search_field))
            return return_rel(query, many=False)
        except:
            try:
                query = CTE.objects.filter(
                    Q(DESTINATARIO__icontains=search_field) | 
                    Q(REMETENTE__icontains=search_field) | 
                    Q(NFE__icontains=search_field) |
                    Q(NR_DACTE__icontains=search_field) | 
                    Q(NR_CONTROLE__icontains=search_field)
                    )
                return cte_search(query)

            except:
                return Response(status=404)

def date(sch_field):
    try:
        date_obj = datetime.datetime.strptime(sch_field, '%d-%m-%y')
    except:
        try:
            date_obj = datetime.datetime.strptime(sch_field, '%d-%m-%Y')
        except:
            _date_obj = datetime.datetime.strptime(sch_field, '%d-%m')
            date_obj = _date_obj.replace(year=datetime.date.today().year)
    
    query = ENTREGA.objects.filter(DATA__date=date_obj)
    return return_rel(query, many=True)

def cte_search(query):
    serializer = CTESerializer(query, many=True)
    fpga = CTE_FPag.objects.filter(CTE=query[0])
    rel = []
    for x in fpga:
        rel.append(ENTREGA.objects.filter(CTE_FPag=x).values()[0])
    # rel = ENTREGA.objects.filter(CTE_FPag=fpga).values()
    return Response({'cte': serializer.data, "rel": rel})

def return_rel(query, many):
    serializer = EntregaRetrieveSerializer(query, many=many)
    return Response(serializer.data)
