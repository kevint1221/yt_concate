from .step import Step


class Cleanup(Step):
    def process(self, data, inputs, utils):
        print("cleanning up")
