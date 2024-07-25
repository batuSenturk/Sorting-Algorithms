import pygame

# Initialize Pygame
pygame.init()

# Constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

# Adjustable frame rate (in frames per second)
FRAME_RATE = 120  # Set this to a high value for faster visualization

# Set up display
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sorting Algorithm Visualization")

def draw_array(arr, current_index=None, color_positions={}):
    window.fill(BLACK)
    
    # Calculate width and scaling factor
    gap = 1  # Thin line gap between bars
    bar_width = (width - (len(arr) - 1) * gap) / len(arr)
    max_val = max(arr)
    height_scale = height / max_val
    
    for i, val in enumerate(arr):
        x = i * (bar_width + gap)
        bar_height = val * height_scale
        if i == current_index:
            color = WHITE
        elif i in color_positions:
            color = WHITE
        else:
            color = GREEN
        pygame.draw.rect(window, color, (x, height - bar_height, bar_width, bar_height))
    
    pygame.display.update()

def visualize_sorting_algorithm(sorting_function, arr):
    run = True
    clock = pygame.time.Clock()
    for step, current_index in sorting_function(arr):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        draw_array(arr, current_index)
        clock.tick(FRAME_RATE)
        if not run:
            break

    # Highlight each bar in white sequentially from smallest to largest
    for i in range(len(arr)):
        draw_array(arr, current_index=i, color_positions={j for j in range(i+1)})
        clock.tick(FRAME_RATE)
    
    pygame.time.wait(2000)  # Wait 2 seconds to show the final sorted array

# Clean up Pygame
def quit_pygame():
    pygame.quit()
