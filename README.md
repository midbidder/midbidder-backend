# midbidder-backend
Backend server for midbidder

## Dependencies
```python
# Creaete virtual env.
python3 -m venv venv/
# Activate virtual env.
source venv/bin/activate
# Run app
python3 app.py
# Deactivate virtual env.
source deactivate
```

## Running Tests and Checkstyle

```python
# Running tests
python3 -m pytest

# Running Checkstyle
python3 -m pycodestyle --ignore=E402,E101 tests app.py

```