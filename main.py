# app.py
from flask import Flask, render_template, jsonify, request, session, url_for
import json

app = Flask(__name__)
app.secret_key = 'askdhbshdgfueywjnfkjsadnhzifs'  # Set this to a random secret string in a real application

# Sample product data
products = [
    {"id": 1, "name": "Vintage Chair", "price": 45, "image": "/static/images/chair.jpg"},
    {"id": 2, "name": "Antique Lamp", "price": 30, "image": "/static/images/lamp.jpg"},
    {"id": 3, "name": "Retro Radio", "price": 25, "image": "/static/images/radio.jpg"},
    {"id": 4, "name": "Classic Watch", "price": 50, "image": "/static/images/watch.webp"},
    {"id": 5, "name": "Old Camera", "price": 40, "image": "/static/images/camera.webp"},
    {"id": 6, "name": "Vinyl Records", "price": 15, "image": "/static/images/record.jpg"},
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/products')
def get_products():
    search_query = request.args.get('search', '').lower()
    filtered_products = [product for product in products if search_query in product['name'].lower()]
    return jsonify(filtered_products)

@app.route('/api/cart', methods=['GET', 'POST'])
def cart():
    if request.method == 'POST':
        cart_data = request.json
        session['cart'] = json.dumps(cart_data)
        return jsonify({"status": "success"})
    else:
        cart_data = json.loads(session.get('cart', '[]'))
        return jsonify(cart_data)

@app.route('/cart')
def cart_page():
    return render_template('cart.html')

if __name__ == '__main__':
    app.run(debug=True)