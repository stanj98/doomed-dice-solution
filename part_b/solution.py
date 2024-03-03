
def undoom_dice(die_A, die_B):
    """Returns a list of non-standard pairs of dice that have the same
    distribution of sums as a standard pair of dice."""

    if not die_A or not die_B:
        raise Exception("Provide input of standard dice to continue")
    
    standard_die = [1,2,3,4,5,6]
    if (die_A != standard_die) or (die_B != standard_die):
        raise Exception("Invalid input!. Provide input of standard dices to continue.")

    original_pair = (die_A, die_B)
    original_sums = sums_distribution(original_pair)
    matching_pairs = []
    all_possible_pairs = all_pairs(all_dice())
    for pair in all_possible_pairs:
        if (max(pair[0]) > 4):
            continue
        if (sums_distribution(pair) == original_sums) and (pair != original_pair):
            matching_pairs.append(pair)
    return matching_pairs

def all_pairs(dice):
    """Return all dice pairs (a, b) where a <= b (to not include (b,a) i.e. avoid duplicate permuations)"""

    all_pairs = []
    for a in dice:
        for b in dice:
            if a <= b:
                all_pairs.append((a, b))
    return all_pairs

def sums_distribution(pair):
    """All possible sums of a die A's side with die B's side. Sorting is performed to ignore 
    duplicates/permutations of a unique set."""

    sums = []
    for side_a in pair[0]:
        for side_b in pair[1]:
            sums.append(side_a + side_b)
    return sorted(sums)

def all_dice():
    """A list of all elements of a 6-sided dice."""

    all_dice = []
    for b in range(1,13):
        for c in range(b, 13):
            for d in range(c, 13):
                for e in range(d, 13):
                    for f in range(e, 13):
                        dice = [1,b,c,d,e,f]
                        all_dice.append(dice)
    return all_dice

try:
    die_A = die_B = [1,2,3,4,5,6]
    result = undoom_dice(die_A, die_B)
    assert len(sums_distribution((result[0]))) == 36
    new_die_A, new_die_B = result[0]
    print(f"\nNew Die A: {new_die_A} \nNew Die B: {new_die_B}\n")
except AssertionError:
    print("Error: Sums distribution does not match the expected length.")
except Exception as e:
    print(f"Error: {e}")