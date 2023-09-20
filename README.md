# interview_exercise

This exercise required creating an API and creating a cli wrapper to interact with the api. 

### Django API Setup
```
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

### CLI API Wrapper
```
Usage: cli_api.py [OPTIONS] COMMAND [ARGS]...

  CLI Wrapper for the security API, assigned by Paylocity

Options:
  --help  Show this message and exit.

Commands:
  get   List all Security Features
  post  Add one or more Security Objects

Usage: cli_api.py get [OPTIONS]

  List all Security Features

Options:
  -s, --sort_date  Sorts the results by date
  --help           Show this message and exit.

Usage: cli_api.py post [OPTIONS]

  Add one or more Security Objects

Options:
  -c, --count INTEGER  Number of objects to add
  --help               Show this message and exit.
```
