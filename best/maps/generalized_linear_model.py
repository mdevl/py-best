"""A class that implements a generalized linear model.

Author:
    Ilias Bilionis

Date:
    8/14/2013
"""


import numpy as np
from function import Function


class GeneralizedLinearModel(Function):

    """A class that implements a generalized linear model."""

    # The basis (must be a best.maps.Function)
    _basis = None

    # The weight matrix/vector
    _weights = None

    @property
    def basis(self):
        return self._basis

    @property
    def weights(self):
        return self._weights

    @weights.setter
    def weights(self, w):
        assert isinstance(w, np.ndarray)
        w = np.atleast_2d(w)
        if self.num_output == 1 and not w.shape[0] == 1:
            w = w.T
        self._weights = w

    def __init__(self, basis, weights=None, num_output=1,
                 name='Generalized Linear Model'):
        """Initialize the object.

        Arguments:
            basis       ---     A basis for the model. It must be a
                                best.maps.Function.

        Keword Arguments:
            weights     ---     The weight matrix vector. It is a weight
                                matrix if basis.num_output > 1. If None,
                                then it is initialized to zero and its
                                dimensionality is found by looking at
                                num_output. It should be a
                                self.num_output x self.basis.num_output
                                matrix.
            num_output  ---     The number of output dimensions of the
                                generalized linear model. If weights is
                                not None, then it is ignored.
            name        ---     A name for the model.
        """
        assert isinstance(basis, Function)
        self._basis = basis
        if weights is None:
            if num_output == 1:
                weights = np.zeros(basis.num_output)
            else:
                weights = np.zeros((num_output, basis.num_output))
        super(GeneralizedLinearModel, self).__init__(self.basis.num_input,
                                                     num_output,
                                                     name=name)
        self.weights = weights

    def _eval(self, x):
        """Evaluate the model at x."""
        return np.dot(self.weights, self.basis._eval(x))

    def _d_eval(self, x):
        """Evaluate the derivative at x."""
        return np.dot(self.weights, self.basis._d_eval(x))