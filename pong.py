import pygame as pg
import sys
import time

pg.init()
font = pg.font.Font(None, 36)
pg.display.set_caption("Pong")
screen_height = 400
screen_width = 600
game_screen = pg.display.set_mode((screen_width, screen_height))
red = (217, 28, 28)
white = (255, 255, 255)
blue = (17, 36, 184)
green = (9, 179, 63)
black = (0, 0, 0)
pg.display.update()
ball_x = 300.0
ball_y = 200.0
move_x = 10
move_y = 10
score_p1 = 0
score_p2 = 0
ball_radius = 15
rect1_x = 20
rect1_y = 150
rect1_h = 100
rect1_w = 20
rect2_x = screen_width - 50
rect2_y = 150
rect2_h = 100
rect2_w = 20
game_on = True
mainClock = pg.time.Clock()

pg.init()
pg.display.set_caption('game base')
screen = pg.display.set_mode((600, 300), 0, 32)
font = pg.font.SysFont(None, 30)
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

click = False
def menu():
    while True:
        game_screen.fill((8, 74, 255))
        draw_text('Main Menu', font, (0, 0, 0), game_screen, 250, 40)

        mx, my = pg.mouse.get_pos()
        button_1 = pg.Rect(200, 100, 200, 50)
        button_2 = pg.Rect(200, 180, 200, 50)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if button_1.collidepoint((mx, my)):
                        game()
                    elif button_2.collidepoint((mx, my)):
                        ai()

        pg.draw.rect(game_screen, (255, 8, 8), button_1)
        pg.draw.rect(game_screen, (255, 8, 8), button_2)

        draw_text('2 player', font, (255, 255, 255), game_screen, 270, 115)
        draw_text('1 player', font, (255, 255, 255), game_screen, 250, 195)

        pg.display.update()






def game():
    time.sleep(2)
    font = pg.font.Font(None, 36)
    pg.display.set_caption("Pong")
    screen_height = 400
    screen_width = 600
    game_screen = pg.display.set_mode((screen_width, screen_height))
    red = (217, 28, 28)
    white = (255, 255, 255)
    blue = (17, 36, 184)
    green = (9, 179, 63)
    black = (0, 0, 0)
    pg.display.update()
    ball_x = 300.0
    ball_y = 200.0
    move_x = 2
    move_y = 2
    score_p1 = 0
    score_p2 = 0
    ball_radius = 15
    rect1_x = 20
    rect1_y = 150
    rect1_h = 100
    rect1_w = 20
    rect2_x = screen_width - 50
    rect2_y = 150
    rect2_h = 100
    rect2_w = 20
    game_on = True
    game_screen.fill(black)
    while game_on:
        pressed = pg.key.get_pressed()
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_on = False

        game_screen.fill(black)
        pg.draw.circle(game_screen, white, (ball_x, ball_y), ball_radius, 0)
        pg.draw.rect(game_screen, blue, (rect1_x, rect1_y, rect1_w, rect1_h), 0)
        pg.draw.rect(game_screen, blue, (rect2_x, rect2_y, rect2_w, rect2_h), 0)
        ball_x += move_x
        ball_y += move_y

        if ball_y >= screen_height - 15 or ball_y <= 15:
            move_y *= -1

        if ball_x >= screen_width + 15:
            score_p2 += 1
            ball_x = screen_width / 2
            ball_y = screen_height / 2

            game_screen.fill(black)
            pg.draw.circle(game_screen, white, (ball_x, ball_y), ball_radius, 0)
            pg.draw.rect(game_screen, blue, (rect1_x, rect1_y, rect1_w, rect1_h), 0)
            pg.draw.rect(game_screen, blue, (rect2_x, rect2_y, rect2_w, rect2_h), 0)
            pg.display.update()
            time.sleep(1)

        elif ball_x <= -15:
            score_p1 += 1
            ball_x = screen_width / 2
            ball_y = screen_height / 2

            game_screen.fill(black)
            pg.draw.circle(game_screen, white, (ball_x, ball_y), ball_radius, 0)
            pg.draw.rect(game_screen, blue,(rect1_x , rect1_y , rect1_w , rect1_h ),0 )
            pg.draw.rect(game_screen , blue ,(rect2_x , rect2_y , rect2_w , rect2_h ),0 )
            pg.display.update()
            time.sleep(1)

        if rect1_x < ball_x < rect1_x + rect1_w:
            if rect1_y < ball_y < rect1_y + rect1_h:
                move_x *= -1

        if rect2_x < ball_x < rect2_x + rect2_w:
            if rect2_y < ball_y < rect2_y + rect2_h:
                move_x *= -1

        if pressed[pg.K_UP] and rect2_y >= 0:
            rect2_y -=5
        elif pressed[pg.K_DOWN] and rect2_y <= screen_height - rect2_h:
            rect2_y +=5

        if pressed[pg.K_w] and rect1_y >=0 :
            rect1_y -=5
        elif pressed[pg.K_s] and rect1_y <= screen_height -rect1_h :
            rect1_y +=5

        score_text=f"{score_p2} : {score_p1}"
        score_surface=font.render(score_text,True ,white )
        score_rect=score_surface.get_rect(center=(screen_width/2 ,50 ))
        game_screen.blit(score_surface,score_rect)

        if score_p1==10:
            game_screen.fill(black)
            ss=font.render("Player 1 Won",True ,white )
            game_screen.blit(ss,score_rect)
            pg.display.update()
            time.sleep(5)
            game_on=False

        elif score_p2==10:
            game_screen.fill(black)
            ss=font.render("Player 2 Won",True ,white )
            game_screen.blit(ss,score_rect)
            pg.display.update()
            time.sleep(5)
            game_on=False

        pg.display.update()
        if(game_on==False):
            menu()

def ai():
    font = pg.font.Font(None, 36)
    pg.display.set_caption("Pong")
    screen_height = 400
    screen_width = 600
    game_screen = pg.display.set_mode((screen_width, screen_height))
    red = (217, 28, 28)
    white = (255, 255, 255)
    blue = (17, 36, 184)
    green = (9, 179, 63)
    black = (0, 0, 0)
    pg.display.update()
    ball_x = 300.0
    ball_y = 200.0
    move_x = 2
    move_y = 2
    score_p1 = 0
    score_p2 = 0
    ball_radius = 15
    rect1_x = 20
    rect1_y = 150
    rect1_h = 100
    rect1_w = 20
    rect2_x = screen_width - 50
    rect2_y = 150
    rect2_h = 100
    rect2_w = 20
    game_on = True
    game_screen.fill(black)
    while game_on:
        pressed = pg.key.get_pressed()
        pg.display.update()
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_on = False

        game_screen.fill(black)
        pg.draw.circle(game_screen, white, (ball_x, ball_y), ball_radius, 0)
        pg.draw.rect(game_screen, blue, (rect1_x, rect1_y, rect1_w, rect1_h), 0)
        pg.draw.rect(game_screen, blue, (rect2_x, rect2_y, rect2_w, rect2_h), 0)
        ball_x += move_x
        ball_y += move_y

        if ball_y >= screen_height - 15 or ball_y <= 15:
            move_y *= -1

        if ball_x >= screen_width + 15:
            score_p2 += 1
            ball_x = screen_width / 2
            ball_y = screen_height / 2

            game_screen.fill(black)
            pg.draw.circle(game_screen, white, (ball_x, ball_y), ball_radius, 0)
            pg.draw.rect(game_screen, blue, (rect1_x, rect1_y, rect1_w, rect1_h), 0)
            pg.draw.rect(game_screen, blue, (rect2_x, rect2_y, rect2_w, rect2_h), 0)
            pg.display.update()
            time.sleep(1)

        elif ball_x <= -15:
            score_p1 += 1
            ball_x = screen_width / 2
            ball_y = screen_height / 2

            game_screen.fill(black)
            pg.draw.circle(game_screen, white, (ball_x, ball_y), ball_radius, 0)
            pg.draw.rect(game_screen, blue, (rect1_x, rect1_y, rect1_w, rect1_h), 0)
            pg.draw.rect(game_screen, blue, (rect2_x, rect2_y, rect2_w, rect2_h), 0)
            pg.display.update()
            time.sleep(1)

        if rect1_x < ball_x < rect1_x + rect1_w:
            if rect1_y < ball_y < rect1_y + rect1_h:
                move_x *= -1

        if rect2_x < ball_x < rect2_x + rect2_w:
            if rect2_y < ball_y < rect2_y + rect2_h:
                move_x *= -1

        rect2_y=ball_y-rect2_h/2
        if pressed[pg.K_w] and rect1_y >= 0:
            rect1_y -= 5
        elif pressed[pg.K_s] and rect1_y <= screen_height - rect1_h:
            rect1_y += 5

        score_text = f"{score_p2} : {score_p1}"
        score_surface = font.render(score_text, True, white)
        score_rect = score_surface.get_rect(center=(screen_width / 2, 50))
        game_screen.blit(score_surface, score_rect)

        if score_p1 == 10:
            game_screen.fill(black)
            ss = font.render("ai won", True, white)
            game_screen.blit(ss, score_rect)
            pg.display.update()
            time.sleep(5)
            menu()
            game_on = False

        elif score_p2 == 10:
            game_screen.fill(black)
            ss = font.render("you won", True, white)
            game_screen.blit(ss, score_rect)
            pg.display.update()
            time.sleep(5)
            menu()
            game_on = False

        pg.display.update()
        if (game_on == False):
            menu()
menu()
