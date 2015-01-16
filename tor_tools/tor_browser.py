from selenium import webdriver
from pyvirtualdisplay import Display

class TorBrowser:
  """
  Use selenium with Tor on a headless version
  of firefox.
  """
  def __init__(self):
    self.display = Display(visible=0, size=(800, 600))
    self.display.start()
    self.browser = webdriver.Firefox(self._set_tor_profile())

  def _set_tor_profile(self):
    profile = webdriver.FirefoxProfile()
    profile.set_preference('network.proxy.type', 1)
    profile.set_preference('network.proxy.socks', '127.0.0.1')
    profile.set_preference('network.proxy.socks_port', 9050)
    return profile