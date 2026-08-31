import random

# Ciclo while per l'inserimento degli integer
varNmbr = 0
varNmbrs = []
varMax = None
varMin = None
varIdx = 0

# Valorizzazione automatica dell'array
while varIdx < 21:
    varNmbrs.append(int(random.randint(0, 10000)))
    varIdx += 1 

for varNmbr in varNmbrs:
    # Numero più alto
    if varMax is None or varMax < varNmbr:
        varMax = varNmbr
    # Numero più basso
    if varMin is None or varMin > varNmbr:
        varMin = varNmbr     

print("Il numero più alto, rilevato dallo script è: ", varMax)   
print("Il numero più alto, rilevato dalla funzione max è: ", max(varNmbrs)) 
print("Il numero più basso, rilevato dallo script è: ", varMin)   
print("Il numero più basso, rilevato dalla funzione min è: ", min(varNmbrs)) 