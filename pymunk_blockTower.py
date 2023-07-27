import pygame
import pygame as pg
import pymunk
import pymunk.pygame_util
import math
import time

pygame.init()

WIDTH, HEIGHT = 1440, 2820
window = pygame.display.set_mode((WIDTH, HEIGHT))

def calculate_distance(p1, p2):
	return math.sqrt((p2[1] - p1[1])**2 + (p2[0] - p1[0])**2)
def calculate_angle(p1, p2):
	return math.atan2(p2[1] - p1[1], p2[0] - p1[0])
def draw(space, window, draw_options, line):
	window.fill("black")

	if line:
		pygame.draw.line(window, "black", line[0], line[1], 3)

	space.debug_draw(draw_options)
	pygame.display.update()

def boundaries(space, width, height):
	YELLOW = (0, 0, 0, 100)
	rects = [
		[(width/2, height - 10), (width, 20), (YELLOW, 100)],
		[(width/2, 10), (width, 20), (YELLOW, 100)],
		[(10, height/2), (20, height), (YELLOW, 100)],
		[(width - 10, height/2), (20, height), (YELLOW, 100)]
	]

	for pos, size, color in rects:
		body = pymunk.Body(body_type=pymunk.Body.STATIC)
		body.position = pos
		shape = pymunk.Poly.create_box(body, size)
		shape.elasticity = 0.7
		shape.friction = 0.4
		space.add(body, shape)


# TOWER
def tower(space, width, height):
	f = (205, 155, 90, 100)
	b = (165, 205, 255, 100)
	YELLOW = (240, 240, 0, 100)
	RED = (230, 10, 0, 100)
	BROWN = (100, 190, 0, 100)
	OR = (240, 120, 10, 100) # orange
	WHITE = (255, 255, 255, 100)
	BLUE = (0, 90, 250, 100)
	rects = [
	    [(750, height - 2450), (340, 40), b, 100],
	    [(600, height - 2350), (40, 150), f, 100],
	    [(900, height - 2350), (40, 150), YELLOW, 100],
	    [(750, height - 2250), (340, 40), RED, 100],
	    [(600, height - 2150), (40, 150), YELLOW, 100],
	    [(900, height - 2150), (40, 150), WHITE, 100],
	    [(750, height - 2050), (340, 40), BLUE, 100],
	    [(600, height - 1950), (40, 150), WHITE, 100],
	    [(900, height - 1950), (40, 150), YELLOW, 100],
	    [(750, height - 1850), (340, 40), WHITE, 100],
	    [(600, height - 1750), (40, 150), WHITE, 100],
	    [(900, height - 1750), (40, 150), WHITE, 100],
	    [(750, height - 1650), (340, 40), WHITE, 100],
	    [(900, height - 1550), (40, 150), WHITE, 100],
	    [(600, height - 1550), (40, 150), WHITE, 100],
	    [(750, height - 1450), (340, 40), WHITE, 100],
	    [(600, height - 1350), (40, 150), WHITE, 100],
	    [(900, height - 1350), (40, 150), WHITE, 100],
	    [(750, height - 1250), (340, 40), WHITE, 100],
	    [(600, height - 1150), (40, 150), WHITE, 100],
	    [(900, height - 1150), (40, 150), RED, 100],
	    [(750, height - 1050), (340, 40), WHITE, 100],
	    [(600, height - 950), (40, 150), WHITE, 100],
	    [(900, height - 950), (40, 150), OR, 100],
	    [(750, height - 850), (340, 40), WHITE, 100],
	    [(600, height - 750), (40, 150), BLUE, 100],
	    [(900, height - 750), (40, 150), WHITE, 100],
	    [(750, height - 650), (340, 40), OR, 100],
	    [(600, height - 550), (40, 150), WHITE, 100],
	    [(900, height - 550), (40, 150), OR, 100],
	    [(750, height - 450), (340, 40), WHITE, 100],
	    [(900, height - 350), (40, 150), OR, 100],
	    [(600, height - 350), (40, 150), BROWN, 100],
	    [(750, height - 240), (340, 40), WHITE, 150],
		[(600, height - 120), (40, 200), OR, 100],
		[(900, height - 120), (40, 200), BROWN, 100],
		[(750, height - 170), (40, 85), BROWN, 100],
	#	[(750, height - 100), (240, 40), WHITE, 100],
		[(750, height - 120), (40, 80), BROWN, 100],
	]

	for pos, size, color, mass in rects:
		body = pymunk.Body()#body_type=pymunk.Body.STATIC)
		body.position = pos
		shape = pymunk.Poly.create_box(body, size, radius=3)
		shape.color = color
		shape.mass = mass
		shape.elasticity = 0.85
		shape.friction = 0.4
		space.add(body, shape)		
		
def create_swinging_ball(space):
	rotation_center_body = pymunk.Body(body_type=pymunk.Body.STATIC)
	rotation_center_body.position = (300, 10)
	body = pymunk.Body()
	body.position = (300, 10)
	line = pymunk.Segment(body, (0, 0), (255, 0), 5)
	circle = pymunk.Circle(body, 40, (255, 0))
	line.friction = 1
	circle.friction = 1
	line.mass = 30
	circle.mass = 30
	circle.elasticity = 0.95
	circle.color = (200, 10, 200, 100)
	rotation_center_joint = pymunk.PinJoint(body, rotation_center_body, (0, 0), (0, 0))
	space.add(circle, line, body, rotation_center_joint)

# BALL
def create_ball(space, radius, mass, pos):
	body = pymunk.Body(body_type=pymunk.Body.STATIC)
	body.position = pos
	shape = pymunk.Circle(body, radius)
	shape.mass = mass
	shape.elasticity = 0.95
	shape.friction = 0.4
	shape.color = (115, 115, 115, 100)
	space.add(body, shape)
	return shape
	
def create_ball3(space, radius, mass, pos):
	body = pymunk.Body(body_type=pymunk.Body.STATIC)
	body.position = pos
	shape = pymunk.Circle(body, radius)
	shape.mass = mass
	shape.elasticity = 0.95
	shape.friction = 0.4
	shape.color = (165, 205, 255, 100)
	space.add(body, shape)
	return shape
	
def create_ball2(space, radius, mass, pos):
	body = pymunk.Body() #(body_type=pymunk.Body.STATIC)
	body.position = pos
	shape = pymunk.Circle(body, radius)
	shape.mass = mass
	shape.elasticity = 0.95
	shape.friction = 0.4
	shape.color = (240, 240, 0, 100)
	space.add(body, shape)
	return shape

def run(window, width, height):
	run = True
	clock = pygame.time.Clock()
	fps = 120
	dt = 1 / fps

	space = pymunk.Space()
	space.gravity = (0, 1500)

	boundaries(space, width, height)
	tower(space, width, height)
#	create_swinging_ball(space)

	draw_options = pymunk.pygame_util.DrawOptions(window)

	pressed_pos = None
	ball = None
	ball2 = None

	while run:
		line = None
		if ball and pressed_pos:
			line = [pressed_pos, pygame.mouse.get_pos()]
            
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				break

			if event.type == pygame.MOUSEBUTTONDOWN:
				if not ball:
					pressed_pos = pygame.mouse.get_pos()
					ball = create_ball(space, 20, 10, pressed_pos)
					ball2 = create_ball2(space, 20, 10, pressed_pos)
					ball3 = create_ball3(space, 20, 10, pressed_pos)
					ball4 = create_ball(space, 20, 10, pressed_pos)
					ball5 = create_ball(space, 20, 10, pressed_pos)
				elif pressed_pos:
					ball.body.body_type = pymunk.Body.DYNAMIC
					ball2.body.body_type = pymunk.Body.DYNAMIC
					ball3.body.body_type = pymunk.Body.DYNAMIC
					ball4.body.body_type = pymunk.Body.DYNAMIC
					ball5.body.body_type = pymunk.Body.DYNAMIC
					angle = calculate_angle(*line)
					force = calculate_distance(*line) * 50
					fx = math.cos(angle) * force
					fy = math.sin(angle) * force
					ball.body.apply_impulse_at_local_point((fx, fy), (0, 0))
					ball2.body.apply_impulse_at_local_point((fx, fy), (0, 0))
					ball3.body.apply_impulse_at_local_point((fx, fy), (0, 0))
					ball4.body.apply_impulse_at_local_point((fx, fy), (0, 0))
					ball5.body.apply_impulse_at_local_point((fx, fy), (0, 0))
					pressed_pos = None
				else:
#					space.remove(ball, ball2, ball2.body, ball.body)
					ball = None
#					ball2 = None

		draw(space, window, draw_options, line)
		space.step(dt) 
		clock.tick(fps)
	pygame.quit()

if __name__ == "__main__":
	run(window, WIDTH, HEIGHT)
