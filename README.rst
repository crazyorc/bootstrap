bootstrap
=========
A tool to help manage a yocto project with layers spread across repositories.


Inspiration
-----------
I work with several yocto projects where each layer is a repo. Searching did
not turn up tools that met my needs.

Google's repo tool works for projects like Freescale's yocto layers where the
project is static. However, the yocto projects I have been involved with have
some dynamic elements to them (eg. recipes change as new versions of code are
ready for testing). Various maintenance tasks become a burden - updating the
config file with the right layer revision, adding/removing layers, etc.

There is substantial overlap between the problems that the dev-pipeline project
solves and the needs of a yocto project maintainer. This project utilizes the
devpipeline library and provides a yocto project oriented porcelain.

In particular, bootstrap supports the following features:

#. Defining required layers (repo + revision) and layer dependencies
#. Defining project filesystem layout via configuration file
#. Updating of configuration file - including add/remove layers


Installation
------------
You must first install devpipeline (devpipeline_).

The simplest way to install is using pip_ (adding the :code:`--user` installs to your home directory).

.. code:: bash

    $ cd /path/to/bootstrap
    $ pip install [--user]

If you don't have pip available, you can run :code:`setup.py` directly (adding the :code:`--user` installs to your home directory).

.. code:: bash

    $ cd /path/to/bootstrap
    $ python setup.py install [--user]

If the install completes you're good to go.  Depending on your project
configuration you may need to install additional tools such as cmake or git;
installing those tools is beyond the scope of this document.


Using
-----
The first thing you'll need to do is write a `project configuration`_.  Once
you're ready, checkout_ the project sources.

.. code:: bash

    # checkout with default settings
    $ bs checkout

That's it.  Check the tool documentation for information on what's available.


Common Tools
------------
* checkout_ - Fetch sources in dependecy order.


.. _project configuration: docs/config.rst
.. _checkout: docs/tools/checkout.rst
.. _devpipeline: https://github.com/snewell/dev-pipeline
.. _pip: https://pypi.python.org/pypi/pip
