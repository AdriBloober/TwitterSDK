class TwitterModel:
    __ignored_parameters__ = []

    @staticmethod
    def from_json(model_class, j):
        model = model_class()
        annotations = model.__annotations__
        if hasattr(model, "__extra_annotations__"):
            annotations.update(model.__extra_annotations__)
        if not j:
            return model
        for k, v in annotations.items():
            if k not in j or (hasattr(model_class, "__ignored_parameters__") and k in model_class.__ignored_parameters__):
                continue
            if v == model_class.__name__:
                v = model_class
            if hasattr(v, "__origin__") and v.__origin__ == list and hasattr(v.__args__[0], "to_json"):
                l = []
                for i in j[k]:
                    l.append(TwitterModel.from_json(v.__args__[0], i))
                setattr(model, k, l)
            elif hasattr(v, "to_json"):
                setattr(model, k, v.from_json(v, j[k]))
            else:
                setattr(model, k, j[k])
        return model

    def to_json(self):
        j = {}
        for k in dir(self):
            if k in self.__ignored_parameters__:
                continue
            v = getattr(self, k)
            if not k.startswith("__") and not callable(v):
                if v == list:
                    l = []
                    for i in v:
                        if hasattr(i, "to_json"):
                            l.append(i.to_json())
                        else:
                            l.append(i)
                    j[k] = l
                elif isinstance(v, TwitterModel):
                    j[k] = v.to_json()
                else:
                    j[k] = v
        return j

    def __repr__(self):
        r = f"<{self.__class__.__name__}"
        for k in dir(self):
            v = getattr(self, k)
            if not k.startswith("__") and not callable(v):
                if hasattr(v, "__repr__"):
                    r += " " + k + "=" + v.__repr__()
                else:
                    r += " " + k + "=" + v
        return r + " >"


class TranslatedTwitterObject(TwitterModel):
    raw = ""

    @staticmethod
    def from_json(model_class, v):
        return model_class(v)

    def to_json(self):
        return self.raw
