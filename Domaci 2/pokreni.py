from obrada import CSVIzvor, ServisRezervacija, TekstualniIzvjestaj

servis = ServisRezervacija(
    CSVIzvor("rezervacije.csv"), TekstualniIzvjestaj("izvjestaj.txt")
)
print(servis.obradi())
