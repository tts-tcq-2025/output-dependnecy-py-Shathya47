

def get_color_map():
    major_colors = ["White", "Red", "Black", "Yellow", "Violet"]
    minor_colors = ["Blue", "Orange", "Green", "Brown", "Slate"]
    color_map = []
    for i, major in enumerate(major_colors):
        for j, minor in enumerate(minor_colors):
            pair_number = i * 5 + j
            color_map.append((pair_number, major, minor))
    return color_map

def format_color_map(color_map):
    lines = []
    for pair_number, major, minor in color_map:
        # BUG: No padding in formatting, causes misalignment
        line = f'{pair_number} | {major} | {minor}'  # <-- intentionally buggy
        lines.append(line)
    return lines

def print_color_map():
    color_map = get_color_map()
    lines = format_color_map(color_map)
    for line in lines:
        print(line)
    return len(lines)




from color_map_module import get_color_map, format_color_map, print_color_map

def test_color_map_count():
    result = print_color_map()
    assert result == 25, f"Expected 25 pairs, but got {result}"

def test_format_structure():
    color_map = get_color_map()
    lines = format_color_map(color_map)
    for line in lines:
        parts = line.split('|')
        assert len(parts) == 3, f"Line formatting broken: {line}"
        assert parts[0].strip().isdigit(), f"Pair number not a digit: {parts[0]}"
        assert parts[1].strip() in ["White", "Red", "Black", "Yellow", "Violet"], f"Unexpected major color: {parts[1]}"
        assert parts[2].strip() in ["Blue", "Orange", "Green", "Brown", "Slate"], f"Unexpected minor color: {parts[2]}"

def test_separator_alignment():
    color_map = get_color_map()
    lines = format_color_map(color_map)
    bar_positions = [line.index('|') for line in lines]
    assert len(set(bar_positions)) == 1, f"Inconsistent '|' alignment: {bar_positions}"

def test_visual_alignment_example():
    color_map = get_color_map()
    lines = format_color_map(color_map)

    # Compare line with single-digit number vs double-digit number
    line_0 = lines[0]   # "0 | White | Blue"
    line_10 = lines[10] # "10 | Red | Green"
    pos_0 = line_0.find('|')
    pos_10 = line_10.find('|')
    assert pos_0 == pos_10, (
        f"Misaligned lines:\n'{line_0}'\n'{line_10}'\n"
        f"Expected '|' at same position, got {pos_0} vs {pos_10}"
    )

if __name__ == "__main__":
    test_color_map_count()
    test_format_structure()
    test_separator_alignment()
    test_visual_alignment_example()
    print("All tests completed.")
