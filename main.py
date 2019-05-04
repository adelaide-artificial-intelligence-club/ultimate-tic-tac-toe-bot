#!/usr/bin/env python3

import sys, random, logging
from util import *
from board_logger import log_board

class Bot:
    def __init__(self):
        self.name = ''

    def doMove(self, state):
        if not self.name:
            self.name = state.getMyName()
            logging.basicConfig(filename=self.name + '.log', level=logging.DEBUG)

        field = state.getField()
        moves = field.getAvailableMoves()
        log_board(field)

        if len(moves):
            return random.choice(moves)

if __name__ == '__main__':
    bot = Bot()
    parser = BotParser(bot)
    parser.run()
