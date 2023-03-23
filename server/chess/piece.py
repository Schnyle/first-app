def pos_to_cart(position):
    row = int(position / 8)
    col = position % 8
    return [row, col]

def cart_to_pos(row, col):
    return (8 * row) + col

class Piece():
    def __init__(self, color, position, state):
        self.color = color
        self.position = position
        self.state = state
        self.state_colors = state['colors']

    def get_moves():    # place holder
        pass

    def check_move(self, target):
        moves = self.get_moves()
        if not target in moves:
            return False
        return True

class King(Piece):
    def __init__(self, color, position, state):
        super().__init__(color, position, state)

    def get_moves(self):
        [row, col] = pos_to_cart(self.position)
        moves = []

        def check_move(delta_row, delta_col):
            new_row = row + delta_row
            new_col = col + delta_col
            if 0 <= new_row <= 7 and 0 <= new_col <= 7:
                new_position = cart_to_pos(new_row, new_col)
                if self.state_colors[new_position] != self.color:
                    moves.append(new_position)

        check_move(1, 0)
        check_move(0, 1)
        check_move(-1, 0)
        check_move(0, -1)
        check_move(1, 1)
        check_move(-1, 1)
        check_move(1, -1)
        check_move(-1, -1)

        # castling
        short_castle_space = [self.state_colors[61], self.state_colors[62]] == ['E', 'E']
        long_castle_sapce = [self.state_colors[59], self.state_colors[58], self.state_colors[57]] == ['E', 'E', 'E']
        if self.state['white_can_castle_short'] and self.position == 60 and short_castle_space:
            moves.append(62) 
        if self.state['white_can_castle_long'] and self.position == 60 and long_castle_sapce:
            moves.append(58) 

        short_castle_space = [self.state_colors[5], self.state_colors[6]] == ['E', 'E']
        long_castle_sapce = [self.state_colors[3], self.state_colors[2], self.state_colors[1]] == ['E', 'E', 'E']
        if self.state['black_can_castle_short'] and self.position == 4 and short_castle_space:
            moves.append(6) 
        if self.state['black_can_castle_long'] and self.position == 4 and long_castle_sapce:
            moves.append(2) 

        return moves
        

class Queen(Piece):
    def __init__(self, color, position, state):
        super().__init__(color, position, state)

    def get_moves(self):
        moves = Rook.get_moves(self) + Bishop.get_moves(self)
        return moves

class Rook(Piece):
    def __init__(self, color, position, state):
        super().__init__(color, position, state)

    def get_moves(self):
        [row, col] = pos_to_cart(self.position)
        moves = []

        def moves_for_lines(type):
            loop = True
            i = 1
            while loop:
                if type == '+row':
                    new_row = row + i
                    new_col = col
                if type == '-row':
                    new_row = row - i
                    new_col = col
                if type == '+col':
                    new_row = row
                    new_col = col + i
                if type == '-col':
                    new_row = row
                    new_col = col - i

                if 0 <= new_row <= 7 and 0 <= new_col <= 7:
                    temp_position = cart_to_pos(new_row, new_col)
                    if self.state_colors[temp_position] == 'E':
                        moves.append(temp_position)
                    elif self.state_colors[temp_position] == self.color:
                        loop = False
                    else:
                        moves.append(temp_position)
                        loop = False
                else:
                    break
                i += 1
        
        moves_for_lines('+row')
        moves_for_lines('-row')
        moves_for_lines('+col')
        moves_for_lines('-col')

        return moves

class Bishop(Piece):
    def __init__(self, color, position, state):
        super().__init__(color, position, state)

    def get_moves(self):
        [row, col] = pos_to_cart(self.position)
        moves = []

        def moves_for_diag(type):
            loop = True
            i = 1
            while loop:
                if type == '++':
                    new_row = row + i
                    new_col = col + i
                if type == '+-':
                    new_row = row + i
                    new_col = col - i
                if type == '-+':
                    new_row = row - i
                    new_col = col + i
                if type == '--':
                    new_row = row - i
                    new_col = col - i

                if 0 <= new_row <= 7 and 0 <= new_col <= 7:
                    new_position = cart_to_pos(new_row, new_col)
                    if self.state_colors[new_position] == 'E':
                        moves.append(new_position)
                    elif self.state_colors[new_position] == self.color:
                        loop = False
                    else:
                        moves.append(new_position)
                        loop = False
                else:
                    break
                i += 1

        moves_for_diag('++')
        moves_for_diag('+-')
        moves_for_diag('-+')
        moves_for_diag('--')

        return moves

class Knight(Piece):
    def __init__(self, color, position, state):
        super().__init__(color, position, state)

    def get_moves(self):
        [row, col] = pos_to_cart(self.position)
        moves = []

        def check_move(delta_row, delta_col):
            new_row = row + delta_row
            new_col = col + delta_col
            if 0 <= new_row <= 7 and 0 <= new_col <= 7:
                new_position = cart_to_pos(new_row, new_col)
                if self.state_colors[new_position] != self.color:
                    moves.append(new_position)

        check_move(1, 2)
        check_move(-1, 2)
        check_move(1, -2)
        check_move(-1, -2)
        check_move(2, 1)
        check_move(-2, 1)
        check_move(2, -1)
        check_move(-2, -1)

        return moves

class Pawn(Piece):
    def __init__(self, color, position, state):
        super().__init__(color, position, state)
        self.moved = True
        if (7 < position < 16) and self.color == 'B':
            self.moved = False
        if (47 < position < 56) and self.color == 'W':
            self.moved = False

    def get_moves(self):
        [row, col] = pos_to_cart(self.position)
        moves = []
        if self.color == 'W':
            # forward 1
            new_position = cart_to_pos(row - 1, col)
            if self.state_colors[new_position] == 'E':
                moves.append(new_position)
            # forward 2
            if not self.moved:
                new_position = cart_to_pos(row - 2, col)
                if self.state_colors[new_position] == 'E':
                    moves.append(new_position)
            # take
            if col > 0:
                new_position = cart_to_pos(row - 1, col - 1)
                current_square_state = self.state_colors[new_position]
                if current_square_state != 'E' and current_square_state != self.color:
                    moves.append(new_position)
            if col < 7:
                new_position = cart_to_pos(row - 1, col + 1)
                if self.state_colors[new_position] != 'E' and self.state_colors[new_position] != self.color:
                    moves.append(new_position)
            
        if self.color == 'B':
            # forward 1
            new_position = cart_to_pos(row + 1, col)
            if self.state_colors[new_position] == 'E':
                moves.append(new_position)
            # forward 2
            if not self.moved:
                new_position = cart_to_pos(row + 2, col)
                if self.state_colors[new_position] == 'E':
                    moves.append(new_position)
            # take
            if col > 0:
                new_position = cart_to_pos(row + 1, col - 1) 
                current_square_state = self.state_colors[new_position]
                if current_square_state != 'E' and current_square_state != self.color:
                    moves.append(new_position)
            if col < 7:
                new_position = cart_to_pos(row + 1, col + 1) 
                current_square_state = self.state_colors[new_position]
                if current_square_state != 'E' and current_square_state != self.color:
                    moves.append(new_position)

        return moves
