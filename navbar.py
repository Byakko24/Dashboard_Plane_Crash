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
#app.layout = dbc.Container([my_title, my_graph, dropdown])
SIDEBAR_STYLE = {"position":"fixed", "top": 0, "left": 0, "bottom": 0, "width": "16rem", "padding": "2rem 1rem", "background-color": "#f8f9fa"}
CONTENT_STYLE = {"margin-left": "18rem", "maring-right": "2rem", "padding": "2rem 1rem"}

sidebar = html.Div([
    html.H2("Sidebar", className="display-4"),
    html.Hr(),
    html.P("Nbe de crashs suivant différents paramètres", className="lead"),
    dbc.Nav(
        [
            dbc.NavLink("Home", href='/', active="exact"),
            dbc.NavLink("Page 1", href="/page-1", active="exact")
        ],
        vertical=True,
        pills=True
    )
], style=SIDEBAR_STYLE)

content = html.Div(id='Page-Content', children=[], style=CONTENT_STYLE)
app.layout = html.Div([
    dcc.Location(id='url'), sidebar, content
])

@app.callback(
    Output("Page-Content", "children"),
    [Input('url', 'pathname')]
)
def page_content(pathname):
    if pathname == '/':
        return [
            html.H1('Nbe crashs par région', style={'textAlign':'center'}),
            dcc.Graph(id='bargraph', figure=px.bar(df.Region.value_counts(), color=df.Region.value_counts(),
                     color_continuous_scale=px.colors.sequential.Viridis, title='Nbe de crashs par région'))
        ]
    elif pathname == '/page-1':
        return [
            html.H1('Nbe crashs par région', style={'textAlign': 'center'}),
            dcc.Graph(id='piegraph', figure=px.pie(df, names=df.Region.value_counts().index, values=df.Region.value_counts(), color=df.Region.value_counts(), title='Nbe crashs par région', hole=.4))
        ]


"""
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
"""

if __name__ == '__main__':
    app.run_server(debug=True)

