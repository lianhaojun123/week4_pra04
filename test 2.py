import random


def main():
    get_pick()


def get_pick():
    picks = []
    num_picks = int(input("How many quick picks ?"))
    for i in range(num_picks):
        for x in range(6):
            picks.append(random.randint(1, 45))



main()
