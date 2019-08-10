import time
import random
from rpgclasses import Hero, FoodFoes


def main():
    intro()
    gameplay()


# Print the welcome message, and wait for input to start the game.
def intro():

    print("""
----------------------------------------------------
------------ Welcome to BIG Buffet RPG! ------------
----------------------------------------------------

Ahoy there! You've stumbled into a delicious looking
buffet. But, only time will tell if you're going to 
walk out a victor, or leave your food unfinished...

    - to play, press [enter]
    - for instructions, press [i]
    - to quit, press, press [q]

-----------------------------------------------------
    """)

    start = input('You:')

    if start == 'q':
        quit()
    
    elif start == 'i':
        print('''
            
-----------------------------------------------------
To play, you will meet a series of tasty, but filling
courses. You'll need to decide whether to collect 
points, by choosing to [e]at, or to not risk filling
up, by pressing [s]kip. 

If you [e]at, you will be pitted against the dish,
and a chance score will be rolled for both you and
the dish. 

The goal is to get the highest score possible! (duh)

Good luck! (You'll need it)...
-----------------------------------------------------

            ''')
        time.sleep(3)
        input("Press enter to continue.")
        pass
#It would be cool to add a loop here so that this functions like a menu.

    else:
        print(f"Great. Let's get started...\n")
        time.sleep(1)
        pass

# Main gameplay
def gameplay():
    # Define the "Opponents" - in this case food items...
    menuitems = [
        FoodFoes('burger', 'bites', 2),
        FoodFoes('pizza', 'bites', 5),
        FoodFoes('chips', 'plates', 11),
        FoodFoes('chicken wings', 'bites', 9),
        FoodFoes('milkshake', 'gulps', 4),
        FoodFoes('taco', 'bites', 7),
        FoodFoes('salad', 'tosses', 1),
        FoodFoes('plates of spaghetti', 'swirls', 8),
        FoodFoes('brownie', 'bites', 14),
        FoodFoes('ice cream', 'scoops', 7),
        FoodFoes('soup', 'bowls', 6),
        FoodFoes('soda', 'gulps', 8)
    ]
#It would be cool to have a large list of items, and then each new game generates menuitems as a random choice of 10 from the larger set.

    # Gather the player information.
    print('So it begins! To start, some details about you!\n')
    time.sleep(1)

    hero = Hero(
        input("What is your name brave soul: "),
        # The size indicates the difficulty level
        int(input("How large are you, on a scale of 1-10? (The larger you are, the easier the game): ")),
        input("What is your title? ")
    )

    print(f"Thank you {hero.title} {hero.name} the {hero.size}/10")
    time.sleep(1)

    # Difficulty easter eggs for the hardest and easiest difficulties
    if hero.size >= 8:
        print(f"Wow, you're a hefty one. eh?\n")
        time.sleep(1)
    elif hero.size <= 3:
        print(f"Not so big, eh? Brave one you are..\n")
        time.sleep(1)

    print("Let's get ready to chow down!\n")
    print('3...')
    time.sleep(1)
    print('2...')
    time.sleep(1)
    print('1...')
    time.sleep(1)

    #Gameplay
    i = 1

    while True:
        currentfood = random.choice(menuitems)
        print(f"\nHere comes course {i}! \nLook's like it's {currentfood}!\n")
        i += 1
        time.sleep(1)
        action = input("Are you going to [e]at it, [s]kip it, or [c]heck which items are left?\n")

        while action not in ['e', 's', 'c', 'q']:
            print(
                "Oops, that's not valid. Please choose [e] to eat, [s] to skip, [c] to check menu. \n To quit use [q]\n")
            time.sleep(1)
            action = input("Are you going to [e]at that, [s]kip it, or [c]heck the menu?\n")

        if action == 'e':
            if hero.eat(currentfood):
                menuitems.remove(currentfood)
                print(f"Your current score is {hero.score}")
            else:
                print(f"Better luck next time, maybe try sitting at the kid's table!\n")
                time.sleep(1)
                if hero.score >= 50:
                    print(f"Looks like you managed to score {hero.score}.. not too shabby!")
                    time.sleep(1)
                    
                    restart = input(f"{hero.name}, would you like to try again? (y/n)")
                    if restart == 'y':
                        i = 1
                        hero.score = 0
                        print(f"Quick stretch {hero.name}, here we go again!")
                        time.sleep(1)
                        pass
                    else:
                        quit()

                else:
                    print(f"Looks like you sored {hero.score}... yikes!")
                    time.sleep(1)

                    restart = input(f"{hero.name}, would you like to try again? (y/n)")
                    if restart == 'y':
                        i = 1
                        hero.score = 0
                        print(f"Quick stretch {hero.name}, here we go again!")
                        time.sleep(2)
                        pass
                    else:
                        quit()

        elif action == 's':
            print('Good call, that looked like quite filling!\n')
            menuitems.remove(currentfood)
            time.sleep(1)

        elif action == 'c':
            print(f"A little peak behind the counter... and ohhh gosh.. {hero.name} sees: \n")
            time.sleep(1)
            for FoodFoe in menuitems:
                print(f"- {FoodFoe} \n")
            input("Press enter to continue\n")
            pass

        elif action == 'q':
            print(f"For the best {hero.name}... this wasn't for the weak hearted anyways.\n")
            time.sleep(1)
            break


if __name__ == '__main__':
    main()

'''
possible addition ideas:

more foods on list.
iron out the probabilities + difficulty system.
highscore storage? 

'''
