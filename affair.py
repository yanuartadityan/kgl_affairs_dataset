import numpy as np
import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt
import seaborn as sns


class AffairState(object):
    def __init__(self):
        pass


def main():
    # print description
    print(sm.datasets.fair.NOTE)

    # load to dataframe
    df = sm.datasets.fair.load_pandas().data

    # print correlation
    sns.pairplot(df, markers='+')
    plt.show()

if __name__ == '__main__':
    main()