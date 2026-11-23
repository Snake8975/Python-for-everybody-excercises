# Librerie
import os

# Ciclo iniziale per l'inserimento dei valori della lista
tUniqueWords=[]
tListRow=[]
tInput2=[]
varCount = 0

#fhandle=open(os.getcwd()+"\\mbox_export_review_sample.mbox","r")
#fhandle=open(os.getcwd()+"\\mailward-sample.mbox","r")
fhandle=open(os.getcwd()+"\\mailward-sample.mbox","r")

# Ciclo elaborazione file
for row in fhandle:
    if row.startswith("From "):
        row=row.rstrip()
        tListRow=row.split()
        varCount += 1
        print(tListRow[1])


# Stampa lista ordinata
if varCount > 1:    
    print(f"There were {varCount} lines in the file with From as the first word")
elif varCount == 1:
    print(f"There was {varCount} line in the file with From as the first word")
else:
    print(f"There wasn't any line in the file with From as the first word")