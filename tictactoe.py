"""
Tic-Tac-Toe Optimality

 1 | 2 | 3
---|---|---
 4 | 5 | 6
---|---|---
 7 | 8 | 9

There are 8 possible winning patterns:
[1,2,3]
[1,4,7]
[1,5,9]
[2,5,8]
[3,5,7]
[3,6,9]
[4,5,6]
[7,8,9]


ASSUMPTIONS:

1) If a player ever has two in a row, and it is his turn, the player will make the winning move
2) If a player is in check and is able to get out of check, the player will make that move
3) X plays first
4) It takes 5 moves minimum to win, and 9 maximum to win/lose/draw

If there are no forces, you can make any legal move

If there is one force you must make that move

If there is more than one force, you lose unless you can escape via the same space. It doesn't matter what move you make because each is 
equally likely to result in a loss. So you lose at the beginning of your turn, two moves before 
there are actually three in a row. This is checkmate.

We're basically going to end up with a list of maybe 300,000 key-value pairs where key = winner/draw and value = list of moves

def legal_moves(board,player): # returns the set of legal moves
	# legal_moves(b,t) = [*int]
	# if opponent is in check, you must make that move
	# if you are in check, you must escape, else there are no legal moves and you forfeit

	if player == "X":
		pass
	else: # player == "O"
		pass

def check_win(board): # returns if the game has been won, and if so, by whom
	# check_win(b) = (game_over?, winner)
	if board[0] == board[1] == board[2]: # [1,2,3]
		winner = board[0]
		return True, winner
	elif board[0] == board[3] == board[6]: # [1,4,7]
		winner = board[0]
		return True, winner
	elif board[0] == board[4] == board[8]: # [1,5,9]
		winner = board[0]
		return True, winner
	elif board[1] == board[4] == board[7]: # [2,5,8]
		winner = board[1]
		return True, winner
	elif board[2] == board[4] == board[6]: # [3,5,7]
		winner = board[2]
		return True, winner
	elif board[2] == board[5] == board[8]: # [3,6,9]
		winner = board[2]
		return True, winner
	elif board[3] == board[4] == board[5]: # [4,5,6]
		winner = board[3]
		return True, winner
	elif board[6] == board[7] == board[8]: # [7,8,9]
		winner = board[6]
		return True, winner
	else:
		return False, None
"""

def checkmate(current, available, player): # checkmate() = (boolean, list)

	win_conditions = [[1,2,3], [1,4,7], [1,5,9], [2,5,8], [3,5,7], [3,6,9], [4,5,6], [7,8,9]]
	
	if player == "X":
		opponent = "O"
	else:
		opponent = "X"

	opponent_property = []

	for i in range(0,len(current)):
		if current[i] = opponent:
			opponent_property.append(i+1)

	checks = 0
	available_space = []

	# now we have a list of opponent properties and available properties
	for i in range(0, len(win_conditions)):
		in_a_row = 0
		num_available = 0
		for j in range(0, len(win_conditions[i])):
			if win_conditions[i][j] in opponent_property:
				in_a_row += 1
			elif win_conditions[i][j] in available:
				num_available += 1
			
			if in_a_row == 2 and num_available == 1:
				checks += 1

	if checks == 0:
		return False, available
	elif checks == 1:
		return False, [something subset of available]
	else:
		# if the available is the center:
			return False, [5]
		else:
			return True, []

	# you're in check if the opponent has 2 of the 3 of any of the win conditions and the 3rd is available
	# count the number of times this is true
	# if 0: false
	# if 1: false, but you have to take that space
	# if >1: true, unless you can escape both via the center space (5)
	pass

def legal_moves(current, available, player): # legal_moves() = [*int]
	# a legal move has to be in available, which we know is at least 1 move
	pass

def game(current, available, history, player): # game() = (string, list)
	check_check = checkmate(current, available, player)
	
	# Check if game is over	
	if len(available) == 0:
		return "draw", history
	elif check_check[0]:
		if player == "X":
			winner = "O"
		else:
			winner = "X"
		return winner, history
	else:

		# Get the set of all possible legal moves
		legal = check_check[1]: # at the moment this is called twice
		for k in range(0,len(legal)):
			
			# Make in-loop variables
			temp_current = current
			temp_available = available
			temp_history = history
			temp_player = player

			# Add move to current & history, make unavailable
			temp_current[legal[k]-1] = temp_player
			temp_history.append(temp_available.pop(k-1))

			# Switch turns
			if temp_player = "X":
				temp_player = "O"
			else:
				temp_player = "X"

			# Recursively create a new game with these features
			game(temp_current, temp_available, temp_history, temp_player)

# Create initial game
game([1,2,3,4,5,6,7,8,9], [1,2,3,4,5,6,7,8,9], [], "X")