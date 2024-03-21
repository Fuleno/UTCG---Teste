from yellow_erza_the_titania import Erza_The_Titania
from card import Card
from tkinter import *
import time

GAME_WIDTH = 1280
GAME_HEIGHT = 720
# -- P1 CARD PLACES
P1A1 = [400,540]
# -- P2 CARD PLACES
P2A1 = [400,180]
# -- UI PLACES
P1A1_ATK = [485,440]

# ------ WINDOW
# window = Tk()
# window.geometry("200x100")
# running = True

Erza = ("Erza","Yellow",130000)
Touka = ("Touka","Yellow",100000)
Zekrom = ("Zekrom","Yellow",90000)
velocidadeErza = 5000
velocidadeTouka = 5500
velocidadeZekrom = 5400
turnSpeed = {}
turnSpeed.update({Erza:velocidadeErza})
turnSpeed.update({Touka:velocidadeTouka})
turnSpeed.update({Zekrom:velocidadeZekrom})
turnSpeedSorted = dict(sorted(turnSpeed.items(), key=lambda x: x[1], reverse=True))
print(turnSpeed)
print()
for key, value in turnSpeedSorted.items():
    print(key[0])
    # em vez desse print, colocar a attack function
    time.sleep(2)
turnSpeed.clear()
print(turnSpeed)

# ------ FINALIZANDO
# window.mainloop()

