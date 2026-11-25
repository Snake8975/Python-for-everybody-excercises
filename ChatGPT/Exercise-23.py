# Inserimento delle liste di base
tgiorni = ["Lunedì", "Martedì", "Mercoledì", "Giovedì", "Venerdì", "Sabato", "Domenica"]
tvendite = [125.50, 98.00, 154.75, 87.30, 210.00, 325.40, 175.20]
vCount = 0
vCountOver150=0
tIncomeOver150=[]

# Ciclo stampa incassi per giorno
for vgiorno in tgiorni:
    print(f"Il giorno {tgiorni[vCount]}, sono stati incassati: {tvendite[vCount]}")
    
    if tvendite[vCount]>150:
        vCountOver150+=1
        tIncomeOver150.append(tvendite[vCount])
    vCount += 1

# Stampa dei totali
print(f"\nL'incasso complessivo della settimana è pari a: {round(sum(tvendite),2)} €")
print(f"\nL'incasso medio giornaliero è pari a: {round(sum(tvendite)/7,2)} €")
print(f"\nIl giorno con l'incasso più alto è {tgiorni[tvendite.index(max(tvendite))]} pari a: {max(tvendite)} €")
print(f"\nIl giorno con l'incasso più basso è {tgiorni[tvendite.index(min(tvendite))]} pari a: {min(tvendite)} €")
print(f"\nGiorni con incasso superiore a 150 €: {vCountOver150}")
print("\nVendite superiori a 150 €:")

# Stampa incassi sopra i 150 €
for vInvocomeOver150 in tIncomeOver150:
    print(f"{vInvocomeOver150} €")

# Ciclo aumento del 10%
print("\nVendite dopo aumento del 10%:")
vCount = 0
for vIncasso in tvendite:
    vIncasso = vIncasso * 1.10
    tvendite[vCount] = vIncasso
    print(f"{round(vIncasso,2)} €")
    vCount+=1
    