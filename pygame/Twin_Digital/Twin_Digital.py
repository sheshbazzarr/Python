import pygame
import logging
import random


#constants for the tile size
Tile_size=16
Ui_width=200
Ui_height=600
Tractor_size=12
white=(255,255,255)
light_brown=(210,180,140)
Dark_brown=(101,67,33)
Green=(0,255,0)
Red=(255,0,0)
Title_size=16
#Default field
field_height=20
field_width=20

#class declarations
class Field:
        """
    Represents a virtual field with custom dimensions and layout.

    This class creates a field represented as a two-dimensional grid.
    Each cell of the grid can contain different types of tiles, such as grass, soil, and various border elements.
    The field's dimensions are specified at the time of object creation.
    The class automatically generates the layout of the field, including the borders and inner soil tiles with random variations.

    Attributes:
        width (int): The width of the field specified by the user, excluding the outer grass layer.
        height (int): The height of the field specified by the user, excluding the outer grass layer.
        layout (list): A 2D list representing the field's layout, including the outer grass layer and the specified soil variations.

    Methods:
        generate_field(height, width): Generates the complete layout of the field with specified height and width. It includes an additional outer layer for grass borders and corners and fills the interior with random soil variations.

    Example:
        >>> field = Field(5, 5)
        >>> field.layout
        [['soil_bottom_right', 'soil_bottom', ...], [...], ...]
    """
    def __init__(self,width ,height):
        self.width=width
        self.height=height
        self.layout=self.generate_field(height,width)
    def generate_field(self,height,width):
        height+=2
        width+=2

        field=[['grass' for _in range(width)] for_in range(height)]
        # Define the tile names for the borders, corners, and soil variations
        grass_corner_tl = 'soil_bottom_right'
        grass_corner_tr = 'soil_bottom_left'
        grass_corner_bl = 'soil_top_right'
        grass_corner_br = 'soil_top_left'
        grass_edge_top = 'soil_bottom'
        grass_edge_bottom = 'soil_top'
        grass_edge_left = 'soil_right'
        grass_edge_right = 'soil_left'
        soil_variations = ['soil1', 'soil2', 'soil3']


            # Fill in the corners
        field[1][1] = grass_corner_tl
        field[1][width - 2] = grass_corner_tr
        field[height - 2][1] = grass_corner_bl
        field[height - 2][width - 2] = grass_corner_br
