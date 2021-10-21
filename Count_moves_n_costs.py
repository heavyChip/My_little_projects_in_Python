# Desired position
dp = (1, 2, 3, 4, 5)

# Actual position
ap = [4, 5, 1, 2, 3]

# Move costs of elements in ap (energy costs)
mc = [100, 300, 200, 450, 600]


def count_moves_n_costs(desired_position, actual_position, moving_cost):
    """
    Function which counts number and costs of necessary moves
    to achieve by numbers (in ap) a desire position (dp).
    """

    # 1. PREPARING SECTION

    # Simple checking if counting is necessary
    if tuple(actual_position) == desired_position:
        print('Numbers are in right positions.')
        return

    # Checking len of elements in positions
    if len(actual_position) != len(desired_position):
        print('You need more or less elements in positions.')
        return

    # Checking type of values in both positions (Should be the same!)
    if set(desired_position).difference(set(actual_position)):
        print('Problem with the numbers in actual position. Must exit.')
        return

    desire_position_li = list(desired_position)
    actual_position_bool = []
    c = 0

    # Creating boolean list in order to know which numbers are on desired positions.
    for item in actual_position:
        if item == desire_position_li[c]:
            actual_position_bool.append(True)
            c += 1
        else:
            actual_position_bool.append(False)
            c += 1

    # 2. MAIN
    # Checking numbers, counting moves and costs, moving numbers to the right positions

    c2 = 0
    all_moves = 0
    energy_sum = 0

    for item in actual_position_bool:

        # Checking numbers place

        if item:
            c2 += 1
            # print('Number is on the right place.')
            continue

        elif actual_position[c2] == desire_position_li[c2]:
            c2 += 1
            actual_position_bool[item] = True
            # print('This number is already in place. I\'ve caught this!\n')
            continue

        else:
            temp = actual_position[c2]

            # Searching desired number to position,
            # taking of it index and index of this number in actual position
            num_which_should_be_in_this_position = desired_position[c2]
            num_which_should_be_in_this_position_index = desired_position.index(num_which_should_be_in_this_position)
            desired_number_index = actual_position.index(num_which_should_be_in_this_position)

            # Counting moves and costs of it
            moves_needed = desired_number_index - num_which_should_be_in_this_position_index
            energy_costs = moving_cost[c2] + moving_cost[desired_number_index]
            all_moves += moves_needed
            energy_sum += energy_costs

            # Printing for view
            print(f'Position before moving : {actual_position}')
            print(f'Needed moves : {moves_needed}')
            print(f'Move(s)/Energy costs : {energy_costs}')

            # Moving numbers and when done setting bool to True
            actual_position[c2] = desired_position[num_which_should_be_in_this_position_index]
            actual_position_bool[c2] = True
            actual_position[desired_number_index] = temp
            print(f'Position after moving : {actual_position}\n')
            c2 += 1
            continue

    # return actual_position, all_moves, energy_sum
    return f"Finished!\nIt took {all_moves} moves and {energy_sum} energy."


cmnc = count_moves_n_costs(dp, ap, mc)
print(cmnc)
