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

import glob
import os

import charms_openstack.adapters
import charms_openstack.charm


class MagnumDashboardCharm(charms_openstack.charm.OpenStackCharm):
    release = 'ussuri'
    name = 'magnum-dashboard'
    packages = ['python3-magnum-ui']
    python_version = 3
    adapters_class = charms_openstack.adapters.OpenStackRelationAdapters
    required_relations = ['dashboard']
    # Use API version 1.9 for magnum (LP: #1998509)
    local_settings = """
OPENSTACK_API_VERSIONS['container-infra'] = 1.9
"""

    def enable_ui_plugin(self):
        source = '/etc/openstack-dashboard/enabled'
        destination = \
            '/usr/lib/python3/dist-packages/openstack_dashboard/local/enabled'
        plugin_files = glob.glob('{}/*_container_infra_*.py'.format(source))
        for plugin_file in plugin_files:
            dest_file = os.path.join(
                destination, os.path.basename(plugin_file))
            try:
                os.symlink(plugin_file, dest_file)
            except FileExistsError:
                # plugin file is already enabled
                continue


class MagnumDashboardCharmXena(MagnumDashboardCharm):
    release = 'xena'
    # magnum-ui's default API version is 1.10, there is no need to override it
    # (LP: #1998509)
    local_settings = ""
