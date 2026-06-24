---
title: "MQTT Message Reference"
lang: en
slug: "leaps-rtls/integration-guide/leaps-api/mqtt-message-reference"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/leaps-rtls/integration-guide/leaps-api/mqtt-message-reference/"
order: 79
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="mqtt-message-reference">
<span id="leaps-mqtt-message-reference"></span><h1>MQTT Message Reference</h1>
<hr class="docutils">
<div class="section" id="common">
<h2>Common</h2>
<div class="section" id="anchor-config">
<span id="id1"></span><h3>anchor_config</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 14%">
<col style="width: 35%">
<col style="width: 12%">
<col style="width: 39%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Field</p></th>
<th class="head"><p>Type</p></th>
<th class="head"><p>Label</p></th>
<th class="head"><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>initiator</p></td>
<td><p>bool</p></td>
<td><p>required</p></td>
<td><p>UWB initiator mode enable.</p></td>
</tr>
<tr class="row-odd"><td><p>location</p></td>
<td><p><a class="reference internal" href="#node-location"><span class="std std-ref">node_location</span></a></p></td>
<td><p>required</p></td>
<td><p>Location of the node.</p></td>
</tr>
<tr class="row-even"><td><p>routing</p></td>
<td><p><a class="reference internal" href="#routing-config"><span class="std std-ref">routing_config</span></a></p></td>
<td><p>required</p></td>
<td><p>Routing configuration.</p></td>
</tr>
<tr class="row-odd"><td><p>bridge</p></td>
<td><p>bool</p></td>
<td><p>optional</p></td>
<td><p>UWB bridge mode enable.</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="node-location">
<span id="id2"></span><h3>node_location</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 6%">
<col style="width: 33%">
<col style="width: 7%">
<col style="width: 54%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Field</p></th>
<th class="head"><p>Type</p></th>
<th class="head"><p>Label</p></th>
<th class="head"><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>x</p></td>
<td><p>float</p></td>
<td><p>required</p></td>
<td><p>X coordinate in meters.</p></td>
</tr>
<tr class="row-odd"><td><p>y</p></td>
<td><p>float</p></td>
<td><p>required</p></td>
<td><p>Y coordinate in meters.</p></td>
</tr>
<tr class="row-even"><td><p>z</p></td>
<td><p>float</p></td>
<td><p>required</p></td>
<td><p>Z coordinate in meters.</p></td>
</tr>
<tr class="row-odd"><td><p>quality</p></td>
<td><p>uint32</p></td>
<td><p>required</p></td>
<td><p>Quality factor from 0% to 100%.</p></td>
</tr>
<tr class="row-even"><td><p>sd_x</p></td>
<td><p>float</p></td>
<td><p>optional</p></td>
<td><p>Standard deviation of X coordinate in meters.</p></td>
</tr>
<tr class="row-odd"><td><p>sd_y</p></td>
<td><p>float</p></td>
<td><p>optional</p></td>
<td><p>Standard deviation of Y coordinate in meters.</p></td>
</tr>
<tr class="row-even"><td><p>sd_z</p></td>
<td><p>float</p></td>
<td><p>optional</p></td>
<td><p>Standard deviation of Z coordinate in meters.</p></td>
</tr>
<tr class="row-odd"><td><p>r95</p></td>
<td><p>float</p></td>
<td><p>optional</p></td>
<td><p>R95 of locations in meters.</p></td>
</tr>
<tr class="row-even"><td><p>x_err</p></td>
<td><p>float</p></td>
<td><p>optional</p></td>
<td><p>Error of X coordinate compared to reference location in meters.</p></td>
</tr>
<tr class="row-odd"><td><p>y_err</p></td>
<td><p>float</p></td>
<td><p>optional</p></td>
<td><p>Error of Y coordinate compared to reference location in meters.</p></td>
</tr>
<tr class="row-even"><td><p>z_err</p></td>
<td><p>float</p></td>
<td><p>optional</p></td>
<td><p>Error of Z coordinate compared to reference location in meters.</p></td>
</tr>
<tr class="row-odd"><td><p>toa</p></td>
<td><p><a class="reference internal" href="#node-toa-measurement-statistics"><span class="std std-ref">node_toa_measurement_statistics</span></a></p></td>
<td><p>repeated</p></td>
<td><p>Statistics of Time Of Arrival measurements.</p></td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="node-status">
<h3>node_status</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 13%">
<col style="width: 22%">
<col style="width: 8%">
<col style="width: 57%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Field</p></th>
<th class="head"><p>Type</p></th>
<th class="head"><p>Label</p></th>
<th class="head"><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>origins</p></td>
<td><p><a class="reference internal" href="#origin-info"><span class="std std-ref">origin_info</span></a></p></td>
<td><p>repeated</p></td>
<td><p>List of origins.</p></td>
</tr>
<tr class="row-odd"><td><p>profile</p></td>
<td><p><a class="reference internal" href="#uwb-profile"><span class="std std-ref">uwb_profile</span></a></p></td>
<td><p>optional</p></td>
<td><p>Current UWB profile.</p></td>
</tr>
<tr class="row-even"><td><p>uwb</p></td>
<td><p><a class="reference internal" href="#uwb-status"><span class="std std-ref">uwb_status</span></a></p></td>
<td><p>optional</p></td>
<td><p>UWB status.</p></td>
</tr>
<tr class="row-odd"><td><p>sensor</p></td>
<td><p><a class="reference internal" href="#sensor-status"><span class="std std-ref">sensor_status</span></a></p></td>
<td><p>optional</p></td>
<td><p>Status of the sensors.</p></td>
</tr>
<tr class="row-even"><td><p>route_active</p></td>
<td><p>bool</p></td>
<td><p>optional</p></td>
<td><p>Indicate the gateway is a route candidate for the node.</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="node-toa-measurement-statistics">
<span id="id3"></span><h3>node_toa_measurement_statistics</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 12%">
<col style="width: 12%">
<col style="width: 11%">
<col style="width: 66%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Field</p></th>
<th class="head"><p>Type</p></th>
<th class="head"><p>Label</p></th>
<th class="head"><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>anchor_id</p></td>
<td><p>uint32</p></td>
<td><p>required</p></td>
<td><p>Anchor ID.</p></td>
</tr>
<tr class="row-odd"><td><p>sd_tdoa</p></td>
<td><p>float</p></td>
<td><p>required</p></td>
<td><p>Standard deviation of Time of Arrival measurement.</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="origin-info">
<span id="id4"></span><h3>origin_info</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 24%">
<col style="width: 24%">
<col style="width: 22%">
<col style="width: 30%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Field</p></th>
<th class="head"><p>Type</p></th>
<th class="head"><p>Label</p></th>
<th class="head"><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>id</p></td>
<td><p>uint64</p></td>
<td><p>required</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>hop_level</p></td>
<td><p>uint32</p></td>
<td><p>required</p></td>
<td></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="sensor-status">
<span id="id5"></span><h3>sensor_status</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 12%">
<col style="width: 8%">
<col style="width: 7%">
<col style="width: 72%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Field</p></th>
<th class="head"><p>Type</p></th>
<th class="head"><p>Label</p></th>
<th class="head"><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>batt</p></td>
<td><p>uint32</p></td>
<td><p>required</p></td>
<td><p>Battery level in mV.</p></td>
</tr>
<tr class="row-odd"><td><p>batt_state</p></td>
<td><p>uint32</p></td>
<td><p>optional</p></td>
<td><p>Indicates the battery status, 0-Unknown | 1-Empty | 2-Low | 3-Medium | 4-Full.</p></td>
</tr>
<tr class="row-even"><td><p>temp</p></td>
<td><p>int32</p></td>
<td><p>required</p></td>
<td><p>Temperature in degrees.</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="service-data">
<span id="id6"></span><h3>service_data</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 4%">
<col style="width: 20%">
<col style="width: 7%">
<col style="width: 70%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Field</p></th>
<th class="head"><p>Type</p></th>
<th class="head"><p>Label</p></th>
<th class="head"><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>type</p></td>
<td><p><a class="reference internal" href="#service-type"><span class="std std-ref">service_type</span></a></p></td>
<td><p>required</p></td>
<td><p>Type of the service request or the type of the response. Refer to <a class="reference internal" href="#service-type"><span class="std std-ref">service_type</span></a>.</p></td>
</tr>
<tr class="row-odd"><td><p>data</p></td>
<td><p>bytes</p></td>
<td><p>optional</p></td>
<td><p>Opaque service data bytes encoded as base64.</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="signup-request">
<span id="id7"></span><h3>signup_request</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 13%">
<col style="width: 34%">
<col style="width: 13%">
<col style="width: 39%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Field</p></th>
<th class="head"><p>Type</p></th>
<th class="head"><p>Label</p></th>
<th class="head"><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>release</p></td>
<td><p><a class="reference internal" href="#version-info"><span class="std std-ref">version_info</span></a></p></td>
<td><p>optional</p></td>
<td><p>Version of the release.</p></td>
</tr>
<tr class="row-odd"><td><p>firmware</p></td>
<td><p><a class="reference internal" href="#version-info"><span class="std std-ref">version_info</span></a></p></td>
<td><p>repeated</p></td>
<td><p>Version of the firmware.</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="signup-response">
<span id="id8"></span><h3>signup_response</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 12%">
<col style="width: 29%">
<col style="width: 12%">
<col style="width: 47%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Field</p></th>
<th class="head"><p>Type</p></th>
<th class="head"><p>Label</p></th>
<th class="head"><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>status</p></td>
<td><p>bool</p></td>
<td><p>required</p></td>
<td><p>Statue/result of the signup.</p></td>
</tr>
<tr class="row-odd"><td><p>firmware</p></td>
<td><p><a class="reference internal" href="#version-info"><span class="std std-ref">version_info</span></a></p></td>
<td><p>required</p></td>
<td><p>Current version of the firmware.</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="tag-config">
<span id="id9"></span><h3>tag_config</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 20%">
<col style="width: 19%">
<col style="width: 7%">
<col style="width: 54%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Field</p></th>
<th class="head"><p>Type</p></th>
<th class="head"><p>Label</p></th>
<th class="head"><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>location_engine</p></td>
<td><p>bool</p></td>
<td><p>required</p></td>
<td><p>Internal location engine enable.</p></td>
</tr>
<tr class="row-odd"><td><p>low_power</p></td>
<td><p>bool</p></td>
<td><p>required</p></td>
<td><p>Low power mode enable.</p></td>
</tr>
<tr class="row-even"><td><p>stationary_detection</p></td>
<td><p>bool</p></td>
<td><p>required</p></td>
<td><p>Stationary detection enable.</p></td>
</tr>
<tr class="row-odd"><td><p>update_rate_nominal</p></td>
<td><p>uint32</p></td>
<td><p>required</p></td>
<td><p>Nominal update rate in multiply of superframe interval.</p></td>
</tr>
<tr class="row-even"><td><p>update_rate_stationary</p></td>
<td><p>uint32</p></td>
<td><p>required</p></td>
<td><p>Stationary update rate in multiply of superframe interval..</p></td>
</tr>
<tr class="row-odd"><td><p>reference_location</p></td>
<td><p><a class="reference internal" href="#node-location"><span class="std std-ref">node_location</span></a></p></td>
<td><p>optional</p></td>
<td><p>Reference location of the tag.</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="uwb-profile">
<span id="id10"></span><h3>uwb_profile</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 20%">
<col style="width: 16%">
<col style="width: 20%">
<col style="width: 44%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Field</p></th>
<th class="head"><p>Type</p></th>
<th class="head"><p>Label</p></th>
<th class="head"><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>sfn_range</p></td>
<td><p>uint32</p></td>
<td><p>required</p></td>
<td><p>Superframe number range.</p></td>
</tr>
<tr class="row-odd"><td><p>microseconds_per_sf</p></td>
<td><p>uint32</p></td>
<td><p>required</p></td>
<td><p>Microseconds per superframe.</p></td>
</tr>
<tr class="row-even"><td><p>microseconds_per_slot</p></td>
<td><p>uint32</p></td>
<td><p>required</p></td>
<td><p>Microseconds per slot.</p></td>
</tr>
<tr class="row-odd"><td><p>update_rate_default</p></td>
<td><p>uint32</p></td>
<td><p>required</p></td>
<td><p>Update rate is in multiple of superframes.</p></td>
</tr>
<tr class="row-even"><td><p>uplink_latency</p></td>
<td><p>uint32</p></td>
<td><p>optional</p></td>
<td><p>Number of slots to wait before the time of arrival data that has been received are
processed by the internal location engine.</p></td>
</tr>
<tr class="row-odd"><td><p>node_signup_optional</p></td>
<td><p>bool</p></td>
<td><p>optional</p></td>
<td><p>Setting this to “true” means that signup is not required for any of the edge nodes
(not gateway nodes), signup is required by default if this parameter is not set or if
it is set to “false”.</p></td>
</tr>
<tr class="row-even"><td><p>latency</p></td>
<td><p>uint32</p></td>
<td><p>optional</p></td>
<td><p>Ethernet latency in number of superframes, the latency is considered when sending
downlink, latency is supposed ot be 0 if this is not set</p></td>
</tr>
<tr class="row-odd"><td><p>max_buffer_size_downlink</p></td>
<td><p>uint32</p></td>
<td><p>optional</p></td>
<td><p>Size is supposed to be unlimited if not set.</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="uwb-rf-config">
<span id="id11"></span><h3>uwb_rf_config</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 9%">
<col style="width: 10%">
<col style="width: 12%">
<col style="width: 69%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Field</p></th>
<th class="head"><p>Type</p></th>
<th class="head"><p>Label</p></th>
<th class="head"><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>chnl</p></td>
<td><p>uint32</p></td>
<td><p>required</p></td>
<td><p>Channel configuration.</p></td>
</tr>
<tr class="row-odd"><td><p>rf_cpl</p></td>
<td><p>uint32</p></td>
<td><p>required</p></td>
<td><p>RF compliance configuration.</p></td>
</tr>
<tr class="row-even"><td><p>pcode</p></td>
<td><p>uint32</p></td>
<td><p>optional</p></td>
<td><p>Preamble code configuration.</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="version-info">
<span id="id12"></span><h3>version_info</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 15%">
<col style="width: 27%">
<col style="width: 24%">
<col style="width: 33%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Field</p></th>
<th class="head"><p>Type</p></th>
<th class="head"><p>Label</p></th>
<th class="head"><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>maj</p></td>
<td><p>uint32</p></td>
<td><p>required</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>min</p></td>
<td><p>uint32</p></td>
<td><p>required</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p>patch</p></td>
<td><p>uint32</p></td>
<td><p>required</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>var</p></td>
<td><p>uint32</p></td>
<td><p>optional</p></td>
<td></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="wifi-config">
<span id="id13"></span><h3>wifi_config</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 17%">
<col style="width: 41%">
<col style="width: 17%">
<col style="width: 24%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Field</p></th>
<th class="head"><p>Type</p></th>
<th class="head"><p>Label</p></th>
<th class="head"><p>Description</p></th>
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
<td><p><a class="reference internal" href="#wifi-region"><span class="std std-ref">wifi_region</span></a></p></td>
<td><p>optional</p></td>
<td></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="interface-config">
<span id="id14"></span><h3>interface_config</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 32%">
<col style="width: 24%">
<col style="width: 44%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Name</p></th>
<th class="head"><p>Number</p></th>
<th class="head"><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>ETHERNET</p></td>
<td><p>0</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>WIFI</p></td>
<td><p>1</p></td>
<td></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="mac-address-type">
<span id="id15"></span><h3>mac_address_type</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 18%">
<col style="width: 7%">
<col style="width: 75%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Name</p></th>
<th class="head"><p>Number</p></th>
<th class="head"><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>EMPTY</p></td>
<td><p>0</p></td>
<td><p>MAC address is empty meaning that the interface is not present.</p></td>
</tr>
<tr class="row-odd"><td><p>DEFAULT</p></td>
<td><p>1</p></td>
<td><p>Default MAC address (cannot be changed).</p></td>
</tr>
<tr class="row-even"><td><p>USER_SPECIFIED</p></td>
<td><p>2</p></td>
<td><p>MAC address specified by the user (can be changed).</p></td>
</tr>
<tr class="row-odd"><td><p>MUTABLE_DEFAULT</p></td>
<td><p>3</p></td>
<td><p>Default MAC address that can be changed only once by the user.</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="routing-config">
<span id="id16"></span><h3>routing_config</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 27%">
<col style="width: 14%">
<col style="width: 59%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Name</p></th>
<th class="head"><p>Number</p></th>
<th class="head"><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>ROUTING_OFF</p></td>
<td><p>0</p></td>
<td><p>UWB routing is turned off.</p></td>
</tr>
<tr class="row-odd"><td><p>ROUTING_ON</p></td>
<td><p>1</p></td>
<td><p>UWB routing is active.</p></td>
</tr>
<tr class="row-even"><td><p>ROUTING_AUTO</p></td>
<td><p>2</p></td>
<td><p>Automatic UWB routing.</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="service-type">
<span id="id17"></span><h3>service_type</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 22%">
<col style="width: 11%">
<col style="width: 67%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Name</p></th>
<th class="head"><p>Number</p></th>
<th class="head"><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>GET_CONFIG</p></td>
<td><p>0</p></td>
<td><p>Request to send configuration.</p></td>
</tr>
<tr class="row-odd"><td><p>TLV_API_CMD</p></td>
<td><p>1</p></td>
<td><p>TLV API command.</p></td>
</tr>
<tr class="row-even"><td><p>TLV_API_ACK</p></td>
<td><p>2</p></td>
<td><p>TLV API command positive acknowledge.</p></td>
</tr>
<tr class="row-odd"><td><p>TLV_API_NACK</p></td>
<td><p>3</p></td>
<td><p>TLV API command negative acknowledge.</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="tls-config">
<span id="id18"></span><h3>tls_config</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 8%">
<col style="width: 5%">
<col style="width: 86%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Name</p></th>
<th class="head"><p>Number</p></th>
<th class="head"><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>OFF</p></td>
<td><p>0</p></td>
<td><p>TLS/SSL turned off.</p></td>
</tr>
<tr class="row-odd"><td><p>SERVER</p></td>
<td><p>1</p></td>
<td><p>TLS authentication of server.</p></td>
</tr>
<tr class="row-even"><td><p>MUTUAL</p></td>
<td><p>2</p></td>
<td><p>Two way TLS authentication of server and the gateway/client.</p></td>
</tr>
<tr class="row-odd"><td><p>SERVER_CN</p></td>
<td><p>3</p></td>
<td><p>TLS authentication of server with checking of the ‘Common Name’.</p></td>
</tr>
<tr class="row-even"><td><p>MUTUAL_CN</p></td>
<td><p>4</p></td>
<td><p>Two way TLS authentication of server and the gateway/client with checking of the ‘Common Name’.</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="uwb-mode-config">
<span id="id19"></span><h3>uwb_mode_config</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 48%">
<col style="width: 18%">
<col style="width: 33%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Name</p></th>
<th class="head"><p>Number</p></th>
<th class="head"><p>Description</p></th>
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
<hr class="docutils">
</div>
<div class="section" id="uwb-status">
<span id="id20"></span><h3>uwb_status</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 24%">
<col style="width: 11%">
<col style="width: 65%">
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
<td><p>Disconnected from the UWB network.</p></td>
</tr>
<tr class="row-odd"><td><p>CONNECTED</p></td>
<td><p>1</p></td>
<td><p>Connected to the UWB network.</p></td>
</tr>
<tr class="row-even"><td><p>CONNECTED_BH</p></td>
<td><p>2</p></td>
<td><p>Connected, backhaul possible.</p></td>
</tr>
<tr class="row-odd"><td><p>UPDATING_FW</p></td>
<td><p>3</p></td>
<td><p>UWB firmware update is in progress.</p></td>
</tr>
<tr class="row-even"><td><p>UWBS_INACTIVE</p></td>
<td><p>4</p></td>
<td><p>Data from UWBS is not coming.</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="wifi-region">
<span id="id21"></span><h3>wifi_region</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 43%">
<col style="width: 20%">
<col style="width: 37%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Name</p></th>
<th class="head"><p>Number</p></th>
<th class="head"><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>EUROPE</p></td>
<td><p>0</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>NORTH_AMERICA</p></td>
<td><p>1</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p>ASIA</p></td>
<td><p>2</p></td>
<td></td>
</tr>
</tbody>
</table>
</div>
</div>
<hr class="docutils">
<div class="section" id="leaps-api">
<h2>leaps_api</h2>
<div class="section" id="leaps-api-inet-config">
<span id="id22"></span><h3>leaps_api.inet_config</h3>
<p>TCP/IP configuration options.</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 11%">
<col style="width: 49%">
<col style="width: 9%">
<col style="width: 30%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Field</p></th>
<th class="head"><p>Type</p></th>
<th class="head"><p>Label</p></th>
<th class="head"><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>ip</p></td>
<td><p><a class="reference internal" href="#leaps-api-ip-config"><span class="std std-ref">leaps_api.ip_config</span></a></p></td>
<td><p>repeated</p></td>
<td><p>IP configuration.</p></td>
</tr>
<tr class="row-odd"><td><p>dns</p></td>
<td><p>string</p></td>
<td><p>repeated</p></td>
<td><p>DNS host.</p></td>
</tr>
<tr class="row-even"><td><p>iface</p></td>
<td><p><a class="reference internal" href="#interface-config"><span class="std std-ref">interface_config</span></a></p></td>
<td><p>required</p></td>
<td><p>Interface selection.</p></td>
</tr>
<tr class="row-odd"><td><p>tls</p></td>
<td><p><a class="reference internal" href="#tls-config"><span class="std std-ref">tls_config</span></a></p></td>
<td><p>required</p></td>
<td><p>TLS/SSL configuration.</p></td>
</tr>
<tr class="row-even"><td><p>dhcp</p></td>
<td><p>bool</p></td>
<td><p>required</p></td>
<td><p>DHCP enabled?</p></td>
</tr>
<tr class="row-odd"><td><p>mac_filter</p></td>
<td><p>bool</p></td>
<td><p>required</p></td>
<td><p>MAC filter enabled?</p></td>
</tr>
<tr class="row-even"><td><p>server</p></td>
<td><p><a class="reference internal" href="#leaps-api-inet-config-server-config"><span class="std std-ref">leaps_api.inet_config.server_config</span></a></p></td>
<td><p>required</p></td>
<td><p>Leaps server configuration.</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="leaps-api-inet-config-server-config">
<span id="id23"></span><h3>leaps_api.inet_config.server_config</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 9%">
<col style="width: 17%">
<col style="width: 15%">
<col style="width: 59%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Field</p></th>
<th class="head"><p>Type</p></th>
<th class="head"><p>Label</p></th>
<th class="head"><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>host</p></td>
<td><p>string</p></td>
<td><p>required</p></td>
<td><p>Leaps server host configuration.</p></td>
</tr>
<tr class="row-odd"><td><p>port</p></td>
<td><p>uint32</p></td>
<td><p>required</p></td>
<td><p>Leaps server port configuration.</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="leaps-api-ip-config">
<span id="id24"></span><h3>leaps_api.ip_config</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 16%">
<col style="width: 21%">
<col style="width: 19%">
<col style="width: 44%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Field</p></th>
<th class="head"><p>Type</p></th>
<th class="head"><p>Label</p></th>
<th class="head"><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>addr</p></td>
<td><p>string</p></td>
<td><p>required</p></td>
<td><p>IP address.</p></td>
</tr>
<tr class="row-odd"><td><p>mask</p></td>
<td><p>string</p></td>
<td><p>optional</p></td>
<td><p>IP address mask.</p></td>
</tr>
<tr class="row-even"><td><p>gateway</p></td>
<td><p>string</p></td>
<td><p>optional</p></td>
<td><p>Gateway IP address.</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="leaps-api-location">
<span id="id25"></span><h3>leaps_api.location</h3>
<p>Topic: {prefix}/{panId/}node/uplink/location/{deviceId}.</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 14%">
<col style="width: 34%">
<col style="width: 12%">
<col style="width: 40%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Field</p></th>
<th class="head"><p>Type</p></th>
<th class="head"><p>Label</p></th>
<th class="head"><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>location</p></td>
<td><p><a class="reference internal" href="#node-location"><span class="std std-ref">node_location</span></a></p></td>
<td><p>required</p></td>
<td><p>Location of the device.</p></td>
</tr>
<tr class="row-odd"><td><p>timestamp</p></td>
<td><p>uint64</p></td>
<td><p>optional</p></td>
<td><p>Timestamp in microseconds.</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="leaps-api-mac-config">
<span id="id26"></span><h3>leaps_api.mac_config</h3>
<p>Configuration of the MAC address.</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 5%">
<col style="width: 23%">
<col style="width: 7%">
<col style="width: 66%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Field</p></th>
<th class="head"><p>Type</p></th>
<th class="head"><p>Label</p></th>
<th class="head"><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>addr</p></td>
<td><p>string</p></td>
<td><p>required</p></td>
<td><p>MAC address in dot-notation.</p></td>
</tr>
<tr class="row-odd"><td><p>type</p></td>
<td><p><a class="reference internal" href="#mac-address-type"><span class="std std-ref">mac_address_type</span></a></p></td>
<td><p>required</p></td>
<td><p>Type of the MAC address. Refer to <a class="reference internal" href="#mac-address-type"><span class="std std-ref">mac_address_type</span></a>.</p></td>
</tr>
<tr class="row-even"><td><p>iface</p></td>
<td><p>string</p></td>
<td><p>required</p></td>
<td><p>Interface that the MAC address belong to. Refer to mac_address_interface.</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="leaps-api-node-config">
<span id="id27"></span><h3>leaps_api.node_config</h3>
<p>Topic: {prefix}/{panId/}{node|gateway}/{uplink|downlink}/config/{deviceId}.</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 13%">
<col style="width: 28%">
<col style="width: 7%">
<col style="width: 53%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Field</p></th>
<th class="head"><p>Type</p></th>
<th class="head"><p>Label</p></th>
<th class="head"><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>label</p></td>
<td><p>string</p></td>
<td><p>required</p></td>
<td><p>Device label.</p></td>
</tr>
<tr class="row-odd"><td><p>uwb_mode</p></td>
<td><p><a class="reference internal" href="#uwb-mode-config"><span class="std std-ref">uwb_mode_config</span></a></p></td>
<td><p>required</p></td>
<td><p>UWB mode configuration.</p></td>
</tr>
<tr class="row-even"><td><p>ble</p></td>
<td><p>bool</p></td>
<td><p>required</p></td>
<td><p>BLE enabled?</p></td>
</tr>
<tr class="row-odd"><td><p>leds</p></td>
<td><p>bool</p></td>
<td><p>required</p></td>
<td><p>LEDs enabled?</p></td>
</tr>
<tr class="row-even"><td><p>fw_update</p></td>
<td><p>bool</p></td>
<td><p>required</p></td>
<td><p>Firmware update enabled?</p></td>
</tr>
<tr class="row-odd"><td><p>anchor</p></td>
<td><p><a class="reference internal" href="#anchor-config"><span class="std std-ref">anchor_config</span></a></p></td>
<td><p>optional</p></td>
<td><p>Anchor-specific configuration.</p></td>
</tr>
<tr class="row-even"><td><p>tag</p></td>
<td><p><a class="reference internal" href="#tag-config"><span class="std std-ref">tag_config</span></a></p></td>
<td><p>optional</p></td>
<td><p>Tag-specific configuration.</p></td>
</tr>
<tr class="row-odd"><td><p>inet</p></td>
<td><p><a class="reference internal" href="#leaps-api-inet-config"><span class="std std-ref">leaps_api.inet_config</span></a></p></td>
<td><p>optional</p></td>
<td><p>TCP/IP configuration</p></td>
</tr>
<tr class="row-even"><td><p>wifi</p></td>
<td><p><a class="reference internal" href="#wifi-config"><span class="std std-ref">wifi_config</span></a></p></td>
<td><p>optional</p></td>
<td><p>Wi-Fi configuration.</p></td>
</tr>
<tr class="row-odd"><td><p>mac</p></td>
<td><p><a class="reference internal" href="#leaps-api-mac-config"><span class="std std-ref">leaps_api.mac_config</span></a></p></td>
<td><p>repeated</p></td>
<td><p>MAC address configuration.</p></td>
</tr>
<tr class="row-even"><td><p>timestamp</p></td>
<td><p>uint64</p></td>
<td><p>optional</p></td>
<td><p>Timestamp in microseconds.</p></td>
</tr>
<tr class="row-odd"><td><p>uwb_rf_config</p></td>
<td><p><a class="reference internal" href="#uwb-rf-config"><span class="std std-ref">uwb_rf_config</span></a></p></td>
<td><p>optional</p></td>
<td><p>UWB channel, preamble code and RF compliance configuration.</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="leaps-api-tdoa-external-le">
<span id="id28"></span><h3>leaps_api.tdoa_external_le</h3>
<p>Topic: {prefix}/{panId/}{node|gateway}/uplink/toa/{deviceId}.</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 20%">
<col style="width: 36%">
<col style="width: 9%">
<col style="width: 35%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Field</p></th>
<th class="head"><p>Type</p></th>
<th class="head"><p>Label</p></th>
<th class="head"><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>type</p></td>
<td><p><a class="reference internal" href="#time-of-arrival-data-type"><span class="std std-ref">time_of_arrival_data_type</span></a></p></td>
<td><p>required</p></td>
<td><p>Type of TOA data</p></td>
</tr>
<tr class="row-odd"><td><p>from</p></td>
<td><p>uint32</p></td>
<td><p>required</p></td>
<td><p>Id of transmitting device</p></td>
</tr>
<tr class="row-even"><td><p>to</p></td>
<td><p>uint32</p></td>
<td><p>required</p></td>
<td><p>Id of receiving device</p></td>
</tr>
<tr class="row-odd"><td><p>rx_timestamp</p></td>
<td><p>uint64</p></td>
<td><p>required</p></td>
<td><p>Receive timestamp (uwb clock)</p></td>
</tr>
<tr class="row-even"><td><p>tx_timestamp</p></td>
<td><p>uint64</p></td>
<td><p>optional</p></td>
<td><p>Transmit timestamp (uwb clock)</p></td>
</tr>
<tr class="row-odd"><td><p>tag_blink_index</p></td>
<td><p>uint32</p></td>
<td><p>optional</p></td>
<td><p>Tag blink index</p></td>
</tr>
<tr class="row-even"><td><p>frame</p></td>
<td><p>uint32</p></td>
<td><p>required</p></td>
<td><p>Frame number</p></td>
</tr>
<tr class="row-odd"><td><p>tn_stat</p></td>
<td><p>bool</p></td>
<td><p>optional</p></td>
<td><p>TN stationary status</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="time-of-arrival-data-type">
<span id="id29"></span><h3>time_of_arrival_data_type</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 27%">
<col style="width: 15%">
<col style="width: 59%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Name</p></th>
<th class="head"><p>Number</p></th>
<th class="head"><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>UNKNOWN</p></td>
<td><p>0</p></td>
<td><p>Unknown</p></td>
</tr>
<tr class="row-odd"><td><p>TWR</p></td>
<td><p>1</p></td>
<td><p>TWR</p></td>
</tr>
<tr class="row-even"><td><p>TDOA_BLINK</p></td>
<td><p>2</p></td>
<td><p>TDoA Blink</p></td>
</tr>
<tr class="row-odd"><td><p>TDOA_BCN</p></td>
<td><p>3</p></td>
<td><p>TDoA Beacon</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="leaps-api-server-status">
<span id="id30"></span><h3>leaps_api.server_status</h3>
<p>Leaps server status uplink topic: {prefix}/server/status.</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 7%">
<col style="width: 38%">
<col style="width: 7%">
<col style="width: 47%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Field</p></th>
<th class="head"><p>Type</p></th>
<th class="head"><p>Label</p></th>
<th class="head"><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>state</p></td>
<td><p><a class="reference internal" href="#leaps-api-connection-state"><span class="std std-ref">leaps_api.connection_state</span></a></p></td>
<td><p>optional</p></td>
<td><p>Status of the Leaps server. Refer to server_state.</p></td>
</tr>
<tr class="row-odd"><td><p>version</p></td>
<td><p>string</p></td>
<td><p>optional</p></td>
<td><p>Leaps Server version.</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="leaps-api-server-request">
<span id="id31"></span><h3>leaps_api.server_request</h3>
<p>Leaps server request downlink topic: {prefix}/server/request.</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 8%">
<col style="width: 34%">
<col style="width: 7%">
<col style="width: 51%">
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
<td><p><a class="reference internal" href="#leaps-api-server-request-type"><span class="std std-ref">leaps_api.server_request.type:</span></a></p></td>
<td><p>optional</p></td>
<td><p>Request to the Leaps server.</p></td>
</tr>
</tbody>
</table>
</div>
<div class="section" id="leaps-api-server-request-type">
<span id="id32"></span><h3>leaps_api.server_request.type:</h3>
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
<td><p>DEPRECATED: Same as PUBLISH_ALL_TOPICS.</p></td>
</tr>
<tr class="row-odd"><td><p>PUBLISH_ALL_TOPICS</p></td>
<td><p>1</p></td>
<td><p>Request to immediately publish all messages for all the nodes.</p></td>
</tr>
</tbody>
</table>
</div>
<div class="section" id="leaps-api-service-data">
<span id="id33"></span><h3>leaps_api.service_data</h3>
<p>Topic: {prefix}/{panId/}node/{uplink|downlink}/service/{deviceId}.</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 13%">
<col style="width: 31%">
<col style="width: 11%">
<col style="width: 46%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Field</p></th>
<th class="head"><p>Type</p></th>
<th class="head"><p>Label</p></th>
<th class="head"><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>type</p></td>
<td><p><a class="reference internal" href="#service-type"><span class="std std-ref">service_type</span></a></p></td>
<td><p>required</p></td>
<td><p>Type of the server data.</p></td>
</tr>
<tr class="row-odd"><td><p>data</p></td>
<td><p>bytes</p></td>
<td><p>optional</p></td>
<td><p>The data bytes encoded as base64.</p></td>
</tr>
<tr class="row-even"><td><p>timestamp</p></td>
<td><p>uint64</p></td>
<td><p>optional</p></td>
<td><p>Timestamp in microseconds.</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="leaps-api-status">
<span id="id34"></span><h3>leaps_api.status</h3>
<p>Topic: {prefix}/{panId}/{node|gateway}/uplink/status/{deviceId}.</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 11%">
<col style="width: 15%">
<col style="width: 7%">
<col style="width: 67%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Field</p></th>
<th class="head"><p>Type</p></th>
<th class="head"><p>Label</p></th>
<th class="head"><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>present</p></td>
<td><p>bool</p></td>
<td><p>required</p></td>
<td><p>Device is present or missing?</p></td>
</tr>
<tr class="row-odd"><td><p>downlink</p></td>
<td><p>bool</p></td>
<td><p>optional</p></td>
<td><p>Sending downlink to the device is possible?</p></td>
</tr>
<tr class="row-even"><td><p>uwb</p></td>
<td><p><a class="reference internal" href="#uwb-status"><span class="std std-ref">uwb_status</span></a></p></td>
<td><p>optional</p></td>
<td><p>Status of the UWB layer.</p></td>
</tr>
<tr class="row-odd"><td><p>batt</p></td>
<td><p>uint32</p></td>
<td><p>optional</p></td>
<td><p>Battery status in mV.</p></td>
</tr>
<tr class="row-even"><td><p>batt_state</p></td>
<td><p>uint32</p></td>
<td><p>optional</p></td>
<td><p>Indicates the battery status, 0-Unknown | 1-Empty | 2-Low | 3-Medium | 4-Full.</p></td>
</tr>
<tr class="row-odd"><td><p>temp</p></td>
<td><p>int32</p></td>
<td><p>optional</p></td>
<td><p>Temperature in degrees.</p></td>
</tr>
<tr class="row-even"><td><p>origins</p></td>
<td><p><a class="reference internal" href="#origin-info"><span class="std std-ref">origin_info</span></a></p></td>
<td><p>repeated</p></td>
<td><p>List of UWB origins.</p></td>
</tr>
<tr class="row-odd"><td><p>profile</p></td>
<td><p><a class="reference internal" href="#uwb-profile"><span class="std std-ref">uwb_profile</span></a></p></td>
<td><p>optional</p></td>
<td><p>Current UWB profile status.</p></td>
</tr>
<tr class="row-even"><td><p>timestamp</p></td>
<td><p>uint64</p></td>
<td><p>optional</p></td>
<td><p>Timestamp in microseconds.</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="leaps-api-user-data">
<span id="id35"></span><h3>leaps_api.user_data</h3>
<p>Topic: {prefix}/{panId}/node/{uplink|downlink}/data/{deviceId}.</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 15%">
<col style="width: 15%">
<col style="width: 14%">
<col style="width: 56%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Field</p></th>
<th class="head"><p>Type</p></th>
<th class="head"><p>Label</p></th>
<th class="head"><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>data</p></td>
<td><p>bytes</p></td>
<td><p>required</p></td>
<td><p>The data bytes encoded as base64.</p></td>
</tr>
<tr class="row-odd"><td><p>overwrite</p></td>
<td><p>bool</p></td>
<td><p>optional</p></td>
<td><p>Overwrite the pending data?</p></td>
</tr>
<tr class="row-even"><td><p>timestamp</p></td>
<td><p>uint64</p></td>
<td><p>optional</p></td>
<td><p>Timestamp in microseconds.</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="leaps-api-mac-address-interface">
<span id="id36"></span><h3>leaps_api.mac_address_interface</h3>
<p>Supported interfaces in terms of MAC addresses configuration.</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 32%">
<col style="width: 24%">
<col style="width: 44%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Name</p></th>
<th class="head"><p>Number</p></th>
<th class="head"><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>UWB</p></td>
<td><p>0</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>BLE</p></td>
<td><p>1</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p>ETHERNET</p></td>
<td><p>2</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>WIFI</p></td>
<td><p>3</p></td>
<td></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="leaps-api-connection-state">
<span id="id37"></span><h3>leaps_api.connection_state</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 18%">
<col style="width: 9%">
<col style="width: 73%">
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
<td><p>Leaps server is disconnected from MQTT broker.</p></td>
</tr>
<tr class="row-odd"><td><p>CONNECTED</p></td>
<td><p>1</p></td>
<td><p>Leaps server is connected to MQTT broker.</p></td>
</tr>
</tbody>
</table>
</div>
</div>
</div>


           </div>
