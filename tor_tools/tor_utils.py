import requesocks
import os
import time  

proxies = {
  'http': 'socks5://127.0.0.1:9050', 
  'https' : 'socks5://127.0.0.9050'
}

def get_ip():
  """
  get your current ip via the proxy
  """
  s = requesocks.session()
  s.proxies = proxies 
  r = s.get('http://icanhazip.com/')
  return r.content.strip()

def refresh_ip():
  """
  Restart Tor until you get a new ip.
  """
  ip = get_ip()
  new_ip = ip 
  while ip == new_ip:
    os.system('sudo pkill -sighup tor') 
    print ip, new_ip
    new_ip = get_ip()
