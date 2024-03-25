from pkg.edivisive import EDivisive
from pkg.relativeMeanDifference import RelativeMeanDifference

class AlgorithmFactory:
    def instantiate_algorithm(self, algorithm, matcher, dataframe, test):
        if algorithm == "EDivisive":
            return EDivisive(matcher, dataframe, test)
        elif algorithm == "RelativeMeanDifference":
            return RelativeMeanDifference(matcher, dataframe, test)
        else:
            raise ValueError("Invalid algorithm called")

