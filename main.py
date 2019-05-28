from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QGridLayout

operators = "%*+-/^"


def main():
	print("RPN Calculator")
	print("--------------")
	while True:
		try:
			print(calculate_expression(input()))
		except ZeroDivisionError:
			print("You cannot divide by zero")
		except NotImplementedError:
			print("There was an error with one of the operators, or one was not implemented yet")
		except RuntimeError:
			print("The expression provided had an invalid number of operators/operands")


def check_number(s):
	""" Checks if a string is a number or not. """
	try:
		float(s)
		return True
	except ValueError:
		return False


def token_to_number(t):
	""" converts a token from the expression into a int or a float """
	try:
		t = int(t)
	except ValueError:
		t = float(t)
	finally:
		return t


def calculate_expression(expression):
	stack = []

	expression = expression.split(" ")

	for token in expression:
		if check_number(token):
			stack.append(token_to_number(token))
		elif token in operators:
			operand_2 = stack.pop()
			operand_1 = stack.pop()
			if token == "%":
				stack.append(operand_1 % operand_2)
			elif token == "*":
				stack.append(operand_1 * operand_2)
			elif token == "+":
				stack.append(operand_1 + operand_2)
			elif token == "-":
				stack.append(operand_1 - operand_2)
			elif token == "/":
				if operand_2 == 0:
					print(stack)
					raise ZeroDivisionError
				stack.append(operand_1 / operand_2)
			elif token == "^":
				stack.append(operand_1 ** operand_2)
		else:
			print(stack)
			raise NotImplementedError

	if len(stack) > 1:
		raise RuntimeError
	else:
		return stack[0]


if __name__ == '__main__':
	main()
