# Seshat: Global History Databank

[Seshat](http://seshat-db.com/) was founded in 2011 to bring together the most current and comprehensive body of knowledge about human history in one place.

This repo contains the necessary Django Python code to host the [Seshat](http://seshat-db.com/) website and interact with the backend PostgreSQL database.

## Developers

Follow the steps on [docs/setup](docs/setup.md).

## GitHub workflow

1. Create a new branch from `dev`
2. Test changes locally
3. Checkout branch on changes on Azure VM and test there (see [Azure Setup](docs/setup.md#azure-setup)).
    - ATI VM is set up currently under the `Sustainable Scholarly Communities around Data and Software` subscription
4. Merge branch into `dev` on this fork
5. Repeat the above until satisfied, then PR `dev` to upstream `dev` branch