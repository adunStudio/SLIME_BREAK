from abc import *


class Scene(metaclass=ABCMeta):

    image = None

    @abstractmethod
    def enter(self):
        pass

    @abstractmethod
    def exit(self):
        pass

    @abstractmethod
    def pause(self):
        pass

    @abstractmethod
    def resume(self):
        pass

    @abstractmethod
    def handle_events(self, events):
        pass

    @abstractmethod
    def update(self, frame_time):
        pass

    @abstractmethod
    def draw(self):
        pass