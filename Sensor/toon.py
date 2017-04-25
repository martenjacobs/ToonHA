"""
Toon van Eneco Utility Gages.
This provides a component for the rebranded Quby thermostat as provided by
Eneco.
"""
import logging

from homeassistant.helpers.entity import Entity
import custom_components.toon as toon_main

_LOGGER = logging.getLogger(__name__)


def setup_platform(hass, config, add_devices, discovery_info=None):
    """Setup sensors."""
    add_devices([
        ToonSensor(hass, 'Gas_current', 'CM3'),
        ToonSensor(hass, 'Gas_today', 'M3'),
        ToonSensor(hass, 'Power_current', 'Watt'),
        ToonSensor(hass, 'Power_today', 'kWh')
    ])
    _toon_main = hass.data[toon_main.TOON_HANDLE]
    for plug in _toon_main.toon.smartplugs:
        add_devices([
            FibaroSensor(hass,
                         '{}_current_power'.format(plug.name),
                         plug.name,
                         'Watt'),
            FibaroSensor(hass,
                         '{}_today_energy'.format(plug.name),
                         plug.name,
                         'kWh')])


class ToonSensor(Entity):
    """Representation of a sensor."""

    def __init__(self, hass, name, unit_of_measurement):
        """Initialize the sensor."""
        self._name = name
        self._state = None
        self._unit_of_measurement = unit_of_measurement
        self.thermos = hass.data[toon_main.TOON_HANDLE]

    @property
    def should_poll(self):
        """Polling required"""
        return True

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def state(self):
        """Return the state of the sensor."""
        return self.thermos.get_data(self.name.lower())

    @property
    def unit_of_measurement(self):
        """Return the unit this state is expressed in."""
        return self._unit_of_measurement

    def update(self):
        """Get the latest data from the sensor."""
        self.thermos.update()


class FibaroSensor(Entity):
    """Representation of a sensor."""

    def __init__(self, hass, name, plug_name, unit_of_measurement):
        """Initialize the sensor."""
        self._name = name
        self._plug_name = plug_name
        self._state = None
        self._unit_of_measurement = unit_of_measurement
        self.toon = hass.data[toon_main.TOON_HANDLE]

    @property
    def should_poll(self):
        """Polling required"""
        return True

    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def state(self):
        """Return the state of the sensor."""
        value = '_'.join(self.name.lower().split('_')[1:])
        return self.toon.get_data(value, self._plug_name)

    @property
    def unit_of_measurement(self):
        """Return the unit this state is expressed in."""
        return self._unit_of_measurement

    def update(self):
        """Get the latest data from the sensor."""
        self.toon.update()
