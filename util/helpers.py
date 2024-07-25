import random

def generate_random_list(lower_bound=0, upper_bound=99):
    arr = list(range(lower_bound, upper_bound + 1))
    random.shuffle(arr)
    return arr
