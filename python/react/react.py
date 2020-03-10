class DAG:
    def __init__(self):
        self._inputs = []
        self._graph = {}


DEFAULT_GRAPH = DAG()


class InputCell:
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if new_value == self._value:
            return
        self._value = new_value

    def __init__(self, initial_value, graph=DEFAULT_GRAPH):
        self._value = initial_value
        self._watchers = {}
        self._graph = graph


class ComputeCell:
    @property
    def value(self):
        self._value = self._calculate()
        return self._value

    def __init__(self, inputs, compute_function, graph=DEFAULT_GRAPH):
        self.compute_function = compute_function
        self.inputs = inputs
        self._value = None
        self._graph = graph

    def add_callback(self, callback):
        pass

    def remove_callback(self, callback):
        pass

    def _calculate(self):
        return self.compute_function([x.value for x in self.inputs])
