class Begivenhed: #Opretter superklassen begivenhed.
    def __init__(self, title, kategori, date, time): #Information til begivenheder markeres med title, kategori, dato og tidspunkt.
        self.title = title
        self.kategori = kategori
        self.date = date
        self.time = time

    def get_visning(self): #Funktion der returnere tekstvisning af en begivenhed.
        return f"{self.title} ({self.kategori}) - {self.date} kl. {self.time}"

    def __str__(self): #Mulighed for at printe objekter.
        return self.get_visning()


#Subklasse 1 (Tid er altid en heldagsbegivenhed)
class HeldagsBegivenhed(Begivenhed):
    def __init__(self, title, kategori, date):
        super().__init__(title, kategori, date, "Hele dagen")

    def get_visning(self):
        return f"{self.title} ({self.kategori}) - {self.date} (Hele dagen)"


# SUBKLASSE 2 (Begivenheder der forgår årligt og som ikke har et tidspunkt)
class ÅrligBegivenhed(Begivenhed):
    def __init__(self, title, kategori, date):
        super().__init__(title, kategori, date, "")

    def get_visning(self): #Overskriver get_visning så den viser at en begivenhed sker årligt.
        return f"{self.title} ({self.kategori}) - hvert år den {self.date}"


# SUBKLASSE 3 (Online begivenhed vises med link)
class OnlineBegivenhed(Begivenhed):
    def __init__(self, title, kategori, date, time, link):
        super().__init__(title, kategori, date, time)
        self.link = link

    def get_visning(self): #Omskriver get_visning til at vise link
        return f"{self.title} (Online) - {self.date} kl. {self.time} • Link: {self.link}"


# REGISTER
class BegivenhedsRegister:
    def __init__(self):
        self.registrere = [ #Laver en liste med begivenhedsobjekter
            Begivenhed("Frokost", "Privat", "24 Januar 2024", "14:00"),
            HeldagsBegivenhed("Skolefri", "Andet", "21 Februar 2027"),
            ÅrligBegivenhed("Fødselsdag", "Privat", "07 Marts"),
        ]

    def tilføj(self, begivenhed): #tilføjer nye begivenheder
        self.registrere.append(begivenhed)

    def vis(self): #Udskriver alle registreret begivenheder
        for begivenhed in self.registrere:
            print(begivenhed)

#Opretter et registreret bibliotek objekt.
bib = BegivenhedsRegister()


# FUNKTION FRA MAIN
#Opretter en ny begivenhed baseret ud fra typen
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
        raise ValueError("Ukendt begivenhedstype!") #Hvis typen ikke findes opstår der en fejl

    bib.tilføj(ny_begivenhed) #Begivenhed tilføjes til bibliokteket og viser alle begivenheder.
    print("Begivenhed oprettet!")
    bib.vis()
