# Scryboard

Trading Card Game Playmat

## Running it

In the `frontend` folder run `ng serve`.

Then, in another terminal, go to the `backend` folder run:
```
pipenv run python app.py
```

Open up the website at [localhost:4200](http://localhost:4200/).

## First Time Setup

### Frontend

#### On Windows

If you don't already have _NodeJS_ installed, do so [here](https://nodejs.org/en) (I used 18.18.0 LTS, but anything with version 18 should work). During the installation make sure you check this box:

![Check the Chocolatey box!](readme-images\chocolatey_box.png)

#### On Linux

NodeJS has installation instructions [here](https://nodejs.org/en/download/package-manager/all). Install LTS version 18.x or 20.x

#### On both

Once _NodeJS_ is installed, in your terminal in the `frontend` folder run `npm install`.

Now the frontend should be good to go, read the [README.md](frontend/README.md) there for further info.

### Backend

As the backend uses Python (3), it must first be installed. Download the latest version from [here](https://www.python.org/downloads/).

`pip` should automatically be installed with Python, but you can make sure with the command `pip --version`.

This project uses `pipenv` to manage dependencies. In the backend folder, run the following commands to install pipenv and then use it to install the necessary dependencies:

```
pip install --user pipenv
pipenv install
```

#### I got an error

If you got an error with `pip install pipenv` about externally managed packages, ignore it with `pip install pipenv --break-system-packages`.

If you get error saying no command named `pipenv` found, try changing it to `python -m pipenv`.
