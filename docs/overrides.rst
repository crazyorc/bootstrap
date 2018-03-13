Package Overrides
=================
Package overrides are a method of providing local alterations to a package
without modifying a build.config.

A simple use case is changing a revision for a given yocto layer.


Format
------
Override files are located in
:code:`${HOME_DIRECTORY}/.bootstrap.d/overrides.d/<override-name>/<package-name>.conf`.
Files are the same section and key/value pairs as other bootstrap files.

Any valid key/values can be used in sections.


Sections
--------
The following sections are supported:

* :code:`append` - Add a value to a package config.  If the package doesn't
  have an option for the key, this functions identically to set.
* :code:`delete` - Remove a value.  This *will not* remove values provided by
  the DEFAULT section.
* :code:`set` - Set a value.


Example
-------
.. code:: bash

    $ cat ~/.bootstrap.d/overrides.d/updated-poky/poky.conf
    [set]
    git.revision = 0000000000000000000000000000000000000000

