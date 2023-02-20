import random


class Character:
    def __init__(self, name, faculty, health, strength, defense):
        self.name = name
        self.faculty = faculty
        self.health = health
        self.strength = strength
        self.defense = defense


class Spell:
    def __init__(self, name, damage, accuracy):
        self.name = name
        self.damage = damage
        self.accuracy = accuracy


# Створюємо персонажів
harry = Character("Гаррі Поттер", "Ґрифіндор", 100, 20, 10)
hermione = Character("Герміона", "Рейвенклов", 100, 15, 15)
cedric = Character("Седрик", "Ґрифіндор", 100, 18, 12)

# Створюємо закляття
ravenclaw_spell = Spell("Рейвенклов", 20, 0.7)
gryffindor_spell = Spell("Ґрифіндор", 25, 0.6)

# Випадково вибираємо закляття для гравців
player1_spell = random.choice([ravenclaw_spell, gryffindor_spell])
player2_spell = random.choice([ravenclaw_spell, gryffindor_spell])

# Випадково визначаємо, хто починає гру
player1_turn = random.choice([True, False])

# Цикл гри
while harry.health > 0 and hermione.health > 0:
    # Визначаємо поточного гравця
    if player1_turn:
        player = harry
        opponent = hermione
        spell = player1_spell
    else:
        player = hermione
        opponent = harry
        spell = player2_spell

    # Гравець атакує
    if random.random() < spell.accuracy:
        damage = spell.damage - opponent.defense
        if damage < 0:
            damage = 0
        opponent.health -= damage
        print(f"{player.name} використовує {spell.name} і завдає {damage} пошкоджень")
    else:
        print(f"{player.name} спробував використати {spell.name}, але промахнувся")

    # Змінюємо поточного гравця
    player1_turn = not player1_turn

# Визначаємо перемож
if harry.health <= 0:
    print("Переможець: Герміона")
elif hermione.health <= 0:
    print("Переможець: Гаррі Поттер")
else:
    print("Щось пішло не так. Гравці живі, але гра закінчилася.")