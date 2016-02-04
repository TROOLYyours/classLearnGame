'''
class Cat:
    def __init__(self):
        self.y = 5
        self.purr()
    def purr(self):
        print(purr)
'''






 
class Hero:
    def __init__(self, name):
        self.name = name + ", " + input("insert additional title to name:")
        self.hp = 50

    def eat(self, food):
        
        if (food == 'apple'):
            self.hp += 12
        elif (food == 'steak'):
            self.hp += 16
        elif food == 'nothing':
            self.hp += 0
        else:
            self.hp -= 5

        if self.hp > 100:
            self.hp = 100 



char = Hero(input('what is your name?:'))

print()
print("Why hello there " + str(char.name))
print()

char.eat(input('what food do you want to eat?:'))

print()
print('okay then ' + str(char.name))
print('current hp level: ' + str(char.hp))



















