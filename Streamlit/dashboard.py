import pandas
import streamlit as st
import plotly.express as px
import datetime

# Load data
game_sales_df = pandas.read_csv('Streamlit/game-sales-cleaning.csv')
game_sales_df['Release'] = pandas.to_datetime(game_sales_df['Release'])

min_date = game_sales_df['Release'].min()
max_date = game_sales_df['Release'].max()


def plot_sales_by_year(data):
    sales_by_year = data.groupby(data['Release'].dt.year)[
        'Sales'].sum().reset_index()
    sales_by_year.columns = ['Release', 'Sales']
    fig = px.line(sales_by_year, x='Release', y='Sales',
                  title='Global Sales by Year')
    return fig


def plot_genre_sales(data):
    fig = px.bar(data, x='Genre', y='Sales',
                 title='Global Sales by Genre')
    return fig


def plot_game_sales(data):
    fig = px.bar(data, x='Name', y='Sales',
                 title='Global Sales by Game')
    return fig


def plot_publisher_sales(data):
    fig = px.bar(data, x='Publisher', y='Sales',
                 title='Global Sales by Publisher')
    return fig


def plot_publisher_release_game(data):
    fig = px.bar(data, x='Publisher', y='Name',
                 title='Global Game by Publisher')
    return fig


def filtered_data(data, start_year, end_year):
    return data[(data['Release'].dt.year >= start_year) & (data['Release'].dt.year <= end_year)]


# Sidebar
with st.sidebar:
    st.title('Dashboard')
    st.write('Select a year range')
    start_year, end_year = st.slider('Year Range', min_value=min_date.year,
                                     max_value=max_date.year, value=(min_date.year, max_date.year))

# Main page
with st.container():
    st.title("GAME SALES DASHBOARD")
    filtered_data = filtered_data(game_sales_df, start_year, end_year)

    st.subheader('Game dengan penjualan terbanyak pada tahun ' +
                 str(start_year) + ' - ' + str(end_year))

    st.write(filtered_data['Name'].loc[filtered_data['Sales'].idxmax()])
    st.write('---')
    st.subheader('Grafik penjualan dari tahun ' +
                 str(start_year) + ' - ' + str(end_year))
    st.plotly_chart(plot_sales_by_year(filtered_data))
    st.write('---')
    st.subheader('Grafik penjualan berdasarkan Publisher dari Tahun ' +
                 str(start_year) + ' - ' + str(end_year))
    st.plotly_chart(plot_publisher_sales(
        filtered_data.groupby('Publisher')['Sales'].sum().reset_index().sort_values('Sales', ascending=False).head(5)))
    st.subheader('Publisher dengan game terbanyak dari Tahun ' +
                 str(start_year) + ' - ' + str(end_year))
    st.plotly_chart(plot_publisher_release_game(
        filtered_data.groupby('Publisher')['Name'].count().reset_index().sort_values('Name', ascending=False).head(5)))
    st.write('---')
    st.subheader('Grafik penjualan berdasarkan Genre dari Tahun ' +
                 str(start_year) + ' - ' + str(end_year))
    st.plotly_chart(plot_genre_sales(
        filtered_data.groupby('Genre')['Sales'].sum().reset_index().sort_values('Sales', ascending=False).head(5)))


text_markdown = """
Created by: [Sukma Ramadhan Asri](
   https://www.linkedin.com/in/sukma-ramadhan-asri-96b27518b/)
    github: [Onedayxzn](https://github.com/onedayxzn/Game-Sales)

"""
st.markdown(text_markdown)
