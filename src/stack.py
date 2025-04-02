_stack = []

def push(name):
    """
    Lägger ett namn (sträng) överst på stacken.
    """
    _stack.append(name)

def pop():
    """
    Tar bort och returnerar det översta namnet från stacken.
    Kastar IndexError om stacken är tom.
    """
    if not _stack:
        raise IndexError("Stacken är tom")
    return _stack.pop()

def peek():
    """
    Returnerar det översta namnet utan att ta bort det.
    Kastar IndexError om stacken är tom.
    """
    if not _stack:
        raise IndexError("Stacken är tom")
    return _stack[-1]

def clear_stack():
    """
    Tömmer stacken.
    """
    _stack.clear()

def size():
    """
    Returnerar antalet element i stacken.
    """
    return len(_stack)
