import datetime
import numpy as np
from pynwb import NWBHDF5IO, NWBFile
from pynwb.testing import TestCase, remove_test_file, NWBH5IOMixin

from ndx_csd import CSD


class TestCSDConstructor(TestCase):

    def test_constructor_1d_probe(self):
        """Test that the constructor for CSD sets values as expected."""

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

        self.assertEqual(csd.name, 'csd')
        self.assertEqual(csd.description, 'CSD of linear probe')
        self.assertEqual(csd.num_trials, 50)
        self.assertEqual(type(csd.num_trials), np.uint)
        np.testing.assert_array_equal(csd.data, data)
        self.assertEqual(csd.data_unit, 'volts/meters^2')
        np.testing.assert_array_equal(csd.time_from_event, time_from_event)
        self.assertEqual(csd.time_unit, 'seconds')
        self.assertEqual(csd.event_description, 'Stimulus onset')
        np.testing.assert_array_equal(csd.rel_electrode_locations_x, rel_electrode_locations_x)
        self.assertIsNone(csd.rel_electrode_locations_y)
        self.assertIsNone(csd.rel_electrode_locations_z)
        self.assertEqual(csd.location_unit, 'meters')
        self.assertEqual(csd.actual_electrodes, False)
        self.assertEqual(csd.electrodes_reference_frame, '0 is bottom (most inferior) of probe, +x is superior')

    def test_constructor_2d_array(self):
        """Test that the constructor for CSD sets values as expected."""

        num_times = 101
        num_channels_x = 10
        num_channels_y = 3
        data = np.random.rand(num_times, num_channels_x, num_channels_y)
        time_from_event = np.linspace(-1, 1, num=num_times)
        rel_electrode_locations_x = np.linspace(0, 0.002, num=num_channels_x)
        rel_electrode_locations_y = np.linspace(0, 0.01, num=num_channels_y)
        csd = CSD(
            name='csd',
            description='CSD of electrode array',
            num_trials=np.uint(50),
            data=data,
            time_from_event=time_from_event,
            event_description='Stimulus onset',
            rel_electrode_locations_x=rel_electrode_locations_x,
            rel_electrode_locations_y=rel_electrode_locations_y,
            actual_electrodes=False,
            electrodes_reference_frame=('(0, 0) is most inferior, most left electrode of array, +x is superior, +y is '
                                        'right')
        )

        self.assertEqual(csd.name, 'csd')
        self.assertEqual(csd.description, 'CSD of electrode array')
        self.assertEqual(csd.num_trials, 50)
        self.assertEqual(type(csd.num_trials), np.uint)
        np.testing.assert_array_equal(csd.data, data)
        self.assertEqual(csd.data_unit, 'volts/meters^2')
        np.testing.assert_array_equal(csd.time_from_event, time_from_event)
        self.assertEqual(csd.time_unit, 'seconds')
        self.assertEqual(csd.event_description, 'Stimulus onset')
        np.testing.assert_array_equal(csd.rel_electrode_locations_x, rel_electrode_locations_x)
        np.testing.assert_array_equal(csd.rel_electrode_locations_y, rel_electrode_locations_y)
        self.assertIsNone(csd.rel_electrode_locations_z)
        self.assertEqual(csd.location_unit, 'meters')
        self.assertEqual(csd.actual_electrodes, False)
        self.assertEqual(csd.electrodes_reference_frame, ('(0, 0) is most inferior, most left electrode of array, '
                                                          '+x is superior, +y is right'))

    def test_constructor_3d_array(self):
        """Test that the constructor for CSD sets values as expected."""

        num_times = 101
        num_channels_x = 10
        num_channels_y = 3
        num_channels_z = 32
        data = np.random.rand(num_times, num_channels_x, num_channels_y)
        time_from_event = np.linspace(-1, 1, num=num_times)
        rel_electrode_locations_x = np.linspace(0, 0.002, num=num_channels_x)
        rel_electrode_locations_y = np.linspace(0, 0.01, num=num_channels_y)
        rel_electrode_locations_z = np.linspace(0, 0.005, num=num_channels_z)
        csd = CSD(
            name='csd',
            description='CSD of 3D electrode array',
            num_trials=np.uint(50),
            data=data,
            time_from_event=time_from_event,
            event_description='Stimulus onset',
            rel_electrode_locations_x=rel_electrode_locations_x,
            rel_electrode_locations_y=rel_electrode_locations_y,
            rel_electrode_locations_z=rel_electrode_locations_z,
            actual_electrodes=False,
            electrodes_reference_frame=('(0, 0, 0) is most inferior, most left, most posterior electrode of array, '
                                        '+x is superior, +y is right, +z is anterior')
        )

        self.assertEqual(csd.name, 'csd')
        self.assertEqual(csd.description, 'CSD of 3D electrode array')
        self.assertEqual(csd.num_trials, 50)
        self.assertEqual(type(csd.num_trials), np.uint)
        np.testing.assert_array_equal(csd.data, data)
        self.assertEqual(csd.data_unit, 'volts/meters^2')
        np.testing.assert_array_equal(csd.time_from_event, time_from_event)
        self.assertEqual(csd.time_unit, 'seconds')
        self.assertEqual(csd.event_description, 'Stimulus onset')
        np.testing.assert_array_equal(csd.rel_electrode_locations_x, rel_electrode_locations_x)
        np.testing.assert_array_equal(csd.rel_electrode_locations_y, rel_electrode_locations_y)
        np.testing.assert_array_equal(csd.rel_electrode_locations_z, rel_electrode_locations_z)
        self.assertEqual(csd.location_unit, 'meters')
        self.assertEqual(csd.actual_electrodes, False)
        self.assertEqual(csd.electrodes_reference_frame, ('(0, 0, 0) is most inferior, most left, most posterior '
                                                          'electrode of array, +x is superior, +y is right, +z is '
                                                          'anterior'))


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
