# Django BBS

Bulletin Board System

![django-version-2.1.5](https://img.shields.io/badge/django-2.1.5-brightgreen.svg)
![python-version-3.7.1](https://img.shields.io/badge/python-v3.7.1-blue.svg)


<br>

## Requirements

### Python Packages

```bash
$ pip install -r requirements.txt
```

<br>

### Set Django SECRET\_KEY

1. Make `.secrets` directory at `ROOT_DIR`

2. Make `base.json` at `/.secrets`

<br>

Form of `base.json`

```json
{
  "SECRET_KEY": "<SECRET_KEY>"
}
```

Input your Django SECRET\_KEY at `<SECRET_KEY>`.  

<br>

### Migrate

```bash
$ python manage.py migrate
```
