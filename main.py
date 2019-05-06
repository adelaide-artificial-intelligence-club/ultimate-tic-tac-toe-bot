#!/usr/bin/env python3

import sys, random, logging
from util import *

def log_board(field, indent='  '):
    logging.debug('')
    for n, row in enumerate(field._Field__mBoard):
        if n:
            if n % 3:
                sep = '---+---+---'
                logging.debug(indent + sep + '‖' + sep + '‖' + sep)
            else:
                sep = '==========='
                logging.debug(indent + sep + '#' + sep + '#' + sep)
        row = ' ‖ '.join(' | '.join(row[i:i+3]) for i in range(0, len(row), 3))
        logging.debug(indent + ' ' + row.replace('0','O').replace('1','X'))
    logging.debug('')

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
            move = random.choice(moves)
            logging.info((move.getX(), move.getY()))
            return move

if __name__ == '__main__':
    bot = Bot()
    parser = BotParser(bot)
    parser.run()
