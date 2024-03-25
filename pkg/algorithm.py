class Algorithm:
    def __init__(self, matcher, dataframe, test):
        self.matcher = matcher
        self.dataframe = dataframe
        self.test = test

    def output_json(self):
        pass

    def output_text(self):
        pass

    def output(self,output_format):
        if output_format=="json":
            return self.output_json()
        elif output_format=="text":
            return self.output_text()
        else:
            raise ValueError("Unsupported output format {output_format} selected")