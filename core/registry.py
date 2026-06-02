registry = []


def register(cls):
    registry.append(cls())
    return cls
