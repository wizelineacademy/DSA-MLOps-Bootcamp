def solve_func(): # Temporal O(k^2), Espacial O(1), con k = 100
    k = 100
    for x in range(-k, k):
        for y in range(-k, k):
            if x == y: continue
            z = A - x - y
            if (x == y) or (y == z) or (x == z): continue
            if (x + y + z == A) and (x*y*z == B) and (x**2 + y**2 + z**2 == C):
                return f"{x} {y} {z}"
    return "No solution."

n = int(input())
for i in range(n): # Temporal O(n * k^2), Espacial O(1), con k = 100
    A, B, C = [int(i) for i in input().split()]

    _sol = solve_func()
    print(_sol)