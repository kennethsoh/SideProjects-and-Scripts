from collections import deque
import sys

portfolio = []
def read_data_from_file():
	path = "portfolio.txt"
	with open(path, "r") as O:
		for line in O:
			line = line.split(",")
			stocks = str(line[0])
			units = int(line[1])
			prices = float(line[2])
			portfolio.append([stocks, units, prices])
	
portfolio = deque(portfolio)
read_data_from_file()

def print_portfolio():
	print(f"{'stocks':<10s}units\tprices")
	index = 0
	for k in portfolio:
		S = str(k[0])
		U = int(k[1])
		P = float(k[2])
		print(f"{S:<10s}{U}\t{P}")
		index +=1
	print()


def profitloss():
	S, U, P = input("What stock do you want to sell? ").split(",")
	S = str(S)
	U = int(U)
	P = float(P)
	cost = U*P
	
	if S == "GME":
		print("You can't sell that now. It's market manipulation.\n")
		sys.exit()
	
	total = 0
	for i in portfolio:
		if S.lower() == (i[0]).lower():
			total += int((i[1]))
	if U > total:
		print("You do not have enough stocks to sell")
		print("Please try again!")
		sys.exit()

	index = 0
	for i in portfolio:
		if S.lower() == (i[0]).lower():
			Unum = U
			if U > int(i[1]):
				Unum = int(i[1])
			pl = round((Unum * P) - (Unum * float(i[2])), 4)
			break
		index += 1
	
	# update portfolio
	units = int(float(i[1])-U)
	i[1] = units
	print(f"The profit/loss is ${pl}\n")

	if i[1] == 0:
		del portfolio[index]

	# if trying to sell more
	
	while units < 0:
		del portfolio[index]
		units = abs(units)
		index = 0
		for j in portfolio:
			if S.lower() == (j[0].lower()):
				Unum = units
				if units > int(j[1]):
					Unum = int(j[1])
				pl = round(((Unum * P) - (Unum * float(j[2]))), 4)
				units = (int(j[1]) - units)
				j[1] = units
				print(f"The profit/loss is ${pl}\n")
				if j[1] == 0:
					del portfolio[index]
				break
			index += 1
		
		
if __name__ == "__main__":
	i = 1
	while i != 0:
		print_portfolio()
		profitloss()
		print_portfolio()
		ask = input("Would you like to continue trading? (y/n)")
		if ask.lower() == "y":
			print()
		else:
			print("Thank you for trading")
			break





















































#Begin license text
#Copyright 2021 kennethsoh (github.com/kennethsoh)
#
#Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. 
#End license text
