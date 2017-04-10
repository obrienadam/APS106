GRAVITY = 9.81

class Rocket:
    def __init__(self, name, mass = 1e5, thrust = 1e7):
        self.name = name
        self.mass = mass
        self.thrust = thrust

        self.vy = 0. # velocity (vertical)
        self.y = 0. # height
        self.time = 0. # flight time

    def acceleration(self):
        return self.thrust/self.mass - GRAVITY # Technically mass would not be a constant!

    def update_position(self, time_step):
        # Use a trapezoidal time integration
        old_vy = self.vy

        self.vy += self.acceleration()*time_step
        self.y += (old_vy + self.vy)/2.*time_step
        self.time += time_step

    def __str__(self):
        return 'Rocket: ' + self.name

    def __len__(self):
        return self.time

if __name__ == '__main__':
    rocket = Rocket('Saturn V', 2.8e6, 3401942.775*9.81)

    print(rocket)

    # or...

    print(str(rocket))

    for i in range(0, 100):
        rocket.update_position(time_step)
        print(rocket)
