from relatorios.models import *
from cte.models import CTE

import json

def checknotfound():
    
    relatorios = ENTREGA.objects.filter(printable = False)
    ok = True
    for x in relatorios :
        misingcte = CTENotFound.objects.filter(relatorio = x.id)
        for y in misingcte:
            try:
                _cte = CTE_FPag.objects.create(
                    CTE = CTE.objects.filter(NR_DACTE= y.cte).get(),
                    F_PAGAMENTO=F_PAGAMENTO.objects.get(pk=y.F_PAGAMENTO.id)
                )
                x.CTE_FPag.add(_cte)
                y.delete()
            except:
                ok = False
        if ok :
            x.printable = True
            x.save()