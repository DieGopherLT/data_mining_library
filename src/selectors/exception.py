class OutOfRange():
	def __init__(self, index, index_range):
		if index < 1 or index > index_range:
			raise IndexError
	