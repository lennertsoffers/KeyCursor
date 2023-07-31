from PyQt5.QtCore import QFile, QTextStream, QIODevice


class StyleLoader:
    def __init__(self, variables_path: str = None):
        self._variables = {}
        self._stylesheets = {}

        self._init_variables(variables_path)

    def get_merged_stylesheets(self, names: list):
        return self._merge_stylesheets([self.get_stylesheet(name=name) for name in names])

    def get_stylesheet(self, name: str) -> str:
        stylesheet = self._stylesheets.get(name)

        if stylesheet is None:
            stylesheet = self._create_stylesheet(name)
            self._stylesheets[name] = stylesheet

        return stylesheet

    def _merge_stylesheets(self, stylesheets: list) -> str:
        return "\n".join(stylesheets)

    def _create_stylesheet(self, path: str) -> str:
        stylesheet = self._load_unmapped_stylesheet(path)
        return self._map_stylesheet(stylesheet)

    def _load_unmapped_stylesheet(self, path: str) -> str:
        file = QFile(path)
        if not file.open(QIODevice.ReadOnly | QIODevice.Text):
            return ""

        content = file.readAll().data().decode("utf-8")
        file.close()

        return content

    def _map_stylesheet(self, stylesheet: str) -> str:
        for variable_name, variable_value in self._variables.items():
            stylesheet = stylesheet.replace(variable_name, variable_value)

        return stylesheet

    def _init_variables(self, path: str) -> None:
        if path is None:
            return

        file = QFile(path)
        if not file.open(QIODevice.ReadOnly | QIODevice.Text):
            return

        stream = QTextStream(file)

        while not stream.atEnd():
            line = stream.readLine().strip().replace(" ", "")
            if line.startswith("@"):
                variable_name, variable_value = line.split("=", 1)
                self._variables[variable_name] = variable_value

        file.close()
