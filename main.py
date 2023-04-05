# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line
#Part 1: Greet Template
def greet(name, greeting='Hello, <name>!'):
    return greeting.replace('<name>', name)
print(greet('Maxim'))
print(greet('Albert', "What's up, <name>!"))
#Part 2: Force
def force(mass, body='earth'):
    body = body.lower()
    planets = {
        'earth': 9.8,
        'sun': 274,
        'jupiter': 24.9,
        'neptune': 11.2,
        'saturn': 10.4,
        'uranus': 8.9,
        'venus': 8.9,
        'mars': 3.7,
        'mercury': 3.7,
        'moon': 1.6,
        'pluto': 0.6
        }
    force = mass * planets[body]
    return round(force,1)

print(force(4))
print(force(15, 'Moon'))
print(force(3))

#Part 3: Gravity
def pull(m1: float, m2: float, d: float):
    g = 6.674 * 10**-11
    pull = g * ((m1 * m2) / (d**2))
    return pull

print(pull(4.6, 15.4, 3))
