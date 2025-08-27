import numpy as np
import random

class TerrainCube:
    def __init__(self, x, y, z, size=1, 
                terrain_type = "grass", 
                height = 0, 
                moisture = 0.5, 
                temperature = 20.0, 
                underground_type = None, 
                underwater_type = None, 
                air_quality = 1.0, 
                elevation_level = 0, 
                veg_density = 0.0, 
                resource_richness = None, 
                weather_safe = True, 
                feature = None):
        """
        Initialize TerrainTile with basic environmental attributes.
        
        Args:
            height (float): Elevation relative to sea level.
            terrain_type (str): Surface type (grass, water, mountain, etc.).
            moisture (float): Soil moisture level between 0 (dry) and 1 (wet).
            temperature (float): Local temperature in Celsius.
            underground_type (str or None): Type of underground layer (soil, rock, cave, magma).
            underwater_type (str or None): Type of underwater feature (reefs, deep water, shallow water).
            air_quality (float): Air purity index (0=polluted, 1=pristine).
            elevation_level (int): Layer index, e.g., negative for underground, 0 for surface, positive for air layers.
            vegetation_density (float): Fraction of tile covered by vegetation (0-1).
            resource_richness (dict or None): Key-value pairs like {'minerals': 0.7, 'water': 0.9}.
            weather_safe (bool): Is the tile safe from severe weather events.
            feature (str or None): Special features like river, forest, cave entrance.
        """
        self.x = x
        self.y = y
        self.z = z
        self.size = size
        self.height = height
        self.terrain_type = terrain_type
        self.moisture = moisture
        self.temperature = temperature
        self.underground_type = underground_type
        self.underwater_type = underwater_type
        self.air_quality = air_quality
        self.elevation_level = elevation_level
        self.veg_density = veg_density
        self.resource_richness = resource_richness if resource_richness else {}
        self.weather_safe = weather_safe
        self.feature = feature

    def update_height(self, new_height):
        self.height = new_height
        self._auto_update_terrain_type()

    def update_type(self, new_type):
        self.terrain_type = new_type

    def update_moisture(self, new_moisture):
        self.moisture = max(0.0, min(1.0, new_moisture))

    def update_temperature(self, new_temp):
        self.temperature = new_temp

    def update_underground_type(self, new_type):
        self.underground_type = new_type

    def update_underwater_type(self, new_type):
        self.underwater_type = new_type

    def update_air_quality(self, new_quality):
        self.air_quality = max(0.0, min(1.0, new_quality))

    def update_elevation_level(self, new_level):
        self.elevation_level = new_level

    def update_vegetation_density(self, new_density):
        self.vegetation_density = max(0.0, min(1.0, new_density))

    def update_resource(self, resource_name, richness):
        self.resource_richness[resource_name] = max(0.0, min(1.0, richness))

    def update_weather_safety(self, is_safe):
        self.weather_safe = is_safe

    def set_feature(self, feature_name):
        self.feature = feature_name

    def _auto_update_terrain_type(self):
        if self.elevation_level < 0:
            # Underground classification
            if self.height < -10:
                self.underground_type = "magma"
                self.terrain_type = "underground_magma"
            elif self.moisture > 0.7:
                self.underground_type = "wet_soil"
                self.terrain_type = "underground_wet_soil"
            else:
                self.underground_type = "rock"
                self.terrain_type = "underground_rock"

        elif self.elevation_level > 0:
            # Aerial classification
            if self.feature == "storm":
                self.terrain_type = "storm_cloud"
            else:
                self.terrain_type = "air"

        else:
            # Surface classification
            if self.height < 0 or self.moisture > 0.8:
                if self.height < -5:
                    self.underwater_type = "deep_water"
                    self.terrain_type = "deep_water"
                else:
                    self.underwater_type = "shallow_water"
                    self.terrain_type = "shallow_water"
                    
            else:
                # Use multiple attributes to classify
                if self.temperature < 0 and self.moisture > 0.5:
                    self.terrain_type = "snow"
                elif self.moisture < 0.2 and self.temperature > 30:
                    self.terrain_type = "desert"
                elif self.vegetation_density > 0.6:
                    self.terrain_type = "forest"
                elif self.height > 15:
                    self.terrain_type = "mountain"
                else:
                    self.terrain_type = "grassland"
            
                # Adjust for features
                if self.feature == "river":
                    self.terrain_type = "river"
                elif self.feature == "volcano":
                    self.terrain_type = "volcanic"

    def is_water(self):
        return self.terrain_type == "water"

    def __str__(self):
        return (f"({self.x}, {self.y}, {self.z}) | Type: {self.terrain_type}, "
                f"Height: {self.height}, Moisture: {self.moisture:.2f}, "
                f"Temp: {self.temperature}°C, Elev: {self.elevation_level}")

def create_terrain_grid_3d(x_size, y_size, z_size, cube_size=1):
    return [[[TerrainCube(x, y, z, cube_size) for x in range(x_size)]
             for y in range(y_size)]
             for z in range(z_size)]

def update_tile(grid, x, y, z, height=None, terrain_type=None):
    """Update the TerrainCube at (x, y, z) with new attributes if provided."""
    if height is not None:
        grid[z][y][x].update_height(height)
    if terrain_type is not None:
        grid[z][y][x].update_type(terrain_type)

def print_terrain_slice(grid, z_level):
    """Print a single horizontal slice (layer) of the 3D grid at z=z_level."""
    print(f"Terrain Slice at Z={z_level}")
    for y in range(len(grid[0])):
        row_str = " | ".join(str(grid[z_level][y][x]) for x in range(len(grid[0][0])))
        print(row_str)
    print()

if __name__ == "__main__":
    grid3d = create_terrain_grid_3d(5, 5, 1)

    print_terrain_slice(grid3d, 0)