import turtle

def backAndForwardLine():
    cellSize = 10
    i=1
    while i < 7:
        turtle.forward( cellSize * 5 ) 
        turtle.right( 90 ) 
        turtle.forward( cellSize ) 
        turtle.right( 90 )
        i=i+1

backAndForwardLine()