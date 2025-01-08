from itertools import product


def create_dict(list1, list2, func):
    """
    Create a dictionary where the keys are pairs of values from two lists
    and the values are the result of a specified aggregation function
    applied to the key pairs.

    Args:
        list1 (list): First list of values.
        list2 (list): Second list of values.
        func (callable): Aggregation function (e.g., sum or multiplication).

    Returns:
        dict: Dictionary with keys as pairs and values as aggregated results.
    """
    # Use itertools.product to generate all possible pairs
    pairs = product(list1, list2)

    # Create a dictionary with the aggregation function applied to each pair
    result_dict = {pair: func(pair[0], pair[1]) for pair in pairs}

    return result_dict


# Define example aggregation functions
def sum_func(a, b):
    return a + b


def mul_func(a, b):
    return a * b


if __name__ == '__main__':
    # Define two example lists
    list1 = [1, 2, 3]
    list2 = [4, 5, 9]

    # Create dictionaries using sum and multiplication functions
    sum_dict = create_dict(list1, list2, sum_func)
    mul_dict = create_dict(list1, list2, mul_func)

    # Print the results
    print("Dictionary with sum function:", sum_dict)
    print("Dictionary with multiplication function:", mul_dict)
