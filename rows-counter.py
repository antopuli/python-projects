
# TESTO A CUI CONTARE LE RIGHE
text = """Nel mezzo del cammin di nostra vita
mi ritrovai per una selva oscura, 
che la diritta via era smarrita. 

Ahi quanto a dir qual era è cosa dura, 
esta selva selvaggia e aspra e forte, 
che nel pensier rinnova la parola."""

# DEFINISCO LE STRUTTURE DATI DI SUPPORTO
tList = list(text)
rows = []
supporingList = ''

# NAVIGO ALL'INTERNO DELLE LETTERE DEL TESTO
# ED INSERISCO ALL'INTERNO DI UNA LISTA LE RIGHE
for i in range(len(tList)):
    if tList[i] == '\n' or i == (len(tList)-1):
        rows.append(list(supporingList))
        supporingList = ''
    else:
        supporingList += tList[i]

# RIMUOVO DALLA LISTA LE SUB-LISTE VUOTE, OVVERO LE
# RIGHE PRIVE DI TESTO
for i in range(rows.count([])): rows.remove([])

# STAMPO A SCHERMO IL RISULTATO DEL PROGRAMMA
print(f'Il testo contiene {len(rows)} righe.')