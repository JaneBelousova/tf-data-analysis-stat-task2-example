import pandas as pd
import numpy as np

from scipy.stats import norm

chat_id = 1124136722 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    m = 0
    N = 2
    alpha = 1 - p
    return np.sqrt(N / 47) * (x.mean() - m) / norm.ppf(alpha / 2), np.sqrt(N / 47) * (x.mean() - m) / norm.ppf(1 - alpha / 2)
