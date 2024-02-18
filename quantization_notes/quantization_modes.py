import numpy as np


def quantize_symmetric_full(n: int, x_f: np.array) -> tuple[float, np.array]:
    lower_bound = -pow(2, n) / 2
    upper_bound = pow(2, n) / 2 - 1

    q_x = ((pow(2, n) - 1) / 2) / np.max(np.abs(x_f))
    x_q = np.clip(np.round(q_x * x_f), lower_bound, upper_bound)

    return q_x, x_q


def quantize_symmetric_restricted(n: int, x_f: np.array) -> tuple[float, np.array]:
    lower_bound = -(pow(2, n) / 2 - 1)
    upper_bound = pow(2, n) / 2 - 1

    q_x = (pow(2, n - 1) - 1) / np.max(np.abs(x_f))
    x_q = np.clip(np.round(q_x * x_f), lower_bound, upper_bound)
    return q_x, x_q


def quantize_asymmetric(n: int, x_f: np.array) -> tuple[float, float, np.array]:
    alpha = np.min(x_f)
    beta = np.max(x_f)
    q_x = (pow(2, n) - 1) / (beta - alpha)
    zero_point = np.round(q_x * alpha)

    x_q = np.clip(np.round(q_x * x_f) - zero_point, 0, pow(2, n) - 1)

    return q_x, zero_point, x_q


def dequantize_symmetric(q_x: float, x_q: np.array) -> np.array:
    return x_q / q_x


def dequantize_asymmetric(q_x: float, zero_point: float, x_q: np.array) -> np.array:
    return (x_q + zero_point) / q_x
