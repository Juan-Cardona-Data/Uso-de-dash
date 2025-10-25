import plotly.express as px
from dash import Dash, dcc, html

app = Dash() #Iniciamos una aplicacion tipo dash

datos= px.data.tips() #Cargamos un dataset de ejemplo
mi_figura= px.pie(datos, names="sex",values="tip") #Creamos una figura tipo pie

# Nuevo: usar gapminder para crear un gráfico de barras (esperanza de vida media por continente en 2007)
gap = px.data.gapminder()
gap_2007 = gap[gap["year"] == 2007]
gap_agg = gap_2007.groupby("continent", as_index=False)["lifeExp"].mean()
mi_barra = px.bar(
    gap_agg,
    x="continent",
    y="lifeExp",
    title="Esperanza de vida media por continente (2007)",
    labels={"lifeExp": "Esperanza de vida (años)", "continent": "Continente"},
)

app.layout = html.Div([
    dcc.Graph(figure=mi_figura),
    # Nuevo gráfico colocado justo debajo del pie
    dcc.Graph(figure=mi_barra)
])

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)