from funcao import CriarBoard, FazMovimento, GetInputValido, PrintBoard, VerificaGanhador, VerificaMovimento

player = 0
board = CriarBoard()
ganhador = VerificaGanhador(board)
while (not ganhador):
    PrintBoard(board)
    i = GetInputValido('Digite a linha: ')
    j = GetInputValido('Digite a coluna: ')

    if(VerificaMovimento(board, i, j)):
        FazMovimento(board, i, j, player)
        player = (player + 1)%2
    else:
        print('A posição digitada já está ocupada')

    ganhador = VerificaGanhador(board)

print('-----------')
print('Parabéns o ganhador é: ',ganhador)
print('-----------')
