import pygame

# Write the code or pseudo-code in Python for the Ship class
window = pygame.display.set_mode((1280, 720))

class Ship:
    def __init__(self):
        self.xvel = 0
        self.yvel = 0
        self.lasers = pygame.sprite.Group()
        self.image = pygame.image.load('ship.png')
        self.rect = self.image.get_rect()

    def center_ship(self):
        self.rect.midbottom = self.screen.get_rect().midbottom

    def fire(self):
        new_laser = Laser()
        self.lasers.add(new_laser)

    def remove_lasers(self):
        self.lasers.remove()

    def move(self):
        self.rect.top += self.yvel
        self.rect.left += self.xvel

    def draw(self):
        window.blit(self.image, self.rect)

    def update(self):
        keys = pygame.key.get_pressed()
        self.xvel = 0
        self.yvel = 0
        if keys[K_a]:
            self.xvel -= 1
        if keys[K_d]:
            self.xvel += 1
        if keys[K_w]:
            self.yvel -= 1
        if keys[K_s]:
            self.yvel += 1
        if keys[K_SPACE]:
            self.fire()

        self.move()
        self.draw()
        for l in lasers:
            l.update()


# Write the code or pseudo-code in Python for the Vector class
class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector({}, {})'.format(self.x, self.y)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __rmul__(self, k: float):
        return Vector(self.x * k, self.y * k)

    def __mul__(self, k: float):
        return Vector(self.x * k, self.y * k)

    def __truediv__(self, k: float):
        return Vector(self.x / k, self.y / k)

    def __neg__(self):
        return Vector(self.x * -1, self.y * -1)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
