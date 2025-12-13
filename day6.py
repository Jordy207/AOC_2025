import os
import time

def puzzle_one(data):
    OPERATIONS = {'+': sum,
                  '*': lambda x: eval('*'.join(map(str, x))),
    }
    num_cols = len(data[0].split())
    cols = []
    for i in range(num_cols):
        col = [int(row.split()[i]) for row in data[:-1]]
        cols.append(col)
    
    result = 0

    operations_given = data[-1].split()
    for idx, col in enumerate(cols):
        op = operations_given[idx]
        result += OPERATIONS[op](col)

    return result

def puzzle_two(data):
    OPERATIONS = {'+': sum,
                  '*': lambda x: eval('*'.join(map(str, x))),
    }

    # print(data)
    current_col = []
    cols = []
    for small_col in range(len(data[0]), 0, -1):
        same_col = False
        current_num = ''
        for row in data[:-1]:
            # print(row, small_col, same_col)
            if row[small_col-1] != ' ':
                current_num += row[small_col-1]
                same_col = True
        # print(current_num, same_col)
        if same_col:
            current_col.append(int(current_num))
        else:
            cols.append(current_col)
            current_col = []
        # print(current_col, cols)
    cols.append(current_col)
    # print(cols)
    operations_given = list(reversed(data[-1].split()))
    result = 0
    for idx, col in enumerate(cols):
        op = operations_given[idx]
        # print(col, op)
        result += OPERATIONS[op](col)

    return result


print("Running Day 6 solutions:")
print("Solving puzzle one example:")
with open(os.path.join("data_files", "day_6", "example.txt")) as f:
    data = f.readlines()
    data = [x.strip() for x in data]
    start = time.time()
    print(f"Example puzzle one: {puzzle_one(data)}")
    print(f"Took {time.time() - start} seconds")

print("-----")
print("Solving puzzle one:")
with open(os.path.join("data_files", "day_6", "input.txt")) as f:
    data = f.readlines()
    data = [x.strip() for x in data]
    start = time.time()
    print(f"Puzzle one: {puzzle_one(data)}")
    print(f"Took {time.time() - start} seconds")

print("-----")
print("Solving puzzle two example:")
with open(os.path.join("data_files", "day_6", "example.txt")) as f:
    data = f.readlines()
    data = [x.rstrip("\n") for x in data]
    start = time.time()
    print(f"Example puzzle two: {puzzle_two(data)}")
    print(f"Took {time.time() - start} seconds")

print("-----")
print("Solving puzzle two:")
with open(os.path.join("data_files", "day_6", "input.txt")) as f:
    data = f.readlines()
    data = [x.rstrip("\n") for x in data]
    start = time.time()
    print(f"Puzzle two: {puzzle_two(data)}")
    print(f"Took {time.time() - start} seconds")