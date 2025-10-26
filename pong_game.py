import pygame,sys,random



pygame.init()
clock=pygame.time.Clock()

screen_width=1200
screen_height=700
screen=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Pong")

#pygame.Rect(x,y,width,height) x and y are of the top left corner and the origin is the top left corner of the screen
ball = pygame.Rect(screen_width/2 - 10,screen_height/2 - 10,20,20)
player = pygame.Rect(screen_width-20,screen_height/2 - 70,10,140)
opponent = pygame.Rect(10,screen_height/2 - 70,10,140)

#pygame.draw(surface,color,rect)
bg_color = pygame.Color('grey12')
light_grey = (200,200,200)

ball_speed_x=7*random.choice((1,-1))
ball_speed_y=7*random.choice((1,-1))

player_speed=0
opponent_speed=0

#score
player_score=0
opponent_score=0
font=pygame.font.Font('freesansbold.ttf',24)
player_score_x=screen_width/2 + 20
player_score_y=32
opponent_score_x=screen_width/2 - 32
opponent_score_y=32

def show_score(x,y,entity_score):
    score=font.render(str(entity_score),True,light_grey)
    screen.blit(score,(x,y))

def ball_restart():
    global ball_speed_x,ball_speed_y
    ball.center=(screen_width/2 - 10,screen_height/2 - 10)
    ball_speed_y*=random.choice((1,-1))
    ball_speed_x *= random.choice((1, -1))


while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit() #uninitialises the pygame module
            sys.exit() #exits out of the program

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_DOWN:
                player_speed+=7
            if event.key==pygame.K_UP:
                player_speed-=7




        if event.type==pygame.KEYUP:
            if event.key==pygame.K_DOWN:
                player_speed-=7
            if event.key==pygame.K_UP:
                player_speed+=7

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_s:
                opponent_speed+=7
            if event.key==pygame.K_w:
                opponent_speed-=7




        if event.type==pygame.KEYUP:
            if event.key==pygame.K_s:
                opponent_speed-=7
            if event.key==pygame.K_w:
                opponent_speed+=7

    if player.top<=0:
        player.top=0
    if player.bottom>=screen_height:
        player.bottom=screen_height

    if opponent.top<=0:
        opponent.top=0
    if opponent.bottom>=screen_height:
        opponent.bottom=screen_height

#checks whether the user has closed the game window

    ball.x+=ball_speed_x
    ball.y+=ball_speed_y

    '''if opponent.top<ball.y:
        opponent.top+=opponent_speed
    if opponent.bottom>ball.y:
        opponent.bottom-=opponent_speed'''

    player.y+=player_speed
    opponent.y+=opponent_speed


    if ball.left<=0:
        player_score+=1

    if ball.right>=screen_width:
        opponent_score+=1


    if ball.top<=0 or ball.bottom>=screen_height:
        ball_speed_y*=-1

    if ball.left<=0 or ball.right>=screen_width:
        ball_restart()

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x*=-1



    #visuals
    screen.fill(bg_color)
    #very crucial because without this previous frames will be visible
    #Screen to be drawn first or else screen will be on top of all the other game elements
    pygame.draw.ellipse(screen,light_grey,ball)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)

    pygame.draw.aaline(screen,light_grey,(screen_width/2,0),(screen_width/2,screen_height))
    show_score(player_score_x,player_score_y,player_score)
    show_score(opponent_score_x,opponent_score_y,opponent_score)
    pygame.display.flip()#draws everything to the GAME WINDOW
    clock.tick(60) #sets the tick-rate
