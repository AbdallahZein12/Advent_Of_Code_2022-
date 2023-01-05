with open('day2.in') as file:
    rounds = [i for i in file.read().strip().split("\n")]
    

    outcomes = {
        'A X':4, 'A Y':8, 'A Z':3, 'B X':1, 'B Y':5, 'B Z':9, 'C X':7, 'C Y':2, 'C Z':6
    }

    total_points = 0 

    for i in rounds:
      total_points += outcomes[i]

    print(f"P1: {total_points}")

    p2_outcomes = {
        'A X':3, 'A Y':4, 'A Z':8, 'B X':1, 'B Y':5, 'B Z':9, 'C X':2, 'C Y':6, 'C Z':7
    }

    t_2 = 0 

    for round in rounds:
      t_2 += p2_outcomes[round]

    print(f"P2: {t_2}")

    
    

    


