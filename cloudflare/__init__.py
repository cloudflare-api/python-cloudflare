import httplib
import json
import urllib

class CloudFlare( object ):
  def __init__( self, email, token ):
    self.EMAIL = email
    self.TOKEN = token

  class APIError( Exception ):
    def __init__( self, value ):
      self.value = value
    def __str__( self ):
      return self.value

  def callAPI( self, params ):
    a = urllib.urlencode( params )
    b = { 'Content-type': 'www-form-urlencoded', 'Accept': '*/*' }
    req = httplib.HTTPSConnection( 'www.cloudflare.com' )
    req.request( 'POST', '/api_json.html', a, b )
    response = req.getresponse()
    data = response.read()
    try:
      data = json.loads( data )
    except ValueError:
      raise self.APIError( 'JSON parse failed.' )
    if data['result'] == 'error':
      raise self.APIError( data['msg'] )
    return data


  # Stats
  def stats( self, z, interval ):
    return self.callAPI( {
      '@act': 'stats',
      '@z': z,
      '@interval': interval,
      '@tkn': self.TOKEN,
      '@email': self.EMAIL
    } )


  # Load all zones
  def zone_load_multi( self ):
    return self.callAPI( {
      '@act': 'zone_load_multi',
      '@email': self.EMAIL,
      '@tkn': self.TOKEN
    } )


  # Load all DNS records
  def rec_load_all( self, z ):
    return self.callAPI( {
      '@act': 'rec_load_all',
      '@email': self.EMAIL,
      '@tkn': self.TOKEN,
      '@z': z
    } )


  # Zone Check
  def zone_check( self, zones ):
    return self.callAPI( {
      '@act': 'zone_check',
      '@email': self.EMAIL,
      '@tkn': self.TOKEN,
      '@zones': zones
    } )


  # Zone IPs
  def zone_ips( self, z, hours, _class = None, geo = None ):
    if _class is None and geo is None:
      return self.callAPI( {
        '@act': 'zone_ips',
        '@email': self.EMAIL,
        '@tkn': self.TOKEN,
        '@z': z,
        '@hours': hours
      } )
    elif _class is not None and geo is None:
      return self.callAPI( {
        '@act': 'zone_ips',
        '@email': self.EMAIL,
        '@tkn': self.TOKEN,
        '@z': z,
        '@hours': hours,
        '@class': _class
      } )
    elif _class is None and geo is not None:
      return self.callAPI( {
        '@act': 'zone_ips',
        '@email': self.EMAIL,
        '@tkn': self.TOKEN,
        '@z': z,
        '@hours': hours,
        '@geo': geo
      } )
    else:
      return self.callAPI( {
        '@act': 'zone_ips',
        '@email': self.EMAIL,
        '@tkn': self.TOKEN,
        '@z': z,
        '@hours': hours,
        '@class': _class,
        '@geo': geo
      } )


  # IP Lookup
  def ip_lkup( self, ip ):
    return callAPI( {
      '@act': 'ip_lkup',
      '@email': self.EMAIL,
      '@tkn': self.TOKEN,
      '@ip': ip
    } )


  # Security Level
  def sec_lvl( self, z, v ):
    return callAPI( {
      '@act': 'sec_lvl',
      '@email': self.EMAIL,
      '@tkn': self.TOKEN,
      '@z': z,
      '@v': v
    } )


  # Cache Level
  def cache_lvl( self, z, v ):
    return self.callAPI( {
      '@act': 'cache_lvl',
      '@email': self.EMAIL,
      '@tkn': self.TOKEN,
      '@z': z,
      '@v': v
    } )


  # Development Mode
  def devmode( self, z, v ):
    return self.callAPI( {
      '@act': 'devmode',
      '@email': self.EMAIL,
      '@tkn': self.TOKEN,
      '@z': z,
      '@v': v
    } )


  # Full Zone Purge
  def fpurge_ts( self, z, v ):
    return self.callAPI( {
      '@act': 'fpurge_ts',
      '@email': self.EMAIL,
      '@tkn': self.TOKEN,
      '@z': z,
      '@v': v
    } )


  # Grab Zones
  def zone_grab( self, zid ):
    return self.callAPI( {
      '@act': 'zone_grab',
      '@email': self.EMAIL,
      '@tkn': self.TOKEN,
      '@zid': zid
    } )


  # Whitelist IP
  def wl( self, key ):
    return self.callAPI( {
      '@act': 'wl',
      '@email': self.EMAIL,
      '@tkn': self.TOKEN,
      '@key': key
    } )


  # Ban/Blacklist IP
  def ban( self, key ):
    return self.callAPI( {
      '@act': 'ban',
      '@email': self.EMAIL,
      '@tkn': self.TOKEN,
      '@key': key
    } )


  # Set DNS Record
  def rec_set( self, zone, _type, content, name, service_mode ):
    return self.callAPI( {
      '@act': 'rec_set',
      '@email': self.EMAIL,
      '@tkn': self.TOKEN,
      '@zone': zone,
      '@type': _type,
      '@content': content,
      '@name': name
    } )


  # Delete DNS record
  def rec_del( self, zone, name ):
    return self.callAPI( {
      '@act': 'rec_del',
      '@email': self.EMAIL,
      '@tkn': self.TOKEN,
      '@zone': zone,
      '@name': name
    } )


  # A Record Update (DIUP)
  def DIUP( self, ip, hosts ):
    return self.callAPI( {
      '@act': 'DIUP',
      '@email': self.EMAIL,
      '@tkn': self.TOKEN,
      '@ip': ip,
      '@hosts': hosts
    } )


  # Toggle IPv6 support
  def ipv46( self, z, v ):
    return self.callAPI( {
      '@act': 'ipv46',
      '@email': self.EMAIL,
      '@tkn': self.TOKEN,
      '@z': z,
      '@v': v
    } )
