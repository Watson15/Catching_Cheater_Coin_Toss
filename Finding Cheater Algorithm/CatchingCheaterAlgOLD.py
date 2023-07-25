import math


def calculate_binomial_coefficient(n, heads):
    if heads > n or heads < 0:
        return 0
    return math.factorial(n) /( (math.factorial(heads) * math.factorial(n - heads)))


def calculate_runs():
    p_cheater = 0.75 #probability cheaters get heads
    p_non_cheater = 0.5 #probability non cheaters get heads
    target_cheaters_ratio = 0.8 #percentage of cheaters caught
    max_false_positives_ratio = 0.05 #accuse fewer then this percentage of players


    num_runs = 1
    heads = 1
    Cumulative_cheat = 0
    Cumulative_not_cheat = 0
    #probability cheater flips heads number of heads on num_runs number of flips
    prob_cheaters = calculate_binomial_coefficient(num_runs, heads) * (p_cheater ** heads) * ((1 - p_cheater) ** (num_runs - heads))
    #probability non cheater flips heads number of heads on num_runs number of flips
    prob_non_cheaters = calculate_binomial_coefficient(num_runs, heads) * (p_non_cheater ** heads) * ((1 - p_non_cheater) ** (num_runs - heads))
    #checks if the identified cheaters ratio and false positives ratio meet the requirements
    while(Cumulative_cheat < target_cheaters_ratio or Cumulative_not_cheat > max_false_positives_ratio):
        prob_cheaters = calculate_binomial_coefficient(num_runs, heads) * (p_cheater ** heads) * ((1 - p_cheater) ** (num_runs - heads))
        Cumulative_cheat += prob_cheaters
        prob_non_cheaters = calculate_binomial_coefficient(num_runs, heads) * (p_non_cheater ** heads) * ((1 - p_non_cheater) ** (num_runs - heads))
        Cumulative_not_cheat += prob_non_cheaters


    if (heads)<(num_runs/2):
        #increase number of coin tosses/flips and resets other variables
        num_runs += 1
        heads = num_runs
        Cumulative_not_cheat=0
        Cumulative_cheat=0
    else:
        #Decrease the number of heads flipped by cheaters and non-cheaters in the next run
        heads-=1
    #print out our final values
    #Note: This is done in an older version of Python. Newer Versions of Python you can #write a print statement as: print(f”Variable: {variable}"), not needing the .format()
    print("Cumulative Probability Cheating: {}".format(Cumulative_cheat*100)+"%")
    print("Cumulative Probability Not Cheating: {}".format(Cumulative_not_cheat*100)+"%")
    print("If the player tosses the coin: {}".format(num_runs)+ " times and flips: {}".format(heads+1)+" or more heads then they are cheating")


calculate_runs()
