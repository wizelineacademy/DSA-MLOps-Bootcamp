def solve_func(n): # Temporal O(m), Espacial O(1), con m := cantidad de digitos de n en base 2 (binario)
    n = bin(n-1)[::-1][:-2]
    msg_ = "{ "

    for i in range(len(n)):
        if n[i] == '1':
            msg_ += f"{3**i}, "

    msg_ = msg_[:-2] +" }"

    return msg_

# This will run forever (or until end of file), to stop execution press stop botton for the notebook cell

while True: # Temporal O(m), Espacial O(1), con m := cantidad de digitos de n en base 2 (binario)
    n = int(input())
    if n == 0: break
    elif n == 1:
        print('{ }')
        continue

    _sol = solve_func(n)
    print(_sol)