MAX_A = 10**4
def solve_func(x): # Temporal O(MAX_A), Espacial O(1)
    for a in range(1, MAX_A):
        if x - a**3 < 1:
            break

        b = round((x - a**3)**(1/3))
        # print(b)
        if (a**3 + b**3 == x):
            return "YES"

    return "NO"


t = int(input())

for i in range(t): # Temporal O(t * MAX_A), Espacial O(1)
    x = int(input())

    _sol = solve_func(x)
    print(_sol)