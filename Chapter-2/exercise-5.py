# Prompt peraccottaro per l'inserimento dei gradi Celsius

varPromptGradiCelsius = input("Quanti gradi sono oggi fuori casa? ")
varGradiCelsius = float(varPromptGradiCelsius)

# Stampa dei gradi in Celsius, Fahrenheit, Kelvin e Rankine
print("Sono", varGradiCelsius, " gradi Celsius")

varGradiFahrenheit = ((varGradiCelsius*(9/5))+32)
print("Sono" , varGradiFahrenheit, " gradi Fahrenheit")

varGradiKelvin = (varGradiCelsius+273.15)
print("Sono", varGradiKelvin, " gradi Kelvin")

varGradiRankine = ((varGradiCelsius+273.15)*(9/5))
print("Sono", varGradiRankine, " gradi Rankine")

print("Grazie per aver utilizzato il convertitore di gradi Celsius in Fahrenheit, Kelvin e Rankine!\n" "Il novizio in Python vi saluta e vi augura una buona giornata!")