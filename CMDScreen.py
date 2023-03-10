import os
from ScreenState import ScreenState


class CMDScreen:
    def __init__(self):
        self.states = []

    def render(self, clear_screen=True):
        if clear_screen:
            os.system("cls")
        for state in self.states:
            print(state.render())

    def register(self, name, value):
        new_state = ScreenState(name, value)
        new_state.register_on_changed(self.render)
        new_state.register_on_unregister(self.unregister)

        self.states.append(new_state)
        return new_state

    def unregister(self, state):
        self.states = list(filter(lambda x: id(x) != id(state), self.states))
        del self
