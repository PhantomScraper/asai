---
title: "leaps_cfg_get"
lang: en
slug: "leaps-rtls/integration-guide/api-commands/leaps-cfg-get"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/leaps-rtls/integration-guide/api-commands/leaps-cfg-get/"
order: 153
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-cfg-get">
<span id="id1"></span><h1>leaps_cfg_get</h1>
<p>Get current configuration options of the node.</p>
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
<li><p class="sd-card-text">initiator: 1-bit (<em>‘0’ | ‘1’ - Initiator role enable</em>)</p></li>
<li><p class="sd-card-text">gateway: 1-bit (<em>‘0’ | ‘1’ - Gateway role enable</em>)</p></li>
<li><p class="sd-card-text">enc_en: 1-bit (<em>‘0’ | ‘1’ - encryption enable</em>)</p></li>
<li><p class="sd-card-text">led_en: 1-bit (<em>‘0’ | ‘1’ - general purpose LEDs enable</em>)</p></li>
<li><p class="sd-card-text">ble_en: 1-bit (<em>‘0’ | ‘1’ - BLE enable</em>)</p></li>
<li><p class="sd-card-text">uwb_mode: 2-bits (<em>0-off, 1-passive, 2-active</em>)</p></li>
<li><p class="sd-card-text">fw_update_en: 1-bit (<em>‘0’ | ‘1’- Firmware update enable</em>)</p></li>
<li><p class="sd-card-text">stnry_en: 1-bit (<em>‘0’ | ‘1’  Stationary detection enabled, if enabled, the stationary update rate is used instead of normal update rate if node is not moving</em>)</p></li>
<li><p class="sd-card-text">meas_mode: 2-bits (<em>‘0’ | ‘1’ | ‘2’ | ‘3’ , 0 - Two way ranging, 1 - UL-TDoA, 2 - DL-TDoA, 3 - reserved</em>)</p></li>
<li><p class="sd-card-text">low_power_en: 1-bit (<em>‘0’ | ‘1’ Low-power mode enable</em>)</p></li>
<li><p class="sd-card-text">loc_engine_en: 1-bit (<em>‘0’ | ‘1’ 0 means do not use internal Location Engine, 1 means internal Location Engine</em>)</p></li>
<li><p class="sd-card-text">profile_id: 3-bits (<em>ID of the profile</em>)</p></li>
<li><p class="sd-card-text">clock_reference: 1-bit (<em>enables clock reference on the node</em>)</p></li>
<li><p class="sd-card-text">uwb_act_ble: 1-bit (<em>uwb activation over ble status on the node</em>)</p></li>
</ul>
</div>
</div>
</div>
</div>
</div>
<hr class="docutils">
<blockquote>
<div><div class="admonition note">
<p class="admonition-title">Note</p>
<p><strong>uwb_bh_routing</strong>: Available only when the firmware is compiled with UWB routing backhaul:</p>
<p>Value : ‘0’ | ‘1’ | ‘2’:</p>
<ul class="simple">
<li><p>0- OFF - anchor will not become a routing anchor</p></li>
<li><p>1- ON - anchor will be preferred by the routing algorithm to be chosen as a routing anchor</p></li>
<li><p>2- AUTO - Whether anchor becomes routing or not depends entirely on the routing algorithm</p></li>
</ul>
</div>
</div></blockquote>
<hr class="docutils">
<p><strong>Example</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 53%">
<col style="width: 47%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="2"><p>TLV Request</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Type</p></td>
<td><p>Length</p></td>
</tr>
<tr class="row-odd"><td><p>0x08</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>Type 0x08 means command leaps_cfg_get</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 5%">
<col style="width: 6%">
<col style="width: 5%">
<col style="width: 4%">
<col style="width: 6%">
<col style="width: 20%">
<col style="width: 30%">
<col style="width: 26%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="8"><p>TLV response</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="2"><p>Type</p></td>
<td rowspan="2"><p>Length</p></td>
<td rowspan="2"><p>Value</p></td>
<td rowspan="2"><p>Type</p></td>
<td rowspan="2"><p>Length</p></td>
<td colspan="3"><p>Value</p></td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line">(bit 7) low_power_en</div>
<div class="line">(bit 6) loc_engine_en</div>
<div class="line">(bit 5) enc_en</div>
<div class="line">(bit 4) led_en</div>
<div class="line">(bit 3) ble_en</div>
<div class="line">(bit 2) fw_update_en</div>
<div class="line">(bits 0-1) uwb_mode:</div>
<div class="line">0 - OFFLINE,</div>
<div class="line">1 - PASSIVE,</div>
<div class="line">2 - ACTIVE</div>
</div>
</td>
<td><div class="line-block">
<div class="line">(bits 6-7) uwb_bh_routing:</div>
<div class="line">0 - OFF,</div>
<div class="line">1 - ON,</div>
<div class="line">2 - AUTO</div>
<div class="line">(bit 5) mode:</div>
<div class="line">0 - tag</div>
<div class="line">1 - anchor</div>
<div class="line">(bit 4) initiator</div>
<div class="line">(bit 3) gateway</div>
<div class="line">(bit 2) stnry_en</div>
<div class="line">(bits 0-1) meas_mode:</div>
<div class="line">0 - TWR,</div>
<div class="line">1 - UL-TDoA</div>
<div class="line">2 - DL-TDoA</div>
<div class="line">3 reserved</div>
</div>
</td>
<td><div class="line-block">
<div class="line">(bits 0-2) profile id</div>
<div class="line">(bit 3) clock reference</div>
<div class="line">(bit 4) uwb_act_ble</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
<td><p>0x46</p></td>
<td><p>0x03</p></td>
<td><p>0x1C</p></td>
<td><p>0x20</p></td>
<td><p>0x02</p></td>
</tr>
</tbody>
</table>
<p>Type 0x40 means status code</p>
<p>Type 0x46 means node configuration</p>
</div>


           </div>
