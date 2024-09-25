# Flask Project

How to install this project:

## Clonning from repo

Using Http

```bash
git clone https://github.com/akmalluthfi/flask-board.git
```

Using SSH

```bash
git clone git@github.com:akmalluthfi/flask-board.git
```

## Setup Project

Setup a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Download dependencies

```bash
pip install -r requirements.txt
```

Copy .env_sample

> Setting your environment

```bash
cp .env_sample .env
```

Generate secret key

```python
import secrets
secrets.token_hex()
```

Initialize the Database

```bash
flask --app board init-db
```

## Run program

```bash
flask --app board run
```
