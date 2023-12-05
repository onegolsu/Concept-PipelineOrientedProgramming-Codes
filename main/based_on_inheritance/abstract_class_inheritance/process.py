from abc import ABC, abstractmethod


class PROCESSOR(ABC):
    @abstractmethod
    def get_1d_process():
        pass

    @abstractmethod
    def get_2d_process():
        pass


class A_PROCESSOR(PROCESSOR):
    def get_1d_process():
        pass

    def get_2d_process():
        pass

    def get_3d_process():
        pass


class B_PROCESSOR(PROCESSOR):
    def get_1d_process():
        pass

    def get_2d_process():
        pass
