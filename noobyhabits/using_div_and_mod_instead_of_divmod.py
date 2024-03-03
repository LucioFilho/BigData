def using_div_and_mod_instead_of_divmod(x, p):
    q, r = x // p, x % p
    q, r = divmod(x, p)
    if r == 0:
        print(f"{p} divides {x} evenly into {q} parts")
    else:
        print(f"{p} divides {x} into {q} parts with a remainder of {r}")
