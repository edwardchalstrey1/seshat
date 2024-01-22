# Seshat: Global History Databank

[Seshat](http://seshat-db.com/) was founded in 2011 to bring together the most current and comprehensive body of knowledge about human history in one place.

This repo contains the necessary Django Python code to host the [Seshat](http://seshat-db.com/) website and interact with the backend PostgreSQL database.

## Developers

Follow the steps on [docs/setup](docs/setup.md).

## GitHub workflow

1. Create a new branch from `dev`
2. Test changes locally
3. Merge changes `dev`
4. Also merge changes from `dev` into `azure`
5. Pull changes on Azure VM for others to test
6. Repeat the above until satisfied, then PR `dev` to upsream `dev` branch