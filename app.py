from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Список заказов
orders = []

@app.route('/')
def index():
    return render_template('index.html', orders=orders)

@app.route('/add', methods=['POST'])
def add_order():
    order = request.form.get('order')
    if order:
        orders.append({'name': order, 'status': 'Cooking'})
    return redirect(url_for('index'))

@app.route('/delete/<int:order_id>', methods=['POST'])
def delete_order(order_id):
    if 0 <= order_id < len(orders):
        orders.pop(order_id)
    return redirect(url_for('index'))


@app.route('/update/<int:order_id>', methods=['POST'])
def update_order(order_id):
    if 0 <= order_id < len(orders):
        new_status = request.form.get('status')
        if new_status in ['Cooking', 'Prepared']:
            orders[order_id]['status'] = new_status
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
