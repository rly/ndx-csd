# ndx-csd Extension for NWB

This is an NWB extension for storing the results of a Current Source Density analysis on extracellularly recorded
local field potential data in 1, 2, or 3 dimensions. Electrode locations can be marked as being actual electrode
locations or virtual (interpolated) locations.

## Installation

`pip install ndx-csd`

## Usage

```python
import datetime
import numpy as np
from pynwb import NWBHDF5IO, NWBFile

from ndx_csd import CSD

# create a new CSD object
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

# create a new NWBFile, processing module for processed ecephys data, and add the CSD
# object to the ecephys module
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

# write the NWB file
filename = 'test.nwb'
with NWBHDF5IO(filename, mode='w') as io:
    io.write(nwbfile)

# read the NWB file and print the CSD object
with NWBHDF5IO(filename, mode='r', load_namespaces=True) as io:
    read_nwbfile = io.read()
    print(read_nwbfile.processing['ecephys']['CSD'])

```

## TODO

- Add support for non-grid-based electrode locations. Think pixel_mask/manifold.

This extension was created using [ndx-template](https://github.com/nwb-extensions/ndx-template).
