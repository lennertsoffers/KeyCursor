class StyleLoader:
    def __init__(self, variables_path: str=None, stylesheets_path=None):
        self._variables = {}
        self._stylesheets = {}

        self._stylesheets_path = stylesheets_path

        self._init_variables(variables_path)

    def get_merged_stylesheets(self, names: list=None, paths: list=None):
        if paths is None:
            return self._merge_stylesheets([self.get_stylesheet(name=name) for name in names])
        else:
            return self._merge_stylesheets([self.get_stylesheet(path=path) for path in paths])

    def get_stylesheet(self, name: str=None, path: str=None) -> str:
        if path is None:
            if name is not None:
                stylesheet_key = self._get_full_stylesheet_key(name)
            else:
                return ""
        else:
            stylesheet_key = path

        stylesheet = self._stylesheets.get(stylesheet_key)

        if stylesheet is None:
            stylesheet = self._create_stylesheet(stylesheet_key)
            self._stylesheets[stylesheet_key] = stylesheet

        return stylesheet

    def _merge_stylesheets(self, stylesheets: list) -> str:
        return "\n".join(stylesheets)

    def _get_full_stylesheet_key(self, name: str) -> str:
        return self._stylesheets_path + "/" + name + ".qss"

    def _create_stylesheet(self, path: str) -> str:
        stylesheet = self._load_unmapped_stylesheet(path)
        return self._map_stylesheet(stylesheet)

    def _load_unmapped_stylesheet(self, path: str) -> str:
        with open(path, "r", encoding="utf-8") as file:
            return file.read()

    def _map_stylesheet(self, stylesheet: str) -> str:
        for variable_name, variable_value in self._variables.items():
            stylesheet = stylesheet.replace(variable_name, variable_value)

        return stylesheet

    def _init_variables(self, variables_path: str) -> None:
        if variables_path is None:
            return

        with open(variables_path, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip().replace(" ", "")
                if line.startswith("@"):
                    variable_name, variable_value = line.split("=", 1)
                    self._variables[variable_name] = variable_value
