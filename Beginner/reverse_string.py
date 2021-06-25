# str = input()

def reverse_string_classical(input_str):
    out = ""
    for x in range(len(input_str) - 1, -1, -1):
        out = out + input_str[x]
    return out


def reverse_string_extended_slice(input_str):
    return input_str[::-1]


if __name__ == "__main__":
    in_ = input("Enter your input String :")

    print(reverse_string_classical(in_))
    print(reverse_string_extended_slice(in_))
