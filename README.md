# USM Games Launcher

This launcher was initially made for the Nerdonomicon 2019, Valparaíso, Chile to launch the games made by members of our initiative.

## Build

To build the launcher into an .exe file run the following command:

````
pyinstaller cli.py \
--add-data games.json;. \
--add-data usmglauncher/templates/index.html;usmglauncher/templates \
--add-data usmglauncher/static/*.css;usmglauncher/static/ \
--add-data usmglauncher/static/Images/*;usmglauncher/static/Images
````
