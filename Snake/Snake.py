import Global as g
frame_count = 0

def draw():
    clear()
    move()
    for segment in g.snake_body:
        g.pygame.draw.rect(g.SCREEN, (0, 200, 0), g.pygame.Rect(segment[0], segment[1], 25, 25))

def move():
    for i, segment in enumerate(g.snake_body):
        if segment[2] == 'n':
            g.snake_body[i] = (segment[0], segment[1]-g.velocity, segment[2])
        elif segment[2] == 's':
            g.snake_body[i] = (segment[0], segment[1]+g.velocity, segment[2])
        elif segment[2] == 'e':
            g.snake_body[i] = (segment[0]+g.velocity, segment[1], segment[2])
        elif segment[2] == 'w':
            g.snake_body[i] = (segment[0]-g.velocity, segment[1], segment[2])

    #handle tail follow-up        
    global frame_count
    frame_count += 1
    if frame_count == 30 / g.velocity:
        frame_count = 0
        for i in range(len(g.snake_body)-1, 0, -1):
            fwd_segment_direction = g.snake_body[i-1][2]
            g.setBodDir(i, fwd_segment_direction)
        g.setBodDir(0, g.direction)

def clear():
    for segment in g.snake_body:
        g.pygame.draw.rect(g.SCREEN, (255, 255, 255), g.pygame.Rect(segment[0], segment[1], 25, 25))
        
def add_segment():
    last_x, last_y, last_direction = g.snake_body[len(g.snake_body)-1]
    offset_dict = {'n': (0,30), 's': (0, -30), 'e': (-30, 0), 'w': (30, 0)}
    offset_x, offset_y = offset_dict[last_direction]
    g.snake_body.append((last_x + offset_x, last_y + offset_y, last_direction))
    
def check_if_coll_itself():
    head_rect = g.pygame.Rect(g.snake_body[0][0], g.snake_body[0][1], 25, 25)
    if len(g.snake_body) > 2:
        temp_rect = [not head_rect.colliderect(g.pygame.Rect(segment[0], segment[1], 25, 25)) for segment in g.snake_body[2:]]
        return not all(temp_rect)
    else: return False
    
def out_of_bounds():
    head_coords = (g.snake_body[0][0], g.snake_body[0][1])
    if head_coords[1] < 100: return True
    elif head_coords[1] > 700: return True
    elif head_coords[0] > 1260: return True
    elif head_coords[0] < 0: return True
    else: return False