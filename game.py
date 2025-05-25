from constants import GRID_SIZE

class Game:
    def __init__(self):
        self.grid = [[0 for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
        self.score = 0
        self.high_score = 0
        self.game_over = False
        self.won = False
        self.animations = []  # List to store animations
        self.add_random_tile()
        self.add_random_tile()
    
    def add_random_tile(self):
        import random
        empty_cells = [(i, j) for i in range(GRID_SIZE) for j in range(GRID_SIZE) if self.grid[i][j] == 0]
        if empty_cells:
            i, j = random.choice(empty_cells)
            self.grid[i][j] = 2 if random.random() < 0.9 else 4
            return True
        return False
    
    def move(self, direction):
        if self.game_over:
            return False
        
        # Save the current grid state to check if it changes
        old_grid = [row[:] for row in self.grid]
        self.animations = []  # Clear previous animations
        
        # Process the move based on direction
        if direction == "up":
            self.move_up()
        elif direction == "down":
            self.move_down()
        elif direction == "left":
            self.move_left()
        elif direction == "right":
            self.move_right()
        
        # Check if the grid changed
        moved = old_grid != self.grid
        
        # Add a new tile if the move was valid
        if moved:
            self.add_random_tile()
            
            # Check for game over or win
            self.check_game_state()
            
            # Update high score
            if self.score > self.high_score:
                self.high_score = self.score
            
        return moved
    
    def move_left(self):
        for i in range(GRID_SIZE):
            # Merge tiles
            line = [tile for tile in self.grid[i] if tile != 0]
            for j in range(len(line) - 1):
                if line[j] == line[j + 1]:
                    line[j] *= 2
                    self.score += line[j]
                    line[j + 1] = 0
            
            # Remove zeros after merging
            line = [tile for tile in line if tile != 0]
            
            # Add animations for moved tiles
            for j in range(len(line)):
                if j < len(line) and self.grid[i][j] != line[j]:
                    # Find the original position of this tile
                    for old_j in range(GRID_SIZE):
                        if self.grid[i][old_j] == line[j]:
                            self.animations.append({
                                'from': (i, old_j),
                                'to': (i, j),
                                'value': line[j],
                                'progress': 0
                            })
                            break
            
            # Fill the row with the merged line and zeros
            self.grid[i] = line + [0] * (GRID_SIZE - len(line))
    
    def move_right(self):
        for i in range(GRID_SIZE):
            # Merge tiles
            line = [tile for tile in self.grid[i] if tile != 0]
            for j in range(len(line) - 1, 0, -1):
                if line[j] == line[j - 1]:
                    line[j] *= 2
                    self.score += line[j]
                    line[j - 1] = 0
            
            # Remove zeros after merging
            line = [tile for tile in line if tile != 0]
            
            # Add animations for moved tiles
            zeros = GRID_SIZE - len(line)
            for j in range(GRID_SIZE - 1, -1, -1):
                new_j = j - zeros
                if new_j >= 0 and self.grid[i][j] != line[new_j]:
                    # Find the original position of this tile
                    for old_j in range(GRID_SIZE):
                        if self.grid[i][old_j] == line[new_j]:
                            self.animations.append({
                                'from': (i, old_j),
                                'to': (i, j),
                                'value': line[new_j],
                                'progress': 0
                            })
                            break
            
            # Fill the row with zeros and the merged line
            self.grid[i] = [0] * (GRID_SIZE - len(line)) + line
    
    def move_up(self):
        for j in range(GRID_SIZE):
            # Extract column
            column = [self.grid[i][j] for i in range(GRID_SIZE) if self.grid[i][j] != 0]
            
            # Merge tiles
            for i in range(len(column) - 1):
                if column[i] == column[i + 1]:
                    column[i] *= 2
                    self.score += column[i]
                    column[i + 1] = 0
            
            # Remove zeros after merging
            column = [tile for tile in column if tile != 0]
            
            # Add animations for moved tiles
            for i in range(len(column)):
                if i < len(column) and self.grid[i][j] != column[i]:
                    # Find the original position of this tile
                    for old_i in range(GRID_SIZE):
                        if self.grid[old_i][j] == column[i]:
                            self.animations.append({
                                'from': (old_i, j),
                                'to': (i, j),
                                'value': column[i],
                                'progress': 0
                            })
                            break
            
            # Update the grid with the merged column
            for i in range(GRID_SIZE):
                self.grid[i][j] = column[i] if i < len(column) else 0
    
    def move_down(self):
        for j in range(GRID_SIZE):
            # Extract column
            column = [self.grid[i][j] for i in range(GRID_SIZE) if self.grid[i][j] != 0]
            
            # Merge tiles
            for i in range(len(column) - 1, 0, -1):
                if column[i] == column[i - 1]:
                    column[i] *= 2
                    self.score += column[i]
                    column[i - 1] = 0
            
            # Remove zeros after merging
            column = [tile for tile in column if tile != 0]
            
            # Add animations for moved tiles
            zeros = GRID_SIZE - len(column)
            for i in range(GRID_SIZE - 1, -1, -1):
                new_i = i - zeros
                if new_i >= 0 and self.grid[i][j] != column[new_i]:
                    # Find the original position of this tile
                    for old_i in range(GRID_SIZE):
                        if self.grid[old_i][j] == column[new_i]:
                            self.animations.append({
                                'from': (old_i, j),
                                'to': (i, j),
                                'value': column[new_i],
                                'progress': 0
                            })
                            break
            
            # Update the grid with the merged column
            for i in range(GRID_SIZE):
                self.grid[i][j] = column[i - zeros] if i >= zeros else 0
    
    def check_game_state(self):
        # Check for 2048 tile (win condition)
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if self.grid[i][j] == 2048:
                    self.won = True
        
        # Check if there are any empty cells
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE):
                if self.grid[i][j] == 0:
                    return  # Game not over
        
        # Check if there are any possible moves
        for i in range(GRID_SIZE):
            for j in range(GRID_SIZE - 1):
                if self.grid[i][j] == self.grid[i][j + 1]:
                    return  # Game not over
        
        for j in range(GRID_SIZE):
            for i in range(GRID_SIZE - 1):
                if self.grid[i][j] == self.grid[i + 1][j]:
                    return  # Game not over
        
        # If we get here, game is over
        self.game_over = True
    
    def reset(self):
        self.__init__()
        self.high_score = self.high_score  # Preserve high score
