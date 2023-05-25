# externalio
An example of adding dascore IO support in an external package using plug-ins

To create your own support for external dascore IO support, do the following:

1. Add your implementation in externalio.core. See [dascore's adding new project support](https://dascore.org/contributing/new_format.html) for more details.
2. Rename this package from externalio to your io format name and update the description in `__init__.py`
3. Look through the pyproject.toml and rename all instances of externalio and follow comment instructions
4. (best practice) create a directory called "tests" and add some tests/test files.

Now, if you have done everything correctly, you should be able to install your package with pip (`pip install .` if in the package directory) and dascore will automatically recognize your format without importing this package.
Try it via:

```python
import dascore as dc

patch = dc.spool("path/to/myfile")[0]

```
