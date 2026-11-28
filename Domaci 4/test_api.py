from fastapi.testclient import TestClient

from main import app

klijent = TestClient(app)


def test_health():
    r = klijent.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_cijena_bez_popusta():
    r = klijent.post("/cijena", json={"noci": 3, "cijena_noci": 80})
    assert r.status_code == 200
    assert r.json()["iznos"] == 240.0


def test_cijena_sa_popustom():
    r = klijent.post("/cijena", json={"noci": 3, "cijena_noci": 80, "popust": 0.2})
    assert r.status_code == 200
    assert r.json()["iznos"] == 192.0


def test_jedna_noc():
    r = klijent.post("/cijena", json={"noci": 1, "cijena_noci": 80})
    assert r.status_code == 200
    assert r.json()["iznos"] == 80.0


def test_trideset_noci():
    r = klijent.post("/cijena", json={"noci": 30, "cijena_noci": 80})
    assert r.status_code == 200
    assert r.json()["iznos"] == 2400.0


def test_popust_100_posto():
    r = klijent.post("/cijena", json={"noci": 2, "cijena_noci": 80, "popust": 1})
    assert r.status_code == 200
    assert r.json()["iznos"] == 0.0


def test_nula_noci():
    r = klijent.post("/cijena", json={"noci": 0, "cijena_noci": 80})
    assert r.status_code == 422


def test_previse_noci():
    r = klijent.post("/cijena", json={"noci": 31, "cijena_noci": 80})
    assert r.status_code == 422


def test_negativna_cijena():
    r = klijent.post("/cijena", json={"noci": 2, "cijena_noci": -80})
    assert r.status_code == 422


def test_prevelika_cijena():
    r = klijent.post("/cijena", json={"noci": 2, "cijena_noci": 1000001})
    assert r.status_code == 422


def test_neispravan_popust():
    r = klijent.post("/cijena", json={"noci": 2, "cijena_noci": 80, "popust": 1.5})
    assert r.status_code == 422


def test_nedostaje_cijena():
    r = klijent.post("/cijena", json={"noci": 2})
    assert r.status_code == 422
