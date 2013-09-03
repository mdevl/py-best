"""This module defines classes that are helpful in designing experiments.

Author:
    Ilias Bilionis

Date:
    8/19/2013
"""


__all__ = ['latin_center', 'latin_edge', 'latin_random', 'latinize']


from ..core import design


def _check_args(num_points, num_dim, seed):
    """Check if the arguments to the latin_*() functions are ok."""
    if seed is None:
        seed = design.get_seed()
    seed = int(seed)
    num_points = int(num_points)
    num_dim = int(num_dim)
    assert seed > 0
    assert num_points >= 1
    assert num_dim >= 1
    return num_points, num_dim, seed


def latin_center(num_points, num_dim, seed=None):
    """
    Construct a centered Latin Square design.

    This is a wrapper of the fortran code:
    `latin_center() <http://people.sc.fsu.edu/~jburkardt/f_src/latin_center/latin_center.html>`_.

    Parameters
    ----------
    num_points : int
                 The number of design points.
    num_dim : int
              The number of dimensions
    seed : int
           A random seed. If ``None``, then it is initialized
           automatically.

    Returns
    -------
    x : (num_points, num_dim) ndarray

    Examples
    --------
    >>> x = best.design.latin_center(10, 2)
    >>> print x
    """
    num_points, num_dim, seed = _check_args(num_points, num_dim, seed)
    return design.latin_center(num_dim, num_points, seed).T


def latin_edge(num_points, num_dim, seed=None):
    """
    Construct a Latin Edge Square design.

    This is a wrapper of the fortran code:
    `latin_center() <http://people.sc.fsu.edu/~jburkardt/f_src/latin_edge/latin_edge.html>`_.

    Parameters
    ----------
    num_points : int
                 The number of design points.
    num_dim : int
              The number of dimensions
    seed : int
           A random seed. If ``None``, then it is initialized
           automatically.

    Returns
    -------
    x : (num_points, num_dim) ndarray

    Examples
    --------
    >>> x = best.design.latin_edge(10, 2)
    >>> print x
    """
    num_points, num_dim, seed = _check_args(num_points, num_dim, seed)
    return design.latin_edge(num_dim, num_points, seed).T


def latin_random(num_points, num_dim, seed=None):
    """
    Construct a Latin Edge Square design.

    This is a wrapper of the fortran code:
    `latin_center() <http://people.sc.fsu.edu/~jburkardt/f_src/latin_random/latin_random.html>`_.

    Parameters
    ----------
    num_points : int
                 The number of design points.
    num_dim : int
              The number of dimensions
    seed : int
           A random seed. If ``None``, then it is initialized
           automatically.

    Returns
    -------
    x : (num_points, num_dim) ndarray

    Examples
    --------
    >>> x = best.design.latin_random(10, 2)
    >>> print x
    """
    num_points, num_dim, seed = _check_args(num_points, num_dim, seed)
    return design.latin_random(num_dim, num_points, seed).T


def latinize(table):
    """
    Adjust an D dimensional dataset of N points so that it forms a
    Latin hypercube.

    Parameters
    ----------
    table : (N, D) array_like
            The dataset to be adjusted. A copy is made.

    Returns
    -------
    table : (N, D) ndarray
            The adjusted dataset.

    Examples
    --------
    >>> X = np.random.rand(100, 2)
    >>> X_adj = best.design.latinize(table)
    >>> plt.plot(X[:, 0], X[:, 1], '+', X_adj[:, 0], X_adj[:, 1], 'o')
    >>> plt.show()
    """
    return design.latinize(table.T.copy()).T


def _sg_string_to_rule(rule_str):
    """
    Turn a Sparse Grid rule from a string to an integer.

    Parameters
    ----------
    rule_str    :   str
                    The rule in str form. Choose from:

                        1. "CC", Clenshaw Curtis Closed Fully Nested rule.
                        2. "F1", Fejer 1 Open Fully Nested rule.
                        3. "F2", Fejer 2 Open Fully Nested rule.
                        4. "GP", Gauss Patterson Open Fully Nested rule.
                        5. "GL", Gauss Legendre Open Weakly Nested rule.
                        6. "GH", Gauss Hermite Open Weakly Nested rule.
                        7. "LG", Gauss Laguerre Open Non Nested rule.

    Returns
    -------
    rule        :   int
                    The rule number.
    """
    if rule_str == 'CC':
        return 1
    elif rule_str == 'F1':
        return 2
    elif rule_str == 'F2':
        return 3
    elif rule_str == 'GP':
        return 4
    elif rule_str == 'GL':
        return 5
    elif rule_str == 'GH':
        return 6
    elif rule_str == 'LG':
        return 7
    raise ValueError('Unkown quadrature rule.')


def sparse_grid(num_dim, max_level, rule='CC'):
    """
    Compute a Sparse Grid.

    Parameters
    ----------
    num_dim     :   int
                    Number of dimensions.
    max_level   :   int
                    The maximum level of the sparse grid.
    rule        :   str
                    The quadrature rule. The default is "CC". Choose from:

                        1. "CC", Clenshaw Curtis Closed Fully Nested rule.
                        2. "F1", Fejer 1 Open Fully Nested rule.
                        3. "F2", Fejer 2 Open Fully Nested rule.
                        4. "GP", Gauss Patterson Open Fully Nested rule.
                        5. "GL", Gauss Legendre Open Weakly Nested rule.
                        6. "GH", Gauss Hermite Open Weakly Nested rule.
                        7. "LG", Gauss Laguerre Open Non Nested rule.

    Returns
    -------
    grid_point  :   (num_point, num_dim) ndarray
                    The points of the grid.
    grid_weight :   num_point ndarray
                    The weights of the grid points.
    """
    rule = _sg_string_to_rule(rule)
    num_point = design.levels_index_size(num_dim, max_level, rule)
    grid_weight, grid_point = design.sparse_grid(num_dim, max_level,
                                                 rule, num_point)
    return grid_point.T, grid_weight.T