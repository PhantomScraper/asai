---
title: "leaps_uwb_profile_get"
lang: en
slug: "leaps-rtls/integration-guide/api-commands/leaps-uwb-profile-get"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/leaps-rtls/integration-guide/api-commands/leaps-uwb-profile-get/"
order: 276
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-uwb-profile-get">
<span id="id1"></span><h1>leaps_uwb_profile_get</h1>
<p>Reads information about UWB profile that is currently active.
Returns “not permitted” if not possible to read the information because of no UWB connection.</p>
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
<li><p class="sd-card-text">sf_period_us: 32-bit unsigned integer (<em>superframe period in microseconds</em>)</p></li>
<li><p class="sd-card-text">slot_period_us: 16 bit unsigned integer (<em>slot period in microseconds</em>)</p></li>
<li><p class="sd-card-text">sf_num_max: 16 bit unsigned integer (<em>superframe number maximum value</em>)</p></li>
<li><p class="sd-card-text">anchor_upd_rate: 16 bit unsigned integer (<em>update rate of the anchor in multiply of superframe period</em>)</p></li>
<li><p class="sd-card-text">active_profile_id: ‘1’|’2’|’3’|’4’|’5’|’6’ (<em>current profile ID/number, value 0 means automatic profile</em>)</p></li>
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
<tr class="row-odd"><td><p>0x1F</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>Type 0x1F(31 dec) means command leaps_uwb_profile_get</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 4%">
<col style="width: 6%">
<col style="width: 5%">
<col style="width: 4%">
<col style="width: 6%">
<col style="width: 15%">
<col style="width: 14%">
<col style="width: 14%">
<col style="width: 13%">
<col style="width: 11%">
<col style="width: 8%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="11"><p>TLV response</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="2"><p>Type</p></td>
<td rowspan="2"><p>Length</p></td>
<td rowspan="2"><p>Value</p></td>
<td rowspan="2"><p>Type</p></td>
<td rowspan="2"><p>Length</p></td>
<td colspan="6"><p>Value</p></td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line">(byte 0-3)</div>
<div class="line">superframe period</div>
<div class="line">in microseconds</div>
</div>
</td>
<td><div class="line-block">
<div class="line">(byte 4-5)</div>
<div class="line">slot period in</div>
<div class="line">microseconds</div>
</div>
</td>
<td><div class="line-block">
<div class="line">(byte 6-7)</div>
<div class="line">superframe</div>
<div class="line">number maximum</div>
</div>
</td>
<td><div class="line-block">
<div class="line">(byte 8-9)</div>
<div class="line">anchor update</div>
<div class="line">rate</div>
</div>
</td>
<td><div class="line-block">
<div class="line">(byte 10)</div>
<div class="line">active</div>
<div class="line">profile ID</div>
</div>
</td>
<td><p>(byte 11)
reserved</p></td>
</tr>
<tr class="row-even"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
<td><p>0x5B</p></td>
<td><p>0x0C</p></td>
<td><p>0xA0 0x86
0x01 0x00</p></td>
<td><p>0xF4
0x01</p></td>
<td><p>0xa0
0x05</p></td>
<td><p>0x1E
0x00</p></td>
<td><p>0x02</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>Type 0x5B(91 dec) means UWB profile info</p>
</div>


           </div>
