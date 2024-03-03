def inserting_or_deleting_while_iterating():
    # d = {chr(65+i): i for i in range(10)}
    # for key, val in d.items():
    #     if val % 2 == 0:
    #         del d[key]
    #         # d[key] = 42

    d = {chr(65 + i): i for i in range(10)}
    for key, val in list(d.items()):
        if val % 2 == 0:
            del d[key]
    print(d)

    d = {chr(65 + i): i for i in range(10)}
    to_delete = set()
    for key, val in d.items():
        if val % 2 == 0:
            to_delete.add(key)

    for key in to_delete:
        del d[key]
    print(d)

