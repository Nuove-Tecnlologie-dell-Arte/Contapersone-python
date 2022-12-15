#Import delle librerie
import RPi.GPIO as GPIO
import pygame
import time

#Inizializzazione delle funzioni
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO. setup (26, GPIO.IN)
GPIO. setup (13, GPIO.IN)
pygame.init()
black = (0,0,0)
screen = pygame.display.set_mode((1440,900),pygame.FULLSCREEN)
screen.fill((255, 255, 255))
setcaratteri = pygame.font.SysFont("Times New Roman", 40)

#Dichiarazione Variabili
contatore = 0
testo = ""
valore= str(contatore)

#Inizio Ciclo per la lettura
while True:

    #Condizione
    if GPIO.input(26) or GPIO.input(13):

        contatore= contatore+1 #Incremento del contatore
        time.sleep(4) #Sospensione
        valore= str(contatore) #Funzione di conversione del valore
        screen.fill((255, 255, 255)) #Comparasa Schermo

        #Dichiarazioni delle funzioni con il testo da far comparire a schermo
        label_display = setcaratteri.render("Da qui sono passati:" + "Artisti:" + valore,1, black)
        label_cervello = setcaratteri.render("Cervelli:" + valore,1, black)
        label_pensieri = setcaratteri.render("Pensieri:" + valore,1, black)
        label_occhi = setcaratteri.render("Occhi:" + str(contatore*2),1, black)
        label_mon = setcaratteri.render("Modi di vedere il mondo:" + valore,1, black)

        #Funzioni di comparsa del testo
        screen.blit(label_display, (350,320))
        screen.blit(label_cervello, (667,360))
        screen.blit(label_pensieri, (667,400))
        screen.blit(label_occhi, (667,440))
        screen.blit(label_mon, (667,480))
        pygame.display.update()
        
    #Controllo per verificare che gli eventi non siano eventi di chiusura
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        pygame.display.update()
