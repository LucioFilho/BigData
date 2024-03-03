# Manual str formatting
def manual_str_formatting(name, subscribers):
    if subscribers > 100000:
        print("Wow " + name + "! you have " + str(subscribers) + " subscribers!")
    else:
        print("Lol " + name + " that's not many subs")

# do it instead
def manual_str_formatting(name, subscribers):
    if subscribers > 100000:
        print(f"Wow {name}! you have {subscribers} subscribers!")
    else:
        print(f"Lol {name} that's not many subs")
