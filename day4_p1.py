import argparse

from utils import read_input


def generate_search_grid():
    """
    [(-1, -1), (0, -1), (1, -1),
    (-1, 0), (0, 0), (1, 0),
    (-1, 1), (0, 1), (1, 1)]
    """
    grid = []
    for j in range(-1, 2):
        for i in range(-1, 2):
            grid.append((i, j))
    return grid


def check_one_position(all_characters, word, i, j, grid):
    if all_characters[j][i] != word[0]:
        return []
    n_rows = len(all_characters)
    n_cols = len(all_characters[0])
    good_match_indices = []
    for gx, gy in grid:
        good_grid = True
        match = []
        for cid, c in enumerate(word):
            cx = i + cid * gx
            cy = j + cid * gy
            if (
                (cx < 0)
                or (cx >= n_cols)
                or (cy < 0)
                or (cy >= n_rows)
                or all_characters[cy][cx] != c
            ):
                good_grid = False
                break
            match.append((cx, cy))
        if good_grid:
            good_match_indices.append(match)

    return good_match_indices


def search_for_word(input_file, word):
    input = read_input(input_file, astype=str)
    input = [text for line in input for text in line]
    assert len(input) > 0
    grid = generate_search_grid()
    n_rows = len(input)
    n_cols = len(input[0])
    all_good_match_indices = []
    for j in range(n_rows):
        for i in range(n_cols):
            good_match_indices = check_one_position(input, word, i, j, grid)
            all_good_match_indices.extend(good_match_indices)
    print(f"Found {len(all_good_match_indices)} instances of {word}")
    return all_good_match_indices


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", type=str, help="Input file for the word search")
    parser.add_argument("word", type=str, default="XMAS", help="Word to search")
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse_arguments()
    all_good_match_indices = search_for_word(**vars(args))
