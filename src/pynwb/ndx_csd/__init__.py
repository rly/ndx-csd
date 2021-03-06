import os
from pynwb import load_namespaces, get_class

# Set path of the namespace.yaml file to the expected install location
ndx_csd_specpath = os.path.join(
    os.path.dirname(__file__),
    'spec',
    'ndx-csd.namespace.yaml'
)

# If the extension has not been installed yet but we are running directly from
# the git repo
if not os.path.exists(ndx_csd_specpath):
    ndx_csd_specpath = os.path.abspath(os.path.join(
        os.path.dirname(__file__),
        '..', '..', '..',
        'spec',
        'ndx-csd.namespace.yaml'
    ))

# Load the namespace
load_namespaces(ndx_csd_specpath)

from .csd import CSD  # noqa: E402,F401
# CSD = get_class('CSD', 'ndx-csd')
from .io import csd as __csd   # noqa: E402,F401
