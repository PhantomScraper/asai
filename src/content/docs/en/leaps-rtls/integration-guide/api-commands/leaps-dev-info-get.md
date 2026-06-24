---
title: "leaps_dev_info_get"
lang: en
slug: "leaps-rtls/integration-guide/api-commands/leaps-dev-info-get"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/leaps-rtls/integration-guide/api-commands/leaps-dev-info-get/"
order: 234
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-dev-info-get">
<span id="id1"></span><h1>leaps_dev_info_get</h1>
<p>Get information about the firmware and hardware of the module.</p>
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
<li><p class="sd-card-text">fw_id: 32-bits integer (<em>firmware id. Possible values are ‘0’ for BLDR, ‘1’ for ELDR - Extended Loader or ‘2’ for main firmware. Main firmware is the default. ELDR is a limited version of main firmware and servers mainly as backup during the firmware update. The ELDR is not supported on all HW.</em>)</p></li>
<li><p class="sd-card-text">bldr_version: 32-bits integer (<em>maj, min, patch, res, var</em>)</p></li>
<li><p class="sd-card-text">eldr_version: 32-bits integer (<em>maj, min, patch, res, var, value 0xFFFFFFFF means that the HW does not support ELDR</em>)</p></li>
<li><p class="sd-card-text">fw_version: 32-bits integer (<em>maj, min, patch, res, var</em>)</p></li>
<li><p class="sd-card-text">bldr_checksum: 32-bits integer</p></li>
<li><p class="sd-card-text">eldr_checksum: 32-bits integer (<em>value 0xFFFFFFFF means that the HW does not support ELDR</em>)</p></li>
<li><p class="sd-card-text">fw_checksum: 32-bits integer</p></li>
<li><p class="sd-card-text">cfg_version: 32-bits integer</p></li>
<li><p class="sd-card-text">hw_version: 32-bits integer</p></li>
</ul>
</div>
</div>
</div>
</div>
</div>
<hr class="docutils">
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 20%">
<col style="width: 18%">
<col style="width: 18%">
<col style="width: 22%">
<col style="width: 22%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="5"><p>firmware version encoding</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>maj = bits
24 - 31</p>
<p>(MAJOR)</p>
</td>
<td><p>min = bits
16 - 23</p>
<p>(MINOR)</p>
</td>
<td><p>patch = bits
8 - 15</p>
<p>(PATCH)</p>
</td>
<td><p>res = bits
4 - 7</p>
<p>(RESERVED)</p>
</td>
<td><p>var = bits
0 - 3</p>
<p>(VARIANT)</p>
</td>
</tr>
</tbody>
</table>
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
<tr class="row-odd"><td><p>0x15</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>Type 0x15 means command leaps_dev_info_get</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 11%">
<col style="width: 8%">
<col style="width: 7%">
<col style="width: 6%">
<col style="width: 8%">
<col style="width: 8%">
<col style="width: 24%">
<col style="width: 14%">
<col style="width: 13%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="9"><p>TLV response</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="2"><p>Type</p></td>
<td rowspan="2"><p>Length</p></td>
<td rowspan="2"><p>Value</p></td>
<td rowspan="2"><p>Type</p></td>
<td rowspan="2"><p>Length</p></td>
<td colspan="4"><p>Value</p></td>
</tr>
<tr class="row-odd"><td><p>fw_id</p></td>
<td><p>bldr_version
eldr_version
fw_version
bldr_checksum
eldr_checksum
fw_checksum</p></td>
<td><p>cfg_version</p></td>
<td><p>hw_version</p></td>
</tr>
<tr class="row-even"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
<td><p>0x50</p></td>
<td><p>0x24</p></td>
<td><p>0x00
0x00
0x00
0x01</p></td>
<td><p>0x00 0x00 0x03 0x01
0xff 0xff 0xff 0xff
0x01 0x00 0x03 0x01
0xd2 0x81 0x9d 0x59
0xff 0xff 0xff 0xff
0xa7 0x34 0x01 0xcd</p></td>
<td><p>0x00
0x07
0x01
0x00</p></td>
<td><p>0x00
0x01
0x41
0xDE</p></td>
</tr>
</tbody>
</table>
<p>Type 0x40 means status code</p>
<p>Type 0x50 means device information</p>
</div>


           </div>
