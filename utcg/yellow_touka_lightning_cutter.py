from card import Card
import tkinter

class Touka_Lightning_Cutter(Card):
    # -- VARIÁVEIS DA CARTA
    INI_ATK = 1400  # ataque inicial da carta
    INI_HP = 100000  # hp inicial da carta
    INI_SPE = 5600  # spe inicial da carta
    card_atk = 1400  # ataque atual da carta
    card_hp = 100000  # hp atual da carta
    card_spe = 5600  # speed atual da carta
    card_id = "Yellow_Touka_Lightning_Cutter"  # id atual da carta, ex. Yellow_Erza_The_Titania
    card_type = "Touka_Rakudai"  # tipo da carta, ex. Erza
    card_displayName = "Touka - Lightning Cutter"  # nome de display, ex. Erza the Titania
    card_image = "images/Rakudai_4_Touka Lightning Cutter2.png"  # imagem da carta
    card_actualImage = None
    card_isAlive = True  # saber se a carta está viva ou não, bool
    card_tableLocation = None
    card_critDMG = 1.5
    card_armor = None
    card_isBlocking = None
    card_ultimateCharges = 1
    # -- VARIÁVEIS DO MOVIMENTO 1
    move1_number = 1
    move1_damage = 100
    move1_istransform = None
    move1_isultimate = False
    move1_selectiontype = "Normal"  # "Normal", "1-3" or "1-6"
    move1_affectedenemies = "Normal"  # "Normal", "HF", "HE", "HEL", "HALL"
    move1_variables = (move1_number,move1_damage,move1_istransform,move1_isultimate,
                       move1_selectiontype,move1_affectedenemies)
    # -- VARIÁVEIS DO MOVIMENTO 2
    move2_number = 2
    move2_damage = 90
    move2_istransform = None
    move2_isultimate = False
    move2_selectiontype = "Normal"  # "Normal", "1-3" or "1-6"
    move2_affectedenemies = "Normal"  # "Normal", "HF", "HE", "HEL", "HALL"
    move2_variables = (move2_number,move2_damage, move2_istransform, move2_isultimate,
                       move2_selectiontype, move2_affectedenemies)
    # -- VARIÁVEIS DO MOVIMENTO 3
    move3_number = 3
    move3_damage = 180
    move3_istransform = None
    move3_isultimate = True
    move3_selectiontype = "Normal"  # "Normal", "1-3" or "1-6"
    move3_affectedenemies = "Normal"  # "Normal", "HF", "HE", "HEL", "HALL"
    move3_variables = (move3_number,move3_damage, move3_istransform, move3_isultimate,
                       move3_selectiontype, move3_affectedenemies)

    def doMove(self,card,move,frontenemy,enemy2,enemy3,team1,team2,turn):
        match move[0]:
            case 1:
                final_damage = int((move[1] / 2) * (card.card_atk + move[1]))
                frontenemy.card_hp -= final_damage
                print("Você está usando o move 1 da Touka!")  # remover depois
            case 2:
                final_damage = int((move[1] / 2) * (card.card_atk + move[1]))
                frontenemy.card_hp -= final_damage
                print("Você está usando o move 2 da Touka!")  # remover depois
            case 3:
                if turn >= 1 and card.card_ultimateCharges > 0:
                    final_damage = int((move[1] / 2) * (card.card_atk + move[1]))
                    frontenemy.card_hp -= final_damage
                    card.card_ultimateCharges -= 1
                    print("Você está usando o move 3 da Touka!")  # remover depois
                else:
                    print("Você não pode tentar usar este move!")