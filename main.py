import os
import json
import pygame
import pygame_gui
from pygame.locals import *


def read_json_file(json_file):
    open_json_file = open(json_file, 'r', encoding='utf-8')
    json_file_loaded = json.load(open_json_file)
    open_json_file.close()
    return json_file_loaded


LAYOUT = read_json_file(os.path.join('Data', 'layout.json'))
GRAPH_GRADIENT = os.path.join('Assets', 'graph_gradient.png')
GRAPH_BLACK = os.path.join('Assets', 'graph_black.png')
GRAPH_WHITE = os.path.join('Assets', 'graph_white.png')
WIDTH, HEIGHT = LAYOUT['column_zero']['square_zero']['source_size']['width'], \
                LAYOUT['column_zero']['square_zero']['source_size']['height']


class graph:
    """ This class creates a graph layout """
    def __init__(self, graph_layout):
        self.graph_layout = graph_layout
        coords = 'coordinates'
        x, y, w, h = ('x', 'y', 'width', 'height')
        x_array = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        y_array = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        column_array = [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
                        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]]
        self.x_array = x_array
        self.y_array = y_array
        self.column_array = column_array
        for i_column, column in enumerate(graph_layout):
            for i_square, square in enumerate(graph_layout[column]):
                square_width, square_height = graph_layout[column][square][coords][w], \
                                              graph_layout[column][square][coords][h]
                x_array[0][i_column] = graph_layout[column][square][coords][x]
                x_array[1][i_column] = graph_layout[column][square][coords][x] + square_width
                y_array[0][i_square] = graph_layout[column][square][coords][y]
                y_array[1][i_square] = graph_layout[column][square][coords][y] + square_height
                column_array[i_column][i_square] = pygame.Rect((x_array[0][i_column], y_array[0][i_square]),
                                                               (square_width, square_height))


'''Create a grid variable that will contain a graph layout.'''
new_grid = [graph(LAYOUT)]


def gooey():
    pygame.init()
    is_running = True
    pygame.display.set_caption('Quick Start')
    window = pygame.display.set_mode((1280, 720))
    gui_manager = pygame_gui.UIManager((1280, 720), os.path.join('Data', 'theme.json'))
    background = pygame.Surface((1920, 1088))
    background.fill(gui_manager.ui_theme.get_colour('dark_bg'))
    clock = pygame.time.Clock()
    graph_gradient = pygame.image.load(GRAPH_GRADIENT)
    graph_black = pygame.image.load(GRAPH_BLACK)
    graph_white = pygame.image.load(GRAPH_WHITE)
    graph_collider = pygame.Rect(0, 0, 1920, 1088)
    window.blit(graph_gradient, graph_collider)
    '''Instantiate a local copy of the x and y array from the graph class for convenient manipulation.'''
    x = [[], []]
    y = [[], []]
    for xn in range(len(new_grid[0].x_array[0])):
        x[0].append(new_grid[0].x_array[0][xn])
        x[1].append(new_grid[0].x_array[1][xn])
    for yn in range(len(new_grid[0].y_array[0])):
        y[0].append(new_grid[0].y_array[0][yn])
        y[1].append(new_grid[0].y_array[1][yn])
    while is_running:
        delta_time = clock.tick(60) / 1000.0
        current_mouse_position = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == QUIT:
                is_running = False
                break
            if event.type == MOUSEMOTION:
                pass
            if event.type == MOUSEBUTTONDOWN:
                '''Get mouse button input.'''
                mouse_button_pressed = pygame.mouse.get_pressed(5)
                '''Check mouse button being pressed.'''
                # print(mouse_button_pressed)
                while mouse_button_pressed[0]:
                    '''Loop through cells.'''
                    for xn in range(len(x[0])):
                        for yn in range(len(y[0])):
                            '''Check if the mouse is inside a cell.'''
                            if current_mouse_position[0] >= x[0][xn]:
                                if current_mouse_position[0] <= x[1][xn]:
                                    if current_mouse_position[1] >= y[0][yn]:
                                        if current_mouse_position[1] <= y[1][yn]:
                                            '''Print the x and y coordinates for all four corners of a cell.'''
                                            # print((x[0][xn], y[0][yn]), (x[1][xn], y[1][yn]))
                                            '''Create a cell at current position.'''
                                            window.blit(graph_black, (x[0][xn], y[0][yn]),
                                                        new_grid[0].column_array[xn][yn])
                                            pass
                                        pass
                                    pass
                                pass
                            pass
                        pass
                    break
                while mouse_button_pressed[2]:
                    '''Check each cell.'''
                    for xn in range(len(x[0])):
                        for yn in range(len(y[0])):
                            '''Check if the mouse is inside a cell.'''
                            if current_mouse_position[0] >= x[0][xn]:
                                if current_mouse_position[0] <= x[1][xn]:
                                    if current_mouse_position[1] >= y[0][yn]:
                                        if current_mouse_position[1] <= y[1][yn]:
                                            '''Print the x and y coordinates for all four corners of a cell.'''
                                            # print((x[0][xn], y[0][yn]), (x[1][xn], y[1][yn]))
                                            '''Create a cell at current position.'''
                                            if pygame.Rect.contains(new_grid[0].column_array[xn][yn],
                                                                    new_grid[0].column_array[xn][yn]):
                                                pass
                                            else:
                                                window.blit(graph_white, (x[0][xn], y[0][yn]),
                                                            new_grid[0].column_array[xn][yn])
                                            pass
                                        pass
                                    pass
                                pass
                            pass
                        pass
                    break
            gui_manager.process_events(event)
        gui_manager.update(delta_time)
        gui_manager.draw_ui(window)
        pygame.display.update()


if __name__ == '__main__':
    '''
    Do:
    new_grid.append(graph(LAYOUT))
    To create a new instance of graph().
    '''
    gooey()
