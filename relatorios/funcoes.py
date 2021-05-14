from relatorios.models import *
from cte.models import CTE
from rest_framework import serializers
from django.core.exceptions import ObjectDoesNotExist

import json
import sys

def checknotfound():
    id_valid = []
    id_error = []
    relatorios = ENTREGA.objects.filter(printable = False)
    for x in relatorios :
        ok = True
        misingcte = CTENotFound.objects.filter(relatorio = x.id)
        for y in misingcte:
            try:
                cte = CTE.objects.filter(NR_DACTE= y.cte).get()
                _cte = CTE_FPag.objects.create(
                    CTE = cte,
                    F_PAGAMENTO=F_PAGAMENTO.objects.get(pk=y.F_PAGAMENTO.id)
                )
                x.CTE_FPag.add(_cte)
                y.delete()
            except ObjectDoesNotExist:
                id_error.append({"_id": x.id, "msg": "CTE não encontrado no banco de dados", "n_cte": y.cte})
                ok = False

        if ok == True :
            x.printable = True
            x.save()
            id_valid.append(x.id)
        else:
            x.save()
            
    return {"succes": id_valid, "error": id_error}
