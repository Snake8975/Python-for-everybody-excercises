import sys

# Variabile input per parsing
varLog = "USER=marco;ACTION=login;STATUS=success"

# Controllo se sono presenti tutti i parametri
if "USER=" not in (varLog):
    print("Attenzione: Manca il parametro USER")
    quit()

if "ACTION=" not in (varLog):
    print("Attenzione: Manca il parametro ACTION")
    quit()

if "STATUS=" not in (varLog):
    print("Attenzione: Manca il parametro STATUS")
    quit()

# Estraggo i parametri
USERpos = varLog.find('USER=')
ACTIONpos = varLog.find('ACTION=')
STATUSpos = varLog.find('STATUS=')

USERvalue = varLog[USERpos+5:ACTIONpos-1]
if USERvalue.strip() == '':
    print("Attenzione: Non è stato inserito alcun valore per USER")
    quit()

ACTIONvalue = varLog[ACTIONpos+7:STATUSpos-1]
if ACTIONvalue.strip() == '':
    print("Attenzione: Non è stato inserito alcun valore per ACTION")
    quit()

STATUSvalue = varLog[STATUSpos+7:len(varLog)]
if STATUSvalue.strip() == '':
    print("Attenzione: Non è stato inserito alcun valore per STATUS")
    quit()        


# Stampo l'output
print(f'Utente {USERvalue} ha eseguito {ACTIONvalue} con esito {STATUSvalue}')