from flask import Flask, request, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = '15198309'


productos = []

@app.route("/")
def index():
    return render_template('index.html', productos=productos)

@app.route("/nuevo", methods=['GET', 'POST'])
def nuevo():
    if request.method == 'POST':
        id_producto = len(productos) + 1  # Generar ID único
        nombre = request.form['nombre']
        cantidad = request.form['cantidad']
        precio = request.form['precio']
        categoria = request.form['categoria']
        fecha_vencimiento = request.form['fecha_vencimiento']

 
        nuevo_producto = {
            'id': id_producto,
            'nombre': nombre,
            'cantidad': cantidad,
            'precio': precio,
            'categoria': categoria,
            'fecha_vencimiento': fecha_vencimiento
        }

        productos.append(nuevo_producto)
        return redirect(url_for('index'))

    return render_template('nuevo.html')

@app.route("/editar/<int:id>", methods=['GET', 'POST'])
def editar(id):
    producto = next((p for p in productos if p['id'] == id), None)

    if request.method == 'POST':
        if producto:
            producto['nombre'] = request.form['nombre']
            producto['cantidad'] = request.form['cantidad']
            producto['precio'] = request.form['precio']
            producto['categoria'] = request.form['categoria']
            producto['fecha_vencimiento'] = request.form['fecha_vencimiento']
        return redirect(url_for('index'))

    return render_template('editar.html', producto=producto)

@app.route("/eliminar/<int:id>", methods=["POST"])
def eliminar(id):
    global productos
    productos = [p for p in productos if p['id'] != id]
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)