import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="white", color_codes=True) 
df = pd.read_csv("/content/Iris.csv")
df.head()

df.plot(kind="scatter", x="SepalLengthCm", y="SepalWidthCm")

sns.jointplot(x="SepalLengthCm", y="SepalWidthCm", data=df, size=5)

sns.FacetGrid(df, hue="Species", size=5).map(plt.scatter, "SepalLengthCm", "SepalWidthCm").add_legend()

sns.boxplot(x="Species", y="PetalLengthCm", data=df)

ax = sns.stripplot(x="Species", y="PetalLengthCm", data=df, jitter=True,edgecolor="gray")

sns.violinplot(x="Species", y="PetalLengthCm", data=df, size=6)

sns.FacetGrid(df, hue="Species", size=6).map(sns.kdeplot, "PetalLengthCm").add_legend()

sns.pairplot(df.drop("Id", axis=1), hue="Species", size=3)

sns.pairplot(df.drop("Id", axis=1), hue="Species", size=3, diag_kind="kde")

df.drop("Id", axis=1).boxplot(by="Species", figsize=(12, 6))

from pandas.plotting import andrews_curves 
andrews_curves(df.drop("Id", axis=1), "Species")

from pandas.plotting import parallel_coordinates
parallel_coordinates(df.drop("Id", axis=1), "Species")

from pandas.plotting import radviz
radviz(df.drop("Id", axis=1), "Species")

#https://colab.research.google.com/drive/13y32mYzpNXv7ErFK2Dc2ueJMT4Msijuy?usp=sharing
#https://towardsdatascience.com/6-lesser-known-pandas-plotting-tools-fda5adb232ef
#https://pandas.pydata.org/docs/reference/api/pandas.plotting.radviz.html
