import json, os
list_Questoes = score = dict()

def CarregarDados() -> None:
    if os.path.exists('bd_Questoes/db_Questoes.json' and 'bd_Questoes/score.json'):
        with open('bd_Questoes/db_Questoes.json', 'r') as arqJson:
            global list_Questoes
            list_Questoes = json.load(arqJson)
        with open('bd_Questoes/score.json', 'r') as arqJson:
            global score
            score = json.load(arqJson)

def GravarDados_Questoes() -> None:
    with open('bd_Questoes/db_Questoes.json', 'w+') as arqJson:
        json.dump(list_Questoes, arqJson, indent=6)

def GravarDados_Score() -> None:
    with open('bd_Questoes/score.json', 'w+') as arqJson:
        json.dump(score, arqJson, indent=2)

# --------------------------------------------------------------------------------

def maiorScore() -> str:
    player = ''
    maior = 0
    for n in score.values():
        if n.get('pontos') > maior:
            maior = n.get('pontos')
            player = n.get('jogador')
    return f'Melhor pontuação: {player} - {maior} Pontos'

def iniciar_Game() -> None:
    if len(list_Questoes) > 0:
        name = input('Digite o nome do jogador: ')
        ponto = 0
        for n in list_Questoes.values():
            print(f"Pergunta {n.get('codigo')}: {n.get('text')}")
            print(f'A) {n.get("a")} ')
            print(f'B) {n.get("b")} ')
            print(f'C) {n.get("c")} ')
            print(f'D) {n.get("d")} ')
            print('-' * 40)
            res = input("Qual a resposta: [A] [B] [C] [D] ").lower()
            if res == n.get('resposta'):
                ponto += 1
        score[len(score) + 1] = {'codigoJogador': len(score) + 1, 'jogador': name, 'pontos': int(ponto)}
        GravarDados_Score()
        print('-'*40)
        print(f'Sua prontuação foi: {ponto}')
    else:
        print('Lista vazia! ')
        pass
    input('-'*40 + '\nENTER para retorna ao menu:')

def adicionar_Questoes() -> None:
    text = input("Digite o texto da questão: ")
    q1 = input("Digite a alternativa A: ")
    q2 = input("Digite a alternativa B: ")
    q3 = input("Digite a alternativa C: ")
    q4 = input("Digite a alternativa D: ")
    res = input("Digite o qual a alternativa correta: [A] [B] [C] [D] ").lower()
    bloco = {'codigo': len(list_Questoes) + 1,  'text': text, 'a': q1, 'b': q2, 'c': q3, 'd': q4, 'resposta': res}
    list_Questoes[len(list_Questoes) + 1] = bloco
    GravarDados_Questoes()
    input('-'*40 + '\nENTER para retorna ao menu:')

def listar_Dados() -> None:
    print(f'Numero de questoes registradas: {len(list_Questoes)}')
    print(f'Quantidade de vezes jogadas: {len(score)}')
    print(maiorScore())
    input('-'*40 + '\nENTER para retorna ao menu:')
