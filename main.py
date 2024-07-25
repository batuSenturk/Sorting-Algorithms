from algs import bubble_sort, merge_sort, quick_sort, insertion_sort, cocktail_sort, heap_sort, selection_sort, radix_sort, shell_sort, gnome_sort, tim_sort, comb_sort, cycle_sort, stooge_sort, odd_even_sort, pancake_sort
from display import visualize_sorting_algorithm, quit_pygame
from util.helpers import generate_random_list

if __name__ == "__main__":
    arr = generate_random_list(lower_bound=0, upper_bound=99)
    
    # Choose sorting algorithm and visualization
    try:
        visualize_sorting_algorithm(heap_sort, arr)
    except KeyboardInterrupt:
        pass
    finally:
        quit_pygame()
