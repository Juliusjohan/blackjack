from player import Player

STARTING_BALANCE = 500

player_name = str(input("Enter your name: "))
p1 = Player(player_name, STARTING_BALANCE)
print(f"Hello {player_name}, you will start with ${STARTING_BALANCE}.")