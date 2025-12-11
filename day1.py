from math import ceil
import os

def puzzle_one(data):
    OPERATORS = {
        'R': lambda x, y: (x + y) % 100,
        'L': lambda x, y: (x - y) % 100,
    }
    current_point = 50 
    ret_val = 0
    for line in data:
        direction, value = line[0], int(line[1:])
        current_point = OPERATORS[direction](current_point, value)
        if current_point == 0:
            ret_val += 1
    return ret_val

def puzzle_two(data):
    def right_turn(start, distance):
        end = start + distance
        position = end % 100
        if end >= 100:
            extra_loops = (end) // 100
            return position, extra_loops
        return position, 0

    def left_turn(start, distance):
        end = start - distance
        position = end % 100
        extra_loops = 0
        if start == 0:
            extra_loops -= 1
        if end == 0:
            return position, 1
        if end < 0:
            return position, extra_loops + abs((-end + 100)// 100)
        return position, 0
        
    OPERATORS = {
        'R': lambda x, y: right_turn(x, y),
        'L': lambda x, y: left_turn(x, y),
    } 
    current_point = 50
    ret_val = 0
    for line in data:
        direction, distance = line[0], int(line[1:])
        current_point, extra_loops = OPERATORS[direction](current_point, distance)
        ret_val += extra_loops
    if current_point == 0:
        ret_val += 1
    return ret_val

print("Running Day 1 solutions:")

with open(os.path.join("data_files", "day_1", "example.txt")) as f:
    data = f.readlines()
    print(f"Example puzzle one: {puzzle_one(data)}")

with open(os.path.join("data_files", "day_1", "puzzle_1.txt")) as f:
    data = f.readlines()
    print(f"Puzzle one: {puzzle_one(data)}")

with open(os.path.join("data_files", "day_1", "example.txt")) as f:
    data = f.readlines()
    print(f"Example puzzle two: {puzzle_two(data)}")

with open(os.path.join("data_files", "day_1", "puzzle_2.txt")) as f:
    data = f.readlines()
    print(f"Puzzle two: {puzzle_two(data)}")