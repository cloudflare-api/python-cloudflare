from distutils.core import setup

setup(
    name='python-cloudflare',
    version='0.2',
    description='Python wrapper for the CloudFlare Client API',
    author='kayteh',
    author_email='me@kayteh.com',
    url='http://github.com/eitak-ssim/python-cloudflare',
    packages=['cloudflare']
    )

package_dir = {'cloudflare': 'lib'}

