def using_eval_as_a_parser():
    data_str = '{"a":1, "b":2, "c":3}'
    data = eval(data_str)
    data = json.loads(data_str)
    with open("file_that_data_str_came_from.txt") as fp:
        data = json.load(fp)
    print(data)
    # pydantic...
