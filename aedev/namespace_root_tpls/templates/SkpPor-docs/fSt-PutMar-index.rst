namespace portions documentation
################################

welcome to the documentation of the portions (modules and packages) of the **{namespace_name}** namespace (:pep:`420`).

.. _{namespace_name}-features-examples:

.. toctree::
    :maxdepth: 1

    {format_file_paths("features_and_examples*.rst", path_prefix=DOCS_FOLDER)}
    code-conventions.rst
    register-new-namespace-portion.rst


.. _{namespace_name}-namespace-portions-api:

**********************
namespace portions API
**********************

the following index lists all registered portions of the **{namespace_name}** namespace, plus any additional modules
of each portion. each section documents the constants, functions and classes of each module.


.. autosummary::
    :toctree: _autosummary
    :nosignatures:

    {portions_import_names}

{'''

*********************
manuals and tutorials
*********************

.. toctree::

    ''' + _manus if (_manus := format_file_paths('man', "**", "*.rst", path_prefix=DOCS_FOLDER)) else ""}


**************************
general indices and tables
**************************

* `portion repositories at {repo_domain} <{repo_root}>`__
* :ref:`genindex`
* :ref:`modindex`
* ``ae`` namespace `projects <https://gitlab.com/ae-group>`__
  and `documentation <https://ae.readthedocs.io>`__
* ``aedev`` namespace `projects <https://gitlab.com/aedev-group>`__
  and `documentation <https://aedev.readthedocs.io>`__
