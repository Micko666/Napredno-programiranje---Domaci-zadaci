import json
from pathlib import Path
putanja = Path(__file__).with_name("Domaci_3.ipynb")
with open(putanja, encoding="utf-8") as fajl:
    celije = json.load(fajl)["cells"]
for celija in celije:
    if celija["cell_type"] != "code":
        continue
    kod = "".join(celija["source"])
    if kod.startswith("for naziv in"):
        continue
    exec(kod, globals())
def test_knn():
    assert type(kreiraj_model("knn")) is KNeighborsClassifier
def test_stablo():
    assert type(kreiraj_model("stablo")) is DecisionTreeClassifier
def test_mae():
    assert izracunaj_metriku([3, 5], [2, 7], "mae") == 1.5
def test_mse():
    assert izracunaj_metriku([3, 5], [2, 7], "mse") == 2.5
def test_accuracy():
    assert izracunaj_metriku([0, 1, 2], [0, 2, 2], "accuracy") == 2 / 3
def test_observer():
    dogadjaji = []
    def prati(dogadjaj, **podaci):
        dogadjaji.append(dogadjaj)
    trener = Trener()
    trener.pretplati(prati)
    trener.treniraj(kreiraj_model("knn"), [[1, 2], [2, 3], [3, 4]], [0, 1, 0])
    assert dogadjaji == ["pocetak_treninga", "kraj_treninga"]
def test_iris():
    assert IrisEksperiment("knn").pokreni() > 0.8
