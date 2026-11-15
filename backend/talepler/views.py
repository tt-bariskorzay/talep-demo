import json

from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from .models import Talep

ALANLAR = {f.name for f in Talep._meta.get_fields()} - {"id", "olusturma"}


def ortam(request):
    return JsonResponse({"ortam": settings.ORTAM, "surum": settings.SURUM})


@csrf_exempt
@require_http_methods(["GET", "POST"])
def talepler(request):
    if request.method == "GET":
        return JsonResponse({"talepler": [t.sozluk() for t in Talep.objects.all()[:20]]})

    try:
        veri = json.loads(request.body or b"{}")
    except json.JSONDecodeError:
        return JsonResponse({"hata": "Geçersiz istek"}, status=400)
    if not str(veri.get("baslik", "")).strip():
        return JsonResponse({"hata": "Başlık zorunludur"}, status=400)

    talep = Talep(**{k: v for k, v in veri.items() if k in ALANLAR and v not in (None, "")})
    talep.full_clean()
    talep.save()
    return JsonResponse(talep.sozluk(), status=201)
