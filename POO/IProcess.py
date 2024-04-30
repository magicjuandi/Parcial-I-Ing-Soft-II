from abc import ABCMeta, abstractmethod


class IProcess(metaclass=ABCMeta):
    @abstractmethod
    def add(self):
        pass

    @abstractmethod 
    def edit(self):
        pass
     
    @abstractmethod
    def remove(self):
        pass

    @abstractmethod
    def checkout(self):
        pass
    