# Publishing to Dev-PyPI

Follow these steps to publish the packages to a dev PyPI instance:

## Prerequisites

1. Install build and twine:

```bash
pip install build twine
```

2. Configure your dev-pypi credentials in `~/.pypirc`:

```
[distutils]
index-servers =
    dev-pypi

[dev-pypi]
repository = https://test.pypi.org/legacy/
username = your_username
password = your_password
```

## Publishing hello-world

```bash
cd hello-world
python -m build
twine upload --repository dev-pypi dist/*
```

## Publishing many-hellos

```bash
cd many-hellos
python -m build
twine upload --repository dev-pypi dist/*
```

## Testing Installation from Dev-PyPI

```bash
# Install the hello-world package from dev-pypi
pip install --index-url https://test.pypi.org/simple/ hello-world

# Install the many-hellos package from dev-pypi
pip install --index-url https://test.pypi.org/simple/ many-hellos
```
