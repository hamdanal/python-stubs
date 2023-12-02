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

<table>
  <tr>
    <th>Project</th>
    <th>Import name</th>
    <th>Links</th>
    <th>Status</th>
  </tr>
  <tr>
    <th>django-netfields</th>
    <th><code>netfields</code></th>
    <th>
      <a href="https://pypi.org/project/django-netfields">PyPI</a>,
      <a href="https://github.com/jimfunk/django-postgresql-netfields">GitHub</a>
    </th>
    <th>Complete</th>
  </tr>
  <tr>
    <th>django-postgres-extra</th>
    <th><code>psqlextra</code></th>
    <th>
      <a href="https://pypi.org/project/django-postgres-extra">PyPI</a>,
      <a href="https://github.com/SectorLabs/django-postgres-extra">GitHub</a>
    </th>
    <th>Incomplete</th>
  </tr>
  <tr>
    <th>pandapower</th>
    <th><code>pandapower</code></th>
    <th>
      <a href="https://pypi.org/project/pandapower">PyPI</a>,
      <a href="https://github.com/e2nIEE/pandapower">GitHub</a>
    </th>
    <th>Incomplete</th>
  </tr>
  <tr>
    <th>geopandas</th>
    <th><code>geopandas</code></th>
    <th>
      <a href="https://pypi.org/project/geopandas">PyPI</a>,
      <a href="https://github.com/geopandas/geopandas">GitHub</a>
    </th>
    <th>Complete</th>
  </tr>
</table>

## Upstreamed stubs

These stubs were included here in the past and have been moved to typeshed or to the their libraries.

<table>
  <tr>
    <th>Project</th>
    <th>Moved to</th>
    <th>Installation</th>
  </tr>
  <tr>
    <th><a href="https://pypi.org/project/seaborn">seaborn</a></th>
    <th><a href="https://github.com/python/typeshed/tree/main/stubs/seaborn">typeshed</a></th>
    <th><code>pip install types-seaborn</code></th>
  </tr>
</table>
