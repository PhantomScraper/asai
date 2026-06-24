---
title: "leaps_fw_update_start"
lang: en
slug: "leaps-rtls/integration-guide/api-commands/leaps-fw-update-start"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/leaps-rtls/integration-guide/api-commands/leaps-fw-update-start/"
order: 238
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-fw-update-start">
<span id="id1"></span><h1>leaps_fw_update_start</h1>
<p>Starts firmware update process. Should be called at the beginning before
<a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/api-commands/leaps-fw-update-xfer#leaps-fw-update-xfer"><span class="std std-ref">leaps_fw_update_xfer</span></a> and it can take up to several seconds. If accepted,
the request returns command status: “ok” followed by the first data request.
The data request should be handled by <a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/api-commands/leaps-fw-update-xfer#leaps-fw-update-xfer"><span class="std std-ref">leaps_fw_update_xfer</span></a>. The target for the
FW update can be either ELDR (extended loader) which has FW ID equal to 1 or
the main FW which has FW ID equal to 2. The ELDR is not supported
on all HW platforms, see <a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/api-commands/leaps-dev-info-get#leaps-dev-info-get"><span class="std std-ref">leaps_dev_info_get</span></a>. command on how to read the device information.
Rebooting into the bootloader or into the ELDR is required during the FW update process since the firmware cannot update itself.</p>
<p>The update is not started if refused. The reasons for refused firmware update are:</p>
<ul class="simple">
<li><p>Not permitted - The FW ID given as the FW update target requires either enter the bootloader mode (the bootloader mode is entered always for a short time after reset, the time for which the module stays in the bootloader mode can be configured by <a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/api-commands/leaps-boot-cfg-set#leaps-boot-cfg-set"><span class="std std-ref">leaps_boot_cfg_set</span></a>).</p></li>
<li><p>Again - reset is required to  switch to ELDR/FW and the update start request needs to be sent again after device reset. The device can be reset by <a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/api-commands/leaps-reset#leaps-reset"><span class="std std-ref">leaps_reset</span></a>.</p></li>
<li><p>Internal error</p></li>
<li><p>Invalid argument - Invalid hardware version or invalid FW ID.</p></li>
</ul>
<p>Ongoing firmware update is restarted by this command.</p>
<hr class="docutils">
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
Input</div>
<ul class="simple">
<li><p class="sd-card-text">hw_version: 32-bit integer (<em>Hardware version</em>)</p></li>
<li><p class="sd-card-text">fw_id: ‘1’ | ‘2’ (<em>1 for ELDR - Extended Loader or 2 for main firmware</em>)</p></li>
<li><p class="sd-card-text">fw_checksum: 32-bit integer (<em>crc32 of the firmware to be uploaded</em>)</p></li>
<li><p class="sd-card-text">fw_size: 32-bit integer (<em>size of the firmware</em>)</p></li>
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
<li><p class="sd-card-text">size: 32-bit integer (<em>Size of data that need to be written by leaps_fw_update_xfer</em>)</p></li>
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
<col style="width: 12%">
<col style="width: 18%">
<col style="width: 15%">
<col style="width: 15%">
<col style="width: 15%">
<col style="width: 13%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="7"><p>TLV
request</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="2"><p>Type</p></td>
<td rowspan="2"><p>Length</p></td>
<td colspan="5"><p>Value</p></td>
</tr>
<tr class="row-odd"><td><p>Hardware
version</p></td>
<td><p>Firmware
ID</p></td>
<td><p>reserved</p></td>
<td><p>firmware
checksum</p></td>
<td><p>size</p></td>
</tr>
<tr class="row-even"><td><p>0x3E</p></td>
<td><p>0x10</p></td>
<td><p>0x2A 0x00
0xCA 0xDE</p></td>
<td><p>0x02</p></td>
<td><p>0x00
0x00
0x00</p></td>
<td><p>0xea
0xF5
0x67
0x6D</p></td>
<td><p>0xC4
0x26
0x00
0x00</p></td>
</tr>
</tbody>
</table>
<p>Type 0x3E (62 dec) means command leaps_fw_update_start</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 12%">
<col style="width: 10%">
<col style="width: 9%">
<col style="width: 7%">
<col style="width: 10%">
<col style="width: 26%">
<col style="width: 26%">
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
<tr class="row-odd"><td><p>Offset</p></td>
<td><p>Size</p></td>
</tr>
<tr class="row-even"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
<td><p>0x7e</p></td>
<td><p>0x08</p></td>
<td><p>0x00 0x00 0x00 0x00</p></td>
<td><p>0x00 0x10 0x00 0x00</p></td>
</tr>
</tbody>
</table>
<p>Type 0x40 means status code</p>
<p>Type 0x7E (126) means firmware data request</p>
</div>


           </div>
