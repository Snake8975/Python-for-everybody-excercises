varRiga = "X-DSPAM-Confidence:    0.8475"
varFloat = float(varRiga[varRiga.find(':') + 1:].strip())
print("Il valore float estratto dalla stringa è:", varFloat)
