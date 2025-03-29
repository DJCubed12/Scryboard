# Backend

Run `pipenv run py app.py` to start the backend application in debug mode. By using debug mode, you don't have to restart the app after making changes and you get more detailed error logs.

To check that it is running go to [http://localhost:5000/]().

## Development

All API endpoints will be stored in the `/endpoints` folder. There we can separate them out into multiple files for organization.

In `endpoints/examples` you can see some VERY basic examples showing how Flask works. Feel free to add a new endpoint (as simple as a function with the little `@current_app.route` on top) just to play around and get comfortable.

## Maintenance

To see what dependencies are outdated run `pipenv update --dry-run`. To actually update them run `pipenv update`. **Please** start the app and test it before committing these changes.
