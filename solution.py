import pandas as pd
import numpy as np


chat_id = 707776914 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    n = len(x)
    s = np.sum(x)
    estimate = 2 * s / (n * 56**2)
    return estimate
