from abc import ABC, abstractmethod

class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

class Sword(Weapon):
    def attack(self):
        return "Боец наносит удар мечом."

class Bow(Weapon):
    def attack(self):
        return "Боец наносит удар из лука."


class Fighter:
    def __init__(self, weapon: Weapon):
        self.weapon = weapon

    def changeWeapon(self, weapon: Weapon):
        self.weapon = weapon

    def attack(self):
        print(self.weapon.attack())

class Monster:
    # Демонстрация простого монстра
    def __init__(self, health=10):
        self.health = health

    def take_damage(self):
        self.health -= 5
        if self.health <= 0:
            print("Монстр побежден!")
        else:
            print("Монстр принимает удар, но все еще в строю.")

def battle(fighter, monster):
    print("Боя началося!")
    while monster.health > 0:
        attack_result = fighter.weapon.attack()
        print(attack_result)
        monster.take_damage()
    print("Бой окончен.")

# Симуляция боя
fighter = Fighter(Sword())  # Сначала используем меч
monster = Monster()

battle(fighter, monster)

fighter.changeWeapon(Bow())  # Меняем оружие на лук
monster = Monster()  # Создаем нового монстра для нового раунда

battle(fighter, monster)