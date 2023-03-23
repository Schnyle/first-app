def pos_to_cart(position):
    row = int(position / 8)
    col = position % 8
    return [row, col]