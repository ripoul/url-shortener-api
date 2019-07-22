<h1 align="center">Welcome to url-shortener-api 👋</h1>

[![Documentation](https://img.shields.io/badge/documentation-yes-brightgreen.svg)](https://github.com/ripoul/url-shortener-api)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://github.com/ripoul/url-shortener-api/blob/master/LICENSE)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)
[![Build Status](https://travis-ci.org/ripoul/url-shortener-api.svg?branch=master)](https://travis-ci.org/ripoul/url-shortener-api)
[![codecov](https://codecov.io/gh/ripoul/url-shortener-api/branch/master/graph/badge.svg)](https://codecov.io/gh/ripoul/url-shortener-api)

> an api to shorten some url

### 🏠 [Homepage](https://github.com/ripoul/url-shortener-api)

The api endpoint is at http://url-shortener.api.ripoul.fr/api/ or https://url-shortener-ripoul.herokuapp.com.
Here some usefull request : 
- `http://url-shortener.api.ripoul.fr/api/providers` to list the available providers
- `http://url-shortener.api.ripoul.fr/api/tinyurl?url=[LONG_URL]` to shorten the url with tinyurl

I've made a web interface. You can find the code [here](https://github.com/ripoul/url-shortener) and the live demo [here](https://url-shortener.ripoul.fr).

## Install

```sh
pip install -r requirements.txt
```

## Usage

```sh
python manage.py runserver
```

If you want all the features, you will need a `.env` file with two items in it : 
- cuttlyAPI -> contains the api key for cuttly
- rebrandlyAPI -> contains the api key for rebrandly

## Run tests

```sh
python manage.py test
```

## Author

👤 **Jules**

* Github: [@ripoul](https://github.com/ripoul)

## 🤝 Contributing

Contributions, issues and feature requests are welcome!<br />Feel free to check [issues page](https://github.com/ripoul/url-shortener-api/issues).

## Show your support

Give a ⭐️ if this project helped you!

## 📝 License

Copyright © 2019 [Jules](https://github.com/ripoul).<br />
This project is [MIT](https://github.com/ripoul/url-shortener-api/blob/master/LICENSE) licensed. 
