---
title: "BLE Interface"
lang: en
slug: "leaps-rtls/integration-guide/leaps-api/ble-interface"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/leaps-rtls/integration-guide/leaps-api/ble-interface/"
order: 131
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="ble-interface">
<h1>BLE Interface</h1>
<div class="section" id="introduction">
<h2>Introduction</h2>
<p>This page describes the LEAPS UWB Subsystem APIs (UWBS) available over the Bluetooth Low Energy (BLE) link.</p>
<p>In the UWBS BLE API design, the UWBS module acts as the BLE peripheral and can be communicated by BLE central devices through the APIs. This document introduces the APIs that the BLE central devices can use for communication.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>In case the Bluetooth on Linux stops working completely, restart the Bluetooth using the following command:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">systemctl restart bluetooth.service</span>
</pre></div>
</div>
</div>
<hr class="docutils">
<div class="section" id="used-terminology">
<h3>Used terminology</h3>
<ul class="simple">
<li><p><strong>UWBS</strong>: The LEAPS UWB Subsystem module. The UWBS acts as a BLE peripheral in the BLE communication.</p></li>
<li><p><strong>CDEV</strong>: The BLE central device that connects to the UWBS peripheral.</p></li>
<li><p><strong>ELDR</strong>: Extended loader.</p></li>
</ul>
</div>
<hr class="docutils">
<div class="section" id="position-representation">
<h3>Position Representation</h3>
<p>In presenting locations and distances in a Real-Time Positioning System, there are two things to consider:</p>
<ul class="simple">
<li><p>Accuracy</p></li>
<li><p>Precision</p></li>
</ul>
<p>Accuracy is the error between the position reported by the nodes and the real position. Currently, the UWBS used in this design provides approximately 10 cm accuracy.</p>
<p>Precision is the value of a least-significant bit (LSB) represented. In the onboard firmware of this system, the precision is 1 mm, i.e. 0.001 meter. The positions are presented in 3-dimensional coordinates (X, Y, Z), where X, Y, and Z each is 32-bit integers (4 bytes). Each LSB represents 1 mm. This is for easier interpretation of the value and easier mathematics over the reported values.</p>
<p>When deciding on the precision, it is important to choose it concerning accuracy to get a meaningful result. It is useless to show the user precise values if accuracy is low. The 1 mm precision is too fine-grained concerning the current 10 cm accuracy. Therefore, in the Android application, a precision of 1 cm, i.e. 0.01 meter, is used. Only when the coordinate/distance has changed over 1 cm will the updated value be presented on the Android application? It is similar to rounding float/double values to a meaningful number of decimal places.</p>
<hr class="docutils">
</div>
</div>
<div class="section" id="ble-communication-with-uwbs">
<span id="blecommunicationwithuwbs"></span><h2>BLE Communication With UWBS</h2>
<div class="line-block">
<div class="line">The BLE central device directly connects with the UWBS to set up and retrieve</div>
<div class="line">parameters. It needs to connect to each device individually to configure/control. The communication with the UWBS is based on request-response model (see <a class="reference internal" href="#ble-gatt-model"><span class="std std-ref">BLE GATT Model</span></a>).</div>
</div>
<div class="line-block">
<div class="line">The UWBS accepts TLV API requests and notifies the central of TLV API response. The BLE central must enable notifications before any request to receive the response. The UWBS supports only one request at a time. See <a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/leaps-api#leapsapi"><span class="std std-ref">LEAPS API</span></a> for details on encoding all TLV frames recognized by the UWBS. Besides accepting requests, the UWBS also generates events. To enable the events:</div>
</div>
<ul class="simple">
<li><p>Enable events in the UWBS by <a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/api-commands/leaps-ble-evt-cfg-set#leaps-ble-evt-cfg-set"><span class="std std-ref">leaps_ble_evt_cfg_set</span></a>.</p></li>
<li><p>enable notification on dedicated characteristic</p></li>
</ul>
<div class="line-block">
<div class="line">The payload of all API requests, responses and events starts with a  2-byte long TLV header where the  first byte corresponds to the type of the frame, followed by second byte representing the the frame’s length. The length should be used to check if the frame is complete when streaming via the BLE characteristics.</div>
</div>
<hr class="docutils">
<div class="section" id="ble-lus-leaps-uart-service-interface">
<h3>BLE LUS (LEAPS UART Service) Interface</h3>
<p>The <a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/leaps-uwbs#leapsuwbs"><span class="std std-ref">LEAPS UWBS</span></a> supports additional <strong>BLE LUS (LEAPS UART Service)</strong> interface, following steps to set up the interface.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>If UART shell is being opened, BLE shell will not be accessed.</p>
</div>
<ol class="arabic">
<li><p>Install the python ble-serial library with below command:</p>
<div class="highlight-Console notranslate"><div class="highlight"><pre><span></span><span class="go">python -m pip install ble-serial==2.7.1</span>
</pre></div>
</div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>If the Windows is being used, please follow additional steps “Additional steps for Windows” in this link <a class="reference external" href="https://github.com/Jakeler/ble-serial">ble-serial</a>.</p>
</div>
</li>
<li><p>Use below command to find device. LEAPS board should appear with name as “LEAPS….”.</p>
<div class="highlight-Console notranslate"><div class="highlight"><pre><span></span><span class="go">ble-scan</span>
</pre></div>
</div>
<p>and the result of successful scan:</p>
<a class="reference internal image-reference" href="../../../../_images/ble-lus-scan.png"><img alt="../../../../_images/ble-lus-scan.png" class="align-center" src="/docs-assets/_images/ble-lus-scan.png" style="width: 920.0px; height: 462.0px;"></a>
</li>
<li><p>To connect serial port, open a terminal and run below commands with MAC addresses found at above steps.</p>
<div class="highlight-Console notranslate"><div class="highlight"><pre><span></span><span class="go">ble-serial -d CA:E5:56:1F:57:3D -r e8573d97-6758-11e9-8860-cb4385c24b83 -w e6bfa235-6758-11e9-979f-5b24c4603eb8 -t 10</span>
</pre></div>
</div>
</li>
<li><p>If successful, it will display as below</p>
<img alt="../../../../_images/ble-lus-passed.png" class="align-center" src="/docs-assets/_images/ble-lus-passed.png">
</li>
<li><p>As the log, the script created a serial port with name as “/tmp/ttyBLE” to communicate with serial port on LEAPS board. Let’s this terminal running, open another terminal and use tools as minicom to access this serial port.</p></li>
<li><p>Press double enter to enter shell.</p></li>
</ol>
<hr class="docutils">
</div>
<div class="section" id="autodisconnect">
<span id="id1"></span><h3>Autodisconnect</h3>
<p>UWBS will terminate the connection automatically after 15 seconds if CDEV does not enable notifications by writing 0x0001 to the CCCD of the characteristic “<strong>API Response</strong>” or “<strong>API Events</strong>” (see <a class="reference internal" href="#ble-gatt-model"><span class="std std-ref">BLE GATT Model</span></a>)</p>
</div>
<hr class="docutils">
<div class="section" id="ble-throughput">
<h3>BLE throughput</h3>
<p>Use the maximum possible ATT MTU and the highest connection priority to  utilize the maximum possible throughput when streaming data to and from UWBS. The maximum MTU supported by the UWBS is 150 bytes. Connection interval preferred by the node is from min 10 ms to max 40 ms, latency 0, timeout 2 sec. Please note that in Bluetooth v4.0 and v4.1, the maximum data length remains at default value regardless of MTU negotiation, which limits the maximum throughput for those Bluetooth versions compared to Bluetooth v4.2 and higher.</p>
</div>
<hr class="docutils">
<div class="section" id="security-encryption">
<h3>Security/encryption</h3>
<div class="line-block">
<div class="line">The system supports two modes of operation on BLE: No encryption or Encryption only (AES-OFB). The encryption features and operation are described in the following section:</div>
</div>
<ul class="simple">
<li><p>Features</p>
<ul>
<li><p>Access control and message integrity (MIC/MAC - Message Integrity Code or Message Authentication Code)</p></li>
<li><p>Confidentiality</p></li>
<li><p>Replay protection</p></li>
</ul>
</li>
<li><p>The wireless encryption on BLE uses AES OFB 128 cipher.</p></li>
<li><p>On an encrypted network, each node which wants to participate in the communication needs to have a 128-bit symmetric key set by the user via</p>
<ul>
<li><p>In the LEAPS Android Manager: via settings</p></li>
<li><p>On module: UART/SPI/UserApp/Shell API</p></li>
</ul>
</li>
<li><p>The encryption/decryption is done in blocks where each block has a fixed size of 16 Bytes. Hence, the encrypted payload size has to be rounded to a multiple of 16 Bytes. In other words, the payload of the message must be aligned to the multiple of 16 bytes if security is enabled. The payload must not be aligned to 16 bytes if encryption is disabled.</p></li>
<li><p>Each message will contain</p>
<ul>
<li><p>Nonce - 16 bytes</p></li>
<li><p>MIC/MAC - 2 bytes</p></li>
<li><p>Payload (aligned to 16 bytes if encryption is enabled)</p></li>
<li><p>See also <a class="reference internal" href="#messageencoding"><span class="std std-ref">Message encoding</span></a></p></li>
</ul>
</li>
<li><p>The picture below explains how the data is encrypted using AES</p>
<ul>
<li><p>In red: secret key and must be protected</p></li>
<li><p>In blue: public data - distributed in every BLE message</p></li>
<li><p>In grey: crypto accelerator / controller</p></li>
<li><p>In yellow: calculated/encrypted blocks</p></li>
<li><p>In green: cleartext / decrypted block</p></li>
</ul>
</li>
</ul>
<img alt="../../../../_images/encryptedusingaes.png" class="align-center" src="/docs-assets/_images/encryptedusingaes.png">
<ul class="simple">
<li><p>The picture below explains how the data is encrypted and chained using AES OFB</p></li>
</ul>
<img alt="../../../../_images/aes_ofb.png" class="align-center" src="/docs-assets/_images/aes_ofb.png">
<img alt="../../../../_images/aes_ofb_02.png" class="align-center" src="/docs-assets/_images/aes_ofb_02.png">
<ul class="simple">
<li><p>Requirements for a node wanting to participate in an encrypted network</p>
<ul>
<li><p>Use correct Nonce for encryption/decryption</p></li>
<li><p>Having 128-bit AES key</p></li>
</ul>
</li>
<li><p>There are two types of nonce - nonce used for message encryption/decryption and nonce used for message integrity check.</p>
<ul>
<li><p>Each encryption/decryption nonce has a length 16 Bytes. The sender generates and embeds the nonce in the sent message. The receiver uses the received nonce as an Initialization Vector (IV) during the decryption.</p></li>
<li><p>Each integrity nonce has a length of 16 Bytes. It is derived from the received message nonce by incrementing it nonce by 1.</p></li>
</ul>
</li>
<li><p>To be resistant to relay attacks, every nonce must be unique, and no nonce should be reused for any message at any time in the network.</p></li>
</ul>
<hr class="docutils">
</div>
<div class="section" id="ble-gatt-model">
<span id="id2"></span><h3>BLE GATT Model</h3>
<p>The <strong>UWBS service</strong> UUID is <strong>680c21d9-c946-4c1f-9c11-baa1c21329e7</strong>. All characteristic values are encoded as little endian as BLE spec suggests.</p>
<hr class="docutils">
<div class="section" id="uwbs-characteristics">
<h4>UWBS Characteristics</h4>
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
<tr class="row-even"><td><p>Std.GAP
service,
label
<strong>0x2A00</strong></p></td>
<td><p>Label</p></td>
<td><p>Var</p></td>
<td><p>UTF-8
encoded
string</p></td>
<td><p>RW</p></td>
</tr>
<tr class="row-odd"><td><p><strong>e6bfa234-
6758-11e9-
979f-5b2
4c4603eb8</strong></p></td>
<td><p>API Request</p></td>
<td><p>Var
50 bytes
max</p></td>
<td><p>message
header +
TLV
encoded
API
request</p></td>
<td><p>WO</p></td>
</tr>
<tr class="row-even"><td><p><strong>e8573d96-
6758-11e9-
8860-cb4
385c24b83</strong></p></td>
<td><p>API
Response</p></td>
<td><p>Var
273
bytes
max</p></td>
<td><p>message
header +
TLV
encoded
API
response</p></td>
<td><p>RO</p></td>
</tr>
<tr class="row-odd"><td><p><strong>003bbdf2-
c634-4b3d-
ab56-7ec889
b89a37</strong></p></td>
<td><p>API
Events</p></td>
<td><p>Var
273
bytes
max</p></td>
<td><p>message
header +
TLV encoded
API events</p></td>
<td><p>RO</p></td>
</tr>
</tbody>
</table>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>The label characteristic is a special one. It is part of the standard mandatory GAP service (0x1800) under the standard Name characteristic (0x2A00).</p>
</div>
<hr class="docutils">
</div>
<div class="section" id="message-encoding">
<span id="messageencoding"></span><h4>Message encoding</h4>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 37%">
<col style="width: 26%">
<col style="width: 37%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Item</p></th>
<th class="head"><p>Length</p></th>
<th class="head"><p>Payload</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><strong>transport header</strong></p></td>
<td><p>2 bytes</p></td>
<td><p>index (1 byte)
total (1 byte)</p></td>
</tr>
<tr class="row-odd"><td><p><strong>nonce</strong></p></td>
<td><p>16 bytes</p></td>
<td><p>message nonce,
irrelevant if
security is turned
off</p></td>
</tr>
<tr class="row-even"><td><p><strong>mic/mac</strong></p></td>
<td><p>2 bytes</p></td>
<td><p>message integrity
check if
encryption is
enabled
or simple sum of
bytes of the
payload if
encryption is
disabled</p></td>
</tr>
<tr class="row-odd"><td><p><strong>payload</strong></p></td>
<td><p>from 0 to 255
bytes</p></td>
<td><p>Value or TLV
encoded frame
(depends on
particular
characteristic)</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="operation-mode">
<span id="operationmode"></span><h4>Operation mode</h4>
<p>Use API request <a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/api-commands/leaps-cfg-get#leaps-cfg-get"><span class="std std-ref">leaps_cfg_get</span></a> to read current configuration. Use <a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/api-commands/leaps-cfg-anchor-set#leaps-cfg-anchor-set"><span class="std std-ref">leaps_cfg_anchor_set</span></a> and <a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/api-commands/leaps-cfg-tag-set#leaps-cfg-tag-set"><span class="std std-ref">leaps_cfg_tag_set</span></a> API request to set UWBS configuration.</p>
</div>
<hr class="docutils">
<div class="section" id="location-data">
<h4>Location data</h4>
<p>Use API request <a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/api-commands/leaps-loc-get#leaps-loc-get"><span class="std std-ref">leaps_loc_get</span></a> to read location data containing position, distances or both. Use requests <a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/api-commands/leaps-pos-set#leaps-pos-set"><span class="std std-ref">leaps_pos_set</span></a> and <a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/api-commands/leaps-pos-get#leaps-pos-get"><span class="std std-ref">leaps_pos_get</span></a> to manipulate the UWBS position alone.</p>
<p>Enable event “location data ready” by <a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/api-commands/leaps-ble-evt-cfg-set#leaps-ble-evt-cfg-set"><span class="std std-ref">leaps_ble_evt_cfg_set</span></a> and receive notifications on the characteristic “events” to automatically get current position and distances from the UWBS.</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 13%">
<col style="width: 13%">
<col style="width: 18%">
<col style="width: 18%">
<col style="width: 18%">
<col style="width: 18%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="6"><p>Location data encoding, received as BLE notification of
characteristic “events”</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="2"><p>type</p></td>
<td rowspan="2"><p>length</p></td>
<td colspan="4"><p>value</p></td>
</tr>
<tr class="row-odd"><td><p>int32_t-
little
endian, is
x coordinate
in millimeters</p></td>
<td><p>int32_t-
little
endian, is
y coordinate
in millimeters</p></td>
<td><p>int32_t-
little
endian, is
z coordinate
in millimeters</p></td>
<td><p>uint8_t-
is position
quality factor
in percents
(0-100)</p></td>
</tr>
<tr class="row-even"><td><p>0x41</p></td>
<td><p>0x0D</p></td>
<td colspan="4"><p>0x4b
0x0a
0x00
0x00
0x1f
0x04
0x00
0x00
0x9c
0x0e
0x00
0x00
0x64</p></td>
</tr>
</tbody>
</table>
<div class="line-block">
<div class="line">Type 0x40 means request/command status</div>
<div class="line">Type 0x41 means position</div>
</div>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 8%">
<col style="width: 8%">
<col style="width: 14%">
<col style="width: 14%">
<col style="width: 14%">
<col style="width: 14%">
<col style="width: 14%">
<col style="width: 14%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="8"><p>Residue of the frame from previous table</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>type</p></td>
<td><p>Length</p></td>
<td colspan="6"><p>value</p></td>
</tr>
<tr class="row-odd"><td></td>
<td></td>
<td><p>uint8_t -
number of
distances
encoded
in the value</p></td>
<td><p>uint16_t - UWB
address in
little endian</p></td>
<td><p>uint32_t -
distance in
millimeters in
little endian</p></td>
<td><p>uint8_t -
distance
quality factor
in percents
(0-100)</p></td>
<td><p>position in
standard 13
byte format
(x,y,z,qf)</p></td>
<td><p>…</p></td>
</tr>
<tr class="row-even"><td><p>0x49</p></td>
<td><p>0x51</p></td>
<td><p>0x04</p></td>
<td colspan="4"><p>position and distance nr. 1</p></td>
<td><p>nr. 2, 3, 4</p></td>
</tr>
</tbody>
</table>
<p>Type 0x49 means position and distances of ranging anchors</p>
<hr class="docutils">
</div>
<div class="section" id="user-data">
<span id="userdata"></span><h4>User Data</h4>
<p>Enable event “user data ready” by <a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/api-commands/leaps-ble-evt-cfg-set#leaps-ble-evt-cfg-set"><span class="std std-ref">leaps_ble_evt_cfg_set</span></a> and receive notifications on the characteristic “events” to automatically receive BLE user data from the UWBS automatically.</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>BLE user data
encoding, received
as BLE
notification of
characteristic
“events”</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="2"><p>type</p></td>
<td rowspan="2"><p>length</p></td>
<td><p>value</p></td>
</tr>
<tr class="row-odd"><td><p>max 128 bytes</p></td>
</tr>
<tr class="row-even"><td><p>0x51</p></td>
<td><p>0x80</p></td>
<td><p>0x01 0x02 0x03 …
0x7F 0x80</p></td>
</tr>
</tbody>
</table>
</div>
<div class="section" id="node-id">
<span id="id3"></span><h4>Node id</h4>
<p>Use request <a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/api-commands/leaps-node-id-get#leaps-node-id-get"><span class="std std-ref">leaps_node_id_get</span></a> to read the address of the UWBS.</p>
</div>
<div class="section" id="network-id">
<span id="networkid"></span><h4>Network id</h4>
<p>Use requests <a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/api-commands/leaps-panid-set#leaps-panid-set"><span class="std std-ref">leaps_panid_set</span></a> and <a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/api-commands/leaps-panid-get#leaps-panid-get"><span class="std std-ref">leaps_panid_get</span></a> to manipulate the ID of the network.</p>
</div>
<div class="section" id="reset-or-reboot">
<span id="id4"></span><h4>Reset or reboot</h4>
<p>Requests which reset the UWBS like <a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/api-commands/leaps-reset#leaps-reset"><span class="std std-ref">leaps_reset</span></a> or <a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/api-commands/leaps-factory-reset#leaps-factory-reset"><span class="std std-ref">leaps_factory_reset</span></a> will disconnect the BLE central before reset. The central should wait 1 sec before connecting again.</p>
</div>
<div class="section" id="anchor-list">
<span id="id5"></span><h4>Anchor list</h4>
<p>See request <a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/api-commands/leaps-anchor-list-get#leaps-anchor-list-get"><span class="std std-ref">leaps_anchor_list_get</span></a>.</p>
</div>
<div class="section" id="device-info">
<span id="deviceinfo"></span><h4>Device info</h4>
<p>See request <a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/api-commands/leaps-dev-info-get#leaps-dev-info-get"><span class="std std-ref">leaps_dev_info_get</span></a> to read the version of firmware, hardware and configuration.</p>
</div>
<div class="section" id="update-rate">
<span id="updaterate"></span><h4>Update rate</h4>
<p>See request <a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/api-commands/leaps-upd-rate-set#leaps-upd-rate-set"><span class="std std-ref">leaps_upd_rate_set</span></a> and <a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/api-commands/leaps-upd-rate-get#leaps-upd-rate-get"><span class="std std-ref">leaps_upd_rate_get</span></a> to change the update rate of the tag node.</p>
<hr class="docutils">
</div>
</div>
<div class="section" id="auto-positioning">
<span id="autopositioning"></span><h3>Auto-positioning</h3>
<p>The BLE API also makes it possible to initiate an auto-positioning process. The auto-positioning process is finished (positions are computed) on the CDEV. The BLE API just makes it possible to initiate distance measurement and retrieval. The workflow is as follows:</p>
<ol class="arabic">
<li><p>Measure:</p>
<blockquote>
<div><ol class="loweralpha simple">
<li><p>Initiator is found and verified (the node must be a <em>real initiator</em>, not just <em>configured as initiator</em>, see <a class="reference internal" href="#operationmode"><span class="std std-ref">Operation mode</span></a> and <a class="reference internal" href="#bleadvertisements"><span class="std std-ref">BLE Advertisements</span></a>)</p></li>
<li><p>Connect to initiator.</p></li>
<li><p>Enable “location ready” event by <a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/api-commands/leaps-ble-evt-cfg-set#leaps-ble-evt-cfg-set"><span class="std std-ref">leaps_ble_evt_cfg_set</span></a> if not enabled already (don’t forget to enable BLE cccd notifications on characteristics).</p></li>
<li><p>Start autopositioning by <a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/api-commands/leaps-autopos-start#leaps-autopos-start"><span class="std std-ref">leaps_autopos_start</span></a> request.</p></li>
<li><p>Received all measured distances from the initiator, save the measured distances to the matrix.</p></li>
<li><p>Disconnect from initiator.</p></li>
<li><p>Get distances from all other (non-initiator) nodes:</p></li>
</ol>
<blockquote>
<div><ol class="lowerroman simple">
<li><p>Connect</p></li>
<li><p>Get location data from UWBS using API request <a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/api-commands/leaps-loc-get#leaps-loc-get"><span class="std std-ref">leaps_loc_get</span></a> and save the distances to the matrix.</p></li>
<li><p>Disconnect</p></li>
</ol>
</div></blockquote>
</div></blockquote>
</li>
<li><p>Evaluate the measure distances, check orthogonality, and compute positions.</p></li>
<li><p>Save the computed positions to nodes on user request (use <a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/api-commands/leaps-pos-set#leaps-pos-set"><span class="std std-ref">leaps_pos_set</span></a> request).</p></li>
</ol>
<hr class="docutils">
</div>
<div class="section" id="ble-advertisements">
<span id="bleadvertisements"></span><h3>BLE Advertisements</h3>
<p>BLE advertisement is a common way for a peripheral device to let others know its presence. According to BLE specification, The broadcast payload is made of triplets, i.e. [length, type, &lt;data&gt;].</p>
<p>The UWBS will broadcast basic information about their <strong>presence and operation mode</strong>. The BLE advertisement is not long enough to also include the position info.</p>
<p>In the BLE advertisement there are 31 bytes to be used:</p>
<ul class="simple">
<li><p>3 bytes are mandatory flags (one AD triplet).</p></li>
<li><p>The rest 28 bytes can be used by the app to fill in AD record (each record has 2 bytes length+type overhead)</p></li>
</ul>
<div class="section" id="presence-broadcast">
<h4>Presence Broadcast</h4>
<p>The BLE on the UWBS module works in connectable undirected mode. It advertises the presence broadcast, which contains the availability of service and some service data. The presence broadcast follows the BLE advertisement frame structure and makes use of 28 bytes to present information. The device name is placed in the scan response and requires active scanning.</p>
<p>The presence broadcast and the scan response encoding are described in the table below.</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 45%">
<col style="width: 55%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>Advertising</strong></p></th>
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
<td><p>0x19 (25 dec)</p></td>
</tr>
<tr class="row-even"><td><p>TYPE</p></td>
<td><p>0x21 (33 dec, Service data)</p></td>
</tr>
<tr class="row-odd"><td rowspan="8"><p>VALUE</p></td>
<td><p><strong>680c2
1d9-c946-4c1f-9c11-baa1c21329e7</strong>
(16 bytes)</p></td>
</tr>
<tr class="row-even"><td><p>PAN ID (2 bytes)</p></td>
</tr>
<tr class="row-odd"><td><p>Node ID (2 bytes)</p></td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line">Flags (1 byte)</div>
<div class="line">Bit layout: OXSEIBUU O -
operation mode (tag 0,
anchor 1)</div>
<div class="line">X - reserved</div>
<div class="line">S - security_enabled</div>
<div class="line">E - error indication</div>
<div class="line">I - initiator_enabled,</div>
<div class="line">B - gateway_enabled</div>
<div class="line">UU - UWB mode: off (0),
passive (1), active (2)</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><p>Change counter (1 byte) -
change counter changes each
time the important internal
state of the UWBS change (e.g.
configuration)</p></td>
</tr>
<tr class="row-even"><td><p>UWB counter (1 byte) -
counting-down counter used by
low-power devices. When this
counter on a LP device reaches
0, the device’s UWB activity
is disabled. When anchor
detects this counter on a
device reaching below a
configured low water mark
value, anchor connects to the
device and resets the counter
to keep device’s UWB active.</p></td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line">UWBS Flags (1 byte)</div>
<div class="line">Bit layout: FUSR</div>
</div>
<div class="line-block">
<div class="line">F - Firmware Type (2 bits, 0=BLDR,
1=ELDR, 2=MAIN)</div>
<div class="line">U - UWB System (2 bits, 0=LEAPS RTLS,
1=FIRA)</div>
<div class="line">S - UWB Sub System (2 bits, 0=UCI,
1=NIQ)</div>
<div class="line">R - reserved,</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>Customer information (1 byte)
Specific information for
customer</p></td>
</tr>
</tbody>
</table>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 45%">
<col style="width: 55%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="2"><p><strong>Scan response</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>LEN</p></td>
<td><p>0x16 (22 dec)</p></td>
</tr>
<tr class="row-odd"><td><p>TYPE</p></td>
<td><p>0x09 (Device name, placed in
scan response packet, use
active scanning to detect it)</p></td>
</tr>
<tr class="row-even"><td><p>VALUE</p></td>
<td><p>“LEAPS” prefix (5 characters)
+ full node ID in hex format
(16 characters)</p></td>
</tr>
</tbody>
</table>
</div>
</div>
<div class="section" id="firmware-update">
<span id="firmwareupdate"></span><h3>Firmware Update</h3>
<p>Firmware update functionality is used to update the UWBS’s firmware. This section describes the control and data flow over the BLE interface. Refer to API requests <a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/api-commands/leaps-fw-update-start#leaps-fw-update-start"><span class="std std-ref">leaps_fw_update_start</span></a> and <a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/api-commands/leaps-fw-update-xfer#leaps-fw-update-xfer"><span class="std std-ref">leaps_fw_update_xfer</span></a> for more details on firmware update process.</p>
<div class="section" id="updating-the-fw-binary">
<h4>Updating the FW binary</h4>
<ol class="arabic simple">
<li><p>CDEV connects to the UWBS.</p></li>
<li><p>CDEV starts updating the FW by <a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/api-commands/leaps-fw-update-start#leaps-fw-update-start"><span class="std std-ref">leaps_fw_update_start</span></a>.</p></li>
<li><p>If UWBS responds with the status “ok” CDEV can skip this step. If UWBS responds with the status “again” CDEV resets UWBS and reconnects after the UWBS reboot, and the CDEV starts the update again. If UWBS responds with the status “not permitted”, then fw update is not possible. Fw update might be disabled in UWBS.</p></li>
<li><p>CDEV sends chunks of FW by <a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/api-commands/leaps-fw-update-xfer#leaps-fw-update-xfer"><span class="std std-ref">leaps_fw_update_xfer</span></a>.</p></li>
<li><p>CDEV resets the UWBS after the last chunk is sent successfully.</p></li>
</ol>
</div>
<div class="section" id="updating-the-eldr-binary">
<h4>Updating the ELDR binary</h4>
<ol class="arabic simple">
<li><p>CDEV reconnects after the UWBS reboot.</p></li>
<li><p>CDEV starts updating the ELDR by <a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/api-commands/leaps-fw-update-start#leaps-fw-update-start"><span class="std std-ref">leaps_fw_update_start</span></a>.</p></li>
<li><p>CDEV sends chunks of ELDR by <a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/api-commands/leaps-fw-update-xfer#leaps-fw-update-xfer"><span class="std std-ref">leaps_fw_update_xfer</span></a>.</p></li>
<li><p>CDEV resets the UWBS after the last chunk is sent successfully.</p></li>
<li><p>CDEV can connect after the UWBS reboot and observe the FW info to verify that the firmware was updated is running.</p></li>
</ol>
<p>CDEV should enable notification on the <strong>API response”</strong> characteristic each time it connects to the UWBS to prevent automatic disconnection of the UWBS (see <a class="reference internal" href="#autodisconnect"><span class="std std-ref">Autodisconnect</span></a>).</p>
<p>Sudden disconnection of the UWBS during the firmware update can be handled by starting again from either step 7 or step 1, depending on the current phase of the update.</p>
</div>
<div class="section" id="transmitting-the-fw-binary">
<h4>Transmitting the FW binary</h4>
<p>The data is transferred to UWBS by <a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/api-commands/leaps-fw-update-xfer#leaps-fw-update-xfer"><span class="std std-ref">leaps_fw_update_xfer</span></a> after the firmware update is initiated by the <a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/api-commands/leaps-fw-update-start#leaps-fw-update-start"><span class="std std-ref">leaps_fw_update_start</span></a>. UWBS tells the CDEV precisely which data buffer it wants by encoding the size and the offset into the response. CDEV starts sending the requested buffer chunk using write without response, so no full round trip involved. Note that each chunk could be transmitted by more than 1 BLE transfer if the MTU of BLE transfer could not contain the requested buffer size. The chunk consists of:</p>
<ul class="simple">
<li><p>Data: fw buffer with size requested by UWBS (240)</p></li>
<li><p>Relative offset (from the very beginning): 4 bytes.</p></li>
</ul>
<p>After the data buffer is sent, CDEV waits for further instructions. During the transmission, the UWBS typically asks for a data buffer sequentially, one by one, to get a continuous byte sequence of firmware. The node might ask for an unexpected buffer if exceptions happen, for example, the current buffer transmission fails.</p>
<p>Firmware update is stopped in case of an error and needs to be started again.</p>
</div>
<div class="section" id="finishing-the-transmission">
<h4>Finishing the transmission</h4>
<p>Once the last data chunk has been successfully received, the UWBS will let the CDEV know it has received the full firmware binary. Upon its reception:</p>
<ol class="arabic simple">
<li><p>CDEV resets the UWBS by <a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/api-commands/leaps-reset#leaps-reset"><span class="std std-ref">leaps_reset</span></a> command which will cause UWBS to disconnect from the CDEV.</p></li>
<li><p>CDEV waits 1 sec.</p></li>
<li><p>CDEV tries to connect to UWBS again and check its firmware status (see <a class="reference internal" href="#deviceinfo"><span class="std std-ref">Device info</span></a>).</p></li>
</ol>
</div>
</div>
</div>
<div class="section" id="appendix-bibliography">
<h2>Appendix - Bibliography</h2>
<ol class="arabic simple">
<li><p><a class="reference external" href="https://devzone.nordicsemi.com/question/55309/connection-issues-with-android-60-marshmallow-and-nexus-6/">https://devzone.nordicsemi.com/question/55309/connection-issues-with-android-60-marshmallow-and-nexus-6/</a></p></li>
<li><p><a class="reference external" href="http://stackoverflow.com/questions/37151579/schemes-for-streaming-data-with-ble-gatt-characteristics">http://stackoverflow.com/questions/37151579/schemes-for-streaming-data-with-ble-gatt-characteristics</a></p></li>
<li><p><a class="reference external" href="https://devzone.nordicsemi.com/nordic/nordic-blog/b/blog/posts/what-to-keep-in-mind-when-developing-your-ble-andr">What to keep in mind when developing your BLE Android app</a></p></li>
<li><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide#leaps-rtls-integration-guie"><span class="std std-ref">Integration Guide</span></a></p></li>
</ol>
</div>
<div class="section" id="appendix-migration-from-dwm-ble-api">
<h2>Appendix - migration from DWM BLE API</h2>
<p>The following table summarizes changes in LEAPS BLE API compared to the former DWM BLE API. This is intended to make the transition to LEAPS BLE API easier. The former GATT model used in DWM BLE API is replaced with a request/response model with fewer characteristic than the former model, see the section  <a class="reference internal" href="#blecommunicationwithuwbs"><span class="std std-ref">BLE Communication With UWBS</span></a>.</p>
<div class="section" id="former-ble-gatt-model">
<h3>Former BLE GATT model</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 37%">
<col style="width: 63%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><div class="line-block">
<div class="line"><strong>name of</strong></div>
<div class="line"><strong>former GATT
characteristic</strong></div>
</div>
</th>
<th class="head"><p><strong>DWM and LEAPS comparison</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Label</p></td>
<td><div class="line-block">
<div class="line">DWM: <em>Standard mandatory GAP
service (0x1800) under the
standard Name characteristic
(0x2A00)</em></div>
<div class="line">LEAPS: no changes, stays the
same</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><p>Operation mode</p></td>
<td><div class="line-block">
<div class="line">DWM: current configuration
of UWBS was contained in
special</div>
<div class="line">characteristic</div>
<div class="line">LEAPS: see <a class="reference internal" href="#operationmode"><span class="std std-ref">Operation mode</span></a>
to read/write configuration
of UWBS, see <a class="reference internal" href="#firmwareupdate"><span class="std std-ref">Firmware Update</span></a>
to switch between
firmware 1 and firmware 2.</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>Update rate</p></td>
<td><p>DWM: current update rate was
contained in special
characteristic LEAPS: see
section <a class="reference internal" href="#updaterate"><span class="std std-ref">Update rate</span></a> to
read/write current update rate
configuration</p></td>
</tr>
<tr class="row-odd"><td><p>Network ID</p></td>
<td><p>DWM: current network Id was
contained in special
characteristic LEAPS: see the section
<a class="reference internal" href="#networkid"><span class="std std-ref">Network id</span></a> to read/write
current network ID</p></td>
</tr>
<tr class="row-even"><td><p>Location data mode</p></td>
<td><p>DWM: used as a setting for a
special characteristic called
“Location data”. LEAPS: not
needed anymore, see <a class="reference internal" href="#userdata"><span class="std std-ref">User Data</span></a>
to get the location from the
UWBS and see the section
<a class="reference internal" href="#autopositioning"><span class="std std-ref">Auto-positioning</span></a> to get
distances when doing
auto-positioning procedure</p></td>
</tr>
<tr class="row-odd"><td><p>Location data</p></td>
<td><p>DWM: current location of UWBS
(that also contained the
distances when
doing auto-positioning
procedure) was contained in a
special characteristic LEAPS:
see the section <em>Location data</em> to
get location and distances</p></td>
</tr>
<tr class="row-even"><td><p>Persisted position</p></td>
<td><div class="line-block">
<div class="line">DWM: persisted position was
written via a special
characteristic</div>
<div class="line">LEAPS: the see the section  <a class="reference internal" href="#userdata"><span class="std std-ref">User Data</span></a>
on how to write
persistent position to the
UWBS</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><p>Device info</p></td>
<td><div class="line-block">
<div class="line">DWM: device information, like
configuration, node ID, and
firmware</div>
<div class="line">version was read from a
special characteristic</div>
<div class="line">LEAPS: see the section <a class="reference internal" href="#deviceinfo"><span class="std std-ref">Device info</span></a>
to read the node firmware
version, see the section  <a class="reference internal" href="#node-id"><span class="std std-ref">Node id</span></a>
to read the ID of the node
and see the section  <a class="reference internal" href="#operationmode"><span class="std std-ref">Operation mode</span></a>
to read the node
configuration</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>Statistics</p></td>
<td><p>DWM: statistics were contained
in a special characteristic
LEAPS: statistics are no longer
supported</p></td>
</tr>
<tr class="row-odd"><td><p>MAC stats</p></td>
<td><p>DWM: MAC statistics were
contained in a special
characteristic LEAPS: MAC
statistics is no longer
supported</p></td>
</tr>
<tr class="row-even"><td><p>Cluster info</p></td>
<td><p>DWM: the UWB cluster information
was contained in a special
characteristic LEAPS: cluster
information is no longer
supported</p></td>
</tr>
<tr class="row-odd"><td><p>Anchor list</p></td>
<td><div class="line-block">
<div class="line">DWM: the current list of
neighbour anchor nodes was
contained in a special
characteristic</div>
<div class="line">LEAPS: see the section  <a class="reference internal" href="#anchor-list"><span class="std std-ref">Anchor list</span></a>
to read the current list
of anchor nodes</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>FW update push</p></td>
<td><div class="line-block">
<div class="line">DWM: firmware update was
started via a special
characteristic that also
used to transfer the new
firmware into the UWBS</div>
<div class="line">LEAPS: see the section <a class="reference internal" href="#firmwareupdate"><span class="std std-ref">Firmware Update</span></a>
on how to start
firmware update and on how
to transfer  the firmware into
the node</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><p>FW update poll</p></td>
<td><div class="line-block">
<div class="line">DWM: UWBS responded to the BLE
central during firmware
update using notifications
on this characteristic</div>
<div class="line">LEAPS: see the section  <a class="reference internal" href="#firmwareupdate"><span class="std std-ref">Firmware Update</span></a>
on how to perform
firmware update</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>Disconnect</p></td>
<td><div class="line-block">
<div class="line">DWM: BLE central disconnects
via a special characteristic,
it was workaround to deal
with the API bug</div>
<div class="line">LEAPS: not supported since
the bug is fixed</div>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</div>
</div>


           </div>
