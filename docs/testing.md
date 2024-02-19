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
    - `--keepdb` ensures you can rerun tests quickly if the setup hasn't changed

## CI

GitHub actions is set up to run on this repo. It uses a custom Docker image that gets built on every push or PR to `dev` if the Dockerfile has changed. See `.github/workflows` and the `Dockerfile`. The tests (`.github/workflows/tests.yml`) and any subsequently introduced workflows should always run on push/PR to `dev`.

To set up pushing the docker image using the GH action workflow, I first did the following:
- Generated a new GitHub token with the `read:packages` and `write:packages` scopes. Under my `Settings > Developer settings > Personal access tokens` (classic token).
- Stored the GitHub token as a secret in the Seshat GitHub repository, `Settings > Secrets`, named `GH_TOKEN`.