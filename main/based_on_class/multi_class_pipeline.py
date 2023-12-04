class MULTI_CLASS_PIPELINE:
    def __init__(self, data) -> None:
        self.data = data

    class PIPELINE_A:
        def __init__(self, data) -> None:
            self.data = data

        def __call__(self, CFG):
            pass

    class PIPELINE_B:
        def __init__(self, data) -> None:
            self.data = data

        def __call__(self, CFG):
            pass

    def __call__(self, CFG):
        a_result = self.PIPELINE_A(self.data)(CFG["PIPELINE_A"])
        result = self.PIPELINE_B(a_result)(CFG["PIPELINE_B"])
        return result


"""
# v_1
multi_class_pipeline = MULTI_CLASS_PIPELINE(data)
result = multi_class_pipeline(CFG)

# v_2
pipeline_a = MULTI_CLASS_PIPELINE.PIPELINE_A(data)

a_result = pipeline_a(CFG["PIPELINE_A"])

pipeline_b = MULTI_CLASS_PIPELINE.PIPELINE_B(a_result)
b_result = pipeline_b(CFG['PIPELINE_B'])
result = b_result
"""