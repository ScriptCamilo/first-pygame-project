import pygame
import os
import random

def main():


    pygame.init()

    logo = pygame.image.load('logo32x32.png')
    pygame.display.set_icon(logo)
    pygame.display.set_caption('DESTROY THE EVIL')

    R1, R2 = 255, 255
    G1, G2 = 255, 255
    B1, B2 = 255, 255

    screen_wi = 1024
    screen_he = 700

    xpos1 = 460
    ypos1 = 530
    step_x1 = 5
    step_y1 = 5

    screen = pygame.display.set_mode((screen_wi, screen_he))
    scale = pygame.transform.scale
    wi = 60
    he = 84

    start01 = pygame.font.Font(os.path.join('Fontes', 'Start.ttf'), 70)
    horrendo01 = pygame.font.Font(os.path.join('Fontes', 'leadcoat.ttf'), 100)
    horrendo02 = pygame.font.Font(os.path.join('Fontes', 'leadcoat.ttf'), 40)
    senha = ['$', '$', '$', '$']
    s = 1234
######################## AQUI SÃO AS IMAGENS DO PERSONAGEM INDO PARA BAIXO #############################################
    v1 = -1
    v = 1
    down01 = pygame.image.load(os.path.join('Nicolas', 'down01.png')).convert()
    down02 = pygame.image.load(os.path.join('Nicolas', 'down02.png')).convert()
    down03 = pygame.image.load(os.path.join('Nicolas', 'down03.png')).convert()
    down04 = pygame.image.load(os.path.join('Nicolas', 'down04.png')).convert()
    down05 = pygame.image.load(os.path.join('Nicolas', 'down05.png')).convert()
    down06 = pygame.image.load(os.path.join('Nicolas', 'down06.png')).convert()

    rundown01 = pygame.image.load(os.path.join('Nicolas', 'rundown01.png')).convert()
    rundown02 = pygame.image.load(os.path.join('Nicolas', 'rundown02.png')).convert()
    rundown03 = pygame.image.load(os.path.join('Nicolas', 'rundown03.png')).convert()
    rundown04 = pygame.image.load(os.path.join('Nicolas', 'rundown04.png')).convert()

    down01.set_colorkey((0, 102, 0))
    down02.set_colorkey((0, 102, 0))
    down03.set_colorkey((0, 102, 0))
    down04.set_colorkey((0, 102, 0))
    down05.set_colorkey((0, 102, 0))
    down06.set_colorkey((0, 102, 0))

    rundown01.set_colorkey((0, 102, 0))
    rundown02.set_colorkey((0, 102, 0))
    rundown03.set_colorkey((0, 102, 0))
    rundown04.set_colorkey((0, 102, 0))

######################## AQUI SÃO AS IMAGENS DO PERSONAGEM INDO PARA CIMA #############################################
    up01 = pygame.image.load(os.path.join('Nicolas', 'up01.png')).convert()
    up02 = pygame.image.load(os.path.join('Nicolas', 'up02.png')).convert()
    up03 = pygame.image.load(os.path.join('Nicolas', 'up03.png')).convert()
    up04 = pygame.image.load(os.path.join('Nicolas', 'up04.png')).convert()
    up05 = pygame.image.load(os.path.join('Nicolas', 'up05.png')).convert()

    runup01 = pygame.image.load(os.path.join('Nicolas', 'runup01.png')).convert()
    runup02 = pygame.image.load(os.path.join('Nicolas', 'runup02.png')).convert()
    runup03 = pygame.image.load(os.path.join('Nicolas', 'runup03.png')).convert()
    runup04 = pygame.image.load(os.path.join('Nicolas', 'runup04.png')).convert()

    up01.set_colorkey((0, 102, 0))
    up02.set_colorkey((0, 102, 0))
    up03.set_colorkey((0, 102, 0))
    up04.set_colorkey((0, 102, 0))
    up05.set_colorkey((0, 102, 0))

    runup01.set_colorkey((0, 102, 0))
    runup02.set_colorkey((0, 102, 0))
    runup03.set_colorkey((0, 102, 0))
    runup04.set_colorkey((0, 102, 0))
######################## AQUI SÃO AS IMAGENS DO PERSONAGEM INDO PARA ESQUERDA ##########################################
    v2 = 1
    vv = 1
    left01 = pygame.image.load(os.path.join('Nicolas', 'left01.png')).convert()
    left02 = pygame.image.load(os.path.join('Nicolas', 'left02.png')).convert()
    left03 = pygame.image.load(os.path.join('Nicolas', 'left03.png')).convert()
    left04 = pygame.image.load(os.path.join('Nicolas', 'left04.png')).convert()
    left05 = pygame.image.load(os.path.join('Nicolas', 'left05.png')).convert()

    runleft01 = pygame.image.load(os.path.join('Nicolas', 'runleft01.png')).convert()
    runleft02 = pygame.image.load(os.path.join('Nicolas', 'runleft02.png')).convert()
    runleft03 = pygame.image.load(os.path.join('Nicolas', 'runleft03.png')).convert()
    runleft04 = pygame.image.load(os.path.join('Nicolas', 'runleft04.png')).convert()
    runleft05 = pygame.image.load(os.path.join('Nicolas', 'runleft05.png')).convert()

    left01.set_colorkey((0, 102, 0))
    left02.set_colorkey((0, 102, 0))
    left03.set_colorkey((0, 102, 0))
    left04.set_colorkey((0, 102, 0))
    left05.set_colorkey((0, 102, 0))

    runleft01.set_colorkey((0, 102, 0))
    runleft02.set_colorkey((0, 102, 0))
    runleft03.set_colorkey((0, 102, 0))
    runleft04.set_colorkey((0, 102, 0))
    runleft05.set_colorkey((0, 102, 0))

######################## AQUI SÃO AS IMAGENS DO PERSONAGEM INDO PARA DIREITA ###########################################
    right01 = pygame.image.load(os.path.join('Nicolas', 'right01.png')).convert()
    right02 = pygame.image.load(os.path.join('Nicolas', 'right02.png')).convert()
    right03 = pygame.image.load(os.path.join('Nicolas', 'right03.png')).convert()
    right04 = pygame.image.load(os.path.join('Nicolas', 'right04.png')).convert()
    right05 = pygame.image.load(os.path.join('Nicolas', 'right05.png')).convert()

    runright01 = pygame.image.load(os.path.join('Nicolas', 'runright01.png')).convert()
    runright02 = pygame.image.load(os.path.join('Nicolas', 'runright02.png')).convert()
    runright03 = pygame.image.load(os.path.join('Nicolas', 'runright03.png')).convert()
    runright04 = pygame.image.load(os.path.join('Nicolas', 'runright04.png')).convert()
    runright05 = pygame.image.load(os.path.join('Nicolas', 'runright05.png')).convert()

    right01.set_colorkey((0, 102, 0))
    right02.set_colorkey((0, 102, 0))
    right03.set_colorkey((0, 102, 0))
    right04.set_colorkey((0, 102, 0))
    right05.set_colorkey((0, 102, 0))

    runright01.set_colorkey((0, 102, 0))
    runright02.set_colorkey((0, 102, 0))
    runright03.set_colorkey((0, 102, 0))
    runright04.set_colorkey((0, 102, 0))
    runright05.set_colorkey((0, 102, 0))



    attack01 = pygame.image.load(os.path.join('Nicolas', 'attack01.png')).convert()
    attack02 = pygame.image.load(os.path.join('Nicolas', 'attack02.png')).convert()
    attack03 = pygame.image.load(os.path.join('Nicolas', 'attack03.png')).convert()
    attack04 = pygame.image.load(os.path.join('Nicolas', 'attack04.png')).convert()
    attack05 = pygame.image.load(os.path.join('Nicolas', 'attack05.png')).convert()
    attack06 = pygame.image.load(os.path.join('Nicolas', 'attack06.png')).convert()
    attack07 = pygame.image.load(os.path.join('Nicolas', 'attack07.png')).convert()
    attack08 = pygame.image.load(os.path.join('Nicolas', 'attack08.png')).convert()
    attack09 = pygame.image.load(os.path.join('Nicolas', 'attack09.png')).convert()

    attack01.set_colorkey((0, 102, 0))
    attack02.set_colorkey((0, 102, 0))
    attack03.set_colorkey((0, 102, 0))
    attack04.set_colorkey((0, 102, 0))
    attack05.set_colorkey((0, 102, 0))
    attack06.set_colorkey((0, 102, 0))
    attack07.set_colorkey((0, 102, 0))
    attack08.set_colorkey((0, 102, 0))
    attack09.set_colorkey((0, 102, 0))

    def move(wi, he, xpos1, ypos1, v1, v2, x1, x2, y1, y2):
        key = pygame.key.get_pressed()
        step_x1 = 5
        step_y1 = 5
########################################################### UP #########################################################
        if not key[pygame.K_LSHIFT] and key[pygame.K_w] and ypos1 > y1:
            ypos1 += -step_y1
            v2 = 0
            if v1 <= -5:
                v1 = -1
            if v1 > -1:
                v1 = 0
            v1 += -v

        elif key[pygame.K_LSHIFT] and key[pygame.K_w] and ypos1 > y1:
            ypos1 += (2.5 * (-step_y1))
            v2 = 0
            if v1 <= -9:
                v1 = -5
            if v1 > -1:
                v1 = 0
            if v1 == -2:
                v1 = -5
            v1 += -v

########################################################## DOWN ########################################################
        elif not key[pygame.K_LSHIFT] and key[pygame.K_s] and ypos1 < y2:
            ypos1 += step_y1
            v2 = 0
            if v1 >= 6:
                v1 = 2
            if v1 < 1:
                v1 = 0
            v1 += v

        elif key[pygame.K_LSHIFT] and key[pygame.K_s] and ypos1 < y2:
            ypos1 += (2.5 * step_y1)
            v2 = 0
            if v1 >= 10:
                v1 = 6
            if v1 < 1:
                v1 = 0
            if v1 == 2:
                v1 = 6
            v1 += v

########################################################### lEFT #######################################################
        elif not key[pygame.K_LSHIFT] and key[pygame.K_a] and xpos1 > x1:
            xpos1 += -step_x1
            v1 = 0
            if v2 <= -5:
                v2 = -1
            if v2 > -1:
                v2 = 0
            v2 += -vv

        elif key[pygame.K_LSHIFT] and key[pygame.K_a] and xpos1 > x1:
            xpos1 += (2.5 * (-step_x1))
            v1 = 0
            if v2 <= -10:
                v2 = -6
            if v2 > -1:
                v2 = 0
            if v2 == -1:
                v2 = -5
            v2 += -vv

######################################################### RIGHT ########################################################
        elif not key[pygame.K_LSHIFT] and key[pygame.K_d] and xpos1 < x2 - 60:
            xpos1 += step_x1
            v1 = 0
            if v2 >= 5:
                v2 = 1
            if v2 < 1:
                v2 = 0
            v2 += vv

        elif key[pygame.K_LSHIFT] and key[pygame.K_d] and xpos1 < x2 - 60:
            xpos1 += (2.5 * step_x1)
            v1 = 0
            if v2 >= 10:
                v2 = 6
            if v2 < 1:
                v2 = 0
            if v2 == 1:
                v2 = 5
            v2 += vv

        elif key[pygame.K_RETURN]:
            v1 = 0
            if v2 >= 19:
                v2 = 14
            elif v2 < 15:
                v2 = 14
            v2 += vv

        ######## MOVIMENTO PARA BAIXO ###################
        if v1 == 1:
            screen.blit(scale(down01, (wi, he)), (xpos1, ypos1))
        elif v1 == 2:
            screen.blit(scale(down02, (wi, he)), (xpos1, ypos1))
        elif v1 == 3:
            screen.blit(scale(down03, (wi, he)), (xpos1, ypos1))
        elif v1 == 4:
            screen.blit(scale(down04, (wi, he)), (xpos1, ypos1))
        elif v1 == 5:
            screen.blit(scale(down05, (wi, he)), (xpos1, ypos1))
        elif v1 == 6:
            screen.blit(scale(down06, (wi, he)), (xpos1, ypos1))
        elif v1 == 7:
            screen.blit(scale(rundown01, (wi, he)), (xpos1, ypos1))
        elif v1 == 8:
            screen.blit(scale(rundown02, (wi, he)), (xpos1, ypos1))
        elif v1 == 9:
            screen.blit(scale(rundown03, (wi, he)), (xpos1, ypos1))
        elif v1 == 10:
            screen.blit(scale(rundown04, (wi, he)), (xpos1, ypos1))

        ######## MOVIMENTO PARA CIMA ##################
        elif v1 == -1:
            screen.blit(scale(up01, (wi, he)), (xpos1, ypos1))
        elif v1 == -2:
            screen.blit(scale(up02, (wi, he)), (xpos1, ypos1))
        elif v1 == -3:
            screen.blit(scale(up03, (wi, he)), (xpos1, ypos1))
        elif v1 == -4:
            screen.blit(scale(up04, (wi, he)), (xpos1, ypos1))
        elif v1 == -5:
            screen.blit(scale(up05, (wi, he)), (xpos1, ypos1))
        elif v1 == -6:
            screen.blit(scale(runup01, (wi, he)), (xpos1, ypos1))
        elif v1 == -7:
            screen.blit(scale(runup02, (wi, he)), (xpos1, ypos1))
        elif v1 == -8:
            screen.blit(scale(runup03, (wi, he)), (xpos1, ypos1))
        elif v1 == -9:
            screen.blit(scale(runup04, (wi, he)), (xpos1, ypos1))

        ######## MOVIMENTO PARA A ESQUERDA ##############
        elif v2 == -1:
            screen.blit(scale(left01, (wi, he)), (xpos1, ypos1))
        elif v2 == -2:
            screen.blit(scale(left02, (wi, he)), (xpos1, ypos1))
        elif v2 == -3:
            screen.blit(scale(left03, (wi, he)), (xpos1, ypos1))
        elif v2 == -4:
            screen.blit(scale(left04, (wi, he)), (xpos1, ypos1))
        elif v2 == -5:
            screen.blit(scale(left05, (wi, he)), (xpos1, ypos1))
        elif v2 == -6:
            screen.blit(scale(runleft01, (wi, he)), (xpos1, ypos1))
        elif v2 == -7:
            screen.blit(scale(runleft02, (wi, he)), (xpos1, ypos1))
        elif v2 == -8:
            screen.blit(scale(runleft03, (wi, he)), (xpos1, ypos1))
        elif v2 == -9:
            screen.blit(scale(runleft04, (wi, he)), (xpos1, ypos1))
        elif v2 == -10:
            screen.blit(scale(runleft05, (wi, he)), (xpos1, ypos1))

        ######## MOVIMENTO PARA A DIREITA ##############
        elif v2 == 1:
            screen.blit(scale(right01, (wi, he)), (xpos1, ypos1))
        elif v2 == 2:
            screen.blit(scale(right02, (wi, he)), (xpos1, ypos1))
        elif v2 == 3:
            screen.blit(scale(right03, (wi, he)), (xpos1, ypos1))
        elif v2 == 4:
            screen.blit(scale(right04, (wi, he)), (xpos1, ypos1))
        elif v2 == 5:
            screen.blit(scale(right05, (wi, he)), (xpos1, ypos1))
        elif v2 == 6:
            screen.blit(scale(runright01, (wi, he)), (xpos1, ypos1))
        elif v2 == 7:
            screen.blit(scale(runright02, (wi, he)), (xpos1, ypos1))
        elif v2 == 8:
            screen.blit(scale(runright03, (wi, he)), (xpos1, ypos1))
        elif v2 == 9:
            screen.blit(scale(runright04, (wi, he)), (xpos1, ypos1))
        elif v2 == 10:
            screen.blit(scale(runright05, (wi, he)), (xpos1, ypos1))

        elif v2 == 11:
            screen.blit(scale(attack01, (wi, he)), (xpos1, ypos1))
            v2 += vv
        elif v2 == 12:
            screen.blit(scale(attack02, (wi, he)), (xpos1, ypos1))
            v2 += vv
        elif v2 == 13:
            screen.blit(scale(attack03, (wi, he)), (xpos1, ypos1))
            v2 += vv
        elif v2 == 14:
            screen.blit(scale(attack04, (wi, he)), (xpos1, ypos1))
            v2 = 11

        elif v2 == 15:
            screen.blit(scale(attack05, (wi, he)), (xpos1, ypos1))
            v2 += 1
        elif v2 == 16:
            screen.blit(scale(attack06, (wi, he)), (xpos1, ypos1))
            v2 += 1
        elif v2 == 17:
            screen.blit(scale(attack07, (wi, he)), (xpos1, ypos1))
            v2 += 1
        elif v2 == 18:
            screen.blit(scale(attack08, (wi, he)), (xpos1, ypos1))
            v2 += 1
        elif v2 == 19:
            screen.blit(scale(attack09, (wi, he)), (xpos1, ypos1))
            v2 = 11

        return xpos1, ypos1, v1, v2


    ################################################## MAPAS ###############################################################
    mapa = 0

    start = pygame.image.load(os.path.join('Mapas', 'start.png')).convert()
    instruc = pygame.image.load(os.path.join('Mapas', 'instructions.png')).convert()
    corredor01 = pygame.image.load(os.path.join('Mapas', 'corredor01.png')).convert()
    corredor02 = pygame.image.load(os.path.join('Mapas', 'corredor02.png')).convert()
    sala01 = pygame.image.load(os.path.join('Mapas', 'sala01.png')).convert()
    sala02 = pygame.image.load(os.path.join('Mapas', 'sala02.png')).convert()
    painel = pygame.image.load(os.path.join('Mapas', 'painel.png')).convert()
    polones = pygame.image.load(os.path.join('Mapas', 'penultima fase.png')).convert()
    caverna = pygame.image.load(os.path.join('Mapas', 'fase final.png')).convert()


    def quebra(s, d):
        x = 4
        s = ('{:<8}'.format(s))
        while True:
            ss = []
            dd = []
            d = str(d)
            d = ''.join(d)
            d = ('{:<8}'.format(d))

            for c in range(x):
                ss.append(s[c])
                dd.append(d[c])

            s = ''.join(ss)
            d = ''.join(dd)
            n1 = 0
            r1 = 0
            r2 = 0
            n2 = 0
            for a in range(x):
                if dd[n1] == ss[n1]:
                    r1 += 1
                    ss[n1] = '$'
                    dd[n1] = 'E'
                n1 += 1

            for b in range(x):
                if dd[n2] in ss:
                    r2 += 1
                    n3 = 0
                    for y in range(x):
                        if dd[n2] == ss[n3]:
                            ss[n3] = '$'
                            break
                        n3 += 1
                    dd[n2] = 'B'

                n2 += 1

            return f'({r1})    ({r2})'

################################################ OBJETOS ###############################################################
    fg = 1
    foguinho01 = scale(pygame.image.load(os.path.join('Objetos', 'tochinha01.png')).convert(), (40, 91))
    foguinho02 = scale(pygame.image.load(os.path.join('Objetos', 'tochinha02.png')).convert(), (40, 91))
    foguinho03 = scale(pygame.image.load(os.path.join('Objetos', 'tochinha03.png')).convert(), (40, 91))
    foguinho04 = scale(pygame.image.load(os.path.join('Objetos', 'tochinha04.png')).convert(), (40, 91))
    foguinho05 = scale(pygame.image.load(os.path.join('Objetos', 'tochinha05.png')).convert(), (40, 91))
    foguinho06 = scale(pygame.image.load(os.path.join('Objetos', 'tochinha06.png')).convert(), (40, 91))

    foguinho01.set_colorkey((0, 0, 0))
    foguinho02.set_colorkey((0, 0, 0))
    foguinho03.set_colorkey((0, 0, 0))
    foguinho04.set_colorkey((0, 0, 0))
    foguinho05.set_colorkey((0, 0, 0))
    foguinho06.set_colorkey((0, 0, 0))

    def foguin(fg):
        if fg == 1:
            screen.blit(foguinho01, (380, 150))
            screen.blit(foguinho04, (580, 150))
            fg += 1
        elif fg == 2:
            screen.blit(foguinho02, (380, 150))
            screen.blit(foguinho05, (580, 150))
            fg += 1
        elif fg == 3:
            screen.blit(foguinho03, (380, 150))
            screen.blit(foguinho06, (580, 150))
            fg = 1
        return fg

    screen.fill((255, 255, 255))
    screen.blit(start, (0, 0))

    pygame.display.flip()

    clock = pygame.time.Clock()




    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        if mapa == 0:
            screen.blit(start, (0, 0))

            if (pygame.mouse.get_pos()[0] > 400 and pygame.mouse.get_pos()[0] < 680) and (pygame.mouse.get_pos()[1] > 300 and pygame.mouse.get_pos()[1] < 340):
                R1 = 0
                G1 = 0
                B1 = 255
                if pygame.mouse.get_pressed()[0]:
                    mapa += 1
            elif (pygame.mouse.get_pos()[0] > 400 and pygame.mouse.get_pos()[0] < 680) and (pygame.mouse.get_pos()[1] > 400 and pygame.mouse.get_pos()[1] < 440):
                R2 = 0
                G2 = 0
                B2 = 255
                if pygame.mouse.get_pressed()[0]:
                    mapa += 0.5

            else:
                R1 = 255
                G1 = 255
                B1 = 255
                R2 = 255
                G2 = 255
                B2 = 255

            screen.blit(horrendo01.render('DESTROY THE EVIL', True, (255, 0, 0)), (175, 50))
            screen.blit(start01.render('Game Start', True, (R1, G1, B1)), (400, 300))
            screen.blit(start01.render('Instructions', True, (R2, G2, B2)), (400, 400))

        elif mapa == 0.5:
            screen.blit(instruc, (0, 0))
            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                mapa = 0


        elif mapa == 1:
            screen.blit(sala01, (0, 0))

            if '$' not in ''.join(senha):
                screen.blit(horrendo02.render(f"{quebra(s, int(''.join(senha)))}", True, (255, 0, 0)), ((452, 20)))
                if s == int(''.join(senha)):
                    mapa += 2

            else:
                screen.blit(horrendo02.render('(0)    (0)', True, (255, 0, 0)), ((452, 20)))

            key = pygame.key.get_pressed()

            if key[pygame.K_RSHIFT] and ypos1 < 20 and xpos1 >= 585 and xpos1 <= 665 and v1 < 0:
                senha = ['$', '$', '$', '$']
                mapa += 1

            xpos1, ypos1, v1, v2 = move(60, 84, xpos1, ypos1, v1, v2, 84, 935, 10, 520)






        if mapa == 2:
            screen.blit(painel, (0, 0))

            key = pygame.key.get_pressed()

            if key[pygame.K_1]:
                if senha[0] == '$':
                    senha[0] = '1'
                elif senha[1] == '$':
                    senha[1] = '1'
                elif senha[2] == '$':
                    senha[2] = '1'
                elif senha[3] == '$':
                    senha[3] = '1'

            elif key[pygame.K_2]:
                if senha[0] == '$':
                    senha[0] = '2'
                elif senha[1] == '$':
                    senha[1] = '2'
                elif senha[2] == '$':
                    senha[2] = '2'
                elif senha[3] == '$':
                    senha[3] = '2'

            elif key[pygame.K_3]:
                if senha[0] == '$':
                    senha[0] = '3'
                elif senha[1] == '$':
                    senha[1] = '3'
                elif senha[2] == '$':
                    senha[2] = '3'
                elif senha[3] == '$':
                    senha[3] = '3'

            elif key[pygame.K_4]:
                if senha[0] == '$':
                    senha[0] = '4'
                elif senha[1] == '$':
                    senha[1] = '4'
                elif senha[2] == '$':
                    senha[2] = '4'
                elif senha[3] == '$':
                    senha[3] = '4'

            elif key[pygame.K_5]:
                if senha[0] == '$':
                    senha[0] = '5'
                elif senha[1] == '$':
                    senha[1] = '5'
                elif senha[2] == '$':
                    senha[2] = '5'
                elif senha[3] == '$':
                    senha[3] = '5'

            elif key[pygame.K_6]:
                if senha[0] == '$':
                    senha[0] = '6'
                elif senha[1] == '$':
                    senha[1] = '6'
                elif senha[2] == '$':
                    senha[2] = '6'
                elif senha[3] == '$':
                    senha[3] = '6'

            elif key[pygame.K_7]:
                if senha[0] == '$':
                    senha[0] = '7'
                elif senha[1] == '$':
                    senha[1] = '7'
                elif senha[2] == '$':
                    senha[2] = '7'
                elif senha[3] == '$':
                    senha[3] = '7'

            elif key[pygame.K_8]:
                if senha[0] == '$':
                    senha[0] = '8'
                elif senha[1] == '$':
                    senha[1] = '8'
                elif senha[2] == '$':
                    senha[2] = '8'
                elif senha[3] == '$':
                    senha[3] = '8'

            elif key[pygame.K_9]:
                if senha[0] == '$':
                    senha[0] = '9'
                elif senha[1] == '$':
                    senha[1] = '9'
                elif senha[2] == '$':
                    senha[2] = '9'
                elif senha[3] == '$':
                    senha[3] = '9'

            elif key[pygame.K_0]:
                if senha[0] == '$':
                    senha[0] = '0'
                elif senha[1] == '$':
                    senha[1] = '0'
                elif senha[2] == '$':
                    senha[2] = '0'
                elif senha[3] == '$':
                    senha[3] = '0'

            screen.blit(horrendo01.render(f'{"  ".join(senha)}', True, (255, 255, 255)), ((340, 120)))

            if key[pygame.K_RCTRL]:
                mapa -= 1




        elif mapa == 3:
            screen.blit(sala02, (0, 0))


            if ypos1 < -10:
                v1 = -1
                v2 = 0
                ypos1 = 540
                xpos1 = 460
                mapa += 1

            if (510 > xpos1 > 475 and ypos1 < 15):
                ypos1 += -step_y1
                if v1 <= -5:
                    v1 = -1
                if v1 > -1:
                    v1 = 0
                v1 += -v

            xpos1, ypos1, v1, v2 = move(60, 84, xpos1, ypos1, v1, v2, 84, 935, 10, 520)


        elif mapa == 4:
            screen.blit(corredor01, (0, 0))

            fg = foguin(fg)

            if xpos1 > 450 and xpos1 < 500 and ypos1 < -5:
                mapa += 1

            xpos1, ypos1, v1, v2 = move(60, 84, xpos1, ypos1, v1, v2, 427, 505, -10, 526)





        elif mapa < 6 and mapa >= 5:
            screen.blit(corredor02, (0, 0))
            foguin(fg)
            v1 = 0
            v2 = 1
            xpos1 = 40
            ypos1 = 340
            mapa += 0.5


        elif mapa == 6:
            screen.blit(polones, (0, 0))

            xpos1, ypos1, v1, v2 = move(30, 42, xpos1, ypos1, v1, v2, 25, 1024, 270, 425)

            if xpos1 > 960 and 390 > ypos1 > 330:
                xpos1 = 10
                ypos1 = 450
                mapa += 1

        elif mapa == 7:
            screen.blit(caverna, (0, 0))
            xpos1, ypos1, v1, v2 = move(60, 84, xpos1, ypos1, v1, v2, 10, 962, 260, 600)


        pygame.display.flip()

        clock.tick(10)




if __name__ == '__main__':
    main()