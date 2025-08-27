import numpy as np

class TerrainCube:
    def __init__(self, x, y, z, 
                 terrain_type="grass", 
                 height=0, 
                 moisture=0.5, 
                 temperature=20.0):
        """
        Minimal version of TerrainCube for NumPy-based grid.
        Extend attributes later as needed.
        """
        self.x = x
        self.y = y
        self.z = z
        self.terrain_type = terrain_type
        self.height = height
        self.moisture = moisture
        self.temperature = temperature

    def update_height(self, new_height):
        self.height = new_height
        # TODO: auto update terrain_type based on height (your turn!)

    def update_type(self, new_type):
        self.terrain_type = new_type

    def __repr__(self):
        return f"Cube({self.x},{self.y},{self.z})[{self.terrain_type}, h={self.height}]"


def create_terrain_grid(shape=(10, 10, 10), default_height=0):
    """
    Create a 3D NumPy array of TerrainCube objects.
    shape = (z, y, x)
    """
    z_size, y_size, x_size = shape
    grid = np.empty(shape, dtype=object)

    for z in range(z_size):
        for y in range(y_size):
            for x in range(x_size):
                grid[z, y, x] = TerrainCube(x, y, z, height=default_height)

    return grid


def update_tile(grid, x, y, z, height=None, terrain_type=None):
    """Update the TerrainCube at (x,y,z)."""
    cube = grid[z, y, x]
    if height is not None:
        cube.update_height(height)
    if terrain_type is not None:
        cube.update_type(terrain_type)


def print_terrain_slice(grid, z_level):
    """Print a single 2D slice at given z index."""
    y_size, x_size = grid.shape[1], grid.shape[2]
    print(f"Slice at Z={z_level}")
    for y in range(y_size):
        row = [str(grid[z_level, y, x]) for x in range(x_size)]
        print(" | ".join(row))
    print()


def get_neighbors(grid, x, y, z):
    """
    Return valid 6-directional neighbors of a cube.
    TODO: Implement this yourself!
    Hint: check bounds before accessing.
    """
    neighbors = []
    # your code here
    return neighbors


if __name__ == "__main__":
    grid = create_terrain_grid((3, 3, 2), default_height=0)
    print_terrain_slice(grid, 0)

    # Try updating a tile
    update_tile(grid, 1, 1, 0, height=5, terrain_type="mountain")
    print_terrain_slice(grid, 0)

    # TODO: Test your get_neighbors implementation here
