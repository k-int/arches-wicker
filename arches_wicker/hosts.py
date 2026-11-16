import re
from django_hosts import patterns, host

host_patterns = patterns(
    "",
    host(re.sub(r"_", r"-", r"arches_wicker"), "arches_wicker.urls", name="arches_wicker"),
)
