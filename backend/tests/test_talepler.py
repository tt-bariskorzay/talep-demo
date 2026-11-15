import json

import pytest

from talepler.models import Talep

pytestmark = pytest.mark.django_db


def gonder(client, veri):
    return client.post("/api/talepler/", json.dumps(veri), content_type="application/json")


def test_talep_olusturulur(client):
    yanit = gonder(client, {"baslik": "Yazıcı çalışmıyor", "aciklama": "3. kat"})
    assert yanit.status_code == 201
    assert Talep.objects.count() == 1


def test_basliksiz_talep_reddedilir(client):
    yanit = gonder(client, {"aciklama": "Başlık yok"})
    assert yanit.status_code == 400
    assert Talep.objects.count() == 0


def test_bozuk_istek_400_doner(client):
    yanit = client.post("/api/talepler/", bytes([0xFF, 0xFE]), content_type="application/json")
    assert yanit.status_code == 400


def test_talepler_listelenir(client):
    Talep.objects.create(baslik="Birinci")
    Talep.objects.create(baslik="İkinci")
    yanit = client.get("/api/talepler/")
    assert yanit.status_code == 200
    assert len(yanit.json()["talepler"]) == 2


def test_ortam_bilgisi_doner(client):
    yanit = client.get("/api/ortam/")
    assert set(yanit.json()) == {"ortam", "surum"}
