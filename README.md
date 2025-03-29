# Scryboard

Trading Card Game Playmat

## Running it

In the `frontend` folder run `ng serve`. Then, in another terminal, go to the `backend` folder run:
```
pipenv run py app.py
```

Open up the website at [localhost:4200](http://localhost:4200/).

## First Time Setup

### Frontend

If you don't already have _NodeJS_ installed, do so [here](https://nodejs.org/en) (I used 18.18.0 LTS, but anything with version 18 should work). During the installation make sure you check this box:

![Check the Chocolatey box!](readme-images\chocolatey_box.png)

Once _NodeJS_ is installed, in your terminal in the `frontend` folder run `npm install`.

Now the frontend should be good to go, read the [README.md](frontend/README.md) there for further info.

### Backend

As the backend uses Python (3), it must first be installed. Download the latest version from [here](https://www.python.org/downloads/).

`pip` should automatically be installed with Python, but you can make sure with the command `pip --version`.

This project uses `pipenv` to manage dependencies. In the backend folder, run the following commands to install pipenv and then use it to install the necessary dependencies:

```
pip install --user pip
pip install --user pipenv
pipenv install
```