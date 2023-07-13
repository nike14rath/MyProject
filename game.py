x = 7 
while True:
  print(x)
  x -= 1
  if x < 3:
    print("Hello")
    if x == 0:
      break
 while  game == True:
        game_board(xstate, ystate) 
        if s == 0 :
            print("This is turn of X:")
            m = int(input("Enter your mark (1-9):"))
            xstate[m-1] = 1 
            if check_win(xstate , ystate):
               game = False
               break
            s+=1
            # check_win(xstate , ystate)
            # game_board() 
        elif s == 1 :
            print("This is turn of O :")
            v = int(input("Enter your mark (1-9):"))
            ystate[v-1] = 1 
            if check_win(xstate , ystate):
               game = False
               break
            s-=1   