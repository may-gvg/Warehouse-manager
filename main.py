import csv

from flask import Flask, render_template, request
from wtforms import Form, BooleanField, StringField, PasswordField, validators, IntegerField, DecimalField

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    print("We received GET")
    return render_template("homepage.html")


@app.route('/product/', methods=['GET', 'POST'])
def list_products():
    print("We received GET")
    form = ProductForm(request.form)
    if request.method == 'POST' and form.validate():
        print(form.data)
        product = Product(name=form.data['name'], unit=form.data['unit'], unit_price=form.data['unit_price'], quantity=form.data['quantity'])
        items2[product.name] = product
        pass
    return render_template("product_list.html", items=items2, form=form)


class Product:
    def __init__(self, name, unit, unit_price, quantity):
        self.name = name
        self.unit = unit
        self.unit_price = unit_price
        self.quantity = quantity


class ProductForm(Form):
    name = StringField('Name', [validators.Required()])
    quantity = IntegerField('Quanity', [validators.Required()])
    unit = IntegerField('Unit', [validators.Required()])
    unit_price = DecimalField('Quanity', [validators.Required()])


product_1 = Product(name="Ryż", unit="kg", unit_price=10, quantity=93)
product_2 = Product(name="Sól", unit="kg", unit_price=2.34, quantity=7)
product_3 = Product(name="Ziemniaki", unit="l", unit_price=9, quantity=35)
product_4 = Product(name="Buraki", unit="m", unit_price=8, quantity=1)
product_5 = Product(name="Śledzie", unit="kg", unit_price=23, quantity=66)
product_6 = Product(name="Wołowina", unit="kg", unit_price=33, quantity=34)

items = [product_1, product_2, product_3, product_4, product_5, product_6]

items2 = {product_1.name: product_1,
          product_2.name: product_2,
          product_3.name: product_3,
          product_4.name: product_4,
          product_5.name: product_5,
          product_6.name: product_6
          }

with open('items.csv', 'w', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    for key, value in items2.items():
        l = [value.name, value.quantity, value.unit, value.unit_price]
        csvwriter.writerow(l)






if __name__ == '__main__':
    app.run()
