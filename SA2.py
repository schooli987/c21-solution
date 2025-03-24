import pygame
import pymunk
import pymunk.pygame_util

def create_ball(space):
    body = pymunk.Body(1, pymunk.moment_for_circle(1, 0, 20))
    body.position = (400, 50)
    shape = pymunk.Circle(body, 20)
    shape.elasticity = 0.2 # Bounciness
    space.add(body, shape)
    return shape
def create_paddle(space, angle):
    body = pymunk.Body(body_type=pymunk.Body.KINEMATIC)
    body.position = (400, 550)
    
    length = 400
    a = (-length//2, 0)
    b = (length//2, 0)
    
    shape = pymunk.Segment(body, a, b, 10)
    shape.elasticity = 1.0
    shape.friction = 0.8
    shape.color = (150, 75, 0, 255)  # Red color (RGBA)
    shape.body.angle = angle
    space.add(body, shape)
    return body, shape

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Bouncing Ball")
clock = pygame.time.Clock()

space = pymunk.Space()
space.gravity = (0, 981)
draw_options = pymunk.pygame_util.DrawOptions(screen)
  
font = pygame.font.Font(None, 36)
ball = create_ball(space)  # Add bouncing ball

paddle_body, paddle = create_paddle(space, angle=0.1)  # Line starts slightly slanted
    
running = True
game_over = False
score = 0
frame_count = 0
while running:
    screen.fill((0, 255, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    paddle_body.angle -= 0.02
                if event.key == pygame.K_RIGHT:
                    paddle_body.angle += 0.02
               

    
    space.step(1/60)
    space.debug_draw(draw_options)
    if paddle_body.position.y > 600:
            game_over = True
    else:
            frame_count += 1
            if frame_count % 60 == 0:  # Increase score every second
                score += 1
    score_text = font.render(f"Score: {score}", True, (0,0,0))
    screen.blit(score_text, (10, 10))    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()


