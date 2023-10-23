from .step import Step


class Preflight(Step):
    def process(self, data, inputs, utils):
        print('In prefligt step')
        utils.create_dirs()