# python-stubs

This repository provides stubs for some python packages that do not offer proper type hints and
have no stubs available. It improves language service experience in editors like VSCode by
providing better autocompletion and sometimes better performance.

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/hamdanal/python-stubs /path/to/python-stubs
   ```
2. In VSCode's `settings.json` file, add the stubs path to the appropriate setting:
   1. If using _Pylance_:
      ```json
      "python.analysis.extraPaths": ["/path/to/python-stubs/stubs"]
      ```
   2. If using _ty_:
      ```json
      "ty.configuration": {
        "environment": {
          "extra-paths": ["/path/to/python-stubs/stubs"]
        }
      }
      ```

## Contributing

Contributions of any kind are welcome. Please open an issue or a send pull request.

To set up a development environment:
1. Install `uv`: https://docs.astral.sh/uv/getting-started/installation/
2. Install the project dependencies: `uv sync --frozen`
3. Run `uv run python run.py --help` for more.

## License

This project is licensed under the MIT License.

## List of available stubs

<table>
  <tr>
    <th>Project</th>
    <th>Import name</th>
    <th>Links</th>
    <th>Status</th>
    <th>Tested</th>
  </tr>
  <tr>
    <th>django-netfields</th>
    <th><code>netfields</code></th>
    <th>
      <a href="https://pypi.org/project/django-netfields">PyPI</a>,
      <a href="https://github.com/jimfunk/django-postgresql-netfields">GitHub</a>
    </th>
    <th>Complete</th>
    <th>No</th>
  </tr>
  <tr>
    <th>django-postgres-extra</th>
    <th><code>psqlextra</code></th>
    <th>
      <a href="https://pypi.org/project/django-postgres-extra">PyPI</a>,
      <a href="https://github.com/SectorLabs/django-postgres-extra">GitHub</a>
    </th>
    <th>Incomplete</th>
    <th>No</th>
  </tr>
  <tr>
    <th>pandapower</th>
    <th><code>pandapower</code></th>
    <th>
      <a href="https://pypi.org/project/pandapower">PyPI</a>,
      <a href="https://github.com/e2nIEE/pandapower">GitHub</a>
    </th>
    <th>Incomplete</th>
    <th>Yes</th>
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
    <th><a href="https://pypi.org/project/pyserial">pyserial</a></th>
    <th><a href="https://github.com/python/typeshed/tree/main/stubs/pyserial">typeshed</a></th>
    <th><code>pip install types-pyserial</code></th>
  </tr>
  <tr>
    <th><a href="https://pypi.org/project/netaddr">netaddr</a></th>
    <th><a href="https://github.com/python/typeshed/tree/main/stubs/netaddr">typeshed</a></th>
    <th><code>pip install types-netaddr</code></th>
  </tr>
  <tr>
    <th><a href="https://pypi.org/project/seaborn">seaborn</a></th>
    <th><a href="https://github.com/python/typeshed/tree/main/stubs/seaborn">typeshed</a></th>
    <th><code>pip install types-seaborn</code></th>
  </tr>
  <tr>
    <th><a href="https://pypi.org/project/shapely">shapely</a></th>
    <th><a href="https://github.com/python/typeshed/tree/main/stubs/shapely">typeshed</a></th>
    <th><code>pip install types-shapely</code></th>
  </tr>
  <tr>
    <th><a href="https://pypi.org/project/geopandas">geopandas</a></th>
    <th><a href="https://github.com/python/typeshed/tree/main/stubs/geopandas">typeshed</a></th>
    <th><code>pip install types-geopandas</code></th>
  </tr>
  <tr>
    <th><a href="https://pypi.org/project/pyogrio">pyogrio</a></th>
    <th><a href="https://github.com/python/typeshed/tree/main/stubs/pyogrio">typeshed</a></th>
    <th><code>pip install types-pyogrio</code></th>
  </tr>
</table>
