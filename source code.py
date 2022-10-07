flag = True
for i in range (0,100):
    if (flag == True):
        flag = False
        from datetime import datetime

        print("-------------------------------TIC TAC TOE-------------------------------")
        print("------------------------------------------INSTRUCTIONS------------------------------------------")
        print("1. IN THE SECTION OF 'CELL NUMBER' ENTER A NUMBER FROM 1-9 AS INDICATED IN THE FOLLOWING BOARD")
        print("2. PLAYER 1 WILL AUTOMATICALLY TAKE 'X' AND PLAYER 2 WILL AUTOMATICALLY TAKE 'O' ")
        print("3. HERE 1-9 REPRESENTS YOUR TIC TAC TOE BOARD. AND EACH NUMBER REPRESENTS A BOARD. REPLACE THE BOARD NUMBERS WITH 'X' OR 'O' ")
        print("-------------------------------------------------------------------------------------------------")
        L1 = ['1', '2', '3']  # ROW ONE
        L2 = ['4', '5', '6']  # ROW TWO
        L3 = ['7', '8', '9']  # ROW THREE

        ###########################
        # FOR ANYONE OUTSIDER
        # L10 L11 L12
        # L20 L21 L22
        # L30 L31 L32
        #############################

        # PRINT THE TIC TAC TOE BOARD
        print("TIC TAC TOE board::: ")
        print(L1[0] + ' ' + L1[1] + ' ' + L1[2] + ' ')
        print(L2[0] + ' ' + L2[1] + ' ' + L2[2] + ' ')
        print(L3[0] + ' ' + L3[1] + ' ' + L3[2] + ' ')
        pl1 = input("PLAYER 1 NAME (X) :: ")
        pl2 = input("PLAYER 2 NAME (O) :: ")
        for i in range(0, 9):

            if (L1[0] == L1[1] == L1[2] or L2[0] == L2[1] == L2[2] or L3[0] == L3[1] == L3[2] or L1[0] == L2[0] == L3[
                0] or L1[1] == L2[1] == L3[1] or L1[2] == L2[2] == L3[2] or L1[0] == L2[1] == L3[2] or L1[2] == L2[1] ==
                    L3[0]):
                if (L1[0] == L1[1] == L1[2] == 'X' or L2[0] == L2[1] == L2[2] == 'X' or L3[0] == L3[1] == L3[
                    2] == 'X' or L1[0] == L2[0] == L3[0] == 'X' or L1[1] == L2[1] == L3[1] == 'X' or L1[2] == L2[2] ==
                        L3[2] == 'X' or L1[0] == L2[1] == L3[2] == 'X' or L1[2] == L2[1] == L3[0] == 'X'):
                    print("_________________________________________________")
                    print("************", pl1, ' is the winner !', "************")
                    print("Final result board :: ")
                    print(L1[0] + ' ' + L1[1] + ' ' + L1[2])
                    print(L2[0] + ' ' + L2[1] + ' ' + L2[2])
                    print(L3[0] + ' ' + L3[1] + ' ' + L3[2])
                    print("_________________________________________________")
                    print("THIS GAME WAS MADE WITH PYTHON 3.9 , CODED BY ishmam ")
                    print(datetime.now())
                    print("_________________________________________________")
                    print("DO YOU WANT TO PLAY AGAIN ? ")
                    des = input("yes or no ? :: ")
                    if (des == 'YES' or des == 'yes' or des == 'Yes'):
                        flag = True
                    else:
                        flag = False
                    break
                else:
                    print("_________________________________________________")
                    print("************", pl2, ' is the winner! ', "************")
                    print("Final result board :: ")
                    print(L1[0] + ' ' + L1[1] + ' ' + L1[2])
                    print(L2[0] + ' ' + L2[1] + ' ' + L2[2])
                    print(L3[0] + ' ' + L3[1] + ' ' + L3[2])
                    print("_________________________________________________")
                    print("THIS GAME WAS MADE WITH PYTHON 3.9 , CODED BY ishmam ")
                    print(datetime.now())
                    print("_________________________________________________")
                    print("DO YOU WANT TO PLAY AGAIN ? ")
                    des = input("yes or no ? :: ")
                    if (des == 'YES' or des == 'yes' or des == 'Yes'):
                        flag = True
                    else:
                        flag = False
                    break

            else:
                print("Updated Tic Tac Toe Board: ")
                print(L1[0] + ' ' + L1[1] + ' ' + L1[2])
                print(L2[0] + ' ' + L2[1] + ' ' + L2[2])
                print(L3[0] + ' ' + L3[1] + ' ' + L3[2])
                if (i % 2 == 0):
                    print(pl1, "'s TURN:: ")
                    board = input("Enter the CELL number you want to put 'X' : ")

                    if int(board) > 9:
                        print("Sorry ! Wrong Input :(")
                        print("Do you wanna play again ? ")
                        des = input("yes or no ? :: ")
                        if (des == 'YES' or des == 'yes' or des == 'Yes'):
                            flag = True
                        else:
                            flag = False
                        break

                    if board == '1':  # UPDATE L10
                        L1[0] = 'X'
                    if board == '2':  # UPADATE L11

                        L1[1] = 'X'
                    if board == '3':  # UPDATE L12

                        L1[2] = 'X'
                    if board == '4':  # UPDATE L20

                        L2[0] = 'X'
                    if board == '5':  # UPDATE L21

                        L2[1] = 'X'
                    if board == '6':  # UPDATE L22

                        L2[2] = 'X'
                    if board == '7':  # UPDATE L30

                        L3[0] = 'X'
                    if board == '8':  # UPDATE L31

                        L3[1] = 'X'
                    if board == '9':  # UPDATE L32

                        L3[2] = 'X'
                else:
                    print(pl2, "'s TURN:: ")
                    board = input("Enter the CELL number you want to put 'O' : ")

                    if int(board) > 9:
                        print("Sorry ! Wrong Input :(")
                        print("Do you wanna play again ? ")
                        des = input("yes or no ? :: ")
                        if (des == 'YES' or des == 'yes' or des == 'Yes'):
                            flag = True
                        else:
                            flag = False
                        break

                    if board == '1':  # UPDATE L10
                        L1[0] = 'O'
                    if board == '2':  # UPADATE L11

                        L1[1] = 'O'
                    if board == '3':  # UPDATE L12

                        L1[2] = 'O'
                    if board == '4':  # UPDATE L20

                        L2[0] = 'O'
                    if board == '5':  # UPDATE L21

                        L2[1] = 'O'
                    if board == '6':  # UPDATE L22

                        L2[2] = 'O'
                    if board == '7':  # UPDATE L30

                        L3[0] = 'O'
                    if board == '8':  # UPDATE L31

                        L3[1] = 'O'
                    if board == '9':  # UPDATE L32

                        L3[2] = 'O'



        else:
            print("Tie")
            print("Do you wanna play again ? ")
            des = input("yes or no ? :: ")
            if (des == 'YES' or des == 'yes' or des == 'Yes'):
                flag = True
            else:
                flag = False

    else:
        print('Thank you for playing ! ')
        break