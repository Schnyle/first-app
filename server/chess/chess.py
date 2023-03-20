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
                print(piece_name)
                if piece_color == 'W':
                    print(piece_color)
                    self.state_dict['white_can_castle_short'] = False
                    self.state_dict['white_can_castle_long'] = False
                elif piece_color == 'B':
                    print(piece_color)
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


        # check user selected their own piece
        this_turns_color = 'W' if self.state_dict['whites_turn'] else 'B'
        this_turns_positions = [i for i, color in enumerate(self.state_dict['colors']) if color == this_turns_color]
        if fromIndex not in this_turns_positions:
            return self.state_dict
        
        if piece_name == 'P':
            selected_piece = piece.Pawn(piece_color, fromIndex, self.state_dict['colors'])
            if selected_piece.check_move(toIndex):
                update_state()
            return self.state_dict

            
        if piece_name == 'H':
            selected_piece = piece.Knight(piece_color, fromIndex, self.state_dict['colors'])
            if selected_piece.check_move(toIndex):
                update_state()
            return self.state_dict
        
        if piece_name == 'B':
            selected_piece = piece.Bishop(piece_color, fromIndex, self.state_dict['colors'])
            if selected_piece.check_move(toIndex):
                update_state()
            return self.state_dict

        if piece_name == 'R':
            selected_piece = piece.Rook(piece_color, fromIndex, self.state_dict['colors'])
            if selected_piece.check_move(toIndex):
                update_state()
            return self.state_dict
    
        if piece_name == 'Q':
            selected_piece = piece.Queen(piece_color, fromIndex, self.state_dict['colors'])
            if selected_piece.check_move(toIndex):
                update_state()
            return self.state_dict
        
        if piece_name == 'K':
            selected_piece = piece.King(piece_color, fromIndex, self.state_dict['colors'])
            if selected_piece.check_move(toIndex):
                update_state()
            return self.state_dict

                