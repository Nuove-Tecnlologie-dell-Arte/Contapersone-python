import RPi.GPIO as GPIO
import pygame
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO. setup (26, GPIO.IN)
GPIO. setup (13, GPIO.IN)
contatore = 0
testo = ""
valore= str(contatore)
pygame.init()
black = (0,0,0)
screen = pygame.display.set_mode((1440,900),pygame.FULLSCREEN)#pygame.FULLSCREEN,0, 32
screen.fill((255, 255, 255))
myFont = pygame.font.SysFont("Times New Roman", 40)


while True:
    #If che incrementa
    if GPIO.input(26) or GPIO.input(13):
        contatore= contatore+1
        time.sleep(4)
        valore= str(contatore)
        with open ('testo.json','w') as f:
            f.write(testo)
        print (testo)
        screen.fill((255, 255, 255))
        labelDisplay = myFont.render("Da qui sono passati:" + "Artisti:" + valore,1, black)
        labelcervello = myFont.render("Cervelli:" + valore,1, black)
        labelpensieri = myFont.render("Pensieri:" + valore,1, black)
        labelocchi = myFont.render("Occhi:" + str(contatore*2),1, black)
        labelmon = myFont.render("Modi di vedere il mondo:" + valore,1, black)
        screen.blit(labelDisplay, (350,320))
        screen.blit(labelcervello, (667,360))
        screen.blit(labelpensieri, (667,400))
        screen.blit(labelocchi, (667,440))
        screen.blit(labelmon, (667,480))
        pygame.display.update()
           
    '''if GPIO.input(13):
        contatore= contatore+1
        time.sleep(4)
        valore= str(contatore)
        testo = "{"+ valore + '"artisti":' + "," + valore + '"cervelli":' + ","+ valore + '"pensieri":' + ","+ str(contatore*2)+ '"occhi":'+ "," +valore + '"modi di vedere il mondo":' + "}"
        
        with open ('testo.json','w') as f:
            f.write(testo)
        print (testo)
        screen.blit(testoDisplay, (50,30))
        pygame.display.update()'''
        
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            
            pygame.quit()
            
            quit()
        pygame.display.update()
