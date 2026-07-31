# THIS FILE IS EXCLUSIVELY MAINTAINED by the project aedev.project_tpls v0.3.91
""" setup of aedev namespace package portion namespace_root_tpls: templates (managed files) for namespace root projects.. """
import pathlib
import sys
from typing import Any
import setuptools


print("SetUp " + __name__ + ": " + sys.executable + str(sys.argv) + f" {sys.path=}")

setup_kwargs: dict[str, Any] = {
    'author': 'AndiEcker',
    'author_email': 'aecker2@gmail.com',
    'classifiers': [
        'Development Status :: 3 - Alpha',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.12',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Typing :: Typed',
    ],
    'description': 'aedev namespace package portion namespace_root_tpls: templates (managed files) for namespace root projects.',
    'extras_require': {
        'dev': [
            'aedev_project_tpls',
            'aedev_aedev',
            'anybadge',
            'flake8',
            'mypy',
            'pylint',
            'pytest',
            'pytest-cov',
            'typing',
            'types-setuptools',
        ],
        'docs': [],
        'tests': [
            'anybadge',
            'flake8',
            'mypy',
            'pylint',
            'pytest',
            'pytest-cov',
            'typing',
            'types-setuptools',
        ],
    },
    'install_requires': [],
    'keywords': [
        'configuration',
        'development',
        'environment',
        'productivity',
    ],
    'license': 'GPL-3.0-or-later',
    'long_description': (pathlib.Path(__file__).parent / 'README.md').read_text(encoding='utf-8'),
    'long_description_content_type': 'text/markdown',
    'name': 'aedev_namespace_root_tpls',
    'package_data': {
        '': [
            'templates/fSt-dev_requirements.txt',
            'templates/fSt-PutMar-README.md',
            'templates/MovPkg-templates/PutMar-_z_SkpTyp-namespace-root_fSt-PutMar-README.md',
            'templates/SkpPor-docs/features_and_examples.rst',
            'templates/SkpPor-docs/fSt-PutMar-index.rst',
        ],
    },
    'packages': [
        'aedev.namespace_root_tpls',
        'aedev.namespace_root_tpls.templates',
        'aedev.namespace_root_tpls.templates.MovPkg-templates',
        'aedev.namespace_root_tpls.templates.SkpPor-docs',
    ],
    'project_urls': {
        'Bug Tracker': 'https://gitlab.com/aedev-group/aedev_namespace_root_tpls/-/issues',
        'Documentation': 'https://aedev.readthedocs.io/en/latest/_autosummary/aedev.namespace_root_tpls.html',
        'Repository': 'https://gitlab.com/aedev-group/aedev_namespace_root_tpls',
        'Source': 'https://aedev.readthedocs.io/en/latest/_modules/aedev/namespace_root_tpls.html',
    },
    'python_requires': '>=3.12',
    'url': 'https://gitlab.com/aedev-group/aedev_namespace_root_tpls',
    'version': '0.3.33',
    'zip_safe': False,
}

if __name__ == "__main__":
    setuptools.setup(**setup_kwargs)
    ...
