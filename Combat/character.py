import random

class Character:
    def __init__(self, name=None):        
        self.name = name
        self.role = self.__class__.__name__ 
        self.boosted = False
        self.hp = None
        self.damage = None
        self.dodgeProbability = None
        self.criticalHitProbability = None

    def setHp(self, hp):
        if hp < 0:
            hp = 0
        self.hp = hp
        return self
    
    def setDamage(self, damage):
        if damage < 0:
            raise ValueError("Damage cannot be negative.")
        self.damage = damage
        return self

    def setDodgeProbability(self, dodgeProbability):
        if not (0 <= dodgeProbability <= 100):
            raise ValueError("Dodge probability must be between 0 and 100.")
        self.dodgeProbability = dodgeProbability
        return self

    def setCriticalHitProbability(self, criticalHitProbability):
        if not (0 <= criticalHitProbability <= 100):
            raise ValueError("Critical hit probability must be between 0 and 100.")
        self.criticalHitProbability = criticalHitProbability
        return self
    
    def powerUp(self, other): {
        
    }

    def attack(self, other): 
        print(f"{self.name} attacks {other.name}!")

        if random.randint(1, 100) <= other.dodgeProbability:
            print(f"{other.name} dodged the attack!")
            return False

        damage = self.damage
        if random.randint(1, 100) <= self.criticalHitProbability:
            damage *= 2
            print(f"Critical hit! {self.name} deals {damage} damage.")

        other.getHurt(damage)
        return True

    def getHurt(self, damage): 
        self.hp -= damage
        if self.hp <= 0:
            self.hp = 0
            print(f"{self.name} has been defeated.")
        else:
            print(f"{self.name} now has {self.hp} HP.")
    

class Wizard(Character):
    def __init__(self, name=None):
        super().__init__(name)
        self.setHp(150).setDamage(10).setDodgeProbability(40).setCriticalHitProbability(30)

    def powerUp(self, other):
        if self.boosted:
            print(f"{self.name} is already boosted.")
            return
        else:
            self.boosted = True
            self.setHp(self.hp * 1.5)
            other.setHp(other.hp / 1.5)
            print(f"{self.name} has been boosted! HP increased to {self.hp}.")
            print(f"{other.name} has been weakened! HP decreased to {other.hp}.")
        

class Warrior(Character):
    def __init__(self, name=None):
        super().__init__(name)
        self.setHp(150).setDamage(15).setDodgeProbability(30).setCriticalHitProbability(40)

    def powerUp(self, other):
        if self.boosted:
            print(f"{self.name} is already boosted.")
            return
        else:
            self.boosted = True
            self.setDamage(self.damage * 1.5)
            other.setDamage(other.damage / 1.5)
            print(f"{self.name} has been boosted! Damage increased to {self.damage}.")
            print(f"{other.name} has been weakened! Damage decreased to {other.damage}.")
    
class Tank(Character):
    def __init__(self, name=None):
        super().__init__(name)
        self.setHp(210).setDamage(20).setDodgeProbability(20).setCriticalHitProbability(50)   

    def powerUp(self, other):
        if self.boosted:
            print(f"{self.name} is already boosted.")
            return
        else:
            self.boosted = True
            self.setCriticalHitProbability(self.criticalHitProbability * 1.5)
            other.setCriticalHitProbability(other.criticalHitProbability / 1.5)
            print(f"{self.name} has been boosted! Critical hit probability increased to {self.criticalHitProbability}.")
            print(f"{other.name} has been weakened! Critical hit probability decreased to {other.criticalHitProbability}.")

class Archer(Character):
    def __init__(self, name=None):
        super().__init__(name)
        self.setHp(120).setDamage(15).setDodgeProbability(50).setCriticalHitProbability(20)

    def powerUp(self, other):
        if self.boosted:
            print(f"{self.name} is already boosted.")
            return
        else:
            self.boosted = True
            self.setCriticalHitProbability(self.criticalHitProbability * 1.5)
            other.setCriticalHitProbability(other.criticalHitProbability / 1.5)
            print(f"{self.name} has been boosted! Critical hit probability increased to {self.criticalHitProbability}.")
            print(f"{other.name} has been weakened! Critical hit probability decreased to {other.criticalHitProbability}.")
            