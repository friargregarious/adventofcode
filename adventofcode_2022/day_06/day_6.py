
# you need to add a subroutine to the device that detects a start-of-packet marker in the datastream. 


# the start of a packet is indicated by a sequence of four characters that are all different.


# mjqjpqmgbljsphdztnvjfqwrcgsmlb 7
# After the first three characters(mjq) have been received, 
# there haven't been enough characters received yet to find the marker. 

# The first time a marker could occur is after the fourth character is received, 
# making the most recent four characters mjqj. Because j is repeated, this isn't a marker.

# bvwbjplbgvbhsrlpgdmjqwftvncz: first marker after character 5
# nppdvjthqldpwncqszvftbrmjlhg: first marker after character 6
# nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg: first marker after character 10
# zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw: first marker after character 11

examples = [("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7),
            ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
            ("nppdvjthqldpwncqszvftbrmjlhg", 6),
            ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10),
            ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11)
            ]

# marker must be 4 non-repeated characters ---> use a {set}

def first_marker(buffer):
    for i in range(4, len(buffer)):
        # print(list(buffer))
        if len(set(buffer[i-4:i])) == 4:
            return i, f"first marker index = {i}"



if __name__ == "__main__":
    for example, answer in examples:
        guess, msg = first_marker(example)
        print(msg, guess, answer, guess==answer)

    for example, answer in examples:
        guess, msg = first_marker(example)
        print(msg, guess, answer, guess == answer)






