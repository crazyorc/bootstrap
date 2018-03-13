#!/usr/bin/python3
"""This modules does the checkout of code from SCM."""

from bootstrap.commands import LayersCommand
from bootstrap.exec import Configure

import devpipeline.scm.scm
import devpipeline.common


def main(args=None):
    # pylint: disable=missing-docstring
    checkout = LayersCommand([
        devpipeline.scm.scm.scm_task
    ], prog="bs checkout", description="Checkout yocto layer repositories")
    devpipeline.common.execute_tool(Configure(), args)
    devpipeline.common.execute_tool(checkout, args)


if __name__ == '__main__':
    main()
