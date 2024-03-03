
def total_die_combinations():
    """Outputs total combinations available when combining two Dices"""

    #initialize dice A and B values using a list
    dice_a = dice_b = [1, 2, 3, 4, 5, 6]

    #to get the total combinations - multiply length of dice A and dice B
    dice_a_len = len(dice_a)
    dice_b_len = len(dice_b)

    #print result
    print(f"Total possible combinations: {dice_a_len * dice_b_len}")

total_die_combinations()

