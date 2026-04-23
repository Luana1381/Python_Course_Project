from studente import Studente

# Creazione degli oggetti (nel nostro caso, studenti)
studente1 = Studente("Luana", "Fasiello", 27, "12345")
studente2 = Studente("Marco", "Rossi", 25, "67890")

# Presentazione studenti
print(studente1.presentati())
print(studente2.presentati())

print("\n--- Aggiunta voti ---")

# Aggiunta voti appartenenti a studente1
studente1.aggiungi_voto(28)
studente1.aggiungi_voto(30)
studente1.aggiungi_voto(27)

# Aggiunta voti per studente2
studente2.aggiungi_voto(25)
studente2.aggiungi_voto(26)

# Calcolo media voti per entrambi gli studenti
print(f"Media voti {studente1.nome}: {studente1.calcola_media()}")
print(f"Media voti {studente2.nome}: {studente2.calcola_media()}")

print("\n--- Attività di studio ---")

# Attività di ogni studente (in ore di studio)
studente1.studia(3)
studente2.studia(2)

