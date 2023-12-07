agent_host = {
    "v": 2,
    "id": "f2e9dfcc-2922-11ed-af22-002285949027",
    "nic": [
        {
          "mac": "00:0c:29:ec:7a:21",
          "enabled": 1,
          "nic_name": "ens33",
          "connected": 1,
          "v4_addresses": [
              {
                  "v4_address": "10.65.150.193",
                  "v4_netmask": "255.255.240.0"
              }
          ],
            "v6_addresses": [
              {
                  "v6_address": "2001::166",
                  "v6_netmask": "ffff:ffff:ffff:ffff::"
              },
              {
                  "v6_address": "fe80::8f5e:b14d:84ac:57d1",
                  "v6_netmask": "ffff:ffff:ffff:ffff::"
              }
          ]
        }
    ],
    "ver": "1.0.3",
    "cpu_id": "0F8BFBFF000306E4",
    "dev_ip": "10.65.150.193",
    "memory": 1838,
    "bios_id": "VMware-564d555d694efee6-29aca5431eec7a21",
    "os_name": "NeoKylin Linux Advanced Server",
    "os_type": "Linux",
    "service": "nsfagent",
    "board_id": "",
    "cpu_arch": "x64",
    "cpu_name": "Intel(R) Xeon(R) CPU E5-2660 v2 @ 2.20GHz",
    "hostname": "ues166",
    "boot_time": 1700532534000,
    "cpu_cores": 1,
    "dev_ip_up": "",
    "host_type": "server",
    "size_unit": 1048576,
    "hashdevice": "5E0D-A7DC-444B-9871",
    "os_version": "V7Update6 (Chromium)",
    "cpu_sockets": 1,
    "cpu_threads": 1,
    "memory_size": 1838,
    "os_kernel_name": "Linux",
    "firewall_status": 1,
    "memory_swap_size": 2047,
    "os_kernel_version": "3.10.0-957.el7.x86_64",
    "os_release_version": "7.6 (Maipo)"
}

# nic_info_list = agent_host.get("nic", [])
# for each_nic in nic_info_list:
#   _ipv4_list = each_nic.get("v4_addresses", [])
#   print('///', _ipv4_list)
#   for each_ip in _ipv4_list:
#     print('mmm', each_ip['v4_address'])


def get_nic_list(agent_host):
    nic_list = []
    nic_info_list = agent_host.get("nic", [])
    for each_nic in nic_info_list:
        nic_info = dict()
        nic_info["mac"] = each_nic.get("mac")
        nic_info["nic_name"] = each_nic.get("nic_name")
        _ipv4_list = each_nic.get("v4_addresses", [])
        _ipv6_list = each_nic.get("v6_addresses", [])
        ipv4_list = []
        ipv6_list = []
        for each_ip in _ipv4_list:
            # print('1111', each_ip)
            ipv4_list.append(each_ip['v4_address'])

        for each_ip in _ipv6_list:
            ipv6_list.append(each_ip['v6_address'])
        nic_info["ipv4"] = ipv4_list
        nic_info["ipv6"] = ipv6_list
        nic_list.append(nic_info)
        # print(nic_list)
    return nic_list


print(get_nic_list(agent_host))
