import pygame
import game
import frogger

TITLE = "Frogger"
CELL_SIZE = 50
NUM_COL = 14
NUM_ROW = 12 # change this for more or less roads
WINDOW_WIDTH  = NUM_COL * CELL_SIZE
WINDOW_HEIGHT = NUM_ROW * CELL_SIZE
DESIRED_RATE  = 60

class PygameApp( game.Game ):

    def __init__( self, title, width, height, frame_rate ):
        super().__init__( title, width, height, frame_rate )
        self.mGame = frogger.Frogger(CELL_SIZE, NUM_COL, NUM_ROW)
        
    def game_logic( self, keys, newkeys, buttons, newbuttons, mouse_position, dt ):
        if pygame.K_UP in keys:
            self.mGame.UP( )

        if pygame.K_RIGHT in keys:
            self.mGame.RIGHT( )

        if pygame.K_LEFT in keys:
            self.mGame.LEFT( )

        if pygame.K_DOWN in keys:
            self.mGame.DOWN( )

        self.mGame.evolve(dt)

    def paint( self, surface ):
        self.mGame.draw( surface )

def main( ):
    pygame.font.init( )
    game = PygameApp( TITLE, WINDOW_WIDTH, WINDOW_HEIGHT, DESIRED_RATE )
    game.main_loop( )
    
if __name__ == "__main__":
    main( )
