# part 01
def calculate_total_wrapping_sqft(data):
    total_wrapping = 0
    total_ribbon = 0

    for gift in data:
        gift = gift.strip('\n')
        dimensions = gift.split('x')
        dimensions = [int(x) for x in dimensions]
        dimensions.sort()
        areas = []

        for d1 in range(0, len(dimensions) - 1):
            for d2 in range(d1 + 1, len(dimensions)):
                areas.append(int(dimensions[d1]) * int(dimensions[d2]))

        bowtie = 1
        for x in dimensions:
            bowtie *= int(x)
        
        areas.sort()
        total_wrapping += 2 * sum(areas) + areas[0]
        total_ribbon += 2 * (dimensions[0] + dimensions[1]) + bowtie

    return total_wrapping, total_ribbon


if __name__ == "__main__":
    file = r"C:\Users\BBREWER2\Documents\MyDirectory\PythonScripts\dataFiles\advertofcode\advert201502.txt"

    with open(file) as f:
        data = f.readlines()
        f.close()

    total_wrapping, total_ribbon = calculate_total_wrapping_sqft(data)
    print(total_wrapping)
    print(total_ribbon)