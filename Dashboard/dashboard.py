import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objects as go

app = dash.Dash(__name__)


app.layout = html.Div([
    html.P("Index:"),
    dcc.Dropdown(
        id="dropdown",
        options=[
            {'label': x, 'value': x}
            for x in ['Health', 'Distribution']
        ],
        value='Health',
        clearable=False,
    ),
    dcc.Graph(id="graph"),
])


@app.callback(
    Output("graph", "figure"), 
    [Input("dropdown", "value")])
def display_index(area):
    if area == "Health":
        fig = go.Figure(
            data=go.Bar(y=[3.7, 1.7], 
                x = ["Women", "Men"],
                marker=dict(color = [1, 2],
                        colorscale = "viridis")))
        fig.update_layout(title="Average number of sick days by gender")
    elif area == "Distribution":
        fig = go.Figure(
            data=go.Bar(y=[725, 6914], 
                x = ["Women", "Men"],
                marker=dict(color = [1, 2],
                        colorscale = "viridis")))
        fig.update_layout(title="Number of employees by gender")
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
