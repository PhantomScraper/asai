---
title: "dwm_fw_update_xfer"
lang: en
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-fw-update-xfer"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/pans-pro-rtls/integration-guide/api-commands/dwm-fw-update-xfer/"
order: 185
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-fw-update-xfer">
<span id="id1"></span><h1>dwm_fw_update_xfer</h1>
<p>This call is available only on the ethernet gateway. It should be called repeatedly
after <a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/api-commands/dwm-fw-update-start#dwm-fw-update-start"><span class="std std-ref">dwm_fw_update_start</span></a> to transfer firmware data chunks until all
the firmware data chunks are transferred. Returns status “ok” followed by the data
request frame until all the data needed for the firmware update is transferred,
in which case status “ok” is returned with no data request following or until the
update ends with an error. The error is indicated by status other
than “ok”. The reasons for the failed firmware update are:</p>
<ul class="simple">
<li><p>internal error</p></li>
<li><p>invalid parameter - e.g. data chunk with zero length</p></li>
<li><p>not permitted - not started yet, or the whole update process has failed</p></li>
<li><p>checksum error - received image is corrupted.</p></li>
</ul>
<p>The size and the offset of the data that are already written to the flash memory
by the firmware update procedure so far are returned as a response
to each call to <a class="reference internal" href="#dwm-fw-update-xfer"><span class="std std-ref">dwm_fw_update_xfer</span></a> until the update is completed.</p>
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
Input</div>
<ul class="simple">
<li><p class="sd-card-text">offset: 32-bit integer (<em>Offset of the total firmware data.</em>)</p></li>
<li><p class="sd-card-text">data: from 4 up to 32 bytes (<em>Firmware data chunk.</em>)</p></li>
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
<p><strong>SPI/UART example</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="4"><p>TLV Request</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Type</p></td>
<td><p>Length</p></td>
<td colspan="2"><p>Value</p></td>
</tr>
<tr class="row-odd"><td></td>
<td></td>
<td><p>Offset</p></td>
<td><p>Data Chunk</p></td>
</tr>
<tr class="row-even"><td><p>0x3F</p></td>
<td><p>0x24</p></td>
<td><p>0x00 0x00
0x00 0x00</p></td>
<td><p>0xA5 0xA5 0xA5
0xA5 0xA5 0xA5
0xA5 0xA5 ….
0xA5 0xA5 0xA5
0xA5</p></td>
</tr>
</tbody>
</table>
<p>Type 0x3F (63 dec) means command dwm_fw_update_xfer</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 17%">
<col style="width: 17%">
<col style="width: 17%">
<col style="width: 17%">
<col style="width: 17%">
<col style="width: 17%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="6"><p>TLV Response</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Type
Length</p></td>
<td><p>Value</p></td>
<td><p>Type</p></td>
<td><p>Length</p></td>
<td colspan="2"><p>Value</p></td>
</tr>
<tr class="row-odd"><td rowspan="2"><p>0x40
0x01</p></td>
<td rowspan="2"><p>0x00</p></td>
<td rowspan="2"><p>0x7E</p></td>
<td rowspan="2"><p>0x08</p></td>
<td><p>Offset</p></td>
<td><p>Size</p></td>
</tr>
<tr class="row-even"><td><p>0x00 0x00
0x00 0x00</p></td>
<td><p>0x00 0x10
0x00 0x00</p></td>
</tr>
</tbody>
</table>
<div class="line-block">
<div class="line">Type 0x40 means status code</div>
<div class="line">Type 0x7E (126 dec) means data request</div>
</div>
</div>


           </div>
