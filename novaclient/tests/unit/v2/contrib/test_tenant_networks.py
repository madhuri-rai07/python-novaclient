# Copyright 2012 OpenStack Foundation
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from novaclient import api_versions
from novaclient import extension
from novaclient.tests.unit import utils
from novaclient.tests.unit.v2 import fakes
from novaclient.v2.contrib import tenant_networks


class TenantNetworkExtensionTests(utils.TestCase):

    def setUp(self):
        super(TenantNetworkExtensionTests, self).setUp()
        extensions = [
            extension.Extension(tenant_networks.__name__.split(".")[-1],
                                tenant_networks),
        ]
        self.cs = fakes.FakeClient(api_versions.APIVersion("2.0"),
                                   extensions=extensions)

    def test_list_tenant_networks(self):
        nets = self.cs.tenant_networks.list()
        self.assert_request_id(nets, fakes.FAKE_REQUEST_ID_LIST)
        self.cs.assert_called('GET', '/os-tenant-networks')
        self.assertGreater(len(nets), 0)

    def test_get_tenant_network(self):
        net = self.cs.tenant_networks.get(1)
        self.assert_request_id(net, fakes.FAKE_REQUEST_ID_LIST)
        self.cs.assert_called('GET', '/os-tenant-networks/1')

    def test_create_tenant_networks(self):
        net = self.cs.tenant_networks.create(label="net",
                                             cidr="10.0.0.0/24")
        self.assert_request_id(net, fakes.FAKE_REQUEST_ID_LIST)
        self.cs.assert_called('POST', '/os-tenant-networks')

    def test_delete_tenant_networks(self):
        ret = self.cs.tenant_networks.delete(1)
        self.assert_request_id(ret, fakes.FAKE_REQUEST_ID_LIST)
        self.cs.assert_called('DELETE', '/os-tenant-networks/1')
