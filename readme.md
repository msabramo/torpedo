# torpedo

A simplified interface for creating session and browser objects on top of `Tor`.

## Requirements

On Mac OS X

```bash
brew install tor phantomjs
```

On Ubuntu 

```bash
sudo apt-get instal tor phantomjs
```

## Install
```
pip install torpedo
```

## Tests
```
git clone https://github.com/abelsonlive/torpedo.git
cd torpedo && nosetests
```

## Examples:

- A `requests.Session` object:

```python
import torpedo

s = torpedo.session()
s.get('http://example.com')
```

- A `selenium.webdriver` headless browser powered by `PhantomJS`:

```python
import torpedo 

b = torpedo.headless()
b.get('http://example.com')
```

- Utilities for getting and resetting your ip address:

```python
import torpedo

print torpedo.get_ip()
torpedo.refresh_ip()
print torpedo.get_ip()
``` 