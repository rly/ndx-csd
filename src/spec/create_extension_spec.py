# -*- coding: utf-8 -*-

import os.path

from pynwb.spec import NWBNamespaceBuilder, export_spec, NWBGroupSpec, NWBAttributeSpec, NWBDatasetSpec


def main():
    # these arguments were auto-generated from your cookiecutter inputs
    ns_builder = NWBNamespaceBuilder(
        doc="""An NWB extension to add support for storing current source density analysis results""",
        name="""ndx-csd""",
        version="""0.1.0""",
        author=list(map(str.strip, """Ryan Ly""".split(','))),
        contact=list(map(str.strip, """rly@lbl.gov""".split(',')))
    )

    ns_builder.include_type('NWBDataInterface', namespace='core')

    data = NWBDatasetSpec(
        name='data',
        doc='The average current source density aligned to a particular event, in volts/meters^2.',
        dtype='float32',
        dims=(
            ('num_times', 'num_electrodes_x'),
            ('num_times', 'num_electrodes_x', 'num_electrodes_y'),
            ('num_times', 'num_electrodes_x', 'num_electrodes_y', 'num_electrodes_z')
        ),
        shape=(
            (None, None),
            (None, None, None),
            (None, None, None, None)
        ),
        attributes=[
            NWBAttributeSpec(
                name='unit',
                doc="Unit of measurement for data, which is fixed to 'volts/meters^2'.",
                dtype='text',
                value='volts/meters^2'
            )
        ]
    )

    time = NWBDatasetSpec(
        name='time_from_event',
        doc='Timestamps representing time from event onset, in seconds.',
        dtype='float32',
        dims=('num_times', ),
        shape=(None, ),
        attributes=[
            NWBAttributeSpec(
                name='unit',
                doc="Unit of measurement for time_from_event, which is fixed to 'seconds'.",
                dtype='text',
                value='seconds'
            ),
            NWBAttributeSpec(
                name='event_description',
                doc='Description of what a time value of 0 represents, i.e., what event is the CSD aligned to.',
                dtype='text',
            ),
        ]
    )

    locs_unit = NWBAttributeSpec(
        name='unit',
        doc="Unit of measurement for coordinate values, which is fixed to 'meters'.",
        dtype='text',
        value='meters'
    )

    rel_electrode_locations_x = NWBDatasetSpec(
        name='rel_electrode_locations_x',
        doc=("X-axis coordinates of CSD, relative to a 'reference_frame', in meters."),
        dtype='float32',
        dims=(
            ('num_electrodes_x', )
        ),
        shape=(
            (None, ),
        ),
        quantity='?',
        attributes=[locs_unit],
    )

    rel_electrode_locations_y = NWBDatasetSpec(
        name='rel_electrode_locations_y',
        doc=("Y-axis coordinates of CSD, relative to a 'reference_frame', in meters."),
        dtype='float32',
        dims=(
            ('num_electrodes_y', )
        ),
        shape=(
            (None, ),
        ),
        quantity='?',
        attributes=[locs_unit],
    )

    rel_electrode_locations_z = NWBDatasetSpec(
        name='rel_electrode_locations_z',
        doc=("Z-axis coordinates of CSD, relative to a 'reference_frame', in meters"),
        dtype='float32',
        dims=(
            ('num_electrodes_z', )
        ),
        shape=(
            (None, ),
        ),
        quantity='?',
        attributes=[locs_unit],
    )

    csd = NWBGroupSpec(
        neurodata_type_def='CSD',
        neurodata_type_inc='NWBDataInterface',
        doc=('Results of a current source density (CSD) analysis.'),
        attributes=[
            NWBAttributeSpec(
                name='description',
                doc='Description of the current source density analysis, including how it was computed.',
                dtype='text'
            ),
            NWBAttributeSpec(
                name='num_trials',
                doc='Number of trials used to compute the average CSD.',
                dtype='uint8'
            ),
            NWBAttributeSpec(
                name='actual_electrodes',
                doc=("Whether the electrode locations provided correspond to actual electrode locations as opposed to "
                     "virtual electrode locations (where interpolation is used to compute the CSD at the virtual "
                     "locations)."),
                dtype='bool',
                default_value=False
            ),
            NWBAttributeSpec(
                name='electrodes_reference_frame',
                doc=("Description of what an electrode location of 0 (or (0,0) or (0,0,0)) represents, e.g., most "
                     "superior point of a linear probe, or most posterior and most left point of a 2D array. This "
                     "value should also describe what a positive value in each dimension represents, e.g., +x is "
                     "superior."),
                dtype='text'
            )
        ],
        datasets=[data, time, rel_electrode_locations_x, rel_electrode_locations_y, rel_electrode_locations_z]
    )

    new_data_types = [csd]

    # export the spec to yaml files in the spec folder
    output_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'spec'))
    export_spec(ns_builder, new_data_types, output_dir)


if __name__ == "__main__":
    # usage: python create_extension_spec.py
    main()
