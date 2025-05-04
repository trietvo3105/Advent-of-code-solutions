import argparse
import re

from utils import read_input


def find_multiplication_inputs(text: str):
    pattern = r"mul\((\d+),(\d+)\)"
    mult_pairs = re.findall(pattern, text)
    mult_pairs = [(int(x), int(y)) for x, y in mult_pairs]
    return mult_pairs


def find_multiplication_inputs_with_instruction(text: str):
    pattern = r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)"
    founds = re.finditer(pattern, text)
    mult_pairs = []
    mult_ok = True
    for found in founds:
        if found.group(0) == "do()":
            mult_ok = True
        elif found.group(0) == "don't()":
            mult_ok = False
        elif mult_ok:
            mult_pairs.append((int(found.group(1)), int(found.group(2))))
    return mult_pairs


def multiply(pair):
    x, y = pair
    return x * y


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "input_file", type=str, help="Input file of corrupted multiplication program"
    )
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse_arguments()
    corrupted_program = read_input(**vars(args), astype=str)
    whole_text = "".join([text for line in corrupted_program for text in line])
    pairs = find_multiplication_inputs(whole_text)
    multiply_results = list(map(multiply, pairs))
    print(
        f"Result (sum of multiplications) of the corrupted program is {sum(multiply_results)}"
    )

    pairs = find_multiplication_inputs_with_instruction(whole_text)
    multiply_results = list(map(multiply, pairs))
    print(
        f"Result (sum of multiplications) of the corrupted program with do() and don't() instruction is {sum(multiply_results)}"
    )
