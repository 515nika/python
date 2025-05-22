class ShipPlacementError(Exception):
    """Корабль нельзя так разместить!"""
    pass

class InvalidCoordinateError(Exception):
    """Недопустимые координаты!"""
    pass