import sys, os
sys.path.insert(0, os.getcwd())
sys.path.insert(0, "plugin")

from unittest.mock import Mock

# https://turlucode.com/mock-python-imports-in-unit-tests/ => for mocking the salome imports!
sys.modules['salome_pluginsmanager'] = Mock()
sys.modules['salome'] = Mock()
sys.modules['salome.smesh'] = Mock()
sys.modules['salome_version'] = Mock()
sys.modules['SMESH'] = Mock()