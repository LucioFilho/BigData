def thinking_and_or_return_bools():
    a = {"a": 1, "b": 2, "c": 3}
    b = [1, 2, 3]
    print(a or b)  # {"a": 1, "b": 2, "c": 3}
    print(a and b)  # [1, 2, 3]
    print({} or [])  # []
    print({} and [])  # {}

    # or: first true one or last false one
    # and: first false one or last true one

    cond = a or b
    if cond == True:
        print("cond is true")
    elif cond:
        print("cond is truthy")
    else:
        print("cond is falsey")

thinking_and_or_return_bools()