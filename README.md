# UNDER CONSTRUCTION

![](https://media.giphy.com/media/3o7btQ0NH6Kl8CxCfK/giphy.gif)

# Kratos Salome Plugin
[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](LICENSE) [![Github CI](https://github.com/philbucher/KratosSalomePlugin/workflows/Plugin%20CI/badge.svg)](https://github.com/philbucher/KratosSalomePlugin/actions) [![Codacy Badge](https://api.codacy.com/project/badge/Grade/6a94f3a9a36b409285fe6c27d8adf9d9)](https://www.codacy.com?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=philbucher/KratosSalomePlugin&amp;utm_campaign=Badge_Grade)

Plugin for the [SALOME platform](https://www.salome-platform.org/) with which it can be used as preprocessor for the finite element programm [KratosMultiphysics](https://github.com/KratosMultiphysics/Kratos).

**Note:** This plugin is currently work in progress. Furthermore it is more research oriented, which means that the user has to have more knowledge of Kratos itself.
For a more consolidated solution please check the [GiD interface](https://github.com/KratosMultiphysics/GiDInterface).

**How does it work?**
This plugin extends the Salome GUI by using the python plugin functionalities, see the [docs](https://docs.salome-platform.org/9/gui/GUI/using_pluginsmanager.html#). It is purely python based, which means that Salome does not have to be compiled. It is sufficient to download the binaries provided by Salome and set up the plugin by following the instructions in the next section.
The plugin works with meshes created in the *Mesh* module of Salome.

**Minimum supported version**
The oldest supported version is Salome 9.3. Check the developers readme for details.

For more information check the [Documentation](documentation)

## Setup
  - Get Salome from <https://www.salome-platform.org/>. Usually it is enough to download and unpack it. For more information check the [installation guide](documentation/install_salome).

  - Get the plugin by cloning this repo.

  - Set the environment variables for using the plugin:
    - _Windows_
        Add an [environment variable](https://www.computerhope.com/issues/ch000549.htm) named`SALOME_PLUGINS_PATH` pointing to the `plugin` directory of where the code was cloned to.
        E.g. `C:\Users\<Username>\KratosSalomePlugin\plugin`

    - _Linux_
        Add an environment variable named`SALOME_PLUGINS_PATH` pointing to the `plugin` directory of where the code was cloned to.
        E.g. `export SALOME_PLUGINS_PATH="${HOME}/KratosSalomePlugin/plugin"`\
        Use `echo SALOME_PLUGINS_PATH="${HOME}/KratosSalomePlugin/plugin" >> ~/.bashrc` to directly add it to your `bashrc`

  - In Salome: Click `Tools/Plugin/Kratos Multiphysics` in order to load the plugin.\
      Also a small icon with which the plugin can be loaded appears in the menu list: <img src="plugin/utilities/kratos_logo.png" width="24">
      <img src="plugin/utilities/load_plugin.png" width="400">

## Quick start
how to start ...


## Usage

## Examples
Examples for the plugin can be found under *plugin/applications/APP_NAME/examples*.
They can also be loaded inside the plugin after loading the corresponding application.

## Contributors

## Acknowledgements
