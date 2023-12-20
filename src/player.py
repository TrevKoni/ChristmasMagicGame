import pygame


class Player:
    def __init__(self, x=100, y=100, width=50, height=50, speed=5):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (255, 0, 0)
        self.speed = speed

    def update(self):
        # Player Movement and Actions
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.rect.y -= self.speed
        if keys[pygame.K_s]:
            self.rect.y += self.speed
        if keys[pygame.K_a]:
            self.rect.x -= self.speed
        if keys[pygame.K_d]:
            self.rect.x += self.speed

    def draw(self, screen):
        # Draw the player character on screen
        pygame.draw.rect(screen, self.color, self.rect)

