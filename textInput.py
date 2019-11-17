import pygame as pg
import sys

import imageMapping
import random
import checker
import math

pg.init()

screenWidth = 1000
screenHeight = 750
screenSize = (screenWidth, screenHeight)
screen = pg.display.set_mode(screenSize)
COLOR_INACTIVE = pg.Color('lightskyblue3')
COLOR_ACTIVE = pg.Color('dodgerblue2')
COLOR_MAIN = pg.Color('azure')
FONT_SIZE = 32
FONT = pg.font.Font(None, FONT_SIZE)
TITLE_FONT = pg.font.Font(None, 80)

LEFT_MARGIN = 100
gameLength = 3
NUM_LEVELS = 3

# Niam's variables
equationsFile = [
    open("static/Level1/Equations.txt", "r").read().splitlines(),
    open("static/Level2/Equations.txt", "r").read().splitlines(),
    open("static/Level3/Equations.txt", "r").read().splitlines() 
]

imageCount = [len(equationsFile[i]) for i in range(0,3)]

# Untested
class Question:

    def __init__(self, number, img, goal_text):
        self.color = COLOR_MAIN
        self.img = img
        self.goal_text = goal_text

        self.inputBox = InputBox(LEFT_MARGIN, LEFT_MARGIN + 200, screenWidth - (2 * LEFT_MARGIN), FONT_SIZE)

    def draw(self, screen): 
        # Draw the goal image
        screen.blit(self.img, (LEFT_MARGIN, LEFT_MARGIN))

        # Draw the input box
        self.inputBox.draw(screen)

    def handle_event(self, event):
        self.inputBox.handle_event(event)

    def isCorrect(self):
        return checker.checker(self.goal_text, self.inputBox.text)
        #return True
    
    def amountCorrect(self):
        return checker.amountCorrect(self.goal_text, self.inputBox.text)


class Button:
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

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pg.draw.rect(screen, self.color, self.rect, 2)

class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pg.Rect(x, y, w, h)
        self.color = COLOR_ACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = True

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
                    print("Hit enter")
                    # print(self.text)
                    # self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(self.rect.w, self.txt_surface.get_width()+10)
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

def numPerms (n, p):
    return math.factorial(n) / math.factorial(n-p)

def main():
    clock = pg.time.Clock()
    done = False
    
    # Ensures that the game does not close before the user tells it to
    while not done:
        # Title Screen
        SPACING = 60
        buttons = [ Button(LEFT_MARGIN, LEFT_MARGIN + 100 + SPACING * i, 85, FONT_SIZE, "Level " + str(i+1)) for i in range(NUM_LEVELS) ]
        seedY = buttons[-1].rect.y + FONT_SIZE + SPACING
        seedInput = InputBox(LEFT_MARGIN + 70, seedY - 5, 30, FONT_SIZE)
        gameLengthInput = InputBox(LEFT_MARGIN + 170, seedY + FONT_SIZE + SPACING, 30, FONT_SIZE, "3")
        notSelected = True
        level = 0

        def isValidSeed (s):
            return s > 0 and s <= numPerms(imageCount, gameLength)

        # Keeps user on Title Screen until a level is selected
        while notSelected:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit("Game closed")
                seedInput.handle_event(event)
                gameLengthInput.handle_event(event)
                for button in buttons:
                    button.handle_event(event)
                    if button.active:
                        # Sets 'level' to the selected variable and exits the title screen
                        level = int(button.text[-1])
                        print(level)
                        notSelected = False
                        break

            # Clears screen
            screen.fill((30, 30, 30))

            # Blits game name and buttons
            screen.blit(TITLE_FONT.render("Rapid TeXing", True, COLOR_MAIN), (LEFT_MARGIN, LEFT_MARGIN))
            screen.blit(FONT.render("Seed: ", True, COLOR_MAIN), (LEFT_MARGIN, seedY))
            screen.blit(FONT.render("Game Length: ", True, COLOR_MAIN), (LEFT_MARGIN, seedY + FONT_SIZE + SPACING))
            seedInput.update()
            seedInput.draw(screen)
            gameLengthInput.update()
            gameLengthInput.draw(screen)
            for button in buttons:
                button.draw(screen)

            # Refreshes display
            pg.display.flip()

        # Updates gameLength based on the user's input
        gameLength = int(gameLengthInput.text)

        # Stopwatch setup
        counter = 0
        timerText = secondsToString(counter).rjust(3)
        pg.time.set_timer(pg.USEREVENT, 1000)

        count = 0 # Sets the number of problems done to 0
        numCorrect = 0
        currentImageCount = imageCount[level-1] 
        possibleSeeds = (math.factorial(currentImageCount) / math.factorial(currentImageCount - gameLength))
        try:
            if (isValidSeed(int(seedInput.text))):
                n = int(seedInput.text)
            else:
                n = random.randint(1,possibleSeeds+1)
        except:
            n = random.randint(1,possibleSeeds+1)

        threeImages =  imageMapping.images(n, currentImageCount, gameLength) # 3-tuple with the 3 id ints
        eqImg = [ pg.image.load("static/Level" + str(level) +"/Eq" + str(threeImages[i]) + ".png") for i in range(0,gameLength) ]

        # Returns an image scaled to be at most (screenWidth - 2.0 * LEFT_MARGIN) wide and 150 high
        def scale(img):
            imgWidth = img.get_rect().width
            imgHeight = img.get_rect().height
            scaleFactor = min((screenWidth - 2.0 * LEFT_MARGIN)/imgWidth, 150.0/imgHeight)
            return pg.transform.scale(img, (int(imgWidth * scaleFactor), int(imgHeight * scaleFactor)))

        eqImg = map (scale, eqImg) # Updates eqImg with scaled image versions
        eqTxt = [equationsFile[level-1][threeImages[i]-1] for i in range(0,gameLength) ]

        questions = [ Question(i, eqImg[i], eqTxt[i]) for i in range(gameLength)]
        skipButton = Button(LEFT_MARGIN, screenHeight - 200, 85, FONT_SIZE, "SKIP (+1 minute)")

        gameDone = False

        while not gameDone:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    sys.exit("Game closed")
                if event.type == pg.USEREVENT: 
                    counter += 1
                    timerText = secondsToString(counter).rjust(3)
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_RETURN:
                        if questions[count].isCorrect():
                            count += 1
                            numCorrect += 1
                            if count >= gameLength:
                                endtime = secondsToString(counter).rjust(3)
                                gameDone = True
                                break
                            else:
                                continue
                        # # Add next image
                        # screen.blit(eqImg[count-1], (0, 0))

                questions[count].inputBox.handle_event(event)
                skipButton.handle_event(event)
            
            # UI Updates
            screen.fill((30, 30, 30))

            if skipButton.active:
                count += 1 # Moves onto next question
                counter += 60 # Increases stopwatch count by 1 min (60 seconds)
                timerText = secondsToString(counter).rjust(3)
                if count >= gameLength: # Checks if game is finished
                    endtime = timerText
                    gameDone = True
                skipButton.active = False

            try:
                # Refreshes inputbox size, clears screen, and displays question and timer
                questions[count].inputBox.update()
                questions[count].draw(screen)
                skipButton.update()
                skipButton.draw(screen)

                screen.blit(FONT.render(timerText, True, COLOR_MAIN), (screenWidth - 150, 40))
                screen.blit(FONT.render("Seed: " + str(n), True, COLOR_MAIN), (150, 40))
                screen.blit(FONT.render(questions[count].amountCorrect(), True, (0,255,0)), (100, 350))
            except IndexError:
                # Shows endgame screen
                screen.blit(TITLE_FONT.render("Level completed!", True, COLOR_MAIN), (LEFT_MARGIN, LEFT_MARGIN))
                screen.blit(FONT.render("Time: " + endtime, True, COLOR_INACTIVE), (LEFT_MARGIN, LEFT_MARGIN + 200))
                screen.blit(FONT.render("Score: " + str(numCorrect) + "/" + str(gameLength), True, COLOR_INACTIVE), (LEFT_MARGIN, LEFT_MARGIN + 240))
                screen.blit(FONT.render("Press ENTER to return to the home page", True, COLOR_ACTIVE), (LEFT_MARGIN, LEFT_MARGIN + 440))
                
                pg.display.flip()
                notQuiteDone = True

                while notQuiteDone:
                    for event in pg.event.get():
                        if event.type == pg.QUIT:
                            sys.exit("Game closed")
                        if event.type == pg.KEYDOWN:
                            if event.key == pg.K_RETURN:
                                notQuiteDone = False
                                break

                # print("got to end screen")
                

            pg.display.flip()
            clock.tick(30)


if __name__ == '__main__':
    main()
    pg.quit()