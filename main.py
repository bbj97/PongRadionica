import pygame, sys, random 

def ballAnimation():
    global ballSpeedX, ballSpeedY, playerScore, opponentScore, scoreTime

    # Animacija kretanja lopte
    ball.x += ballSpeedX
    ball.y += ballSpeedY

    # Postavljanje granica terena za loptu
    if ball.top <= 0 or ball.bottom >= screenHeight:
        ballSpeedY *= -1

    # Rastavljen IF UVJET na dva dijela, dodan playerScore i opponentScore
    if ball.left <= 0:
        playerScore += 1
        scoreTime = pygame.time.get_ticks() # Biljezenje vremena kad se pogodi lijevi zid


    if ball.right >= screenWidth:
        opponentScore += 1
        scoreTime = pygame.time.get_ticks() # Bilježenje vremena kada se pogodi desni zid


    # Sudaranje lopte sa igracem
    if ball.colliderect(player) and ballSpeedX>0:
        if abs(ball.right - player.left) < 10:
            ballSpeedX *= -1
        elif abs(ball.bottom - player.top) <10 and ballSpeedY > 0 :
            ballSpeedY *= -1
        elif abs(ball.top - player.bottom) < 10 and ballSpeedY < 0:
            ballSpeedY *= -1
            
    # Sudaranje lopte s protivnikom
    if ball.colliderect(opponent):
        if abs(ball.left - opponent.left) < 10:
            ballSpeedX *= -1
        elif abs(ball.bottom - opponent.top) <10 and ballSpeedY > 0 :
            ballSpeedY *= -1
        elif abs(ball.top - opponent.bottom) < 10 and ballSpeedY < 0:
            ballSpeedY *= -1


def playerAnimation():
    # Kretanje playera
    player.y += playerSpeed

    # Granice terena za igraca
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screenHeight:
        player.bottom = screenHeight

def opponentAnimation():
    global opponentSpeed
    # opponent.y += opponentSpeed

    # Granice terena za protivnika
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screenHeight:
        opponent.bottom = screenHeight
    
    # Kretanje uz loptu
    if opponent.top < ball.y:
        opponent.top += opponentSpeed
    if opponent.bottom > ball.y:
        opponent.top -= opponentSpeed

def ballRestart():
    global ballSpeedX, ballSpeedY, scoreTime

    currentTime = pygame.time.get_ticks()
    ball.center = (screenWidth/2, screenHeight/2)

    if currentTime - scoreTime < 2100:
        ballSpeedX, ballSpeedY = 0, 0       # Držanje lopte zaustavljenom 2.1s 
        # CurrentTime - scoreTime, /700, 3-(), Round cijeli broj
        countdownText = gameFont.render(f"{round(3-(currentTime-scoreTime)/700)}", False, lightGrey)
        screen.blit(countdownText, (screenWidth/2,40))
    else: 
        # Kretanje lopte u random smjeru nakon 2.1s 
        ballSpeedX = 7 * random.choice((-1,1))
        ballSpeedY = 7 * random.choice((-1,1))
        scoreTime = None   

         




pygame.init()
clock = pygame.time.Clock()

screenWidth = 1024
screenHeight = 768

screen = pygame.display.set_mode((screenWidth,screenHeight))

# Kreiranje lopte, igrača i protivnika
ball = pygame.Rect(screenWidth/2-15, screenHeight/2-15, 30, 30)
player = pygame.Rect(screenWidth-20, screenHeight/2-70, 10, 140)
opponent = pygame.Rect(10, screenHeight/2-70, 10, 140)


#otvoriti paletu boja
bgColor = pygame.Color('grey12')
lightGrey = (200,200,200)

pygame.display.set_caption("Pong game")

# Brzine lopte po osi
ballSpeedX = 7 * random.choice((-1, 1))
ballSpeedY = -7 * random.choice((-1, 1))
playerSpeed = 0 # prvo vrijednost 0, objekt se ne kreće, zatim vrijednost 7
opponentSpeed = 7 


# Varijable za score tekst
playerScore = 0
opponentScore = 0
gameFont = pygame.font.Font("Oswald-Regular.ttf", 32)

# Timer
scoreTime = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                playerSpeed += 7 # napraviti samo ovu, stisnit i odmah pustit tipku i pokazati
            if event.key == pygame.K_UP:
                playerSpeed -= 7 
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                playerSpeed -= 7
            if event.key == pygame.K_UP:
                playerSpeed += 7
        

    # Iscrtavanje objekata
    screen.fill(bgColor)
    pygame.draw.rect(screen, lightGrey, player)
    pygame.draw.rect(screen, lightGrey, opponent)
    pygame.draw.ellipse(screen, lightGrey, ball)
    pygame.draw.aaline(screen, lightGrey, (screenWidth/2,0), (screenWidth/2,screenHeight))

    # Restart lopte kad se pojavi scoreTime
    if scoreTime:
        ballRestart()
    

    # Funckije za animaciju
    ballAnimation()
    playerAnimation()
    opponentAnimation()
    

    # Ispis na screen
    playerText = gameFont.render(f"{playerScore}", False, lightGrey)
    screen.blit(playerText, (screenWidth/2+20,screenHeight/2))

    opponentText = gameFont.render(f"{opponentScore}", False, lightGrey)
    screen.blit(opponentText, (screenWidth/2-20,screenHeight/2))

    pygame.display.flip()
    clock.tick(60)