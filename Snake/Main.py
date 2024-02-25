import Global as g
import Input
import Snake
import Apple as a
import HUD

g.pygame.init()
g.SCREEN.fill((255, 255, 255))
g.pygame.display.set_caption("Snake")
apple1 = a.Apple()

running = True
while running:
    running = Input.handle_input()
    
    #main loop
    if not g.failstate:
        g.SCREEN.fill((200,255,200))
        HUD.draw()
        
        #draw and move the snake
        Snake.move()
        Snake.draw()
        Snake.follow_up()
        g.failstate = Snake.check_if_coll_itself() or Snake.out_of_bounds()
    
        if not apple1.is_spawned and not apple1.eaten:
            apple1.spawn()
        else:
            apple1 = a.Apple()
        apple1.check_collision_w_head()
    #end main loop
        
    #failstate
    else:
        g.SCREEN.fill((255, 255, 255))
        font = g.pygame.font.SysFont(None, 100)
        img = font.render('You Failed!', True, (200, 0, 0))
        g.SCREEN.blit(img, (420, 260))

    g.pygame.display.flip()
    g.clock.tick(120)
    
g.pygame.quit()