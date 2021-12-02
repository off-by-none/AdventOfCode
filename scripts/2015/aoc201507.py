def format_data(data):
    fdata = []
    for d in data:
        d = d.strip("\n")
        d = d.replace("AND", "&")
        d = d.replace("OR", "|")
        d = d.replace("RSHIFT", ">>")
        d = d.replace("LSHIFT", "<<")
        d = d.replace("NOT", "~")
        d = d.split(" ")
        fdata.append(d)

    return fdata


def get_wire_value(data, wire):
    for d in data:
        if len(d) <= 3:
            print(d)
        

    return True


if __name__ == "__main__":
    file = r"C:\Users\BBREWER2\Documents\MyDirectory\PythonScripts\dataFiles\advertofcode\advert201507.txt"

    with open(file) as f:
        data = f.readlines()
        f.close()

    data = format_data(data)
    value = get_wire_value(data, "a")
        