import dash
import dash_bootstrap_components as dbc

FONT_AWESOME = dbc.icons.FONT_AWESOME
dbc_css = (
    "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.4/dbc.min.css"
)

styles = [
    "https://fonts.googleapis.com/icon?family=Material+Icons",
    FONT_AWESOME,
    dbc_css,
    dbc.themes.BOOTSTRAP,
]

app = dash.Dash(
    __name__,
    meta_tags=[{"name": "viewport", "content": "width=device-width"}],
    external_stylesheets=styles,
)

app.config["suppress_callback_exceptions"] = True
app.scripts.config.serve_locally = True
server = app.server
