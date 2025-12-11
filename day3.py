import os
from itertools import combinations
import time

def puzzle_one(data):
    # result = 0
    return sum([max(int(''.join(i)) for i in combinations(battery_bank.strip(), 2)) for battery_bank in data])
    # for battery_bank in data:
    #     values = battery_bank.strip()
    #     max_val = max(int(''.join(i)) for i in combinations(values, 2))
    #     print(f"Max value for bank {values} is {max_val}")
    #     result += max_val
    # return result

def puzzle_two(data):
    # Combinations of 12 from each battery bank is way too slow when each bank has 100 digits.
    # return sum([max(int(''.join(i)) for i in combinations(battery_bank.strip(), 12)) for battery_bank in data])
    ### vvvv I peeked at the solution vvvv ###
    result = 0
    for battery_bank in data:
        res_jolt = list()
        start_idx = 0
        battery_bank = battery_bank.strip()
        for _ in range(12):
            can_skip = len(battery_bank) - start_idx - (12 - len(res_jolt))
            search_space = battery_bank[start_idx:start_idx + can_skip + 1]
            max_jolt = max(search_space)
            best_pos = start_idx + search_space.index(max_jolt)
            res_jolt.append(max_jolt)
            start_idx = best_pos + 1
        result += int(''.join(res_jolt))

    return result
    
print("Running Day 3 solutions:")
with open(os.path.join("data_files", "day_3", "example.txt")) as f:
    data = f.readlines()
    start = time.time()
    print(f"Example puzzle one: {puzzle_one(data)}")
    print(f"Took {time.time() - start} seconds")

with open(os.path.join("data_files", "day_3", "puzzle_1.txt")) as f:
    data = f.readlines()
    start = time.time()
    print(f"Puzzle one: {puzzle_one(data)}")
    print(f"Took {time.time() - start} seconds")

with open(os.path.join("data_files", "day_3", "example.txt")) as f:
    data = f.readlines()
    start = time.time()
    print(f"Example puzzle two: {puzzle_two(data)}")
    print(f"Took {time.time() - start} seconds")

with open(os.path.join("data_files", "day_3", "puzzle_2.txt")) as f:
    data = f.readlines()
    start = time.time()
    print(f"Puzzle two: {puzzle_two(data)}")
    print(f"Took {time.time() - start} seconds")