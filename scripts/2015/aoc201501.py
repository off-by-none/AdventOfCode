# part 01
def net_floor(data):
    count = {}

    for n in data:
        if n in count: 
            count[n] += 1
        else: 
            count[n] = 1

    up = count['(']
    down = count[')']
    floor = up - down

    return floor


# part 02
def basement_position(data):
    floor = 0
    position = 0

    for n in data:
        position += 1
        
        if n == '(': 
            floor += 1
        elif n == ')': 
            floor -= 1
        
        if floor < 0:
            break
    
    return position


if __name__ == "__main__":
    file = r"C:\Users\BBREWER2\Documents\MyDirectory\PythonScripts\dataFiles\advertofcode\advert201501.txt"

    with open(file) as f:
        data = f.readlines()
        f.close()

    print(f'Part_01: {net_floor(data[0])}')
    print(f'Part_02: {basement_position(data[0])}')
