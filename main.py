def sort(width, height, length, mass):
    if width <= 0 or height <= 0 or length <= 0 or mass <= 0:
        raise ValueError("Values must be greater than 0")
    
    volume = width * height * length
    is_bulky = False
    
    if(volume >= 1000000 or width >= 150 or height >= 150 or length >= 150):
        is_bulky = True
    
    if mass >= 20 and is_bulky:
        return "HEAVY"
    elif mass >= 20 or is_bulky:
        return "SPECIAL"
    return "STANDARD"
    