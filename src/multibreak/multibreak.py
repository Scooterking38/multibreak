class BreakLevel(Exception):
    def __init__(self, levels=1):
        super().__init__()
        self.levels = levels

def break_(n=1):
    if n < 1: raise ValueError("break levels must be more than 1")
    raise BreakLevel(n)

def handle_break(func):
    def wrapper(*args, **kwargs):
        try: func(*args, **kwargs)
        except BreakLevel as e:
            e.levels -= 1
            if e.levels > 0: raise e
    return wrapper
