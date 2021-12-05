import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go


app = dash.Dash(__name__)

TEMPLATE = 'plotly_white'

app.layout = html.Div([
    html.H1("Gender Equality Index", 
        style={'color': '#3da4ab', 
        'fontSize': 24, 
        'text-align' : 'center',
        'font-family' : 'Gill Sans',
        }),
    html.Div(children=[
        dcc.Graph(id="health", style={'display': 'inline-block', 'width': '33%'}),
        dcc.Graph(id="distribution", style={'display': 'inline-block', 'width': '33%'}),
        dcc.Graph(id="pay", style={'display': 'inline-block', 'width': '33%'}),
    ]),
    html.P("Choose what you care about:"),
    dcc.Dropdown(
        id="dropdown",
        options=[
            {'label': x, 'value': x}
            for x in ['Health', 'Distribution']
        ],
        value='Distribution',
        clearable=False,
    ),
])

@app.callback(
    Output(component_id="health", component_property="figure"), 
    [Input("dropdown", "value")])
def display_health(value):
    fig = go.Figure(
        data=go.Bar(y=[8.6, 3.0], 
            x = ["Women", "Men"],
            marker=dict(color = ['#3da4ab', '#fe8a71'])))
    fig.update_layout(
        title="Average number of sick days by gender",
        template=TEMPLATE,
    )
    return fig

@app.callback(
    Output(component_id="distribution", component_property="figure"), 
    [Input("dropdown", "value")])
def display_distribution(value):
    fig = go.Figure(
        data=[go.Pie(labels=["Women", "Men"], 
            values=[12821, 49129], 
            hole=.5,
            marker=dict(colors = ['#3da4ab', '#fe8a71']))])
    fig.update_layout(
        title="Number of employees by gender",
        template=TEMPLATE,
    )
    return fig

@app.callback(
    Output(component_id="pay", component_property="figure"), 
    [Input("dropdown", "value")])
def display_pay(value):
    years = list(range(2014, 2019))
    male_pay = [100] * len(years)
    female_pay = [96, 97, 96, 101, 98]
    fig = go.Figure(
        data = [
            go.Scatter(x=years, y=male_pay,
                        mode='lines+markers',
                        name='Men',
                        marker_color='#fe8a71'),
            go.Scatter(x=years, y=female_pay,
                        mode='lines+markers',
                        name='Women',
                        marker_color='#3da4ab')
        ]
    )
    fig.update_layout(
        title="Average pay since 2014",
        template=TEMPLATE,
    )
    return fig

if __name__ == "__main__":
    app.run_server(debug=True)
