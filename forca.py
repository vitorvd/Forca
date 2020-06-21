def jogar():
    print('################################')
    print('### Seja bem-vindo a Forca! ###')
    print('################################')

    palavra_secreta = "uva"
    letras_acertadas = []
    for letra in palavra_secreta:
        letras_acertadas.append('_')

    acertou = False
    enforcou = False
    erros = 0

    print(letras_acertadas)

    while (not acertou and not enforcou):
        chute = input('Qual a letra? ')

        if chute in palavra_secreta:
            posicao = 0
            for letra in palavra_secreta:
                if chute.upper() == letra.upper():
                    letras_acertadas[posicao] = letra
                posicao += 1
        else:
            erros += 1

        acertou = '_' not in letras_acertadas
        enforcou = erros == 6
        print(letras_acertadas)

        if acertou:
            print('Parabéns, você acertou a palavra!')
        elif not acertou and enforcou:
            print('Os seus 6 chutes acabaram, fim de jogo!')
        elif not acertou and not enforcou:
            print('Você errou o chute! Cê ainda têm {}'.format(6 - erros))

jogar()
