class GENERAL_PROCESSOR:
    def general_preprocess():
        pass

    def general_process():
        pass

    def general_postprocess():
        pass


class A_PROCESSOR(GENERAL_PROCESSOR):
    def __init__(self, data) -> None:
        self.data = data

    def preprocess(self, CFG):
        super().general_preprocess()
        pass

    def process(self, CFG):
        super().general_process()
        pass

    def postprocess(self, CFG):
        super().general_postprocess()
        pass

    def __call__(self, CFG):
        cfg = CFG["processor"]
        self.preprocess(cfg["PRE_PROCESSO"])
        self.process(cfg["PROCESS"])
        self.postprocess(cfg["POST_PROCESS"])


class B_PROCESSOR(GENERAL_PROCESSOR):
    def __init__(self, data) -> None:
        self.data = data

    def preprocess(self, CFG):
        super().general_preprocess()
        pass

    def process(self, CFG):
        super().general_process()
        pass

    def postprocess(self, CFG):
        super().general_postprocess()
        pass

    def __call__(self, CFG):
        cfg = CFG["processor"]
        self.preprocess(cfg["PRE_PROCESSO"])
        self.process(cfg["PROCESS"])
        self.postprocess(cfg["POST_PROCESS"])
