def not_knowing_about_raw_strings():
    some_path = "windows\\path\\to\\file.txt"
    some_path = r"c:\path\to\file.txt"

    some_regex = "\\d+\\.\\d*"
    some_regex = r"\d+\.\d*"

    val = 42
    interpolated = fr"\\ {val} //"
    print(interpolated)

    # gotcha = r"can't end in backslash \" # SyntaxError
    print(gotcha)
