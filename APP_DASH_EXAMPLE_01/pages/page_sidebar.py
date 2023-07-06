import dash
import dash.dcc as dcc
import dash.html as html
import dash_bootstrap_components as dbc

from app import *

# Layout of Dash App
APP_LOGO = app.get_asset_url("itau.png")

layout = html.Div(
    [
        html.Div(
            [
                # width: 3rem ensures the logo is the exact width of the
                # collapsed sidebar (accounting for padding)
                html.Img(src=APP_LOGO, style={"width": "3rem"}),
                html.H2("Footprint - PD"),
            ],
            className="sidebar-header",
        ),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink(
                    [
                        html.I(className="fa-solid fa-house"),
                        html.Span("Home", className="text-side-bar"),
                    ],
                    href="/",
                    active="exact",
                ),
                dbc.NavLink(
                    [
                        html.I(className="fa-solid fa-filter"),
                        html.Span("Funil", className="text-side-bar"),
                    ],
                    href="/pd_funil",
                    active="exact",
                ),
                dbc.NavLink(
                    [
                        html.I(className="fa-solid fa-ranking-star"),
                        html.Span("Ranking", className="text-side-bar"),
                    ],
                    href="/pd_ranking",
                    active="exact",
                ),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    className="sidebar",
)
