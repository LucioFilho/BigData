strict = True

def storing_inputs_and_or_outputs_as_globals():
    for i in range(100):
        if strict:
            ...
        else:
            ...

    global ans
    ans = ...

# SELF PROMO