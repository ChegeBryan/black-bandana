[![Build Status](https://travis-ci.org/ChegeBryan/black-bandana.svg?branch=develop)](https://travis-ci.org/ChegeBryan/black-bandana) [![Coverage Status](https://coveralls.io/repos/github/ChegeBryan/black-bandana/badge.svg?branch=develop)](https://coveralls.io/github/ChegeBryan/black-bandana?branch=develop) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/d806d0ac5d5d4e79aec1b4443dd5a8c2)](https://www.codacy.com/app/ChegeBryan/black-bandana?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=ChegeBryan/black-bandana&amp;utm_campaign=Badge_Grade)
[![Maintainability](https://api.codeclimate.com/v1/badges/562cc17e179a8efb443a/maintainability)](https://codeclimate.com/github/ChegeBryan/black-bandana/maintainability)
# black-bandana
user authentication using JSON Web Tokens in Flask Web API

<p align="center">
  <br>
  <img src="./screenshot.png">
  <a href="https://chegebryan.github.io/black-bandana/UI">UI</a> Hosted with ❤️ at Github pages
</p>

## Getting started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Prerequisites

- python 3.6
- pip3

If you wish to clone the repo please satisfy the requirements in the requirements.txt

## Installing

```
clone the repo to local machine

git clone https://github.com/ChegeBryan/black-bandana.git

pip3 install virtualenv

```
### Create a virtual environment and install requirements
- Navigate to the cloned repo directory and open terminal from there.
- run `virtualenv venv` to create virtual environment with the name `venv`
- activate the virtualenv by `source venv/bin/activate`
- `pip3 install -r requirements.txt` to install app requirements on your virtual environment

### Starting the server
- set APP_SETTING variable `export APP_SETTING=development`
- followed by `python manage.py run`

### Running the tests
- run `pytest` at the app root directory
- run with coverage `pytest --cov=app/tests`

### Built with
- [Flask](http://flask.pocoo.org/docs/1.0/)
- [Flask-RestPlus](https://flask-restplus.readthedocs.io/en/stable/)

### Contributing
Contributions will be highly appreciated, Help and make a pull request and lets build software together.

### Authors
[Chege Brian](https://github.com/ChegeBryan)

## Acknowledgements
Hat tip to self for the passion to learn. 😎😎😎