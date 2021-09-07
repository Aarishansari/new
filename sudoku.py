import random
import math

def CheckBox(lst,sudoku,row,N):
	sudo_sudoku = []
	sqt = int(math.sqrt(N))
	row_num = len(sudoku)
	col_num = N - len(lst)
	row_floor = row_num//sqt
	col_floor = col_num//sqt
	#print(row_num,col_num)
	sudo_sudoku = sudoku.copy()
	sudo_sudoku.append(row)
	for r in range(row_floor*sqt,row_floor*sqt+sqt):
		for c in range(col_floor*sqt,col_floor*sqt+sqt):
			if row_num == r and col_num == c:
				return True
			#print(r,c,'hh')
			#print(sudo_sudoku)
			if lst[0] == sudo_sudoku[r][c]:
				return False
				
	return True



def CheckColumns(lst,sudoku,N):
	
	row_num = len(sudoku)
	col_num = N - len(lst)
	for i in range(0,row_num): 
		#print(i,col_num,'as',sudoku)
		if sudoku[i][col_num] == lst[0]:
			print(lst,sudoku[i][col_num],'bnvcmv')
			return False 

	return True

def CheckConditions(lst,sudoku,N,row,flag):
	
	
	for i in range(0,len(lst)):		
		
	
		if CheckColumns(lst,sudoku,N) == True and CheckBox(lst,sudoku,row,N) == True:	
			
			flag = 1
			row.append(lst[0])
			#print(lst,row)
			lst.pop(0)
			#print('hiidfgh')
			row,flag = CheckConditions(lst,sudoku,N,row,flag)
			if flag == 1:
				return row,flag
			else:
				lst.append(row[-1])
				row.pop(-1)

		

		flag = 0
		lst.append(lst[0])
		lst.pop(0)
		#print(lst,row,"hiii")

	if row == []:
		print(sudoku,lst,N,row,flag)
		#exit()
		#row,flag = CheckConditions(lst,sudoku,N,row,flag)
	return row,flag



def CreateSudoku(N,sudoku):
	
	lst=list(range(1,N+1))
	random.shuffle(lst)
	sudoku.append(lst)	
	
	while len(sudoku) < N:
		row = []
		flag = 0
		lst=list(range(1,N+1))
		random.shuffle(lst)
		
		row,flag = CheckConditions(lst,sudoku,N,row,flag)
		#print(row)
		if row != []:
		
			sudoku.append(row)		 
		#print(sudoku,'asdfgh')
	return sudoku 




if __name__ == "__main__":

	sudoku =[]
	sudoku = CreateSudoku(9,sudoku)

	print(sudoku)
