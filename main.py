import pygame
import sys
import time

from constants import (
    SCREEN_WIDTH, SCREEN_HEIGHT, 
    GAME_STATE_START, GAME_STATE_PLAYING, GAME_STATE_PAUSED, 
    GAME_STATE_GAME_OVER, GAME_STATE_WIN
)
from game import Game
from renderer import draw_game, draw_start_screen, draw_pause_screen

def main():
    # Set up the display
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Match & Merge - Number Puzzle")
    clock = pygame.time.Clock()
    
    # Initialize game state
    game = Game()
    running = True
    current_state = GAME_STATE_START
    
    # Main game loop
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            # Handle start screen events
            if current_state == GAME_STATE_START:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    button_rect = draw_start_screen(screen)
                    if button_rect.collidepoint(event.pos):
                        current_state = GAME_STATE_PLAYING
            
            # Handle game events when playing
            elif current_state == GAME_STATE_PLAYING:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        game.move("up")
                    elif event.key == pygame.K_DOWN:
                        game.move("down")
                    elif event.key == pygame.K_LEFT:
                        game.move("left")
                    elif event.key == pygame.K_RIGHT:
                        game.move("right")
                    elif event.key == pygame.K_r:
                        game.reset()
                    elif event.key == pygame.K_c and game.won:
                        game.won = False  # Continue playing after winning
                    elif event.key == pygame.K_ESCAPE:
                        current_state = GAME_STATE_PAUSED
            
            # Handle paused state
            elif current_state == GAME_STATE_PAUSED:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    current_state = GAME_STATE_PLAYING
            
            # Handle game over state
            elif current_state == GAME_STATE_GAME_OVER:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                    game.reset()
                    current_state = GAME_STATE_PLAYING
            
            # Handle win state
            elif current_state == GAME_STATE_WIN:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
                    game.won = False
                    current_state = GAME_STATE_PLAYING
        
        # Draw the appropriate screen based on game state
        if current_state == GAME_STATE_START:
            draw_start_screen(screen)
        elif current_state == GAME_STATE_PLAYING:
            draw_game(screen, game)
            
            # Check for game over or win to update state
            if game.game_over:
                current_state = GAME_STATE_GAME_OVER
            elif game.won:
                current_state = GAME_STATE_WIN
        
        elif current_state == GAME_STATE_PAUSED:
            # Draw the game in the background
            draw_game(screen, game)
            # Draw pause overlay
            draw_pause_screen(screen)
        
        elif current_state == GAME_STATE_GAME_OVER:
            draw_game(screen, game)
        
        elif current_state == GAME_STATE_WIN:
            draw_game(screen, game)
        
        # Update the display
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
