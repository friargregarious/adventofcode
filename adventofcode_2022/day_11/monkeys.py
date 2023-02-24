import sys, json
TEST = "test" in sys.argv
VERBOSE = "verbose" in sys.argv

def monkeys(s: list):
    datalist = iter(s)

    while True:
        monkey = {}

        # GET THE MONKEY NAME
        monkey_name = next(datalist)

        this_monkey = monkey_name.strip("Monkey :\n")
        monkey[this_monkey] = {}

        if VERBOSE:
            print(monkey)

        # WHAT ITEMS IS THE MONKEY CARRYING?
        m_items = next(datalist)
        int_items = [int(x) for x in m_items.strip(
            "Starting items:\n").split(", ")]
        monkey[this_monkey]["items"] = int_items

        if VERBOSE:
            print("items",  monkey[this_monkey]["items"])

        # WHAT OPERATION DO WE USE ON THIS MONKEY?
        m_oper = next(datalist)
        monkey[this_monkey]["operation"] = m_oper.replace(
            "Operation: new =", "").strip().split(" ")

        if VERBOSE:
            print("operation",  monkey[this_monkey]["operation"])

        # HOW DO WE TEST THIS MONKEY?
        m_test = next(datalist)
        monkey[this_monkey]["test"] = int(m_test.strip("Test: divisible by \n"))

        if VERBOSE:
            print("test",  monkey[this_monkey]["test"])

        # WHAT TO DO IF TRUE?
        m_true = next(datalist)

        test_true = int(m_true.replace("If true: throw to monkey", "").strip())
        monkey[this_monkey]["if_true"] = test_true

        if VERBOSE:
            print("if_true",  monkey[this_monkey]["if_true"])


        # WHAT TO DO IF FALSE?
        m_false = next(datalist)

        test_false = int(m_false.replace("If false: throw to monkey", "").strip())
        monkey[this_monkey]["if_false"] = test_false

        if VERBOSE:
            print("if_false",  monkey[this_monkey]["if_false"])


        # IS THIS THE END OF THE FILE?
        yield monkey

        try:
            blank = next(datalist).strip()
            if blank == "":
                pass
        except StopIteration as e:
            break

def show_all_monkeys(d:dict):
    inv_list=[]
    for this_monkey in d:
        inv_list.append([this_monkey, d[this_monkey]["items"]])
    return inv_list



def get_monkeys():
    return dict(
        json.loads(
            str(
                open("monkeys.json").read()
                )
            )
        )

def put_monkeys(d:dict):
    with open("monkeys.json","w") as monkeyfile:
        monkeyfile.write(json.dumps(d, indent=4))

if __name__ == "__main__":


    if TEST:
        source = "sample.txt"
    else:
        source = "input.txt"
    
    for monkey in monkeys(list(open(source).readlines())):
        print(monkey)
        