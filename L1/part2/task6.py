class BinaryTree:

	def __init__(self, product_id: int, product_price):
		self.product_id = product_id
		self.product_price = product_price
		self.left = None
		self.right = None

	def __str__(self):
		return f'Node [{str(self.product_id)}] {str(self.product_price)}'

	def _find_node_data(self, product_id):
		if product_id < self.product_id:
			if self.left is None:
				return None
			return self.left._find_node_data(product_id)
		elif product_id > self.product_id:
			if self.right is None:
				return None
			return self.right._find_node_data(product_id)
		else:
			return self.product_price

	def get_product_cost(self, product_id: int, count: int):
		product_price = self._find_node_data(product_id)
		if product_price is not None:
			return product_price * count
		return f'Not found product with ID {product_id}'


if __name__ == '__main__':
	tree = BinaryTree(22, 2.5)
	tree.left = BinaryTree(11, 10.25)
	tree.right = BinaryTree(23, 3)
	tree.left.left = BinaryTree(9, 12.3)
	tree.left.right = BinaryTree(10, 8)
	tree.right.left = BinaryTree(24, 4.8)
	tree.right.right = BinaryTree(30, 8.5)

	product_id = int(input("Enter product ID: "))
	product_count = int(input("Enter product count: "))
	print("Total product price: " + str(tree.get_product_cost(product_id, product_count)))
