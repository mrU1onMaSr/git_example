def addition(number: int, until_number: int) -> list[str]:
    lst = []
    for i in range(1,until_number+1):
        lst.append(f"{number} + {i} = {number + i}")
    return lst

def multiplication(number: int, until_number: int) -> list[str]:
    lst = []
    for i in range(1,until_number+1):
        lst.append(f"{number} x {i} = {number * i}")
    return lst