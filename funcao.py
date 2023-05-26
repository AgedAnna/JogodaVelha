branco = "_"
token = ['X','O']

def CriarBoard():
    board = [
        [branco, branco, branco],
        [branco, branco, branco],
        [branco, branco, branco],
    ]
    return board
def PrintBoard(board):
    for i in range(3):
        print("|".join(board[i]))
        if(i<2):
            print('-----')

def GetInputValido(mensagem):
    try:
        n = int(input(mensagem))
        if (n>=1 and n<=3):
            return n - 1
        else:
            print("Digite um lugar entre as linhas 1 e 3")
            return GetInputValido(mensagem)
    except:
        print('Número inválido')
        GetInputValido(mensagem)

def VerificaMovimento(board, i , j):
    if(board[i][j] == branco):
        return True
    else:
        return False
def FazMovimento(board, i, j, player):
    board[i][j] = token[player]

def VerificaGanhador(board):
        #linhas
        for i in range(3):
            if(board[i][0] == board [i][1] and board[i][1] == board[i][2] and board[i][0] != branco):
                return board[i][0]

        # colunas
        for i in range(3):
            if (board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] != branco):
                return board[0][i]

        #diagonal principal
        if(board[0][0] != branco and board[0][0] == board[1][1] and board[1][1] == board[2][2]):
            return board[0][0]

        #diagonal secundária
        if (board[0][2] != branco and board[0][2] == board[1][1] and board[1][1] == board[2][0]):
            return board[0][2]

        for i in range(3):
            for j in range(3):
                if(board[i][j]==branco):
                    return False

        return 'Empate'
