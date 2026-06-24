---
title: "leaps_loc_get"
lang: en
slug: "leaps-rtls/integration-guide/api-commands/leaps-loc-get"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/leaps-rtls/integration-guide/api-commands/leaps-loc-get/"
order: 226
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-loc-get">
<span id="id1"></span><h1>leaps_loc_get</h1>
<hr class="docutils">
<p>Get last distances to the ranging anchors and get the position.The event
is generated and the status changes when all TWR measurements are
completed and new location data are available for the user. When low
power mode is used, it will work in the same way.</p>
<p>For anchor node, the position and distances are available only if the
auto-positioning procedure has been done. The auto-positioning procedure
is started via the BLE interface.</p>
<hr class="docutils">
<p><strong>Tag node</strong></p>
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
Input</div>
<ul class="simple">
<li><p class="sd-card-text">8-bit unsigned integer (output options, 0 - distances to ranging anchors, 1 - my position + distances to ranging anchors, 2 - positions and distances to ranging anchors, 3 - my position + distances and position to ranging anchors)</p></li>
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
<li><p class="sd-card-text"><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/leaps-api/api-generic-data-types#statuscode"><span class="std std-ref">Status Code</span></a>, [my_position], [timestamp, flags, count, [{addr, anchor_distance, pqf}, …]], [timestamp, flags, count, [{anchor_position, addr, anchor_distance, pqf}, ..]]</p></li>
<li><p class="sd-card-text">timestamp: 32-bit integer? (timestamp in microseconds)</p></li>
<li><p class="sd-card-text">flags: 8-bit unsigned integer? (is_moving indication)</p></li>
<li><p class="sd-card-text">count: 8-bit integer (number of elements in the list that follows, the list can contain positions, distances or both)</p></li>
<li><p class="sd-card-text">my_position, anchor_position: 13 bytes (See <a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/leaps-api/api-generic-data-types#position"><span class="std std-ref">Position</span></a>)</p></li>
<li><p class="sd-card-text">addr: 16-bit integer (UWB address/id of the opposite node)</p></li>
<li><p class="sd-card-text">distance: 32-bit integer (distance to the opposite in millimeters)</p></li>
<li><p class="sd-card-text">pqf: 8-bit integer (quality factor)</p></li>
</ul>
</div>
</div>
</div>
</div>
</div>
<hr class="docutils">
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>If <strong>Tag node</strong> - available parameter - pos: <strong>position</strong> (position of the opposite node, that correspond with the distance)</p>
</div>
<hr class="docutils">
<p><strong>Example 1 (my position + distances and positions to ranging anchors)</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 35%">
<col style="width: 32%">
<col style="width: 32%">
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
<tr class="row-odd"><td><p>0x0C</p></td>
<td><p>0x01</p></td>
<td><p>0x03</p></td>
</tr>
</tbody>
</table>
<p>Type 0x0C means command loc_get</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 12%">
<col style="width: 10%">
<col style="width: 10%">
<col style="width: 7%">
<col style="width: 10%">
<col style="width: 16%">
<col style="width: 7%">
<col style="width: 10%">
<col style="width: 19%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="9"><p>TLV
response</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Type</p></td>
<td><p>Length</p></td>
<td><p>Value
status</p></td>
<td><p>Type</p></td>
<td><p>Length</p></td>
<td><p>Value
position of
this node
(13 bytes)</p></td>
<td><p>Type</p></td>
<td><p>Length</p></td>
<td><p>Value
positions and
distances to
ranging
anchors
(86 bytes)</p></td>
</tr>
<tr class="row-odd"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
<td><p>0x41</p></td>
<td><p>0x0D</p></td>
<td><p>…</p></td>
<td><p>0x49</p></td>
<td><p>0x56</p></td>
<td><p>…</p></td>
</tr>
</tbody>
</table>
<p>Type 0x40 means status code</p>
<p>Type 0x41 means position</p>
<p>Type 0x49 means position and distances on a tag node</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 16%">
<col style="width: 27%">
<col style="width: 13%">
<col style="width: 13%">
<col style="width: 14%">
<col style="width: 17%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="6"><p>Encoding of positions and distances to ranging anchors</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="2"><p>Timestamp in
microseconds</p></td>
<td rowspan="2"><div class="line-block">
<div class="line">flags (1 byte)</div>
</div>
<div class="line-block">
<div class="line">(bit 0) is_moving</div>
<div class="line">(bits 1-7) reserved</div>
</div>
</td>
<td rowspan="2"><p>number of
encoded
positions
and
distances
(1 byte)</p></td>
<td colspan="2"><p>position
and
distance
nr. 1
(20 bytes)</p></td>
<td><p>position and
distance
nr.2, 3, 4
(60 bytes)</p></td>
</tr>
<tr class="row-odd"><td><p>distance
nr.1</p>
<p>(7 bytes)</p>
</td>
<td><p>position
nr.1</p>
<p>(13 bytes)</p>
</td>
<td><p>…</p></td>
</tr>
<tr class="row-even"><td><p>0x64
0x0A
0x01
0x00</p></td>
<td><p>0x00</p></td>
<td><p>0x04</p></td>
<td><p>…</p></td>
<td><p>…</p></td>
<td><p>…</p></td>
</tr>
</tbody>
</table>
<p>Type 0x49 means position and distances on a tag node.</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 24%">
<col style="width: 39%">
<col style="width: 37%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>Distance encoding</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>UWB address</p>
<p>(2 bytes)</p>
</td>
<td><p>distance in millimeters</p>
<p>(4 bytes)</p>
</td>
<td><p>distance quality factor
in percents
(1 byte)</p></td>
</tr>
<tr class="row-odd"><td><p>0xAB 0xCD</p></td>
<td><p>0xE8 0x03 0x00 0x00</p></td>
<td><p>0x5F</p></td>
</tr>
</tbody>
</table>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 25%">
<col style="width: 23%">
<col style="width: 25%">
<col style="width: 28%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="4"><p>Position encoding</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>x coordinate
in millimeters</p>
<p>(4 bytes)</p>
</td>
<td><p>y coordinate
in
millimeters
(4 bytes)</p></td>
<td><p>z coordinate
in millimeters</p>
<p>(4 bytes)</p>
</td>
<td><p>position quality
factor in
percents
(1 byte)</p></td>
</tr>
<tr class="row-odd"><td><p>0x4b 0x0a 0x00
0x00</p></td>
<td><p>0x1f 0x04
0x00 0x00</p></td>
<td><p>0x9c 0x0e 0x00
0x00</p></td>
<td><p>0x64</p></td>
</tr>
</tbody>
</table>
<p><strong>Example 2 (my position + distances to ranging anchors)</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 35%">
<col style="width: 32%">
<col style="width: 32%">
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
<tr class="row-odd"><td><p>0x0C</p></td>
<td><p>0x01</p></td>
<td><p>0x03</p></td>
</tr>
</tbody>
</table>
<p>Type 0x0C means command loc_get</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 12%">
<col style="width: 10%">
<col style="width: 10%">
<col style="width: 7%">
<col style="width: 10%">
<col style="width: 16%">
<col style="width: 7%">
<col style="width: 10%">
<col style="width: 19%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="9"><p>TLV response</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="2"><p>Type</p></td>
<td rowspan="2"><p>Length</p></td>
<td><p>Value</p></td>
<td rowspan="2"><p>Type</p></td>
<td rowspan="2"><p>Length</p></td>
<td><p>Value</p></td>
<td rowspan="2"><p>Type</p></td>
<td rowspan="2"><p>Length</p></td>
<td><p>Value</p></td>
</tr>
<tr class="row-odd"><td><p>status
code</p></td>
<td><p>position of
this node
(13 bytes)</p></td>
<td><p>distances to
ranging
anchors
(90 bytes)</p></td>
</tr>
<tr class="row-even"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
<td><p>0x41</p></td>
<td><p>0x0D</p></td>
<td><p>…</p></td>
<td><p>0x48</p></td>
<td><p>0x5A</p></td>
<td><p>…</p></td>
</tr>
</tbody>
</table>
<p>Type 0x40 means status code</p>
<p>Type 0x41 means position</p>
<p>Type 0x48 means distances of ranging anchors</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 16%">
<col style="width: 29%">
<col style="width: 13%">
<col style="width: 17%">
<col style="width: 24%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="5"><p>Encoding of distances to ranging anchors</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>timestamp
in
microseconds
(4 bytes)</p></td>
<td><div class="line-block">
<div class="line">flags (1 byte)</div>
</div>
<div class="line-block">
<div class="line">(bit 0) is_moving</div>
<div class="line">(bits 1-7) reserved</div>
</div>
</td>
<td><p>number
of
distances
encoded</p>
<p>(1 byte)</p>
</td>
<td><p>distance nr.1</p>
<p>(7 bytes)</p>
</td>
<td><p>distance nr. 2, 3,
… , 11, 12</p>
<p>(77 bytes)</p>
</td>
</tr>
<tr class="row-odd"><td><p>0x64
0x12
0x0E
0x00</p></td>
<td><p>0x00</p></td>
<td><p>0x04</p></td>
<td><p>…</p></td>
<td><p>…</p></td>
</tr>
</tbody>
</table>
</div>


           </div>
