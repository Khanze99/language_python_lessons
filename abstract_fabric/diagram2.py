

class DiagramFactory:

    @classmethod
    def make_diagram(cls, width, height):
        return cls.Diagram(width, height)

    @classmethod
    def make_rectangle(cls, x, y, width, height, fill="white", stroke="black"):
        return cls.Rectangle(x, y, width, height, fill, stroke)

    @classmethod
    def make_text(cls, x, y, text, fontsize=12):
        return cls.Text(x, y, text, fontsize)

    class Diagram:
        def __init__(self, width, height):
            self.diagram = []
            for y in range(width):
                self.diagram.append([])
                for x in range(height):
                    if (y == 0 and x == 0) or (y == width - 1 and x == height - 1) or (y == width - 1 and x == 0) or (
                            y == 0 and x == height - 1):
                        self.diagram[y].append('+')
                    elif (y == 0 or y == width - 1) and (0 < x < height - 1):
                        self.diagram[y].append('-')
                    elif (x == 0 or x == height - 1) and (0 < y < width - 1):
                        self.diagram[y].append('|')
                    else:
                        self.diagram[y].append("%")

        def add(self, component):
            for y, row in enumerate(component.rows):
                for x, char in enumerate(row):
                    self.diagram[y + component.y][x + component.x] = char
