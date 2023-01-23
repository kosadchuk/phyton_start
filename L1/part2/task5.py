import statistics


class GroupLimitError(Exception):

	def __init__(self, message):
		self.message = message

	def __str__(self):
		return f'Group Limit exceeded. {self.message}'


class Student:

	def __init__(self, name: str, surname: str, record_book_id: int):
		self.name = name
		self.surname = surname
		self.record_book_id = record_book_id
		self.__record_book_grades = []

	def __str__(self):
		return f'{self.name} {self.surname} {self.record_book_id}'

	def add_record_book_grades(self, grades_list: dict):
		self.__record_book_grades = grades_list

	def get_grades(self):
		return self.__record_book_grades


class Group:

	def __init__(self, group_name: str, max_limit=10):
		self.group_name = group_name
		self.max_limit = max_limit
		self.__students = []

	def add_student(self, student: Student):
		if len(self.__students) >= self.max_limit:
			raise GroupLimitError(f'Max limit is {self.max_limit}')

		if student in self.__students:
			raise ValueError('Duplicate student')

		self.__students.append(student)

	def get_avg_score_each_student(self):
		result = {}

		for student in self.__students:
			result[student.surname + ' ' + student.name] = statistics.mean(student.get_grades().values())

		return result

	def get_avg_highest_scores(self, limit=5):
		result = []

		all_avg = self.get_avg_score_each_student()
		sorted_all_avg = sorted(all_avg.items(), key=lambda x: x[1], reverse=True)
		dict(sorted_all_avg)

		i = 0
		while i < limit:
			result.append(sorted_all_avg[i])
			i += 1

		return result


student_1 = Student('Kateryna', 'Osadchuk', 123)
student_2 = Student('Petro', 'Ostapenko', 125)
student_3 = Student('Viktor', 'Petrenko', 126)
student_4 = Student('Oleg', 'Zamanskyi', 127)
student_1.add_record_book_grades({"OOP": 4, "Math": 4, "DataBase": 5, "English": 3})
student_2.add_record_book_grades({"OOP": 2, "Math": 3, "DataBase": 3, "English": 4})
student_3.add_record_book_grades({"OOP": 3, "Math": 4, "DataBase": 5, "English": 4})
student_4.add_record_book_grades({"OOP": 2, "Math": 2, "DataBase": 3, "English": 4})
group = Group("ТВ-з11")
group.add_student(student_1)
group.add_student(student_2)
group.add_student(student_3)
group.add_student(student_4)

print('Average score of each student\n', group.get_avg_score_each_student())
print('Average score for best students\n', list(map(str, group.get_avg_highest_scores(2))))



