import json

def get_key_features(data, key_feature_map):
    features = {}
    for key in data:
        if key in key_feature_map:
            features[key] = data[key]
    return json.dumps(features)

# 示例数据
json_data = {
    "hostname": "ZHANGPENGQIANG",
    "ctime": 1697798773,
    "object": "alert",
    "id": "24efe54a-5f1d-11ed-a2a3-f0d4e2ea0490",
    "victim_id": "24efe54a-5f1d-11ed-a2a3-f0d4e2ea0490",
    "dev_ip": "10.65.6.175",
    "victim_ip": "10.65.6.175",
    "action": "create",
    "osc": "windows",
    "username": "nsfocus",
    "ver": "1.0.4",
    "pid": 25960,
    "cmdline": "wmic  ntdomain list brief",
    "pprocess": "C:\\Windows\\System32\\cmd.exe",
    "log_object": "process",
    "v": 1,
    "timestamp": 1697798774,
    "rule_id": 24,
    "ppid": 27460,
    "alert_id": "CB34CA61-040F-41b5-A4F4-BE5CB0368BE3",
    "boot_time": 12277359,
    "company": "MicrosoftCorporation",
    "md5": "e4cf847182d343390b2cfef403fdc4b4",
    "process": "C:\\Windows\\System32\\wbem\\WMIC.exe",
    "log_id": "ae4ea8bb-6409-4140-94a4-f14cd88dd99c",
    "kill_chain_stage": 1,
    "attack_stage": 2,
    "level": 1,
    "event_name": "利用wmic获取域信息",
    "event_type": 4,
    "analysis_tech": "ioa",
    "techniques": "Windows Management Instrumentation",
    "attack_id": "T1047",
    "detect_module": "ioa",
    "sip": "10.65.6.175"
}

key_feature_map = {
    "domain": "域名",
    "path": "路径",
    "SourceName": "源名称",
    "cmdline": "命令行",
    "payload": "载荷",
    "vendor": "厂商",
    "pprocess": "父进程",
    "address": "地址",
    "process": "进程",
    "md5": "MD5",
    "disk": "磁盘",
    "source_address": "源地址",
    "remote_address": "目标地址",
    "actor": "组织",
    "new_value": "注册表值",
    "source_port": "源端口",
    "serial": "序列号",
    "virus_name": "病毒名称",
    "valuename": "值名称",
    "EventCode": "事件代码",
    "module": "模块"
}

result = get_key_features(json_data, key_feature_map)
print(result)