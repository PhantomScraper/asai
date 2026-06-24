---
title: "leaps_fw_update_xfer"
lang: en
slug: "leaps-rtls/integration-guide/api-commands/leaps-fw-update-xfer"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/leaps-rtls/integration-guide/api-commands/leaps-fw-update-xfer/"
order: 239
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-fw-update-xfer">
<span id="id1"></span><h1>leaps_fw_update_xfer</h1>
<hr class="docutils">
<p>Should be called repeatedly after <a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/api-commands/leaps-fw-update-start#leaps-fw-update-start"><span class="std std-ref">leaps_fw_update_start</span></a> to transfer firmware
data chunks until all the firmware is transferred. Returns status “ok”
if the data chunk was processed successfully or an error. The error is
indicated by status other than “ok”. The reasons for failed firmware
update are:</p>
<ul class="simple">
<li><p>internal error</p></li>
<li><p>invalid parameter - e.g. data chunk with zero length, or corrupted data</p></li>
<li><p>not permitted - not started yet or the whole update process has failed</p></li>
<li><p>checksum error - corrupted data received or the checksum value provided at the start of the update by the <a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/api-commands/leaps-fw-update-start#leaps-fw-update-start"><span class="std std-ref">leaps_fw_update_start</span></a> and the checksum calculated by the module at the end does not match</p></li>
</ul>
<p>The size and offset of the data that have been processed so far by the firmware update
procedure are returned in the response to each call of leaps_fw_update_xfer until the
update is complete.</p>
<hr class="docutils">
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
Input</div>
<ul class="simple">
<li><p class="sd-card-text">offset: 32-bit integer (<em>Offset of the total firmware data.</em>)</p></li>
<li><p class="sd-card-text">data: from 4 up to 240 bytes (<em>Firmware data chunk.</em>)</p></li>
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
<li><p class="sd-card-text">offset: 32-bit integer (<em>Offset of data that need to be written next by leaps_fw_update_xfer</em>)</p></li>
<li><p class="sd-card-text">size: 32-bit integer (<em>Size of firmware data chunk that need to be written by leaps_fw_update_xfer</em>)</p></li>
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
<col style="width: 13%">
<col style="width: 11%">
<col style="width: 24%">
<col style="width: 51%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="4"><p>TLV Request</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="2"><p>Type</p></td>
<td rowspan="2"><p>Length</p></td>
<td colspan="2"><p>Value</p></td>
</tr>
<tr class="row-odd"><td><p>offset</p></td>
<td><p>data chunk</p></td>
</tr>
<tr class="row-even"><td><p>0x3F</p></td>
<td><p>0x24</p></td>
<td><p>0x00 0x00 0x00
0x00</p></td>
<td><p>0xA5 0xA5 0xA5 0xA5 0xA5 0xA5 0xA5
0xA5 …. 0xA5 0xA5 0xA5 0xA5</p></td>
</tr>
</tbody>
</table>
<p>Type 0x3F (63 dec) means command leaps_fw_update_xfer</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 14%">
<col style="width: 11%">
<col style="width: 11%">
<col style="width: 8%">
<col style="width: 11%">
<col style="width: 23%">
<col style="width: 23%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="7"><p>TLV response</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="2"><p>Type</p></td>
<td rowspan="2"><p>Length</p></td>
<td rowspan="2"><p>Value</p></td>
<td rowspan="2"><p>Type</p></td>
<td rowspan="2"><p>Length</p></td>
<td colspan="2"><p>Value</p></td>
</tr>
<tr class="row-odd"><td><p>offset</p></td>
<td><p>size</p></td>
</tr>
<tr class="row-even"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x04</p></td>
<td><p>0x7E</p></td>
<td><p>0x08</p></td>
<td><p>0x00 0x00 0x00
0x00</p></td>
<td><p>0x00 0x10 0x00
0x00</p></td>
</tr>
</tbody>
</table>
<p>Type 0x40 means status code</p>
<p>Type 0x7E (126 dec) means firmware data request</p>
</div>


           </div>
