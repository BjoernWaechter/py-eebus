def array_2_dict(arr):
    return {list(v.keys())[0]: v[list(v.keys())[0]] for v in arr}


class SpineMessageType:
    def __init__(
        self
    ):
        pass

    def get_data(self):
        raise NotImplementedError("get_data has to be implemented")

    def __str__(self):
        pass