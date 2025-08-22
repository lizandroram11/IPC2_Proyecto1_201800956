from graphviz import Digraph

dot = Digraph(comment="Prueba Graphviz", format="png")

dot.node("A", "Nodo A", shape="box", color="lightblue", style="filled")
dot.node("B", "Nodo B", shape="ellipse", color="lightgreen", style="filled")
dot.edge("A", "B", label="conecta")

output_path = dot.render("prueba_grafica", cleanup=True)
print(f"✅ Gráfica generada en: {output_path}")