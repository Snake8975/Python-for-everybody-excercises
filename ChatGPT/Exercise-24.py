# Librerie
import os

# Importazione degli ordini
fhandle=open(os.getcwd()+"\\order_exsercise_24.txt","r")

# PARTE 1: Stampa dettagli ordini
# Salvo le righe ordine
tRigheOrdine=[]
tRigaOrdine=[]
vCountOrdine=0
vCountOrdOver500=0
vTotaleOrdine=0
vOrderMax = None
for righe in fhandle:
    tRigheOrdine.append(righe)
    tRigaOrdine=righe.split(";")

    # Stampo i dettagli dell'ordine
    print(f"Ordine: {tRigaOrdine[0]}")
    print(f"Cliente: {tRigaOrdine[1]}")
    print(f"Prodotto: {tRigaOrdine[2]}")
    vQta = int(tRigaOrdine[3])
    vPrezzo = float(tRigaOrdine[4])
    print(f"Quantità: {vQta}")
    print(f"Prezzo unitario: {vPrezzo} €")
    print(f"Totale ordine: {round(vQta*vPrezzo,2)} €\n")

    # Campi totali e massimi
    vCountOrdine += 1
    vTotaleOrdine = vTotaleOrdine + (vQta*vPrezzo)
    if vOrderMax is None or (vQta*vPrezzo) > vOrderMax:
        vOrderMax = (vQta*vPrezzo)
        vCodOrderMax = tRigaOrdine[0]
        vClienteOrderMax = tRigaOrdine[1]

    if (vQta*vPrezzo) > 500:
        vCountOrdOver500 +=1

# PARTE 2: Stampa totali ordini
print(f"Numero di ordini: {vCountOrdine}")
print(f"\nTotale ordini: {vTotaleOrdine} €")
print(f"\nValore merdio ordini: {round(vTotaleOrdine/vCountOrdine,2)} €")
print(f"\nl'ordine {vCodOrderMax} del cliente {vClienteOrderMax} pari a {vOrderMax}€, è l'ordine con il valore più alto.")
print(f"\nNumero ordini sopra i 500€: {vCountOrdOver500}")

# PARTE 3: Ordini importanti
# Salvo le righe ordine
tordini_importanti=[]
print("\nQuesti sono gli ordini più importanti:")
for righe in tRigheOrdine:
    tRigaOrdine=righe.split(";")
    vQta = int(tRigaOrdine[3])
    vPrezzo = float(tRigaOrdine[4])

    if (vQta*vPrezzo) > 500:
        tordini_importanti.append(tRigaOrdine[0])
        print(tRigaOrdine[0])     

# PARTE BONUS: Ricerca del cliente
while True:
    varUser=input("\nInserisci il cliente che vuoi ricercare: ")
    varUser = varUser.strip()
    if varUser =='':
        print("Errore: devi inserire il cliente")
        continue
    break

varCount = 0
for righe in tRigheOrdine:
    varRow = righe
    tRigaOrdine=righe.split(";")
    if varUser.lower() == tRigaOrdine[1].lower().strip():
        print(f"{tRigaOrdine[0]} - {tRigaOrdine[2]}")
        varCount += 1

if varCount == 0:
    print("Non è stato trovato alcun ordine per il cliente inserito")

