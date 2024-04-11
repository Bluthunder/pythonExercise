"""
Date: 11 April 2024
Tower of Hanoi using Recursion

"""
import timeit

# This implementation is taken from DSA thinking with python
def tower_of_hanoi(num_disk, start_peg=1, end_peg=3):
    if num_disk:
        tower_of_hanoi(num_disk - 1, start_peg, 6 - start_peg - end_peg)
        print(f"Move disk {num_disk} from peg {start_peg} to peg {end_peg}")
        tower_of_hanoi(num_disk - 1, 6 - start_peg - end_peg, end_peg)


if __name__ == '__main__':
    tower_of_hanoi(num_disk=10)


