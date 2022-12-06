
# you need to add a subroutine to the device that detects a start-of-packet marker in the datastream. 


# the start of a packet is indicated by a sequence of four characters that are all different.



# After the first three characters(mjq) have been received, 
# there haven't been enough characters received yet to find the marker. 

# The first time a marker could occur is after the fourth character is received, 
# making the most recent four characters mjqj. Because j is repeated, this isn't a marker.
# START OF PACKET MARKER
# mjqjpqmgbljsphdztnvjfqwrcgsmlb first marker after character 7
# bvwbjplbgvbhsrlpgdmjqwftvncz: first marker after character 5
# nppdvjthqldpwncqszvftbrmjlhg: first marker after character 6
# nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg: first marker after character 10
# zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw: first marker after character 11

# START OF MSG MARKER
# mjqjpqmgbljsphdztnvjfqwrcgsmlb: first marker after character 19
# bvwbjplbgvbhsrlpgdmjqwftvncz: first marker after character 23
# nppdvjthqldpwncqszvftbrmjlhg: first marker after character 23
# nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg: first marker after character 29
# zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw: first marker after character 26

examples = [("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7, 19),
            ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5, 23),
            ("nppdvjthqldpwncqszvftbrmjlhg", 6, 23),
            ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10, 29),
            ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11, 26)
            ]



# marker must be 4 non-repeated characters ---> use a {set}

def marker(buffer, marker_len=4):
    # A start-of-message marker is just like a start-of-packet marker, 
    # except it consists of 14 distinct characters rather than 4.
    
    for i in range(marker_len, len(buffer)):
        # print(list(buffer))
        if len(set(buffer[i-marker_len:i])) == marker_len:
            return i, f"Packet marker index = {i}"



if __name__ == "__main__":
    for example, p1_answer, p2_answer in examples:
        # guess, msg = marker(example)
        # print(msg, p1_answer, guess == p1_answer)

        guess, msg = marker(example, marker_len=14)
        print(msg, p2_answer, guess == p2_answer)

    part_1_guess, part_1_msg = marker(str(open("input.txt").read()))
    print("Packet Marker:", part_1_msg, part_1_guess)

    part_2_guess, part_2_msg = marker(str(open("input.txt").read()), marker_len=14)
    print("Message Marker:", part_2_msg, part_2_guess)





