# Scryboard

Web-based visualizer for Magic The Gathering

## Running it

If this is your first time using the app, first read through the "First Time Setup" section.

Running this app will require two terminals, one in the `frontend/` folder, and one in `backend/`.

In the `frontend/` folder run `npm run start`.

Then, in the `backend/` terminal run `pipenv run python app.py`.

Finally, open up the website at [localhost:4200](http://localhost:4200/).

Until the physical Scryboard mats are developed, please use the `mat_emulator.py` tool in the `tools/` folder. To use the tool, simply run `pipenv run python mat_emulator.py` from the `tools/` directory.

## First Time Setup

### Frontend

#### On Windows

If you don't already have _NodeJS_ installed, do so [here](https://nodejs.org/en) (I used 18.18.0 LTS, but anything with version 18 should work). During the installation make sure you check the box that says install Chocolatey:

![Check the Chocolatey box!](readme-images\chocolatey_box.png)

#### On Linux

NodeJS has installation instructions [here](https://nodejs.org/en/download/package-manager/all). Install LTS version 18.x or 20.x

#### On both

Once _NodeJS_ is installed, in your terminal in the `frontend/` folder run `npm install`.

Now the frontend should be good to go, read the [README.md](frontend/README.md) there for further info.

### Backend

As the backend uses Python (3), it must first be installed. Download the latest version from [here](https://www.python.org/downloads/).

`pip` should automatically be installed with Python, but you can make sure with the command `pip --version`.

This project uses `pipenv` to manage dependencies. In the backend folder, run the following commands to install pipenv and then use it to install the necessary dependencies:

```
pip install --user pipenv
pipenv install
```

#### Troubleshooting Pipenv errors

If you got an error with `pip install pipenv` about externally managed packages, ignore it with `pip install pipenv --break-system-packages`.

If you get error saying no command named `pipenv` found, try changing it to `python -m pipenv`.

### Developer tools

The `tools/` folder houses the `mat_emulator.py` tool, with its own dependencies. In this folder run `pipenv install`. In case of errors refer to the above _"Troubleshooting Pipenv errors"_ section.

## Testing

Currently unit tests only exist for the backend. To run these, simply go to the `backend/` folder and run `pipenv run pytest`. The tests themselves can be found in `backend/tests`.