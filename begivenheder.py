Begivenheder = dict()

class Begivenhed:
    def __init__(self, title, kategori, date, time):
        self.title = title
        self.kategori = kategori
        self.date = date
        self.time = time

    def __str__(self):
        return f"{self.title} ({self.kategori}) - {self.date} kl. {self.time}"

class BegivenhedsRegister:
    def __init__(self):
        self.registrere = [
            Begivenhed("Frokost", "Privat", "24 Januar 2024", "14:00"),
            Begivenhed("Skole", "Andet", "21 Februar 2027", "12:00"),
        ]

    def tilføj(self, begivenhed):
        self.registrere.append(begivenhed)

    def vis(self):
        for begivenhed in self.registrere:
            print(begivenhed)


bib = BegivenhedsRegister()


def nyBegivenhed():
    registrerSvar = input("Vil du oprette en ny begivenhed? (ja/nej): ").lower()

    if registrerSvar == "ja":
        title = input("Navn: ")
        kategori = input("Kategori: ")
        date = input("Dato: ")
        time = input("Tidspunkt: ")

        ny_begivenhed = Begivenhed(title, kategori, date, time)
        bib.tilføj(ny_begivenhed)
        print("Begivenhed oprettet!")
    else:
        print("Ingen begivenhed oprettet")


nyBegivenhed()
bib.vis()