# Python_Course_Project
Simple Python Project  

# Dettagli Progetto e Gestione Classe Studente 
Questo progetto implementa, in linguaggio Python,  una semplice applicazione basata sulla **programmazione orientata agli oggetti (OOP)** per la gestione di studenti universitari.  
L'obiettivo è modellare uno studente come oeggetto, dotato di attributi e comportamenti, e dimostrare come più istanze della stessa classe possano mantenere **stati indipendenti**.  

## Struttura del progetto 
Il progetto è organizzato in modo modulare:
- "studente.py": contiene la definziione della classe "Studente";  
- "main.py": contiente il programma principale che crea e utilizza gli oggetti.  
Questa seprazione consente maggiore chiarezza, riutilizzabilità del codice e una migliore organizzazione logica. 
  
## Funzionalità implementate
La classe "Studente" permette di: 
- memorizzare dati anagrafici (nome, cognome, età, matricola);
- gestire una lista di voti (per ogni studente); 
- aggiungere nuovi voti;
- calcolare la media dei voti;
- descrivere l'attività degli studenti in termini di ore di studio;
- fornire una presentazione dello studente. 

## Esecuzione del programma
Per eseguire il progetto: 
1. Aprire il terminale
2. Spostarsi nella cartella del progetto 
3. Eseguire il seguente comando

```bash
python main.py  
```

Eseguendo il programma, si ottiene un output simile al seguente: 
" Ciao, sono Luana Fasiello, ho 27 anni e la mia matricola è 12345.
Ciao, sono Marco Rossi, ho 25 anni e la mia matricola è 67890.

--- Aggiunta voti ---
Media voti Luana: 28.333333333333332
Media voti Marco: 25.5

--- Attività di studio ---
Luana sta studiando per 3 ore.
Marco sta studiando per 2 ore."


