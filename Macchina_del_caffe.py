# RICCARDO LA ROCCA
# Macchina del caffè in python

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resources(str):
    ritorno = True
    acqua = resources["water"]  # acqua contiene le risorse della macchinetta
    caffe = resources["coffee"]
    acqua -= MENU[str]["ingredients"][
        "water"]  # se acqua <0 significa che le risorse richieste sono maggiori di quelle contenute nella macchinetta
    caffe -= MENU[str]["ingredients"]["coffee"]

    global is_on
    str_alert = ""  # stringa con le risorse non valide
    if acqua < 0:
        str_alert += "There is not enough water. "
        ritorno = False
        is_on = False  # spengo anche la macchina se manca qualcosa
    if caffe < 0:
        str_alert += "There is not enough coffee. "
        ritorno = False
        is_on = False
    if str != "espresso":  # se non e' espresso controllo anche il latte (cappuccino e latte)
        latte = resources["milk"]
        latte -= MENU[str]["ingredients"]["milk"]
        if latte < 0:
            str_alert += "There is not enough milk. "
            ritorno = False
            is_on = False
    if not ritorno:
        print(str_alert)
    return ritorno


# Stampa le risorse della macchina
def print_report():
    for (chiave, valore) in resources.items():  # items ritorna una tupla con key e valore associato
        if chiave == "water" or chiave == "milk":
            print(f"{chiave}: {valore}ml")
        else:
            print(f"{chiave}: {valore}g")
    print(f"Money: ${machine_wallet}")


# effettua input e controlla se valido
def coins_input():
    totale_input_locale = 0
    moneta_input = 0

    print("Quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01")
    try:
        # quarters
        moneta_input = float(input("How many quarters? "))
        if moneta_input > 20:  # massimo 5$ di input
            while moneta_input > 20:
                print("You can't insert more than 20 quarters!")
                moneta_input = float(input("How many quarters? "))
        totale_input_locale += moneta_input * 0.25

        # dimes
        moneta_input = float(input("How many dimes? "))
        if moneta_input > 30:
            while moneta_input > 30:
                print("You can't insert more than 30 dimes")
                moneta_input = float(input("How many dimes? "))
        totale_input_locale += moneta_input * 0.1

        # nickles
        moneta_input = float(input("How many nickles? "))
        if moneta_input > 10:
            while moneta_input > 10:
                print("You can't insert more than 10 nickles!")
                moneta_input = float(input("How many nickles? "))
        totale_input_locale += moneta_input * 0.05

        # pennies
        moneta_input = float(input("How many pennies? "))
        if moneta_input > 20:
            while moneta_input > 20:
                print("You can't insert more than 20 pennies!")
                moneta_input = float(input("How many pennies? "))
        totale_input_locale += moneta_input * 0.01

    except ValueError:
        print("Invalid input")
    return totale_input_locale


# modifica le quantità nella macchinetta
def reduce_resources(str):  # str contiene sempre il nome della bevanda scelta
    global resources  # globale per poter accedere ai valori direttamente
    dict_ingredienti = MENU[str]["ingredients"]

    for ingrediente, quantita in dict_ingredienti.items():
        resources[ingrediente] -= quantita


# controlla se il saldo è abbastanza per acquistare il caffe
def check_money(str, totale_input):
    if totale_input >= MENU[str]["cost"]:  # input maggiore del prezzo di listino
        print(f"Here is your {str}. Enjoy!")
        global machine_wallet  # dichiaro la variabile globale cosi' da poterla raggiungere
        machine_wallet += MENU[str]["cost"]
        reduce_resources(str)
        if totale_input > MENU[str]["cost"]:
            totale_input -= MENU[str]["cost"]
            print(f"Here is {round(totale_input, 2)}$ dollars in change")
            print_report()
    else:
        print("Sorry that's not enough money. Money refunded")
    print("\n")


def print_prices():
    print('''La Rocca Cafe
    Espresso: 1.5$
    Latte: 2.5$
    Cappuccino: 3$\n''')


# TODO MAIN
print_prices()
is_on = True  # flag
machine_wallet = 0

totale_input = 0

while is_on:  # inizializzato a True, continua finché non cambia stato (off)
    if is_on:
        stringa_Input = input('What would you like? (espresso/latte/cappuccino/prices): ').lower()

    if stringa_Input == 'off':
        is_on = False
        print("Machine turned off")
    elif stringa_Input == 'report':
        print_report()
    elif stringa_Input == 'espresso' or stringa_Input == 'latte' or stringa_Input == 'cappuccino':
        if check_resources(stringa_Input):  # se ci sono abbastanza risorse richiedo denaro
            totale_input = coins_input()
            check_money(stringa_Input, totale_input)
    elif stringa_Input == 'prices':
        print_prices()
    else:
        print("Invalid input")
