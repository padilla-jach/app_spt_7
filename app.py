#Librerías necesarias
import streamlit as st
import pandas as pd
import plotly.graph_objects as go

#Lectura de la base de datos

df = pd.read_csv('C:/Users/EQUIPO/Downloads/vehicles_us.csv')
df = df.dropna(subset=['model_year'])
df = df[df['model_year'] > 1990]

#Boton para activar el histograma

st.header('Sprint 7: Análisis de la base de datos de la venta de autos')

st.write('Se presentan gráficos indicativos del comportamiento del mercado de autos en Estados Unidos.')

hist_button = st.checkbox('Construir histograma')

distribution_button = st.button('Generar gráfico de dispersión')


# Lógica a ejecutar cuando se hace clic en el botón
if hist_button :
    # Escribir un mensaje en la aplicación
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig_1 = go.Figure(data = [go.Histogram(x = df['model_year'])])
    fig_1.update_layout(title_text = 'Model year')
    st.plotly_chart(fig_1, use_container_width = True)



if distribution_button :

    st.write('Generación de un diagrama de dispersión entre las millas recorridas y el costo del auto')
    fig_2 = go.Figure(data = [go.Scatter(x = df['days_listed'], y = df['price'], mode = 'markers')])
    # Opcional: Puedes añadir un título al gráfico si lo deseas
    fig_2.update_layout(title_text = 'days V. Price')
    fig_2.update_xaxes(title_text = 'days in the market')
    fig_2.update_yaxes(title_text = 'price (dollars)')
    st.plotly_chart(fig_2, use_container_width = True)