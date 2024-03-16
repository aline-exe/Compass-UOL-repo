import pandas 

df = pandas.read_csv('Sprint-7\\Python\\actors.csv')

ator = df.loc[df['Number of Movies'].idxmax(), 'Actor'] 
n_filmes = df['Number of Movies'].max()

if __name__ == "__main__":
    print (f'{ator}\n{n_filmes}')