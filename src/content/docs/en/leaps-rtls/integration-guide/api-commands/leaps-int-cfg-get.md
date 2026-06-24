---
title: "leaps_int_cfg_get"
lang: en
slug: "leaps-rtls/integration-guide/api-commands/leaps-int-cfg-get"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/leaps-rtls/integration-guide/api-commands/leaps-int-cfg-get/"
order: 267
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-int-cfg-get">
<span id="id1"></span><h1>leaps_int_cfg_get</h1>
<p>Read configuration flags that, if set, enable the setting of a dedicated
GPIO pin (CORE_INT) in case of an event. This call is available only on
UART/SPI interfaces.</p>
<hr class="docutils">
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
Input</div>
<ul class="simple">
<li><p class="sd-card-text">(<em>none</em>)</p></li>
</ul>
</div>
</div>
</div>
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
Output</div>
<ul class="simple">
<li><p class="sd-card-text"><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/leaps-api/api-generic-data-types#statuscode"><span class="std std-ref">Status Code</span></a></p></li>
<li><p class="sd-card-text">spi_data_ready: ‘0’ | ‘1’ (<em>new SPI data ready event , 0=disable, 1=enable</em>)</p></li>
<li><p class="sd-card-text">loc_ready: ‘0’ | ‘1’ (<em>new location data ready event, 0=disable, 1=enable</em>)</p></li>
<li><p class="sd-card-text">bh_status_changed: ‘0’ | ‘1’ (<em>UWBMAC status changed, 0=disable, 1=enable</em>)</p></li>
<li><p class="sd-card-text">bh_data_ready: ‘0’ | ‘1’ (<em>UWBMAC backhaul data ready, 0=disable, 1=enable</em>)</p></li>
<li><p class="sd-card-text">bh_initialized_changed: ‘0’ | ‘1’ (<em>UWBMAC route configured, 0=disable, 1=enable</em>)</p></li>
<li><p class="sd-card-text">uwb_scan_ready: ‘0’ | ‘1’ (<em>UWB scan result is available</em>)</p></li>
<li><p class="sd-card-text">uwb_usr_data_ready: ‘0’ | ‘1’ (<em>event when new user data is received over UWBMAC, 0=disable, 1=enable</em>)</p></li>
<li><p class="sd-card-text">uwbmac_joined_changed: ‘0’ | ‘1’ (<em>UWBMAC joined event, 0=disable, 1=enable</em>)</p></li>
<li><p class="sd-card-text">uwb_usr_data_sent: ‘0’ | ‘1’ (<em>user data transmission completed over UWBMAC, 0=disable, 1=enable</em>)</p></li>
<li><p class="sd-card-text">proxy_pos_ready: ‘0’ | ‘1’ (<em>event when proxy positions are ready,  0=disable, 1=enable</em>)</p></li>
<li><p class="sd-card-text">ble_usr_data_ready: ‘0’ | ‘1’ (<em>event when user data isreceived on BLE, 0=disable, 1=enable</em>)</p></li>
<li><p class="sd-card-text">ble_usr_data_sent: ‘0’ | ‘1’ (<em>event when user data over BLE are sent, 0=disable, 1=enable</em>)</p></li>
<li><p class="sd-card-text">ble_conn_state_changed: ‘0’ | ‘1’ (<em>event when BLE connection state change, 0=disable, 1=enable</em>)</p></li>
<li><p class="sd-card-text">distance_alarm_th_1: ‘0’ | ‘1’ (<em>event when distance alarm occur for threshold 1, 0=disable, 1=enable</em>)</p></li>
<li><p class="sd-card-text">distance_alarm_th_2: ‘0’ | ‘1’ (<em>event when distance alarm occur for threshold 2, 0=disable, 1=enable</em>)</p></li>
</ul>
</div>
</div>
</div>
</div>
</div>
<hr class="docutils">
<p><strong>Example</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 52%">
<col style="width: 48%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="2"><p>TLV Request</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Type</p></td>
<td><p>Length</p></td>
</tr>
<tr class="row-odd"><td><p>0x35</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>Type 0x35 means command leaps_int_cfg_get</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 10%">
<col style="width: 11%">
<col style="width: 10%">
<col style="width: 10%">
<col style="width: 11%">
<col style="width: 49%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="6"><p>TLV
response</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="2"><p>Type</p></td>
<td rowspan="2"><p>Length</p></td>
<td rowspan="2"><p>Value</p></td>
<td rowspan="2"><p>Type</p></td>
<td rowspan="2"><p>Length</p></td>
<td><p>Value</p></td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line">(bit 15) res erved</div>
<div class="line">(bit 14) distance_alarm_th_2</div>
<div class="line">(bit 13) distance_alarm_th_1</div>
<div class="line">(bit 12) ble_conn_state_changed</div>
<div class="line">(bit 11) ble_usr_data_sent</div>
<div class="line">(bit 10) ble_usr_data_ready</div>
<div class="line">(bit 9) proxy_pos_ready</div>
<div class="line">(bit 8) uwb_usr_data_sent</div>
<div class="line">(bit 7) uwbmac_joined_changed</div>
<div class="line">(bit 6) uwb_usr_data_ready</div>
<div class="line">(bit 5) uwb_scan_ready</div>
<div class="line">(bit 4) bh_initialized_changed</div>
<div class="line">(bit 3) bh_data_ready</div>
<div class="line">(bit 2) bh _status_changed</div>
<div class="line">(bit 1) spi_data_ready</div>
<div class="line">(bit 0) loc_ready</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
<td><p>0x47</p></td>
<td><p>0x02</p></td>
<td><p>0x0E
0x00</p></td>
</tr>
</tbody>
</table>
<p>Type 0x47 means interrupt configuration</p>
</div>


           </div>
