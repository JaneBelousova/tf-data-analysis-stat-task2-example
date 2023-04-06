import pandas as pd
import numpy as np

from scipy.stats import norm
from scipy.stats import chi2
import statistics as st

chat_id = 1124136722 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    m = 0
    df = 2
    N = 2
    alpha = 1 - p
    return np.sqrt(N * st.variance(x, m) / chi2.ppf(1 - alpha / 2, df) / 47), np.sqrt(N * st.variance(x, m) / chi2.ppf(alpha / 2, df) / 47)
