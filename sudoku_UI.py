import math
import sudoku




def GetUserInput():
	while True:
		n = input("Enter the dimension of sudoku.\nDimension should be perfect square. \n Example '4' '9' '16'. \n==>> ")
		n  = int(n)
		if n > 0:
			sqt = math.sqrt(n)
			if sqt*sqt == n:
				break

	return n,int(sqt)




def CreateStructure(n,r,sudk):
	print(sudk)
	count = 0
	f = open("sudoku","w")
	f.write("\n")
	for i in range(0,r):
		f.write(" ")
		for j in range(0,r*4):
			f.write("_")
	
	for l in range(0,r):
		for k in range(0,r*2):
			f.write("\n")
			for j in range(0,r):
				f.write("|")
				for i in range(0,r):
					for h in range(0,4):
						if n > 9 :
							if h == 1 and k%2 == 0:
								f.write(" ")
							if h == 1:
								pass
							else:
								if h == 2 and k%2 != 0:
								
									if sudk[count] > 9:
									
										f.write("%s" % sudk[count])
										count += 1

									else:
										f.write(" ")
										f.write("%s" % sudk[count])
										count += 1

								
								else:
									f.write(" ")
						else:
							if h == 2 and k%2 != 0:

								f.write("%s" % sudk[count])
								count += 1
							else:
								f.write(" ")
					


			f.write("|")
		f.write("\n")
		for i in range(0,r):
			f.write("|")
			for j in range(0,r*4):
				f.write("_")
		f.write("|")

		

			
	f.close()

def GetSudoku(n):
	sudk = []
	sudku = sudoku.CreateSudoku(n,sudk)
	sudk = [item for sublist in sudku for item in sublist]

	return sudk

#sudk = [3, 15, 9, 11, 13, 6, 2, 1, 16, 8, 14, 10, 4, 12, 7, 5, 1, 5, 2, 12, 14, 16, 9, 10, 4, 7, 6, 13, 8, 3, 11, 15, 16, 13, 7, 8, 15, 12, 3, 4, 1, 9, 5, 11, 14, 6, 2, 10, 14, 10, 6, 4, 5, 11, 7, 8, 15, 12, 3, 2, 13, 16, 9, 1, 5, 11, 8, 14, 4, 9, 10, 13, 3, 15, 12, 16, 7, 2, 1, 6, 12, 9, 16, 3, 2, 5, 1, 14, 6, 11, 4, 7, 10, 8, 15, 13, 15, 1, 13, 6, 12, 8, 11, 7, 2, 10, 9, 14, 5, 4, 16, 3, 10, 2, 4, 7, 3, 15, 6, 16, 5, 1, 13, 8, 12, 11, 14, 9, 2, 6, 11, 15, 9, 4, 16, 5, 7, 3, 10, 12, 1, 13, 8, 14, 9, 12, 5, 1, 10, 7, 8, 3, 13, 14, 2, 4, 16, 15, 6, 11, 8, 4, 3, 16, 6, 13, 14, 12, 11, 5, 1, 15, 2, 9, 10, 7, 7, 14, 10, 13, 11, 1, 15, 2, 8, 6, 16, 9, 3, 5, 4, 12, 6, 16, 12, 10, 8, 3, 5, 9, 14, 4, 11, 1, 15, 7, 13, 2, 13, 3, 14, 9, 7, 2, 12, 15, 10, 16, 8, 6, 11, 1, 5, 4, 11, 7, 1, 2, 16, 14, 4, 6, 12, 13, 15, 5, 9, 10, 3, 8, 4, 8, 15, 5, 1, 10, 13, 11, 9, 2, 7, 3, 6, 14, 12, 16]
if __name__ == "__main__": 
	
	n,r = GetUserInput()
	sudk = GetSudoku(n)
	CreateStructure(n,r,sudk)
	




