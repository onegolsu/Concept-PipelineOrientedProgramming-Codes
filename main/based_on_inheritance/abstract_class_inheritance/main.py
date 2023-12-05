from preprocess import A_PRE_PROCESSOR, B_PRE_PROCESSOR
from process import A_PROCESSOR, B_PROCESSOR
from postprocess import A_POST_PROCESSOR, B_POST_PROCESSOR


def get_data():
    pass


def get_cfg():
    pass


data = get_data()
CFG = get_cfg()


def pipeline_1d_composer(preprocessor, processor, postprocessor):
    pipeline = lambda data: postprocessor.get_1d_post_process(
        processor.get_1d_process(preprocessor.get_1d_pre_process(data))
    )
    return pipeline


def pipeline_2d_composer(preprocessor, processor, postprocessor):
    pipeline = lambda data: postprocessor.get_2d_post_process(
        processor.get_2d_process(preprocessor.get_2d_pre_process(data))
    )
    return pipeline


a_1d_pipeline = pipeline_1d_composer(A_PRE_PROCESSOR, A_PROCESSOR, A_POST_PROCESSOR)
a_2d_pipeline = pipeline_2d_composer(A_PRE_PROCESSOR, A_PROCESSOR, A_POST_PROCESSOR)

b_1d_pipeline = pipeline_1d_composer(B_PRE_PROCESSOR, B_PROCESSOR, B_POST_PROCESSOR)
b_2d_pipeline = pipeline_2d_composer(B_PRE_PROCESSOR, B_PROCESSOR, B_POST_PROCESSOR)

# can be use_by composer
from functools import reduce

def function_composer(f, g):
    return lambda x: f(g(x))

def composer(functions):
    return reduce(lambda x, y: function_composer(x, y), functions)