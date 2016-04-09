import pygame
import time

# Initilizes pygame, display and clock
pygame.mixer.pre_init(44100,16,2,4096)
pygame.init()
game_display = pygame.display.set_mode((600,200))
pygame.display.set_caption("River Crossing")
clock = pygame.time.Clock()

# Loads all images
man_img = pygame.image.load("man.png")
fox_img = pygame.image.load("fox.png")
chicken_img = pygame.image.load("chicken.png")
grain_img = pygame.image.load("grain.png")
gameover_img = pygame.image.load("gameover.png")
youwon_img = pygame.image.load("youwon.png")
wave1 = pygame.image.load("wave1.png")
log = pygame.image.load("log.png")
background_img = pygame.image.load("background.png")
playagain_img = pygame.image.load("playagain.png")
rock = pygame.image.load("rock.png")
rock2 = pygame.image.load("rock2.png")
pause = pygame.image.load("pause.png")
controls = pygame.image.load("controls.png")
frontsea = pygame.image.load("frontsea.png")
pausebackground = pygame.image.load("pausebackground.png")
gameoverbackground = pygame.image.load("gameoverbackground.png")
startscreen = pygame.image.load("startscreen.png")

playagain = True
	
# Updates all image coordinates
def update_image(manx, many, foxx, foxy, grainx, grainy, chickenx, chickeny, boatx, boaty, wave1y, wave2y, paused):
	game_display.blit(background_img, (0,0))
	game_display.blit(wave1, (150, wave1y))
	game_display.blit(rock, (0, 145))
	game_display.blit(rock2, (440, 145))
	game_display.blit(log, (boatx, boaty))
	game_display.blit(frontsea, (0,wave2y))
	game_display.blit(man_img, (manx, many))
	game_display.blit(fox_img, (foxx, foxy))
	game_display.blit(grain_img, (grainx, grainy))
	game_display.blit(chicken_img, (chickenx, chickeny))
	game_display.blit(pause, (3,3))
	
	if paused:
		game_display.blit(pausebackground, (0,0))
		game_display.blit(controls, (0,5))

# Game loop
def gameloop():
	pygame.mixer.music.load("sang.mp3")
	pygame.mixer.music.set_volume(0.1)
	pygame.mixer.music.play(-1)
	
	# Where to place item in boat
	item_loaded_left_x = 187
	item_loaded_right_x = 395
	
	# Gives all moving objects start values
	bird_x = 0
	bird_y = 0
	bird_x_dir = 0.4
	
	wave1_y = 180
	wave2_y = 180
	wave1_y_dir = 0.07
	wave2_y_dir = -0.07

	boat_x = 157
	boat_y = 160
	boat_y_dir = -0.05
	boat_x_dir = 0
	boat_is_left = True

	man_leftside_x = -12
	man_rightside_x = 438
	man_x = man_leftside_x
	man_y = 110
	man_x_dir = 0
	man_y_dir = 0
	man_loaded = False
	man_is_left = True

	fox_leftside_x = 22
	fox_rightside_x = 468
	fox_x = fox_leftside_x
	fox_y = 130
	fox_x_dir = 0
	fox_y_dir = 0
	fox_loaded = False
	fox_is_left = True
	fox_ate_chicken = False

	grain_leftside_x = 60
	grain_rightside_x = 507
	grain_x = grain_leftside_x
	grain_y = 143
	grain_x_dir = 0
	grain_y_dir = 0
	grain_loaded = False
	grain_is_left = True

	chicken_leftside_x = 88	
	chicken_rightside_x = 529
	chicken_x = chicken_leftside_x
	chicken_y = 145
	chicken_x_dir = 0
	chicken_y_dir = 0
	chicken_loaded = False
	chicken_is_left = True
	chicken_ate_grain = False

	player_lose = False
	player_win = False
	
	paused = False	
	playing = True
	global playagain

	while playing:
		
		# Checks if user loses
		if man_loaded:
			if (chicken_is_left and grain_is_left) or (chicken_is_left == False and grain_is_left == False):
				if chicken_loaded == False and grain_loaded == False:
					chicken_ate_grain = True
					player_lose = True
				
			if (chicken_is_left and fox_is_left) or (chicken_is_left == False and fox_is_left == False):
				if chicken_loaded == False and fox_loaded == False:
					fox_ate_chicken = True
					player_lose = True
		
		# Checks if user wins
		if man_is_left == False and fox_is_left == False and grain_is_left == False and chicken_is_left == False:
			if man_loaded == False and fox_loaded == False and grain_loaded == False and chicken_loaded == False:
				player_win = True	
				
		# If user loses: quit or play again
		if player_lose:
			choosing = True	
			pygame.mixer.music.load("gameover.mp3")
			pygame.mixer.music.set_volume(3)
			pygame.mixer.music.play(1)
			
			game_display.blit(gameoverbackground, (0,0))
			game_display.blit(gameover_img, (-3,10))
			game_display.blit(playagain_img, (0,0))
			pygame.display.update()
			
			while choosing:				
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						playagain = False
						playing = False
						choosing = False
					
					elif event.type == pygame.KEYDOWN:
						if event.key == pygame.K_RETURN:
							playagain = True
							playing = False
							choosing = False
							
						elif event.key == pygame.K_ESCAPE:
							playagain = False
							playing = False
							choosing = False
		
		# If user wins: quit or play again
		if player_win:
			choosing = True	
			pygame.mixer.music.load("winningsound.mp3")
			pygame.mixer.music.set_volume(0.3)
			pygame.mixer.music.play(1)
			
			game_display.blit(gameoverbackground, (0,0))
			game_display.blit(youwon_img, (0, 0))
			game_display.blit(playagain_img, (0,0))
			pygame.display.update()
		
			while choosing:				
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						playagain = False
						playing = False
						choosing = False
						
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_RETURN:
							playagain = True
							playing = False
							choosing = False
							
						elif event.key == pygame.K_ESCAPE:
							playagain = False
							playing = False
							choosing = False	
			
		# Stops boat and passengers at left bank	
		if boat_x == 157:
			boat_x_dir = 0
			man_x_dir = 0
			fox_x_dir = 0
			grain_x_dir = 0
			chicken_x_dir = 0
			boat_is_left = True
			
		# Stops boat and passengers at right bank
		elif boat_x == 365:
			boat_x_dir = 0
			man_x_dir = 0
			fox_x_dir = 0
			grain_x_dir = 0
			chicken_x_dir = 0
			boat_is_left = False
		
		if playing:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					playing = False
					playagain = False
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						playing = False
						playagain = False
				
				if paused == False:
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_SPACE: # Cross river
							if man_loaded:
								if boat_is_left:
									boat_x_dir = 1
									if man_loaded:
										man_x_dir = 1
									if fox_loaded:
										fox_x_dir = 1
									if grain_loaded:
										grain_x_dir = 1
									if chicken_loaded:
										chicken_x_dir = 1
								else:
									boat_x_dir = -1
									if man_loaded:
										man_x_dir = -1
									if fox_loaded:
										fox_x_dir = -1
									if grain_loaded:
										grain_x_dir = -1
									if chicken_loaded:
										chicken_x_dir = -1		
								
						elif event.key == pygame.K_m: # Load/unload man
							if man_loaded:
								if boat_x_dir == 0:
									if boat_is_left:
										man_x = man_leftside_x
										man_is_left = True
										man_loaded = False
									
									else:
										man_x = man_rightside_x
										man_is_left = False
										man_loaded = False
							else:				
								if boat_is_left:
									if man_is_left:
										man_x = 155
										man_loaded = True
								else:
									if man_is_left == False:
										man_x = 363
										man_loaded = True
										
						elif event.key == pygame.K_f: # Load/unload fox
							if fox_loaded:
								if boat_x_dir == 0:
									if boat_is_left:
										fox_x = fox_leftside_x
										fox_is_left = True
										fox_loaded = False
									else:
										fox_x = fox_rightside_x
										fox_is_left = False
										fox_loaded = False
							else:
								if boat_x_dir == 0:
									if grain_loaded == False and chicken_loaded == False:
										if boat_is_left:
											if fox_is_left:
												fox_x = item_loaded_left_x
												fox_loaded = True
										else:
											if fox_is_left == False:
												fox_x = item_loaded_right_x
												fox_loaded = True
											
						elif event.key == pygame.K_g: # Load/unload grain
							if grain_loaded:
								if boat_x_dir == 0:
									if boat_is_left:
										grain_x = grain_leftside_x
										grain_is_left = True
										grain_loaded = False
									else:
										grain_x = grain_rightside_x
										grain_is_left = False
										grain_loaded = False
							else:
								if boat_x_dir == 0:
									if fox_loaded == False and chicken_loaded == False:
										if boat_is_left:
											if grain_is_left:
												grain_x = item_loaded_left_x
												grain_loaded = True
										else:
											if grain_is_left == False:
												grain_x = item_loaded_right_x
												grain_loaded = True
											
						elif event.key == pygame.K_c: # Load/unload chicken
							if chicken_loaded:
								if boat_x_dir == 0:
									if boat_is_left:
										chicken_x = chicken_leftside_x
										chicken_is_left = True
										chicken_loaded = False
									else:
										chicken_x = chicken_rightside_x
										chicken_is_left = False
										chicken_loaded = False
							else:
								if boat_x_dir == 0:
									if fox_loaded == False and grain_loaded == False:																
										if boat_is_left:
											if chicken_is_left:
												chicken_x = item_loaded_left_x
												chicken_loaded = True
										else:
											if chicken_is_left == False:
												chicken_x = item_loaded_right_x
												chicken_loaded = True
				
				# Pause game				
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_p:
						if paused:
							paused = False						
						else:
							paused = True
		
		# Control wave y-movement					
		if wave1_y >= 182:
			wave1_y_dir = -0.07
		
		if wave1_y <= 178:
			wave1_y_dir = 0.07
		
		if wave2_y >= 182:
			wave2_y_dir = -0.07
		
		if wave2_y <= 178:
			wave2_y_dir = 0.07
		
		# Controll boat y-movement
		if boat_y >= 163:
			boat_y_dir = -0.05	
		
		if boat_y <= 157:
			boat_y_dir = 0.05	
			
		# Control passenger y-movement
		if man_loaded:
			man_y = boat_y - 45
		else:
			man_y_dir = 0
			man_y = 110
			
		if fox_loaded:
			fox_y = boat_y - 25
		else:
			fox_y_dir = 0
			fox_y = 130
			
		if grain_loaded:
			grain_y = boat_y -13
		else:
			grain_y_dir = 0
			grain_y = 143
		
		if chicken_loaded:
			chicken_y = boat_y - 12
		else:
			chicken_y_dir = 0
			chicken_y = 145
		
		# Update coordinates for moving objects							
		man_x += man_x_dir
		fox_x += fox_x_dir
		grain_x += grain_x_dir
		chicken_x += chicken_x_dir
		boat_x += boat_x_dir
		boat_y += boat_y_dir
		wave1_y += wave1_y_dir
		wave2_y += wave2_y_dir
		
		# Update display
		if player_lose == False and player_win == False:
			if paused:
				update_image(man_x, man_y, fox_x, fox_y, grain_x, grain_y, chicken_x, chicken_y, boat_x, boat_y, wave1_y, wave2_y, True)
				pygame.display.update()				
				clock.tick(120)
			else:
				update_image(man_x, man_y, fox_x, fox_y, grain_x, grain_y, chicken_x, chicken_y, boat_x, boat_y, wave1_y, wave2_y, False)
				pygame.display.update()
				clock.tick(120)		

def main():
	starting = True
	running = True
	global playagain

	while running:
		# Show start screen and wait for user to start/exit the game
		while starting == True:
			game_display.blit(startscreen, (0,0))
			pygame.display.update()
			
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					starting = False
					running = False		
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_RETURN:
						starting = False		
					elif event.key == pygame.K_ESCAPE:
						starting = False
						playagain = False
		
		# Run game loop if user wants to play again, exits if not
		if playagain:
			gameloop()
		else:
			running = False
			
if __name__ == "__main__": main()
				

