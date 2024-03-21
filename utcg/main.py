from tkinter import *
import time
from yellow_erza_the_titania import Erza_The_Titania
from yellow_touka_lightning_cutter import Touka_Lightning_Cutter
from yellow_todoroki_my_own_power import Todoroki_My_Own_Power
from yellow_pokemon_zekrom_dragon_of_the_unova_myth import Zekrom_Dragon_Of_The_Unova_Myth

GAME_WIDTH = 1280
GAME_HEIGHT = 720
# -- P1 CARD PLACES
P1A1 = [400,540]
P1A2 = [640,540]
P1A3 = [880,540]
# -- P2 CARD PLACES
P2A1 = [400,180]
P2A2 = [640,180]
P2A3 = [880,180]
# -- P1 e P2 CONFIRM
p1confirm = False
p2confirm = False
# -- P1 e P2 ATTACKS
# - P1
p1a1move = [0,0,0] # move [1, 2, 3] // 0 = deselecionado, 1 = selecionado
p1a2move = [0,0,0]
p1a3move = [0,0,0]
# - P2
p2a1move = [0,0,0]
p2a2move = [0,0,0]
p2a3move = [0,0,0]
# - GERAL
move = [p1a1move,p1a2move,p1a3move,p2a1move,p2a2move,p2a3move]
turnSpeed = {}
turn = 0
# - SWITCHERS
p1a1switching = False
p1a2switching = False
p1a3switching = False
p2a1switching = False
p2a2switching = False
p2a3switching = False
# - IMAGENS
p1a1_image = "images/None.png"
p1a2_image = "images/None.png"
p1a3_image = "images/None.png"
p2a1_image = "images/None.png"
p2a2_image = "images/None.png"
p2a3_image = "images/None.png"
# -- STAT TEXTS
# - P1
p1a1_hptext = "STAT"
p1a1_atktext = "STAT"
p1a1_spetext = "STAT"
p1a2_hptext = "STAT"
p1a2_atktext = "STAT"
p1a2_spetext = "STAT"
p1a3_hptext = "STAT"
p1a3_atktext = "STAT"
p1a3_spetext = "STAT"
# - P2
p2a1_hptext = "STAT"
p2a1_atktext = "STAT"
p2a1_spetext = "STAT"
p2a2_hptext = "STAT"
p2a2_atktext = "STAT"
p2a2_spetext = "STAT"
p2a3_hptext = "STAT"
p2a3_atktext = "STAT"
p2a3_spetext = "STAT"

def p1switch(button_press):
    global cardat_p1a1
    global cardat_p1a2
    global cardat_p1a3
    global p1a1switching
    global p1a2switching
    global p1a3switching

    match button_press:
        case "p1a1switch":
            p1a1switching = True
            p1a1atk1.config(state=DISABLED)
            p1a1atk2.config(state=DISABLED)
            p1a1ult.config(state=DISABLED)
            p1a1switch.config(state=DISABLED)
        case "p1a2switch":
            p1a2switching = True
            p1a2atk1.config(state=DISABLED)
            p1a2atk2.config(state=DISABLED)
            p1a2ult.config(state=DISABLED)
            p1a2switch.config(state=DISABLED)
        case "p1a3switch":
            p1a3switching = True
            p1a3atk1.config(state=DISABLED)
            p1a3atk2.config(state=DISABLED)
            p1a3ult.config(state=DISABLED)
            p1a3switch.config(state=DISABLED)
    if p1a1switching is True:
        if p1a2switching is True:
            p1a3switch.config(state=DISABLED)
        if p1a3switching is True:
            p1a2switch.config(state=DISABLED)
    if p1a2switching is True:
        if p1a3switching is True:
            p1a1switch.config(state=DISABLED)
def p2switch(button_press):
    global cardat_p2a1
    global cardat_p2a2
    global cardat_p2a3
    global p2a1switching
    global p2a2switching
    global p2a3switching

    match button_press:
        case "p2a1switch":
            p2a1switching = True
            p2a1atk1.config(state=DISABLED)
            p2a1atk2.config(state=DISABLED)
            p2a1ult.config(state=DISABLED)
            p2a1switch.config(state=DISABLED)
        case "p2a2switch":
            p2a2switching = True
            p2a2atk1.config(state=DISABLED)
            p2a2atk2.config(state=DISABLED)
            p2a2ult.config(state=DISABLED)
            p2a2switch.config(state=DISABLED)
        case "p2a3switch":
            p2a3switching = True
            p2a3atk1.config(state=DISABLED)
            p2a3atk2.config(state=DISABLED)
            p2a3ult.config(state=DISABLED)
            p2a3switch.config(state=DISABLED)
    if p2a1switching is True:
        if p2a2switching is True:
            p2a3switch.config(state=DISABLED)
        if p2a3switching is True:
            p2a2switch.config(state=DISABLED)
    if p2a2switching is True:
        if p2a3switching is True:
            p2a1switch.config(state=DISABLED)
def confirmfunc(button_press):
    global cardat_p1a1
    global cardat_p1a2
    global cardat_p1a3
    global cardat_p2a1
    global cardat_p2a2
    global cardat_p2a3
    global turn
    global turn_label
    global isAttacking
    global turnSpeed
    global p1confirm
    global p2confirm
    global p1a1switching
    global p1a2switching
    global p1a3switching
    global p2a1switching
    global p2a2switching
    global p2a3switching

    match button_press:
        case "p1confirm":
            p1confirm = True
            p1confirm_button.config(state=DISABLED)
            p1movebuttons_disable()
        case "p2confirm":
            p2confirm = True
            p2confirm_button.config(state=DISABLED)
            p2movebuttons_disable()
    if p1confirm is True and p2confirm is True:
        # ---- P1 SWITCH
        if p1a1switching is True:
            if p1a2switching is True:
                cardat_p1a1, cardat_p1a2 = cardat_p1a2, cardat_p1a1
                p1a1switching, p1a2switching = False, False
            if p1a3switching is True:
                cardat_p1a1, cardat_p1a3 = cardat_p1a3, cardat_p1a1
                p1a1switching, p1a3switching = False, False
        if p1a2switching is True:
            if p1a3switching is True:
                cardat_p1a2, cardat_p1a3 = cardat_p1a3, cardat_p1a2
                p1a2switching, p1a3switching = False, False
        # ---- P2 SWITCH
        if p2a1switching is True:
            if p2a2switching is True:
                cardat_p2a1, cardat_p2a2 = cardat_p2a2, cardat_p2a1
                p2a1switching, p2a2switching = False, False

            if p2a3switching is True:
                cardat_p2a1, cardat_p2a3 = cardat_p2a3, cardat_p2a1
                p2a1switching, p2a3switching = False, False
        if p2a2switching is True:
            if p2a3switching is True:
                cardat_p2a2, cardat_p2a3 = cardat_p2a3, cardat_p2a2
                p2a2switching, p2a3switching = False, False

        statUpdate()
        imgUpdate()
        # -- p1a1
        match p1a1move[0]:
            case 1:
                p1a1turntuple = (cardat_p1a1, cardat_p1a1.move1_variables,
                                 cardat_p2a1, cardat_p2a2, cardat_p2a3,
                                 cardat_p1a2, cardat_p1a3)
                turnSpeed.update({p1a1turntuple:cardat_p1a1.card_spe})
                p1a1move[0] = 0
        match p1a1move[1]:
            case 1:
                p1a1turntuple = (cardat_p1a1, cardat_p1a1.move2_variables,
                                 cardat_p2a1, cardat_p2a2, cardat_p2a3,
                                 cardat_p1a2, cardat_p1a3)
                turnSpeed.update({p1a1turntuple: cardat_p1a1.card_spe})
                p1a1move[1] = 0
        match p1a1move[2]:
            case 1:
                p1a1turntuple = (cardat_p1a1, cardat_p1a1.move3_variables,
                                 cardat_p2a1, cardat_p2a2, cardat_p2a3,
                                 cardat_p1a2, cardat_p1a3)
                turnSpeed.update({p1a1turntuple: cardat_p1a1.card_spe})
                p1a1move[2] = 0
        # -- p1a2
        match p1a2move[0]:
            case 1:
                p1a2turntuple = (cardat_p1a2, cardat_p1a2.move1_variables,
                                 cardat_p2a2, cardat_p2a1, cardat_p2a3,
                                 cardat_p1a1, cardat_p1a3)
                turnSpeed.update({p1a2turntuple: cardat_p1a2.card_spe})
                p1a2move[0] = 0
        match p1a2move[1]:
            case 1:
                p1a2turntuple = (cardat_p1a2, cardat_p1a2.move2_variables,
                                 cardat_p2a2, cardat_p2a1, cardat_p2a3,
                                 cardat_p1a1, cardat_p1a3)
                turnSpeed.update({p1a2turntuple: cardat_p1a2.card_spe})
                p1a2move[1] = 0
        match p1a2move[2]:
            case 1:
                p1a2turntuple = (cardat_p1a2, cardat_p1a2.move3_variables,
                                 cardat_p2a2, cardat_p2a1, cardat_p2a3,
                                 cardat_p1a1, cardat_p1a3)
                turnSpeed.update({p1a2turntuple: cardat_p1a2.card_spe})
                p1a2move[2] = 0
        # -- p1a3
        match p1a3move[0]:
            case 1:
                p1a3turntuple = (cardat_p1a3, cardat_p1a3.move1_variables,
                                 cardat_p2a3, cardat_p2a1, cardat_p2a2,
                                 cardat_p1a1, cardat_p1a2)
                turnSpeed.update({p1a3turntuple: cardat_p1a3.card_spe})
                p1a3move[0] = 0
        match p1a3move[1]:
            case 1:
                p1a3turntuple = (cardat_p1a3, cardat_p1a3.move2_variables,
                                 cardat_p2a3, cardat_p2a1, cardat_p2a2,
                                 cardat_p1a1, cardat_p1a2)
                turnSpeed.update({p1a3turntuple: cardat_p1a3.card_spe})
                p1a3move[1] = 0
        match p1a3move[2]:
            case 1:
                p1a3turntuple = (cardat_p1a3, cardat_p1a3.move3_variables,
                                 cardat_p2a3, cardat_p2a1, cardat_p2a2,
                                 cardat_p1a1, cardat_p1a2)
                turnSpeed.update({p1a3turntuple: cardat_p1a3.card_spe})
                p1a3move[2] = 0
        # -- p2a1
        match p2a1move[0]:
            case 1:
                p2a1turntuple = (cardat_p2a1, cardat_p2a1.move1_variables,
                                 cardat_p1a1, cardat_p1a2, cardat_p1a3,
                                 cardat_p2a2, cardat_p2a3)
                turnSpeed.update({p2a1turntuple: cardat_p2a1.card_spe})
                p2a1move[0] = 0
        match p2a1move[1]:
            case 1:
                p2a1turntuple = (cardat_p2a1, cardat_p2a1.move2_variables,
                                 cardat_p1a1, cardat_p1a2, cardat_p1a3,
                                 cardat_p2a2, cardat_p2a3)
                turnSpeed.update({p2a1turntuple: cardat_p2a1.card_spe})
                p2a1move[1] = 0
        match p2a1move[2]:
            case 1:
                p2a1turntuple = (cardat_p2a1, cardat_p2a1.move3_variables,
                                 cardat_p1a1, cardat_p1a2, cardat_p1a3,
                                 cardat_p2a2, cardat_p2a3)
                turnSpeed.update({p2a1turntuple: cardat_p2a1.card_spe})
                p2a1move[2] = 0
        # -- p2a2
        match p2a2move[0]:
            case 1:
                p2a2turntuple = (cardat_p2a2, cardat_p2a2.move1_variables,
                                 cardat_p1a2, cardat_p1a1, cardat_p1a3,
                                 cardat_p2a1, cardat_p2a3)
                turnSpeed.update({p2a2turntuple: cardat_p2a2.card_spe})
                p2a2move[0] = 0
        match p2a2move[1]:
            case 1:
                p2a2turntuple = (cardat_p2a2, cardat_p2a2.move2_variables,
                                 cardat_p1a2, cardat_p1a1, cardat_p1a3,
                                 cardat_p2a1, cardat_p2a3)
                turnSpeed.update({p2a2turntuple: cardat_p2a2.card_spe})
                p2a2move[1] = 0
        match p2a2move[2]:
            case 1:
                p2a2turntuple = (cardat_p2a2, cardat_p2a2.move3_variables,
                                 cardat_p1a2, cardat_p1a1, cardat_p1a3,
                                 cardat_p2a1, cardat_p2a3)
                turnSpeed.update({p2a2turntuple: cardat_p2a2.card_spe})
                p2a2move[2] = 0
        # -- p2a3
        match p2a3move[0]:
            case 1:
                p2a3turntuple = (cardat_p2a3, cardat_p2a3.move1_variables,
                                 cardat_p1a3, cardat_p1a1, cardat_p1a2,
                                 cardat_p2a1, cardat_p2a2)
                turnSpeed.update({p2a3turntuple: cardat_p2a3.card_spe})
                p2a3move[0] = 0
        match p2a3move[1]:
            case 1:
                p2a3turntuple = (cardat_p2a3, cardat_p2a3.move2_variables,
                                 cardat_p1a3, cardat_p1a1, cardat_p1a2,
                                 cardat_p2a1, cardat_p2a2)
                turnSpeed.update({p2a3turntuple: cardat_p2a3.card_spe})
                p2a3move[1] = 0
        match p2a3move[2]:
            case 1:
                p2a3turntuple = (cardat_p2a3, cardat_p2a3.move3_variables,
                                 cardat_p1a3, cardat_p1a1, cardat_p1a2,
                                 cardat_p2a1, cardat_p2a2)
                turnSpeed.update({p2a3turntuple: cardat_p2a3.card_spe})
                p2a3move[2] = 0

        # -- ataques e sistema de velocidade
        turnspeedsorted = dict(sorted(turnSpeed.items(), key=lambda x: x[1], reverse=True))
        for key, value in turnspeedsorted.items():
            if key[0].card_isAlive is True:
                attack_function(*key)
                time.sleep(2)
        turnspeedsorted.clear()
        turnSpeed.clear()
        isAttacking = "No one"
        moveLabelUpdate()

        p1confirm = False
        p2confirm = False
        p1confirm_button.config(state=ACTIVE)
        p2confirm_button.config(state=ACTIVE)
        p1movebuttons_enable()
        p2movebuttons_enable()
        turn += 1
        turn_label.config(text="Turn: " + str(turn))
def send_attack(button_press):
    global p1a1move
    global p1a2move
    global p1a3move
    global p2a1move
    global p2a2move
    global p2a3move

    match button_press:
        # -- p1a1 atk 1 - 3
        case "p1a1atk1":
            p1a1move[0] = 1
            p1a1atk1.config(state=DISABLED)
            p1a1atk2.config(state=DISABLED)
            p1a1ult.config(state=DISABLED)
            p1a1switch.config(state=DISABLED)
        case "p1a1atk2":
            p1a1move[1] = 1
            p1a1atk1.config(state=DISABLED)
            p1a1atk2.config(state=DISABLED)
            p1a1ult.config(state=DISABLED)
            p1a1switch.config(state=DISABLED)
        case "p1a1atk3":
            p1a1move[2] = 1
            p1a1atk1.config(state=DISABLED)
            p1a1atk2.config(state=DISABLED)
            p1a1ult.config(state=DISABLED)
            p1a1switch.config(state=DISABLED)
        # -- p1a2 atk 1 - 3
        case "p1a2atk1":
            p1a2move[0] = 1
            p1a2atk1.config(state=DISABLED)
            p1a2atk2.config(state=DISABLED)
            p1a2ult.config(state=DISABLED)
            p1a2switch.config(state=DISABLED)
        case "p1a2atk2":
            p1a2move[1] = 1
            p1a2atk1.config(state=DISABLED)
            p1a2atk2.config(state=DISABLED)
            p1a2ult.config(state=DISABLED)
            p1a2switch.config(state=DISABLED)
        case "p1a2atk3":
            p1a2move[2] = 1
            p1a2atk1.config(state=DISABLED)
            p1a2atk2.config(state=DISABLED)
            p1a2ult.config(state=DISABLED)
            p1a2switch.config(state=DISABLED)
        # -- p1a3 atk 1 - 3
        case "p1a3atk1":
            p1a3move[0] = 1
            p1a3atk1.config(state=DISABLED)
            p1a3atk2.config(state=DISABLED)
            p1a3ult.config(state=DISABLED)
            p1a3switch.config(state=DISABLED)
        case "p1a3atk2":
            p1a3move[1] = 1
            p1a3atk1.config(state=DISABLED)
            p1a3atk2.config(state=DISABLED)
            p1a3ult.config(state=DISABLED)
            p1a3switch.config(state=DISABLED)
        case "p1a3atk3":
            p1a3move[2] = 1
            p1a3atk1.config(state=DISABLED)
            p1a3atk2.config(state=DISABLED)
            p1a3ult.config(state=DISABLED)
            p1a3switch.config(state=DISABLED)
        # -- p2a1 atk 1 e- 3
        case "p2a1atk1":
            p2a1move[0] = 1
            p2a1atk1.config(state=DISABLED)
            p2a1atk2.config(state=DISABLED)
            p2a1ult.config(state=DISABLED)
            p2a1switch.config(state=DISABLED)
        case "p2a1atk2":
            p2a1move[1] = 1
            p2a1atk1.config(state=DISABLED)
            p2a1atk2.config(state=DISABLED)
            p2a1ult.config(state=DISABLED)
            p2a1switch.config(state=DISABLED)
        case "p2a1atk3":
            p2a1move[2] = 1
            p2a1atk1.config(state=DISABLED)
            p2a1atk2.config(state=DISABLED)
            p2a1ult.config(state=DISABLED)
            p2a1switch.config(state=DISABLED)
        # -- p2a2 atk 1 - 3
        case "p2a2atk1":
            p2a2move[0] = 1
            p2a2atk1.config(state=DISABLED)
            p2a2atk2.config(state=DISABLED)
            p2a2ult.config(state=DISABLED)
            p2a2switch.config(state=DISABLED)
        case "p2a2atk2":
            p2a2move[1] = 1
            p2a2atk1.config(state=DISABLED)
            p2a2atk2.config(state=DISABLED)
            p2a2ult.config(state=DISABLED)
            p2a2switch.config(state=DISABLED)
        case "p2a2atk3":
            p2a2move[2] = 1
            p2a2atk1.config(state=DISABLED)
            p2a2atk2.config(state=DISABLED)
            p2a2ult.config(state=DISABLED)
            p2a2switch.config(state=DISABLED)
        # -- p2a3 atk 1 - 3
        case "p2a3atk1":
            p2a3move[0] = 1
            p2a3atk1.config(state=DISABLED)
            p2a3atk2.config(state=DISABLED)
            p2a3ult.config(state=DISABLED)
            p2a3switch.config(state=DISABLED)
        case "p2a3atk2":
            p2a3move[1] = 1
            p2a3atk1.config(state=DISABLED)
            p2a3atk2.config(state=DISABLED)
            p2a3ult.config(state=DISABLED)
            p2a3switch.config(state=DISABLED)
        case "p2a3atk3":
            p2a3move[2] = 1
            p2a3atk1.config(state=DISABLED)
            p2a3atk2.config(state=DISABLED)
            p2a3ult.config(state=DISABLED)
            p2a3switch.config(state=DISABLED)
def attack_function(card,move,frontenemy,enemy2,enemy3,team1,team2):
    global turn
    global isAttacking
    global attacking_label
    possiblecards = (card, frontenemy, enemy2, enemy3, team1, team2)
    isAttacking = card.card_displayName
    moveLabelUpdate()
    card.doMove(card,move,frontenemy,enemy2,enemy3,team1,team2,turn)
    for i in possiblecards:
        if i.card_hp <= 0:
            i.card_isAlive = False

    statUpdate()
    # - problema: hp não atualiza durante os ataques saindo
    # canva e window update não estão funcionando,
    # ao que parece
def cancel(button_press):
    global p1a1move
    global p1a2move
    global p1a3move
    global p2a1move
    global p2a2move
    global p2a3move
    global p1a1switching
    global p1a2switching
    global p1a3switching
    global p2a1switching
    global p2a2switching
    global p2a3switching

    match button_press:
        case "p1cancel":
            p1a1switching, p1a2switching, p1a3switching = False, False, False
            p1movebuttons_enable()
            p1a1move = [0, 0, 0]
            p1a2move = [0, 0, 0]
            p1a3move = [0, 0, 0]
            p1confirm_button.config(state=ACTIVE)
        case "p2cancel":
            p2a1switching, p2a2switching, p2a3switching = False, False, False
            p2movebuttons_enable()
            p2a1move = [0, 0, 0]
            p2a2move = [0, 0, 0]
            p2a3move = [0, 0, 0]
            p2confirm_button.config(state=ACTIVE)
def p1movebuttons_enable():
    # - p1a1
    p1a1atk1.config(state=ACTIVE)
    p1a1atk2.config(state=ACTIVE)
    p1a1ult.config(state=ACTIVE)
    p1a1switch.config(state=ACTIVE)
    # - p1a2
    p1a2atk1.config(state=ACTIVE)
    p1a2atk2.config(state=ACTIVE)
    p1a2ult.config(state=ACTIVE)
    p1a2switch.config(state=ACTIVE)
    # - p1a3
    p1a3atk1.config(state=ACTIVE)
    p1a3atk2.config(state=ACTIVE)
    p1a3ult.config(state=ACTIVE)
    p1a3switch.config(state=ACTIVE)
def p1movebuttons_disable():
    # -- p1a1
    p1a1atk1.config(state=DISABLED)
    p1a1atk2.config(state=DISABLED)
    p1a1ult.config(state=DISABLED)
    p1a1switch.config(state=DISABLED)
    # -- p1a2
    p1a2atk1.config(state=DISABLED)
    p1a2atk2.config(state=DISABLED)
    p1a2ult.config(state=DISABLED)
    p1a2switch.config(state=DISABLED)
    # -- p1a3
    p1a3atk1.config(state=DISABLED)
    p1a3atk2.config(state=DISABLED)
    p1a3ult.config(state=DISABLED)
    p1a3switch.config(state=DISABLED)
def p2movebuttons_enable():
    # - p2a1
    p2a1atk1.config(state=ACTIVE)
    p2a1atk2.config(state=ACTIVE)
    p2a1ult.config(state=ACTIVE)
    p2a1switch.config(state=ACTIVE)
    # - p2a2
    p2a2atk1.config(state=ACTIVE)
    p2a2atk2.config(state=ACTIVE)
    p2a2ult.config(state=ACTIVE)
    p2a2switch.config(state=ACTIVE)
    # - p2a3
    p2a3atk1.config(state=ACTIVE)
    p2a3atk2.config(state=ACTIVE)
    p2a3ult.config(state=ACTIVE)
    p2a3switch.config(state=ACTIVE)
def p2movebuttons_disable():
    # -- p2a1
    p2a1atk1.config(state=DISABLED)
    p2a1atk2.config(state=DISABLED)
    p2a1ult.config(state=DISABLED)
    p2a1switch.config(state=DISABLED)
    # -- p2a2
    p2a2atk1.config(state=DISABLED)
    p2a2atk2.config(state=DISABLED)
    p2a2ult.config(state=DISABLED)
    p2a2switch.config(state=DISABLED)
    # -- p2a3
    p2a3atk1.config(state=DISABLED)
    p2a3atk2.config(state=DISABLED)
    p2a3ult.config(state=DISABLED)
    p2a3switch.config(state=DISABLED)
def imgFirstCreate():
    global p1a1_image
    global p1a2_image
    global p1a3_image
    global p2a1_image
    global p2a2_image
    global p2a3_image

    p1a1_image = canvas.create_image(P1A1[0], P1A1[1], image=cardat_p1a1.card_actualImage)
    p1a2_image = canvas.create_image(P1A2[0], P1A2[1], image=cardat_p1a2.card_actualImage)
    p1a3_image = canvas.create_image(P1A3[0], P1A3[1], image=cardat_p1a3.card_actualImage)
    p2a1_image = canvas.create_image(P2A1[0], P2A1[1], image=cardat_p2a1.card_actualImage)
    p2a2_image = canvas.create_image(P2A2[0], P2A2[1], image=cardat_p2a2.card_actualImage)
    p2a3_image = canvas.create_image(P2A3[0], P2A3[1], image=cardat_p2a3.card_actualImage)
def statFirstCreate():
    # - P1
    global p1a1_hptext
    global p1a1_atktext
    global p1a1_spetext
    global p1a2_hptext
    global p1a2_atktext
    global p1a2_spetext
    global p1a3_hptext
    global p1a3_atktext
    global p1a3_spetext
    # - P2
    global p2a1_hptext
    global p2a1_atktext
    global p2a1_spetext
    global p2a2_hptext
    global p2a2_atktext
    global p2a2_spetext
    global p2a3_hptext
    global p2a3_atktext
    global p2a3_spetext
    # -- P1
    # - HP
    p1a1_hptext = canvas.create_text(P1A1[0] - 3, P1A1[1] + 116, text="{:,}".format(cardat_p1a1.card_hp),
                                     font=("System", 11, "bold"))
    p1a2_hptext = canvas.create_text(P1A2[0] - 3, P1A1[1] + 116, text="{:,}".format(cardat_p1a2.card_hp),
                                     font=("System", 11, "bold"))
    p1a3_hptext = canvas.create_text(P1A3[0] - 3, P1A3[1] + 116, text="{:,}".format(cardat_p1a3.card_hp),
                                     font=("System", 11, "bold"))
    # - ATK
    p1a1_atktext = canvas.create_text(P1A1[0] - 59, P1A1[1] + 116, text="{:,}".format(cardat_p1a1.card_atk),
                                      font=("System", 11, "bold"))
    p1a2_atktext = canvas.create_text(P1A2[0] - 59, P1A1[1] + 116, text="{:,}".format(cardat_p1a2.card_atk),
                                      font=("System", 11, "bold"))
    p1a3_atktext = canvas.create_text(P1A3[0] - 59, P1A3[1] + 116, text="{:,}".format(cardat_p1a3.card_atk),
                                      font=("System", 11, "bold"))
    # - SPE
    p1a1_spetext = canvas.create_text(P1A1[0] + 56, P1A1[1] + 116, text="{:,}".format(cardat_p1a1.card_spe),
                                      font=("System", 11, "bold"))
    p1a2_spetext = canvas.create_text(P1A2[0] + 56, P1A1[1] + 116, text="{:,}".format(cardat_p1a2.card_spe),
                                      font=("System", 11, "bold"))
    p1a3_spetext = canvas.create_text(P1A3[0] + 56, P1A3[1] + 116, text="{:,}".format(cardat_p1a3.card_spe),
                                      font=("System", 11, "bold"))
    # -- P2
    # - HP
    p2a1_hptext = canvas.create_text(P2A1[0] - 3, P2A1[1] + 116, text="{:,}".format(cardat_p2a1.card_hp),
                                     font=("System", 11, "bold"))
    p2a2_hptext = canvas.create_text(P2A2[0] - 3, P2A1[1] + 116, text="{:,}".format(cardat_p2a2.card_hp),
                                     font=("System", 11, "bold"))
    p2a3_hptext = canvas.create_text(P2A3[0] - 3, P2A3[1] + 116, text="{:,}".format(cardat_p2a3.card_hp),
                                     font=("System", 11, "bold"))
    # - ATK
    p2a1_atktext = canvas.create_text(P2A1[0] - 59, P2A1[1] + 116, text="{:,}".format(cardat_p2a1.card_atk),
                                      font=("System", 11, "bold"))
    p2a2_atktext = canvas.create_text(P2A2[0] - 59, P2A1[1] + 116, text="{:,}".format(cardat_p2a2.card_atk),
                                      font=("System", 11, "bold"))
    p2a3_atktext = canvas.create_text(P2A3[0] - 59, P2A3[1] + 116, text="{:,}".format(cardat_p2a3.card_atk),
                                      font=("System", 11, "bold"))
    # - SPE
    p2a1_spetext = canvas.create_text(P2A1[0] + 56, P2A1[1] + 116, text="{:,}".format(cardat_p2a1.card_spe),
                                      font=("System", 11, "bold"))
    p2a2_spetext = canvas.create_text(P2A2[0] + 56, P2A1[1] + 116, text="{:,}".format(cardat_p2a2.card_spe),
                                      font=("System", 11, "bold"))
    p2a3_spetext = canvas.create_text(P2A3[0] + 56, P2A3[1] + 116, text="{:,}".format(cardat_p2a3.card_spe),
                                      font=("System", 11, "bold"))
def imgUpdate():
    global p1a1_image
    global p1a2_image
    global p1a3_image
    global p2a1_image
    global p2a2_image
    global p2a3_image
    # - P1
    canvas.itemconfig(p1a1_image, image=cardat_p1a1.card_actualImage)
    canvas.itemconfig(p1a2_image, image=cardat_p1a2.card_actualImage)
    canvas.itemconfig(p1a3_image, image=cardat_p1a3.card_actualImage)
    # - P2
    canvas.itemconfig(p2a1_image, image=cardat_p2a1.card_actualImage)
    canvas.itemconfig(p2a2_image, image=cardat_p2a2.card_actualImage)
    canvas.itemconfig(p2a3_image, image=cardat_p2a3.card_actualImage)
    window.update()
def statUpdate():
    # - P1A1
    if cardat_p1a1.card_isAlive is True:
        canvas.itemconfig(p1a1_atktext, text="{:,}".format(cardat_p1a1.card_atk))
        canvas.itemconfig(p1a1_hptext, text="{:,}".format(cardat_p1a1.card_hp))
        canvas.itemconfig(p1a1_spetext, text="{:,}".format(cardat_p1a1.card_spe))
    else:
        canvas.itemconfig(p1a1_atktext, text="".format(cardat_p1a1.card_atk))
        canvas.itemconfig(p1a1_hptext, text="".format(cardat_p1a1.card_hp))
        canvas.itemconfig(p1a1_spetext, text="".format(cardat_p1a1.card_spe))
        cardat_p1a1.card_actualImage = nadaImg
    # - P1A2
    if cardat_p1a2.card_isAlive is True:
        canvas.itemconfig(p1a2_atktext, text="{:,}".format(cardat_p1a2.card_atk))
        canvas.itemconfig(p1a2_hptext, text="{:,}".format(cardat_p1a2.card_hp))
        canvas.itemconfig(p1a2_spetext, text="{:,}".format(cardat_p1a2.card_spe))
    else:
        canvas.itemconfig(p1a2_atktext, text="".format(cardat_p1a2.card_atk))
        canvas.itemconfig(p1a2_hptext, text="".format(cardat_p1a2.card_hp))
        canvas.itemconfig(p1a2_spetext, text="".format(cardat_p1a2.card_spe))
        cardat_p1a2.card_actualImage = nadaImg
    # - P1A3
    if cardat_p1a3.card_isAlive is True:
        canvas.itemconfig(p1a3_atktext, text="{:,}".format(cardat_p1a3.card_atk))
        canvas.itemconfig(p1a3_hptext, text="{:,}".format(cardat_p1a3.card_hp))
        canvas.itemconfig(p1a3_spetext, text="{:,}".format(cardat_p1a3.card_spe))
    else:
        canvas.itemconfig(p1a3_atktext, text="".format(cardat_p1a3.card_atk))
        canvas.itemconfig(p1a3_hptext, text="".format(cardat_p1a3.card_hp))
        canvas.itemconfig(p1a3_spetext, text="".format(cardat_p1a3.card_spe))
        cardat_p1a3.card_actualImage = nadaImg
    # - P2A1
    if cardat_p2a1.card_isAlive is True:
        canvas.itemconfig(p2a1_atktext, text="{:,}".format(cardat_p2a1.card_atk))
        canvas.itemconfig(p2a1_hptext, text="{:,}".format(cardat_p2a1.card_hp))
        canvas.itemconfig(p2a1_spetext, text="{:,}".format(cardat_p2a1.card_spe))
    else:
        canvas.itemconfig(p2a1_atktext, text="".format(cardat_p2a1.card_atk))
        canvas.itemconfig(p2a1_hptext, text="".format(cardat_p2a1.card_hp))
        canvas.itemconfig(p2a1_spetext, text="".format(cardat_p2a1.card_spe))
        cardat_p2a1.card_actualImage = nadaImg
    # - P2A2
    if cardat_p2a2.card_isAlive is True:
        canvas.itemconfig(p2a2_atktext, text="{:,}".format(cardat_p2a2.card_atk))
        canvas.itemconfig(p2a2_hptext, text="{:,}".format(cardat_p2a2.card_hp))
        canvas.itemconfig(p2a2_spetext, text="{:,}".format(cardat_p2a2.card_spe))
    else:
        canvas.itemconfig(p2a2_atktext, text="".format(cardat_p2a2.card_atk))
        canvas.itemconfig(p2a2_hptext, text="".format(cardat_p2a2.card_hp))
        canvas.itemconfig(p2a2_spetext, text="".format(cardat_p2a2.card_spe))
        cardat_p2a2.card_actualImage = nadaImg
    # - P2A3
    if cardat_p2a3.card_isAlive is True:
        canvas.itemconfig(p2a3_atktext, text="{:,}".format(cardat_p2a3.card_atk))
        canvas.itemconfig(p2a3_hptext, text="{:,}".format(cardat_p2a3.card_hp))
        canvas.itemconfig(p2a3_spetext, text="{:,}".format(cardat_p2a3.card_spe))
    else:
        canvas.itemconfig(p2a3_atktext, text="".format(cardat_p2a3.card_atk))
        canvas.itemconfig(p2a3_hptext, text="".format(cardat_p2a3.card_hp))
        canvas.itemconfig(p2a3_spetext, text="".format(cardat_p2a3.card_spe))
        cardat_p2a3.card_actualImage = nadaImg
    # - FINALIZANDO
    canvas.update()
    window.update()
def moveLabelUpdate():
    canvas.itemconfig(attacking_label, text=isAttacking+" is executing a move.")
    canvas.update()
    window.update()
# ------ WINDOW
window = Tk()
window.title("UTCG")
window.resizable(False, False)
running = True

# ------ CANVA
canvas = Canvas(window, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()
window.update()

# ------ LABELS
turn_label = Label(window, text="Turn: "+str(turn),font=("System",20))
turn_label.place(x=100,y=30)
isAttacking = "No one"
attacking_label = canvas.create_text(520,10,text=isAttacking+" is executing a move.",font=("Small Fonts",10))
p1_label = Label(window, text="P1:",font=("System",20,"italic"))
p1_label.place(x=250,y=550)
p2_label = Label(window, text="P2:",font=("System",20,"italic"))
p2_label.place(x=250,y=190)

# ------ CARTAS
nadaImg = PhotoImage(file="images/Nada.png")
# -- P1
p1card1 = Erza_The_Titania()
p1card1.card_tableLocation = "P1A1"
p1card1.card_actualImage = PhotoImage(file=p1card1.card_image)
cardat_p1a1 = p1card1

p1card2 = Zekrom_Dragon_Of_The_Unova_Myth()
p1card2.card_tableLocation = "P1A2"
p1card2.card_actualImage = PhotoImage(file=p1card2.card_image)
cardat_p1a2 = p1card2

p1card3 = Todoroki_My_Own_Power()
p1card3.card_tableLocation = "P1A3"
p1card3.card_actualImage = PhotoImage(file=p1card3.card_image)
cardat_p1a3 = p1card3

# -- P2
p2card1 = Erza_The_Titania()
p2card1.card_tableLocation = "P2A1"
p2card1.card_actualImage = PhotoImage(file=p2card1.card_image)
cardat_p2a1 = p2card1

p2card2 = Touka_Lightning_Cutter()
p2card2.card_tableLocation = "P2A2"
p2card2.card_actualImage = PhotoImage(file=p2card2.card_image)
cardat_p2a2 = p2card2

p2card3 = Todoroki_My_Own_Power()
p2card3.card_tableLocation = "P2A3"
p2card3.card_actualImage = PhotoImage(file=p2card3.card_image)
cardat_p2a3 = p2card3
# --
p1allcards = (p1card1, p1card2, p1card3)
p2allcards = (p2card1, p2card2, p2card3)
# -- BOTÕES
# - P1A1
# SWITCH
p1a1switch_frame = Frame(window,bg="pink",bd=5)
p1a1switch_frame.place(x=P1A1[0]-35,y=P1A1[1]-165)
p1a1switch = Button(p1a1switch_frame,command=lambda m="p1a1switch": p1switch(m),text="SWITCH")
p1a1switch.grid(row=0,column=0)
# MOVES
p1a1move_frame = Frame(window,bg="pink",bd=5)
p1a1move_frame.place(x=P1A1[0]-58,y=P1A1[1]+140)
p1a1atk1 = Button(p1a1move_frame,command=lambda m="p1a1atk1": send_attack(m),text="atk1")
p1a1atk2 = Button(p1a1move_frame,command=lambda m="p1a1atk2": send_attack(m),text="atk2")
p1a1ult = Button(p1a1move_frame,command=lambda m="p1a1atk3": send_attack(m),text="atk3")
p1a1atk1.grid(row=0,column=0)
p1a1atk2.grid(row=0,column=1)
p1a1ult.grid(row=0,column=2)
# - P1A2
# SWITCH
p1a2switch_frame = Frame(window,bg="pink",bd=5)
p1a2switch_frame.place(x=P1A2[0]-35,y=P1A2[1]-165)
p1a2switch = Button(p1a2switch_frame,command=lambda m="p1a2switch": p1switch(m),text="SWITCH")
p1a2switch.grid(row=0,column=0)
# MOVES
p1a2move_frame = Frame(window,bg="pink",bd=5)
p1a2move_frame.place(x=P1A2[0]-58,y=P1A2[1]+140)
p1a2atk1 = Button(p1a2move_frame,command=lambda m="p1a2atk1": send_attack(m),text="atk1")
p1a2atk2 = Button(p1a2move_frame,command=lambda m="p1a2atk2": send_attack(m),text="atk2")
p1a2ult = Button(p1a2move_frame,command=lambda m="p1a2atk3": send_attack(m),text="atk3")
p1a2atk1.grid(row=0,column=0)
p1a2atk2.grid(row=0,column=1)
p1a2ult.grid(row=0,column=2)
# - P1A3
# SWITCH
p1a3switch_frame = Frame(window,bg="pink",bd=5)
p1a3switch_frame.place(x=P1A3[0]-35,y=P1A3[1]-165)
p1a3switch = Button(p1a3switch_frame,command=lambda m="p1a3switch": p1switch(m),text="SWITCH")
p1a3switch.grid(row=0,column=0)
# MOVES
p1a3move_frame = Frame(window,bg="pink",bd=5)
p1a3move_frame.place(x=P1A3[0]-58,y=P1A3[1]+140)
p1a3atk1 = Button(p1a3move_frame,command=lambda m="p1a3atk1": send_attack(m),text="atk1")
p1a3atk2 = Button(p1a3move_frame,command=lambda m="p1a3atk2": send_attack(m),text="atk2")
p1a3ult = Button(p1a3move_frame,command=lambda m="p1a3atk3": send_attack(m),text="atk3")
p1a3atk1.grid(row=0,column=0)
p1a3atk2.grid(row=0,column=1)
p1a3ult.grid(row=0,column=2)
# - P2A1
# SWITCH
p2a1switch_frame = Frame(window,bg="pink",bd=5)
p2a1switch_frame.place(x=P2A1[0]-35,y=P2A1[1]-165)
p2a1switch = Button(p2a1switch_frame,command=lambda m="p2a1switch": p2switch(m),text="SWITCH")
p2a1switch.grid(row=0,column=0)
# MOVES
p2a1move_frame = Frame(window,bg="pink",bd=5)
p2a1move_frame.place(x=P2A1[0]-58,y=P2A1[1]+140)
p2a1atk1 = Button(p2a1move_frame,command=lambda m="p2a1atk1": send_attack(m),text="atk1")
p2a1atk2 = Button(p2a1move_frame,command=lambda m="p2a1atk2": send_attack(m),text="atk2")
p2a1ult = Button(p2a1move_frame,command=lambda m="p2a1atk3": send_attack(m),text="atk3")
p2a1atk1.grid(row=0,column=0)
p2a1atk2.grid(row=0,column=1)
p2a1ult.grid(row=0,column=2)
# - P2A2
# SWITCH
p2a2switch_frame = Frame(window,bg="pink",bd=5)
p2a2switch_frame.place(x=P2A2[0]-35,y=P2A2[1]-165)
p2a2switch = Button(p2a2switch_frame,command=lambda m="p2a2switch": p2switch(m),text="SWITCH")
p2a2switch.grid(row=0,column=0)
# MOVES
p2a2move_frame = Frame(window,bg="pink",bd=5)
p2a2move_frame.place(x=P2A2[0]-58,y=P2A2[1]+140)
p2a2atk1 = Button(p2a2move_frame,command=lambda m="p2a2atk1": send_attack(m),text="atk1")
p2a2atk2 = Button(p2a2move_frame,command=lambda m="p2a2atk2": send_attack(m),text="atk2")
p2a2ult = Button(p2a2move_frame,command=lambda m="p2a2atk3": send_attack(m),text="atk3")
p2a2atk1.grid(row=0,column=0)
p2a2atk2.grid(row=0,column=1)
p2a2ult.grid(row=0,column=2)
# - P2A3
# SWITCH
p2a3switch_frame = Frame(window,bg="pink",bd=5)
p2a3switch_frame.place(x=P2A3[0]-35,y=P2A3[1]-165)
p2a3switch = Button(p2a3switch_frame,command=lambda m="p2a3switch": p2switch(m),text="SWITCH")
p2a3switch.grid(row=0,column=0)
# MOVES
p2a3move_frame = Frame(window,bg="pink",bd=5)
p2a3move_frame.place(x=P2A3[0]-58,y=P2A3[1]+140)
p2a3atk1 = Button(p2a3move_frame,command=lambda m="p2a3atk1": send_attack(m),text="atk1")
p2a3atk2 = Button(p2a3move_frame,command=lambda m="p2a3atk2": send_attack(m),text="atk2")
p2a3ult = Button(p2a3move_frame,command=lambda m="p2a3atk3": send_attack(m),text="atk3")
p2a3atk1.grid(row=0,column=0)
p2a3atk2.grid(row=0,column=1)
p2a3ult.grid(row=0,column=2)
# - CONFIRM
p1confirm_button = Button(window,command=lambda m="p1confirm": confirmfunc(m),text="confirm",bg="pink",activebackground="pink")
p1confirm_button.place(x=250,y=590)
p2confirm_button = Button(window,command=lambda m="p2confirm": confirmfunc(m),text="confirm",bg="pink",activebackground="pink")
p2confirm_button.place(x=250,y=230)
# - CANCEL
p1cancel_button = Button(window,command=lambda m="p1cancel": cancel(m),text="cancel",bg="pink",activebackground="pink")
p1cancel_button.place(x=250,y=620)
p2cancel_button = Button(window,command=lambda m="p2cancel": cancel(m),text="cancel",bg="pink",activebackground="pink")
p2cancel_button.place(x=250,y=260)

# --- CARTAS E SUAS IMAGENS
imgFirstCreate()
# --- CARTAS E SEUS TEXTOS:
statFirstCreate()

# ------ FINALIZAÇÃO
window.mainloop()