import re


def generate_initials(name: str, length: int = 2, *, uppercase: bool = True) -> str:
    name = name.strip("\x00").strip()
    if uppercase:
        name = name.upper()
    name = re.sub(r'[!@#$%^&*(),.?":{}|<>_]', "", name)
    name = name.strip("-").strip("\x00").strip()
    names = name.split()

    if len(names) < length:
        names = [part for name_part in names for part in name_part.split("-")]

    if len(names) == 1:
        return name[:length]

    initials = ""
    assigned_names = 0
    start = 0
    for index in range(length):
        if (index == length - 1 and index > 0) or index > len(names) - 1:
            index = len(names) - 1
        if assigned_names >= len(names):
            start += 1
        initials += names[index][start : start + 1]
        assigned_names += 1

    return initials[:length]
