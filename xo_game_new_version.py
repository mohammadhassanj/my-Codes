def enter(board,winner):                                                      
          num = int(input('how much puzzle do you want\nfor example 4 for 4 * 4\n'))
          board = board(num)
          show(board)                               
          user1 = input("please Enter user1 name\n")
          user2 = input("please Enter user2 name\n")
          flag = True
          while True: 
              if flag:                                                           
                  selection = int(input("\nEnter your chice {}\n".format(user1)))-1
                  flag = False
                  sym = "X"
              else:                                                              
                  selection = int(input("\nEnter your chice {}\n".format(user2)))-1
                  flag = True
                  sym = "O"        
              column = selection%num
              row = selection//num                   
              if board[row][column] not in ["X","O"]:
                  board[row][column] = sym
              else:                                                    
                  print ("\nthere is full select other place\n!!!!!!!")
                  if flag:flage=False
                  else: flag = True 
              winner1 = winner(board)
              if winner1:       
                  winner = user1 if 'X' in winner1 else user2
                  show(board)
                  return "{} is Winner".format(winner)
                   
              if "0" not in str(board):
                  show(board)
                  return "every things is equal"
              show(board)
           
 
 
def show(board):                                                              
     stri = "|{:^3}"*len(board)                                                
     start = 1        
     for row in board:                         
         form = []                             
         row2 = [str(item) for item in range(start,start+len(row))]
         for i,j in zip(row,row2):
             if i == "X" or i == "O":
                 form.append(i)                                             
             else:                                                          
                 form.append(j)
         print (stri.format(*form)+"|")
         start+=len(board)
 
def board(num):                                                               
     board = [['0' for j in range(num)] for i in range(num)]                   
     return board 
 
def winner(puzzle):                                                           
     #row checking                                                             
     players = ["O"*len(puzzle),"X"*len(puzzle)]
     for item in puzzle:                                             
         if "".join(item) in players:                              
             return ''.join(item)                                              
     #column checkig                     
     for column in range(len(puzzle[0])):
         result = ''                                                        
         for row in range(len(puzzle)):                                     
             result+=puzzle[row][column]                
         if result in players:         
             return result                                                  
     ghotre1,ghotre2 = '',''                                                
     for index,row in enumerate(puzzle):
         ghotre1+=row[index]     
         ghotre2+=row[-(index+1)]
                                                      
     if ghotre1 in players:                     
         return ghotre1                                
     elif ghotre2 in players:                                     
         return ghotre2                                           
     else:                      
         return False
 
if __name__ == "__main__":
     enter(board,winner)
