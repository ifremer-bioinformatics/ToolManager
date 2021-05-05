# =============================================================================
# Tool Directory 
#
# A program to prepare an HTML table listing softwares available on
# a file system.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# (c) 2017-20 Ifremer-Bioinformatics Team
# =============================================================================

import re
import os
from jinja2 import Template

def khtml(args):
    data = {}
    # Read the file and get the infos
    for l in args.info:
        key, value = re.split(r'=', l.rstrip('\n'))
        data[key] = value

    template = open('template/template.html', "r").read()
    webpage = open(os.path.join(args.path, 'index.html'), "w")

    #Load the template and make the rendering
    tm = Template(template)
    msg = tm.render(d=data)
    webpage.write(msg)

    # Close file
    webpage.close()