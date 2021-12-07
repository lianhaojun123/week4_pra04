import random


def main():
    num_picks = int(input("How many quick picks?"))
    for i in range(num_picks):
        picks = []
        for x in range(6):
            picks.append(random.randint(1, 45))
        picks.sort()
        print(f"{picks[0]:2} {picks[1]:2} {picks[2]:2} {picks[3]:2} {picks[4]:2} {picks[5]:2}")


main()
