---
title: "leaps_uwbs_get"
lang: en
slug: "leaps-rtls/integration-guide/api-commands/leaps-uwbs-get"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/leaps-rtls/integration-guide/api-commands/leaps-uwbs-get/"
order: 280
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-uwbs-get">
<span id="id1"></span><h1>leaps_uwbs_get</h1>
<p>Get UWB subsystem configuration.</p>
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
<li><p class="sd-card-text">uwbs_type: ‘0’ | ‘1’ (<em>UWB subsystem , 0=LEAPS RTLS, 1=FIRA</em>)</p></li>
<li><p class="sd-card-text">uwbs_mode: ‘0’ | ‘1’ (<em>For LEAPS RTLS, this field is unused and it will return 0. For FIRA, 0=UCI, 1=NIQ</em>)</p></li>
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
<col style="width: 35%">
<col style="width: 65%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="2"><p>TLV Request</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="2"><p>Type</p></td>
<td rowspan="2"><p>Length</p></td>
</tr>
<tr class="row-odd"></tr>
<tr class="row-even"><td><p>0x8D</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>Type 0x8D means command leaps_uwbs_get</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 11%">
<col style="width: 11%">
<col style="width: 11%">
<col style="width: 11%">
<col style="width: 11%">
<col style="width: 46%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="6"><p>TLV response</p></th>
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
<tr class="row-odd"><td><p>UWB Subsystem configuration (1 byte)</p>
<div class="line-block">
<div class="line">(bits 0-1): UWB Subsystem Type</div>
<div class="line">(bits 2-3): UWB Subsystem Mode</div>
<div class="line">(bits 4-7): reserved</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
<td><p>0x8D</p></td>
<td><p>0x01</p></td>
<td><p>0x05</p></td>
</tr>
</tbody>
</table>
<p>Type 0x40 means status code
Type 0x8D means UWB Subsystem configuration</p>
</div>


           </div>
