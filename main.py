import pygame
import sys
from random import shuffle

# Configurações da tela
LARGURA, ALTURA = 800, 600
BRANCO = (255, 255, 255)
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)
VERMELHO = (255, 0, 0)

pygame.init()
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo Educacional de Lógica")
fonte = pygame.font.SysFont("arial", 30)

# Perguntas e respostas
perguntas = [
    {"pergunta": "Qual é o próximo número da sequência: 2, 4, 6, 8, ?", "opcoes": ["9", "10", "12", "14"], "resposta": "10"},
    {"pergunta": "Quantos bits tem 1 byte?", "opcoes": ["4", "8", "16", "32"], "resposta": "8"},
    {"pergunta": "O que significa o operador 'and' em Python?", "opcoes": ["OU", "E", "NÃO", "XOR"], "resposta": "E"}
]
shuffle(perguntas)

indice = 0
pontos = 0

# Funções

def mostrar_texto(texto, x, y, cor=PRETO):
    render = fonte.render(texto, True, cor)
    tela.blit(render, (x, y))


def mostrar_pergunta():
    tela.fill(BRANCO)
    pergunta = perguntas[indice]
    mostrar_texto(pergunta["pergunta"], 50, 50)

    for i, opcao in enumerate(pergunta["opcoes"]):
        mostrar_texto(f"{i + 1}) {opcao}", 50, 150 + i * 50)


def verificar_resposta(resposta):
    global indice, pontos
    correta = perguntas[indice]["resposta"]

    if resposta == correta:
        pontos += 10
    indice += 1


# Loop principal
rodando = True
while rodando:
    tela.fill(BRANCO)

    if indice < len(perguntas):
        mostrar_pergunta()
    else:
        mostrar_texto(f"Fim de jogo! Pontuação final: {pontos}", 200, 250, VERDE)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_1:
                verificar_resposta(perguntas[indice]["opcoes"][0])
            elif evento.key == pygame.K_2:
                verificar_resposta(perguntas[indice]["opcoes"][1])
            elif evento.key == pygame.K_3:
                verificar_resposta(perguntas[indice]["opcoes"][2])
            elif evento.key == pygame.K_4:
                verificar_resposta(perguntas[indice]["opcoes"][3])

    pygame.display.update()

pygame.quit()
sys.exit()
