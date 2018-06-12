from src.model.cart_pole_parameters import CartPoleParameters

# Keeps the state of the application
class Document:
    def __init__(self):
        self._parameters = CartPoleParameters()