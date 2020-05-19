import random as r


def main():
    dice_roll = int(input('How many dice would you like to roll: '))
    dice_sum = 0
    for i in range(0, dice_roll):
        roll = r.randint(1, 6)
        dice_sum += roll
        if roll == 1:
            print(f'You rolled a {roll}! Critical low')
        elif roll == 6:
            print(f'You rolled a {roll}! High roll!')
        else:
            print(f'You rolled a {roll}')
    print(f'Your total is --> {dice_sum}')


if __name__ == "__main__":
    main()
