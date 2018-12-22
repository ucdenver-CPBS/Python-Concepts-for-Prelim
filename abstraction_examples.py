from abc import abstractmethod, ABC


###################
# Basic Pipeline
###################

# Note that Step uses Abstract Beta Class (ABC) to indicate that it is intended to be extended
class Step(ABC):
    @abstractmethod
    def run(self, output):
        pass


class Pipeline:
    def __init__(self):
        self.steps = []
        self.output = 0

    def add_step(self, step):
        self.steps.append(step)

    def run_steps(self):
        for step in self.steps:
            # All steps will have this run method because they are all derived from the Step class
            self.output = step.run(self.output)


###################
# Specific Pipeline
###################

class MathOperation(Step, ABC):
    def __init__(self, value):
        self.value = value


class Add(MathOperation):
    def run(self, output):
        return output + self.value  # Note how value here was defined in the MathOperation class


class Subtract(MathOperation):
    def run(self, output):
        return output - self.value


class MultiplyBy(MathOperation):
    def run(self, output):
        return output * self.value


class DivideBy(MathOperation):
    def __init__(self, value):
        if value == 0:
            print("Don't divide by zero")
            raise ZeroDivisionError  # Don't allow your users to make stupid mistakes
        super().__init__(value)

    def run(self, output):
        return output / self.value


if __name__ == '__main__':
    pipeline = Pipeline()

    try:
        pipeline.add_step(Add(2))
        pipeline.add_step(Subtract(1))
        pipeline.add_step(MultiplyBy(1))
        pipeline.add_step(MultiplyBy(128))
        pipeline.add_step(DivideBy(2))
        pipeline.add_step(Subtract(1))
        pipeline.add_step(DivideBy(0))
        pipeline.add_step(Add(2))
        pipeline.add_step(Add(9))
    except:
        print("Tried to add a bad step")

    # Nothing has been run yet
    assert pipeline.output == 0

    pipeline.run_steps()
    assert pipeline.output == 63
    print(f"The output is {pipeline.output}")
