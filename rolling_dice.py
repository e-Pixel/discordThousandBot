from random import randint

def roll_once():
	val1 = randint(1,6) 	
	single_roll = ":game_die: {}".format(str(val1)) + "!"
	return single_roll # result once 

def roll_twice():
	global val1
	global val2
	val1 = randint(1,6)
	val2 = randint(1,6)
	sum_rols = val1 + val2
	double_roll = ":game_die: {} + :game_die: {} = :game_die: {} !".format(str(val1), str(val2), str(sum_rols)) 
	return double_roll # result twice

def sum():
	return val1 + val2