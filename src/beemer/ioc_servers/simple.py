"""
Simple IOC server built with caproto.

This is based on the caproto example at
https://github.com/caproto/caproto/blob/master/caproto/ioc_examples/simple.py
"""

from caproto.server import PVGroup, ioc_arg_parser, pvproperty, run


class SimpleIOC(PVGroup):
    """
    A simple IOC with three uncoupled read/writable PVs.

    Scalar PVs
    ----------
    A (int)
    B (float)

    Array PVs
    ---------
    C (array of int)
    """

    A = pvproperty(value=1, doc="An integer")
    B = pvproperty(value=2.0, doc="A float")
    C = pvproperty(value=[1, 2, 3], doc="An array of integers (max length 3)")


def main():
    """
    Run this IOC server.
    """
    ioc_options, run_options = ioc_arg_parser(
        desc="Simple IOC", default_prefix="simple:"
    )
    ioc = SimpleIOC(**ioc_options)
    run(ioc.pvdb, **run_options)


if __name__ == "__main__":
    main()
