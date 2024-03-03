
def compute_standard_die_sum_and_frequencies():
    """Outputs sum and respective frequencies available within the probability distribution"""

    #initialize dice A and B values using a list
    dice_a = dice_b = [1, 2, 3, 4, 5, 6]

    #sample space
    print("Sample Space:")
    for a_val in dice_a:
        for b_val in dice_b:
            print(f"({a_val}, {b_val})", end = "\t")
        print("\n")

    #obtain the distribution of potential sums
    distribution = {}
    
    for dice_a_val in range(1, 7):
        for dice_b_val in range(1, 7):
            sum_val = dice_a_val + dice_b_val
            distribution[sum_val] = distribution[sum_val] + 1 if sum_val in distribution else 1
    
    #output the sum and its occurences from distribution
    for val, occurrences in distribution.items():
        print(f"Val: {val}, \tOccurrences: {occurrences}")


compute_standard_die_sum_and_frequencies()
    