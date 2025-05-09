# Backend

Run `pipenv run python app.py` to start the backend application in debug mode. By using debug mode, you don't have to restart the app after making changes and you get more detailed error logs.

To check that it is running go to [http://localhost:5000/]().

## Development

All API endpoints will be stored in the `/endpoints` folder. There we can separate them out into multiple files for organization.

## Maintenance

To see what dependencies are outdated run `pipenv update --dry-run`. To actually update them run `pipenv update`. **Please** start the app and test it before committing these changes.

## Testing

Tests are available in the `tests/` folder. To run them run `pipenv run pytest`.
