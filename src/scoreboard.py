#scoreboard file
#author ntn
import pygame

class Scoreboard:

    def __init__(self,screen, initial_score=0):
        self.score = initial_score
        self.font = pygame.font.SysFont(None,48)
        self.screen = screen
        self.left_score = initial_score
        self.right_score = initial_score

    def increment_score(self, player):
        if player == "playerOne":
            self.left_score += 1
        elif player == "playerTwo":
            self.right_score += 1

    def update_score(self,left_score, right_score):
        self.left_score = left_score
        self.right_score = right_score

    def render(self):
        score_text = self.font.render(f"{self.left_score} - {self.right_score}",True, (255,255,255))

        score_x = (self.screen.get_width() - score_text.get_width()) // 2
        score_y = 10

        buffer = 10
        background_rect = pygame.Rect(score_x - buffer, score_y - buffer, score_text.get_width() + 2*buffer, score_text.get_height() + 2*buffer)
        self.screen.fill((0,0,0),background_rect)

        self.screen.blit(score_text, (score_x, score_y))