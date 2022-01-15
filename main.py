from canvas import Canvas
from shapes import Rectangle, Square

canvas_height = int(input('Enter canvas height: '))
canvas_width = int(input('Enter canvas width: '))

colors = {'white':(255, 255, 255), 'black':(0, 0, 0)}
canvas_color = input('Enter canvas color (white or black): ')

canvas = Canvas(color= colors[canvas_color], height=canvas_height, width=canvas_width)

while True:
    shape_type = input('What do u like to draw? Enter quit to quit. ')
    if shape_type.lower() == 'rectangle':
        x_input = int(input('Enter x of rectangle: '))
        y_input = int(input('Enter y of rectangle: '))
        rect_height = int(input('Enter rectangle height: '))
        rect_width = int(input('Enter rectangle width: '))
        red_input =int(input('How much red do u want (0 to 255)?  '))
        green_input = int(input('How much green do u want (0 to 255)?  '))
        blue_input =int(input('How much blue do u want (0 to 255)?  '))
        rect = Rectangle(color=(red_input, green_input, blue_input), x=x_input, y=y_input, height=rect_height, width=rect_width)
        rect.draw(canvas)

    if shape_type.lower() == 'square':
        x_input = int(input('Enter x of square: '))
        y_input = int(input('Enter y of square: '))
        side_input = int(input('Enter square sides: '))

        red_input =int(input('How much red do u want (0 to 255)?  '))
        green_input = int(input('How much green do u want (0 to 255)?  '))
        blue_input =int(input('How much blue do u want (0 to 255)?  '))
        square = Square(color=(red_input, green_input, blue_input), x=x_input, y=y_input, side=side_input)
        square.draw(canvas)

    if shape_type.lower() == 'quit':
        break

canvas.make('data.png')
