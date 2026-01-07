
#opgaver = dict()


#class opgaver:
    #def __init__(self, title, kort_beskrivelse, deadline):
        #self.title = title
        #self.kort_beskrivelse = kort_beskrivelse
        #self.deadline = deadline

    #opgaver.append(opgaver)

    #opgaver = {"title" : "gåtur", "rengøring", "lektier"}
    #opgaver = {"deadline" : "2 timer", "5 timer", "1 timer"}


#færdigøre shit



class opgave:
    def __init__(self, titel):
        self.titel = titel

    def beskrivelse(self):

        pass

class lektie(opgave):
    def __init__(self, titel, sider):
        super().__init__(titel)
        self.sider = sider

    def beskrivelse(self):
        return f"lektie: {self.titel} på {self.sider}"

class deadline(opgave):
    def __init__(self, titel, dato):
        super().__init__(titel)
        self.dato = dato

    def beskrivelse(self):
        return f"deadline: {self.titel} d. {self.dato}"

opgaver = []

opgaver.append(lektie("matematik", 10))
opgaver.append(deadline("matematik", "12/1"))

for opgave in opgaver:
    print(opgave.beskrivelse())

