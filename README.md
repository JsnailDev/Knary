# knary-api

## Prerequisites

To run this project, you need to have the following installed on your computer:

- Python 3.11
- Poetry
- Postgres

## Installation

To install the project dependencies, run the following command in the project directory:

```bash
poetry install
```

Then, duplicate the `env.example` file and rename it as `.env`. Edit the `.env` file with your own configuration settings.

## Usage

To activate the virtualenv, use the following command:

```bash
source .venv/bin/activate
```

To run the project, use the following command:

```bash
uvicorn app.main:app --reload
```

You should see some output on the console.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
