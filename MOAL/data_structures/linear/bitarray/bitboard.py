# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
from MOAL.helpers.display import print_h3
from MOAL.computer_organization.bit_field import BitField

DEBUG = True if __name__ == '__main__' else False


class ChessPieceBitBoard(BitField):
    """According to Wikipedia, bitfield and bitboard can be used
    interchangeably in terms of structure, so we'll use our previous
    implementation of a bitfield here."""
    def __init__(self):
        self.cols = list('abcdefgh')
        self.rows = range(1, 8)
        super(ChessPieceBitBoard, self).__init__()
        self._populate_fields()

    def __str__(self):
        print('COLS: {}\nROWS: {}'.format(self.cols, self.rows))
        return ''

    def _populate_fields(self):
        """Populates the bitfield with corresponding values for rows/columns.
        See upload.wikimedia.org
            /wikipedia/commons/thumb/b/b6
            /SCD_algebraic_notation.svg/242px-SCD_algebraic_notation.svg.png
        For an example of the coordinate system in chess.
        """
        for col in self.cols:
            for row in self.rows:
                # Use overloaded __setitem__, which sets the bit field bit value
                self['{}{}'.format(col, row)] = False


class ChessBoard:

    def __init__(self):
        self.winner = None
        self.white = {'position': 0, 'captures': 0}
        self.black = {'position': 0, 'captures': 0}
        # Each piece has its own board:
        self.boards = {}
        pieces = (
            (1, 'king'),
            (1, 'queen'),
            (2, 'rook'),
            (2, 'bishop'),
            (2, 'knight'),
            (8, 'pawn'),
        )
        for num_pieces, piece_name in pieces:
            self[piece_name] = num_pieces

    def __str__(self):
        for name, board in self.boards.iteritems():
            print('Board name: [{}], {}'.format(name, ''))
        return ''

    def __setitem__(self, piece_name, num_pieces):
        if num_pieces > 1:
            for index in range(num_pieces):
                self.boards['{}_{}'.format(
                    piece_name, index)] = ChessPieceBitBoard()
        else:
            self.boards[piece_name] = ChessPieceBitBoard()

    def __getitem__(self, piece):
        return self.boards[piece]

    def move(self, piece, player, old_position, new_position):
        print('Moving {} piece `{}` from {} to {}'.format(
            player, piece, old_position, new_position))
        # Set old position to inactive in bitarray
        self.boards[piece][old_position] = False
        # Set new position to active in bitarray
        self.boards[piece][new_position] = True


if DEBUG:
    with Section('BitBoards'):
        print_h3('Chess bit board')
        chess_board = ChessBoard()
        # A rather... fast game. from: chess.about.com
        #   /od/tipsforbeginners/ss/Foolsmate.htm#step-heading
        moves = (
            ('pawn_6', 'white', 'f2', 'f3'),
            ('pawn_5', 'black', 'e6', 'e5'),
            ('pawn_7', 'white', 'g2', 'g4'),
            ('queen', 'black', 'd8', 'h4'),  # checkmate!
        )
        for info in moves:
            piece, player, old, new = info
            chess_board.move(piece, player, old, new)

        print(chess_board['king'])
        print(chess_board)
