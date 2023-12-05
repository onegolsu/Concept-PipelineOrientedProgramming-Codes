from abc import ABC, abstractmethod


class POSTPROCESSOR(ABC):
    @abstractmethod
    def get_1d_post_process():
        pass

    @abstractmethod
    def get_2d_post_process():
        pass


class A_POST_PROCESSOR(POSTPROCESSOR):
    def get_1d_post_process():
        pass

    def get_2d_post_process():
        pass

    def get_3d_post_process():
        pass


class B_POST_PROCESSOR(POSTPROCESSOR):
    def get_1d_post_process():
        pass

    def get_2d_post_process():
        pass
