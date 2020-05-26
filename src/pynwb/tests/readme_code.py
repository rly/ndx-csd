import datetime
import numpy as np
from pynwb import NWBHDF5IO, NWBFile

from ndx_csd import CSD


import datetime
import numpy as np
from pynwb import NWBHDF5IO, NWBFile

from ndx_csd import CSD


num_times = 101
num_channels = 32
data = np.random.rand(num_times, num_channels)
time_from_event = np.linspace(-1, 1, num=num_times)
rel_electrode_locations_x = np.linspace(0, 0.002, num=num_channels)
csd = CSD(
    name='csd',
    description='CSD of linear probe',
    num_trials=np.uint(50),
    data=data,
    time_from_event=time_from_event,
    event_description='Stimulus onset',
    rel_electrode_locations_x=rel_electrode_locations_x,
    actual_electrodes=False,
    electrodes_reference_frame='0 is bottom (most inferior) of probe, +x is superior'
)


nwbfile = NWBFile(
    session_description='session_description',
    identifier='identifier',
    session_start_time=datetime.datetime.now(datetime.timezone.utc)
)
ecephys_module = nwbfile.create_processing_module(
    name='ecephys',
    description='processed ecephys data'
)
ecephys_module.add(csd)

filename = 'test.nwb'
with NWBHDF5IO(filename, mode='w') as io:
    io.write(nwbfile)

with NWBHDF5IO(filename, mode='r', load_namespaces=True) as io:
    read_nwbfile = io.read()
    print(read_nwbfile.processing['ecephys']['CSD'])
