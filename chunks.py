import pandas as pd


def readCsv(filename):
    table = pd.read_table(filename, sep=',', chunksize=100)
    i = 0
    for df in table:
        print(df)
        df.to_csv('/Users/macbookpro/Documents/crimes-in-chicago/crime' + str(i) + '.csv')
        i += 1


readCsv('/Users/macbookpro/Documents/crimes-in-chicago/Chicago_Crimes_2012_to_2017.csv')
