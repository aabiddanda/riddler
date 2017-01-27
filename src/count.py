#!/usr/local/bin/python3

'''
	Script to solve counting puzzle for Count Von Count on Twitter
'''

import argparse as arg
from num2words import num2words

'''
	Returns character string of the count
        TODO : perform this without 'and' etc...
'''
def count(n):
	num_str = num2words(n) + '!'
	num_str = num_str.replace(' and ', " ")
	num_str = num_str.replace('-', ' ')
	num_str = num_str.replace(',', ' ')
	return(num_str)


'''
	Returns the first number that breaks the character bound c:
	@args c - number of characters allowed
	@return  - 
'''
def max_count(c):
	max_cnt = 0
	n = 0
	place = 0
	while max_cnt < c:
		i = [n + int(x*(10**place)) for x in range(1,10)]
		l = [len(count(a)) for a in i]
		m = max(l)
		max_cnt = m
		for ni in range(0,len(i)):
			if (l[ni] >= c):
				n = i[ni]
				print("Limit : %d\tlen : %d" % (i[ni], l[ni]))
				break
			if l[ni] == m:
				n = i[ni]
				break
		place += 1
	return(n) 

if __name__ =='__main__':
	parser = arg.ArgumentParser()
	parser.add_argument('-c', required=True, type=int, default=20, help='character limit')
	args = parser.parse_args()

	# Step 1: Apply recursive equation to find where the maximum is greatest
	max_count(args.c)	        
