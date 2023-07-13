#program to make game Tic Tak Toe
def game_board(xstate, ystate):
  one = "X" if xstate[0] ==1 else "O" if ystate[0]==1 else " "
  Two = "X" if xstate[1] ==1 else "O" if ystate[1]==1 else " "
  Three="X" if xstate[2] ==1 else "O" if ystate[2]==1 else " " 
  four= "X" if xstate[3] ==1 else "O" if ystate[3]==1 else " " 
  Five= "X" if xstate[4] ==1 else "O" if ystate[4]==1 else " "  
  six = "X" if xstate[5] ==1 else "O" if ystate[5]==1 else " " 
  seven="X" if xstate[6] ==1 else "O" if ystate[6]==1 else " " 
  eight="X" if xstate[7] ==1 else "O" if ystate[7]==1 else " " 
  nine= "X" if xstate[8] ==1 else "O" if ystate[8]==1 else " " 
  print(f"            {one}   |   {Two}   |   {Three}   ")
  print(f"         -------|-------|------")
  print(f"            {four}   |   {Five}   |   {six}   ")
  print(f"         -------|-------|------")
  print(f"            {seven}   |   {eight}   |   {nine}   ")
def check_win(xstate, ystate):
   xwin = [[0, 1, 2 ], [3, 4, 5 ], [6, 7 , 8 ],[0, 4, 8 ], [2,4, 6]]  
   for win in xwin:
    if (xstate[win[0]] + xstate[win[1]] + xstate[win[2]]) == 3 :
      print (" GAME OVER  !!!")
      print (" X has won !!!")
      print("------------------------------------------")
      print("END OF THE GAME!!!!!!")
      return 1
    if (ystate[win[0]] + ystate[win[1]] + ystate[win[2]]) == 3 :
      print (" GAME OVER  !!!")
      print (" O has won !!!")
      print("------------------------------------------")
      print("END OF THE GAME!!!!!!")
      return 0
    return -1  
  
if __name__ == "__main__" :
    print("Welcome to tic - tack - toe !!!")
    xstate = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ystate = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    s = 0
    game = True
    game_board(xstate, ystate)
    while True :
      if s == 0 :
        m = int(input("This is the chance of X :"))
        if xstate[m-1] ==1 :
          print("This Value is already Entered!!")
          m = int(input("please Re Enter the value:"))
        xstate[m-1] = 1 
          
        s += 1
      elif s == 1 :
        m = int(input("This is the chance of O :"))
        if ystate[m-1] ==1 :
          print("This Value is already Entered!!")
          m = int(input("please Re Enter the value:"))
        ystate[m-1] = 1 
        # if check_win(xstate, ystate):
        #   break
        s -= 1
      
      game_board(xstate, ystate)
      if check_win(xstate, ystate) != -1:
        break
        
        