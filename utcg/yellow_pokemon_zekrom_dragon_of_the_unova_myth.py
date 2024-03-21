from card import Card

class Zekrom_Dragon_Of_The_Unova_Myth(Card):
    # -- VARIÁVEIS DA CARTA
    INI_ATK = 1100  # ataque inicial da carta
    INI_HP = 90000  # hp inicial da carta
    INI_SPE = 4400  # spe inicial da carta
    card_atk = 1100  # ataque atual da carta
    card_hp = 90000  # hp atual da carta
    card_spe = 4400  # speed atual da carta
    card_id = "Yellow_Zekrom_Dragon_Of_The_Unova_Myth"  # id atual da carta, ex. Yellow_Erza_The_Titania
    card_type = "Zekrom"  # tipo da cThearta, ex. Erza
    card_displayName = "Zekrom Dragon of the Unova Myth"  # nome de display, ex. Erza the Titania
    card_image = "images/Pokemon_4_Zekrom Dragon of the Unova Myth2.png"  # imagem da carta
    card_actualImage = None
    card_isAlive = True  # saber se a carta está viva ou não, bool
    card_tableLocation = None
    card_critDMG = 1.5
    card_armor = None
    card_isBlocking = None
    card_isTransformed = False
    card_ultimateCharges = 1
    # -- VARIÁVEIS DO MOVIMENTO 1
    move1_number = 1
    move1_damage = 95
    move1_istransform = None
    move1_isultimate = False
    move1_selectiontype = "Normal"  # "Normal", "1-3" or "1-6"
    move1_affectedenemies = "HE"  # "Normal", "HF", "HE", "HEL", "HALL"
    move1_variables = (move1_number, move1_damage, move1_istransform, move1_isultimate,
                       move1_selectiontype, move1_affectedenemies)
    # -- VARIÁVEIS DO MOVIMENTO 2
    move2_number = 2
    move2_damage = 110
    move2_istransform = None
    move2_isultimate = False
    move2_selectiontype = "Normal"  # "Normal", "1-3" or "1-6"
    move2_affectedenemies = "HALL"  # "Normal", "HF", "HE", "HEL", "HALL"
    move2_variables = (move2_number, move2_damage, move2_istransform, move2_isultimate,
                       move2_selectiontype, move2_affectedenemies)
    # -- VARIÁVEIS DO MOVIMENTO 3
    move3_number = 3
    move3_istransform = True
    move3_transformatkmultiply = 2
    move3_transformspemultiply = 2
    move3_isultimate = None
    move3_selectiontype = "Normal"  # "Normal", "1-3" or "1-6"
    move3_affectedenemies = "Normal"  # "Normal", "HF", "HE", "HEL", "HALL"
    move3_variables = (move3_number, move3_istransform, move3_transformatkmultiply,
                       move3_transformspemultiply, move3_isultimate, move3_selectiontype,
                       move3_affectedenemies)

    def doMove(self,card,move,frontenemy,enemy2,enemy3,team1,team2,turn):
        match move[0]:
            case 1:
                final_damage = int((move[1] / 2) * (card.card_atk + move[1]))
                frontenemy.card_hp -= final_damage
                enemy2.card_hp -= final_damage
                enemy3.card_hp -= final_damage
                print("Você está usando o move 1 do Zekrom!")  # remover depois
            case 2:
                final_damage = int((move[1] / 2) * (card.card_atk + move[1]))
                frontenemy.card_hp -= final_damage
                enemy2.card_hp -= final_damage
                enemy3.card_hp -= final_damage
                team1.card_hp -= final_damage
                team2.card_hp -= final_damage
                print("Você está usando o move 2 do Zekrom!")  # remover depois
            case 3:
                if turn >= 2 and card.card_isTransformed is False:
                    card.card_atk = int(card.card_atk*2)
                    card.card_spe = int(card.card_spe*2)
                    card.card_isTransformed = True
                    print("Você está usando o move 3 do Zekrom!")
                else:
                    print("Ele não pode se transformar!")