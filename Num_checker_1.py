import re

def show_differences_between_sets():
    # Function returns (in a set) differences between two sets of numbers

    pattern_sett = set(list(range(11)))
    #pattern_sett = {0,1,2,3,4,5,6,7,8,9,10}
    temp_entered_numbers = input("Enter numbers from 0 to 10 in order to create a set: ")

    pattern = re.compile(r"(10|[0-9])")
    temp_entered_numbers = pattern.findall(temp_entered_numbers)

    entered_numbers_sett = set(map(int, temp_entered_numbers))
    #print(entered_numbers_sett)

    differences_sett = pattern_sett.difference(entered_numbers_sett)
    #print(list(differences_sett))

    return differences_sett

show_differences_between_sets()
