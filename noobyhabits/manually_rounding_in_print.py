def manually_rounding_in_print():  
    t = 1.23456
    print(f"Finished in {t}s")
    print(f"Finished in {round(t, 2)}s")
    print(f"Finished in {t:.2f}s")
