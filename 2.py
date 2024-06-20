from flask import Flask, render_template, request, redirect, url_for
from database import db, Item

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

    if not Item.query.all():
        default_items = [
            {'name': 'Молоко', 'price': 50},
            {'name': 'Хлеб', 'price': 30},
            {'name': 'Яйца', 'price': 70}
        ]
        for item in default_items:
            db.session.add(Item(name=item['name'], price=item['price']))
        db.session.commit()

@app.route('/')
def index():
    inventory = Item.query.all()
    return render_template('index1.html', inventory=inventory)

@app.route('/add', methods=['POST'])
def add_item():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        new_item = Item(name=name, price=int(price))
        db.session.add(new_item)
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:item_id>', methods=['POST'])
def delete_item(item_id):
    item_to_delete = Item.query.get_or_404(item_id)
    db.session.delete(item_to_delete)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)