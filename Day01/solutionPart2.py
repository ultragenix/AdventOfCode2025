"""
Advent of Code 2025 - Day 01 Part 2 Solution
Circular position tracker with rotation commands - Enhanced counting

PART 2 CHANGE: Now counts EVERY time position 0 is reached during
rotations, not just the final position. For example, if rotating right
from position 98 by 5 steps (98→99→0→1→2→3), position 0 is reached
once during the rotation. If rotating by 105 steps, position 0 would
be reached twice (going around the circle).
"""

# Input file path containing rotation commands (L/R followed by number)
input_path = "/home/genix/Workspace/AdventOfCode/Day01/input.txt"


def rotationCall(current_position, selected_input):
    """
    Parse and execute a rotation command, counting all passes through
    position 0.

    Args:
        current_position: Current position on the circular track (0-99)
        selected_input: Command string starting with 'L' or 'R'
                        followed by a number

    Returns:
        tuple: (new_position, zero_count) where zero_count is how
               many times position 0 was reached during this rotation
    """
    all_zero_count = 0
    # Check if command is a left rotation (e.g., 'L5')
    if selected_input.startswith("L"):
        number_rotation = int(selected_input[1:])  # Extract number after 'L'
        new_position, zero_count = rotationLeft(
            current_position, number_rotation)

        all_zero_count += zero_count

    # Check if command is a right rotation (e.g., 'R3')
    if selected_input.startswith("R"):
        number_rotation = int(selected_input[1:])  # Extract number after 'R'
        new_position, zero_count = rotationRight(
            current_position, number_rotation)

        all_zero_count += zero_count

    return new_position, all_zero_count


def rotationLeft(current_position, number_rotation):
    """
    Rotate left (counter-clockwise) on the circular track.
    Counts each time position 0 is passed through during the rotation.

    Args:
        current_position: Current position (0-99)
        number_rotation: Number of steps to rotate left

    Returns:
        tuple: (new_position, zero_count) where zero_count is how many times
               position 0 was reached during this rotation
    """
    zero_count = 0

    # Rotate left one step at a time, counting 0 passages
    for _ in range(number_rotation):
        current_position -= 1

        # Count if we land on position 0 during rotation
        if current_position == 0:
            zero_count += 1

        # Wrap around: if position goes below 0, jump to 99
        if current_position == -1:
            current_position = 99

    return current_position, zero_count


def rotationRight(current_position, number_rotation):
    """
    Rotate right (clockwise) on the circular track.
    Counts each time position 0 is passed through during the rotation.

    Args:
        current_position: Current position (0-99)
        number_rotation: Number of steps to rotate right

    Returns:
        tuple: (new_position, zero_count) where zero_count is how many times
               position 0 was reached during this rotation
    """
    zero_count = 0

    # Rotate right one step at a time, counting 0 passages
    for _ in range(number_rotation):
        current_position += 1

        # Wrap around: if position reaches 100, jump to 0
        if current_position == 100:
            current_position = 0

        # Count if we land on position 0 during rotation
        # KEY difference from Part 1: count EVERY time we hit 0,
        # not just final position
        if current_position == 0:
            zero_count += 1

    return current_position, zero_count


# Main puzzle execution - Part 2
# Starting position for the puzzle
current_position = 50

# Counter for how many times we reach position 0
# (counting all passes during rotations)
solution = 0

# Read and process each rotation command from input file
with open(input_path) as f:
    for line in f:
        # Execute the rotation command and get the count of 0 passages
        current_position, zero_count = rotationCall(current_position, line)
        print(current_position)

        # Add all the times we passed through 0 during this rotation
        solution += zero_count

# Display the final answer
print(f'la solution est :{solution}')


if __name__ == "__main__":
    print("ok")
