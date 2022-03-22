import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

dict_test = {
    "a": [1, 2, 3],
    "b": [4, 5, 6]
}

test_df = pd.DataFrame(dict_test)

plot = sns.lineplot(data = test_df, x = "a", y = "b")
plt.show()