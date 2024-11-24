def write_to_file(file_path, content):
    with open(file_path, "w") as f:
        f.write(content)


def read_from_file(file_path):
    with open(file_path, "r") as f:
        return f.read()
