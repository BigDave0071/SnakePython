import pygame
import random

#Settings
screen_w = 1920
screen_h = 1080
velocity = 3 #pixels per frame; MAX is tile_size or size + dist
max_fps = 120
d_size = 60 #default size
d_dist = 5 #default distance

#adjust tile size according to velocity
d_tile_size = d_size + d_dist
if d_tile_size % velocity != 0:
    adj_size = (d_tile_size % velocity) // 2
    adj_dist = (d_tile_size % velocity) - adj_size
    d_size -= adj_size
    d_dist -= adj_dist
    d_tile_size = d_size + d_dist

#adjust screen dimensions according to tile size
screen_w -= screen_w % d_tile_size
screen_h -= screen_h % d_tile_size

#miscellaneous
SCREEN = pygame.display.set_mode([screen_w, screen_h])
clock = pygame.time.Clock()
failstate = False
HUD_w = screen_w
HUD_h = screen_h//10
velocity_start = velocity

#start drawables
bgtile1 = pygame.image.load("drawables/bgtile1.png")
bgtile1 = pygame.transform.scale(bgtile1, (d_tile_size, d_tile_size))
bgtile2 = pygame.image.load("drawables/bgtile2.png")
bgtile2 = pygame.transform.scale(bgtile2, (d_tile_size, d_tile_size))
bgtile3 = pygame.image.load("drawables/bgtile3.png")
bgtile3 = pygame.transform.scale(bgtile3, (d_tile_size, d_tile_size))
bgtile4 = pygame.image.load("drawables/bgtile4.png")
bgtile4 = pygame.transform.scale(bgtile4, (d_tile_size, d_tile_size))

snakesegment_hor = pygame.image.load("drawables/snakesegment.png")
snakesegment_hor = pygame.transform.scale(snakesegment_hor, (d_size, d_size))
snakesegment_vert = pygame.transform.rotate(snakesegment_hor, 90)

snakehead_n = pygame.image.load("drawables/snakehead.png")
snakehead_n = pygame.transform.scale(snakehead_n, (d_size, d_size))
snakehead_e = pygame.transform.rotate(snakehead_n, -90)
snakehead_s = pygame.transform.rotate(snakehead_e, -90)
snakehead_w = pygame.transform.rotate(snakehead_s, -90)

snakelast_w = pygame.image.load("drawables/snakelast.png")
snakelast_w = pygame.transform.scale(snakelast_w, (d_size, d_size))
snakelast_n = pygame.transform.rotate(snakelast_w, -90)
snakelast_e = pygame.transform.rotate(snakelast_n, -90)
snakelast_s = pygame.transform.rotate(snakelast_e, -90)

defapple = pygame.image.load("drawables/defaultapple.png")
defapple = pygame.transform.scale(defapple, (d_size, d_size))
#end drawables

#randomize background
background_arr = [[random.choice([bgtile1, bgtile2, bgtile3, bgtile4]) for x in range(screen_w // d_tile_size)] for y in range(screen_h // d_tile_size)]

def randomize_spawn_pos():
    min_x = d_size * 5 * velocity if d_size * 5 * velocity < screen_w // 2 - d_size else screen_w // 2 - d_size
    max_x = screen_w - d_size * 5 * velocity if screen_w - d_size * 5 * velocity > screen_w // 2 + d_size else screen_w // 2 + d_size
    min_y = HUD_h + d_size * 5 * velocity if HUD_h + d_size * 5 * velocity < screen_h // 2 - d_size else screen_h // 2 - d_size
    max_y = screen_h - d_size * 5 * velocity if screen_h - d_size * 5 * velocity > screen_h // 2 + d_size else screen_h // 2 + d_size
    rnd_x, rnd_y = (random.randint(min_x, max_x), random.randint(min_y, max_y))
    return (rnd_x - rnd_x % d_tile_size, rnd_y - rnd_y % d_tile_size)

def randomize_direction():
    rnd_char_dict = {
        0: 'n',
        1: 's',
        2: 'e',
        3: 'w'
    }
    return rnd_char_dict[random.randint(0, 3)] #north, s, e or w

# initial snake body
head_x, head_y = randomize_spawn_pos()
direction = randomize_direction()
snake_body = [(head_x, head_y, direction)]


#Help functions
def get_middle_pos(w=0, h=0):
    return (screen_w // 2 - w // 2, screen_h // 2 - h // 2)

def reset(): #KEEP UPDATING!!!
    global snake_body
    global direction
    global failstate
    global is_reset

    failstate = False
    new_head_x, new_head_y = randomize_spawn_pos()
    direction = randomize_direction()
    snake_body = [(new_head_x, new_head_y, direction)]