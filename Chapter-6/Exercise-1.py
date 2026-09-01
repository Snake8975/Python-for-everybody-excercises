# Recupero la stringa da stampare
varString = input("Inserisci la stringa da stampare: ")
varString = varString
varLenStr = int(len(varString))
varLenStrNeg = varLenStr * -1
varIdx = -1

# Test 1 - Stampa caratteri al contrario con while
print("Test con while")
while varIdx >= varLenStrNeg:
    print(varString[varIdx])
    varIdx -= 1

print("Test con for")
for varIdx in range(varLenStr - 1, -1, -1):
    print(varString[varIdx])




