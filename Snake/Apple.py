import Global as g
import random

#Yo epic tutorial incoming

#classe Apple con attr: 
# -> bool is_spawned; int x_coord; int y_coord 
class Apple: #Questa è la classe della mela
    def __init__(self): #Questo è il constructor
        self.is_spawned = False #"self." equivale a "this." su java
        loop = True
        while loop: #Tutta questa parte con il loop e i randint è semplicemente la logica per generare coordinate random.
            rnd_x = random.randint(50, 1230)
            rnd_y = random.randint(50, 670)
            loop = not self.valid_pos(rnd_x, rnd_y)    
        self.x_coord = rnd_x
        self.y_coord = rnd_y
        
    def valid_pos(self, x, y): #Controlla se le coordinate sono su uno dei segmenti del serpente
        for segment in g.snake_body:
            if segment[0] <= x <= segment[0]+25 and segment[1] <= y <= segment[1]:
                return False
                break
            else: return True

    def spawn(self): #Questa method semplicemente prende le coordinate x, y dell'oggetto e disegna il quadrato rosso della mela
        g.pygame.draw.rect(g.SCREEN, (200, 0, 0), g.pygame.Rect(self.x_coord, self.y_coord, 20, 20))
        self.is_spawned
      
#Guarda Main.py per l'init dell'oggetto Apple, Line 9
        

"""
quindi: 
la mela può essere creata come oggetto, sceglie delle
coordinate random sullo schermo entro 50px di bordo su
tutti i lati, con valid_pos() controlla se le coordinate 
si trovano sul serpente, con spawn() viene disegnata la 
mela sulle coordinate scelte. Già implementato nel loop
su Main.py controllando se è già spawnata, quindi se la
despawni basta cambiare la variabile self.is_spawned in
'False'.

COME CONTINUARE?
1. Mangiare la mela:
bisogna fare un modo per detectare se il serpente tocca
la mela. Due approcci sono possibili:
        rect1 = g.pygame.Rect(coord_x, coord_y, 20, 20)
        rect2 = g.pygame.Rect(coord_x, coord_y, 20, 20)
    1. rect1.colliderect(rect2)
        non ho ancora testato questa funzione
        quindi poi devi vedere tu come usarla
    2. Spawna le mele solo dove può passare il serpente
        (griglia 25px) e if snake_body[0] == apple.coords:
        apple.gets_eaten() o qualcosa del genere
    Tu prova ad usare la libreria pygame.Rect

2. Allungare il serpente:
se vai a vedere in Input.py, nell'if-elif sotto p.KEYDOWN
vedrai Snake.add_segment(), che allunga automaticamente il 
serpente (trovi la definizione in Snake.py).
Basta Chiamare questa funzione quando collided = True (vedi 1.)

3. Implementa ciò che vuoi
io mi occuperò del fail_state di quando il serpente tocca se 
stesso o i bordi. Lavorerò anche sulla GUI, su un ipotetico menù
iniziale e magari anche su una specie di scoreboard.
Questo lascialo fare a me in modo da evitare conflitti di merge.



"""
