import random
import time

#The opponents (food items)
class FoodFoes(object):

    def __init__(self, name, quality, amount):
        self.name = name
        self.quality = quality
        self.amount = amount

    def __repr__(self):
        return f"{self.amount} {self.quality} of {self.name}!"

#The player
class Hero(object):

    def __init__(self, name, size, title, score=0):
        self.name = name
        self.size = size
        self.title = title
        self.score = score

    def __str__(self):
        if self.size <= 3:
            stature = "small"
        elif self.size <= 7:
            stature = "average"
        else:
            stature = "hefty"
        return f"You're {self.title} {self.name} of {stature} size."

    def eat(self, FoodFoe):
        print(f'Risky! But, {FoodFoe.name} does look tasty!')
        time.sleep(1)

        playerroll = random.randint(1, 50) * self.size
        opproll = random.randint(1, 50) * FoodFoe.amount

        print(f"Looks like you can stomach {playerroll} {FoodFoe.quality} of {FoodFoe.name} this course...\n")
        time.sleep(2)
        print("The {2} fills you up by: {} {}!.\n".format(FoodFoe.name, opproll, FoodFoe.quality))
        time.sleep(1)

        if playerroll >= opproll:
            self.score += 20
            print(f"Yum, yum... {self.name} devoured the {FoodFoe.name}, what's next?!\n")
            time.sleep(1)
            return True
        else:
            print(f"Did you eat before this? Looks like the {FoodFoe.name} wasted you, {self.name}!\n")
            time.sleep(1)
            return False

#class has uppercase letter, argument doesn't