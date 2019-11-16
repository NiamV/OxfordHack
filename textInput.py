import pygame as pg
import sys

import imageMapping
import random

pg.init()

screenWidth = 1000
screenHeight = 750
screenSize = (screenWidth, screenHeight)
screen = pg.display.set_mode(screenSize)
COLOR_INACTIVE = pg.Color('lightskyblue3')
COLOR_ACTIVE = pg.Color('dodgerblue2')
COLOR_MAIN = pg.Color('azure')
FONT = pg.font.Font(None, 32)

LEFT_MARGIN = 100
GAME_LENGTH = 3

# Niam's variables
imageCount = 8
equationsFile = open("static/Equations.txt", "r").read().splitlines()

# Untested
class Question:

    def __init__(self, number, img, goal_text):
        self.color = COLOR_MAIN
        self.img = img
        self.goal_text = goal_text

        self.inputBox = InputBox(LEFT_MARGIN, LEFT_MARGIN + 200, screenWidth - (2 * LEFT_MARGIN), 32)

    def draw(self, screen): 
        # Draw the goal image
        screen.blit(self.img, (LEFT_MARGIN, LEFT_MARGIN))

        # Draw the input box
        self.inputBox.draw(screen)

    def handle_event(self, event):
        self.inputBox.handle_event(event)


class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(screen, self.color, self.rect, 2)

def secondsToString(secs):
    m, s = divmod(secs, 60)
    h, m = divmod(m, 60)

    return '{:d}:{:02d}:{:02d}'.format(h, m, s)

# def newGame():
#     count = 0
#     n = random.randint(1,imageCount*(imageCount-1)*(imageCount-2))
#     threeImages =  imageMapping.images(n, imageCount) # 3-tuple with the 3 id ints
#     eqImg = [pg.image.load("static/Eq" + str(threeImages[i]) + ".png") for i in range(0,3) ]
#     eqTxt = [equationsFile[threeImages[i]-1] for i in range(0,3) ]

#     questions = [ Question(i, eqImg[i], eqTxt[i]) for i in range(GAME_LENGTH)]

#     while not done:
#         for event in pg.event.get():
#                 if event.type == pg.QUIT:
#                         done = True
#                 if event.type == pg.KEYDOWN:
#                     if event.key == pg.K_SPACE:
#                         count += 1
#                         if count > 3:
#                             done = True
#                             break
#                         # Clear screen
#                         screen.fill((0,0,0)) 
#                         # Add next image
#                         screen.blit(eqImg[count-1], (0, 0))

def main():
    clock = pg.time.Clock()
    done = False

    while not done:
        # Stopwatch setup
        counter = 0
        timerText = secondsToString(counter).rjust(3)
        pg.time.set_timer(pg.USEREVENT, 1000)

        count = 0
        n = random.randint(1,imageCount*(imageCount-1)*(imageCount-2))
        threeImages =  imageMapping.images(n, imageCount) # 3-tuple with the 3 id ints
        eqImg = [pg.image.load("static/Eq" + str(threeImages[i]) + ".png") for i in range(0,3) ]
        eqTxt = [equationsFile[threeImages[i]-1] for i in range(0,3) ]

        questions = [ Question(i, eqImg[i], eqTxt[i]) for i in range(GAME_LENGTH)]

        gameDone = False

        while not gameDone:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    done = True
                    gameDone = True
                    break
                if event.type == pg.USEREVENT: 
                    counter += 1
                    timerText = secondsToString(counter).rjust(3)
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                        count += 1
                        if count >= GAME_LENGTH:
                            gameDone = True
                            break 
                        # # Add next image
                        # screen.blit(eqImg[count-1], (0, 0))

                questions[count].inputBox.handle_event(event)
            
            # UI Updates
            screen.fill((30, 30, 30))


            try:
                # Refreshes inputbox size, clears screen, and displays question and timer
                questions[count].inputBox.update()
                questions[count].draw(screen)

                screen.blit(FONT.render(timerText, True, COLOR_MAIN), (screenWidth - 150, 40))
            except IndexError:
                # Shows endgame screen
                screen.blit(FONT.render("You're done!", True, COLOR_MAIN), (LEFT_MARGIN, LEFT_MARGIN))
                pg.display.flip()
                notQuiteDone = True

                # BAD FIX!
                while notQuiteDone:
                    for event in pg.event.get():
                        if event.type == pg.QUIT:
                            done = True
                            gameDone = True
                            notQuiteDone = False
                            break
                        if event.type == pg.KEYDOWN:
                            if event.key == pg.K_RETURN:
                                notQuiteDone = False
                                break

                print("got to end screen")
                

            pg.display.flip()
            clock.tick(30)


if __name__ == '__main__':
    main()
    pg.quit()