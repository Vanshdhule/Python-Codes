import random

game_matrix = {
    'Snake': {'Snake': 'Draw', 'Water': 'Player', 'Gun': 'Com'},
    'Water': {'Snake': 'Com', 'Water': 'Draw', 'Gun': 'Player'},
    'Gun': {'Snake': 'Player', 'Water': 'Com', 'Gun': 'Draw'}
}

options = ("Snake", "Water", "Gun")

player_choice = input("Snake, Water, Gun: ").capitalize()
print("Player:", player_choice)

com_choice = random.choice(options)
print("Com:", com_choice)

result = game_matrix[player_choice][com_choice]

if result == 'Draw':
    print("It's a draw!")
elif result == 'Player':
    print("Player wins!")
elif result == 'Com':
    print("Com wins!")

        


        

  