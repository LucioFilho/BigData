import math

def single_letter_variables():
    for i in range(100):  # OK
        ...

    for idx in range(100):  # easier to ctrl+f for idx
        ...

    _ = "unused OK"

    x, y, z = (1, 2, 3)  # OK

    a0, r, t = 1.0, .01, 1.0
    a = a0 * math.exp(r * t)

    # Please use names
    p = "data.txt"
    with open(p) as f:
        for l in f:
            s = l.split()
            t, u = s[0], s[-1]
            ti, ui = int(t), int(u)
            d = ui - ti
            ...

    # with open(p) as fp:
    #     for line in fp:
    #         tokens = line.split()
    #         first_token, last_token = tokens[0], tokens[-1]
    #         first_int, last_int = int(first_token), int(last_token)
    #         diff = last_int - first_int
    #         ...
