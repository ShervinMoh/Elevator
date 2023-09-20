import pygame
import time

# Initialize Pygame
pygame.init()

# Set the dimensions of the screen
screen_width = 600
screen_height = 600

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Simple Elevator Simulator")

font_style = pygame.font.SysFont("bahnschrift", 20) 

black = (1, 4, 4)

# Game loop
def game_loop():

    # Elevator variables
    elevator_x = 250
    elevator_y = 470

    target_floors = []  # List to store the target floors
    elevator_speed = 1  # Speed at which the elevator moves

    last_floor_time = time.time()  # Initialize last floor time

    running = True
    while running:

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    target_floors.append(470)  # Add floor A as a target
                elif event.key == pygame.K_b:
                    target_floors.append(320)  # Add floor B as a target
                elif event.key == pygame.K_c:
                    target_floors.append(170)  # Add floor C as a target
                elif event.key == pygame.K_d:
                    target_floors.append(20)   # Add floor D as a target

        if target_floors and elevator_y < target_floors[0]:
            elevator_y += elevator_speed  # Move elevator up
        elif target_floors and elevator_y > target_floors[0]:
            elevator_y -= elevator_speed  # Move elevator down
        elif target_floors:
            current_time = time.time()  # Get current time
            if current_time - last_floor_time >= 5:  # Wait for 3 seconds
                if len(target_floors) > 1:
                    del target_floors[0]  # Remove the current floor from the targets
                last_floor_time = current_time  # Update last floor time

        # Fill the screen with a color
        screen.fill((153, 255, 204))  # Light green color

        # Floors
        pygame.draw.rect(screen, (128, 128, 128), pygame.Rect(250, 120, 100, 10))  # Floor D
        d_floor = font_style.render("Press D", True, black)
        screen.blit(d_floor, [170, 115])

        pygame.draw.rect(screen, (128, 128, 128), pygame.Rect(250, 270, 100, 10))  # Floor C
        c_floor = font_style.render("Press C", True, black)
        screen.blit(c_floor, [170, 265])

        pygame.draw.rect(screen, (128, 128, 128), pygame.Rect(250, 420, 100, 10))  # Floor B
        b_floor = font_style.render("Press B", True, black)
        screen.blit(b_floor, [170, 415])

        pygame.draw.rect(screen, (128, 128, 128), pygame.Rect(250, 570, 100, 10))  # Floor A
        a_floor = font_style.render("Press A", True, black)
        screen.blit(a_floor, [170, 565])


        # Elevator
        pygame.draw.rect(screen, (255, 255, 153), pygame.Rect(elevator_x, elevator_y, 100, 100))

        # Update the screen
        pygame.display.flip()

        # Add a small delay to control the speed of the elevator
        pygame.time.delay(10)

    # Quit Pygame
    pygame.quit()


if __name__ == '__main__':
    game_loop()