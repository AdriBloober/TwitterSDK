class PathOperation:
    def __init__(self, raw_path, needs_authentication=True, version_requirement=True):
        self.needs_authentication = needs_authentication
        if type(raw_path) == str:
            self.raw_path = raw_path.split("/")[1:]
        else:
            self.raw_path = raw_path
        self.version_requirement = version_requirement

    def __add__(self, other):
        if type(other) == PathOperation:
            return PathOperation(self.raw_path + other.raw_path, version_requirement=self.version_requirement)
        elif type(other) == str:
            return PathOperation(self.raw_path + other.split("/")[1:], version_requirement=self.version_requirement)
        else:
            raise TypeError(f"Unsupported types '{self.__class__.__name__}' + '{type(other)}'.")

