---
title: "leaps_dev_status_get"
lang: en
slug: "leaps-rtls/integration-guide/api-commands/leaps-dev-status-get"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/leaps-rtls/integration-guide/api-commands/leaps-dev-status-get/"
order: 277
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-dev-status-get">
<span id="id1"></span><h1>leaps_dev_status_get</h1>
<p>Reads device status information.</p>
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
<li><p class="sd-card-text">uptime: 32-bit unsigned integer (<em>device uptime in seconds</em>)</p></li>
<li><p class="sd-card-text">temperature: 16-bit signed integer (<em>temperature in degrees Celsius</em>)</p></li>
<li><p class="sd-card-text">battery_voltage: 16-bit unsigned integer (<em>battery voltage in millivolts</em>)</p></li>
<li><p class="sd-card-text">battery_state: 4-bits (battery state = NO_BATTERY: 0,  CHARGING: 1, CHARGED: 2, DISCHARGE: 3, VBAT_LOW: 4, VBAT_EMPTY= 5)</p></li>
<li><p class="sd-card-text">battery_level: 7-bit unsigned integer (<em>battery level in percents</em>)</p></li>
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
<tr class="row-odd"><th class="head"><p>TLV Request</p></th>
<th class="head"></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Type</p></td>
<td><p>Length</p></td>
</tr>
<tr class="row-odd"><td><p>0x25</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>Type 0x25 (37 dec) means command leaps_dev_status_get</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 12%">
<col style="width: 10%">
<col style="width: 8%">
<col style="width: 7%">
<col style="width: 10%">
<col style="width: 10%">
<col style="width: 15%">
<col style="width: 29%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="8"><p>TLV
response</p></th>
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
<tr class="row-odd"><td><p>uptime</p></td>
<td><p>temperature</p></td>
<td><div class="line-block">
<div class="line">battery:</div>
<div class="line">(byte 0-1) voltage</div>
<div class="line">(byte 2 ) level</div>
<div class="line">(byte 3) state</div>
<div class="line">(byte 4-5) reserved</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
<td><p>0x59</p></td>
<td><p>0x0C</p></td>
<td><p>0x2C
0x00
0x00
0x00</p></td>
<td><p>0x22
0x00</p></td>
<td><p>0x2d 0x0f 0x3e</p>
<p>0x01 0x00 0x00</p>
</td>
</tr>
</tbody>
</table>
<p>Type 0x40 (64 dec) means status code</p>
<p>Type 0x59 (89 dec) means device status</p>
</div>


           </div>
