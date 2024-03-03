def do_io_taking_path(path: str):
    with open(path, "w") as fp:
        fp.write("...")
        # do_io_taking_io(fp)


def do_io_taking_io(fp: typing.TextIO):
    fp.write("...")


def calls_do_io_with_gzip_io():
    with gzip.open("example.txt.gz", "wt") as fp:
        do_io_taking_io(fp)

    with gzip.open("example.txt.gz", "rt") as fp:
        assert fp.read() == "..."
