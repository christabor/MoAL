# -*- coding: utf-8 -*-

from flask import Flask
from flask import jsonify


app = Flask(__name__)
app.debug = True


@app.route('/product/<product_id>')
def inventory(product_id):
    print('Getting inventory for product: {}'.format(product_id))
    response = jsonify({
        'data': {
            'id': product_id,
            'inventory': 30,
        }
    })
    return response

if __name__ == '__main__':
    app.run(debug=True, port=5003)
