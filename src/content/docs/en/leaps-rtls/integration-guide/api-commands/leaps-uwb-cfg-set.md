---
title: "leaps_uwb_cfg_set"
lang: en
slug: "leaps-rtls/integration-guide/api-commands/leaps-uwb-cfg-set"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/leaps-rtls/integration-guide/api-commands/leaps-uwb-cfg-set/"
order: 274
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-uwb-cfg-set">
<span id="id1"></span><h1>leaps_uwb_cfg_set</h1>
<p>Sets UWB configuration parameters.</p>
<ul class="simple">
<li><p>DW1000: can support channel 2, 3 and Channel 5.</p></li>
<li><p>DW3000: can support channel 5 and 9.</p></li>
</ul>
<hr class="docutils">
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
Input</div>
<ul class="simple">
<li><p class="sd-card-text">preamble_code: ‘9’ | ‘10’ | ‘11’ | ‘12’ (<em>UWB preamble code</em>)</p></li>
<li><p class="sd-card-text">channel: ‘2’ | ‘3’ | ‘5’ | ‘9’ (<em>UWB channel</em>)</p></li>
<li><p class="sd-card-text">pg_delay: 1 byte (<em>Transmitter Calibration – Pulse Generator Delay</em>)</p></li>
<li><p class="sd-card-text">lna_enable: ‘0’ | ‘1’</p></li>
<li><p class="sd-card-text">pa_enable: ‘0’ | ‘1’</p></li>
<li><p class="sd-card-text">rf1_enable: ‘0’ | ‘1’</p></li>
<li><p class="sd-card-text">rf2_enable: ‘0’ | ‘1’</p></li>
<li><p class="sd-card-text">tx_power: 4 bytes (<em>TX Power Control</em>)</p></li>
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
<col style="width: 18%">
<col style="width: 18%">
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
<div class="line">(1st byte) preamble_code</div>
<div class="line">(2nd byte) pg_delay</div>
<div class="line">(3rd byte) channel</div>
<div class="line">(4th byte, bit 0) lna_enable</div>
<div class="line">(4th byte, bit 1) pa_enable</div>
<div class="line">(4th byte, bit 2) rf1_enable</div>
<div class="line">(4th byte, bit 3) rf2_enable</div>
<div class="line">(4th byte, bits 4-8) reserved</div>
<div class="line">(5th-8th byte) tx_power</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>0x17</p></td>
<td><p>0x08</p></td>
<td><p>0x09 0xC3
0x05 0x03
0x85 0x65
0x45 0x25</p></td>
</tr>
</tbody>
</table>
<p>Type 0x17 means command leaps_uwb_cfg_set</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 34%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV Reponse</p></th>
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
</div>


           </div>
