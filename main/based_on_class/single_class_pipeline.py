class SINGLE_CLASS_PIPELINE:
    def __init__(self, data) -> None:
        self.data = data

    def pre_process(self, CFG):
        pass

    def process(self, CFG):
        pass

    def post_process(self, CFG):
        pass

    def __call__(self, CFG):
        pre_processed_data = self.pre_process(self.data, CFG["PRE_PROCESS"])
        processed_data = self.process(pre_processed_data, CFG["PROCESS"])
        post_processed_data = self.post_process(processed_data, CFG["POST_PROCESS"])
        return post_processed_data


"""
single_class_pipeline = SINGLE_CLASS_PIPELINE(data)
result = single_class_pipeline(CFG)
"""
