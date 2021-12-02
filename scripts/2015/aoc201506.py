def format_instructions(data):
    instructions = []
    for instruction in data:
        build_instruction = []
        instruction = instruction.strip("\n")
        instruction = instruction.split(" ")
        
        if "turn" in instruction:
            instruction.remove("turn")
        
        start = instruction[1].split(",")
        end = instruction[3].split(",")

        build_instruction.append(instruction[0])
        build_instruction.append(int(start[0]))
        build_instruction.append(int(start[1]))
        build_instruction.append(int(end[0]))
        build_instruction.append(int(end[1]))
        
        instructions.append(build_instruction)

    return instructions


def plug_in_lights(instructions):
    lights = [[0 for x in range(1000)] for y in range(1000)]
    lights_on_count = 0
    for instruction in instructions:
        action = instruction[0]
        
        if action == "toggle":
            for light_row in range(instruction[2], instruction[4] + 1):
                for light_col in range(instruction[1], instruction[3] + 1):
                    if lights[light_row][light_col] == 0:
                        lights[light_row][light_col] = 1
                    else:
                        lights[light_row][light_col] = 0
        elif action == "off":
            for light_row in range(instruction[2], instruction[4] + 1):
                for light_col in range(instruction[1], instruction[3] + 1):
                    lights[light_row][light_col] = 0
        elif action == "on":
            for light_row in range(instruction[2], instruction[4] + 1):
                for light_col in range(instruction[1], instruction[3] + 1):
                    lights[light_row][light_col] = 1

    for x in range(1000):
        for y in range(1000):
            lights_on_count += lights[x][y]

    return lights_on_count


def plug_in_lights_p2(instructions):
    lights = [[0 for x in range(1000)] for y in range(1000)]
    brightness = 0
    for instruction in instructions:
        action = instruction[0]
        
        if action == "toggle":
            for light_row in range(instruction[2], instruction[4] + 1):
                for light_col in range(instruction[1], instruction[3] + 1):
                    lights[light_row][light_col] += 2
        elif action == "off":
            for light_row in range(instruction[2], instruction[4] + 1):
                for light_col in range(instruction[1], instruction[3] + 1):
                    if lights[light_row][light_col] > 0:
                        lights[light_row][light_col] -= 1
        elif action == "on":
            for light_row in range(instruction[2], instruction[4] + 1):
                for light_col in range(instruction[1], instruction[3] + 1):
                    lights[light_row][light_col] += 1

    for x in range(1000):
        for y in range(1000):
            brightness += lights[x][y]

    return brightness


if __name__ == "__main__":
    file = r"C:\Users\BBREWER2\Documents\MyDirectory\PythonScripts\dataFiles\advertofcode\advert201506.txt"

    with open(file) as f:
        data = f.readlines()
        f.close()

    instructions = format_instructions(data)
    #print(plug_in_lights(instructions))
    print(plug_in_lights_p2(instructions))
        