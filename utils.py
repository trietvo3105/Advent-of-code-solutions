import os
import numpy as np


def read_input(input_file, astype=int):
    assert os.path.isfile(input_file) and input_file.endswith(".txt")
    try:
        return np.loadtxt(input_file).astype(astype)
    except Exception:
        data = []
        with open(input_file, "r") as f:
            for line in f:
                numbers = list(map(astype, line.strip().split()))
                data.append(numbers)
        return data
