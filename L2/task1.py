
class Ticket:

	def __init__(self, ticket_id, price):
		self.ticket_id = ticket_id
		self.price = price

	def __str__(self):
		return f'{self.ticket_id} {self.price}'

	def print_ticket(self):
		return f"""\n
	    ******************************************************
	    *                                                    *
	       Ticket № {self.ticket_id}                        
	       Price {self.get_ticket_price()}                   
	    *                                                    *
	    ******************************************************"""

	def get_ticket_price(self):
		return self.price


class Events:
	def __init__(self, event_name, event_price):
		self.event_name = event_name
		self.event_price = event_price


class RegularTicket(Ticket):

	def __init__(self, ticket_id, price):
		super().__init__(ticket_id, price)


class AdvanceTicket(Ticket):

	def __init__(self, ticket_id, price):
		super().__init__(ticket_id, price)

	def get_ticket_price(self):
		regular_price = super().get_ticket_price()
		return regular_price * 0.6


class LateTicket(Ticket):

	def __init__(self, ticket_id, price):
		super().__init__(ticket_id, price)

	def get_ticket_price(self):
		regular_price = super().get_ticket_price()
		return regular_price * 1.10


class StudentTicket(Ticket):

	def __init__(self, ticket_id, price):
		super().__init__(ticket_id, price)

	def get_ticket_price(self):
		regular_price = super().get_ticket_price()
		return regular_price * 0.5


if __name__ == '__main__':

	event1 = Events('DOU event', 2000)
	event2 = Events('Web Seminar', 1500)
	event3 = Events('Start IT', 4000)

	print('Hello! What event do you want to visit?\n')
	print(f'\t1 = {event1.event_name}')
	print(f'\t2 = {event2.event_name}')
	print(f'\t3 = {event3.event_name}')

	event_id = input("\nEnter your choice: ")

	event = None
	if event_id == '1':
		event = event1
	elif event_id == '2':
		event = event2
	elif event_id == '3':
		event = event3
	else:
		print("Wrong input value")

	if event is not None:
		print(f'\nBasic price for this event is: {event.event_price}\n')
		print('What kind of ticket do you want to buy?\n')
		print('\t1 = Regular\n\t2 = Advance (-40%)\n\t3 = Late(+10%)\n\t4 = Student(-50%)\n')
		type = input("Enter your choice: ")
		ticket = None
		if type == '1':
			ticket = RegularTicket(1234567889, event.event_price)
		elif type == '2':
			ticket = AdvanceTicket(1234567889, event.event_price)
		elif type == '3':
			ticket = LateTicket(1234567889, event.event_price)
		elif type == '4':
			ticket = StudentTicket(1234567889, event.event_price)
		else:
			print("Wrong input value")

		if ticket is not None:
			print('\nThis ticket will be cost for you: '+str(ticket.get_ticket_price()))
			print("Do you want to print this ticket?\n\t1 = Yes\n\t2 = No")
			print_ticket = input("Enter your choice: ")
			if print_ticket == '1':
				print(ticket.print_ticket())
			else:
				print("Goodbuy!")

