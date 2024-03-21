from card import Card

class Futaba_The_Navigator(Card):
    # -- VARIÁVEIS DA CARTA
    INI_ATK = 300  # ataque inicial da carta
    INI_HP = 90000  # hp inicial da carta
    INI_SPE = 3750  # spe inicial da carta
    card_atk = 300  # ataque atual da carta
    card_hp = 90000  # hp atual da carta
    card_spe = 3750  # speed atual da carta
    card_id = "Blue_Futaba_The_Navigator"  # id atual da carta, ex. Yellow_Erza_The_Titania
    card_type = "Futaba"  # tipo da cThearta, ex. Erza
    card_displayName = "Futaba The Navigator"  # nome de display, ex. Erza the Titania
    card_image = "images/Persona_3_Futaba The Navigator.png"  # imagem da carta
    card_actualImage = None
    card_isAlive = True  # saber se a carta está viva ou não, bool
    card_tableLocation = None
    card_critDMG = 1.5
    card_armor = None
    card_isBlocking = None
    card_ultimateCharges = 1
    # -- VARIÁVEIS DO MOVIMENTO 1
    move1_damage = 0
    move1_maxregen = 20000
    move1_ishealing = True
    move1_istransform = None
    move1_isultimate = False
    move1_selectiontype = "Send"  # "Normal", "1-3" or "1-6"
    move1_affectedenemies = "Normal"  # "Normal", "HF", "HE", "HEL", "THEL", "HALL"
    # -- VARIÁVEIS DO MOVIMENTO 2
    move2_damage = 0
    move2_regen = 50000
    move2_ishealing = True
    move2_istransform = None
    move2_isultimate = False
    move2_selectiontype = "Send"  # "Normal", "1-3" or "1-6"
    move2_affectedenemies = "Normal"  # "Normal", "HF", "HE", "HEL", "THEL", "HALL"
    # -- VARIÁVEIS DO MOVIMENTO 3
    move3_damage = 0
    move3_istransform = None
    move3_isultimate = True
    move3_selectiontype = "Normal"  # "Normal", "1-3" or "1-6"
    move3_affectedenemies = "THEL"  # "Normal", "HF", "HE", "HEL", "THEL", "HALL"
