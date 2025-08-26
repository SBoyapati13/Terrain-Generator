class TerrainTile:
    def __init__(self, height = 0, terrain_type = "grass") -> None:
        self.height = height
        self.terrain_type = terrain_type

    def update_height(self, new_height):
        self.height = new_height

    def update_type(self, new_type):
        self.terrain_type = new_type

    def __str__(self) -> str:
        return f"Type: {self.terrain_type}, Height: {self.height}"

def create_terrain_grid(rows, cols):
    return [[TerrainTile() for _ in range(cols)] for _ in range(rows)]

def update_tile(grid, x, y, height = None, terrain_type = None):
    if height is not None:
        grid[x][y].update_height(height)
    
    if terrain_type is not None:
        grid[x][y].update_type(terrain_type)

def print_terrain_grid(grid):
    for row in grid:
        print(" | ".join(str(tile) for tile in row))
    print()

if __name__ == "__main__":
    grid = create_terrain_grid(5, 5)

    update_tile(grid, 0, 0, height = 10, terrain_type = "water")
    update_tile(grid, 2, 3, height = 5, terrain_type = "mountain")

    print_terrain_grid(grid)