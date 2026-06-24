---
title: "leaps_alarm_start"
lang: en
slug: "leaps-rtls/integration-guide/api-commands/leaps-alarm-start"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/leaps-rtls/integration-guide/api-commands/leaps-alarm-start/"
order: 147
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-alarm-start">
<span id="id1"></span><h1>leaps_alarm_start</h1>
<p>Activates on board alarm for a specified time period.</p>
<hr class="docutils">
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
Input</div>
<ul class="simple">
<li><p class="sd-card-text">LED, motor, buzzer: ‘0’ | ‘1’ (<em>1 enables particular alarm</em>)</p></li>
<li><p class="sd-card-text">duration: 8-bit unsigned integer (alarm time period in multiple of 200 ms)</p></li>
<li><p class="sd-card-text">intensity: 8-bit unsigned integer (<em>alarm intensity</em>)</p></li>
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
<col style="width: 17%">
<col style="width: 17%">
<col style="width: 66%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV Request</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Type</p></td>
<td><p>Length</p></td>
<td><p>Value</p></td>
</tr>
<tr class="row-odd"><td rowspan="2"><p>0x85</p></td>
<td rowspan="2"><p>0x04</p></td>
<td><p>byte 0: alarm conf iguration</p>
<ul class="simple">
<li><p>bit 0 - enable LED</p></li>
<li><p>bit 1 - enable buzzer</p></li>
<li><p>bit 2 - enable motor</p></li>
<li><p>bit 3-7 reserved</p></li>
</ul>
<div class="line-block">
<div class="line">byte 1: reserved</div>
<div class="line">byte 2: duration in multiple of 200 ms</div>
<div class="line">byte 3: intensity</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>0x07 0x00 0x05 0xff</p></td>
</tr>
</tbody>
</table>
<p>Type 0x85 means command leaps_alarm_start</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 49%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV Response</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Type</p></td>
<td><p>Length</p></td>
<td><p>Value <strong>(see error codes)</strong></p></td>
</tr>
<tr class="row-odd"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>Type 0x40 means err_code of the previous command</p>
</div>


           </div>
