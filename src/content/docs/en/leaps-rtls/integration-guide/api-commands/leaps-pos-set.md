---
title: "leaps_pos_set"
lang: en
slug: "leaps-rtls/integration-guide/api-commands/leaps-pos-set"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/leaps-rtls/integration-guide/api-commands/leaps-pos-set/"
order: 227
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-pos-set">
<span id="id1"></span><h1>leaps_pos_set</h1>
<p>Set default position of the node. Default position is not used when in
tag mode but is stored anyway so the module can be configured to anchor
mode and use the value previously set by leaps_pos_set. This call does a
write to internal flash in case of new value being set, hence should not
be used frequently and can take in worst case hundreds of milliseconds!</p>
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
Input</div>
<ul class="simple">
<li><p class="sd-card-text">x: 32-bit integer (position coordinate in millimeters)</p></li>
<li><p class="sd-card-text">y: 32-bit integer (position coordinate in millimeters)</p></li>
<li><p class="sd-card-text">z: 32-bit integer (position coordinate in millimeters)</p></li>
<li><p class="sd-card-text">pqf: 8-bit integer (position quality factor)</p></li>
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
<p><strong>Example 1</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 12%">
<col style="width: 12%">
<col style="width: 18%">
<col style="width: 21%">
<col style="width: 20%">
<col style="width: 16%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="6"><p>TLV
request</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="2"><p>Type</p></td>
<td rowspan="2"><p>Length</p></td>
<td colspan="4"><p>Value</p></td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line">int32_t -</div>
<div class="line">little endian,</div>
<div class="line">is x</div>
<div class="line">coordinate in</div>
<div class="line">millimeters</div>
</div>
</td>
<td><div class="line-block">
<div class="line">int32_t -</div>
<div class="line">little endian,</div>
<div class="line">is y</div>
<div class="line">coordinate in</div>
<div class="line">millimeters</div>
</div>
</td>
<td><div class="line-block">
<div class="line">int32_t -</div>
<div class="line">little endian,</div>
<div class="line">is z</div>
<div class="line">coordinate in</div>
<div class="line">millimeters</div>
</div>
</td>
<td><div class="line-block">
<div class="line">uint8_t -</div>
<div class="line">is quality</div>
<div class="line">factor in</div>
<div class="line">percents</div>
<div class="line">(0-100)</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>0x01</p></td>
<td><p>0x0D</p></td>
<td colspan="4"><p>0x4b 0x0a
0x00 0x00
0x1f 0x04
0x00 0x00
0x9c 0x0e
0x00 0x00
0x64</p></td>
</tr>
</tbody>
</table>
<p>Type 0x01 means command leaps_pos_set</p>
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
