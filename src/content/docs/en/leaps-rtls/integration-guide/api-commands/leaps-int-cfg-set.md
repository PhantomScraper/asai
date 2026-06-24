---
title: "leaps_int_cfg_set"
lang: en
slug: "leaps-rtls/integration-guide/api-commands/leaps-int-cfg-set"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/leaps-rtls/integration-guide/api-commands/leaps-int-cfg-set/"
order: 148
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-int-cfg-set">
<span id="id1"></span><h1>leaps_int_cfg_set</h1>
<p>Enables/disables setting of the dedicated GPIO pin in case of an event.
Interrupts/events are communicated to the user by setting the GPIO pin
CORE_INT. User can use the pin as a source of an external interrupt. The
interrupt can be processed by reading the status (leaps_status_get) and
reacting according to the new status. The status is cleared
automatically after it is read. This call writes internal flash in case
of new values being set, hence should not be used frequently and can
take in worst case hundreds of milliseconds!</p>
<hr class="docutils">
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
Input</div>
<ul class="simple">
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
<li><p class="sd-card-text">ble_usr_data_ready: ‘0’ | ‘1’ (<em>event when user data is received on BLE, 0=disable, 1=enable</em>)</p></li>
<li><p class="sd-card-text">ble_usr_data_sent: ‘0’ | ‘1’ (<em>event when user data over BLE are sent, 0=disable, 1=enable</em>)</p></li>
<li><p class="sd-card-text">ble_conn_state_changed: ‘0’ | ‘1’ (<em>event when BLE connection state change, 0=disable, 1=enable</em>)</p></li>
<li><p class="sd-card-text">distance_alarm_th_1: ‘0’ | ‘1’ (<em>event when distance alarm occur for threshold 1, 0=disable, 1=enable</em>)</p></li>
<li><p class="sd-card-text">distance_alarm_th_2: ‘0’ | ‘1’ (<em>event when distance alarm occur for threshold 2, 0=disable, 1=enable</em>)</p></li>
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
<col style="width: 19%">
<col style="width: 19%">
<col style="width: 63%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV Request</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="2"><p>Type</p></td>
<td rowspan="2"><p>Length</p></td>
<td><p>Value</p></td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line">(bit 15) reserved</div>
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
<div class="line">(bit 4) bh_initialize d_changed</div>
<div class="line">(bit 3) bh_data_ready</div>
<div class="line">(bit 2) bh_status_changed</div>
<div class="line">(bit 1) spi_data_ready</div>
<div class="line">(bit 0) loc_ready</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>0x34</p></td>
<td><p>0x02</p></td>
<td><p>0x0F 0x01</p></td>
</tr>
</tbody>
</table>
<p>Type 0x34 means command leaps_int_cfg_set</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 34%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV response</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Type</p></td>
<td><p>Length</p></td>
<td><p>Value</p></td>
</tr>
<tr class="row-odd"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>Type 0x40 means status code</p>
</div>


           </div>
