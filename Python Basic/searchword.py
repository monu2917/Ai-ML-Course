data = True

with open('simpale.txt', "r") as f:
    while data:
        data = f.readline()

        if 'monu' in data:
            print("monu is found")
            break

        print(data)