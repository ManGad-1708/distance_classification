import pandas as pd

data = {
    "Feature1": [1, 2, 3, 4, 5],
    "Feature2": [5, 4, 3, 2, 1],
    "Label": ["A", "B", "A", "B", "A"]
}

df = pd.DataFrame(data)
print(df.head())