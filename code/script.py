import pandas as pd
import pathlib
import plotly.express as px
import os



def extraer(url):

    data = pd.read_csv(url, delimiter=';')

    return data



def asdate(df):

    df['dt'] = pd.to_datetime(df['dt'])

    df['year'] = df['dt'].dt.year

    return df


if __name__ == '__main__':

    url = '../data/datos_mock.csv'


    data = extraer(url)

    data = asdate(data)

    data.head(5)

    fig = px.line(data, x='dt', y='valor', title='Gráfico Interactivo de Líneas')


    fig.show()

    ruta = os.path.join('..', 'results', 'grafico_interactivo.html')

    os.makedirs(os.path.dirname(ruta), exist_ok=True)

    fig.write_html(ruta)


