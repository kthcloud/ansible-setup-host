import json
import os

import cs

config = json.load(open("/etc/kthcloud/setup-config.json"))

endpoint = config['cloudstack']['endpoint']
apiKey = config['cloudstack']['apiKey']
secret = config['cloudstack']['secret']
zone = config['cloudstack']['zone']
pod = config['cloudstack']['pod']
cluster = config['cloudstack']['cluster']
host = config['host']['name']
hostIp = config['host']['ip']
username = config['host']['username']
password = config['host']['password']

# connect to cloudstack
cloudstack = cs.CloudStack(endpoint=endpoint, key=apiKey, secret=secret)

# get zone id
zone_id = None
zones = cloudstack.listZones()
for z in zones['zone']:
    if z['name'] == zone:
        zone = z['id']
        break

if zone_id is None:
    available_zones = ', '.join([z['name'] for z in zones['zone']])
    raise Exception(
        f'Zone {zone} not found, available zones are: {available_zones}')

# get pod id
pod_id = None
pods = cloudstack.listPods()
for p in pods['pod']:
    if p['name'] == pod:
        pod = p['id']
        break
if pod_id is None:
    available_pods = ', '.join([p['name'] for p in pods['pod']])
    raise Exception(
        f'Pod {pod} not found, available pods are: {available_pods}')

# get cluster id
cluster_id = None
clusters = cloudstack.listClusters()
for c in clusters['cluster']:
    if c['name'] == cluster:
        cluster = c['id']
        break

if cluster_id is None:
    available_clusters = ', '.join(
        [c['name'] for c in clusters['cluster']])
    raise Exception(
        f'Cluster {cluster} not found, available clusters are: {available_clusters}')

# add host
cloudstack.addHost(
    zoneid=zone,
    podid=pod,
    clusterid=cluster,
    hypervisor='KVM',
    url=hostIp,
    username=username,
    password=password,
)

print(f'Successfully added host {host} to {zone}:{pod}:{cluster}')