import pygame
import game
# YOU SHOULD CHANGE THIS TO IMPORT YOUR GAME MODULE
import asteroids

# YOU SHOULD CONFIGURE THESE TO MATCH YOUR GAME
# window title bar text
TITLE = "Asteroids"
# pixels width
WINDOW_WIDTH  = 700
# pixels high
WINDOW_HEIGHT = 600
# frames per second
DESIRED_RATE  = 10

class PygameApp( game.Game ):

    def __init__( self, title, width, height, frame_rate ):

        game.Game.__init__( self, title, width, height, frame_rate )
        
        # create a game instance
        # YOU SHOULD CHANGE THIS TO IMPORT YOUR GAME MODULE
        self.mGame = asteroids.Asteroids( width, height )
        return
        
        
    def game_logic( self, keys, newkeys, buttons, newbuttons, mouse_position, dt ):
        
        x = mouse_position[ 0 ]
        y = mouse_position[ 1 ]

        # Update the state of the game instance
        # YOU SHOULD CHANGE THIS TO IMPORT YOUR GAME MODULE
        # if pygame.K_a in newkeys:
        #     self.mGame.actOnPressA( )
        # elif pygame.K_a in keys:
        #     self.mGame.actOnHoldA( )
        
        # if pygame.K_UP in keys:
        #     self.mGame.actOnHoldUP( )

        # if 1 in newbuttons:
        #     self.mGame.actOnLeftClick( x, y )

        # self.mGame.evolve( dt )

        if pygame.K_a in keys:
            self.mGame.turnShipLeft( 10.0 )

        if pygame.K_d in keys:
            self.mGame.turnShipRight( 10.0 )

        if pygame.K_w in keys:
            self.mGame.accelerateShip(2.0 )

        if pygame.K_s in keys:
            self.mGame.accelerateShip( -2.0)   
        if pygame.K_SPACE in newkeys:
            self.mGame.fire()    
        

        self.mGame.evolve( dt )

        return
    
    def paint( self, surface ):
        # Draw the current state of the game instance
        self.mGame.draw( surface )
        return

def main( ):
    pygame.font.init( )
    game = PygameApp( TITLE, WINDOW_WIDTH, WINDOW_HEIGHT, DESIRED_RATE )
    game.main_loop( )
    
if __name__ == "__main__":
    main( )
