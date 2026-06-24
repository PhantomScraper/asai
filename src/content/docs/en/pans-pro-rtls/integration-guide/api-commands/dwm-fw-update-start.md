---
title: "dwm_fw_update_start"
lang: en
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-fw-update-start"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/pans-pro-rtls/integration-guide/api-commands/dwm-fw-update-start/"
order: 184
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-fw-update-start">
<span id="id1"></span><h1>dwm_fw_update_start</h1>
<p>This call is available only on the ethernet gateway. It starts the firmware update.
It should be called at the beginning before any call to <a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/api-commands/dwm-fw-update-xfer#dwm-fw-update-xfer"><span class="std std-ref">dwm_fw_update_xfer</span></a>.
If accepted, the request returns command status: “ok” followed by the first data request.
The data request should always be handled by the <a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/api-commands/dwm-fw-update-xfer#dwm-fw-update-xfer"><span class="std std-ref">dwm_fw_update_xfer</span></a>.
The update is not started if refused.</p>
<p>The reasons for refused firmware update are:</p>
<ul class="simple">
<li><p>Not permitted - invalid hardware version is given, or the module is not in the bootloader mode (the bootloader mode is always entered for a short period after the reset; the time for which the module stays in the bootloader mode can be configured by <a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/api-commands/dwm-boot-cfg-set#dwm-boot-cfg-set"><span class="std std-ref">dwm_boot_cfg_set</span></a>)</p></li>
<li><p>Internal error</p></li>
<li><p>Busy - firmware update is already in progress.</p></li>
</ul>
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
Input</div>
<ul class="simple">
<li><p class="sd-card-text">hw_version: 32-bit integer (<em>Hardware version</em>)</p></li>
<li><p class="sd-card-text">fw_version: 32-bit integer (<em>Version of the firmware</em>)</p></li>
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
<li><p class="sd-card-text"><a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">Status code</span></a></p></li>
<li><p class="sd-card-text">offset: 32-bit integer (Offset of data that need to be written next by <a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/api-commands/dwm-fw-update-xfer#dwm-fw-update-xfer"><span class="std std-ref">dwm_fw_update_xfer</span></a>)</p></li>
<li><p class="sd-card-text">size: 32-bit integer (Size of data that need to be written by <a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/api-commands/dwm-fw-update-xfer#dwm-fw-update-xfer"><span class="std std-ref">dwm_fw_update_xfer</span></a>)</p></li>
</ul>
</div>
</div>
</div>
</div>
</div>
<p><strong>SPI/UART example</strong></p>
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
<tr class="row-odd"><th class="head" colspan="6"><p>TLV Request</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Type</p></td>
<td><p>Length</p></td>
<td><p>Hardware
Version</p></td>
<td><p>Firmware
Version</p></td>
<td><p>Firmware
Checksum</p></td>
<td><p>Size</p></td>
</tr>
<tr class="row-odd"><td><p>0x3E</p></td>
<td><p>0x10</p></td>
<td><p>0x2A
0x00
0xCA
0xDE</p></td>
<td><p>0x01 0x00
0x01 0x01</p></td>
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
<p>Type 0x3E (62 dec) means command <a class="reference internal" href="#dwm-fw-update-start"><span class="std std-ref">dwm_fw_update_start</span></a></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 14%">
<col style="width: 14%">
<col style="width: 14%">
<col style="width: 14%">
<col style="width: 14%">
<col style="width: 14%">
<col style="width: 14%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="7"><p>TLV Response</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Type</p></td>
<td><p>Length</p></td>
<td><p>Value</p></td>
<td><p>Type</p></td>
<td><p>Length</p></td>
<td colspan="2"><p>Value</p></td>
</tr>
<tr class="row-odd"><td rowspan="2"><p>0x40</p></td>
<td rowspan="2"><p>0x01</p></td>
<td rowspan="2"><p>0x00</p></td>
<td rowspan="2"><p>0x7E</p></td>
<td rowspan="2"><p>0x08</p></td>
<td><p>Offset</p></td>
<td><p>Size</p></td>
</tr>
<tr class="row-even"><td><p>0x00
0x00
0x00
0x00</p></td>
<td><p>0x00
0x10
0x00
0x00</p></td>
</tr>
</tbody>
</table>
<div class="line-block">
<div class="line">Type 0x40 means <a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">Status code</span></a></div>
<div class="line">Type 0x7E (126) means data request</div>
</div>
</div>


           </div>
