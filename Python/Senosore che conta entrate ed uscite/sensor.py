import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.IN) 
GPIO.setup(13, GPIO.IN)
GPIO.setup(6, GPIO.OUT)
contatore = 0
acceso = True
acceso2 = True
testo = ""
valore = str(contatore)

while True:

    #Sensore Entrata

    if GPIO.input(26) and (GPIO.input(13) == False) and acceso == True:
        acceso2 = False
        contatore = contatore + 1 
        time.sleep(4)
        testo = "{" + '"artisti":' + valore + "," + '"occhi":' + str(contatore*2) + "}" #continuare in base al numero di elementi da scrivere nel .JSON
        with open("testo.json", "w") as f:
            f.write(testo)
        acceso2 = True
    
    #Sensore Uscita
    
    if GPIO.input(13) and (GPIO.input(26) == False) and acceso2 == True:
        acceso = False
        #Controllo in caso il contatore cercasse di segnare un un numero minore di zero
        if (contatore <= 0):
            contatore = 0
        else:
            contatore = contatore - 1 
        time.sleep(4)
        testo = "{" + '"artisti":' + valore + "," + '"occhi":' + str(contatore*2) + "}" #continuare in base al numero di elementi da scrivere nel .JSON
        with open("testo.json", "w") as f:
            f.write(testo)
        acceso = True
