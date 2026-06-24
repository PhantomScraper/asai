---
title: "BLE Interface"
lang: en
slug: "pans-pro-rtls/integration-guide/ble-inteface"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/pans-pro-rtls/integration-guide/ble-inteface/"
order: 97
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="ble-interface">
<span id="pans-ble-interface"></span><h1>BLE Interface</h1>
<p>In the BLE API design, the DWM module acts as the BLE peripheral and
can be communicated by BLE central devices through the APIs. This
document introduces the APIs that the BLE central devices can use for
the communication. An Android application and PANS PRO Manager are
provided to exercise the BLE APIs.</p>
<p>The BLE central device directly connects with the network nodes to
set up and retrieve parameters. It needs to connect to each device
individually to configure/control.</p>
<p>In the BLE scheme, normal GATT operations, including read, write, and
notification are provided.</p>
<blockquote>
<div><div class="figure align-default">
<a class="reference internal image-reference" href="../../../_images/image31.png"><img alt="../../../_images/image31.png" src="/docs-assets/_images/image31.png" style="width: 5.70833in; height: 2.01111in;"></a>
</div>
</div></blockquote>
<p>The figure above show that’s the DWM1001 BLE event handler translates
the GATT operations into generic API commands. In the meantime, when
there are BLE-related events, the BLE event handler will send the
corresponding notification to the BLE client.</p>
<p>Detailed BLE APIs are introduced in section <em>BLE API</em>.</p>
<hr class="docutils">
<div class="section" id="le-gatt-model">
<h2>LE GATT Model</h2>
<p>The <strong>network node service</strong> UUID is <strong>680c21d9-c946-4c1f-9c11-baa1c21329e7</strong>. All characteristic values are encoded as little endian as BLE specification suggests.</p>
<div class="section" id="network-node-characteristics">
<h3>Network Node Characteristics</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 28%">
<col style="width: 15%">
<col style="width: 11%">
<col style="width: 38%">
<col style="width: 8%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>uuid</p></th>
<th class="head"><p>name</p></th>
<th class="head"><p>Length</p></th>
<th class="head"><p>Value</p></th>
<th class="head"><p>flags</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>“Std. GAP service, label 0x2A00”</p></td>
<td><p>Label</p></td>
<td><p>Var</p></td>
<td><p>UTF-8 encoded string</p></td>
<td><p>RW</p></td>
</tr>
<tr class="row-odd"><td><p>3f0afd88-7770-46b0-b5e7-9fc099598964</p></td>
<td><p>Operation mode</p></td>
<td><p>2 bytes</p></td>
<td><p>See the section below for details on data encoding</p></td>
<td><p>RW</p></td>
</tr>
<tr class="row-even"><td><p>80f9d8bc-3bff-45bb-a181-2d6a37991208</p></td>
<td><p>Network ID</p></td>
<td><p>2 bytes</p></td>
<td><p>Unique identification of the network (PAN ID)</p></td>
<td><p>RW</p></td>
</tr>
<tr class="row-odd"><td><p>a02b947e-df97-4516-996a-1882521e0ead</p></td>
<td><p>Location data mode</p></td>
<td><p>1 byte</p></td>
<td><p>0 - Position
1 - Distances
2 - Position + distances”</p></td>
<td><p>RW</p></td>
</tr>
<tr class="row-even"><td><p>003bbdf2-c634-4b3d-ab56-7ec889b89a37</p></td>
<td><p>Location data</p></td>
<td><p>106 bytes max</p></td>
<td><p>See the section below for details on data encoding</p></td>
<td><p>RO</p></td>
</tr>
<tr class="row-odd"><td><p>f4a67d7d-379d-4183-9c03-4b6ea5103291</p></td>
<td><p>Proxy positions</p></td>
<td><p>76 bytes max</p></td>
<td><p>Used by the module as a notification about
new tag positions for the BLE central</p></td>
<td><p>RO</p></td>
</tr>
<tr class="row-even"><td><p>1e63b1eb-d4ed-444e-af54-c1e965192501</p></td>
<td><p>Device info</p></td>
<td><p>29 bytes</p></td>
<td><p>Node ID (8 bytes), HW version (4 bytes),
FW1 version (4 bytes), FW2 version (4 bytes),
FW1 checksum (4 bytes), FW2 checksum (4 bytes),
RDonly Operation flags (1 byte)</p></td>
<td><p>RO</p></td>
</tr>
<tr class="row-odd"><td><p>1e630001-d4ed-444e-af54-c1e965192501
[PANS PRO]</p></td>
<td><p>Device status</p></td>
<td><p>8 bytes</p></td>
<td><p>Uptime (4 bytes, unsigned integer),
battery level
(1 byte, unsigned integer), reserved (1 byte)
, temperature (2 bytes, integer)</p></td>
<td><p>RO</p></td>
</tr>
<tr class="row-even"><td><p>0eb2bc59-baf1-4c1c-8535-8a0204c69de5</p></td>
<td><p>Statistics</p></td>
<td><p>120 bytes</p></td>
<td><p>Node statistics</p></td>
<td><p>RO</p></td>
</tr>
<tr class="row-odd"><td><p>5955aa10-e085-4030-8aa6-bdfac89ac32b</p></td>
<td><p>FW update push</p></td>
<td><p>Max 37 bytes</p></td>
<td><p>Used to send structured data (FW update packets)
to the module (BLE peripheral), the size is set
according to max transmission unit (MTU).
See the section below for details on data encoding.</p></td>
<td><p>WO</p></td>
</tr>
<tr class="row-even"><td><p>9eed0e27-09c0-4d1c-bd92-7c441daba850</p></td>
<td><p>FW update poll</p></td>
<td><p>9 bytes</p></td>
<td><p>Used by the module as a response/notification
for the BLE central.
See the section below for details on data encoding.</p></td>
<td><p>RO</p></td>
</tr>
<tr class="row-odd"><td><p>ed83b848-da03-4a0a-a2dc-8b401080e473</p></td>
<td><p>Disconnect</p></td>
<td><p>1 byte</p></td>
<td><p>Used to explicitly disconnect from BLE
peripheral by writing value=1
(workaround due to Android behavior)</p></td>
<td><p>WO</p></td>
</tr>
<tr class="row-even"><td><p>“5b10c428-af2f-486f-aee1-9dbd79b6bccb
[PANS PRO Modified]”</p></td>
<td><p>Anchor list</p></td>
<td><p>65 bytes</p></td>
<td><p>Count (1 byte), list of node IDs (2 bytes),
RSSI (1 byte), seat (1 bytes)
max 16 elements in list</p></td>
<td><p>RO</p></td>
</tr>
<tr class="row-odd"><td><p>9d5ab03b-cbf8-4ae5-9f11-63e45f538ada</p></td>
<td><p>AES key</p></td>
<td><p>16 bytes</p></td>
<td><p>AES symmetric key
To be implemented in R2</p></td>
<td><p>RW</p></td>
</tr>
</tbody>
</table>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>The label characteristic is a special one. It is part of the standard mandatory GAP service (0x1800) under the standard Name characteristic (0x2A00).</p>
</div>
</div>
<div class="section" id="operation-mode-characteristic">
<h3>Operation mode characteristic</h3>
<p>The operation mode characteristic is of 2 bytes and contains the configuration information of the nodes. The format is defined as follows:</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 50%">
<col style="width: 50%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="2"><p><strong>1st byte (bit 7 down to 0)</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Bit</p></td>
<td><p>Value</p></td>
</tr>
<tr class="row-odd"><td><p>7</p></td>
<td><p>tag (0), anchor (#.</p></td>
</tr>
<tr class="row-even"><td><p>6 - 5</p></td>
<td><p>UWB - off (0), passive (#.,
active (2)</p></td>
</tr>
<tr class="row-odd"><td><p>4</p></td>
<td><p>firmware 1 (0), firmware 2
(#.</p></td>
</tr>
<tr class="row-even"><td><p>3</p></td>
<td><p>accelerometer enable (0, #.</p></td>
</tr>
<tr class="row-odd"><td><p>2</p></td>
<td><p>LED indication enabled (0,
#.</p></td>
</tr>
<tr class="row-even"><td><p>1</p></td>
<td><p>firmware update enable (0,
#.</p></td>
</tr>
<tr class="row-odd"><td><p>0</p></td>
<td><p>BLE enabled (0,#.</p></td>
</tr>
</tbody>
</table>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 46%">
<col style="width: 54%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="2"><p><strong>2nd byte (bit 7 down to 0)</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Bit</p></td>
<td><p>Value</p></td>
</tr>
<tr class="row-odd"><td><p>7</p></td>
<td><p>initiator enable, anchor
specific (0, #.</p></td>
</tr>
<tr class="row-even"><td><p>6</p></td>
<td><p>low-power mode enable, tag
specific (0, #.</p></td>
</tr>
<tr class="row-odd"><td><p>5</p></td>
<td><p>location engine enable, tag
specific (0, #.</p></td>
</tr>
<tr class="row-even"><td><p>4 - 0</p></td>
<td><p>reserved</p></td>
</tr>
</tbody>
</table>
</div>
<div class="section" id="location-data-characteristic">
<h3>Location data characteristic</h3>
<p>Location data characteristics can contain position, distances or
both. The format of the position and distances are defined as
follows:</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 47%">
<col style="width: 53%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Type (1 byte)</p></th>
<th class="head"><p>Value</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>0 - Position only</p></td>
<td><p>X,Y,Z coordinates (each 4
bytes)+ quality factor (1
byte), size: 13 bytes</p></td>
</tr>
<tr class="row-odd"><td><p>1 - Distances</p></td>
<td><p>The first byte is distance count
(1 byte).</p>
<p>Sequence of node ID (2 bytes),
distance (4 bytes), and
quality factor (1 byte).</p>
<p>Max value contains 15
elements, size: 8 - 106.</p>
</td>
</tr>
<tr class="row-even"><td><p>2 - Position and
Distances</p></td>
<td><p>Encoded Position (as
described above, 13 bytes)
Encoded Distances (as
described above, 8 - 29
bytes) - position and
distances are sent by tag,
number of ranging anchors is
max 4.</p></td>
</tr>
</tbody>
</table>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>The characteristic value might be completely empty (zero length),
meaning that there are neither known positions nor known
distances.</p>
</div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>Although location data mode includes position and distances, it is
still possible to receive distances only in the characteristic in
case a position is unknown.</p>
</div>
</div>
<hr class="docutils">
<div class="section" id="proxy-positions-characteristic">
<h3>Proxy Positions Characteristic</h3>
<p>This characteristic is provided to overcome the limitations of
concurrently connected nodes to the BLE central (mobile device). A
passive node uses this characteristic to stream/notify about tag
position updates.</p>
<p>Data are encoded in this characteristic as follows:</p>
<ul class="simple">
<li><p>1 byte: number of elements (max 5)</p></li>
<li><p>[Sequence] tag position: 2 byte node ID, 13 byte position</p></li>
</ul>
<p>Thus, the maximum size of 5 tag positions is 76 bytes long.</p>
</div>
<hr class="docutils">
<div class="section" id="anchor-specific-characteristics">
<h3>Anchor-specific Characteristics</h3>
<p>An anchor may operate in a special mode called ‘Gateway’ and
‘Initiator’. These are orthogonal and do not influence each other.
Gateway flag is read-only, while the user can set the initiator.
Also, each anchor has a seat number within its cluster.</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 20%">
<col style="width: 20%">
<col style="width: 20%">
<col style="width: 20%">
<col style="width: 20%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>UUID</p></th>
<th class="head"><p>Name</p></th>
<th class="head"><p>Length</p></th>
<th class="head"><p>Value</p></th>
<th class="head"><p>Flags</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><strong>3f0af
d88-7770-46
b0-b5
e7-9fc09959
8964</strong></p></td>
<td><p>Operation
Mode (see
above)</p></td>
<td><p>2 bytes</p></td>
<td><p>Bit 7
in 2nd
byte:</p>
<p>initiator
enable
(0, #.
(see
subsection
Operation
Mode
cha
racteristic
for detail),</p>
</td>
<td><p>RW</p></td>
</tr>
<tr class="row-odd"><td><p><strong>1e63
b1eb-d4ed-4
44e-a
f54-c1e9651
92501</strong></p></td>
<td><p>Device info
(see
above)</p></td>
<td></td>
<td><p>RD
only</p>
<p>operation
flags:
BXXXXXXX
B:
gateway
1/0</p>
</td>
<td><p>RO</p></td>
</tr>
<tr class="row-even"><td><p><strong>f0f26c
9b-2c8c-49a
c-ab6
0-fe03def1b
40c</strong></p></td>
<td><dl class="simple">
<dt>Persisted</dt><dd><p>position</p>
</dd>
</dl>
</td>
<td><p>13
bytes</p></td>
<td><blockquote>
<div><p>X,Y,Z</p>
</div></blockquote>
<p>coordinates
each
4-byte
precision
+
quality
factor
(1 byte,
Value 1
- 100)</p>
</td>
<td><p>WO</p></td>
</tr>
<tr class="row-odd"><td><p><strong>28d0
1d60-89de-4
bfa-b
6e9-651ba59
6232c</strong></p></td>
<td><p>MAC stats</p></td>
<td><p>4 bytes</p></td>
<td><p>Reserved
for
internal
debug MAC
statistics</p></td>
<td><p>RO</p></td>
</tr>
<tr class="row-even"><td><p><strong>17b16
13e-98f2-44
36-bc
de-23af17a1
0c72</strong></p></td>
<td><p>Cluster
info</p></td>
<td><p>5 bytes</p></td>
<td><p>Seat number
(1
by
te)/Cluster
map (2
byt
es)/Cluster
neighbor
map (2
bytes)</p></td>
<td><p>RO</p></td>
</tr>
<tr class="row-odd"><td><p><strong>5b10c4
28-af2f-486
f-aee
1-9dbd79b6b
ccb</strong>
<strong>[Not in
PANS</strong>
<strong>PRO]</strong></p></td>
<td><p>Anchor list</p></td>
<td><p>65
bytes</p></td>
<td><p>Count (1
byte), list
of node  IDs
(2 bytes),
RSSI (1
byte), seat
(1
bytes) max
16 elements
in list [No
longer
available
in PANS PRO
as it is no
longer
ancho
r-specific]</p></td>
<td><p>RO</p></td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="tag-specific-characteristics">
<h3>Tag-specific Characteristics</h3>
<p>Each tag determines its position based on the information sent by
4 surrounding anchors. The tag provides complete information on how
its position is computed (read-only).</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 20%">
<col style="width: 20%">
<col style="width: 20%">
<col style="width: 20%">
<col style="width: 20%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>UUID</p></th>
<th class="head"><p>Name</p></th>
<th class="head"><p>Length</p></th>
<th class="head"><p>Value</p></th>
<th class="head"><p>Flags</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><strong>3f0a
fd88-7770-4
6b0-
b5e7-9fc099
598964</strong></p></td>
<td><p>Operation
Mode (see
above)</p></td>
<td><p>2 bytes</p></td>
<td><p>Bit 6
in 2nd
byte:
low
power
mode
enable
(0, #.
Bit 5
in 2nd
byte:
location
engine
enable
(0, #.
(see
subsection
Operation
Mode
cha
racteristic
for detail)</p></td>
<td><p>RW</p></td>
</tr>
<tr class="row-odd"><td><p><strong>7bd4
7f30-5602-4
389
-b069-83057
31308b6</strong></p></td>
<td><p>Update
rate</p></td>
<td><p>8 bytes</p></td>
<td><p>Layout: U1
(4 bytes),
U2 (4
bytes)
Broadcast
new
position
each <em>U1</em>
ms when
moving,
broadcast
new
position
each <em>U2</em>
ms when
stationary.</p></td>
<td><p>RW</p></td>
</tr>
</tbody>
</table>
</div>
</div>
<hr class="docutils">
<div class="section" id="ble-auto-positioning">
<h2>BLE Auto-Positioning</h2>
<p>The BLE API also makes it possible to initiate an auto-positioning process. The auto-positioning process is finished (positions are computed) on the mobile device. The BLE API makes it possible to initiate distance measurement and retrieval. The workflow is as follows:</p>
<ol class="arabic">
<li><p>Measure:</p>
<blockquote>
<div><ol class="loweralpha simple">
<li><p>Initiator is found and verified (the node must be a <em>real initiator</em>, not just <em>configured</em> <em>as initiator</em>).</p></li>
<li><p>Initiator/network is put to measure distances mode:</p>
<ol class="lowerroman simple">
<li><p>Make sure that location data mode is configured for distances or position  and distances.</p></li>
<li><p>Start observing location data characteristics (setup cccd notification).</p></li>
<li><p>Receive all measured distances from the initiator and save the measured distances to the matrix.</p></li>
<li><p>Stop observation.</p></li>
</ol>
</li>
<li><p>Distances from all other (non-initiator) nodes are retrieved:</p>
<ol class="lowerroman simple">
<li><p>Connect.</p></li>
<li><p>Make sure that location data mode is configured for distances or position and distances.</p></li>
<li><p>Retrieve the value stored in location data characteristic (directly) and save the measured distances to the matrix</p></li>
<li><p>Disconnect.</p></li>
</ol>
</li>
</ol>
</div></blockquote>
</li>
<li><p>Evaluate: evaluate the measure distances, check orthogonality, and compute positions.</p></li>
<li><p>Save the computed positions to nodes (on user request).</p></li>
</ol>
</div>
<hr class="docutils">
<div class="section" id="ble-advertisements">
<h2>BLE Advertisements</h2>
<p>BLE advertisement is a common way for a peripheral device to let
others know its presence. According to BLE spec, The broadcast payload is made of triplets, i.e. [length, type, &lt;data&gt;]. Anchors and
tags will broadcast basic information about their <strong>presence and
operation mode</strong>. The BLE advertisement is not long enough to also
include the position info.</p>
<p>In the BLE advertisement, 31 bytes are used:</p>
<ul class="simple">
<li><p>3 bytes are mandatory flags (one AD triplet).</p></li>
<li><p>The app can use the remaining 28 bytes to fill in AD records (each record has 2 bytes length+type overhead).</p></li>
</ul>
<div class="section" id="presence-broadcast">
<h3>Presence Broadcast</h3>
<p>The BLE on the DWM module works in connectable undirected mode. It
advertises the presence broadcast that contains the availability of
service and some service data. The presence broadcast follows the BLE
advertisement frame structure and makes use of the 28 bytes to
present information.</p>
<p>Since the presence is a broadcast with a connectable flag set to
true, a shortened local name AD record of 8 bytes must be included
here to overcome potential Android BLE stack bugs (as described in
<em>[1]</em>). The remaining bytes are filled with service data: 2 bytes for
the AD record header, 16 bytes UUID, 1 byte shortened operation mode
and 1-byte change counter.</p>
<p>The presence broadcast frame has 3 + 20 + 8 bytes in total, i.e. 31
bytes (out of 31 bytes).The frame structure is shown in the table
below.</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 42%">
<col style="width: 58%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>AD triplet - part
identification</strong></p></th>
<th class="head"><p><strong>Value</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>LEN</p></td>
<td><p>0x02</p></td>
</tr>
<tr class="row-odd"><td><p>TYPE</p></td>
<td><p>0x01 (Flags)</p></td>
</tr>
<tr class="row-even"><td><p>VALUE</p></td>
<td><p>Device/Advertisement flags -
connectable</p></td>
</tr>
<tr class="row-odd"><td><p>LEN</p></td>
<td><p>0x13 (19 in decimal)</p></td>
</tr>
<tr class="row-even"><td><p>TYPE</p></td>
<td><p>0x21 (SERVICE_DAT).</p></td>
</tr>
<tr class="row-odd"><td rowspan="3"><p>VALUE</p></td>
<td><dl class="simple">
<dt>680c21d9-c946-4c1f-9c11-baa1c21329e7</dt><dd><p>(16 bytes)</p>
</dd>
</dl>
</td>
</tr>
<tr class="row-even"><td><p>Bit layout: OXXEFFUU (1
byte)
O - operation mode (tag 0,
anchor #. XX - reserved
E - error indication
FF - flags: initiator,
gateway
UU - UWB: off (0), passive
(#., active (2)</p></td>
</tr>
<tr class="row-odd"><td><p>Change counter (1 byte) -
change counter changes each
time a characteristic gets
changed (except for node
statistics and specifically
for Tag: location dat#..</p></td>
</tr>
<tr class="row-even"><td><p>LEN</p></td>
<td><p>0x07 (max)</p></td>
</tr>
<tr class="row-odd"><td><p>TYPE</p></td>
<td><p>0x08 (Shortened local name)</p></td>
</tr>
<tr class="row-even"><td><p>VALUE</p></td>
<td><p>First 6 letters (or less) of
device local name as defined
by GATT spec.</p></td>
</tr>
</tbody>
</table>
</div>
</div>
<hr class="docutils">
<div class="section" id="ble-firmware-update">
<h2>BLE Firmware Update</h2>
<p>Firmware update functionality is used to update the module’s firmware. It can be performed either over UWB or BLE. This section describes the control and data flow over BLE.</p>
<p>During the FW update, two characteristics, <strong>FW update push</strong> and <strong>FW update poll</strong> are used to implement the request/response protocol.</p>
<p><strong>Initiating FW Update</strong></p>
<p>Steps:</p>
<ol class="arabic simple">
<li><p>The <em>Mobile device</em> (BLE central) sets up an indication on <strong>FW update poll</strong> characteristic changes (CCCD).</p></li>
<li><p>The <em>Mobile device</em> asks the network node if it is willing to perform the update by sending the update request/offer packet to <strong>FW update push</strong> characteristic. This initialization packet contains the firmware version, checksum, and overall firmware binary size (in bytes). This process is reliable write, also known as write with response.</p></li>
</ol>
<ol class="arabic simple" start="3">
<li><p>The <em>Network node</em> responds with indication on the <em>FW update poll</em> in two cases:</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>Case 1: YES, “send me the first data buffer”. see <em>Transmitting the FW binary</em> section for more information;</p></li>
<li><p>Case 2: NO, and <em>error code</em> provides a refuse reason.</p></li>
</ul>
</div></blockquote>
<p>Error states:</p>
<p><strong>Mobile device</strong>: Received explicit NO indication along with error code/reason.
<strong>Resolution</strong>: The <em>Mobile device</em> disables CCCD indication on the <em>FW update poll</em> and notifies the upper layer about the refused reason.
<strong>Network node</strong>: Sudden disconnect
<strong>Resolution</strong>: Leave the FW update mode and reset the current state as if the FW update did not happen.
<strong>Mobile device</strong>: Detects that connection has been closed.
<strong>Resolution</strong>: Retry. If still unsuccessful after 30 seconds from FW update initialization, report to the upper layer. Let the user re-initiate the firmware update on request.</p>
<hr class="docutils">
<div class="section" id="transmitting-the-fw-binary">
<h3>Transmitting the FW binary</h3>
<p>This section is inspired by <em>[2]</em>.</p>
<p>The network Node initiates the data transmission and tells the mobile device precisely which data buffer it requires. This communication is
done using a <em>FW buffer request</em>: size and offset. Mobile device starts sending the requested buffer in small chunks using the write command without response and as such, there is no full round trip involved. The elementary chunk size equals to MTU to fit into a single transmitted packet. The chunk consists of:</p>
<ul class="simple">
<li><p>Data: size should be rounded to a power of 2. The current chunk size is set to 32 bytes.</p></li>
<li><p>Relative offset (from the very beginning): 4 bytes.</p></li>
<li><p>Identification of the message type: FIRMWARE_DATA_CHUNK (= 0x1): 1 byte</p></li>
</ul>
<p>The network node completely drives the  data transmission . After
the data buffer is sent, the mobile device waits for further
instructions. During the transmission, the network node normally asks
for data buffers sequentially, one by one, to get a continuous byte
sequence of firmware. For instance, the node might ask for an
unexpected buffer if there are exceptions, especially in cases where
the current buffer transmission fails.</p>
<p>Error states:</p>
<p><strong>Network node</strong>: data chunks are missing upon receiving (non-continuous sequence), or out-of-order chunks.
<strong>Resolution</strong>: send <em>FW buffer request</em> specifying the missing chunk and the rest of the buffer.
<strong>Mobile device</strong>: receives <em>FW buffer request</em> during ongoing data transmission.
<strong>Resolution</strong>: stop sending data, set the current offset to the one in the <em>FW buffer request</em> and restart data transmission.</p>
</div>
<hr class="docutils">
<div class="section" id="finishing-the-transmission">
<h3>Finishing the transmission</h3>
<p>Once the last data buffer has been successfully received, the network node will inform the mobile device through an indication on the <em>FW update poll</em> that it has received the full firmware binary.</p>
<p>Upon its reception, the mobile device:</p>
<ul class="simple">
<li><p>Disconnects from the network node.</p></li>
<li><p>Waits 500 ms.</p></li>
<li><p>Tries to connect to the network node again and check its firmware status.</p></li>
</ul>
</div>
<hr class="docutils">
<div class="section" id="fw-update-push-poll-format">
<h3>FW update push/poll format</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 28%">
<col style="width: 14%">
<col style="width: 14%">
<col style="width: 15%">
<col style="width: 16%">
<col style="width: 14%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="6"><p>FW update push</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Update offer/request-
Firmware meta</p></td>
<td><p>Type == 0
(1 byte)</p></td>
<td><p>HW version
(4 bytes)</p></td>
<td><p>FW version
(4 bytes)</p></td>
<td><p>FW checksum
(4 bytes)</p></td>
<td><p>size
(4 bytes)</p></td>
</tr>
<tr class="row-odd"><td><p>Firmware data chunk</p></td>
<td><p>type == 1
(1 byte)</p></td>
<td><p>offset
(4 bytes)</p></td>
<td colspan="3"><p>data
(max 32 bytes)</p></td>
</tr>
</tbody>
</table>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 34%">
<col style="width: 34%">
<col style="width: 18%">
<col style="width: 15%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="4"><p>FW update poll</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Firmware buffer request</p></td>
<td><p>type == 1
(1 byte)</p></td>
<td><p>offset
(4 bytes)</p></td>
<td><p>size
(4 bytes)</p></td>
</tr>
<tr class="row-odd"><td><p>Signals</p></td>
<td><p>type ==
0 (upload
refused), 2
(upload
complete),
3 (save failed)
14 (save failed,
invalid
checksum) (1
byte)</p></td>
<td colspan="2"><p>0 bytes</p></td>
</tr>
</tbody>
</table>
</div>
</div>
</div>


           </div>
