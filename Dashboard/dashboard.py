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
    html.Div(children=[
        html.P("Rate to what extent you care about the following factors:",
            style={'color': '#3da4ab', 
            'fontSize': 19, 
            'text-align' : 'center',
            'font-family' : 'Gill Sans',
            }),
        dcc.Slider(
            id='slider-health',
            min=1,
            max=5,
            step=0.5,
            value=10,
            marks={
                1: '1',
                2: '2',
                3: '3',
                4: '4',
                5: '5'
            },
            tooltip={"placement": "left", "always_visible": True},
        ),
        html.Br(),
        dcc.Slider(
            id='slider-distribution',
            min=1,
            max=5,
            step=0.5,
            value=10,
            marks={
                1: '1',
                2: '2',
                3: '3',
                4: '4',
                5: '5'
            },
            tooltip={"placement": "left", "always_visible": True},
        ),
        html.Br(),
        dcc.Slider(
            id='slider-pay',
            min=1,
            max=5,
            step=0.5,
            value=10,
            marks={
                1: '1',
                2: '2',
                3: '3',
                4: '4',
                5: '5'
            },
            tooltip={"placement": "left", "always_visible": True},
        )],
        style={'width': '50%', 'padding' : 50, 'margin' : '0 auto'},
    ),
    dcc.Dropdown(
        id="dropdown",
        options=[
            {'label': x, 'value': x}
            for x in ['Health', 'Distribution']
        ],
        value='Distribution',
        clearable=False,
    ),
    dcc.Graph(id="index"),
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

@app.callback(
    Output(component_id="index", component_property="figure"), 
    [Input("dropdown", "value")])
def display_index(value):
    opacity = [0.5, 0.7, 0.9]
    rgba = [
        "rgba(89, 209, 240, ",
        "rgba(9, 158, 109, ",
        "rgba(235, 96, 61, ",
    ]
    colors = []
    for i in range(len(opacity)):
        color = rgba[i] + str(opacity[i]) + ")"
        colors.append(color)
    fig = go.Figure(go.Barpolar(
        r=[0.75, 1.8, 1.3],
        theta=[30, 90, 150],
        width=[58] * 3,
        marker_color=colors,
    ))

    fig.update_layout(
        template='simple_white',
        polar = dict(
            radialaxis = dict(range=[0, 2], showticklabels=False, ticks=''),
            angularaxis = dict(showticklabels=False, ticks=''),
            sector = [0, 180],
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )

    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
