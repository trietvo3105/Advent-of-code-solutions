import os
import argparse
import numpy as np

from utils import read_input


def check_one_report(levels: list):
    if len(levels) <= 2:
        return False
    level_diffs = np.diff(levels)
    safe = (
        ((level_diffs > 0).all() or (level_diffs < 0).all())
        and (np.abs(level_diffs) >= 1).all()
        and (np.abs(level_diffs) <= 3).all()
    )
    return safe


def check_one_report_with_problem_dampener(levels: list):
    if check_one_report(levels):
        return True
    for i in range(len(levels)):
        new_levels = [levels[j] for j in range(len(levels)) if j != i]
        if check_one_report(new_levels):
            return True
    return False


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", type=str, help="Input file of reports' levels")
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse_arguments()
    reports_levels = read_input(**vars(args))
    print("Checking reports...")
    count_safe = 0
    for idx, report in enumerate(reports_levels):
        report_safe = check_one_report(report)
        count_safe += int(report_safe)
        # print(f"\tReport {idx} is {'safe' if report_safe else 'unsafe'}")
    print(f"--> There are {count_safe} safe reports")

    print("Checking reports with Problem Dampener...")
    count_safe = 0
    for idx, report in enumerate(reports_levels):
        report_safe = check_one_report_with_problem_dampener(report)
        count_safe += int(report_safe)
        # print(f"\tReport {idx} is {'safe' if report_safe else 'unsafe'}")
    print(f"--> There are {count_safe} safe reports")
