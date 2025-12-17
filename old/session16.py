class Sprite:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def move(self):
        print(f"{self.name} is moving")

class Player(Sprite):
    def __init__(self, name, color, heart):
        super().__init__(name, color)
        self.heart = heart
        
    def jump(self):
        print(f"{self.name} is jumping")

class Enemy(Sprite):
    def __init__(self, name, color, bullet):
        super().__init__(name, color)
        self.bullet = bullet
        
    def attack(self):
        print(f"{self.name} is attacking")

mario = Player("mario", "red", 10)
mario.move()
mario.jump()


e1 = Enemy("e1", "black", 4)
e1.move()
e1.attack()