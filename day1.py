import os
import argparse
import numpy as np

from utils import read_input


def get_total_different_distance(locations_array: np.ndarray):
    sorted_locs_team1 = np.sort(locations_array[:, 0], axis=0, kind="quicksort")
    sorted_locs_team2 = np.sort(locations_array[:, 1], axis=0, kind="quicksort")
    sorted_locs = np.sum(np.abs(sorted_locs_team1 - sorted_locs_team2))
    return sorted_locs


def get_similarity_score(locations_array: np.ndarray):
    occurrences = np.array(
        [np.count_nonzero(locations_array[:, 1] == x) for x in locations_array[:, 0]]
    )
    return np.sum(occurrences * locations_array[:, 0])


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", type=str, help="Input file of location IDs")
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse_arguments()
    locations = read_input(**vars(args))
    distance = get_total_different_distance(locations)
    similarity_score = get_similarity_score(locations)
    print(f"The distance is {distance}")
    print(f"The similarity score is {similarity_score}")
