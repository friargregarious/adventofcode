directions = str(open("input.txt").read())

floor = 0
steps = 0

for i in directions:
    steps += 1

    if i =="(":
        floor += 1
    else:
        floor -= 1
        if floor == -1:
            print(f"Santa entered the basement at step {steps}")
    

print(f"Santa should go to floor {floor}")
