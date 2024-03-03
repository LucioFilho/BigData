def concatenating_strings_with_plus():
    s = ""
    for i in range(100):
        s += f"some string {i}"

    ss = io.StringIO()
    for i in range(100):
        ss.write(f"some string {i}")
    s = ss.getvalue()

    lines = []
    for i in range(100):
        lines.append(f"some string {i}")
    s = "\n".join(lines)

    return s
