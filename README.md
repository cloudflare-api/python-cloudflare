# Python-CloudFlare
This is a 1:1 wrapper around the CloudFlare API in Python

## Copying
This software is released under no license. It is free for you to use, steal, sell, break, modify, or really anything else.

## Installing
        sudo python setup.py install

## Using
To call the API wrapper, this has to be done.
        from cloudflare import CloudFlare
        cfapi = CloudFlare(your_email, your_api_key)

All methods are exact copies of the CloudFlare API documentation found <a href='//www.cloudflare.com/docs/client-api.html'>here</a>.
**Please note**, when I say exact copy, I mean EXACT copy. The parameters are in the same order. Any optional parameters can be skipped with `None`.

Updating an A record from this API would look like this...
        result = cfapi.DIUP('8.8.102.112', 'example.com,example.org')
        #=> Returns a dict of what the API returned for that method.

## Support
I will provide support via email (katie.price@geodelab.com) or by Twitter (<a href='//twitter.com/xietak'>@xietak</a>)
