# stormi.py

import turtle

def shap_pic ():
    glen = turtle.Turtle ()
    glen.color ("pink")
    glen.speed (3)
    glen.shape ("circle")
    
    window = turtle.Screen ()
    window.bgcolor ("red")

    glen.left (90)
    glen.forward (150)
    glen.right (150)
    glen.forward (175)
    glen.right (210)
    glen.forward (150)

    glen.right (90)
    glen.forward (150)

    glen.left (0)
    glen.backward (75)

    glen.right (90)
    glen.forward (150)

    glen.left (270)
    glen.forward (60)

    glen.right (180)
    glen.forward (120)

    glen.backward (60)

    glen.left (90)
    glen.forward (150)

    glen.right (90)
    glen.forward (150)

    glen.right (90)
    glen.forward (150)

    glen.right (90)
    glen.forward (70)
    
    window.exitonclick()


shap_pic ()

        
