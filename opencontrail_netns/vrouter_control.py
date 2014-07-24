import sys

import getopt
import logging
import socket

from contrail_lib import rpc_client_instance, uuid_from_string
import contrail_vrouter_api.gen_py.instance_service


def add_interface(interface_name, vmi, vm, mac):
    from contrail_vrouter_api.gen_py.instance_service import ttypes
    data = ttypes.Port(
        uuid_from_string(vmi),
        uuid_from_string(vm),
        interface_name,
        '0.0.0.0',
        [0] * 16,
        mac)

    logging.debug(data)
    rpc = rpc_client_instance()
    if not rpc:
        return
    try:
        rpc.AddPort([data])
    except socket.error:
        logging.error('RPC failure')


def del_interface(vmi):
    rpc = rpc_client_instance()
    if not rpc:
        return
    try:
        rpc.DeletePort(uuid_from_string(vmi))
    except socket.error:
        logging.error('RPC failure')

    logging.info('Deleted virtual-machine-interface uuid = ' + vmi)


def interface_register(vm, vmi, iface_name):
    mac = vmi.virtual_machine_interface_mac_addresses.mac_address[0]
    add_interface(iface_name, vmi.uuid, vm.uuid, mac)


def interface_unregister(vmi_uuid):
    del_interface(vmi_uuid)
