import requests
from flask import jsonify, request, abort
from app import app, db
from app.models import Product, ProductUser
from config import Config
from producer import publish

@app.route('/api/products', methods=['GET'])
def list_products():
    data = db.session.query(Product).all()
    return jsonify(data)


@app.route('/api/products', methods=['POST'])
def create_product():
    data = request.json
    product = Product(id=data['id'], title=data['title'], image=data['image'])
    db.session.add(product)
    db.session.commit()
    print('Product Created')
    return jsonify(product)


@app.route('/api/products/<int:id>', methods=['PUT'])
def update_product(id):
    data = request.json
    product = Product.query.get(id)
    product.title = data['title']
    product.image = data['image']
    db.session.commit()
    print('Product Updated')
    return jsonify(product)


@app.route('/api/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get(id)
    db.session.delete(product)
    db.session.commit()
    print('Product Deleted')
    return jsonify(product)

@app.route('/api/products/<int:id>/like', methods=['POST'])
def like(id):
    req = requests.get(f'http://{Config.DOCKER_LOCALHOST}:8000/api/user')
    json = req.json()

    try:
        productUser = ProductUser(user_id=json['id'], product_id=id)
        db.session.add(productUser)
        db.session.commit()

        publish('product_liked', id)
    except:
        abort(400, 'You already liked this product')

    return jsonify({
        'message': 'success'
    })
