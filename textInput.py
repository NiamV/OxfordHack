import pygame as pg
import sys

import imageMapping
import random

pg.init()

screenWidth = 640
screenHeight = 480
screenSize = (screenWidth, screenHeight)
screen = pg.display.set_mode(screenSize)
COLOR_INACTIVE = pg.Color('lightskyblue3')
COLOR_ACTIVE = pg.Color('dodgerblue2')
COLOR_MAIN = pg.Color('azure')
FONT = pg.font.Font(None, 32)

LEFT_MARGIN = 100

# Untested
class Question:

    def __init__(self, number, img, img_id):
        self.color = COLOR_MAIN
        self.img = img

        self.w = screenWidth - (2 * LEFT_MARGIN)
        self.h = 32
        self.x = LEFT_MARGIN
        self.y = LEFT_MARGIN + (200 * number)
        self.inputBox = InputBox(self.x, self.y + (2 * h), self.w, self.h)

    def draw(self, screen): 
        # Draw the goal image
        screen.blit(img, (LEFT_MARGIN, LEFT_MARGIN))

        # Draw the input box
        self.inputBox.draw(screen)


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

def main():
    clock = pg.time.Clock()
    input_box1 = InputBox(100, 100, 140, 32)
    input_box2 = InputBox(100, 300, 140, 32)
    input_boxes = [input_box1, input_box2]
    done = False
    imageCount = 8
    images = []

    # Stopwatch setup
    counter = 0
    timerText = secondsToString(counter).rjust(3)
    pg.time.set_timer(pg.USEREVENT, 1000)

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.USEREVENT: 
                counter += 1
                timerText = secondsToString(counter).rjust(3) if counter > 0 else 'boom!'
            if event.type == pg.KEYDOWN:
                # niamPygame.py
                if event.key == pg.K_SPACE:
                    n = random.randint(1,imageCount*(imageCount-1)*(imageCount-2))
                    images =  imageMapping.images(n, imageCount)
                # end

            for box in input_boxes:
                box.handle_event(event)

        for box in input_boxes:
            box.update()

        # Updates UI
        screen.fill((30, 30, 30))
        for box in input_boxes:
            box.draw(screen)
        for i in range(len(images)):
            eq = pg.image.load("static/Eq" + str(images[i]) + ".png")
            y = 300 * i
            screen.blit(eq, (0,y))

        screen.blit(FONT.render(timerText, True, COLOR_MAIN), (screenWidth - 150, 40))

        pg.display.flip()
        clock.tick(30)


if __name__ == '__main__':
    main()
    pg.quit()