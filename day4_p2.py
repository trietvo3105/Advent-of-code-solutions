import argparse

from utils import read_input


def check_one_position_for_crossing(all_characters, word, i, j, grid):
    if len(word) % 2 != 1:
        return []
    middle_character = word[len(word) // 2]
    if all_characters[j][i] != middle_character:
        return []

    n_rows = len(all_characters)
    n_cols = len(all_characters[0])
    extracted_word = ""
    good_match_indices = []
    good_position = True
    for gx, gy in grid:
        cx = i + gx
        cy = j + gy
        if (cx < 0) or (cx >= n_cols) or (cy < 0) or (cy >= n_rows):
            good_position = False
            break
        extracted_word += all_characters[cy][cx]
        good_match_indices.append((cx, cy))
    if good_position and (extracted_word == word or extracted_word == word[::-1]):
        return good_match_indices

    return []


def search_for_crossing_words(input_file, word):
    input = read_input(input_file, astype=str)
    input = [text for line in input for text in line]
    assert len(input) > 0
    half_len_word = len(word) // 2
    grid_1 = [(-1, -1), (1, 1)]
    grid_2 = [(1, -1), (-1, 1)]
    grid_1_extended = []
    grid_2_extended = []
    for idx, ((gx1, gy1), (gx2, gy2)) in enumerate(zip(grid_1, grid_2)):
        iter = (
            range(half_len_word, idx, -1) if idx == 0 else range(idx, half_len_word + 1)
        )
        for i in iter:
            grid_1_extended.append((i * gx1, i * gy1))
            grid_2_extended.append((i * gx2, i * gy2))
        if idx == 0:
            grid_1_extended.append((0, 0))
            grid_2_extended.append((0, 0))

    n_rows = len(input)
    n_cols = len(input[0])
    all_good_match_indices = []
    for j in range(n_rows):
        for i in range(n_cols):
            good_match_indices1 = check_one_position_for_crossing(
                input, word, i, j, grid_1_extended
            )
            good_match_indices2 = check_one_position_for_crossing(
                input, word, i, j, grid_2_extended
            )
            if len(good_match_indices1) and len(good_match_indices2):
                all_good_match_indices.append(good_match_indices1 + good_match_indices2)

    print(
        f"Found {len(all_good_match_indices)} instances of crossing {word}, a.k.a. X-{word}"
    )
    return all_good_match_indices


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", type=str, help="Input file for the word search")
    parser.add_argument("word", type=str, default="MAS", help="Word to search")
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse_arguments()
    all_crossing_good_match_indices = search_for_crossing_words(**vars(args))
