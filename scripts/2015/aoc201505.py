def check_is_nice_1(data):
    nice_count = 0

    for string in data:
        string = string.strip('\n')
        vowels = 0
        double_char = 0
        bad_string = 0
        previous_char = ''
    
        for l in string:
            if l in ['a', 'e', 'i', 'o', 'u']: 
                vowels += 1
            
            if l == previous_char:
                double_char += 1
            
            if previous_char + l in ['ab', 'cd', 'pq', 'xy']:
                bad_string += 1

            previous_char = l
        
        if vowels >= 3 and double_char > 0 and bad_string == 0:
            nice_count += 1

    return nice_count


def check_is_nice_2(data):
    nice_count = 0

    for string in data:
        string = string.strip('\n')
        hasRepeatingPair = False
        hasMiddleChar = False

        pairs = []
        for i in range(len(string) - 1):
            pairs.append(string[i] + string[i + 1])
        
        for x in range(len(pairs) - 2):
            for y in range(x + 2, len(pairs)):
                if pairs[x] == pairs[y]:
                    hasRepeatingPair = True
                    break
        
        for i in range(len(pairs) - 1):
            if pairs[i][0] == pairs[i + 1][1]:
                hasMiddleChar = True
                break
        
        if hasRepeatingPair and hasMiddleChar:
            nice_count += 1

    return nice_count


if __name__ == "__main__":
    file = r"C:\Users\BBREWER2\Documents\MyDirectory\PythonScripts\dataFiles\advertofcode\advert201505.txt"

    with open(file) as f:
        data = f.readlines()
        f.close()

    print(check_is_nice_2(data))
        