import threading
import turtle
import mttkinter

def planets():
    """simulates motion of Mercury, Venus, Earth, and Mars"""

    mercury = turtle.Turtle()
    venus = turtle.Turtle()
    earth = turtle.Turtle()
    mars = turtle.Turtle()
    mercury.shape('circle')
    venus.shape('circle')
    earth.shape('circle')
    mars.shape('circle')
    mercury.pu()
    venus.pu()
    earth.pu()
    mars.pu()
    mercury.sety(-58)
    venus.sety(-108)
    earth.sety(-150)
    mars.sety(-228)
    mercury.pd()
    venus.pd()
    earth.pd()
    mars.pd()
    mars.speed(7.5)
    venus.speed(3)
    earth.speed(2)
    mars.speed(1)
    t = [threading.Thread(target=f) for f in [
         (lambda: mercury.circle(58)),
         (lambda: venus.circle(108)),
         (lambda: earth.circle(150)),
         (lambda: mars.circle(228))]]
    for i in t:
        i.start()
    # We have to do at least one more turtle (or tkinter)
    # operation after starting the threads, or the main
    # thread will try to exit immediately, which will
    # cause it to block on the background threads, which
    # will cause the background threads to queue up events
    # that never get run, and hello deadlock.
    dummy = turtle.Turtle()

planets()
