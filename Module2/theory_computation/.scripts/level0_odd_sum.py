# Solution 1
# ---------------------------------------------------------------------------
def solve_func(a, b): # Temporal O(n) solution, Espacial O(n), con n = b-a
    _odd_array = [
        number for number in range(a, b+1) if number % 2 != 0]
    return sum(_odd_array)


_t = int(input())

for _i in range(_t): # Temporal O(n * t) solution, Espacial O(n), con n = b-a
    _a = int(input())
    _b = int(input())

    _sol = solve_func(_a, _b)

    print(f"Case {_i + 1}: {_sol}")
# ---------------------------------------------------------------------------

# Solution 2
# ---------------------------------------------------------------------------
def solve_func(a, b): # Temporal O(1) solution, Espacial O(1)
    a = a if a % 2 != 0 else a + 1
    b = b if b % 2 != 0 else b - 1 # No es necesario

    _pos_a = (a + 1) // 2
    _pos_b = (b + 1) // 2

    return _pos_b**2 - (_pos_a - 1)**2


_t = int(input())

for _i in range(_t): # Temporal O(t) solution, Espacial O(1)
    _a = int(input())
    _b = int(input())

    _sol = solve_func(_a, _b)
    print(f"Case {_i + 1}: {_sol}")
# ---------------------------------------------------------------------------