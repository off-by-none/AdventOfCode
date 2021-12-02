def move_to_house(start_row, start_col, direction):
    if direction == '^':
        start_row += 1
    elif direction == 'v':
        start_row -= 1
    elif direction == '>':
        start_col += 1
    elif direction == '<':
        start_col -= 1
    
    next_house = (start_row, start_col)
    return next_house

def advert01(data):
    houses = [(0, 0)]
    
    for direction in data:
        row = houses[-1][0]
        col = houses[-1][1]
        
        houses.append(move_to_house(row, col, direction))
    
    distinct_houses = []
    for house in houses:
        if house not in distinct_houses:
            distinct_houses.append(house)
    
    return len(distinct_houses)


def advert02(data):
    santa_houses = [(0, 0)]
    robo_houses = [(0, 0)]
    direction_num = 0

    for direction in data:
        direction_num += 1

        if direction_num % 2 == 0:
            row = santa_houses[-1][0]
            col = santa_houses[-1][1]
            santa_houses.append(move_to_house(row, col, direction))
        else:
            row = robo_houses[-1][0]
            col = robo_houses[-1][1]
            robo_houses.append(move_to_house(row, col, direction))
    
    houses = santa_houses + robo_houses
    distinct_houses = []
    for house in houses:
        if house not in distinct_houses:
            distinct_houses.append(house)
    
    return len(distinct_houses)


if __name__ == "__main__":
    file = r"C:\Users\BBREWER2\Documents\MyDirectory\PythonScripts\dataFiles\advertofcode\advert201503.txt"

    with open(file) as f:
        data = f.readlines()
        f.close()

    #print(data)
    print(advert01(data[0]))
    print(advert02(data[0]))
