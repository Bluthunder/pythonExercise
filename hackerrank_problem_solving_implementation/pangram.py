def pangram(s):
    a = set(s.lower())
    return 'pangram' if len(a) == 27 else 'not pangram'

# if __name__ == '__main__':
#