import chess.pgn
import chess.svg
from fentopng import PositionToImage
import glob

class Converter:
    def __init__(self, filename) -> None:
        self.file = open(filename)
        self.game = chess.pgn.read_game(self.file) 
        self.board = self.game.board()

    def convertAllPositions(self):
        images = []
        for move in self.game.mainline_moves():
            self.board.push(move)
            converter = PositionToImage(self.board)
            images.append(converter.convert())
        images[0].save("converted.gif", format="GIF", append_images=images[1:], save_all=True, duration=1000, loop=0)

if __name__ == "__main__":
    converter = Converter("game.pgn")
    converter.convertAllPositions()
