dict = {'Ade': 10, 'Wale': 15, 'John': 20, 'Qudus': 16}
player_name = input("Enter a player name: ").title()

for player in dict:
    if player == player_name:
        print(dict[player])
        break
else:
    print(f"No player named {player_name} found.")
