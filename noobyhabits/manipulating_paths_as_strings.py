def manipulating_paths_as_strings():
    path = "path/to/data/my_data.json"
    zipped_file = path.removesuffix(".json") + ".zip"
    data_dir = "/".join(path.split("/")[-2])
    other_file = f"{data_dir}/other_file.txt"
    deeper_dir = f"{data_dir}/abc/def"

    path = pathlib.Path("path/to/data/my_data.json")
    zipped_file = path.with_suffix(".zip")
    data_dir = path.parent
    other_file = path.with_name("other_file.txt")
    deeper_dir = data_dir.joinpath("abc", "def")

    # also os.path but pathlib is preferred
