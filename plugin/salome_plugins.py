#  _  __         _          ___       _               ___ _           _
# | |/ /_ _ __ _| |_ ___ __/ __| __ _| |___ _ __  ___| _ \ |_  _ __ _(_)_ _
# | ' <| '_/ _` |  _/ _ (_-<__ \/ _` | / _ \ '  \/ -_)  _/ | || / _` | | ' \
# |_|\_\_| \__,_|\__\___/__/___/\__,_|_\___/_|_|_\___|_| |_|\_,_\__, |_|_||_|
#                                                               |___/
# License: BSD License ; see LICENSE
#
# Main authors: Philipp Bucher (https://github.com/philbucher)
#

'''
This is the file that is detected by salome in order to load the plugin
Do not rename or move this file!
Check "salome_pluginsmanager.py" for more information
'''

import os
import sys
import logging
import logging.handlers

logger_level = 2 # default value: 0

logger_levels = { 0 : logging.WARNING,
                  1 : logging.INFO,
                  2 : logging.DEBUG }


root_logger = logging.getLogger()
root_logger.setLevel(logger_levels[logger_level])
root_logger.handlers.clear()

ch = logging.StreamHandler()
root_logger.addHandler(ch)

from utilities.utils import GetAbsPathInPlugin
fh = logging.handlers.RotatingFileHandler(os.path.join(GetAbsPathInPlugin(), "../plugin.log"), maxBytes=5*1024*1024, backupCount=1)
formatter = logging.Formatter("%(asctime)s | %(name)s | %(levelname)s : %(message)s", "%Y-%m-%d %H:%M:%S")
fh.setFormatter(formatter)

root_logger.addHandler(fh)

logger = logging.getLogger(__name__)
logger.debug('loading "salome_plugins"')


def InitializePlugin(context):
    """This is the main function for initializing the plugin
    The functions used must be declared inside this function, otherwise they are not available
    when the plugin is being loaded inside of Salome
    """

    ### settings for development/debugging
    reinitialize_data_handler = True # default value: False
    reload_modules = True # default value: False

    # python imports
    import os
    import sys
    import logging
    logger = logging.getLogger(__name__)

    # plugin imports
    from utilities import utils
    from module_reload_order import MODULE_RELOAD_ORDER

    ### functions used in the plugin ###
    def ReloadModules():
        """Force reload of the modules
        This way Salome does not have to be reopened
        when something in the modules is changed
        """

        logger.debug("Starting to reload modules")

        for module_name in MODULE_RELOAD_ORDER:
            the_module = __import__(module_name, fromlist=[module_name[-1]])

            if sys.version_info < (3, 0): # python 2
                reload(the_module)
            elif sys.version_info >= (3, 4): # python >= 3.4
                import importlib
                importlib.reload(the_module)
            else: # python > 2 and <= 3.3
                # this variant is not strictly necessary, since salome uses either py2.7 (Salome 8) or py 3.6 (Salome 9)
                import imp
                imp.reload(the_module)

        # check the list
        # Note: performing the checks after reloading, this way Salome does not have to be closed for changing the list
        for module_name in MODULE_RELOAD_ORDER:
            if MODULE_RELOAD_ORDER.count(module_name) > 1:
                raise Exception('Module "{}" exists multiple times in the module reload order list!'.format(module_name))

        for module_name in utils.GetPythonModulesInDirectory(utils.GetPluginPath()):
            if module_name not in MODULE_RELOAD_ORDER and module_name != "salome_plugins":
                raise Exception('The python file "{}" was not added to the list for reloading modules!'.format(module_name))

        logger.debug("Successfully reloaded modules")


    ### initializing the plugin ###
    logger.debug("Starting to initialize plugin")

    if reload_modules:
        ReloadModules()

    logger.debug("Successfully initialized plugin")

    # message saying that it is under development
    info_msg  = 'This Plugin is currently under development and not fully operational yet.\n'
    info_msg += 'Please check "https://github.com/philbucher/KratosSalomePlugin" again at a later time.\n'
    info_msg += 'For further questions / requests please open an issue or contact "philipp.bucher@tum.de" directly.'

    QMessageBox.warning(None, 'Under Development', info_msg) # for some reason works without importing "QMessageBox". not going to be investigated since temp solution


### Registering the Plugin in Salome ###

fct_args = [
    'Kratos Multiphysics',
    'Starting the plugin for Kratos Multiphysics',
    InitializePlugin]

import salome_pluginsmanager
import utilities.salome_utilities as salome_utils

if salome_utils.GetVersion() >= (9,3):
    from utilities.utils import GetAbsPathInPlugin
    from qtsalome import QIcon
    icon_file = GetAbsPathInPlugin("utilities","kratos_logo.png")
    fct_args.append(QIcon(icon_file))

salome_pluginsmanager.AddFunction(*fct_args)
