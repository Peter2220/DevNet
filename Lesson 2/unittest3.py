import json
import unittest

# Check if the NX-OS (Nexus Switch) version is 9.3(3)
class TestStringMethods(unittest.TestCase):
    def test_version(self):
        switch_version = switch_os()
        self.assertEqual(switch_version, '9.3(3)')

# Read from NX-API_show_version.json file
def switch_os():
    with open('NX-API_show_version.json', 'r') as f:
        show_version_output = json.loads(f.read())
    switch_os = show_version_output['ins_api']['outputs']['output']['body']['nxos_ver_str']
    return switch_os


if __name__ == '__main__':
    unittest.main()
