import pygame

# Game states
GAME_STATE_START = 0
GAME_STATE_PLAYING = 1
GAME_STATE_PAUSED = 2
GAME_STATE_GAME_OVER = 3
GAME_STATE_WIN = 4

# Constants
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 500
GRID_SIZE = 4
CELL_SIZE = 80
GRID_PADDING = 10
HEADER_HEIGHT = 100
ANIMATION_SPEED = 10

# Colors
BACKGROUND_COLOR = (250, 248, 239)
GRID_COLOR = (187, 173, 160)
EMPTY_CELL_COLOR = (205, 193, 180)
TEXT_COLOR = (119, 110, 101)
BUTTON_COLOR = (142, 122, 101)
BUTTON_HOVER_COLOR = (158, 138, 120)
BUTTON_TEXT_COLOR = (249, 246, 242)
TILE_COLORS = {
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46)
}
TEXT_LIGHT = (249, 246, 242)
TEXT_DARK = (119, 110, 101)

# Initialize pygame and fonts
pygame.init()

# Fonts
title_font = pygame.font.SysFont("Arial", 36, bold=True)
score_font = pygame.font.SysFont("Arial", 24)
tile_font = pygame.font.SysFont("Arial", 36, bold=True)
game_over_font = pygame.font.SysFont("Arial", 48, bold=True)
instruction_font = pygame.font.SysFont("Arial", 16)
button_font = pygame.font.SysFont("Arial", 28, bold=True)
start_title_font = pygame.font.SysFont("Arial", 48, bold=True)
