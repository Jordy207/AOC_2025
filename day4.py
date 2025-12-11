import os
import time

def puzzle_one(data):
    x_size = len(data[0])
    y_size = len(data)
    result = 0
    # papers = []
    for y, data_row in enumerate(data):
        for x in range(x_size):
            if data_row[x] == '@':
                papers_seen = -1
                nine_by_nine = list()
                if y > 0:
                    nine_by_nine.append(data[y-1][max(0, x-1):min(x_size, x+2)])
                nine_by_nine.append(data_row[max(0, x-1):min(x_size, x+2)])
                if y < y_size - 1:
                    nine_by_nine.append(data[y+1][max(0, x-1):min(x_size, x+2)])
                papers_seen += sum(nine_by_nine.count('@') for nine_by_nine in nine_by_nine)
                if papers_seen < 4:
                    result += 1
                    # papers.append((y, x))
    # for x,y in papers:
    #     data[x] = data[x][:y] + 'x' + data[x][y+1:]
    # print('\n'.join(''.join(row) for row in data))
    return result
              
def puzzle_two(data):
    pass

print("Running Day 4 solutions:")
with open(os.path.join("data_files", "day_4", "example.txt")) as f:
    data = [x.strip() for x in f.readlines()]
    start = time.time()
    print(f"Example puzzle one: {puzzle_one(data)}")
    print(f"Took {time.time() - start} seconds")

with open(os.path.join("data_files", "day_4", "puzzle_1.txt")) as f:
    data = [x.strip() for x in f.readlines()]
    start = time.time()
    print(f"Puzzle one: {puzzle_one(data)}")
    print(f"Took {time.time() - start} seconds")

with open(os.path.join("data_files", "day_4", "example.txt")) as f:
    data = [x.strip() for x in f.readlines()]
    start = time.time()
    print(f"Example puzzle two: {puzzle_two(data)}")
    print(f"Took {time.time() - start} seconds")

with open(os.path.join("data_files", "day_4", "puzzle_2.txt")) as f:
    data = [x.strip() for x in f.readlines()]
    start = time.time()
    print(f"Puzzle two: {puzzle_two(data)}")
    print(f"Took {time.time() - start} seconds")