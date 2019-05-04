#!/usr/bin/env python3

import sys, random, logging
from util import *

class Bot:
    def __init__(self):
        self.name = ''

    def doMove(self, state):
        if not self.name:
            self.name = state.getMyName()
            logging.basicConfig(filename=self.name + '.log', level=logging.INFO)

        moves = state.getField().getAvailableMoves()
        if (len(moves) > 0):
            return moves[random.randrange(len(moves))]
        else:
            return None

if __name__ == '__main__':
    bot = Bot()
    parser = BotParser(bot)
    parser.run()
