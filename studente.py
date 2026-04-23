class Studente:
    # Costruzione classe 
    def __init__(self, nome, cognome, eta, matricola):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta
        self.matricola = matricola
        self.voti = [] #Inizialmente la lista creata è una lista vuota

    # Presentazione studente
    def presentati(self):
        return f"Ciao, sono {self.nome} {self.cognome}, ho {self.eta} anni e la mia matricola è {self.matricola}."
    
    # Aggiunta di un voto alla lista 
    def aggiungi_voto(self, voto):
        self.voti.append(voto)

    # Calcolo della media dei voti
    def calcola_media(self):
        if len(self.voti) == 0:
            return 0
        return sum(self.voti) / len(self.voti)
    
    # Descrizione attività dello studente in termini di studio (in ore)
    def studia(self, ore):
        print(f"{self.nome} sta studiando per {ore} ore.")
        

    