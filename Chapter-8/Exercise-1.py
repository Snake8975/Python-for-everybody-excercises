# Dichiaro le funzioni
def chop(listPrm):
    listPrm.pop(0)
    listPrm.pop(-1)

def middle(listPrm):
    rtnListSav = []
    rtnListSav.append(listPrm[0])
    rtnListSav.append(listPrm[-1])
    return rtnListSav

# Ciclo iniziale per l'inserimento dei valori della lista
tInput=[]
tInput1=[]
tInput2=[]

while True:
    if len(tInput)<3:
        varInput = input('Inserisci un valore per la lista (almeno 3): ')
    else:
        varInput = input("Inserisci un valore per la lista o 'exit' per processare i dati: ")

    if varInput=='':
        print("Errore: inserire almeno un valore.")
        continue
    elif varInput.strip().lower()=='exit':
        break
    else:
        tInput.append(varInput) 

tInput1 = tInput.copy()
tInput2 = tInput.copy()

chop(tInput1)
tInput2 = middle(tInput2)

print(tInput1)
print(tInput2)




    