---
title: "leaps_uwb_cfg_get"
lang: en
slug: "leaps-rtls/integration-guide/api-commands/leaps-uwb-cfg-get"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/leaps-rtls/integration-guide/api-commands/leaps-uwb-cfg-get/"
order: 275
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-uwb-cfg-get">
<span id="id1"></span><h1>leaps_uwb_cfg_get</h1>
<p>Gets UWB configuration parameters.</p>
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
<li><p class="sd-card-text">preamble_code: ‘9’ | ‘10’ | ‘11’ | ‘12’ (<em>UWB preamble code</em>)</p></li>
<li><p class="sd-card-text">pg_delay: 1 byte (<em>Transmitter Calibrat Pulse Generator Delay value</em>)</p></li>
<li><p class="sd-card-text">channel: ‘2’ | ‘3’ | ‘5’ | ‘9’ (<em>UWB channel</em>)</p></li>
<li><p class="sd-card-text">lna_enable: ‘0’ | ‘1’</p></li>
<li><p class="sd-card-text">pa_enable: ‘0’ | ‘1’</p></li>
<li><p class="sd-card-text">rf1_enable: ‘0’ | ‘1’</p></li>
<li><p class="sd-card-text">rf2_enable: ‘0’ | ‘1’</p></li>
<li><p class="sd-card-text">tx_power: 4 bytes (<em>Units of transmission power control</em>)</p></li>
<li><p class="sd-card-text">rf_compliance: ‘0’ | ‘1’ | ‘2’ (<em>RF compliance option, 0: FCC/ETSI, 1: ETSI + 10dB, 2: ARIB, 3: Custom</em>)</p></li>
<li><p class="sd-card-text">pg_delay_comp: 1 byte (<em>Transmitter Calibrati Pulse Generator Delay value,  Compensated</em>)</p></li>
<li><p class="sd-card-text">tx_power_comp: 4 bytes (<em>Units of transmission power control, Compensated</em>)</p></li>
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
<tr class="row-odd"><td><p>0x18</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>Type 0x18 (24 dec) means command leaps_uwb_cfg_get</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 8%">
<col style="width: 10%">
<col style="width: 8%">
<col style="width: 8%">
<col style="width: 10%">
<col style="width: 55%">
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
<div class="line">(1st byte) preamble_code</div>
<div class="line">(2nd byte) pg_delay</div>
<div class="line">(3rd byte) channel</div>
<div class="line">(4th byte, bit 0) lna_enable</div>
<div class="line">(4th byte, bit 1) pa_enable</div>
<div class="line">(4th byte, bit 2) rf1_enable</div>
<div class="line">(4th byte, bit 3) rf2_enable</div>
<div class="line">(4th byte, bits 4-8) reserved</div>
<div class="line">(5t h-8th byte) tx_power</div>
<div class="line">(9th byte) rf_compliance</div>
<div class="line">(10th byte) pg_dela_comp</div>
<div class="line">(11th -12th byte) reserved</div>
<div class="line">(13th -16th byte) tx_power_comp</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
<td><p>0x4F</p></td>
<td><p>0x10</p></td>
<td><p>0x09 0x34 0x05 0x03 0xfd 0xfd 0xfd 0xfd
0x00 0x34 0x00 0x00 0xfd 0xfd 0xfd 0xfd</p></td>
</tr>
</tbody>
</table>
<p>Type 0x4F means UWB configuration</p>
</div>


           </div>
