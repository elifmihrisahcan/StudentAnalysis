import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

adp = pd.read_excel("DATA\MAPdata.xlsx")

sns.heatmap(adp.corr(), annot = True)

//nskrkmz iyidir ya.























