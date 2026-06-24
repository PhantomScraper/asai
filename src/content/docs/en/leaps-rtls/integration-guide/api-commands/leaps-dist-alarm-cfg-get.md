---
title: "leaps_dist_alarm_cfg_get"
lang: en
slug: "leaps-rtls/integration-guide/api-commands/leaps-dist-alarm-cfg-get"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/leaps-rtls/integration-guide/api-commands/leaps-dist-alarm-cfg-get/"
order: 253
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-dist-alarm-cfg-get">
<span id="id1"></span><h1>leaps_dist_alarm_cfg_get</h1>
<p>Reads configuration of distance alarm detection.</p>
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
<li><p class="sd-card-text">threshold_1: 32-bits unsigned integer (<em>distance threshold in millimeters</em>)</p></li>
<li><p class="sd-card-text">threshold_2: 32-bits unsigned integer (<em>distance threshold in millimeters</em>)</p></li>
<li><p class="sd-card-text">mincon: 8-bits unsigned integer (<em>threshold hysteresis in multiple of update rate</em>)</p></li>
<li><p class="sd-card-text">minnoconn: 8-bits unsigned integer (<em>threshold hysteresis in multiple of update rate</em>)</p></li>
<li><p class="sd-card-text">options: 8-bits unsigned integer (<em>alarm indication options, 0 - LED (discrete), 1 - LED (continuous), 2 - Buzzer (continuous), 3 - Motor (continuous)</em>)</p></li>
</ul>
</div>
</div>
</div>
</div>
</div>
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
<tr class="row-odd"><td><p>0x31</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>Type 0x31 (49 dec) means command leaps_serial_cfg_get</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 8%">
<col style="width: 7%">
<col style="width: 6%">
<col style="width: 5%">
<col style="width: 7%">
<col style="width: 15%">
<col style="width: 15%">
<col style="width: 7%">
<col style="width: 8%">
<col style="width: 13%">
<col style="width: 10%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="11"><p>TLV response</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="2"><p>Type</p></td>
<td rowspan="2"><p>Length</p></td>
<td rowspan="2"><p>Value</p></td>
<td rowspan="2"><p>Type</p></td>
<td rowspan="2"><p>Length</p></td>
<td colspan="6"><p>Value</p></td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line">distance</div>
<div class="line">threshold nr.1</div>
<div class="line">(millimeters)</div>
</div>
</td>
<td><div class="line-block">
<div class="line">distance</div>
<div class="line">threshold nr.2</div>
<div class="line">(millimeters)</div>
</div>
</td>
<td><p>mincon</p></td>
<td><p>minnocon</p></td>
<td><div class="line-block">
<div class="line">options
bits (3-7)
reserved</div>
<div class="line">bits (0-2)
alarm
in
dication
options</div>
</div>
</td>
<td><p>reserved
(8 bytes)</p></td>
</tr>
<tr class="row-even"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
<td><p>0x52</p></td>
<td><p>0x13</p></td>
<td><p>0xDC
0x05
0x00
0x00</p></td>
<td><p>0xC4
0x09
0x00
0x00</p></td>
<td><p>0x02</p></td>
<td><p>0x02</p></td>
<td><p>0x01</p></td>
<td><p>0x00 0x00
0x00 0x00
0x00 0x00
0x00 0x00</p></td>
</tr>
</tbody>
</table>
<p>Type 0x40 means status code</p>
<p>Type 0x52 (82) means distance alarm configuration</p>
</div>


           </div>
