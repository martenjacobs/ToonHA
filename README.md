# Toon Home Assistant component

The toon component platform can be used to control your Toon thermostat. It uses the toonlib library
by Costas Tyfoxylos (https://github.com/costastf/toonlib). This component adds a climate device for
your Toon thermostat and sensors for power and gas consumption..

Install the files
===

On your Home Assistant instance, go to \<config directory\>/custom_components. Create a folder named
climate and a folder named sensor, if they don't already exist. Now copy the files:
```
toon.py ---> <config directory>/custom_components
Sensor/toon.py ---> <config directory>/custom_components/sensor
Climate/toon.py ---> <config directory>/custom_components/climate
```
Configuration
===

To add Toon to Home Assistant, add the following to your configuration.yaml file:
```
# Example configuration.yaml entry
toon:
    username: YOUR_USERNAME
    password: YOUR_PASSWORD
```
- username (Required): Username for Mijn Eneco.
- password (Required): Password for Mijn Eneco.