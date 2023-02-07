import random as rnd
def start():
    Level1 = int(1)
    HP1 = float(0)
    MP1 = float(0)
    Damage1 = float(0)
    Def1 = float(0)
    Crit_Rate1 = float(0)
    abilities_character1 = list()
    abilities_list1 = list()
    Level2 = int(1)
    HP2 = float(0)
    MP2 = float(0)
    Damage2 = float(0)
    Def2 = float(0)
    Crit_Rate2 = float(0)
    abilities_character2 = list()
    abilities_list2 = list()
    while True:
        try:
            abilities_character1.clear()
            print("#====================================================+==========#")
            print("|           Виберіть персонажа разом з його класом:             |")
            print("|  ГРІФІНДОР       РАЙВЕНКЛОВ       ГАФЕЛПАФ        СЛИЗЕРИН    |")
            print('|---------------------------------------------------------------|')
            print("|Гаррі Поттер    Полумна Лавгуд     Седрик        Драко Малфой  |")
            print('|(невколупний)     (творчий)     (наполегливий)   (невколупний) |')
            print("|   Герміона       Чжоу Чанг      Ханна Аббот     Вінсент Кребб |")
            print('|(наполегливий)   (вразливий)      (творчий)       (вразливий)  |')
            print("#===============================================================#")
            character1 = str(input('Виберіть першого персонажа: '))
            class1 = str(input('Впишіть клас який знаходиться під іменем вашого персонажа: '))
            if class1.lower() == 'невколупний':
                HP1 = 20
                MP1 = 5
                Damage1 = 6
                Def1 = 4
                Crit_Rate1 = 25
                break
            if class1.lower() == 'творчий':
                HP1 = 18
                MP1 = 10
                Damage1 = 4
                Def1 = 9
                Crit_Rate1 = 15
                break
            elif class1.lower() == 'наполегливий':
                HP1 = 20
                MP1 = 10
                Damage1 = 5
                Def1 = 5
                Crit_Rate1 = 15
                break
            elif class1.lower() == 'вразливий':
                HP1 = 16
                MP1 = 10
                Damage1 = 4
                Def1 = 4
                Crit_Rate1 = 13
                break
            else:
                raise Exception('Невідомий персонаж! Повторіть спробу!')
        except Exception as e:
            print(e)
    while True:
        try:
            character2 = str(input('Виберіть другого персонажа: '))
            class2 = str(input('Впишіть клас який знаходиться під іменем вашого персонажа: '))
            if class2.lower() == 'невколупний':
                HP2 = 20
                MP2 = 5
                Damage2 = 6
                Def2 = 4
                Crit_Rate2 = 20
                break
            elif class2.lower() == 'творчий':
                HP2 = 18
                MP2 = 10
                Damage2 = 4
                Def2 = 9
                Crit_Rate2 = 15
                break
            elif class2.lower() == 'наполегливий':
                HP2 = 20
                MP2 = 10
                Damage2 = 5
                Def2 = 5
                Crit_Rate2 = 15
                break
            elif class2.lower() == 'вразливий':
                HP2 = 16
                MP2 = 10
                Damage2 = 4
                Def2 = 4
                Crit_Rate2 = 13
                break
            else:
                raise Exception('Невідомий клас! Повторіть спробу!')

        except Exception as e:
            print(e)
    game_process(HP1, MP1, Damage1, Def1, Crit_Rate1, abilities_character1, character1, HP2, MP2, Damage2, Def2, Crit_Rate2, abilities_character2, character2)

def game_process(HP1, MP1, Damage1, Def1, Crit_Rate1, abilities_character1, character1, HP2, MP2, Damage2, Def2, Crit_Rate2, abilities_character2, character2):
    for i in range(0, 3):
        print(f"Хвиля №{i+1}")
        while True:
            print("Інформація про : ")
            print(f"Персонаж: {character2}")
            print(f"HP: {HP2}")
            print(f"MP: {MP2}")
            print(f"Damage: {Damage2}")
            print(f"Def: {Def2}")
            print(f"Crit Rate: {Crit_Rate2}")
            print(f"Здібності: {abilities_character2}")
            print("================================")
            print("Інформація про ")
            print(f"Персонаж: {character1}")
            print(f"HP: {HP1}")
            print(f"MP: {MP1}")
            print(f"Damage: {Damage1}")
            print(f"Def: {Def1}")
            print(f"Crit Rate: {Crit_Rate1}")
            print(f"Здібності: {abilities_character1}")
            start = bool(rnd.randint(0, 2))
            if start == True: #user1
                print('Ваш хід:')
                input()
                start = False
                result_damage_by_user1 = Damage1 + (Damage1*Crit_Rate1/100)
                if result_damage_by_user1 > Def2:
                    current_damage = result_damage_by_user1 - Def2
                    Def2 = 0
                    HP2 -= current_damage
                    if HP2 < 0:
                        HP2 = 0
                        print(f"Ви вбили {character2}!")
                        break
                else:
                    Def2 -= result_damage_by_user1
            else: #user2
                start = True
                result_damage_by_user2 = Damage2 + (Damage2*Crit_Rate2/100)
                if result_damage_by_user2 > Def1:
                    current_damage = result_damage_by_user2 - Def1
                    Def1 = 0
                    HP1 -= current_damage
                    if HP1 < 0:
                        HP1 = 0
                        print(f'Ви вбили {character1}')
                        break
                    end()
                else:
                    Def1 -= result_damage_by_user2
                    input()

def end():
    print('Exit')
if __name__ == "__main__":
    try:
        start()
    except Exception as e:
        print(e)