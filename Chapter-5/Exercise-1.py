# Ciclo while per l'inserimento degli integer
varCount = 0
varTotal = 0
while True:
    varInpNum = input("Enter a number: ")
    if varInpNum.strip() == 'done':
        break

    try:
        varInpNum = int(varInpNum)
    except ValueError:
        print("Invalid input")
        continue

    varCount += 1    
    varTotal = varTotal + varInpNum

print("Il totale dei numeri inseriti è: ", varTotal)
print("Sono stati inseriti " ,varCount ," numeri")
try:
    print("La media artimetica è pari a: ", (varTotal/varCount))
except ZeroDivisionError:    
    print("La media artimetica risulta un numero indefinito, in quanto dividendo e divisore sono entrambi pari a 0")