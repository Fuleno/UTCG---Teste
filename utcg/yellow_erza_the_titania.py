from card import Card

class Erza_The_Titania(Card):
    # -- VARIÁVEIS DA CARTA
    INI_ATK = 1050  # ataque inicial da carta
    INI_HP = 135000  # hp inicial da carta
    INI_SPE = 5280  # spe inicial da carta
    card_atk = 1050  # ataque atual da carta
    card_hp = 135000  # hp atual da carta
    card_spe = 5280  # speed atual da carta
    card_id = "Yellow_Erza_The_Titania"  # id atual da carta, ex. Yellow_Erza_The_Titania
    card_type = "Erza"  # tipo da cThearta, ex. Erza
    card_displayName = "Erza The Titania"  # nome de display, ex. Erza the Titania
    card_image = "images/Fairy Tail_Yellow_Erza_The_Titania2.png"  # imagem da carta
    card_actualImage = None
    card_isAlive = True  # saber se a carta está viva ou não, bool
    card_tableLocation = None
    card_critDMG = 1.5
    card_armor = None
    card_isBlocking = None
    card_ultimateCharges = 1
    # -- VARIÁVEIS DO MOVIMENTO 1
    move1_number = 1
    move1_damage = 140
    move1_regen = None
    move1_maxregen = None
    move1_ishealing = None
    move1_istransform = None
    move1_transformstatsmultiply = None
    move1_transformatkmultiply = None
    move1_transformhpmultiply = None
    move1_transformspemultiply = None
    move1_isultimate = False
    move1_isblockmove = None
    move1_selectiontype = "Normal"  # "Normal", "Send", "1-3" or "1-6"
    move1_affectedenemies = "Normal"  # "Normal", "HF", "HE", "HEL", "THEL", "HALL"
    move1_variables = (move1_number, move1_damage, move1_regen, move1_maxregen, move1_ishealing,
                       move1_istransform, move1_transformstatsmultiply,
                       move1_transformatkmultiply, move1_transformhpmultiply,
                       move1_transformspemultiply, move1_isultimate, move1_isblockmove,
                       move1_selectiontype, move1_affectedenemies)
    # -- VARIÁVEIS DO MOVIMENTO 2
    move2_number = 2
    move2_damage = 90
    move2_regen = None
    move2_maxregen = None
    move2_ishealing = None
    move2_istransform = None
    move2_transformstatsmultiply = None
    move2_transformatkmultiply = None
    move2_transformhpmultiply = None
    move2_transformspemultiply = None
    move2_isultimate = False
    move2_isblockmove = None
    move2_selectiontype = "Normal"  # "Normal", "Send", "1-3" or "1-6"
    move2_affectedenemies = "Normal"  # "Normal", "HF", "HE", "HEL", "THEL", "HALL"
    move2_variables = (move2_number, move2_damage, move2_regen, move2_maxregen, move2_ishealing,
                       move2_istransform, move2_transformstatsmultiply,
                       move2_transformatkmultiply, move2_transformhpmultiply,
                       move2_transformspemultiply, move2_isultimate, move2_isblockmove,
                       move2_selectiontype, move2_affectedenemies)
    # -- VARIÁVEIS DO MOVIMENTO 3
    move3_number = 3
    move3_damage = 80
    move3_regen = None
    move3_maxregen = None
    move3_ishealing = None
    move3_istransform = None
    move3_transformstatsmultiply = None
    move3_transformatkmultiply = None
    move3_transformhpmultiply = None
    move3_transformspemultiply = None
    move3_isultimate = None
    move3_isblockmove = None
    move3_selectiontype = "Normal"  # "Normal", "Send", "1-3" or "1-6"
    move3_affectedenemies = "Normal"  # "Normal", "HF", "HE", "HEL", "THEL", "HALL"
    move3_variables = (move3_number, move3_damage, move3_regen, move3_maxregen, move3_ishealing,
                       move3_istransform, move3_transformstatsmultiply,
                       move3_transformatkmultiply, move3_transformhpmultiply,
                       move3_transformspemultiply, move3_isultimate, move3_isblockmove,
                       move3_selectiontype, move3_affectedenemies)

    def doMove(self,card,move,frontenemy,enemy2,enemy3,team1,team2,turn):
        match move[0]:
            case 1:
                final_damage = int((move[1] / 2) * (card.card_atk + move[1]))
                frontenemy.card_hp -= final_damage
                print("Você está usando o move 1 da Erza!")  # remover depois
            case 2:
                final_damage = int((move[1] / 2) * (card.card_atk + move[1]))
                frontenemy.card_hp -= final_damage
                print("Você está usando o move 2 da Erza!")  # remover depois
            case 3:
                final_damage = int((move[1] / 2) * (card.card_atk + move[1]))
                frontenemy.card_hp -= final_damage
                print("Você está usando o move 3 da Erza!")  # remover depois
