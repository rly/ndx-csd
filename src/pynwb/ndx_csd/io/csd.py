from pynwb import register_map
from pynwb.io.core import NWBContainerMapper

from .. import CSD


@register_map(CSD)
class CSDObjectMapper(NWBContainerMapper):

    def __init__(self, spec):
        super().__init__(spec)
        time_from_event_spec = self.spec.get_dataset('time_from_event')
        self.map_spec('event_description', time_from_event_spec.get_attribute('event_description'))
