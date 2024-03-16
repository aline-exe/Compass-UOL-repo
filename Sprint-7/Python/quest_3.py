import pandas 

df = pandas.read_csv('Sprint-7\\Python\\actors.csv')

media_ator = df.groupby ('Actor') ['Number of Movies'].mean() #agrupar a media dos filmes por nome de ator

maior_media_nome = media_ator.idxmin()


if __name__ == '__main__':
    print (f'{maior_media_nome}')