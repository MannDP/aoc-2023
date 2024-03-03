def read_file(path: str) -> list[str]:
    return [l.rstrip() for l in open(path, "r")]
