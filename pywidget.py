import pygame
import pygwidgets

pygame.init()

# Set up the display
screen = pygame.display.set_mode((300, 400))
pygame.display.set_caption('Pygwidgets Calculator')

# Create the display box
display_box = pygwidgets.DisplayText(screen, (50, 50), '', fontSize=36)

# Create the number buttons
button_1 = pygwidgets.TextButton(screen, (50, 150), '1')
button_2 = pygwidgets.TextButton(screen, (100, 150), '2')
button_3 = pygwidgets.TextButton(screen, (150, 150), '3')
button_4 = pygwidgets.TextButton(screen, (50, 200), '4')
button_5 = pygwidgets.TextButton(screen, (100, 200), '5')
button_6 = pygwidgets.TextButton(screen, (150, 200), '6')
button_7 = pygwidgets.TextButton(screen, (50, 250), '7')
button_8 = pygwidgets.TextButton(screen, (100, 250), '8')
button_9 = pygwidgets.TextButton(screen, (150, 250), '9')
button_0 = pygwidgets.TextButton(screen, (100, 300), '0')

# Create the operation buttons
button_add = pygwidgets.TextButton(screen, (200, 150), '+')
button_subtract = pygwidgets.TextButton(screen, (200, 200), '-')
button_multiply = pygwidgets.TextButton(screen, (200, 250), '*')
button_divide = pygwidgets.TextButton(screen, (200, 300), '/')
button_equals = pygwidgets.TextButton(screen, (150, 350), '=')
button_clear = pygwidgets.TextButton(screen, (50, 350), 'C')

# Set up the calculator logic
operand_1 = ''
operand_2 = ''
operation = ''
result = ''

# Handle button clicks
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        # Handle number button clicks
        if button_1.handleEvent(event):
            operand_1 += '1'
            display_box.setValue(operand_1)
        elif button_2.handleEvent(event):
            operand_1 += '2'
            display_box.setValue(operand_1)
        elif button_3.handleEvent(event):
            operand_1 += '3'
            display_box.setValue(operand_1)
        elif button_4.handleEvent(event):
            operand_1 += '4'
            display_box.setValue(operand_1)
        elif button_5.handleEvent(event):
            operand_1 += '5'
            display_box.setValue(operand_1)
        elif button_6.handleEvent(event):
            operand_1 += '6'
            display_box.setValue(operand_1)
        elif button_7.handleEvent(event):
            operand_1 += '7'
            display_box.setValue(operand_1)
        elif button_8.handleEvent(event):
            operand_1 += '8'
            display_box.setValue(operand_1)
        elif button_9.handleEvent(event):
            operand_1 += '9'
            display_box.setValue(operand_1)
        elif button_0.handleEvent(event):
            operand_1 += '0'
            display_box.setValue(operand_1)
            
        # Handle operation button clicks
        elif button_add.handleEvent(event):
            operation = '+'
            operand_2 = operand_1
