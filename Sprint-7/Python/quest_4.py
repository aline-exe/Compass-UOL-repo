import pandas

df = pandas.read_csv('Sprint-7\\Python\\actors.csv')

frequencia = df['#1 Movie'].value_counts()
mais_frequente = frequencia[frequencia>=3] #imprimir só os que aparecem 3 ou mais vezes

if __name__ == '__main__':
        print (f'{mais_frequente}')