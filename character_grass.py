from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 0
y = 90
count = 0
angle = 270
first = 0

while(True):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x,y)

    if count == 0:
        if x < 780 and y == 90:
            x = x + 2
        elif y < 550 and x == 780:
            y = y + 2
        elif y == 550 and x > 20: 
            x = x - 2
        elif x == 20 and y > 90:
            y = y-2
            if y == 90:
                count = 1

    elif count == 1:
        if first == 0:
            x = 400
            y = 90
            first = 1
        else:
            x = 400 + 200 * math.cos(math.radians(angle))
            y = 290 + 200 * math.sin(math.radians(angle))
            
            angle = angle + 1
            
            if angle == 630:
                count = 0
                x = 0
                y = 90
                first = 0
                angle = 270
            
    delay(0.01)

close_canvas()
    
    


    
    
