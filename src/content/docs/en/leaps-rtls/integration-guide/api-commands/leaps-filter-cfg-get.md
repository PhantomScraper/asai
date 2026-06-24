---
title: "leaps_filter_cfg_get"
lang: en
slug: "leaps-rtls/integration-guide/api-commands/leaps-filter-cfg-get"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/leaps-rtls/integration-guide/api-commands/leaps-filter-cfg-get/"
order: 254
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-filter-cfg-get">
<span id="id1"></span><h1>leaps_filter_cfg_get</h1>
<p>Read configuration of one of the filters (e.g. location filter or
measurement filter).</p>
<hr class="docutils">
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
Input</div>
<ul class="simple">
<li><p class="sd-card-text">id: ?8-bit unsigned integer (<em>ID of the filter, 0 - measurement filter, 1 - location filter, 2 - measurement selection strategy, 3 - position coordinate</em>)</p></li>
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
<li><p class="sd-card-text">filter_id: 8-bits unsigned integer (<em>ID of the filter, 0 - measurement filter, 1 - location filter. 2 - measurement selection strategy, 3 - position coordinate</em>)</p></li>
<li><p class="sd-card-text">filter_val: byte array with maximum length 12 ?</p></li>
</ul>
</div>
</div>
</div>
</div>
</div>
<div class="section" id="filter-values">
<h2>Filter values</h2>
<table class="colwidths-given docutils align-default">
<colgroup>
<col style="width: 20%">
<col style="width: 80%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Filter ID</p></th>
<th class="head"><p>Filter Val</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>0 (measurement)</p></td>
<td><p>TBD</p></td>
</tr>
<tr class="row-odd"><td><p>1 (location)</p></td>
<td><p>Byte[0] = Mode (0 - Disable Moving Average Filter, 1 - Enable Moving Average Filter)</p></td>
</tr>
<tr class="row-even"><td><p>2 (measurement selection strategy)</p></td>
<td><p>Byte[0] = Type (0 - QUAD, 1 - RSSI, 2 - Round robin)</p></td>
</tr>
<tr class="row-odd"><td><p>3 (position coordinate)</p></td>
<td><div class="line-block">
<div class="line">Byte[0] = Type (0 - CARTESIAN, 1 - WSG84)</div>
<div class="line">If Type = 1(WSG84)</div>
<div class="line-block">
<div class="line">Byte[1]..Byte[4] = WSG84 Latitude of the Cartesian origin[0,0,0] * 10^7</div>
<div class="line">Byte[5]..Byte[8] = WSG84 Longitude of the Cartesian origin[0,0,0] * 10^7</div>
</div>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div class="section" id="measurement-selection-strategy">
<h2>Measurement selection strategy</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 24%">
<col style="width: 76%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Strategy</p></th>
<th class="head"><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>QUAD</p></td>
<td><p>TN selects up to 4 measurements of ANs from 4
quadrants for the best TN location calculation</p></td>
</tr>
<tr class="row-odd"><td><p>RSSI</p></td>
<td><p>TN selects up to 4 measurements of ANs with highest
RSSI</p></td>
</tr>
<tr class="row-even"><td><p>Round robin</p></td>
<td><p>TN takes turn to select up to 4 measurements from
all ANs in it’s anchor list in the round robin
manner. (e.g: anchor list has 6 ANs (1,2,3,4,5,6),
each round TN selects measurements of ANs:
(1,2,3,4), (5,6,1,2), (3,4,5,6) …</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
<p><strong>Example</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 26%">
<col style="width: 24%">
<col style="width: 50%">
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
<tr class="row-odd"><td><p>filter id</p></td>
</tr>
<tr class="row-even"><td><p>0x1B</p></td>
<td><p>0x01</p></td>
<td><p>0x03</p></td>
</tr>
</tbody>
</table>
<p>Type 0x1B (27 dec) means command leaps_filter_cfg_get</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 24%">
<col style="width: 15%">
<col style="width: 12%">
<col style="width: 9%">
<col style="width: 12%">
<col style="width: 18%">
<col style="width: 12%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="7"><p>TLV response</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="2"><p>Type</p></td>
<td rowspan="2"><p>Length</p></td>
<td><p>Value</p></td>
<td rowspan="2"><p>Type</p></td>
<td rowspan="2"><p>Length</p></td>
<td colspan="2"><p>Value</p></td>
</tr>
<tr class="row-odd"><td><p>status
code</p></td>
<td><p>filter id</p></td>
<td><p>filter
val</p></td>
</tr>
<tr class="row-even"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
<td><p>0x54</p></td>
<td><p>0x0a</p></td>
<td><p>0x03</p></td>
<td><p>0x01
0x18
0x49
0xB7
0xFA
0xD3
0xE6
0xAF
0x00</p></td>
</tr>
</tbody>
</table>
<p>Type 0x40 means status code</p>
<p>Type 0x54 (84) means filter configuration</p>
</div>
</div>


           </div>
