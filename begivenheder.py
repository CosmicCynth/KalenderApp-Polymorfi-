

class Begivenhed:
    def __init__(self, title, kategori, date, time):
        self.title = title
        self.kategori = kategori
        self.date = date
        self.time = time

    def get_visning(self):
        return f"{self.title} ({self.kategori}) - {self.date} kl. {self.time}"

    def __str__(self):
        return self.get_visning()


# SUBKLASSE 1 – Heldagsbegivenhed (tid bliver altid 'Hele dagen')
class HeldagsBegivenhed(Begivenhed):
    def __init__(self, title, kategori, date):
        super().__init__(title, kategori, date, "Hele dagen")

    def get_visning(self):
        return f"{self.title} ({self.kategori}) - {self.date} (Hele dagen)"


# SUBKLASSE 2 – Årlig begivenhed (KRÆVER IKKE TIME)
class ÅrligBegivenhed(Begivenhed):
    def __init__(self, title, kategori, date):
        super().__init__(title, kategori, date, "")

    def get_visning(self):
        return f"{self.title} ({self.kategori}) - hvert år den {self.date}"


# SUBKLASSE 3 – Online begivenhed
class OnlineBegivenhed(Begivenhed):
    def __init__(self, title, kategori, date, time, link):
        super().__init__(title, kategori, date, time)
        self.link = link

    def get_visning(self):
        return f"{self.title} (Online) - {self.date} kl. {self.time} • Link: {self.link}"


# REGISTER
class BegivenhedsRegister:
    def __init__(self):
        self.registrere = [
            Begivenhed("Frokost", "Privat", "24 Januar 2024", "14:00"),
            HeldagsBegivenhed("Skolefri", "Andet", "21 Februar 2027"),
            ÅrligBegivenhed("Fødselsdag", "Privat", "07 Marts"),
        ]

    def tilføj(self, begivenhed):
        self.registrere.append(begivenhed)

    def vis(self):
        for begivenhed in self.registrere:
            print(begivenhed)


bib = BegivenhedsRegister()


# FUNKTION FRA MAIN – kan stadig kaldes som før
def nyBegivenhed(titlebeg, kategoribeg, datebeg, timebeg, type="normal"):
    if type == "normal":
        ny_begivenhed = Begivenhed(titlebeg, kategoribeg, datebeg, timebeg)

    elif type == "heldag":
        ny_begivenhed = HeldagsBegivenhed(titlebeg, kategoribeg, datebeg)

    elif type == "årlig":
        ny_begivenhed = ÅrligBegivenhed(titlebeg, kategoribeg, datebeg)

    elif type == "online":
        ny_begivenhed = OnlineBegivenhed(titlebeg, kategoribeg, datebeg, timebeg, link="www.mødelink.com")

    else:
        raise ValueError("Ukendt begivenhedstype!")

    bib.tilføj(ny_begivenhed)
    print("Begivenhed oprettet!")
    bib.vis()
