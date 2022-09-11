# Пятая программа второй практической работы
#
from sklearn.datasets import fetch_california_housing
import pandas as pd
data = fetch_california_housing(as_frame=True)

print(data)
