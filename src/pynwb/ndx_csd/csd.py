import numpy as np
from hdmf.utils import docval, getargs
from pynwb import register_class
from pynwb.core import NWBDataInterface


@register_class('CSD', 'ndx-csd')
class CSD(NWBDataInterface):
    __nwbfields__ = ('description',
                     'num_trials',
                     'data',
                     'time_from_event',
                     'event_description',
                     'rel_electrode_locations_x',
                     'rel_electrode_locations_y',
                     'rel_electrode_locations_z',
                     'electrodes_reference_frame',
                     'actual_electrodes')

    # these are fixed values in the spec
    __time_from_event_unit = 'seconds'
    __data_unit = 'volts/meters^2'
    __rel_electrode_locations_unit = 'meters'

    # these docval args were modified from the CSD.__init__.__docval__ generated by get_class
    @docval(
        {'doc': 'The name of this CSD object.',
         'name': 'name',
         'type': str},
        {'doc': 'Description of the current source density analysis, '
                'including how it was computed.',
         'name': 'description',
         'type': str},
        {'doc': 'Number of trials used to compute the average CSD.',
         'name': 'num_trials',
         'type': np.unsignedinteger},
        {'doc': 'The average current source density aligned to a particular '
                'event, in volts/meters^2.',
         'name': 'data',
         'shape': [[None, None],
                   [None, None, None],
                   [None, None, None, None]],
         'type': ('data', 'array_data')},
        {'doc': 'Timestamps representing time from event onset, in seconds.',
         'name': 'time_from_event',
         'shape': [None],
         'type': ('data', 'array_data')},
        {'doc': 'Description of what a time value of 0 represents, i.e., '
                'what event is the CSD aligned to.',
         'name': 'event_description',
         'type': str},
        {'doc': 'Description of what a value of 0 (or (0,0) or (0,0,0)) '
                'represents, e.g., top (most superior point) of a linear '
                'probe, or most posterior and most left point of a 2D array. '
                'This value should also describe what a positive value in '
                'each dimension represents, e.g., +x is superior.',
         'name': 'electrodes_reference_frame',
         'type': str},
        {'default': None,
         'doc': "X-axis coordinates of CSD, relative to the "
                "'electrodes_reference_frame', in meters.",
         'name': 'rel_electrode_locations_x',
         'shape': [None],
         'type': ('data', 'array_data')},
        {'default': None,
         'doc': "Y-axis coordinates of CSD, relative to the "
                "'electrodes_reference_frame', in meters.",
         'name': 'rel_electrode_locations_y',
         'shape': [None],
         'type': ('data', 'array_data')},
        {'default': None,
         'doc': "Z-axis coordinates of CSD, relative to the "
                "'electrodes_reference_frame', in meters.",
         'name': 'rel_electrode_locations_z',
         'shape': [None],
         'type': ('data', 'array_data')},
        {'default': False,
         'doc': 'Whether the electrode locations provided correspond to '
                'actual electrode locations as opposed to virtual electrode '
                'locations (where interpolation is used to compute the CSD '
                'at the virtual locations).',
         'name': 'actual_electrodes',
         'type': bool})
    def __init__(self, **kwargs):
        super().__init__(kwargs['name'])

        description, num_trials, data = getargs('description', 'num_trials', 'data', kwargs)
        time_from_event, event_description = getargs('time_from_event', 'event_description', kwargs)
        actual_electrodes, electrodes_reference_frame = getargs('actual_electrodes', 'electrodes_reference_frame',
                                                                kwargs)
        rel_electrode_locations_x, rel_electrode_locations_y, rel_electrode_locations_z = getargs(
            'rel_electrode_locations_x', 'rel_electrode_locations_y', 'rel_electrode_locations_z', kwargs)
        self.description = description
        self.num_trials = num_trials
        self.data = data
        self.time_from_event = time_from_event
        self.event_description = event_description
        self.actual_electrodes = actual_electrodes
        self.electrodes_reference_frame = electrodes_reference_frame
        self.rel_electrode_locations_x = rel_electrode_locations_x
        self.rel_electrode_locations_y = rel_electrode_locations_y
        self.rel_electrode_locations_z = rel_electrode_locations_z

    @property
    def time_unit(self):
        return self.__time_from_event_unit

    @property
    def data_unit(self):
        return self.__data_unit

    @property
    def location_unit(self):
        return self.__rel_electrode_locations_unit
