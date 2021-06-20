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

def checktype(search_field):

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

    elif(bool(re.search("remetente|REMETENTE|Remetente", search_field))):
        term = re.sub("\s", "", re.sub("remetente|REMETENTE|Remetente", "", search_field), 1)
        query = CTE.objects.filter(REMETENTE__icontains=term)
        try:
            return cte_search(query)
        except:
            return Response(status=404)

    elif(bool(re.search("destinatario|DESTINATARIO|Destinatario", search_field))):
        term = re.sub("\s", "", re.sub("destinatario|DESTINATARIO|Destinatario", "", search_field), 1)
        query = CTE.objects.filter(DESTINATARIO__icontains=term)
        try:
            return cte_search(query)
        except:
            return Response(status=404)

    elif(bool(re.search("nfe|NFE|nota|Nota", search_field))):
        term = re.sub('\s', '', re.sub("nfe|NFE|nota|Nota", '', search_field))
        try:
            int(term)
            query = CTE.objects.filter(NFE__icontains=term)
            return cte_search(query)
        except:
            return Response(status=500)
    
    else:
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
    serializer = EntregaRetrieveSerializer(query, many=True)
    return Response(serializer.data)

def cte_search(query):
    serializer = CTESerializer(query, many=True)
    fpga = CTE_FPag.objects.filter(CTE=query[0])
    rel = []
    for x in fpga:
        rel.append(ENTREGA.objects.filter(CTE_FPag=x).values()[0])
    # rel = ENTREGA.objects.filter(CTE_FPag=fpga).values()
    return Response({'cte': serializer.data, "rel": rel})
