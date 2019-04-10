Inequality Coefficients:
========================

This is small library with some implemented coefficients (or indices)
intended to measure inequality or concentration of the values in a
population.

Implemented coefficients
-------------
* Gini Coefficient
* Ratio top / rest

Installation
------------

This library is hosted on PyPI, so installation is straightforward. The
easiest way to install type this at the command line (Linux, Mac, or
Windows):

    pip install inequality_coefficients

This library also depends on numpy, but `pip` should take of that for
you already.

Basic Usage
-----------

For the simplest, typical use cases, this tells you everything you need
to know.:

    import inequality_coefficients as ineq
    data = array([1.7, 3.2 ...]) # data can be list of nums or numpy array
    gini_coeff = ineq.gini_coeff(data)
    ratio_top_rest = ineq.ratio_top10_rest(data)

Acknowledgements
----------------

Many thanks to Felipe Ortega to open source his implementation of the
Gini coefficient, available here:
https://github.com/ryanwitt/wikixray/blob/master/graphics.py.

My code is based on that implementation, although I have made some
changes and added a correction for small datasets based on [Deltas,
2003](https://doi.org/10.1162/rest.2003.85.1.226).
