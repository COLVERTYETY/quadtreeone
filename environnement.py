import sys
import pygame as pg
import particules
import qtrees
pg.init()
WIDTH=800
HEIGHT=600
screen = pg.display.set_mode((WIDTH,HEIGHT))
font = pg.font.Font(None, 30)
clock = pg.time.Clock()
done = False

particules.particule.SURFACE=screen
particules.particule.generaterandompos(100)

qtrees.quadtree.SURFACE=screen
SEED = qtrees.quadtree(0,0,WIDTH,HEIGHT)
SEED.children.clear()
SEED.construct(particules.particule.ARRAY)

while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True

    screen.fill((0,0,0))
    particules.particule.drawall()
    SEED = qtrees.quadtree(0,0,WIDTH,HEIGHT)
    SEED.children.clear()
    SEED.construct(particules.particule.ARRAY)
    SEED.recursifdraw()
    fps = font.render(str(int(clock.get_fps())), True, pg.Color('white'))
    screen.blit(fps, (10, 10))
    pg.display.flip()
    clock.tick()

pg.quit()
sys.exit()
