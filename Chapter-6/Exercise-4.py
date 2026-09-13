# definisco la variabile su cu operare
varStr = 'X-DSPAM-Confidence: 0.8475'
varIdxBegin = varStr.find(':')
varIdxEnd = len(varStr)
varNumStr = varStr[varIdxBegin+1:varIdxEnd].strip()
print("Il numero estratto e convertito è: ", float(varNumStr))
# Stampo il conteggio dei caratteri
#print("Il carattere è apparso ",countChar(varString, varStringChk)," volte.")