# __{namespace_name}__ {project_type} project

{project_desc}

{TEMPLATE_PLACEHOLDER_ID_PREFIX}{TEMPLATE_INCLUDE_FILE_PLACEHOLDER_ID}{TEMPLATE_PLACEHOLDER_ID_SUFFIX}
    README_intro.md
{TEMPLATE_PLACEHOLDER_ARGS_SUFFIX}

## {namespace_name} namespace root package use-cases

this package is the root project of the {namespace_name} namespace and their portions (the modules
and packages belonging to the namespace {namespace_name}). it provides helpers and templates
in order to bundle and ease the maintenance, for example to:

* update and deploy managed files created and renewed from template files.
* merge docstrings of all portions into a single combined and cross-linked documentation.
* compile and publish documentation via Sphinx onto [ReadTheDocs]({docs_root} "{namespace_name} on RTD").
* bulk manage/update/refactor multiple portion projects of this namespace simultaneously using the
  [git repository manager tool (__pjm__)](https://gitlab.com/aedev-group/aedev_project_manager).

to enable the update and deployment of managed files generated from the templates provided by
this root package, add this root package to the development requirements file ({REQ_DEV_FILE_NAME})
of each portion project of this namespace. in this entry you can optionally specify the version of
this project.

and because this {project_type} package is only needed for development tasks, it will never need to
be added to the installation requirements file ({REQ_FILE_NAME}) of a namespace portion project.

please check the [project manager manual](
https://aedev.readthedocs.io/en/latest/man/project_manager.html "project_manager manual")
for more detailed information on the provided actions of the __pjm__ tool.


## installation

no installation is needed to use this project for your portion projects, because the __pjm__ tool is
automatically fetching this and the other template projects from {repo_root} (and
in the specified version).

an installation is only needed if you want to adapt this {project_type} project for your needs or if you want
to contribute to this root package. in this case please follow the instructions given in the
:ref:`contributing` document.

{TEMPLATE_PLACEHOLDER_ID_PREFIX}{TEMPLATE_INCLUDE_FILE_PLACEHOLDER_ID}{TEMPLATE_PLACEHOLDER_ID_SUFFIX}
    README_outro.md
{TEMPLATE_PLACEHOLDER_ARGS_SUFFIX}

## namespace portions

the following {len(portions_packages)} portions are currently included in this namespace:

{portions_pypi_refs_md}
