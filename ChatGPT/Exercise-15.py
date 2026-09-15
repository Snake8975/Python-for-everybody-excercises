# Recupero la stringa principale
while True:

    # Controllo che sia inserito qualcosa
    varUserName = input("Inserisci lo Username: ")
    if len(varUserName.strip()) == 0:
        print("E' obbligatorio inserire un valore.")
        continue

    # Controllo che la lunghezza non sia inferiore a 5 caratteri    
    if len(varUserName.strip()) < 5:
        print("La lunghezza dello Username dev'essere di almeno 5 caratteri.")
        continue

    # Controllo che lo username non sia o abbia la parola 'admin'
    if "admin" in varUserName.strip().lower():
        print("Lo Username non può essere o contenere la parola 'admin'.")
        continue

    break    

# Stampo lo username corretto
print("Username: ", varUserName.strip().lower())