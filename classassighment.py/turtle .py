import turtle
import math

# Set up the screen
wn = turtle.Screen()
wn.bgcolor("black")

# Create the sun
sun = turtle.Turtle()
sun.shape("circle")
sun.color("yellow")
sun.shapesize(4)  # Increase the size of the sun

# Create a dictionary with planet data
planets_data = {
    "Mercury": {"color": "gray", "radius": 50, "speed": 3},
    "Venus": {"color": "orange", "radius": 80, "speed": 2},
    "Earth": {"color": "blue", "radius": 110, "speed": 1.5},
    "Mars": {"color": "red", "radius": 150, "speed": 1},
    "Jupiter": {"color": "tan", "radius": 200, "speed": 0.5},
    "Saturn": {"color": "gold", "radius": 250, "speed": 0.3},
    "Uranus": {"color": "cyan", "radius": 300, "speed": 0.2},
    "Neptune": {"color": "aquamarine", "radius": 350, "speed": 0.15}
}

planets = {}  # Dictionary to store planet turtles

# Create turtles for each planet and set initial position
for planet, data in planets_data.items():
    planets[planet] = turtle.Turtle()
    planets[planet].shape("circle")
    planets[planet].color(data["color"])
    planets[planet].shapesize(0.5)  # Set the size of the planet
    planets[planet].up()
    planets[planet].goto(data["radius"], 0)

# Function to make the planets orbit the sun
def orbit():
    for planet, data in planets_data.items():
        x = data["radius"] * math.cos(math.radians(data["speed"]))  # Orbit radius
        y = data["radius"] * math.sin(math.radians(data["speed"]))
        planets[planet].goto(x, y)
        data["speed"] += 1  # Controls the speed of animation

    wn.ontimer(orbit, 10)  # Call the orbit function again after 10 milliseconds

orbit()  # Start the orbiting animation

turtle.done()
