import pygame

from typing import Optional
from math import atan2, degrees


class babyroid:
    def __init__(self, x: int, time: int) -> None:
        """Constructor for babyroids class

        Args:
            x (int): x position of the object
            time (int): time the object will be printed
        """
        self.surf = pygame.image.load('assets/BabyRoid.png')
        self.x = x
        self.x_copy = x
        self.y = -50
        self.time = time
        self.rect = self.surf.get_rect(midbottom=(x, self.y))
        self.taken = False

    def collision_detector(self, obj: pygame.Rect) -> bool:
        """to detect collision towards a babyroid object

        Args:
            obj (pygame.Rect): the obj where the collision detector must detect

        Returns:
            bool: True if the objects collided
        """
        return self.rect.colliderect(obj)

    def move(self, x: int, y: int) -> tuple:
        """moves the babyroid object

        Args:
            x (int): x offset of the object movement
            y (int): y offset of the object movement
        """
        self.x += x
        self.y += y
        self.rect = self.surf.get_rect(midbottom=(self.x, self.y))
        return self.surf, self.rect

    def update(self, obj: pygame.Rect) -> tuple:
        """update the position of the babyroid object

        Args:
            obj (pygame.Rect): the asteroid object to check if collision happens
        """
        global score
        x = 0
        y = 3
        if self.collision_detector(obj):
            score += 1
            self.y = -50
            self.rect = self.surf.get_rect(midbottom=(self.x_copy, -50))
            self.taken = True
            return self.surf, self.rect
        if not self.taken:
            return self.move(x, y)
        return self.surf, self.rect


class bullet:
    def __init__(self, x, y, mouse, x_offset, y_offset):
        """bullet constructor

        Args:
            x (int): intial x position of the bullet
            y (int): intial x position of the bullet
            mouse (tuple<int>): mouse x and y position
            x_offset (int): x speed
            y_offset (int): y speed
        """
        self.surf = pygame.image.load('assets/bullet.png')
        self.x = x
        self.y = y
        self.x_offset = x_offset
        self.y_offset = y_offset
        self.rect = self.surf.get_rect(midbottom=(x, y))

    def collision_detector(self, obj:pygame.Rect) -> bool:
        """collision detector for bullets

        Args:
            obj (pygame.Rect): what object should be tested for collision

        Returns:
            bool: if the objects being checked collided
        """
        return self.rect.colliderect(obj)

    def move(self, x:int, y:int) -> None:
        """method to move the bullet object

        Args:
            x (int): x speed offset
            y (int): y speed offset
        """
        self.x -= x
        self.y -= y
        self.rect = self.surf.get_rect(midbottom=(self.x, self.y))


class ship:
    def __init__(self, type: int, x: int, y: int,
                 cooldown: int, ship_number: int, time: int) -> None:
        """ship constructor

        Args:
            type (int): ship type
            x (int): ship location
            y (int): ship location
            cooldown (int): length in time units which tells how long a ship will be available to shoot again
            ship_number (int): ship identifier
            time (int): in seconds, the time the ship will enter the screen
        """
        self.type = type
        self.x_pos = x
        self.y_pos = y
        self.image = pygame.image.load('assets/ship.png')
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.cooldown = cooldown
        self.ship_number = ship_number
        self.time = time

    def shoot(self, mouse_pos: tuple, run: int, rise: int) -> None:
        """function that will create a bullet from a ship

        Args:
            mouse_pos (tuple<int>): x and y postion of the mouse
            run (int): x offset value
            rise (int): y offset value
        """
        now = pygame.time.get_ticks()
        global previous_time
        if now - previous_time >= self.cooldown:
            previous_time = now
            bullets.append(bullet(self.x_pos, self.y_pos,
                           (mouse_pos[0]-self.x_pos, mouse_pos[1]-self.y_pos), run, rise))

    def rotate(self, run: int, rise: int) -> tuple:
        """a method that makes the ship rotate to follow the mouse cursor

        Args:
            run (int): x offset value
            rise (int): y offset value

        Returns:
            pygame.surface, pygame.rectangle: returns the suface and rectangle of the object
        """
        angle = degrees(atan2(rise, run))
        image = pygame.transform.rotate(self.image, -angle)
        rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        return image, rect


class Level:

    global screen
    global width
    global heigth

    def __init__(self, length: int, start_time: int) -> None:
        """level constructor

        Args:
            length (int): end time of the leve
            start_time (int): starting time of the level
        """
        self.length = length
        self.seconds = 0
        self.ship_queue = []
        self.babyroidQueue = []
        self.shipCounter = 0
        self.mouse_x = 0
        self.mouse_y = 0
        self.start_time = start_time
        self.last_game = 0
        self.restart_count = 0

    def start(self) -> Optional[int]:
        """Main game loop

        Returns:
            Optional[int]: score at the end of the game
        """
        global win
        game_over = False
        game_close = False
        screen.blit(background_surf, background_rect)
        y = 0
        y1 = height

        while not game_over:
            self.seconds = (
                (pygame.time.get_ticks()-self.start_time)/1000) - self.last_game

            mouse_x, mouse_y = pygame.mouse.get_pos()
            ateRhoid_rect = ateRhoid_surf.get_rect(center=(mouse_x, mouse_y))

            while game_close == True:
                screen.blit(background_surf, (0, 0))
                message()
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            self.restart(
                                (pygame.time.get_ticks()-self.start_time)/1000)
                            return
                        if event.key == pygame.K_p:
                            self.restart(
                                (pygame.time.get_ticks()-self.start_time)/1000)
                            self.start()
                        if event.key == pygame.K_c:
                            return score

                    elif event.type == pygame.QUIT:
                        game_over = True
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
            if self.seconds > self.length:
                game_close = True
                win = True

            y += 8
            y1 += 8

            screen.blit(background_surf, (0, y))
            screen.blit(background_surf, (0, y1))

            if y > height:
                y = -height
            if y1 > height:
                y1 = -height

            screen.blit(ateRhoid_surf, ateRhoid_rect)

            flag = self.show_ship((mouse_x, mouse_y), ateRhoid_rect)
            if flag:
                game_close = True

            self.show_babyroid(ateRhoid_rect)

            pygame.display.update()
            clock.tick(60)
        pygame.quit()
        quit()

    def show_ship(self, mouse_pos: tuple, obj: pygame.Rect) -> Optional[bool]:
        """function to put the ship on the screen

        Args:
            mouse_pos (tuple<int>): mouse position
            obj (pygame.rectangle): asteroid object

        Returns:
            bool: if the asteroid object collided to a bullet
        """

        for i in self.ship_queue:
            run, rise = mouse_pos[0]-i.x_pos, mouse_pos[1]-i.y_pos

            if(self.seconds > i.time):
                if(self.seconds < i.time + 3):
                    image, rect = i.rotate(run, rise)
                    i.shoot(mouse_pos, run, rise)
                    screen.blit(image, rect)
        return self.show_bullets(obj)

    def show_babyroid(self, obj: object) -> None:
        """shows babyroid in the screen

        Args:
            obj (object): babyroid instance
        """        
        count = 0
        for i in self.babyroidQueue:
            if self.seconds > i.time:
                print("Babyroid", count, ": ", i.x, " ", i.y)
                surf, rect = i.update(obj)
                screen.blit(surf, rect)
            count += 1

    def add_ship(self, time:int, x:int, y:int, cooldown:int) -> None:
        """adds a ship to the the ship queue

        Args:
            time (int): the time where the ship will be present on the screen
            x (int): x location of the ship
            y (int): y location of the ship
            cooldown (int): shooting cooldown
        """
        ship_1 = ship(1, x, y, cooldown, 0, time)
        self.ship_queue.append(ship_1)

    def add_babyroid(self, time:int, x:int) -> None:
        """adds babyroid entity

        Args:
            time (int): point in time it adds baby roid
            x (int): position of the baby roid
        """        
        bbroid = babyroid(x, time)
        self.babyroidQueue.append(bbroid)

    def restart(self, seconds:float) -> None:
        """restarts the score

        Args:
            seconds (float): time that is assigned to the last game
        """        
        global bullets
        global score
        
        self.last_game = seconds
        self.restart_count += 1
        
        bullets = []
        score = 0
        
        for i in self.babyroidQueue:
            i.y = -50
            i.taken = False

    def show_bullets(self, obj:pygame.Rect) -> bool:
        """shows the bullet on the screen

        Args:
            obj (pygame.rectangle): asteroid object

        Returns:
            bool: if the asteroid object collided to a bullet
        """

        for i in bullets:
            screen.blit(i.surf, i.rect)
            i.move(5 * -(i.x_offset/250), 5 * -(i.y_offset/200))

            if i.collision_detector(obj):
                return True


def initialize_game() -> tuple:
    """initilize the levels of the ateroids game

    Returns:
        level: returns the created levels
    """
    level1 = Level(43, pygame.time.get_ticks())
    level1.add_ship(1, 100, 350, 1500)
    level1.add_ship(4, 600, 350, 1500)
    level1.add_ship(7, 780, 700, 1500)
    level1.add_ship(15, 550, 600, 1500)
    level1.add_ship(18, 400, 150, 1500)
    level1.add_ship(23, 950, 700, 1500)
    level1.add_ship(28, 420, 500, 1500)
    level1.add_ship(33, 1050, 720, 1500)
    level1.add_ship(37, 380, 150, 1500)

    level1.add_babyroid(8, 550)
    level1.add_babyroid(17, 680)
    level1.add_babyroid(34, 566)

    level2 = Level(60, pygame.time.get_ticks())

    level2.add_ship(1, 100, 350, 350)
    level2.add_ship(4, 600, 350, 350)
    level2.add_ship(7, 780, 700, 350)
    level2.add_ship(15, 550, 600, 350)
    level2.add_ship(18, 400, 150, 350)
    level2.add_ship(23, 950, 700, 350)
    level2.add_ship(28, 420, 500, 350)
    level2.add_ship(33, 1050, 720, 350)
    level2.add_ship(37, 380, 150, 350)

    level2.add_babyroid(8, 900)
    level2.add_babyroid(17, 500)
    level2.add_babyroid(34, 650)

    level3 = Level(60, pygame.time.get_ticks())

    level3.add_ship(1, 100, 350, 250)
    level3.add_ship(4, 600, 350, 250)
    level3.add_ship(7, 780, 700, 250)
    level3.add_ship(15, 550, 600, 250)
    level3.add_ship(18, 400, 150, 250)
    level3.add_ship(23, 1050, 700, 250)
    level3.add_ship(28, 420, 500, 250)
    level3.add_ship(33, 950, 720, 250)
    level3.add_ship(37, 380, 150, 250)
    level3.add_ship(40, 800, 600, 100)

    level3.add_babyroid(8, 120)
    level3.add_babyroid(17, 1060)
    level3.add_babyroid(34, 320)

    return (level1, level2, level3)


def start_game(plevel: int) -> Optional[int]:

    level1, level2, level3 = initialize_game()
    if plevel == 1:
        score = level1.start()
    elif plevel == 2:
        score = level2.start()
    elif plevel == 3:
        score = level3.start()
    return score


def message() -> None:
    """ Output the prompt when game_over = true
    """

    global score
    x = 0
    if not win:
        screen.blit(font_style.render("You Lost!", True, 'Red'), (610, 250))
        screen.blit(font_style.render(
            "P - Play Again", True, 'Red'), (610, 270))
        screen.blit(font_style.render("Q - Quit", True, 'Red'), (610, 290))
    else:
        screen.blit(font_style.render("You Win!", True, 'Green'), (610, 250))
        screen.blit(font_style.render(
            "Babyroids Caught:", True, 'Green'), (570, 270))
        for _ in range(0, score):
            bbroid = pygame.image.load("assets/BabyRoid.png")
            bbroid = pygame.transform.scale(bbroid, (50, 50))
            screen.blit(bbroid, (570+x, 300))
            x += 50
        for _ in range(0, 3-score):
            bbroid = pygame.image.load("assets/BabyRoidx.png")
            bbroid = pygame.transform.scale(bbroid, (50, 50))
            screen.blit(bbroid, (570+x, 300))
            x += 50
        screen.blit(font_style.render(
            "Press C to Continue", True, 'Green'), (560, 350))


# if __name__ == '__main__':
pygame.init()

bullets = []
screen = pygame.display.set_mode((1280, 720))
previous_time = pygame.time.get_ticks()
score = 0
width = 250
height = 700
win = False

pygame.display.set_caption('AteRhoids')

clock = pygame.time.Clock()
font_style = pygame.font.Font(None, 25)

background_surf = pygame.image.load('assets/bg.png')
px, py = background_surf.get_size()
background_surf = pygame.transform.scale(background_surf, (px, 700))
background_rect = background_surf.get_rect()

ateRhoid_surf = pygame.image.load('assets/AteRhoids.png')
pygame.mouse.set_pos((250, 700))
ateRhoid_rect = ateRhoid_surf.get_rect(center=(250, 700))

start_game(1)
