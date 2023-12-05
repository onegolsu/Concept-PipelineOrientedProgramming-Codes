from abc import ABC, abstractmethod


class PREPROCESSOR(ABC):
    @abstractmethod
    def get_1d_pre_process():
        pass

    @abstractmethod
    def get_2d_pre_process():
        pass


class A_PRE_PROCESSOR(PREPROCESSOR):
    def get_1d_pre_process():
        pass

    def get_2d_pre_process():
        pass

    def get_3d_pre_process():
        pass


class B_PRE_PROCESSOR(PREPROCESSOR):
    def get_1d_pre_process():
        pass

    def get_2d_pre_process():
        pass
