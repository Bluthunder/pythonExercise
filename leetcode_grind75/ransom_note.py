"""
Date: 10 April 2024
Leet Code Grind 75 Question: 3
DSA Topic: Hash Map

"""


# This is using two dicts
def is_ransom_note(ransom_note: str, magazine: str) -> bool:
    ransom_note_dict = {}
    magazine_dict = {}

    for r_ch in ransom_note:
        if r_ch not in ransom_note_dict:
            ransom_note_dict[r_ch] = 1
        else:
            ransom_note_dict[r_ch] += 1

    for m_ch in magazine:
        if m_ch not in magazine_dict:
            magazine_dict[m_ch] = 1
        else:
            magazine_dict[m_ch] += 1

    for ch in ransom_note:
        if ch not in magazine_dict or magazine_dict[ch] < ransom_note_dict[ch]:
            return False
    return True


def is_ransom_note_opt(ransom_note: str, magazine: str) -> bool:
    magazine_dict = {}

    for c in magazine:
        if c not in magazine_dict:
            magazine_dict[c] = 1
        else:
            magazine_dict[c] += 1

    for ch in ransom_note:
        if ch not in magazine_dict or magazine_dict[ch] == 0:
            return False
        else:
            magazine_dict[ch] -= 1

    return True


if __name__ == '__main__':
    ransom_string = "Today is April 10"

    magazine_string = "10 is one of the numbers and days in the April Month. Today"

    print(is_ransom_note(ransom_string, magazine_string))

    print(is_ransom_note_opt(ransom_string, magazine_string))
