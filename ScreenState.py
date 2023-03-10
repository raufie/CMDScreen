class ScreenState:
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.f = lambda: None
        self.on_unregister = lambda: print("UNABLE TO DELETE")

    def render(self):
        return f"{self.name}\n{self.value}"

    def set_name(self, name):
        self.name = name
        self.on_change()

    def set_value(self, value):
        self.value = value
        self.on_change()

    def register_on_changed(self, f):
        self.on_change = f

    def register_on_unregister(self, f):
        self.on_unregister = f

    def unregister(self):
        self.on_unregister(self)
