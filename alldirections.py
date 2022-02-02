import random
import matplotlib.pyplot as plt


def simulate():
    y1, y2, x = [], [], []
    arr = initialise_array()
    rows, cols = len(arr), len(arr[0])
    it, reward1, reward2, a, b, c, d = 0, 0, 0, 0, 0, rows - 1, cols - 1
    directions = ["E", "W", "N", "S", "NE", "NW", "SE", "SW"]
    one, two = 0, 0
    while not (arr[rows-1][cols-1] == 1 and arr[0][0] == 2):
        if not (a == rows - 1 and b == cols - 1):
            d1 = random.choice(directions)
            if d1 == "E" and b < cols - 1:
                if arr[a][b+1] == 2:
                    reward1 -= 10
                else:
                    arr[a][b+1] = 1
                    arr[a][b] = 0
                    b += 1
                    if not two:
                        reward1 += 5
                    else:
                        reward1 -= 5
            elif d1 == "W" and b > 0:
                if arr[a][b-1] == 2:
                    reward1 -= 10
                else:
                    arr[a][b-1] = 1
                    arr[a][b] = 0
                    b -= 1
                    if not two:
                        reward1 += 1
                    else:
                        reward1 -= 1
            elif d1 == "N" and a > 0:
                if arr[a-1][b] == 2:
                    reward1 -= 10
                else:
                    arr[a-1][b] = 1
                    arr[a][b] = 0
                    a -= 1
                    if not two:
                        reward1 += 1
                    else:
                        reward1 -= 1
            elif d1 == "S" and a < rows - 1:
                if arr[a+1][b] == 2:
                    reward1 -= 10
                else:
                    arr[a+1][b] = 1
                    arr[a][b] = 0
                    a += 1
                    if not two:
                        reward1 += 5
                    else:
                        reward1 -= 5
            elif d1 == "NE" and a > 0 and b < cols - 1:
                if arr[a-1][b+1] == 2:
                    reward1 -= 10
                else:
                    arr[a-1][b+1] = 1
                    arr[a][b] = 0
                    a -= 1
                    b += 1
                    if not two:
                        reward1 += 1
                    else:
                        reward1 -= 1
            elif d1 == "NW" and a > 0 and b > 0:
                if arr[a-1][b-1] == 2:
                    reward1 -= 10
                else:
                    arr[a-1][b-1] = 1
                    arr[a][b] = 0
                    a -= 1
                    b -= 1
                    if not two:
                        reward1 += 1
                    else:
                        reward1 -= 1
            elif d1 == "SE" and a < rows - 1 and b < cols - 1:
                if arr[a+1][b+1] == 2:
                    reward1 -= 10
                else:
                    arr[a+1][b+1] = 1
                    arr[a][b] = 0
                    a += 1
                    b += 1
                    if not two:
                        reward1 += 5
                    else:
                        reward1 -= 5
            elif d1 == "SW" and a < rows - 1 and b > 0:
                if arr[a+1][b-1] == 2:
                    reward1 -= 10
                else:
                    arr[a+1][b-1] = 1
                    arr[a][b] = 0
                    a += 1
                    b -= 1
                    if not two:
                        reward1 += 1
                    else:
                        reward1 -= 1
        else:
            one = 1
        if not (c == 0 and d == 0):
            d2 = random.choice(directions)
            if d2 == "E" and d < cols - 1:
                if arr[c][d + 1] == 1:
                    reward2 -= 10
                else:
                    arr[c][d + 1] = 2
                    arr[c][d] = 0
                    d += 1
                    if not one:
                        reward2 += 1
                    else:
                        reward2 -= 1
            elif d2 == "W" and d > 0:
                if arr[c][d - 1] == 1:
                    reward2 -= 10
                else:
                    arr[c][d - 1] = 2
                    arr[c][d] = 0
                    d -= 1
                    if not one:
                        reward2 += 5
                    else:
                        reward2 -= 5
            elif d2 == "N" and c > 0:
                if arr[c - 1][d] == 1:
                    reward2 -= 10
                else:
                    arr[c - 1][d] = 2
                    arr[c][d] = 0
                    c -= 1
                    if not one:
                        reward2 += 5
                    else:
                        reward2 -= 5
            elif d2 == "S" and c < rows - 1:
                if arr[c + 1][d] == 1:
                    reward2 -= 10
                else:
                    arr[c + 1][d] = 2
                    arr[c][d] = 0
                    c += 1
                    if not one:
                        reward2 += 1
                    else:
                        reward2 -= 1
            elif d2 == "NE" and c > 0 and d < cols - 1:
                if arr[c - 1][d + 1] == 1:
                    reward2 -= 10
                else:
                    arr[c - 1][d + 1] = 2
                    arr[c][d] = 0
                    c -= 1
                    d += 1
                    if not one:
                        reward2 += 1
                    else:
                        reward2 -= 1
            elif d2 == "NW" and c > 0 and d > 0:
                if arr[c - 1][d - 1] == 1:
                    reward2 -= 10
                else:
                    arr[c - 1][d - 1] = 2
                    arr[c][d] = 0
                    c -= 1
                    d -= 1
                    if not one:
                        reward2 += 5
                    else:
                        reward2 -= 5
            elif d2 == "SE" and c < rows - 1 and d < cols - 1:
                if arr[c + 1][d + 1] == 1:
                    reward2 -= 10
                else:
                    arr[c + 1][d + 1] = 2
                    arr[c][d] = 0
                    c += 1
                    d += 1
                    if not one:
                        reward2 += 1
                    else:
                        reward2 -= 1
            elif d2 == "SW" and c < rows - 1 and d > 0:
                if arr[c + 1][d - 1] == 1:
                    reward2 -= 10
                else:
                    arr[c + 1][d - 1] = 2
                    arr[c][d] = 0
                    c += 1
                    d -= 1
                    if not one:
                        reward2 += 1
                    else:
                        reward2 -= 1
        else:
            two = 1
        it += 1
        x.append(it)
        y1.append(reward1)
        y2.append(reward2)
        print("\nMove #", it)
        print_array(arr)
        print("Reward score of 1st agent : " + str(reward1))
        print("Reward score of 2nd agent : " + str(reward2))
    plt.title("Relative performance of both agents")
    plt.scatter(x, y1, marker="s")
    plt.plot(x, y1, label="Agent 1")
    plt.scatter(x, y2, marker="^")
    plt.plot(x, y2, label="Agent 2")
    plt.xlabel("Number of moves")
    plt.ylabel("Reward score")
    plt.legend()
    plt.show()


def initialise_array():
    rows = int(input("Enter size of room : "))
    cols = rows
    arr = [[0 for _ in range(cols)] for __ in range(rows)]
    arr[0][0] = 1
    arr[rows-1][cols-1] = 2
    print("Initial state")
    print_array(arr)
    return arr


def print_array(arr):
    for i in arr:
        for j in i:
            print(j, end=" ")
        print()


if __name__ == "__main__":
    simulate()
