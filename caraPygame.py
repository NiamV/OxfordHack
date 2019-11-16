import pygame as pg


pg.init()
screen = pg.display.set_mode((128, 128))
clock = pg.time.Clock()

counter, text = 0, '0'.rjust(3)
pg.time.set_timer(pg.USEREVENT, 1000)
font = pg.font.SysFont('Consolas', 30)

while True:
    for e in pg.event.get():
        if e.type == pg.USEREVENT: 
            counter += 1
            text = str(counter).rjust(3) if counter > 0 else 'boom!'
        if e.type == pg.QUIT: break
    else:
        screen.fill((255, 255, 255))
        screen.blit(font.render(text, True, (0, 0, 0)), (32, 48))
        pg.display.flip()
        clock.tick(60)
        continue
    break