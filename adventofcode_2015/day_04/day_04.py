import sys
import hashlib


def miner(key="", nonce=0):
    my_encoder = hashlib.md5()
    this_try = f"{key}{nonce}"
    print(f"trying: {this_try.rjust(20)}")
    my_encoder.update(this_try.encode())
    result = my_encoder.hexdigest()

    return result


if "test" in sys.argv:
    keys = [("abcdef", 609043, "000001dbbfa"),
            ("pqrstuv", 1048970, "000006136ef")]

    for this_try in keys:
        test_key, t_nonce, answer = this_try
        result = miner(key=test_key, nonce=t_nonce)

        if result.startswith(answer):
            print(test_key.rjust(12), t_nonce, result.rjust(20), "SUCCESS!!!")
        else:
            print(test_key.rjust(12), t_nonce, result.rjust(20),  "FAIL!!!")


else:
    given_key = "bgvyzdsv"

    if "part2" in sys.argv:
        difficulty = "0" * 6
    else:
        difficulty = "0" * 5

    result = ""

    real_nonce = 0
    while True:
        result = miner(key=given_key, nonce=real_nonce)
        if result.startswith(difficulty):
            if "part2" in sys.argv:
                print("PART 2", given_key.rjust(12), real_nonce,
                      result.rjust(20), "SUCCESS!!!")
            else:
                print("PART 1", given_key.rjust(12), real_nonce,
                      result.rjust(20), "SUCCESS!!!")
            break
        real_nonce += 1
