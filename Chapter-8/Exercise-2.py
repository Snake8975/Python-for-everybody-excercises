# Librerie
import os

# Dichiaro le funzioni
def chkCount(tPrm, tString ):
    if tPrm.count(tString) > 0:
        return 1
    else:
        return 0

# Ciclo iniziale per l'inserimento dei valori della lista
tUniqueWords=[]
tListRow=[]
tInput2=[]

fhandle=open(os.getcwd()+"\\romeo.txt","r")

# Ciclo elaborazione file
for row in fhandle:
    row=row.rstrip()
    tListRow=row.split()

    # Ciclo elaborazione riga
    for tRow in tListRow:
        varWord = tRow
        if chkCount(tUniqueWords, varWord) == 0:
            tUniqueWords.append(varWord)

# Stampa lista ordinata
print(sorted(tUniqueWords))
