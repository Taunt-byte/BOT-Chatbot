import os

def  processar_resposta(resposta,nome):
    if resposta == "1":
        print(f'{os.linesep}{nome}Mercúrio, Vênus, Terra, Marte, Júpiter, Saturno, Urano e Netuno{os.linesep}')
    elif resposta == "2":
        print(f'{os.linesep}{nome}O som não pode propagar-se no espaço, pois, nesse ambiente, existe o vácuo. Por não haver moléculas no ambiente, as ondas sonoras não são transmitidas, e o resultado de uma explosão no espaço, por exemplo, seria o silêncio.{os.linesep}')
    elif resposta == "3":
        print(f'{os.linesep}{nome}Apesar de não ser possível pousar em Júpiter, é possível aterrissar nas luas de Galileu, levando à possibilidade de exploração humana tripulada. Os principais alvos são Europa, devido à possibilidade de vida e oceanos, e Calisto, devido à sua pequena dose de radiação.{os.linesep}')
    elif resposta == "4":
        print(f'{os.linesep}{nome}Praticamente todos os foguetes deixam peças e pedaços na órbita ao serem lançados, como estágios de lançamentos abandonados, peças ejetadas, entre outros. Também existem muitos satélites que encerraram sua vida útil e continuam a orbitar a Terra sem qualquer atividade, passando a serem considerados como lixo espacial.{os.linesep}')
    else:
        print('Digite apenas 1,2,3 ou 4 ')
def start():
    #Apresentar o chatbot
    print('Olá Seja bem vindo ao chat')
    nome = input('Qual o seu nome? : ')
    #Oferecer menu de interação
    while True:
        resposta = input(
            f'O que gostaria de saber sobre o espaço hoje? {os.linesep} [1] - Quais são os planetas que estão no nosso sistema solar? {os.linesep}[2] - existe som no espaço ? {os.linesep} [3] - dá para pisar em Júpiter? {os.linesep} [4] - Ao redor da Terra há muito lixo espacial? {os.linesep}'
        )

    #Processar resposta enviada pelo usuario
    processar_resposta(resposta,nome)

    if __name__ == '__main__':
        start()