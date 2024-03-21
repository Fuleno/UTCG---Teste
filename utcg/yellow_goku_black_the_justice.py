from card import Card

class Goku_Black_The_Justice(Card):
    # -- VARIÁVEIS DA CARTA
    INI_ATK = 1100  # ataque inicial da carta
    INI_HP = 100000  # hp inicial da carta
    INI_SPE = 5000  # spe inicial da carta
    card_atk = 1100  # ataque atual da carta
    card_hp = 100000  # hp atual da carta
    card_spe = 5000  # speed atual da carta
    card_id = "Yellow_Goku_Black_The_Justice"  # id atual da carta, ex. Yellow_Erza_The_Titania
    card_type = "Goku_Black"  # tipo da cThearta, ex. Erza
    card_displayName = "Goku Black - The Justice"  # nome de display, ex. Erza the Titania
    card_image = "images/DBZ_Yellow_Goku Black The Justice2.png"  # imagem da carta
    card_actualImage = None
    card_isAlive = True  # saber se a carta está viva ou não, bool
    card_tableLocation = None
    card_critDMG = 1.5
    card_armor = None
    card_isBlocking = None
    card_ultimateCharges = 1
    # -- VARIÁVEIS DO MOVIMENTO 1
    move1_damage = 120
    move1_istransform = None
    move1_isultimate = False
    move1_selectiontype = "Normal"  # "Normal", "1-3" or "1-6"
    move1_affectedenemies = "Normal"  # "Normal", "HF", "HE", "HEL", "HALL"
    # -- VARIÁVEIS DO MOVIMENTO 2
    move2_damage = 0
    move2_maxregen = 20000
    move2_ishealing = True
    move2_istransform = None
    move2_isultimate = False
    move2_selectiontype = "Normal"  # "Normal", "1-3" or "1-6"
    move2_affectedenemies = "Normal"  # "Normal", "HF", "HE", "HEL", "HALL"
    # -- VARIÁVEIS DO MOVIMENTO 3
    move3_damage = 200
    move3_istransform = None
    move3_isultimate = True
    move3_selectiontype = "Normal"  # "Normal", "1-3" or "1-6"
    move3_affectedenemies = "Normal"  # "Normal", "HF", "HE", "HEL", "HALL"
