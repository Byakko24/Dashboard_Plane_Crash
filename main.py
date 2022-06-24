from dash import Dash, html, dcc, Output, Input
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

#Récupération des données et mise sous forme d'un dataframe
df = pd.read_csv('Plane Crash dataset.csv', encoding='ISO-8859-1')
df = df.rename(columns={"Flight phase": "flight_phase", "Flight type": "flight_type", "Crash site": "crash_site", "Crash cause": "crash_cause"})

#Création des composants
app = Dash(__name__, external_stylesheets=[dbc.themes.SOLAR])
my_title = dcc.Markdown(children='# Dashboard Plane Crash')
my_graph = dcc.Graph(figure={})
dropdown = dcc.Dropdown(options=['Bar Plot', 'Pie Plot'], value='Bar Plot', clearable=False)


#fig = px.bar(df.Region.value_counts(), color=df.Region.value_counts(), color_continuous_scale=px.colors.sequential.Viridis, title='Nbe de crashs par région')
#fig2 = px.pie(df.flight_phase.value_counts(), color=df.flight_phase.value_counts())

#Construction layout
app.layout = dbc.Container([my_title, my_graph, dropdown])

#Création callbacks
@app.callback(
    Output(my_graph, component_property='figure'),
    Input(dropdown, component_property='value')
)
def my_func(user_input):
    if user_input == 'Bar Plot':
        fig = px.bar(df.Region.value_counts(), color=df.Region.value_counts(),
                     color_continuous_scale=px.colors.sequential.Viridis, title='Nbe de crashs par région')
    elif user_input == 'Pie Plot':
        fig = px.pie(df, names=df.Region.value_counts().index, values=df.Region.value_counts(), color=df.Region.value_counts(), title='Nbe crashs par région', hole=.4)

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)

