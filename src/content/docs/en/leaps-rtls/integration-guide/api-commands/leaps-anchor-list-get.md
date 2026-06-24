---
title: "leaps_anchor_list_get"
lang: en
slug: "leaps-rtls/integration-guide/api-commands/leaps-anchor-list-get"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/leaps-rtls/integration-guide/api-commands/leaps-anchor-list-get/"
order: 233
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-anchor-list-get">
<span id="id1"></span><h1>leaps_anchor_list_get</h1>
<p>Read list of surrounding anchors. Works for anchors only. Anchors in the
list can be from the same network or from neighbor network as well.</p>
<hr class="docutils">
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
Input</div>
<ul class="simple">
<li><p class="sd-card-text">offset: 8-bit unsigned integer (<em>Offset on anchor list, used when there are more than 8 anchors in the list; 0 - no offset</em>)</p></li>
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
<li><p class="sd-card-text"><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/leaps-api/api-generic-data-types#statuscode"><span class="std std-ref">Status Code</span></a>, timestamp, flags, count, [anchor_0, anchor_1, …]</p></li>
<li><p class="sd-card-text">timestamp: 32-bit unsigned integer (<em>up-time in microseconds</em>)</p></li>
<li><p class="sd-card-text">count: 1 byte (<em>element count, 8 is the maximum number of elements in the list that 1 TLV response could carry</em>)</p></li>
<li><p class="sd-card-text">anchor_1, anchor_2, …, anchor_N: (<em>list of anchors</em>)</p></li>
<li><p class="sd-card-text">anchor_N: node_id, position, rssi, seat, neighbor_network (<em>anchor list element where N can be from 1 to 8</em>)</p></li>
<li><p class="sd-card-text">node_id: 2 bytes (<em>anchor ID</em>)</p></li>
<li><p class="sd-card-text">position: 12 bytes</p></li>
<li><p class="sd-card-text">rssi: 1 byte signed (<em>signal strength indicator</em>)</p></li>
<li><p class="sd-card-text">rx_rate: 1 byte unsigned (<em>packet error rate</em>)</p></li>
<li><p class="sd-card-text">seat: 5 bits (<em>seat number occupied by the anchor</em>)</p></li>
<li><p class="sd-card-text">neighbor_network: 1 bit (<em>status flags that indicates if anchor is from current network or if it is from neighbor network</em>)</p></li>
<li><p class="sd-card-text">seens: 1 byte (<em>Number of BCN frames received from the anchor. This counter overflows at 255</em>)</p></li>
<li><p class="sd-card-text">rx_coll: 16-bit unsigned integer (<em>Number of seat collisions with this anchor</em>)</p></li>
<li><p class="sd-card-text">rx_consec: 1 byte (<em>Number of consecutive BCN frames received from the anchor</em>)</p></li>
<li><p class="sd-card-text">dist: 32-bit unsigned integer (<em>Distance from the anchor in millimeters</em>)</p></li>
<li><p class="sd-card-text">drift_avg: float (4 bytes) (<em>Average clock drift w.r.t the anchor</em>)</p></li>
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
<tr class="row-odd"><td><p>0x0B</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>Type 0x0B means command leaps_anchor_list_get</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 32%">
<col style="width: 26%">
<col style="width: 41%">
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
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 3%">
<col style="width: 4%">
<col style="width: 9%">
<col style="width: 5%">
<col style="width: 10%">
<col style="width: 8%">
<col style="width: 10%">
<col style="width: 5%">
<col style="width: 5%">
<col style="width: 13%">
<col style="width: 5%">
<col style="width: 5%">
<col style="width: 5%">
<col style="width: 5%">
<col style="width: 5%">
<col style="width: 4%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="16"><p>TLV response (residue of the frame from previous table)</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Type</p></td>
<td><p>Length</p></td>
<td colspan="14"><p>Value</p></td>
</tr>
<tr class="row-odd"><td rowspan="3"><p>0x56</p></td>
<td rowspan="3"><p>0xE1</p></td>
<td rowspan="2"><p>uint32 -
timestamp
(little endian)</p></td>
<td rowspan="2"><p>uint8 -
flags</p></td>
<td rowspan="2"><p>uint8 - number of
elements encoded
in the list</p></td>
<td colspan="10"><p>anchor nr. 1</p></td>
<td><p>anchors
nr. 2
…
nr. 8</p></td>
</tr>
<tr class="row-even"><td><p>uint16 -
UWB address in
little endian</p></td>
<td><p>3 x int32 -
position coordinates
x,y,z in little
endian</p></td>
<td><p>int8 -
RSSI</p></td>
<td><p>uint8 -
rx_rate</p></td>
<td><div class="line-block">
<div class="line">uint8 - flags</div>
</div>
<div class="line-block">
<div class="line">(bits 0-4) seat number</div>
<div class="line">(bit 5) neighbor_network</div>
<div class="line">(bits 6-7) reserved</div>
</div>
</td>
<td><p>uint8 -
seens</p></td>
<td><p>uint16 -
rx_coll</p></td>
<td><p>uint8 -
rx_consec</p></td>
<td><p>uint32 -
dist</p></td>
<td><p>float -
drift_avg</p></td>
<td><p>…</p></td>
</tr>
<tr class="row-odd"><td><p>0xe8
0x03
0x00
0x00</p></td>
<td><p>0x00</p></td>
<td><p>0x08</p></td>
<td colspan="10"><p>0xab 0xbc …</p></td>
<td><p>…</p></td>
</tr>
</tbody>
</table>
<p>Type 0x40 means status code</p>
<p>Type 0x56 means anchor list</p>
</div>


           </div>
