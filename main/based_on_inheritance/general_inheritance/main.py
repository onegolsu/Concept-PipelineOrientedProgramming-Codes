# general inheritance pipeline

## need caution on method to compose it into pipeline
from preprocess import A_PRE_PROCESSOR, B_PRE_PROCESSOR
from process import A_PROCESSOR, B_PROCESSOR
from postprocess import A_POST_PROCESSOR, B_POST_PROCESSOR


def get_data():
    pass


def get_cfg():
    pass


data = get_data()
CFG = get_cfg()


# raw
def pipeline_composer(preprocessor, processor, postprocessor):
    pipeline = lambda data, cfg: postprocessor(processor(preprocessor(data)(cfg))(cfg))(cfg)
    return pipeline


a_pipeline = pipeline_composer(A_PRE_PROCESSOR, A_PROCESSOR, A_POST_PROCESSOR)
a_result = a_pipeline(data, CFG)

b_pipeline = pipeline_composer(B_PRE_PROCESSOR, B_PROCESSOR, B_POST_PROCESSOR)
b_result = b_pipeline(data, CFG)

# can be used with partial
from functools import partial

class MyClass:
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b


MyClass_partial = partial(MyClass, 1)
myclass = MyClass_partial(2)
myclass.a, myclass.b
# -> (1,2)
