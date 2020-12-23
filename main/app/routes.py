from flask import jsonify, request
from app import app, db
from app.models import Product

@app.route('/api/products')
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
