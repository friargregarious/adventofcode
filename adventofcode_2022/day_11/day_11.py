import sys
import monkeys

TEST = "test" in sys.argv
VERBOSE = "verbose" in sys.argv
PART1 = "part1" in sys.argv
OUTFILE = "outfile" in sys.argv
PRINTON1K = "p1k" in sys.argv
PART2 = "part2" in sys.argv


if OUTFILE:
    fileout = "output.txt"
elif PART2:
    fileout = "part2_output.txt"

outfile = open(fileout, "w")
outfile.close()



if TEST:
    source = "sample.txt"
else:
    source = "input.txt"

# refresh our data from the source
this_pack = {}
for monk in monkeys.monkeys(list(open(source).readlines())):
    # print(monk)
    this_pack.update(monk)

# print(this_pack)
# store formatted data to json temp
monkeys.put_monkeys(this_pack)
# start a working dict by pulling from our json temp
this_pack = monkeys.get_monkeys()

monkey_inspections = {}


if "r50" in sys.argv:
    rounds = 5 * 10
elif "r100" in sys.argv:
    rounds = 10 * 10
elif "r1k" in sys.argv:
    rounds = 100 * 10
elif "r2k" in sys.argv:
    rounds = 200 * 10
elif "r5k" in sys.argv:
    rounds = 500 * 10
elif "r10k" in sys.argv:
    rounds = 1000 * 10
else:
    rounds = 20

for rnd in range(1, 1 + rounds):
    with open(fileout, "a") as outfile:
        for this_monkey in this_pack:
            if this_monkey not in monkey_inspections:
                monkey_inspections[this_monkey] = 0

            if OUTFILE:
                print("###################\n",
                    this_pack[this_monkey], "\n###################", file=outfile)
            
            # Monkey 0:
            inventory = this_pack[this_monkey]["items"].copy()
            this_pack[this_monkey]["items"]

            for inhand in inventory:
                monkey_inspections[this_monkey] += 1
                #   Monkey inspects an item with a worry level of 79.
                this_pack[this_monkey]["items"].pop(0)
                true_monkey = this_pack[this_monkey]["if_true"]
                false_monkey = this_pack[this_monkey]["if_false"]

                #     Worry level is multiplied by 19 to 1501.
                _, oper, ammount = this_pack[this_monkey]["operation"]
                if ammount == "old":
                    ammount = inhand
                else:
                    ammount = int(ammount)

                if oper == "*":
                    new_worry = inhand * int(ammount)
                elif oper == "+":
                    new_worry = inhand + int(ammount)
                else:
                    print("ERROR CAN'T FIND OPERATION IN MONKEYS")

                #     Monkey gets bored with item. Worry level is divided by 3 to 500.
                if PART1:
                    relief = new_worry // 3
                elif PART2:
                    relief = new_worry % 10
                    # relief = int((new_worry // 3 ) * 1 )

                #     Current worry level is not divisible by 23.
                #     monkeytest = newworry % test == 0
                m_test = this_pack[this_monkey]["test"]
                monkey_test = relief % m_test == 0

                #     Item with worry level 500 is thrown to monkey 3.
                if monkey_test:
                    #     true throw to monkeynumt
                    throw_to = str(true_monkey)
                else:
                    #     else throw to monkeynumf
                    throw_to = str(false_monkey)

                this_pack[throw_to]["items"].append(relief)
                monkeys.put_monkeys(this_pack)
                if OUTFILE:
                    print(f"""Monkey {this_monkey} with items {this_pack[this_monkey]["items"]}
                        tested {inhand} {oper} {ammount} as {new_worry} 
                        but relief {relief} was / {m_test} tested {monkey_test}
                        so threw to monkey {throw_to} {this_pack[throw_to]["items"]}
                        """, file=outfile)

        if PART2 and rnd in [1, 20, 50, 75, 100, 200, 500, 750] + [ 1000 * x for x in range(1,11)]:
            print(f"\nAfter round {rnd}", file=outfile)
            for m, insp in monkey_inspections.items():
                print(f"Monkey {m} inspected items {insp} times.", file=outfile)
        

        if PRINTON1K and (rnd % 1000 == 0):
            print(f"End of round {rnd}")
            for row in monkeys.show_all_monkeys(this_pack):
                print("Total inspections:", monkey_inspections[row[0]], row)

totals = list(monkey_inspections.values())
totals.sort()
print(totals)
most, sec_most = totals[-2:]
print(most, sec_most, f"Total level of monkey business after {rounds} rounds {most * sec_most}")
