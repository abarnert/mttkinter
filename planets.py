import threading
import turtle
import mttkinter

class Planet(turtle.Turtle):
    def __init__(self, y, speed, orbit):
        super().__init__()
        self.shape('circle')
        self.pu()
        self.sety(y)
        self.pd()
        self.speed(speed)
        self.orbit = orbit
    def revolve(self):
        self.circle(self.orbit)

def planets():
    """simulates motion of Mercury, Venus, Earth, and Mars"""

    mercury = Planet(y=-58, speed=7.5, orbit=58)
    venus = Planet(y=-108, speed=3, orbit=108)
    earth = Planet(y=-150, speed=2, orbit=150)
    mars = Planet(y=-228, speed=1, orbit=228)
    planets = (mercury, venus, earth, mars)
    for planet in planets:
        planet.thread = threading.Thread(target=planet.revolve)
        planet.thread.start()
    # We have to do at least one more turtle (or tkinter)
    # operation after starting the threads, or the main
    # thread will try to exit immediately, which will
    # cause it to block on the background threads, which
    # will cause the background threads to queue up events
    # that never get run, and hello deadlock.
    turtle.Screen().exitonclick()

planets()
