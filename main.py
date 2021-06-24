from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    print("We received GET")
    return render_template("homepage.html")


@app.route('/product/', methods=['GET'])
def list_products():
    print("We received GET")
    return render_template("product_list.html")



class Product:
    def __init__(self, name, unit, unit_price, quantity):
        self.name = name
        self.unit = unit
        self.unit_price = unit_price
        self.quantity = quantity


product_1 = Product(name="Ryż", unit="kg", unit_price=10, quantity=93)
product_2 = Product(name="Sól", unit="kg", unit_price=2.34, quantity=7)
product_3 = Product(name="Ziemniaki", unit="l", unit_price=9, quantity=35)
product_4 = Product(name="Buraki", unit="m", unit_price=8, quantity=1)
product_5 = Product(name="Śledzie", unit="kg", unit_price=23, quantity=66)
product_6 = Product(name="Wołowina", unit="kg", unit_price=33, quantity=34)

items = [product_1, product_2, product_3, product_4, product_5, product_6]

if __name__ == '__main__':
    app.run()
