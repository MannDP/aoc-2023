def read_file(path: str) -> list[str]:
    return [line.rstrip() for line in open(path, "r")]
