import datetime
import numpy as np
from pynwb import NWBHDF5IO, NWBFile
from pynwb.testing import TestCase, remove_test_file, NWBH5IOMixin

from ndx_csd import CSD


class TestCSDRoundtrip(TestCase):
    """Simple roundtrip test for CSD."""

    def setUp(self):
        self.nwbfile = NWBFile(
            session_description='session_description',
            identifier='identifier',
            session_start_time=datetime.datetime.now(datetime.timezone.utc)
        )
        self.path = 'test.nwb'

    def tearDown(self):
        remove_test_file(self.path)

    def test_roundtrip(self):
        """
        Add a CSD to an "ecephys" processing module in the NWBFile, write it to file, read the file, and test that the
        CSD from the file matches the original CSD.
        """

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
            electrodes_reference_frame='0 is bottom of probe, +x is superior'
        )

        ecephys_module = self.nwbfile.create_processing_module(
            name='ecephys',
            description='processed ecephys data'
        )
        ecephys_module.add(csd)

        with NWBHDF5IO(self.path, mode='w') as io:
            io.write(self.nwbfile)

        with NWBHDF5IO(self.path, mode='r', load_namespaces=True) as io:
            read_nwbfile = io.read()
            self.assertContainerEqual(csd, read_nwbfile.processing['ecephys']['CSD'])


class TestCSDRoundtripPyNWB(NWBH5IOMixin, TestCase):
    """Complex, more complete roundtrip test for TetrodeSeries using pynwb.testing infrastructure.

    The CSD will be placed inside nwbfile/acquisition.
    """

    def setUpContainer(self):
        """ Return the test CSD to read/write """
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
            electrodes_reference_frame='0 is bottom of probe, +x is superior'
        )
        return csd

    def addContainer(self, nwbfile):
        """Add the test CSD to the given NWBFile."""
        ecephys_module = nwbfile.create_processing_module(
            name='ecephys',
            description='processed ecephys data'
        )
        ecephys_module.add(self.container)

    def getContainer(self, nwbfile):
        """Get the test CSD to the given NWBFile."""
        return nwbfile.processing['ecephys']['CSD']
