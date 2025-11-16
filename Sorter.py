def sort(width, height, length, mass):
    """
    Determines the correct stack for a package based on its dimensions and mass.
    """

    volume = width * height * length

    is_bulky = (
        volume >= 1_000_000 or
        width >= 150 or
        height >= 150 or
        length >= 150
    )

    is_heavy = mass >= 20

    if is_bulky and is_heavy:
        return "REJECTED"
    elif is_bulky or is_heavy:
        return "SPECIAL"
    else:
        return "STANDARD"
