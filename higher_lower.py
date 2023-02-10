from art import logo, vs
from game_data import data
import random

score = 0
while True:
    print(logo)

    rd = random.choice(data)
    rd_name = rd["name"]
    rd_description = rd["description"]
    rd_country = rd["country"]
    rd_followers = rd["follower_count"]

    print("******************************************************************")
    print(f"Compare A: {rd_name}, a {rd_description}, from {rd_country}")
    print("******************************************************************")

    print(vs)

    rdm = random.choice(data)
    rdm_name = rdm["name"]
    rdm_description = rdm["description"]
    rdm_country = rdm["country"]
    rdm_followers = rdm["follower_count"]

    print("******************************************************************")
    print(f"Compare B: {rdm_name}, a {rdm_description}, from {rdm_country}")
    print("******************************************************************")

    maxs = max(rd_followers, rdm_followers)
    mins = min(rd_followers, rdm_followers)

    users_choice = input("Who has more followers. 'A' or 'B':  ").upper()

    if users_choice == 'A' and maxs == rd_followers:
        score += 1
        print("##################################################################")
        print(f"Wawu!!! Ride on!!! Your score is {score}")
        print("##################################################################")
    elif users_choice == 'B' and maxs == rdm_followers:
        score += 1
        print("##################################################################")
        print(f"Wawu!!! Ride on!!! Your score is {score}")
        print("##################################################################")
    elif users_choice == 'A' and maxs != rd_followers:
        print("##################################################################")
        print(f"The game ends here for you! Your score is {score}")
        print("##################################################################")
        break
    elif users_choice == 'B' and maxs != rdm_followers:
        print("##################################################################")
        print(f"The game ends here for you! Your score is {score}")
        print("##################################################################")
        break
    else:
        print("##################################################################")
        print(f"option is out of reach,Your score is {score}")
        print("##################################################################")
        break
