import pygame as pg
import moderngl as mgl
import sys
from model import *

class Graphicsengine:
    def __init__(self, win_size=(900, 600)):

        pg.init()

        self.WIN_SIZE = win_size
        # Atributos do opengl
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
        # Cria opengl context
        pg.display.set_mode(self.WIN_SIZE, flags=pg.OPENGL | pg.DOUBLEBUF)
        # Detecta e usa o contexto opengl existente
        self.ctx = mgl.create_context()
        # Cria um objeto para verificar o tempo
        self.clock = pg.time.Clock()
        self.scene = Triangle(self)


    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.scene.destroy()
                pg.quit()
                sys.exit()

    def render(self):
        self.ctx.clear(color=(0.08, 0.16, 0.18))
        self.scene.render()
        pg.display.flip()

    def run(self):
        while True:
            self.check_events()
            self.render()
            self.clock.tick(60)

if __name__ == '__main__':
    app = Graphicsengine()
    app.run()
