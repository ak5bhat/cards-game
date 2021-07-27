# This is a two player game where each player picks up the top most card 
# and will win that round if he/she has the highest number. 
# The deck will be shuffled to have a fair play.
# Total 10 round game. The maximum point holder wins.

import random

#Game variables:
deck = 10
p_won_score = (deck/2) +1 

class Person:
    count =0
    def __init__(self, name):
        self.name = name
        self.points = 0
        self.cards = list(range(1,deck +1,1))
        
        random.shuffle(self.cards)
        
    def pick_card(self):
        picked_card = self.cards[0]
        self.cards.remove(picked_card)
        
        print(f"{self.name} card is {picked_card}")
        return picked_card
    
    def add_point(self):
        self.points +=1
        print(f'A point has been added to {self.name}')
        
    def is_game_over(self):
        return len(self.cards) == 0 or self.points == p_won_score  # making dynamic ; here p_won_score will be 6
        
        
p1 = Person("Player 1")

p2 = Person("Player 2")

print("Game Starts...\n--------------------------")
while True:
    input("Press Enter to pick a card!")
    Person.count += 1
    print(f"\nGAME {Person.count}")
    
    p1_card = p1.pick_card()
    p2_card = p2.pick_card()
    if p1_card > p2_card:
        p1.add_point()
    elif p2_card > p1_card:
        p2.add_point()
    else:
        print("TIE!")
    
    if  p1.is_game_over() or p2.is_game_over():
        print("\nGame Over!!")
        if p1.points> p2.points:
            print(f"{p1.name} Wins!")
        elif p2.points > p1.points:
            print(f"{p2.name} Wins!")
        else:
            print("Score is tie!\nIts a Draw!")
        
        print(f"Final Score: {p1.points} - {p2.points}")
        break
    
    print(f"Score: {p1.points} - {p2.points}")
        
        