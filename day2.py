import math
import os
import time 

def puzzle_one(data):
    invalid_ids = set()
    for id_range in data:
        start_id, end_id = id_range.split('-')
        for i in range(int(start_id), int(end_id) + 1):
            str_id = str(i)
            if len(str_id) % 2 != 0:
                continue
            first_half = str_id[:len(str_id)//2]
            second_half = str_id[len(str_id)//2:]
            if first_half == second_half:
                invalid_ids.add(i)
    return sum(invalid_ids)

def puzzle_two(data):
    def divisorGenerator(n):
        large_divisors = []
        for i in range(1, int(math.sqrt(n) + 1)):
            if n % i == 0:
                yield i
                if i*i != n:
                    large_divisors.append(n / i)
        for divisor in reversed(large_divisors):
            yield divisor

    invalid_ids = set()
    for id_range in data:
        start_id, end_id = id_range.split('-')

        divisors = dict()
        for i in range(int(start_id), int(end_id) + 1):
            str_id = str(i)
            if len(str_id) not in divisors:
                divisors[len(str_id)] = list(divisorGenerator(len(str_id)))
            divisors_string = list(divisors[len(str_id)])
            del divisors_string[0]  # remove 1
            for divisor in divisors_string:
                parts_divisor = list()
                for part in range(int(divisor)):
                    idx_start = part*int(len(str_id)/divisor)
                    idx_end = (part+1)*int(len(str_id)/divisor)
                    parts_divisor.append(str_id[idx_start:idx_end])
                if all(x == parts_divisor[0] for x in parts_divisor):
                    invalid_ids.add(i)
    return sum(invalid_ids)

with open(os.path.join("data_files", "day_2", "example.txt")) as f:
    data = f.readline().split(',')
    print(f"Example puzzle one: {puzzle_one(data)}")

with open(os.path.join("data_files", "day_2", "puzzle_1.txt")) as f:
    data = f.readline().split(',')
    start = time.time()
    print(f"Puzzle one: {puzzle_one(data)}")
    end = time.time()
    print(f"Time taken: {end - start} seconds my 1")

with open(os.path.join("data_files", "day_2", "example.txt")) as f:
    data = f.readline().split(',')
    print(f"Example puzzle two: {puzzle_two(data)}")

with open(os.path.join("data_files", "day_2", "puzzle_2.txt")) as f:
    data = f.readline().split(',')
    start = time.time()
    print(f"Puzzle two: {puzzle_two(data)}")
    end = time.time()
    print(f"Time taken: {end - start} seconds my 2")