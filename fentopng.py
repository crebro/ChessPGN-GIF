from typing import ItemsView
import chess
from PIL import Image

class PositionToImage:
    def __init__(self, board : chess.Board) -> None:
        self.board = str(board).split("\n")
        self.background = Image.open("resources/board.png")
        self.bgWidth, self.bgHeight = self.background.size
        self.itemSize = self.bgWidth // 8
        self.images = {
            "r": self.loadImage("resources/br.png"),
            "q": self.loadImage("resources/bq.png"),
            "k": self.loadImage("resources/bk.png"),
            "n": self.loadImage("resources/bn.png"),
            "b": self.loadImage("resources/bb.png"),
            "p": self.loadImage("resources/bp.png"),
            "P": self.loadImage("resources/wp.png"),
            "Q": self.loadImage("resources/wq.png"),
            "K": self.loadImage("resources/wk.png"),
            "R": self.loadImage("resources/wr.png"),
            "B": self.loadImage("resources/wb.png"),
            "N": self.loadImage("resources/wn.png"),
        }

    def loadImage(self, location):
        image =  Image.open(location).resize( (self.itemSize, self.itemSize) ).convert('RGBA')
        return image

    def convert(self,):
        for rowI, row in enumerate(self.board):
            for colI, item in enumerate(''.join(row.split())):
                if item == ".":
                    continue
                image = self.images[item]
                imageWidth, imageHeight = image.size
                self.background.paste(image, ( (colI) * imageWidth, (rowI) * imageHeight   ), image )
        return self.background
