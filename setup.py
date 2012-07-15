from distutils.core import setup

setup(
    name='python-cloudflare',
    version='0.1',
    description='Python wrapper for the CloudFlare Client API',
    author='Katie Price',
    author_email='katie.price@geodelab.com',
    url='http://git.eitak.se/python-cloudflare',
    packages=['cloudflare']
    )

package_dir = {'cloudflare': 'lib'}

