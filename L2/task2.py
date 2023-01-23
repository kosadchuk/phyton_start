class Pizza:

	def __init__(self):
		self.name = 'Base'
		self.extra = []
		self.ingredients = ['Cheese', 'Tomato']

	def __str__(self):
		return f'{self.name}  {self.ingredients}  {self.extra}'

	def set_extra(self, extra):
		self.extra.append(extra)



class MondayPizza(Pizza):

	def __init__(self):
		super().__init__()
		self.name = 'Margarita'
		self.ingredients = ['Cheese', 'Tomato', 'Basil']


class TuesdayPizza(Pizza):

	def __init__(self):
		super().__init__()
		self.name = 'Papperoni'
		self.ingredients = ['Cheese', 'Tomato', 'Papperoni']


class WednesdayPizza(Pizza):

	def __init__(self):
		super().__init__()
		self.name = 'Hawaiian'
		self.ingredients = ['Cheese', 'Chicken', 'Pineapple']


class ThursdayPizza(Pizza):

	def __init__(self):
		super().__init__()
		self.name = 'Calzone'
		self.ingredients = ['Cheese', 'Meat', 'Tomato']


class FridayPizza(Pizza):

	def __init__(self):
		super().__init__()
		self.name = '4 seasons'
		self.ingredients = ['Cheese', 'Meat', 'Chicken', 'Ham', 'Basil']



if __name__ == '__main__':

	print('Hello! What is the day of week today?')
	print('\tEnter one of the day:\n\t\tMonday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday')
	day_of_week = input('Your choice: ')

	if day_of_week not in ['Saturday', 'Sunday']:

		get_class = lambda x: globals()[x]
		dow_class = get_class(day_of_week + "Pizza")()

		if dow_class:

			print(f'Today pizza of the day is: {dow_class.name}\nIt is consists of {dow_class.ingredients}')
			print('Do you want some extra ingredients?')
			extra = {'1': 'Ham', '2': 'Pepperoni', '3': 'Double cheese', '4': 'Mushrooms', '5': 'No extra'}
			extra_choice = None

			while extra_choice != '5':
				for i in extra.keys():
					print(f'\t{i} = {extra[i]}')
				extra_choice = input('Enter: ')
				if extra_choice == '5':
					print(f'Your order is pizza-of-the-day {dow_class.name}')
					str = '';
					if len(dow_class.extra) > 0:
						print('With extra: ')
						for i in dow_class.extra:
							print(i)
				elif extra_choice in extra.keys():
					print(f'\n\t{extra[extra_choice]} was added to pizza\n')
					dow_class.set_extra(extra[extra_choice])
					print('Do you want more extra?')
				else:
					print("Wrong input value")

			else:
				print('Wrong input value')
	else:
		print('Sorry, today pizza for business lunches not available')
