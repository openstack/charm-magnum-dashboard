# Overview

This subordinate charm provides the Magnum Dashboard plugin for use with the OpenStack Dashboard.

# Usage

Example minimal deploy:

    juju deploy openstack-dashboard --config openstack-origin=cloud:bionic-ussuri
    juju deploy magnum-dashboard
    juju add-relation \
        openstack-dashboard:dashboard-plugin magnum-dashboard:dashboard

# Bugs

Please report bugs on [Launchpad](https://bugs.launchpad.net/charm-magnum-dashboard/+filebug).

For general questions please refer to the OpenStack [Charm Guide](https://docs.openstack.org/charm-guide/latest/).