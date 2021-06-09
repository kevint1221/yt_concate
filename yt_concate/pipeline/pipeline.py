"""
This is a pipeline that execute each step
"""

from .steps.step import StepException


class Pipeline:
    def __init__(self, steps):
        self.steps = steps

    def run(self, inputs, utils):
        data = None
        for step in self.steps:
            try:
                data = step.process(data, inputs, utils)  # each process passing data to next step
            except StepException as e:
                print("exception in step happened at: ", e)
                break
