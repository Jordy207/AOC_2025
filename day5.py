import os
import time

def puzzle_one(data):
    blank_line_idx = data.index("")
    ranges = data[:blank_line_idx]
    to_check = data[blank_line_idx + 1:]
    
    result = 0
    for line in to_check:
        number = int(line.strip())
        for range_pair in ranges:
            start, end = map(int, range_pair.split("-"))
            if start <= number <= end:
                result += 1
                break

    return result

def puzzle_two(data):
    blank_line_idx = data.index("")
    ranges = data[:blank_line_idx]

    ranges = [(int(range_pair[0]), int(range_pair[1])) for range_pair in (range_pair.split("-") for range_pair in ranges)]
    ranges = sorted(ranges)
    result = 0
    current_start, current_end = ranges[0]

    #|---|
    #  |-------|
    #     |---|
    for start, end in ranges[1:]:
        if start <= current_end <= end:
            current_end = end
        elif current_end < start:
            result += current_end - current_start + 1
            current_start, current_end = start, end
    return result + (current_end - current_start + 1)
         

print("Running Day 5 solutions:")
print("Solving puzzle one example:")
with open(os.path.join("data_files", "day_5", "example.txt")) as f:
    data = f.readlines()
    data = [x.strip() for x in data]
    start = time.time()
    print(f"Example puzzle one: {puzzle_one(data)}")
    print(f"Took {time.time() - start} seconds")

print("-----")
print("Solving puzzle one:")
with open(os.path.join("data_files", "day_5", "input.txt")) as f:
    data = f.readlines()
    data = [x.strip() for x in data]
    start = time.time()
    print(f"Puzzle one: {puzzle_one(data)}")
    print(f"Took {time.time() - start} seconds")

print("-----")
print("Solving puzzle two example:")
with open(os.path.join("data_files", "day_5", "example.txt")) as f:
    data = f.readlines()
    data = [x.strip() for x in data]
    start = time.time()
    print(f"Example puzzle two: {puzzle_two(data)}")
    print(f"Took {time.time() - start} seconds")

print("-----")
print("Solving puzzle two:")
with open(os.path.join("data_files", "day_5", "input.txt")) as f:
    data = f.readlines()
    data = [x.strip() for x in data]
    start = time.time()
    print(f"Puzzle two: {puzzle_two(data)}")
    print(f"Took {time.time() - start} seconds")