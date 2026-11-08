# Funzioni
def funzioneControlloLog(varLog):

    varListLog = varLog.split('|') 

    # Ricavo data e ora
    varDataOra = varListLog[0].strip().split()
    varData = varDataOra[0]
    varOra = varDataOra[1] 

    # Ricavo il livello di log
    varLivelloLog = varListLog[1].strip()

    # Ricavo l'utente
    varUtente = varListLog[2].strip().split('=')[1]

    # Ricavo l'azione
    varAzione = varListLog[3].strip().split('=')[1]

    # Ricavo il tempo di esecuzione
    varTempoEsecuzione = varListLog[4].strip().split('=')[1]
    varTempoEsecuzione = float(varTempoEsecuzione)

    # Ricavo lo stato operazione
    if varTempoEsecuzione <= 0.5:
        varStatoOperazione = 'NORMALE'
    else:
        varStatoOperazione = 'LENTA'

    # Stampo i risultati
    print('Data:', varData)
    print('Ora:', varOra)
    print('Livello:', varLivelloLog)
    print('Utente:', varUtente)
    print('Azione:', varAzione)
    print(f'Tempo di esecuzione: {varTempoEsecuzione} secondi')
    print('Stato operazione:', varStatoOperazione)
    return


funzioneControlloLog('2026-11-08 14:32:10 | INFO | USER=marco | ACTION=LOGIN | TIME=0.245')
funzioneControlloLog('2026-11-08 15:45:22 | WARN | USER=anna | ACTION=UPLOAD | TIME=1.875')
funzioneControlloLog('2026-11-08 16:12:05 | ERROR | USER=luca | ACTION=DELETE | TIME=0.63')
funzioneControlloLog("2026-11-08  14:32:10  |  INFO  | USER=marco  |  ACTION=LOGIN | TIME=0.245 ")


  
