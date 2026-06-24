---
title: "leaps_panid_profile_get"
lang: en
slug: "leaps-rtls/integration-guide/api-commands/leaps-panid-profile-get"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/leaps-rtls/integration-guide/api-commands/leaps-panid-profile-get/"
order: 265
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-panid-profile-get">
<span id="id1"></span><h1>leaps_panid_profile_get</h1>
<p>Get UWB network identifier (PANID) along with the ZONE ID to assist with anchor selection. The PANID Mask and Actual PANID, which
help support tag roaming across multiple distinct networks with varying PANIDs.</p>
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
<li><p class="sd-card-text">panid: 16-bit unsigned integer (<em>the UWB panid</em>)</p></li>
<li><p class="sd-card-text">panid_mask: 16-bit unsigned integer (<em>the UWB panid mask</em>)</p></li>
<li><p class="sd-card-text">actual_panid: 16-bit unsigned integer (<em>the UWB actual panid of TN</em>)</p></li>
<li><p class="sd-card-text">zone_id: 8-bit unsigned integer (<em>the UWB zone id of AN</em>)</p></li>
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
<tr class="row-odd"><td><p>0x41</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>Type 0x41 means command leaps_panid_profile_get</p>
<p>If the devices is AN, the <cite>actual_panid</cite> is the same with <cite>panid</cite></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 8%">
<col style="width: 11%">
<col style="width: 11%">
<col style="width: 8%">
<col style="width: 11%">
<col style="width: 9%">
<col style="width: 14%">
<col style="width: 14%">
<col style="width: 15%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="9"><p>TLV
response</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="2"><p>Type</p></td>
<td rowspan="2"><p>Length</p></td>
<td><p>Value</p></td>
<td rowspan="2"><p>Type</p></td>
<td rowspan="2"><p>Length</p></td>
<td colspan="4"><p>Value</p></td>
</tr>
<tr class="row-odd"><td><p>status
code</p></td>
<td><p>panid</p></td>
<td><p>panid
mask</p></td>
<td><p>actual
panid</p></td>
<td><p>zone id</p></td>
</tr>
<tr class="row-even"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
<td><p>0xC2</p></td>
<td><p>0x06</p></td>
<td><p>0xCD
0xAB</p></td>
<td><p>0xFF
0xFF</p></td>
<td><p>0xCD
0xAB</p></td>
<td><p>0x01</p></td>
</tr>
</tbody>
</table>
<p>Type 0x40 means status code</p>
<p>Type 0xC2 means PANID Profile</p>
</div>


           </div>
