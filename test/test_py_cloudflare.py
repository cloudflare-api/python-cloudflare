__author__ = 'ccbndh'

from cloudflare import CloudFlare
import unittest


class TestPyCloudFlareClient(unittest.TestCase):

    def setUp(self):
        self.cfapi = CloudFlare('EMAIL', 'API_KEY')

    def test_create_new_record_dns(self):
        self.assertEqual(self.cfapi.rec_new('domain', 'A', 'subdomain', '1.2.3.4')['result'], 'success')

    def test_delete_new_record_dns(self):
        dns_id = self.cfapi.get_rec_id_by_name('domain', 'subdomain')
        self.assertEqual(self.cfapi.rec_delete('domain', dns_id)['result'], 'success')

if __name__ == "__main__":
    unittest.main()