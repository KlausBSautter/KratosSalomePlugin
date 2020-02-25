#  _  __         _          ___       _               ___ _           _
# | |/ /_ _ __ _| |_ ___ __/ __| __ _| |___ _ __  ___| _ \ |_  _ __ _(_)_ _
# | ' <| '_/ _` |  _/ _ (_-<__ \/ _` | / _ \ '  \/ -_)  _/ | || / _` | | ' \
# |_|\_\_| \__,_|\__\___/__/___/\__,_|_\___/_|_|_\___|_| |_|\_,_\__, |_|_||_|
#                                                               |___/
# License: BSD License ; see LICENSE
#
# Main authors: Philipp Bucher (https://github.com/philbucher)
#

# python imports
import unittest, sys, os
from unittest.mock import Mock

# plugin imports
sys.path.append(os.pardir) # required to be able to do "from plugin import xxx"
sys.path.append(os.path.join(os.pardir, "plugin")) # required that the imports from the "plugin" folder work inside the py-modules of the plugin
import sys
https://turlucode.com/mock-python-imports-in-unit-tests/ => for mocking the salome imports!
sys.modules['salome_pluginsmanager'] = Mock()
sys.modules['salome'] = Mock()
sys.modules['salome.smesh'] = Mock()
sys.modules['salome_version'] = Mock()
sys.modules['SMESH'] = Mock()

from plugin import salome_plugins


class TestSalomePlugins(unittest.TestCase):
    def test_initialization(self):
        context = None # should not be needed
        salome_plugins.InitializePlugin(context)


if __name__ == '__main__':
    unittest.main()
