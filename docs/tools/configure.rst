configure
=========

Synopsis
--------
.. code::

    bs configure [-h] [--config CONFIG] [--override OVERRIDE]


Description
-----------
Configure a project to prepare for checkout. This will apply any overrides that
have been specified.

This is required before most other tools will work.


Options
-------
  -h, --help            show this help message and exit
  --config CONFIG       Build configuration file (default: build.config)
  --override OVERRIDE   Collection of override options to use. If you require
                        multiple types of overrides, separate the names with
                        commas. (default: None)

