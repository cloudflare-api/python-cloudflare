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
        req = httplib.HTTPSConnection( 'www.cloudflare.com' )
        req.request( 'GET', '/api_json.html?'+params )
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
        return self.callAPI( "a=%s&email=%s&tkn=%s&z=%z&interval=%z" % ( 'stats', self.EMAIL, self.TOKEN, z, interval ) )


    # Load all zones
    def zone_load_multi( self ):
        return self.callAPI( "a=%s&email=%s&tkn=%s" % ( 'zone_load_multi', self.EMAIL, self.TOKEN ) )


    # Load all DNS records
    def rec_load_all( self, z ):
        return self.callAPI( "a=%s&email=%s&tkn=%s&z=%s" % ( 'rec_load_all', self.EMAIL, self.TOKEN, z ) )

    # Zone Check
    def zone_check( self, zones ):
        return self.callAPI( "a=%s&email=%s&tkn=%s&zs=%s" % ( 'zone_check', self.EMAIL, self.TOKEN, zones ) )

    # Zone IPs
    def zone_ips( self, z, hours, _class = None, geo = None ):
        if _class is None and geo is None:
            return self.callAPI( "a=%s&email=%s&tkn=%s&z=%s&hours=%s" % ( 'zone_ips', self.EMAIL, self.TOKEN, z, hours ) )
        elif _class is not None and geo is None:
            return self.callAPI( "a=%s&email=%s&tkn=%s&z=%s&hours=%s&class=%s" % ( 'zone_ips', self.EMAIL, self.TOKEN, z, hours, _class ) )
        elif _class is None and geo is not None:
            return self.callAPI( "a=%s&email=%s&tkn=%s&z=%s&hours=%s&geo=%s" % ( 'zone_ips', self.EMAIL, self.TOKEN, z, hours, geo ) )
        else:
            return self.callAPI( "a=%s&email=%s&tkn=%s&z=%s&hours=%s&class=%s&geo=%s" % ( 'zone_ips', self.EMAIL, self.TOKEN, z, hours, _class, geo ) )


    # IP Lookup
    def ip_lkup( self, ip ):
        return self.callAPI( "a=%s&email=%s&tkn=%s&ip=%s" % ( 'ip_lkup', self.EMAIL, self.TOKEN, ip ) )


    # Security Level
    def sec_lvl( self, z, v ):
        return self.callAPI( "a=%s&email=%s&tkn=%s&z=%s&v=%s" % ( 'sec_lvl', self.EMAIL, self.TOKEN, z, v ) )


    # Cache Level
    def cache_lvl( self, z, v ):
        return self.callAPI( "a=%s&email=%s&tkn=%s&z=%s&v=%s" % ( 'cache_lvl', self.EMAIL, self.TOKEN, z, v ) )


    # Development Mode
    def devmode( self, z, v ):
        return self.callAPI( "a=%s&email=%s&tkn=%s&z=%s&v=%s" % ( 'devmode', self.EMAIL, self.TOKEN, z, v ) )



    # Full Zone Purge
    def fpurge_ts( self, z, v ):
        return self.callAPI( "a=%s&email=%s&tkn=%s&z=%s&v=%s" % ( 'fpurge_ts', self.EMAIL, self.TOKEN, z, v ) )


    # Grab Zones
    def zone_grab( self, zid ):
        return self.callAPI( "a=%s&email=%s&tkn=%s&zid=%s" % ( 'zone_grab', self.EMAIL, self.TOKEN, zid ) )


    # Whitelist IP
    def wl( self, key ):
        return self.callAPI( "a=%s&email=%s&tkn=%s&key=%s" % ( 'wl', self.EMAIL, self.TOKEN, key ) )


    # Ban/Blacklist IP
    def ban( self, key ):
        return self.callAPI( "a=%s&email=%s&tkn=%s&key=%s" % ( 'ban', self.EMAIL, self.TOKEN, key ) )


    # Create new DNS Record
    def rec_new( self, zone, _type, content, name, service_mode ):
        fmt = "a=%s&email=%s&tkn=%s&z=%s&type=%s&content=%s&name=%s&service_mode=%s&ttl=1"
        values = ('rec_new', self.EMAIL, self.TOKEN, zone, _type, content, name, service_mode)
        return self.callAPI( fmt % values )


    # Delete DNS record
    def rec_delete( self, zone, name ):
        return self.callAPI( "a=%s&email=%s&tkn=%s&z=%s&name=%s" % ( 'rec_delete', self.EMAIL, self.TOKEN, zone, name ) )


    # Edit an existing record
    def rec_edit( self, z, _type, _id, name, content ):
        fmt = "a=%s&tkn=%s&id=%s&email=%s&z=%s&type=%s&name=%s&content=%s&ttl=1"
        return self.callAPI( fmt % ( 'rec_edit', self.TOKEN, _id, self.EMAIL, z, _type, name, content))


    # Toggle IPv6 support
    def ipv46( self, z, v ):
        return self.callAPI( "a=%s&email=%s&tkn=%s&z=%s&v=%s" % ( 'ipv46', self.EMAIL, self.TOKEN, z, v ) )


    # Single file purge DROP-IN
    def fpurge_whatever( self, z, v ):
        raise NotImplemented
        #return self.callAPI( "a=%s&email=%s&tkn=%s&z=%s&v=%s" % ( 'fpurge_whatever', self.EMAIL, self.TOKEN, z, v ) )
