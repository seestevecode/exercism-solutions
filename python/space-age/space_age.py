"""Calculate ages on other planets"""

ORBITS = {
    'mercury': 0.2408467,
    'venus': 0.61519726,
    'earth': 1.0,
    'mars': 1.8808158,
    'jupiter': 11.862615,
    'saturn': 29.447498,
    'uranus': 84.016846,
    'neptune': 164.79132
}

EARTH_YEAR_IN_SECONDS = 31_557_600

class SpaceAge:
    
    def __init__(self, seconds):
        self.age_in_earth_years = seconds / EARTH_YEAR_IN_SECONDS

    def on_planet(self, planet):
        return round(self.age_in_earth_years / ORBITS[planet], 2)
    
    def on_mercury(self):
        return SpaceAge.on_planet(self, 'mercury')
        
    def on_venus(self):
        return SpaceAge.on_planet(self, 'venus')
        
    def on_earth(self):
        return SpaceAge.on_planet(self, 'earth')

    def on_mars(self):
        return SpaceAge.on_planet(self, 'mars')

    def on_jupiter(self):
        return SpaceAge.on_planet(self, 'jupiter')

    def on_saturn(self):
        return SpaceAge.on_planet(self, 'saturn')

    def on_uranus(self):
        return SpaceAge.on_planet(self, 'uranus')

    def on_neptune(self):
        return SpaceAge.on_planet(self, 'neptune')
    