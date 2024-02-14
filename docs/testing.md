# Testing

## Running tests locally

**Pre-reqs:**
- Activate your project python environment
- Install test packages
    ```
        pip install -r requirements/tests.txt
    ```

**Running the tests:**
1. Make sure the Seshat repo root directory is in your PYTHONPATH
    ```
        export PYTHONPATH="${PYTHONPATH}:/path/to/seshat"
    ```
2. Run tests for apps
    ```
        python manage.py test <app name> --keepdb
    ```
    - Where `<app name>` is e.g. `seshat.apps.core` (or leave this off to run all tests)
    - `--keepdb` if you haven't changed the setup