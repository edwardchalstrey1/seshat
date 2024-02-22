# Seshat: Global History Databank

[Seshat](http://seshat-db.com/) was founded in 2011 to bring together the most current and comprehensive body of knowledge about human history in one place.

This repo contains the necessary Django Python code to host the [Seshat](http://seshat-db.com/) website and interact with the backend PostgreSQL database.

## Developers

Follow the steps on [docs/setup](docs/setup.md).

## GitHub process

1. Create a new branch from `dev`
2. Test changes locally
3. Test changes on Azure VM set up with Pulumi if needed (see [Azure Setup](docs/setup.md)).
    - ATI VMs are set up currently under the `Sustainable Scholarly Communities around Data and Software` subscription
4. Merge branch into `dev` on this fork
5. Repeat the above until satisfied, then PR `dev` to upstream `dev` branch

## Tests and checks

On this fork, currently GH actions is set up to run django tests for the following apps when pushing or PR-ing to the `dev` branch:
- Core

See [docs/testing](docs/testing.md) on how to run locally.