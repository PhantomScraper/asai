---
title: "leaps_dist_alarm_cfg_set"
lang: en
slug: "leaps-rtls/integration-guide/api-commands/leaps-dist-alarm-cfg-set"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/leaps-rtls/integration-guide/api-commands/leaps-dist-alarm-cfg-set/"
order: 252
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-dist-alarm-cfg-set">
<span id="id1"></span><h1>leaps_dist_alarm_cfg_set</h1>
<p>Changes configuration of distance alarm detection. Writes internal
flash, do not use it frequently.</p>
<hr class="docutils">
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
Input</div>
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
<col style="width: 9%">
<col style="width: 10%">
<col style="width: 15%">
<col style="width: 15%">
<col style="width: 10%">
<col style="width: 9%">
<col style="width: 16%">
<col style="width: 18%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="8"><p>TLVT response</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="2"><p>Type</p></td>
<td rowspan="2"><p>Length</p></td>
<td colspan="6"><p>Value</p></td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line">distance
threshold</div>
<div class="line">nr.1
(millimeters)</div>
</div>
</td>
<td><div class="line-block">
<div class="line">distance
threshold</div>
<div class="line">nr.2
(millimeters)</div>
</div>
</td>
<td><p>mincon</p></td>
<td><p>minnocon</p></td>
<td><div class="line-block">
<div class="line">options
bits (3-7) -
reserved</div>
<div class="line">bits (0-2) -
alarm
indication
options</div>
</div>
</td>
<td><p>reserved
(8 bytes)</p></td>
</tr>
<tr class="row-even"><td><p>0x33</p></td>
<td><p>0x13</p></td>
<td><p>0xDC 0x05
0x00 0x00</p></td>
<td><p>0xC4 0x09
0x00 0x00</p></td>
<td><p>0x02</p></td>
<td><p>0x02</p></td>
<td><p>0x01</p></td>
<td><p>0x00 0x00 0x00 0x00
0x00 0x00 0x00 0x00</p></td>
</tr>
</tbody>
</table>
<p>Type 0x33 (51 dec) means command leaps_dist_alarm_cfg_set</p>
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
