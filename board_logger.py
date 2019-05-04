import logging

board_logger = logging.getLogger('test')
board_logger.setLevel('DEBUG')
board_filehandler = logging.FileHandler('board.log')
board_filehandler.setLevel('DEBUG')
board_logger.addHandler(board_filehandler)

def log_board(field):
    board_logger.debug('')
    for n, row in enumerate(field._Field__mBoard):
        if n:
            if n % 3:
                s = 3*'-'+'+'+3*'-'+'+'+3*'-'
                board_logger.debug('  '+s+'‖'+s+'‖'+s)
            else:
                board_logger.debug('  '+11*'='+'#'+11*'='+'#'+11*'=')
        row = ' ‖ '.join((' | '.join(row[0:3]),' | '.join(row[3:6]),' | '.join(row[6:9])))
        board_logger.debug('   ' + row.replace('0','O').replace('1','X') + ' ')
