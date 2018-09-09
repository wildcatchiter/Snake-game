import time	
import pygame as py
import sys
from random import randint as r 
from pygame.locals import *


class Apple:
	pos_x = 0
	pos_y = 0
	speed = 50

	def __init__(self, pos_x, pos_y):
		self.pos_x = self.pos_x * self.speed
		self.pos_y = self.pos_y * self.speed

	def draw(self, surface, image):
		surface.blit(image, (self.pos_x, self.pos_y))

class Player:
	x = [1]
	y = [1]

	step = 5
	count = 0 
	count_max = 2

	length = 1
	direction = ''
	speed = 20

	def __init__(self):
		for i in range(2000):
			self.x.append(-100)
			self.y.append(-100)	

	def draw(self, surface, image):
		for i in range(0, self.length - 1):
			surface.blit(image,(self.x[i], self.y[i]))
	
	def update(self):
		self.count += 1
		if self.count > self.count_max:
			
			for i in range(self.length - 1, 0, -1):
				self.x[i] = self.x[i - 1] 
				self.y[i] = self.y[i - 1] 

			if self.direction == 'LEFT':
				self.x[0] -= self.speed
				
			if self.direction == 'RIGHT': 
				self.x[0] += self.speed
					
			if self.direction == 'DOWN': 
				self.y[0] += self.speed
					
			if self.direction == 'UP':
				self.y[0] -= self.speed 

			self.count = 0

	def moveLeft(self):
		self.direction = 'LEFT' 

	def moveRight(self):
		self.direction = 'RIGHT'

	
	def moveDown(self):
		self.direction = 'DOWN'
	
	def moveUp(self):
		self.direction = 'UP'	


class Game:
	def isCollision(self, x, y, pos_x, pos_y, bsize):
		if	pos_x - bsize <= x <= pos_x + bsize and pos_y - bsize <= y <= pos_y + bsize:
				return True
		return False

class App:
	py.init()
	#py.time.delay(1000)

	screen_width = 600
	screen_height = 600
	
	def __init__ (self):
		self.running = True
		self.game = Game()

		self.player = Player()
		self.apple = Apple(5,5)

	def on_render(self):
		self.player.draw(self.window, self.image)
		self.apple.draw(self.window, self.food) 
		py.display.flip()

	#def on_init(self):
	#	self.window.fill((0,0,0))

	def dr(self, x, y):
		self.position_x = x
		self.position_y = y

		self.window.blit(self.image, (self.position_x, self.position_y))

		py.display.update()
		py.time.delay(15)

	def on_loop(self):
		
		for i in range(2, self.player.length):
			if self.game.isCollision(self.player.x[0], self.player.y[0], self.player.x[i], self.player.y[i], 15):
				#print('You lose! Score: ' + str(self.player.length - 1))
				self.restart()
				break
				exit(0)
		
		#for i in range(0, self.player.length):
		if self.game.isCollision(self.apple.pos_x, self.apple.pos_y, self.player.x[0], self.player.y[0], 25):
			self.apple.pos_x = r(15, self.screen_width - 25)		
			self.apple.pos_y = r(15, self.screen_height - 25)
			self.player.length += 1		
				
		if self.player.x[0] + 20 >= self.screen_width or self.player.x[0] + 0 <= 0:
			#print('YOU DIED. Score: ' + str(self.player.length - 1))
			self.restart()
			
			exit()

		if self.player.y[0] + 20 >= self.screen_height or self.player.y[0] + 0 <= 0:
			#print('YOU DIED. Score: ' + str(self.player.length - 1))
			self.restart()
		
			exit()

	def restart(self):
		py.time.delay(300)
			#self.window = py.display.set_mode((self.screen_width, self.screen_height))
		self.window.fill((0,0,0))

			#self.image = py.image.load('block1.jpg').convert()
			
			#Y
		self.dr(80, 58)
		self.dr (80, 86)
		self.dr (80, 114)
		self.dr (107, 133)
		self.dr (135, 133)

		self.dr (162, 114)
		self.dr (162, 58)
		self.dr (162, 86)
		self.dr (162, 142)
		self.dr (162, 170)

		self.dr (161, 198)
		self.dr (134, 216)
		self.dr (106, 216)
		self.dr (80, 198)
		py.display.update()


		#O
		self.dr (232, 75)
		self.dr (232, 103)
		self.dr (232, 131)
		self.dr (232, 159)
		self.dr (232, 187)

		self.dr (260, 58)
		self.dr (288, 58)

		self.dr (316, 75)
		self.dr (316, 103)
		self.dr (316, 131)
		self.dr (316, 160)
		self.dr (316, 187)

		self.dr (288, 206)
		self.dr (260, 206)
		py.display.update()


		#U
		self.dr (386, 60)
		self.dr (386, 90)
		self.dr (386, 120)
		self.dr (386, 150)
		self.dr (386, 180)

		self.dr (470, 60)
		self.dr (470, 90)
		self.dr (470, 120)
		self.dr (470, 150)
		self.dr (470, 180)

		self.dr (442, 208)
		self.dr (414, 208)
		py.display.update()


		#L
		self.dr (80, 300)
		self.dr (80, 330)
		self.dr (80, 360)
		self.dr (80, 390)
		self.dr (80, 420)

		self.dr (80, 450)
		self.dr (107, 450)
		self.dr (134, 450)
		self.dr (161, 450)
		py.display.update()


		#O
		self.dr (220, 319)
		self.dr (220, 347)
		self.dr (220, 375)
		self.dr (220, 403)
		self.dr (220, 431)

		self.dr (248, 300)
		self.dr (276, 300)

		self.dr (304, 319)
		self.dr (304, 347)
		self.dr (304, 375)
		self.dr (304, 403)
		self.dr (304, 431)

		self.dr (248, 450)
		self.dr (276, 450)
		py.display.update()


		#S
		self.dr (354, 319)
		self.dr (380, 300)
		self.dr (406, 300)
		self.dr (432, 319)
		self.dr (354, 345)
		self.dr (380, 365)
		self.dr (405, 390)
		self.dr (431, 409)
		self.dr (431, 435)
		self.dr (405, 454)
		self.dr (379, 454)
		self.dr (353, 435)
		py.display.update()


		#E
		self.dr (482, 300)
		self.dr (482, 326)
		self.dr (482, 352)
		self.dr (482, 378)
		self.dr (482, 404)
		self.dr (482, 430)
		self.dr (482, 456)
		
		self.dr (508, 300)
		self.dr (534, 300)
		#self.dr (560, 300)
		
		self.dr (508, 378)
		self.dr (534, 378)
		#self.dr (560, 378)
		
		self.dr (508, 456)
		self.dr (534, 456)
		#self.dr (560, 454)

		Player.x = [1]
		Player.y = [1]
		self.player = Player()
		self.apple = Apple(5, 5)
		self.on_execute()
		exit()
	
	def on_execute(self):
		#self.player = Player()

		self.window = py.display.set_mode((self.screen_width, self.screen_height), py.RESIZABLE)
		self.window.fill((0,0,0))
		
		self.food = py.image.load('block2.jpg').convert()
		self.image = py.image.load('block1.jpg').convert()
		
		clock = py.time.Clock()
		
		py.event.pump() 
		
		while 1:
			
			keys = py.key.get_pressed()
		
			self.window.fill((0, 0, 0))

			for e in py.event.get():
				if e.type == QUIT:
					py.quit()
					exit()

		
			self.player.update()

			if keys[py.K_RIGHT]: 
				self.player.moveRight()
				
			if keys[py.K_LEFT]: 
				self.player.moveLeft()
								
			if keys[py.K_DOWN]: 
				self.player.moveDown()
			
			if keys[py.K_ESCAPE]:
				py.time.wait(1000)	
					
			if keys[py.K_UP]:
				self.player.moveUp()
	
			self.on_render()
			
			self.on_loop()
					
			clock.tick(55)				

if __name__ == '__main__':
	theApp = App()
	theApp.on_execute()	

