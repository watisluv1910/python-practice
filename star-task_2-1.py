import numpy as np


def add(a, b):
    np_a, np_b = np.array(a), np.array(b)
    if np_a.shape == np_b.shape:
        flat_np_a, flat_np_b = np_a.flatten(), np_b.flatten()
        return [flat_np_a[i] + flat_np_b[i] for i in range(len(flat_np_a))]
    else:
        raise ValueError("Initial matrices must be the same shape.")


if __name__ == "__main__":
    add([[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]])
