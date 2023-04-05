import pandas as pd
import numpy as np

from scipy.stats import norm
from scipy.stats import chi2

chat_id = 1124136722 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    return (np.sqrt((x.mean()**2 ) / chi2.ppf(1 - alpha / 2)) / 47), \
           (np.sqrt((x.mean()**2 ) / chi2.ppf(alpha / 2)) / 47)
