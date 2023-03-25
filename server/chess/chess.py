import piece as piece

def update_str(string, value, index):
    return string[:index] + value + string[index + 1:]

class Chess:
    def __init__(self, state):
        self.state = state
        self.state_dict = self.state.to_dict()

    def move(self, fromIndex, toIndex):
        piece_name = self.state_dict['pieces'][fromIndex]
        piece_color = self.state_dict['colors'][fromIndex]

        # check for king in check
        king_piece_indexes = [index for (index, char) in enumerate(self.state_dict['pieces']) if char == 'K']
        if self.state_dict['colors'][king_piece_indexes[0]] == piece_color:
            king_index = king_piece_indexes[0]
        else:
            king_index = king_piece_indexes[1]    
        
        if piece_name == 'K':
            king_index = toIndex

        # print(king_index)
        
        def update_state():
            self.state_dict['pieces'] = update_str(self.state_dict['pieces'], 'E', fromIndex)
            self.state_dict['colors'] = update_str(self.state_dict['colors'], 'E', fromIndex)
            self.state_dict['pieces']  = update_str(self.state_dict['pieces'], piece_name, toIndex)
            self.state_dict['colors'] = update_str(self.state_dict['colors'], piece_color, toIndex)
            self.state_dict['whites_turn'] = not self.state_dict['whites_turn']
            self.state_dict['fromIndex'] = fromIndex
            self.state_dict['toIndex'] = toIndex

            # castling
            if piece_name == 'K':
                if piece_color == 'W':
                    self.state_dict['white_can_castle_short'] = False
                    self.state_dict['white_can_castle_long'] = False
                elif piece_color == 'B':
                    self.state_dict['black_can_castle_short'] = False
                    self.state_dict['black_can_castle_long'] = False        

            if piece_name == 'R':
                if fromIndex == 56:
                    self.state_dict['white_can_castle_long'] = False
                elif fromIndex == 63:
                    self.state_dict['white_can_castle_short'] = False
                elif fromIndex == 0:
                    self.state_dict['black_can_castle_long'] = False
                elif fromIndex == 7:
                    self.state_dict['black_can_castle_short'] = False

            if piece_name == 'K' and piece_color == 'W' and fromIndex == 60 and toIndex == 62:
                self.state_dict['pieces'] = update_str(self.state_dict['pieces'], 'E', 63)
                self.state_dict['colors'] = update_str(self.state_dict['colors'], 'E', 63)
                self.state_dict['pieces'] = update_str(self.state_dict['pieces'], 'R', 61)
                self.state_dict['colors'] = update_str(self.state_dict['colors'], 'W', 61)

            if piece_name == 'K' and piece_color == 'W' and fromIndex == 60 and toIndex == 58:
                self.state_dict['pieces'] = update_str(self.state_dict['pieces'], 'E', 56)
                self.state_dict['colors'] = update_str(self.state_dict['colors'], 'E', 56)
                self.state_dict['pieces'] = update_str(self.state_dict['pieces'], 'R', 59)
                self.state_dict['colors'] = update_str(self.state_dict['colors'], 'W', 59)

            if piece_name == 'K' and piece_color == 'B' and fromIndex == 4 and toIndex == 6:
                self.state_dict['pieces'] = update_str(self.state_dict['pieces'], 'E', 7)
                self.state_dict['colors'] = update_str(self.state_dict['colors'], 'E', 7)
                self.state_dict['pieces'] = update_str(self.state_dict['pieces'], 'R', 5)
                self.state_dict['colors'] = update_str(self.state_dict['colors'], 'B', 5)

            if piece_name == 'K' and piece_color == 'B' and fromIndex == 4 and toIndex == 2:
                self.state_dict['pieces'] = update_str(self.state_dict['pieces'], 'E', 0)
                self.state_dict['colors'] = update_str(self.state_dict['colors'], 'E', 0)
                self.state_dict['pieces'] = update_str(self.state_dict['pieces'], 'R', 3)
                self.state_dict['colors'] = update_str(self.state_dict['colors'], 'B', 3)

   

        # check user selected their own piece
        this_turns_color = 'W' if self.state_dict['whites_turn'] else 'B'
        this_turns_positions = [i for i, color in enumerate(self.state_dict['colors']) if color == this_turns_color]
        if fromIndex not in this_turns_positions:
            return self.state_dict
        
        # pawn
        if piece_name == 'P':
            selected_piece = piece.Pawn(piece_color, fromIndex, self.state_dict)
            if selected_piece.check_move(toIndex):
                update_state()
            return self.state_dict

        # knight (horse)
        if piece_name == 'H':
            selected_piece = piece.Knight(piece_color, fromIndex, self.state_dict)
            if selected_piece.check_move(toIndex):
                update_state()
            return self.state_dict
        
        # bishop
        if piece_name == 'B':
            selected_piece = piece.Bishop(piece_color, fromIndex, self.state_dict)
            if selected_piece.check_move(toIndex):
                update_state()
            return self.state_dict

        # rook
        if piece_name == 'R':
            selected_piece = piece.Rook(piece_color, fromIndex, self.state_dict)
            if selected_piece.check_move(toIndex):
                update_state()
            return self.state_dict
    
        # queen
        if piece_name == 'Q':
            selected_piece = piece.Queen(piece_color, fromIndex, self.state_dict)
            if selected_piece.check_move(toIndex):
                update_state()
            return self.state_dict
        
        # king
        if piece_name == 'K':
            selected_piece = piece.King(piece_color, fromIndex, self.state_dict)
            if selected_piece.check_move(toIndex):
                update_state()
            return self.state_dict

                