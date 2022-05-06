from operator import truediv


def jogar():
    print("******************************************")
    print("Bem vindo ao jogo de Forca!")
    print("******************************************")

    palavra_secreta = "banana".upper()
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]
    
    enforcou = False
    acertou = False
    erros = 0
    vidas = 6

    print(letras_acertadas)

    while(not enforcou and not acertou):
        
        chute = input("Digite uma letra:")
        chute = chute.strip().upper()

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            vidas -= 1
            enforcou = erros == 6
            print("Você só pode errar mais {} vezes".format(vidas))
        acertou = "_" not in letras_acertadas


        print(letras_acertadas)

    if (acertou):
        print("Você ganhou!")
    else:
        print("Você perdeu!")

if(__name__ == "__main__"):
    jogar()