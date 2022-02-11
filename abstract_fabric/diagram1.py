
SVG_TEXT = """<text x="{x}" y="{y} text-anchor="left" font-family="sans-serif" font-size="{fontsize}">{text}</text>"""
SVG_SCALE = 20


class SvgText:
    def __init__(self, x, y, text, fontsize):
        x *= SVG_SCALE
        y *= SVG_SCALE
        fontsize *= SVG_SCALE // 10
        self.svg = SVG_TEXT.format(**locals())


class Text:
    def __init__(self, x, y, text, fontsize):
        self.x = x
        self.y = y
        self.rows = [list(text)]


class SvgDiagram:
    def __init__(self): pass  # TODO ?

    def add(self, component):
        self.diagram.appeng(component.svg)


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


class DiagramFactory:

    def make_diagram(self, width, height):
        return Diagram(width, height)

    def make_rectangle(self, x, y, width, height, fill="white", stroke="black"):
        return Rectangle(x, y, width, height, fill, stroke)

    def make_text(self, x, y, text, fontsize=12):
        return Text(x, y, text, fontsize)


class SvgDiagramFactory:

    def make_diagram(self, width, height):
        return SvgDiagram(width, height)

    def make_rectangle(self, x, y, width, height, fill="white", stroke="black"):
        return SvgRectangle(x, y, width, height, fill, stroke)

    def make_text(self, x, y, text, fontsize=12):
        return SvgText(x, y, text, fontsize)


def create_diagram(factory):
    diagram = factory.make_diagram(30, 7)
    rectangle = factory.make_rectangle(4, 1, 22, 5, "yellow")
    text = factory.make_text(7, 3, "Abstract Factory")
    diagram.add(rectangle)
    diagram.add(text)
    return diagram


def main():
    txtDiagram = create_diagram(DiagramFactory())
    txtDiagram.save(textFilename)

    svgDiagram = create_diagram(SvgDiagramFactory())
    svgDiagram.save(svgFilename)