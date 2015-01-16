import requesocks
from tor_utils import proxies

def TorSession():
  session = requesocks.session() 
  session.proxies = proxies 
  return session 
