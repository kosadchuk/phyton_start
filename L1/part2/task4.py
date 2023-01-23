class parseTextFile:

	def __init__(self, filename):
		self.filename = filename

	def count_chars(self):
		text_length = 0
		with open(self.filename, "r") as file_obj:
			line = file_obj.readline()
			while line:
				text_length += len(line)
				line = file_obj.readline()
		return text_length

	def count_words(self):
		words_count = 0
		with open(self.filename, "r") as file_obj:
			line = file_obj.readline()
			while line:
				words_count += len(line.split())
				line = file_obj.readline()
		return words_count

	def count_sentences(self):
		sentences_count = 0
		with open(self.filename, "r") as file_obj:
			line = file_obj.readline()
			while line:
				sentences_count += len(line.split('.'))
				line = file_obj.readline()
		return sentences_count

	def print_text(self):
		with open(self.filename, "r") as file_obj:
			line = file_obj.readline()
			while line:
				print(line, end="")
				line = file_obj.readline()


filename = "text_file_task4.txt"
text_file = parseTextFile(filename)
text_file.print_text()
print(f'\nText has {str(text_file.count_chars())} characters')
print(f'\nText has {str(text_file.count_words())} words')
print(f'\nText has {str(text_file.count_sentences())} sentences')

