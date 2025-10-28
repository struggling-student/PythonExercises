# generate_ex2_test_images.py
# This script generates 16x16 PNG images for testing ex2.
# It uses the provided 'images.py' library.

import os
import images

# Define image dimensions
IMG_SIZE = 16
HALF_SIZE = IMG_SIZE // 2
QUARTER_SIZE = IMG_SIZE // 4
EIGHTH_SIZE = IMG_SIZE // 8

# Define common colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)


# --- Helper for image creation ---
def create_image_data(width, height, background_color=BLACK):
    """Creates an empty image data structure (list of lists of RGB tuples)."""
    return [[background_color for _ in range(width)] for _ in range(height)]


# --- Image Generation Functions ---
def generate_solid_color(color, filename):
    """Generates a solid color image."""
    image_data = create_image_data(IMG_SIZE, IMG_SIZE, color)
    images.save(image_data, filename)
    print(f"Generated {filename}")


def generate_square_on_background(bg_color, fg_color, filename, x_offset, y_offset, size):
    """Generates an image with a solid square on a background."""
    image_data = create_image_data(IMG_SIZE, IMG_SIZE, bg_color)
    for y in range(y_offset, y_offset + size):
        for x in range(x_offset, x_offset + size):
            if 0 <= x < IMG_SIZE and 0 <= y < IMG_SIZE:
                image_data[y][x] = fg_color
    images.save(image_data, filename)
    print(f"Generated {filename}")


def generate_circle_on_background(bg_color, fg_color, filename, center_x, center_y, radius):
    """Generates an image with a solid circle on a background."""
    image_data = create_image_data(IMG_SIZE, IMG_SIZE, bg_color)
    for y in range(IMG_SIZE):
        for x in range(IMG_SIZE):
            if (x - center_x) ** 2 + (y - center_y) ** 2 <= radius ** 2:
                image_data[y][x] = fg_color
    images.save(image_data, filename)
    print(f"Generated {filename}")


def generate_checkerboard(block_size, color1, color2, filename):
    """Generates a checkerboard pattern."""
    image_data = create_image_data(IMG_SIZE, IMG_SIZE)
    for y in range(IMG_SIZE):
        for x in range(IMG_SIZE):
            if (x // block_size % 2 == 0 and y // block_size % 2 == 0) or \
                    (x // block_size % 2 == 1 and y // block_size % 2 == 1):
                image_data[y][x] = color1
            else:
                image_data[y][x] = color2
    images.save(image_data, filename)
    print(f"Generated {filename}")


def generate_vertical_stripes(stripe_width, color1, color2, filename):
    """Generates vertical stripes."""
    image_data = create_image_data(IMG_SIZE, IMG_SIZE)
    for y in range(IMG_SIZE):
        for x in range(IMG_SIZE):
            if (x // stripe_width) % 2 == 0:
                image_data[y][x] = color1
            else:
                image_data[y][x] = color2
    images.save(image_data, filename)
    print(f"Generated {filename}")


def generate_complex_shape(filename):
    """Generates a more complex shape (e.g., a hollow rectangle with a line)."""
    image_data = create_image_data(IMG_SIZE, IMG_SIZE, WHITE)

    # Draw a hollow rectangle (black perimeter)
    rect_x, rect_y, rect_w, rect_h = QUARTER_SIZE, QUARTER_SIZE, HALF_SIZE, HALF_SIZE
    for x in range(rect_x, rect_x + rect_w):
        image_data[rect_y][x] = BLACK  # Top
        image_data[rect_y + rect_h - 1][x] = BLACK  # Bottom
    for y in range(rect_y, rect_y + rect_h):
        image_data[y][rect_x] = BLACK  # Left
        image_data[y][rect_x + rect_w - 1] = BLACK  # Right

    # Draw a diagonal line inside the rectangle
    for i in range(HALF_SIZE):
        x = rect_x + i
        y = rect_y + i
        if 0 <= x < IMG_SIZE and 0 <= y < IMG_SIZE:
            image_data[y][x] = BLACK

    images.save(image_data, filename)
    print(f"Generated {filename}")


# --- Helper to generate expected image data for flood fill tests ---
def _generate_expected_flood_fill(image_data, x, y, replacement_color):
    """
    Simulates a flood fill to generate the expected image data.
    This is a reference implementation for testing purposes.
    """
    height = len(image_data)
    width = len(image_data[0])

    # Create a deep copy to modify
    expected_data = [row[:] for row in image_data]

    if not (0 <= x < width and 0 <= y < height):
        return expected_data  # No fill if start point is invalid

    target_color = expected_data[y][x]
    if target_color == replacement_color:
        return expected_data  # No fill if colors are the same

    q = [(x, y)]
    visited = set()
    visited.add((x, y))

    head = 0
    while head < len(q):
        cx, cy = q[head]
        head += 1

        expected_data[cy][cx] = replacement_color

        # Check neighbors (4-connected)
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = cx + dx, cy + dy
            if (0 <= nx < width and 0 <= ny < height and
                    expected_data[ny][nx] == target_color and
                    (nx, ny) not in visited):
                q.append((nx, ny))
                visited.add((nx, ny))
    return expected_data


if __name__ == '__main__':
    base_output_folder = "ex2_test_data"
    input_folder = os.path.join(base_output_folder, "input_images")
    expected_folder = os.path.join(base_output_folder, "expected_images")
    output_folder = os.path.join(base_output_folder, "output_images")  # This will be where program.py saves

    os.makedirs(input_folder, exist_ok=True)
    os.makedirs(expected_folder, exist_ok=True)
    os.makedirs(output_folder, exist_ok=True)  # Ensure output folder for program.py exists

    print(f"Generating test images and expected results in '{base_output_folder}'...")

    # Test Case 1: Blue Square on Black Background
    in_path_1 = os.path.join(input_folder, "blue_square_on_black.png")
    expected_path_1 = os.path.join(expected_folder, "expected_blue_square_fill.png")
    x1, y1 = 8, 8  # Center of the blue square
    replacement_color_1 = RED
    generate_square_on_background(BLACK, BLUE, in_path_1, QUARTER_SIZE, QUARTER_SIZE, HALF_SIZE)
    original_data_1 = images.load(in_path_1)
    expected_data_1 = _generate_expected_flood_fill(original_data_1, x1, y1, replacement_color_1)
    images.save(expected_data_1, expected_path_1)
    print(f"Generated {expected_path_1}")

    # Test Case 2: Solid Red Image
    in_path_2 = os.path.join(input_folder, "solid_red.png")
    expected_path_2 = os.path.join(expected_folder, "expected_solid_red_fill.png")
    x2, y2 = 0, 0  # Any pixel
    replacement_color_2 = GREEN
    generate_solid_color(RED, in_path_2)
    original_data_2 = images.load(in_path_2)
    expected_data_2 = _generate_expected_flood_fill(original_data_2, x2, y2, replacement_color_2)
    images.save(expected_data_2, expected_path_2)
    print(f"Generated {expected_path_2}")

    # Test Case 3: Checkerboard (Black and White)
    in_path_3 = os.path.join(input_folder, "checkerboard_32px.png")
    expected_path_3 = os.path.join(expected_folder, "expected_checkerboard_fill.png")
    x3, y3 = 0, 0  # Top-left black pixel
    replacement_color_3 = BLUE
    generate_checkerboard(EIGHTH_SIZE, BLACK, WHITE, in_path_3)
    original_data_3 = images.load(in_path_3)
    expected_data_3 = _generate_expected_flood_fill(original_data_3, x3, y3, replacement_color_3)
    images.save(expected_data_3, expected_path_3)
    print(f"Generated {expected_path_3}")

    # Test Case 4: Green Circle on White Background
    in_path_4 = os.path.join(input_folder, "green_circle_on_white.png")
    expected_path_4 = os.path.join(expected_folder, "expected_green_circle_fill.png")
    x4, y4 = 0, 0  # Top-left corner (white background)
    replacement_color_4 = MAGENTA
    generate_circle_on_background(WHITE, GREEN, in_path_4, HALF_SIZE, HALF_SIZE, EIGHTH_SIZE * 3)
    original_data_4 = images.load(in_path_4)
    expected_data_4 = _generate_expected_flood_fill(original_data_4, x4, y4, replacement_color_4)
    images.save(expected_data_4, expected_path_4)
    print(f"Generated {expected_path_4}")

    # Test Case 5: Complex Shape (Hollow rectangle with diagonal line on white background)
    in_path_5 = os.path.join(input_folder, "complex_shape_fill.png")
    expected_path_5 = os.path.join(expected_folder, "expected_complex_shape_fill.png")
    x5, y5 = 8, 8  # A white pixel inside the hollow rectangle
    replacement_color_5 = YELLOW
    generate_complex_shape(in_path_5)
    original_data_5 = images.load(in_path_5)
    expected_data_5 = _generate_expected_flood_fill(original_data_5, x5, y5, replacement_color_5)
    images.save(expected_data_5, expected_path_5)
    print(f"Generated {expected_path_5}")

    print("\nAll test images and expected results generated.")
