########################################################### UP #########################################################
if not key[pygame.K_LSHIFT] and key[pygame.K_w] and ypos1 > 10:
    ypos1 += -step_y1
    v2 = 0
    if v1 <= -5:
        v1 = -1
    if v1 > -1:
        v1 = 0
    v1 += -v

elif key[pygame.K_LSHIFT] and key[pygame.K_w] and ypos1 > 10:
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
elif not key[pygame.K_LSHIFT] and key[pygame.K_s] and ypos1 < 520:
    ypos1 += step_y1
    v2 = 0
    if v1 >= 6:
        v1 = 2
    if v1 < 1:
        v1 = 0
    v1 += v

elif key[pygame.K_LSHIFT] and key[pygame.K_s] and ypos1 < 520:
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
elif not key[pygame.K_LSHIFT] and key[pygame.K_a] and xpos1 > 84:
    xpos1 += -step_x1
    v1 = 0
    if v2 <= -5:
        v2 = -1
    if v2 > -1:
        v2 = 0
    v2 += -vv

elif key[pygame.K_LSHIFT] and key[pygame.K_a] and xpos1 > 84:
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
elif not key[pygame.K_LSHIFT] and key[pygame.K_d] and xpos1 < 935 - 60:
    xpos1 += step_x1
    v1 = 0
    if v2 >= 5:
        v2 = 1
    if v2 < 1:
        v2 = 0
    v2 += vv

elif key[pygame.K_LSHIFT] and key[pygame.K_d] and xpos1 < 935 - 60:
    xpos1 += (2.5 * step_x1)
    v1 = 0
    if v2 >= 10:
        v2 = 6
    if v2 < 1:
        v2 = 0
    if v2 == 1:
        v2 = 5
    v2 += vv

######## MOVIMENTO PARA BAIXO ###################
if v1 == 1:
    screen.blit(down01, (xpos1, ypos1))
elif v1 == 2:
    screen.blit(down02, (xpos1, ypos1))
elif v1 == 3:
    screen.blit(down03, (xpos1, ypos1))
elif v1 == 4:
    screen.blit(down04, (xpos1, ypos1))
elif v1 == 5:
    screen.blit(down05, (xpos1, ypos1))
elif v1 == 6:
    screen.blit(down06, (xpos1, ypos1))
elif v1 == 7:
    screen.blit(rundown01, (xpos1, ypos1))
elif v1 == 8:
    screen.blit(rundown02, (xpos1, ypos1))
elif v1 == 9:
    screen.blit(rundown03, (xpos1, ypos1))
elif v1 == 10:
    screen.blit(rundown04, (xpos1, ypos1))

######## MOVIMENTO PARA CIMA ##################
elif v1 == -1:
    screen.blit(up01, (xpos1, ypos1))
elif v1 == -2:
    screen.blit(up02, (xpos1, ypos1))
elif v1 == -3:
    screen.blit(up03, (xpos1, ypos1))
elif v1 == -4:
    screen.blit(up04, (xpos1, ypos1))
elif v1 == -5:
    screen.blit(up05, (xpos1, ypos1))
elif v1 == -6:
    screen.blit(runup01, (xpos1, ypos1))
elif v1 == -7:
    screen.blit(runup02, (xpos1, ypos1))
elif v1 == -8:
    screen.blit(runup03, (xpos1, ypos1))
elif v1 == -9:
    screen.blit(runup04, (xpos1, ypos1))

######## MOVIMENTO PARA A ESQUERDA ##############
elif v2 == -1:
    screen.blit(left01, (xpos1, ypos1))
elif v2 == -2:
    screen.blit(left02, (xpos1, ypos1))
elif v2 == -3:
    screen.blit(left03, (xpos1, ypos1))
elif v2 == -4:
    screen.blit(left04, (xpos1, ypos1))
elif v2 == -5:
    screen.blit(left05, (xpos1, ypos1))
elif v2 == -6:
    screen.blit(runleft01, (xpos1, ypos1))
elif v2 == -7:
    screen.blit(runleft02, (xpos1, ypos1))
elif v2 == -8:
    screen.blit(runleft03, (xpos1, ypos1))
elif v2 == -9:
    screen.blit(runleft04, (xpos1, ypos1))
elif v2 == -10:
    screen.blit(runleft05, (xpos1, ypos1))

######## MOVIMENTO PARA A DIREITA ##############
elif v2 == 1:
    screen.blit(right01, (xpos1, ypos1))
elif v2 == 2:
    screen.blit(right02, (xpos1, ypos1))
elif v2 == 3:
    screen.blit(right03, (xpos1, ypos1))
elif v2 == 4:
    screen.blit(right04, (xpos1, ypos1))
elif v2 == 5:
    screen.blit(right05, (xpos1, ypos1))
elif v2 == 6:
    screen.blit(runright01, (xpos1, ypos1))
elif v2 == 7:
    screen.blit(runright02, (xpos1, ypos1))
elif v2 == 8:
    screen.blit(runright03, (xpos1, ypos1))
elif v2 == 9:
    screen.blit(runright04, (xpos1, ypos1))
elif v2 == 10:
    screen.blit(runright05, (xpos1, ypos1))