import random as r


def main():
    dice_roll = 2
    dice_sum = 0
    for i in range(0, dice_roll):
        roll = r.randint(1, 6)
        dice_sum += roll
        print(f'You rolled a {roll}')
    print(f'Your total is --> {dice_sum}')


if __name__ == "__main__":
    main()
