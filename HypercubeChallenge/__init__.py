"""
The HypercubeChallenge library

This library is designed to build an array of vectors in an n-dimensional 
hypercube, whose vectors satisfy a system of non-linear constraints.

This library includes the following functions:

::

    HypercubeChallenge.src.__main__.main()

this is the entry point of the command line interface. :code:`main()` directs 
arguments from the CLI to the necessary subroutines within the library for 
calculation.

::

    HypercubeChallenge.src.calculator.calculate(
        input_file, n_results
    )

the calculator uses the input file and n_results integer to run the calculation.
results are returned to be saved.

::

    HypercubeChallenge.src.tools.cmd_reader.reader()

the reader function parses the command-line interface arguments for calculation.

::

    HypercubeChallenge.src.tools.cleaning.cleaner(
        class_object, report_values, test_values
    )

the cleaning function extracts the passing test values from the test_values 
array and appends them to the report_values array, using constraints defined in
the class_object.

::

    HypercubeChallenge.src.tools.generator.generate(
        test_values, report_values
    )

the generate function uses linear interpolation to build new test values from
previously rejected test values and accepted report values.

"""

from HypercubeChallenge import src
