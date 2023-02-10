import random

from art import logo, vs
from game_data import data

score = 0

while True:
    sorry = "Sorry, you lose!!!"
    option = "Option not available"
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
        print(f"Wawu!!! You have {score} point")
    elif users_choice == 'B' and maxs == rdm_followers:
        score += 1
        print(f"Wawu!!! You have {score} point")
    elif users_choice == 'A' and maxs != rd_followers:
        print(sorry,"Your total score is",score)
        break
    elif users_choice == 'B' and maxs != rdm_followers:
        print(sorry,"Your total score is",score)
        break
    else:
        print(option)
