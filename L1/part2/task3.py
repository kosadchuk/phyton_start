class Product:

    def __init__(self, name: str, price: float, description: str):
        self.price = price
        self.description = description
        self.name = name


class Customer:

    def __init__(self, name: str, surname: str, patronymic: str, mobile_phone: str):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.mobile_phone = mobile_phone


class Order:

    def __init__(self, order_id: int):
        self.order_id = order_id
        self.customer = None
        self.products = []
        self.total_price = 0

    def add_customer(self, customer: Customer):
        if isinstance(customer, Customer) and not self.customer:
            self.customer = customer

    def add_product(self, product: Product):
        if isinstance(product, Product):
            self.products.append(product)

    def calc_total_order_price(self):
        self.total_price = 0
        for i, product in enumerate(self.products):
            self.total_price += float(product.price)
        return self.total_price


new_customer = Customer('Kateryna', 'Osadchuk', 'Mykhailivna', "+380632511121")
product_1 = Product('Banana', '67', 'Sweet banana')
product_2 = Product('Milka', '15', 'Chocolate')
new_order = Order(2)

new_order.add_customer(new_customer)
new_order.add_product(product_1)
new_order.add_product(product_2)
print('The total order value', new_order.calc_total_order_price())


