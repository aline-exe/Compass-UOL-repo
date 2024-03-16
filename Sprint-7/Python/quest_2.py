import pandas

df = pandas.read_csv('Sprint-7\\Python\\actors.csv')

mediaf = df['Number of Movies'].mean()

if __name__ == '__main__':
    print (f'{mediaf}')

