# Definisco il ciclo di lettura della temperatura della macchina, fino a quando non viene inserita la paola FINE
while True:
   varInpTemp = input("Inserisci temperatura: ")

   # Esco per FINE
   if varInpTemp == "FINE":
      print("Acquisizione terminata.")
      break

   # Controllo che il valore inserito sia un numero   
   try:
    varInpTemp = float(varInpTemp)
   except ValueError:
      print("Valore non valido.")
      continue

   if varInpTemp < 0:
      continue

   # Stampo la temperatura inserita, se il valore è corretto
   print("Rilevazione accettata: ", varInpTemp, "°")

