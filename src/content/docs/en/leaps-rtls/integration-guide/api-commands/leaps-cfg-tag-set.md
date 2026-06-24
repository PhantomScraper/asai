---
title: "leaps_cfg_tag_set"
lang: en
slug: "leaps-rtls/integration-guide/api-commands/leaps-cfg-tag-set"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/leaps-rtls/integration-guide/api-commands/leaps-cfg-tag-set/"
order: 150
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-cfg-tag-set">
<span id="id1"></span><h1>leaps_cfg_tag_set</h1>
<p>Configure node as tag with given options. Encryption can’t be enabled if the encryption
key is not set. This call requires reset for a new configuration to take
effect (leaps_reset). This call does a write to internal flash in case
of new value being set, hence should not be used frequently and can take
in worst case hundreds of milliseconds!</p>
<hr class="docutils">
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
Input</div>
<ul class="simple">
<li><p class="sd-card-text">stnry_en: 1-bit (<em>‘0’ | ‘1’  Stationary detection enabled, if enabled, the stationary update rate is used instead of normal update rate if node is not moving</em>)</p></li>
<li><p class="sd-card-text">meas_mode: 2-bits (<em>‘0’ - TWR, Two way ranging,  ‘1’ - TDOA,  time difference of arrival, ‘2’, ‘3’ - reserved</em>)</p></li>
<li><p class="sd-card-text">low_power_en: 1-bit (<em>‘0’ | ‘1’ Low-power mode enable</em>)</p></li>
<li><p class="sd-card-text">loc_engine_en: 1-bit (<em>‘0’ | ‘1’ 0 means do not use internal Location Engine, 1 means internal Location Engine</em>)</p></li>
<li><p class="sd-card-text">enc_en: 1-bit (<em>‘0’ | ‘1’ encryption enable</em>)</p></li>
<li><p class="sd-card-text">led_en: 1-bit (<em>‘0’ | ‘1’ general purpose LEDs enable</em>)</p></li>
<li><p class="sd-card-text">ble_en: 1-bit (<em>‘0’ | ‘1’ BLE enable</em>)</p></li>
<li><p class="sd-card-text">uwb_mode: 2-bits (<em>‘0’ | ‘1’ | ‘2’ 0-off, 1-passive, 2-active</em>)</p></li>
<li><p class="sd-card-text">fw_update_en: 1-bit (<em>‘0’ | ‘1’ Firmware update enable</em>)</p></li>
<li><p class="sd-card-text">profile_id: 3-bit unsigned integer (<em>ID of the profile</em>)</p></li>
<li><p class="sd-card-text">uwb_act_ble: 1-bit unsigned integer (<em>UWB activation over BLE</em>)</p></li>
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
<col style="width: 11%">
<col style="width: 9%">
<col style="width: 32%">
<col style="width: 31%">
<col style="width: 16%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="5"><p>TLV response</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="2"><p>Type</p></td>
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
<div class="line">(bits 0-1) uwb_mode</div>
</div>
</td>
<td><div class="line-block">
<div class="line">(bits 4-7) reserved</div>
<div class="line">(bit 3) uwb_act_ble</div>
<div class="line">(bit 2) stnry_en</div>
<div class="line">(bits 0-1) meas_mode</div>
</div>
</td>
<td><p>(bits 0-2)
profile id</p></td>
</tr>
<tr class="row-even"><td><p>0x05</p></td>
<td><p>0x03</p></td>
<td><p>0x72</p></td>
<td><p>0x04</p></td>
<td><p>0x05</p></td>
</tr>
</tbody>
</table>
<p>Type 0x05 means command leaps_cfg_tag_set</p>
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
