---
title: "MQTT Message Reference"
lang: en
slug: "pans-pro-rtls/integration-guide/mqtt-message-reference"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/pans-pro-rtls/integration-guide/mqtt-message-reference/"
order: 75
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="mqtt-message-reference">
<span id="pans-mqtt-message-reference"></span><h1>MQTT Message Reference</h1>
<p>This page describes the detail of each API definition</p>
<div class="section" id="anchorconfiguration">
<span id="id1"></span><h2>AnchorConfiguration</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>Field</strong></p></th>
<th class="head"><p><strong>Type</strong></p></th>
<th class="head"><p><strong>Label</strong></p></th>
<th class="head"><p><strong>Description</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>initiator</p></td>
<td><p>bool</p></td>
<td><p>required</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>position</p></td>
<td><p>Position</p></td>
<td><p>optional</p></td>
<td><p>Anchor position
coordinates</p></td>
</tr>
<tr class="row-even"><td><p>routingConfig</p></td>
<td><p>Rout
ingAnchorConfig
uration</p></td>
<td><p>required</p></td>
<td><p>routing
configuration</p></td>
</tr>
<tr class="row-odd"><td><p>routingStatus</p></td>
<td><p>Rout
ingAnchorStatus</p></td>
<td><p>optional</p></td>
<td><p>routing info
- valid for
uplink only,
read-only</p></td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="fwversion">
<h2>FwVersion</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>Field</strong></p></th>
<th class="head"><p><strong>Type</strong></p></th>
<th class="head"><p><strong>Label</strong></p></th>
<th class="head"><p><strong>Description</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>release</p></td>
<td><p>string</p></td>
<td><p>optional</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>firmware</p></td>
<td><p>string</p></td>
<td><p>repeated</p></td>
<td></td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="kernelposition">
<h2>KernelPosition</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>Field</strong></p></th>
<th class="head"><p><strong>Type</strong></p></th>
<th class="head"><p><strong>Label</strong></p></th>
<th class="head"><p><strong>Description</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>x</p></td>
<td><p>bytes</p></td>
<td><p>required</p></td>
<td><div class="line-block">
<div class="line">coordinate
as opaque
bytes
sequence,
kernel
driver
cannot
operate
with
floats in
kernel
space</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><p>y</p></td>
<td><p>bytes</p></td>
<td><p>required</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p>z</p></td>
<td><p>bytes</p></td>
<td><p>required</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>quality</p></td>
<td><p>uint32</p></td>
<td><p>required</p></td>
<td><div class="line-block">
<div class="line">quality
factor
(0-100),
PB uses
variable
length
encoding,
no worries
about the
length</div>
</div>
</td>
</tr>
</tbody>
</table>
<hr class="docutils">
<p>MacConfig</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>Field</strong></p></th>
<th class="head"><p><strong>Type</strong></p></th>
<th class="head"><p><strong>Label</strong></p></th>
<th class="head"><p><strong>Description</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>address</p></td>
<td><p>string</p></td>
<td><p>required</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>type</p></td>
<td><p>string</p></td>
<td><p>required</p></td>
<td><p>EMPTY,
DEFAULT,
USER_SPECIFIED,
MUTABLE_DEFAULT</p></td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="gatewayconfig">
<h2>GatewayConfig</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>Field</strong></p></th>
<th class="head"><p><strong>Type</strong></p></th>
<th class="head"><p><strong>Label</strong></p></th>
<th class="head"><p><strong>Description</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>ipAddress</p></td>
<td><p>string</p></td>
<td><p>repeated</p></td>
<td><p>List of IP
addresses,
masks and IP
gateways</p></td>
</tr>
<tr class="row-odd"><td><p>ipMask</p></td>
<td><p>string</p></td>
<td><p>repeated</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p>ipGateway</p></td>
<td><p>string</p></td>
<td><p>repeated</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>dns</p></td>
<td><p>string</p></td>
<td><p>repeated</p></td>
<td><p>DNS</p>
<p>configuration</p>
</td>
</tr>
<tr class="row-even"><td><p>interface</p></td>
<td><p>string</p></td>
<td><p>required</p></td>
<td><p>Interface
type
ETHERNET,WIFI,
…</p></td>
</tr>
<tr class="row-odd"><td><p>dhcp</p></td>
<td><p>bool</p></td>
<td><p>required</p></td>
<td><p>DHCP</p>
<p>configuration</p>
</td>
</tr>
<tr class="row-even"><td><p>tls</p></td>
<td><p>string</p></td>
<td><p>required</p></td>
<td><p>TLS
configuration
OFF,
SERVER,
MUTUAL,
SERVER_CN,
MUTUAL_CN</p></td>
</tr>
<tr class="row-odd"><td><p>server</p></td>
<td><p>string</p></td>
<td><p>required</p></td>
<td><p>Server
address and
port</p></td>
</tr>
<tr class="row-even"><td><p>port</p></td>
<td><p>uint32</p></td>
<td><p>required</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>macFilter</p></td>
<td><p>bool</p></td>
<td><p>required</p></td>
<td><p>MAC filter</p>
<p>configuration</p>
</td>
</tr>
<tr class="row-even"><td><p>wifi</p></td>
<td><p>WifiConfig</p></td>
<td><p>optional</p></td>
<td><p>WIFI
configuration,
the WIFI
is
available
and it can
be
configured
if this
field
appears in
the uplink
message</p></td>
</tr>
<tr class="row-odd"><td><p>mac</p></td>
<td><p>MacConfig</p></td>
<td><p>repeated</p></td>
<td><div class="line-block">
<div class="line">read only
list of
MAC
addresses
of the
interfaces</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>label</p></td>
<td><p>string</p></td>
<td><p>required</p></td>
<td><p>UWB node
label</p></td>
</tr>
<tr class="row-odd"><td><p>uwbMode</p></td>
<td><p>UwbMode</p></td>
<td><p>required</p></td>
<td><p>UWB mode 0 -
offline, 1
- passive, 2
- active</p></td>
</tr>
<tr class="row-even"><td><p>leds</p></td>
<td><p>bool</p></td>
<td><p>required</p></td>
<td><p>enable or
disable LEDs</p></td>
</tr>
<tr class="row-odd"><td><p>uw
bFirmwareUpdate</p></td>
<td><p>bool</p></td>
<td><p>required</p></td>
<td><p>firmware
update
enable/disable</p></td>
</tr>
<tr class="row-even"><td><p>initiator</p></td>
<td><p>bool</p></td>
<td><p>required</p></td>
<td><p>UWB anchor
initiator</p></td>
</tr>
<tr class="row-odd"><td><p>uwbBridge</p></td>
<td><p>bool</p></td>
<td><p>required</p></td>
<td><p>UWB bridge</p></td>
</tr>
<tr class="row-even"><td><p>position</p></td>
<td><p>Position</p></td>
<td><p>required</p></td>
<td><p>gateway
position</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="gatewaystatusandconfig">
<span id="pans-gatewaystatusandconfig"></span><h2>GatewayStatusAndConfig</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>Field</strong></p></th>
<th class="head"><p><strong>Type</strong></p></th>
<th class="head"><p><strong>Label</strong></p></th>
<th class="head"><p><strong>Description</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>networkId</p></td>
<td><p>uint32</p></td>
<td><p>optional</p></td>
<td><p>UWB network
id</p></td>
</tr>
<tr class="row-odd"><td><p>bridgeNodeId</p></td>
<td><p>sfixed64</p></td>
<td><p>optional</p></td>
<td><p>Identification
of the
bridge node
which is
connected to
KD to the
server</p></td>
</tr>
<tr class="row-even"><td><p>version</p></td>
<td><p>FwVersion</p></td>
<td><p>optional</p></td>
<td><p>Firmware
version
numbers</p></td>
</tr>
<tr class="row-odd"><td><p>uwb</p></td>
<td><p>string</p></td>
<td><p>optional</p></td>
<td><dl class="simple">
<dt>UWB status:</dt><dd><p>connected,
connected_bh,
disconnected,
updating_fw</p>
</dd>
</dl>
</td>
</tr>
<tr class="row-even"><td><p>configuration</p></td>
<td><p>GatewayConfig</p></td>
<td><p>optional</p></td>
<td><p>configuration
options</p></td>
</tr>
<tr class="row-odd"><td><p>debugLog</p></td>
<td><p>DebugLog</p></td>
<td><p>optional</p></td>
<td><p>to be passed
to the
Gateway</p></td>
</tr>
<tr class="row-even"><td><p>timestamp</p></td>
<td><p>uint64</p></td>
<td><p>optional</p></td>
<td><p>timestamp in
microseconds</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="nodeconfigdownlink">
<span id="id2"></span><h2>NodeConfigDownlink</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 24%">
<col style="width: 28%">
<col style="width: 24%">
<col style="width: 24%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>Field</strong></p></th>
<th class="head"><p><strong>Type</strong></p></th>
<th class="head"><p><strong>Label</strong></p></th>
<th class="head"><p><strong>Description</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>configuration</p></td>
<td><p>Node Configuration</p></td>
<td><p>required</p></td>
<td><p>what can be
changed from
client</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="nodeconfiguplink">
<span id="id3"></span><h2>NodeConfigUplink</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 24%">
<col style="width: 28%">
<col style="width: 24%">
<col style="width: 24%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>Field</strong></p></th>
<th class="head"><p><strong>Type</strong></p></th>
<th class="head"><p><strong>Label</strong></p></th>
<th class="head"><p><strong>Description</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>configuration</p></td>
<td><p>Node Configuration</p></td>
<td><p>required</p></td>
<td><blockquote>
<div><p>modifiable</p>
</div></blockquote>
<p>configuration
can be
changed via
API</p>
</td>
</tr>
<tr class="row-odd"><td><p>timestamp</p></td>
<td><p>uint64</p></td>
<td><p>optional</p></td>
<td><p>timestamp in
microseconds</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="nodedatadownlink">
<span id="pans-nodedatadownlink"></span><h2>NodeDataDownlink</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>Field</strong></p></th>
<th class="head"><p><strong>Type</strong></p></th>
<th class="head"><p><strong>Label</strong></p></th>
<th class="head"><p><strong>Description</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>data</p></td>
<td><p>bytes</p></td>
<td><p>required</p></td>
<td><p>opaque data
(max 36 bytes)</p></td>
</tr>
<tr class="row-odd"><td><p>overwrite</p></td>
<td><p>bool</p></td>
<td><p>optional</p></td>
<td><p>flags</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="nodedatauplink">
<span id="pans-nodedatauplink"></span><h2>NodeDataUplink</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>Field</strong></p></th>
<th class="head"><p><strong>Type</strong></p></th>
<th class="head"><p><strong>Label</strong></p></th>
<th class="head"><p><strong>Description</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>data</p></td>
<td><p>bytes</p></td>
<td><p>required</p></td>
<td><p>opaque data
(max 40 bytes)</p></td>
</tr>
<tr class="row-odd"><td><p>superFrameNumber</p></td>
<td><p>uint32</p></td>
<td><p>optional</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p>timestamp</p></td>
<td><p>uint64</p></td>
<td><p>optional</p></td>
<td><p>timestamp in
microseconds</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="nodelocationuplink">
<span id="pans-nodelocationuplink"></span><h2>NodeLocationUplink</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>Field</strong></p></th>
<th class="head"><p><strong>Type</strong></p></th>
<th class="head"><p><strong>Label</strong></p></th>
<th class="head"><p><strong>Description</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>position</p></td>
<td><p>Position</p></td>
<td><p>required</p></td>
<td><p>embedded
position</p></td>
</tr>
<tr class="row-odd"><td><p>superFrameNumber</p></td>
<td><p>uint32</p></td>
<td><p>optional</p></td>
<td><p>superframe</p></td>
</tr>
<tr class="row-even"><td><p>timestamp</p></td>
<td><p>uint64</p></td>
<td><p>optional</p></td>
<td><p>timestamp in
microseconds</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="nodeservicedownlink">
<span id="pans-nodeservicedownlink"></span><h2>NodeServiceDownlink</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>Field</strong></p></th>
<th class="head"><p><strong>Type</strong></p></th>
<th class="head"><p><strong>Label</strong></p></th>
<th class="head"><p><strong>Description</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>type</p></td>
<td><p>string</p></td>
<td><p>required</p></td>
<td><p>TLV_API</p></td>
</tr>
<tr class="row-odd"><td><p>data</p></td>
<td><p>bytes</p></td>
<td><p>required</p></td>
<td><p>TLV encoded
binary data
that
represent
API call</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="nodeserviceuplink">
<span id="pans-nodeserviceuplink"></span><h2>NodeServiceUplink</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>Field</strong></p></th>
<th class="head"><p><strong>Type</strong></p></th>
<th class="head"><p><strong>Label</strong></p></th>
<th class="head"><p><strong>Description</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>type</p></td>
<td><p>string</p></td>
<td><p>required</p></td>
<td><p>TLV_API_ACK,
TLV_API_NACK</p></td>
</tr>
<tr class="row-odd"><td><p>data</p></td>
<td><p>bytes</p></td>
<td><p>optional</p></td>
<td><p>TLV encoded
API call
response</p></td>
</tr>
<tr class="row-even"><td><p>timestamp</p></td>
<td><p>uint64</p></td>
<td><p>optional</p></td>
<td><p>timestamp in
microseconds</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="nodestatusuplink">
<span id="pans-nodestatusuplink"></span><h2>NodeStatusUplink</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>Field</strong></p></th>
<th class="head"><p><strong>Type</strong></p></th>
<th class="head"><p><strong>Label</strong></p></th>
<th class="head"><p><strong>Description</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>present</p></td>
<td><p>bool</p></td>
<td><p>optional</p></td>
<td><p>true if
present,
false if
non-present</p></td>
</tr>
<tr class="row-odd"><td><p>downlink</p></td>
<td><p>bool</p></td>
<td><p>optional</p></td>
<td><p>true if
possible,
false if
non-possible</p></td>
</tr>
<tr class="row-even"><td><p>lqi</p></td>
<td><p>uint32</p></td>
<td><p>optional</p></td>
<td><p>Link quality
indication:
0=poor
1=good</p></td>
</tr>
<tr class="row-odd"><td><p>batt</p></td>
<td><p>uint32</p></td>
<td><p>optional</p></td>
<td><p>battery
level in
mV</p></td>
</tr>
<tr class="row-even"><td><p>batt_state</p></td>
<td><p>uint32</p></td>
<td><p>optional</p></td>
<td><p>Indicates the
battery
status,
0-Unknown</p>
<ul class="simple">
<li><p>1-Empty</p></li>
<li><p>2-Low</p></li>
<li><p>3-Medium</p></li>
<li><p>4-Full.</p></li>
</ul>
</td>
</tr>
<tr class="row-odd"><td><p>temp</p></td>
<td><p>uint32</p></td>
<td><p>optional</p></td>
<td><p>temperature
in degrees
of celsius</p></td>
</tr>
<tr class="row-even"><td><p>timestamp</p></td>
<td><p>uint64</p></td>
<td><p>optional</p></td>
<td><p>timestamp in
microseconds</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="nodeconfiguration">
<span id="pans-nodeconfiguration"></span><h2>NodeConfiguration</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 22%">
<col style="width: 34%">
<col style="width: 22%">
<col style="width: 22%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>Field</strong></p></th>
<th class="head"><p><strong>Type</strong></p></th>
<th class="head"><p><strong>Label</strong></p></th>
<th class="head"><p><strong>Description</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>label</p></td>
<td><p>string</p></td>
<td><p>required</p></td>
<td><p>common
configuration
properties</p></td>
</tr>
<tr class="row-odd"><td><p>nodeType</p></td>
<td><p>OperationMode</p></td>
<td><p>required</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p>ble</p></td>
<td><p>bool</p></td>
<td><p>required</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>leds</p></td>
<td><p>bool</p></td>
<td><p>required</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p>uw
bFirmwareUpdate</p></td>
<td><p>bool</p></td>
<td><p>required</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>anchor</p></td>
<td><p>AnchorConfiguration</p></td>
<td><p>optional</p></td>
<td><p>either-or:
in sync
with
Operation
Mode
anchor
specific</p></td>
</tr>
<tr class="row-even"><td><p>tag</p></td>
<td><p>TagConfiguration</p></td>
<td><p>optional</p></td>
<td><p>tag specific</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="position">
<span id="pans-position"></span><h2>Position</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>Field</strong></p></th>
<th class="head"><p><strong>Type</strong></p></th>
<th class="head"><p><strong>Label</strong></p></th>
<th class="head"><p><strong>Description</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>x</p></td>
<td><p>float</p></td>
<td><p>required</p></td>
<td><p>coordinates</p></td>
</tr>
<tr class="row-odd"><td><p>y</p></td>
<td><p>float</p></td>
<td><p>required</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p>z</p></td>
<td><p>float</p></td>
<td><p>required</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>quality</p></td>
<td><p>uint32</p></td>
<td><p>required</p></td>
<td><div class="line-block">
<div class="line">quality
factor
(0-100),
PB uses
variable
length
encoding,
no worries
about the
length</div>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="tagconfiguration">
<h2>TagConfiguration</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>Field</strong></p></th>
<th class="head"><p><strong>Type</strong></p></th>
<th class="head"><p><strong>Label</strong></p></th>
<th class="head"><p><strong>Description</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>stat
ionaryDetection</p></td>
<td><p>bool</p></td>
<td><p>required</p></td>
<td><p>detect
stationary
state ~
accelerometer</p></td>
</tr>
<tr class="row-odd"><td><p>responsive</p></td>
<td><p>bool</p></td>
<td><p>required</p></td>
<td><p>responsive
mode ~
low-power</p></td>
</tr>
<tr class="row-even"><td><p>locationEngine</p></td>
<td><p>bool</p></td>
<td><p>required</p></td>
<td><p>locate?</p></td>
</tr>
<tr class="row-odd"><td><p>nomUpdateRate</p></td>
<td><p>uint32</p></td>
<td><p>required</p></td>
<td><p>nominal
(regular)
update rate</p></td>
</tr>
<tr class="row-even"><td><p>statUpdateRate</p></td>
<td><p>uint32</p></td>
<td><p>required</p></td>
<td><p>static
update
rate (if
stat
ionaryDetection
is turned
on)</p></td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="wificonfig">
<h2>WifiConfig</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>Field</strong></p></th>
<th class="head"><p><strong>Type</strong></p></th>
<th class="head"><p><strong>Label</strong></p></th>
<th class="head"><p><strong>Description</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>ssid</p></td>
<td><p>string</p></td>
<td><p>required</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>password</p></td>
<td><p>string</p></td>
<td><p>required</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p>region</p></td>
<td><p>string</p></td>
<td><p>required</p></td>
<td><p>EUROPE,
NORTH_AMERICA,
ASIA</p></td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="operatingfirmware">
<h2>OperatingFirmware</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>Name</strong></p></th>
<th class="head"><p><strong>Number</strong></p></th>
<th class="head"><p><strong>Description</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>FW1</p></td>
<td><p>0</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>FW2</p></td>
<td><p>1</p></td>
<td></td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="operationmode">
<h2>OperationMode</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>Name</strong></p></th>
<th class="head"><p><strong>Number</strong></p></th>
<th class="head"><p><strong>Description</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>TAG</p></td>
<td><p>0</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>ANCHOR</p></td>
<td><p>1</p></td>
<td></td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="routinganchorconfiguration">
<h2>RoutingAnchorConfiguration</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>Name</strong></p></th>
<th class="head"><p><strong>Number</strong></p></th>
<th class="head"><p><strong>Description</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>ROUTING_CFG_OFF</p></td>
<td><p>0</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>ROUTING_CFG_ON</p></td>
<td><p>1</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p>ROUTING_CFG_AUTO</p></td>
<td><p>2</p></td>
<td></td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="routinganchorstatus">
<h2>RoutingAnchorStatus</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>Name</strong></p></th>
<th class="head"><p><strong>Number</strong></p></th>
<th class="head"><p><strong>Description</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>ROUTING_STAT_INACTIVE</p></td>
<td><p>0</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>ROUTING_STAT_SELECTED</p></td>
<td><p>1</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p>ROUTING_STAT_ACTIVE</p></td>
<td><p>2</p></td>
<td></td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="uwbmode">
<h2>UwbMode</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>Name</strong></p></th>
<th class="head"><p><strong>Number</strong></p></th>
<th class="head"><p><strong>Description</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>UWB_MODE_OFFLINE</p></td>
<td><p>0</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>UWB_MODE_PASSIVE</p></td>
<td><p>1</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p>UWB_MODE_ACTIVE</p></td>
<td><p>2</p></td>
<td></td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="uwbstatus">
<h2>UwbStatus</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Name</p></th>
<th class="head"><p>Number</p></th>
<th class="head"><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>DISCONNECTED</p></td>
<td><p>0</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>CONNECTED</p></td>
<td><p>1</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p>CONNECTED_BH</p></td>
<td><p>2</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>UPDATING_FW</p></td>
<td><p>3</p></td>
<td></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="serverrequest">
<span id="id4"></span><h2>ServerRequest</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 21%">
<col style="width: 7%">
<col style="width: 72%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Name</p></th>
<th class="head"><p>Number</p></th>
<th class="head"><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>REFRESH_TOPICS</p></td>
<td><p>0</p></td>
<td><p>Request to immediately publish all messages for all the nodes.</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="servermessage">
<span id="pans-servermessage"></span><h2>ServerMessage</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 23%">
<col style="width: 23%">
<col style="width: 23%">
<col style="width: 31%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Field</p></th>
<th class="head"><p>Type</p></th>
<th class="head"><p>Label</p></th>
<th class="head"><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>request</p></td>
<td><p>string</p></td>
<td><p>optional</p></td>
<td><p>Refer to
<a class="reference internal" href="#serverrequest"><span class="std std-ref">ServerRequest</span></a></p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="servernodelist">
<span id="id5"></span><h2>ServerNodeList</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 11%">
<col style="width: 14%">
<col style="width: 12%">
<col style="width: 64%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Field</p></th>
<th class="head"><p>Type</p></th>
<th class="head"><p>Label</p></th>
<th class="head"><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>network</p></td>
<td><p>uint32</p></td>
<td><p>required</p></td>
<td><p>UWB network panID.</p></td>
</tr>
<tr class="row-odd"><td><p>node</p></td>
<td><p>string</p></td>
<td><p>repeated</p></td>
<td><p>UWB node ID/address as hexadecimal number.</p></td>
</tr>
</tbody>
</table>
</div>
</div>


           </div>
