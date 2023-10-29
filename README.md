# python-stubs

This repository provides stubs for some python packages that do not offer proper type hints
and have no stubs available. The main goal is to provide helpers for VSCode's Pylance language
server to offer better autocompletion. Another goal is to improve the performance of VSCode's
python extension where it suffers from slow downs with some packages (For example, installing
`pandapower` without the stubs, python analysis in VSCode takes up to 7 seconds to complete on
every change).

## Usage

1. Clone the repository:
    ```bash
    git clone https://github.com/hamdanal/python-stubs /path/to/python-stubs
    ```
2. Add the following to VSCode's `settings.json`:
    ```json
    "python.analysis.stubPath": "/path/to/python-stubs/stubs"
    ```

## Contributing

Contributions of any kind are welcome. Please open an issue or a send pull request.

## License

This project is licensed under the MIT License.

## Acknowledgments

Some of the project settings and development tools are taken from/based off the
[typeshed](https://github.com/python/typeshed) project.

## Why not typeshed?

These stubs could ideally be added to typeshed, and everyone using IDEs like VSCode and PyCharm
or static type checkers like mypy would benefit from them. Unfortunately, there are some reasons
that make this difficult to add a new package to typeshed:
- In the case of `netfields` and `psqlextra`: These packages depend on
  [django-types](https://github.com/sbdchd/django-types) and
  [djangorestframework-types](https://github.com/sbdchd/djangorestframework-types) projects that
  are maintained outside of typeshed.
- In the case of `pandapower`, the package is very large (about 330 .py files) and has a **lot**
  of dependencies (18 direct dependencies with the extras, about 45 total dependencies)

If you think otherwise and are interested in adding any of these stubs to typeshed, you are welcome
to copy the stubs in this repository and use them as a starting point.

## TODO

The project is already useful as is, but there are still some things to do:
- [ ] Some stubs are incomplete; they are just enough to make Pylance *happy*.
- [ ] The stubs are not tested. Should be tested with pyright, mypy, stubtest and optionally pytype.
- [ ] No CI is set up yet.

## List of available stubs

Project | Links | Status
------- | ----- | ------
django-netfields | [PyPI](https://pypi.org/project/django-netfields/), [GitHub](https://github.com/jimfunk/django-postgresql-netfields) | Incomplete
django-postgres-extra | [PyPI](https://pypi.org/project/django-postgres-extra/), [GitHub](https://github.com/SectorLabs/django-postgres-extra) | Incomplete
pandapower | [PyPI](https://pypi.org/project/pandapower/), [GitHub](https://github.com/e2nIEE/pandapower) | Incomplete
seaborn | [PyPI](https://pypi.org/project/seaborn/), [GitHub](https://github.com/mwaskom/seaborn) | Upstreamed to typeshed
geopandas | [PyPI](https://pypi.org/project/geopandas/), [GitHub](https://github.com/geopandas/geopandas) | Complete
