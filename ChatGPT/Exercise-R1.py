# Ciclo di recupero e controllo dei parametri di input
while True:
    
    # Ore lavorate
    varOreIn = input("Inserisci le ore lavorate: ")
    try:
        varOre=float(varOreIn)
    except ValueError:
        print("Attenzione: Il valore inserito non è un numero, pertanto non può essere considerate come ore.")
        continue

    if varOre <= 0:
        print("Attenzione: Le ore non possono essere negative.")
        continue    

    break

while True:    
    # Paga oraria
    varValOreIn = input("Inserisci la tariffa oraria: ")
    try:
        varValOre=float(varValOreIn)
    except ValueError:
        print("Attenzione: Il valore inserito non è un numero, pertanto non può essere considerato come una tariffa.")
        continue  

    if varValOre <= 0:
        print("Attenzione: Il valore della tariffa non può essere minore o pari a zero.")
        continue   

    break

# Elaborazione della paga
if varOre <= 40:
    varPaga= varOre * varValOre
else:
    varPaga = (varValOre * 40) + ((varOre-40.0)*(varValOre*1.5))    

# Stampa paga 
print(f"Le verranno accreditati {round(varPaga,2)} €.")


