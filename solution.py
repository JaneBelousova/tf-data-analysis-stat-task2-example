import pandas as pd
import numpy as np

from scipy.stats import chi2

chat_id = 1124136722 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    N = 2
    alpha = 1 - p
    return np.sqrt((x**2).sum() / 47 / chi2.ppf(1 - alpha / 2, 2 * len(x))), np.sqrt((x**2).sum() / 47 / chi2.ppf(alpha / 2, 2 * len(x)))
