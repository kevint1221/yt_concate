from .step import Step


class Setup(Step):
    def process(self, data, inputs, utils):
        print("setting up directory")
        utils.create_dir()