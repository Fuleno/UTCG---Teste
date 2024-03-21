from card import Card

class Todoroki_My_Own_Power(Card):
    # -- VARIÁVEIS DA CARTA
    INI_ATK = 900  # ataque inicial da carta
    INI_HP = 85000  # hp inicial da carta
    INI_SPE = 4500  # spe inicial da carta
    card_atk = 900  # ataque atual da carta
    card_hp = 85000  # hp atual da carta
    card_spe = 4500  # speed atual da carta
    card_id = "Yellow_Todoroki_My_Own_Power"  # id atual da carta, ex. Yellow_Erza_The_Titania
    card_type = "Todoroki"  # tipo da carta, ex. Erza
    card_displayName = "Todoroki - My Own Power"  # nome de display, ex. Erza the Titania
    card_image = "images/BNH_Yellow_Todoroki My Own Power2.png"  # imagem da carta
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
    move1_damage = 110
    move1_istransform = None
    move1_isultimate = False
    move1_selectiontype = "Normal"  # "Normal", "1-3" or "1-6"
    move1_affectedenemies = "Normal"  # "Normal", "HF", "HE", "HEL", "HALL"
    move1_variables = (move1_number, move1_damage, move1_istransform, move1_isultimate,
                       move1_selectiontype, move1_affectedenemies)
    # -- VARIÁVEIS DO MOVIMENTO 2
    move2_number = 2
    move2_damage = 0
    move2_istransform = None
    move2_isultimate = False
    move2_isblockmove = True
    move2_selectiontype = "Normal"  # "Normal", "1-3" or "1-6"
    move2_affectedenemies = "Normal"  # "Normal", "HF", "HE", "HEL", "HALL"
    # -- VARIÁVEIS DO MOVIMENTO 3
    move3_number = 3
    move3_damage = 0
    move3_istransform = True
    move3_transformstatsmultiply = 1.5
    move3_isultimate = None
    move3_selectiontype = "Normal"  # "Normal", "1-3" or "1-6"
    move3_affectedenemies = "Normal"  # "Normal", "HF", "HE", "HEL", "HALL"

    def doMove(self,card,move,frontenemy,enemy2,enemy3,team1,team2,turn):
        match move[0]:
            case 1:
                final_damage = int((move[1] / 2) * (card.card_atk + move[1]))
                frontenemy.card_hp -= final_damage
                print("Você está usando o move 1 do Todoroki!")  # remover depois
            case 2:
                card.card_isBlocking = True
                print("A carta está bloqueando!")  # remover depois
            case 3:
                if turn >= 2 and card.card_isTransformed is False:
                    card.card_atk = int(card.card_atk*1.5)
                    card.card_hp = int(card.card_hp*1.5)
                    card.card_spe = int(card.card_spe*1.5)
                    card.card_isTransformed = True
                    print("Você está usando o move 3 do Todoroki!")
                else:
                    print("Ele não pode se transformar!")