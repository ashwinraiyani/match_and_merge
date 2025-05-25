import pygame
from constants import (
    SCREEN_WIDTH, SCREEN_HEIGHT, GRID_SIZE, CELL_SIZE, GRID_PADDING, HEADER_HEIGHT,
    BACKGROUND_COLOR, GRID_COLOR, EMPTY_CELL_COLOR, TEXT_COLOR, BUTTON_COLOR, 
    BUTTON_HOVER_COLOR, BUTTON_TEXT_COLOR, TILE_COLORS, TEXT_LIGHT, TEXT_DARK,
    title_font, score_font, tile_font, game_over_font, instruction_font, 
    button_font, start_title_font, ANIMATION_SPEED
)

def draw_tile(screen, x, y, value):
    # Get color based on value
    color = TILE_COLORS.get(value, (237, 194, 46))
    
    # Draw tile background
    pygame.draw.rect(screen, color, (x, y, CELL_SIZE, CELL_SIZE), border_radius=5)
    
    # Draw value text
    text_color = TEXT_LIGHT if value > 4 else TEXT_DARK
    text = tile_font.render(str(value), True, text_color)
    
    # Center text on tile
    text_rect = text.get_rect(center=(x + CELL_SIZE/2, y + CELL_SIZE/2))
    screen.blit(text, text_rect)

def draw_game(screen, game):
    # Clear the screen
    screen.fill(BACKGROUND_COLOR)
    
    # Draw header
    title_text = title_font.render("Number Puzzle", True, TEXT_COLOR)
    screen.blit(title_text, (20, 20))
    
    score_text = score_font.render(f"Score: {game.score}", True, TEXT_COLOR)
    screen.blit(score_text, (20, 60))
    
    high_score_text = score_font.render(f"Best: {game.high_score}", True, TEXT_COLOR)
    screen.blit(high_score_text, (SCREEN_WIDTH - 120, 60))
    
    # Draw grid background
    pygame.draw.rect(screen, GRID_COLOR, 
                    (GRID_PADDING, HEADER_HEIGHT, 
                     SCREEN_WIDTH - 2 * GRID_PADDING, 
                     SCREEN_WIDTH - 2 * GRID_PADDING))
    
    # Draw cells
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            # Calculate cell position
            x = GRID_PADDING + j * (CELL_SIZE + GRID_PADDING)
            y = HEADER_HEIGHT + i * (CELL_SIZE + GRID_PADDING)
            
            # Draw empty cell
            pygame.draw.rect(screen, EMPTY_CELL_COLOR, (x, y, CELL_SIZE, CELL_SIZE), border_radius=5)
            
            # Draw tile if not empty
            if game.grid[i][j] != 0:
                draw_tile(screen, x, y, game.grid[i][j])
    
    # Draw animations
    for anim in game.animations[:]:
        from_i, from_j = anim['from']
        to_i, to_j = anim['to']
        
        # Calculate positions
        from_x = GRID_PADDING + from_j * (CELL_SIZE + GRID_PADDING)
        from_y = HEADER_HEIGHT + from_i * (CELL_SIZE + GRID_PADDING)
        to_x = GRID_PADDING + to_j * (CELL_SIZE + GRID_PADDING)
        to_y = HEADER_HEIGHT + to_i * (CELL_SIZE + GRID_PADDING)
        
        # Calculate current position based on progress
        progress = anim['progress'] / 100.0
        current_x = from_x + (to_x - from_x) * progress
        current_y = from_y + (to_y - from_y) * progress
        
        # Draw the animated tile
        draw_tile(screen, current_x, current_y, anim['value'])
        
        # Update animation progress
        anim['progress'] += ANIMATION_SPEED
        if anim['progress'] >= 100:
            game.animations.remove(anim)
    
    # Draw game over message
    if game.game_over:
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((255, 255, 255, 180))
        screen.blit(overlay, (0, 0))
        
        game_over_text = game_over_font.render("Game Over!", True, (119, 110, 101))
        text_rect = game_over_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 30))
        screen.blit(game_over_text, text_rect)
        
        restart_text = score_font.render("Press R to restart", True, (119, 110, 101))
        restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 30))
        screen.blit(restart_text, restart_rect)
    
    # Draw win message
    elif game.won:
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
        overlay.fill((255, 255, 255, 180))
        screen.blit(overlay, (0, 0))
        
        win_text = game_over_font.render("You Win!", True, (119, 110, 101))
        text_rect = win_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 30))
        screen.blit(win_text, text_rect)
        
        continue_text = score_font.render("Press C to continue", True, (119, 110, 101))
        continue_rect = continue_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 30))
        screen.blit(continue_text, continue_rect)
    
    # Draw instructions at the bottom
    instructions = instruction_font.render("Use arrow keys to move. Press R to restart.", True, TEXT_COLOR)
    screen.blit(instructions, (20, SCREEN_HEIGHT - 30))

def draw_start_screen(screen):
    # Fill background
    screen.fill(BACKGROUND_COLOR)
    
    # Draw title
    title_text = start_title_font.render("Match & Merge", True, TEXT_COLOR)
    title_rect = title_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/4))
    screen.blit(title_text, title_rect)
    
    # Draw subtitle
    subtitle_text = title_font.render("Number Puzzle", True, TEXT_COLOR)
    subtitle_rect = subtitle_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/4 + 50))
    screen.blit(subtitle_text, subtitle_rect)
    
    # Draw simple game logo (a stylized 2048 tile)
    logo_size = 120
    logo_x = SCREEN_WIDTH/2 - logo_size/2
    logo_y = SCREEN_HEIGHT/2 - 30
    
    # Draw main tile
    pygame.draw.rect(screen, TILE_COLORS[2048], 
                   (logo_x, logo_y, logo_size, logo_size), border_radius=10)
    
    # Draw logo text
    logo_text = start_title_font.render("2048", True, TEXT_LIGHT)
    logo_text_rect = logo_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 30))
    screen.blit(logo_text, logo_text_rect)
    
    # Create and draw start button
    button_width = 200
    button_height = 60
    button_x = SCREEN_WIDTH/2 - button_width/2
    button_y = SCREEN_HEIGHT/2 + 100
    
    button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
    
    # Check if mouse is hovering over button
    mouse_pos = pygame.mouse.get_pos()
    button_hovered = button_rect.collidepoint(mouse_pos)
    
    # Draw button with hover effect
    button_color = BUTTON_HOVER_COLOR if button_hovered else BUTTON_COLOR
    pygame.draw.rect(screen, button_color, button_rect, border_radius=8)
    
    # Draw button text
    button_text = button_font.render("Start Game", True, BUTTON_TEXT_COLOR)
    button_text_rect = button_text.get_rect(center=button_rect.center)
    screen.blit(button_text, button_text_rect)
    
    return button_rect

def draw_pause_screen(screen):
    # Draw semi-transparent overlay
    overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
    overlay.fill((255, 255, 255, 180))
    screen.blit(overlay, (0, 0))
    
    # Draw pause text
    pause_text = game_over_font.render("PAUSED", True, (119, 110, 101))
    text_rect = pause_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
    screen.blit(pause_text, text_rect)
    
    # Draw resume instructions
    resume_text = score_font.render("Press ESC to resume", True, (119, 110, 101))
    resume_rect = resume_text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 50))
    screen.blit(resume_text, resume_rect)
