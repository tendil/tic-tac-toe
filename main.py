X = "X"
O = "O"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9


def display_instruct():
	"""Выводит на экран инструкцию для игрока."""
	print(
		"""
	   Добро пожаловать на ринг грандиознейших интеллектуальных состязаний всех времён.
	   Твой мозг и мой процессор сойдутся в схватке за доской игры "Крестики-нолики".
	   Чтобы сделать ход, введи число от 0 до 8. Числа однозначно соотвествуют полям
	   доски - так, как показано ниже:

						   0 | 1 | 2
						   ---------
						   3 | 4 | 5
						   ---------
						   6 | 7 | 8

	   Приготовься с к бою, жалкий человечишка. Вот-вот начнётся решающее сражение.\n
	   """
	)


def ask_yes_no(question):
	"""Задаёт вопрос с ответом 'Да' или 'Нет'."""
	response = None
	while response not in ("y", "n"):
		response = input(question).lower()
	return response


def get_answer(question: str, low_int: int, high_int: int):
	"""Просит ввести число из диапазона"""
	answer = ''
	integers = [str(i) for i in range (low_int, high_int )]
	while answer not in integers:
		answer = input(question)
	return int(answer)


def human_move(board, human):
	"""Получает ход человека"""
	legal = legal_moves(board)
	move = None
	while move not in legal:
		move = get_answer("\nТвой ход. Выбери одно из полей (0 - 8):", 0, NUM_SQUARES)
		if move not in legal:
			print("\nСмешной человечешка! Это поле уже занято. Выбери другое.\n")
			print("Ладно... Проехали...\n")
	return move

def pieces():
	"""Определяет принадлежность перового хода."""
	go_first = ask_yes_no("Хочешь оставить за собой первый ход? (y, n): ")
	if go_first == "y":
		print("\nНу что ж, дают тебе фору: играй крестиками.")
		human = X
		computer = O
	else:
		print("\nТвоя удаль тебя погубит... Буду начинать я.")
		computer = X
		human = O
	return computer, human


def new_board():
	"""Создаёт новую игровую доску."""
	board = []
	for square in range(NUM_SQUARES):
		board.append(EMPTY)
	return board


def display_board(board):
	"""Отображает игровую доску на экране."""
	print("\n\t", board[0], "|", board[1], "|", board[2])
	print("\t", "----------")
	print("\t", board[3], "|", board[4], "|", board[5])
	print("\t", "----------")
	print("\t", board[6], "|", board[7], "|", board[8])


def legal_moves(board):
	"""Создаёт список доступных ходов."""
	moves = []
	for square in range(NUM_SQUARES):
		if board[square] == EMPTY:
			moves.append(square)
	return moves


def winner(board):
	"""Определяет победителя в игре."""
	WAYS_TO_WIN = ((0, 1, 2),
				   (3, 4, 5),
				   (6, 7, 8),
				   (0, 3, 6),
				   (1, 4, 7),
				   (2, 5, 8),
				   (0, 4, 8),
				   (2, 4, 6))
	for row in WAYS_TO_WIN:
		if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
			winner = board[row[0]]
			return winner
		if EMPTY not in board:
			return TIE
	return None


def computer_move(board, computer, human):
	"""Делает ход за комп."""
	# создадим рабочую копию доски, потому что функция будет менять некотороые элементы в списке
	board = board[:]
	# ходы, от лучшего к худшему
	BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)

	print("Я выберу поле номер", end=" ")
	# если сдедующим ходом может победить компьютер, выберем этот ход
	for move in legal_moves(board):
		board[move] = computer
		if winner(board) == computer:
			print(move)
			return move
		# выполнив проверку этого хода, отменим его (в локальной копии игровой доски)
		board[move] = EMPTY

	# если следующим ходом может победить человек, блокируем этот ход
	for moves in legal_moves(board):
		board[move] = human
		if winner(board) == human:
			print(move)
			return move
		# выполнив проверку этого хода, отменим его (в локальной копии игровой доски)
		board[move] = EMPTY

	# поскольку следующим ходом ни одна из сторон не может победить,
	# выберем лучшее из доступных полей
	for move in BEST_MOVES:
		if move in legal_moves(board):
			print(move)
			return move


def next_turn(turn):
	"""Осуществляет переход хода."""
	if turn == X:
		return O
	else:
		return X


def restart_game():
	rest = input('\nХочешь сыграть ещё раз? - "y" или "n" - ')
	if rest == 'y':
		main()
	elif rest == 'n':
		exit()
	else:
		print('Выбери только y или n')
		restart_game()


def congrat_winner(the_winner, computer, human):
	"""Поздравляет победителя игры."""
	if the_winner != TIE:
		print("Три", the_winner, "в ряд!\n")

	else:
		print("Ничья!\n")
		return restart_game()

	if the_winner == computer:
		print("Это было предсказуемо... Победа в очередной раз досталась мне!\n" \
			  "Вот ещё один довод в пользу того, что компьютеры превосходят человека решительно во всём.")
		return restart_game()

	elif the_winner == human:
		print(
			"Неужели ты как-то сумел меня перехитрить белковый? На этот раз тебя повезло, но больше я такого не допущу! \n" \
			"Клянусь: я, компьютер, не допущу этого никогда!!!")
		return restart_game()

	elif the_winner == TIE:
		print("Тебе несказанно повезло, дружок: ты сумел сыграть вничью. \n" \
			  "Не каждый так может, так что радуйся. Завтра тебе уже не суждено так сыграть, тк мои алгоритмы будут улучшены.")
		return restart_game()

def main():
	display_instruct()
	computer, human = pieces()
	turn = X
	board = new_board()
	display_board(board)
	while not winner(board):
		if turn == human:
			move = human_move(board, human)
			board[move] = human
		else:
			move = computer_move(board, computer, human)
			board[move] = computer
		display_board(board)
		turn = next_turn(turn)
	the_winner = winner(board)
	congrat_winner(the_winner, computer, human)


# запуск программы
main()
