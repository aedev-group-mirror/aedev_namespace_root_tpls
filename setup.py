# THIS FILE IS EXCLUSIVELY MAINTAINED by the project aedev.project_tpls v0.3.76
""" setup of aedev namespace package portion namespace_root_tpls: templates (managed files) for namespace root projects.. """
import sys
# noinspection PyUnresolvedReferences
import pathlib
# noinspection PyUnresolvedReferences
import setuptools


print("SetUp " + __name__ + ": " + sys.executable + str(sys.argv) + f" {sys.path=}")

setup_kwargs = {
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
            'pytest-django',
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
            'pytest-django',
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
            'templates/de_tpl_dev_requirements.txt',
            'templates/de_otf_de_tpl_README.md',
            'templates/de_mtp_templates/de_otf__z_de_spt_namespace-root_de_otf_de_tpl_README.md',
            'templates/de_sfp_docs/de_otf_de_tpl_index.rst',
            'templates/de_sfp_docs/features_and_examples.rst',
        ],
    },
    'packages': [
        'aedev.namespace_root_tpls',
        'aedev.namespace_root_tpls.templates',
        'aedev.namespace_root_tpls.templates.de_mtp_templates',
        'aedev.namespace_root_tpls.templates.de_sfp_docs',
    ],
    'project_urls': {
        'Bug Tracker': 'https://gitlab.com/aedev-group/aedev_namespace_root_tpls/-/issues',
        'Documentation': 'https://aedev.readthedocs.io/en/latest/_autosummary/aedev.namespace_root_tpls.html',
        'Repository': 'https://gitlab.com/aedev-group/aedev_namespace_root_tpls',
        'Source': 'https://aedev.readthedocs.io/en/latest/_modules/aedev/namespace_root_tpls.html',
    },
    'python_requires': '>=3.12',
    'url': 'https://gitlab.com/aedev-group/aedev_namespace_root_tpls',
    'version': '0.3.27',
    'zip_safe': False,
}

if __name__ == "__main__":
    setuptools.setup(**setup_kwargs)
    pass
