# Copyright 2021 Canonical Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import os

import charms_openstack.adapters
import charms_openstack.charm


class MagnumDashboardCharm(charms_openstack.charm.OpenStackCharm):
    release = 'rocky'
    name = 'octavia-dashboard'
    packages = ['python3-magnum-ui']
    python_version = 3
    adapters_class = charms_openstack.adapters.OpenStackRelationAdapters
    required_relations = ['dashboard']

    def enable_ui_plugin(self):
        source = '/etc/openstack-dashboard/enabled'
        destination = '/usr/lib/python3/dist-packages/openstack_dashboard/local/enabled'
        for filename in os.listdir(source):
            if "container_infra" in filename:
                src = os.path.join(source, filename)
                dst = os.path.join(destination, filename)
                os.symlink(src, dst)
