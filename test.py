import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dict_test = {
    "fruits": ["melon", "watermelon"],
    "vegs": ["spinach", "lettuce"]
}

test_df = pd.DataFrame(dict_test)
print(test_df)