from io import StringIO

class StringReader:
    def __init__(self, content):
        self.content = content

    def read(self, filename=None):
        edges = []

        stream = StringIO(self.content)

        for line in stream:
            line = line.strip()

            if not line or line.startswith("#"): continue
            parts = line.split()
            if len(parts) != 2:
                raise ValueError(f"Некорректная строка в файле: {line}")

            u,v = map(int, parts)
            edges.append((u,v))

        return edges

class StringWriter:
    def __init__(self):
        self.stream = StringIO()

        def write(self, filename, matrix):
            for row in matrix:
                self.stream.write(" ".join(map(int, row)) + "\n")

        def getValue(self):
            return self.stream.getValue()