def add(a, b):
    """
    Returnerar summan av a och b.
    """
    return a + b

def subtract(a, b):
    """
    Returnerar resultatet av a minus b.
    """
    return a - b

def multiply(a, b):
    """
    Returnerar produkten av a och b.
    """
    return a * b

def divide(a, b):
    """
    Returnerar kvoten av a delat med b.
    Kastar ett ValueError om b är 0.
    """
    if b == 0:
        raise ValueError("Delat med noll")
    return a / b