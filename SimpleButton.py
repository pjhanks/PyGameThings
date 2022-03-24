# SimpleButton Class
#
# Uses a state machine approach

import pygame
from pygame.locals import *

class SimpleButton():
    # Used to track the state of the button
    STATE_IDLE = 'idle' # button up, mouse not over button
    STATE_ARMED = 'armed' # button is down, mouse is over button
    STATE_DISARMED = 'disarmed' # clicked down on button, rolled off

    def __init__(self, window, loc, up, down):
        self.window = window
        self.loc = loc
        self.surfaceUp = pygame.image.load(up)
        self.surfaceDown = pygame.image.load(down)

        # Get the rect of the button
        self.rect = self.surfaceUp.get_rect()
        self.rect[0] = loc[0]
        self.rect[1] = loc[1]

        self.state = SimpleButton.STATE_IDLE

    def handleEvent(self, eventObj):
        # Returns True iff user clicks the button
        # Normally returns false

        if eventObj.type not in (MOUSEMOTION, MOUSEBUTTONDOWN, MOUSEBUTTONUP):
            return False

        eventPointInButtonRect = self.rect.collidepoint(eventObj.pos)

        if self.state == SimpleButton.STATE_IDLE:
            if (eventObj.type == MOUSEBUTTONDOWN) and eventPointInButtonRect:
                self.state = SimpleButton.STATE_ARMED

            elif self.state == SimpleButton.STATE_ARMED:
                if (eventObj.type == MOUSEBUTTONUP) and eventPointInButtonRect:
                    self.state = SimpleButton.STATE_IDLE
                    return True

                if (eventObj.type == MOUSEMOTION) and (not eventPointInButtonRect):
                    self.state = SimpleButton.STATE_DISARMED

            elif self.state == SimpleButton.STATE_DISARMED:
                if eventPointInButtonRect:
                    self.state = SimpleButton.STATE_ARMED
                elif eventObj.type == MOUSEBUTTONUP:
                    self.state = SimpleButton.STATE_IDLE

            return False

    def draw(self):
        if self.state == SimpleButton.STATE_ARMED:
            self.window.blit(self.surfaceDown, self.loc)

        else:
            self.window.blit(self.surfaceUp, self.loc)