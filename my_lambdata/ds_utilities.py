import pandas as pd
from sklearn.model_selection import train_test_split
from tabulate import tabulate


class DfHelper():

    def __init__(self, df):
        self.df = df.copy()

    def enlarge(self, n):
        """
        This function will multiply the input by 100
        """
        return n*100

    def has_null(self, details=True):
        """ has_null:

              Takes in a dataframe (df) and returns a value of
              True if the dataframe has null values or False if
              the dataframe does not containe null values.

              By default, this also prints a table showing which
              features contain null values as well as how many null
              values they contain. This cant be disabled by passing
              in a False value for details.

              -----------
              Parameters:
              -----------

                  df (pd.DataFrame): A DataFrame that will be checked for
                                    null values.

                  details (boolean): True or False, will determine whether
                                    or not the detailed table will be
                                    displayed.
        """
        df = self.df.copy()
        count = 0
        data = []

        for null, feature in zip(df.isnull().sum(), df.isnull().sum().index):
            data.append([feature, null])
            count += null

        data.append(['Total', count])

        if details:
            print(tabulate(data, headers=('Feature', 'Nulls')))

        if count > 0:
            return True
        else:
            return False

    def train_val_test(self, train_size=0.7, val_size=0.5):
        """train_val_test:

              This function splits a dataframe into train, validation
              and test sets.  By default it splits the dataframe 70%/15%/15%
              into train, validation, and test respectively

              ----------
              Parameters
              ----------

                df (pd.DataFrame): a dataframe to be split

                train_size (float): float between 0 and 1 that will determine
                                    the percentage of the original dataframe
                                    that will be used to make the train set.

                val_size (float): float between 0 and 1 that will determine
                                  the percentage of the remaining dataframe
                                  that will be used to make the validation
                                  set. The remaining percentage will be used
                                  to make the test set.
        """
        df = self.df.copy()

        train, val_test = train_test_split(df, train_size=train_size)
        val, test = train_test_split(val_test, train_size=val_size)

        return train, val, test
