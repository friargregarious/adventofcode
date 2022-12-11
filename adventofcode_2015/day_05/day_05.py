import sys

NAUGHTY = False
NICE = not NAUGHTY

TEST = "test" in sys.argv


def p1_tests(word):

    # 1 It contains at least three vowels(aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
    vowel_count = 0
    for letter in word:
        if letter in ["a", "e", "i", "o", "u"]:
            vowel_count += 1
    if TEST:
        print(f" #1 Vowels Found: {vowel_count}", end="")
    rule_1 = vowel_count >= 3

    # 2 It contains at least one letter that appears twice in a row, like xx, abcdde(dd), or aabbccdd(aa, bb, cc, or dd).
    double_letter_count = ""
    for letter in word:
        if letter * 2 in word:
            double_letter_count += letter * 2

    if TEST:
        print(f" #2 Double Letters: {double_letter_count}", end="")
    rule_2 = double_letter_count != ""

    # 3 It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
    bad_strings = ["ab", "cd", "pq", "xy"]
    bad_found = ""
    for pattern in bad_strings:
        if pattern in word:
            bad_found += pattern
    if TEST:
        print(f" #3 Bad Found: {bad_found}", end=" ")
    rule_3 = bad_found == ""

    return NAUGHTY not in [rule_1, rule_2, rule_3]


if TEST:
    examples = {
        # because it has at least three vowels(u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
        "ugknbfddgicrmopn": NICE,
        # because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
        "aaa": NICE,
        "jchzalrnumimnmhp": NAUGHTY,  # because it has no double letter.
        "haegwjzuvuyypxyu": NAUGHTY,  # because it contains the string xy.
        "dvszwmarrgswjxmb": NAUGHTY,  # because it contains only one vowel.
    }

    for word, result in examples.items():
        passed = p1_tests(word)
        print(passed, result)

if "part1" in sys.argv:
    word_list = list( open("input.txt").readlines() )
    nice_count = 0

    for word in word_list:
        if p1_tests(word):
            nice_count += 1
    print(f"There are {nice_count} nice words in Santa's List.")

if "part2" in sys.argv:
    nice_count = 0
    word_list = list(open("input.txt").readlines())

    # It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy(xy) or aabcdefgaa(aa), but not like aaa(aa, but it overlaps).
    def p2_RULE_1(word):
        for i in range(2, len(word)-1):
            pattern = word[i-2:i]
            remaining = word[i:]
            if pattern in remaining:
                print(pattern, remaining, pattern in remaining)
                return True
        return False

    # It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi(efe), or even aaa.
    def p2_RULE_2(word):
        for i in range(3, len(word)):
            segment = word[i-3:i]
            test_char = segment[0]
            rule_test = segment.endswith(test_char)
            if rule_test:
                print(segment, test_char, rule_test)
                return True
        return False

    for word in word_list:
        r1 = p2_RULE_1(word)
        r2 = p2_RULE_2(word)
        if r1 and r2:
            nice_count += 1
            # print(word, r1, r2)
    print(f"There are {nice_count} nice words in part 2 of Santa's List.")


