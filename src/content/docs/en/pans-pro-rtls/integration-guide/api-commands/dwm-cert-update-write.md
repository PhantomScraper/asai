---
title: "dwm_cert_update_write"
lang: en
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-cert-update-write"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/pans-pro-rtls/integration-guide/api-commands/dwm-cert-update-write/"
order: 173
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-cert-update-write">
<span id="id1"></span><h1>dwm_cert_update_write</h1>
<p>This call is available only on the ethernet gateway. It should be called repeatedly after <a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/api-commands/dwm-cert-update-start#dwm-cert-update-start"><span class="std std-ref">dwm_cert_update_start</span></a> to transfer the certificate until all the data chunks are transferred. Returns status “ok” followed by the data request until all the data is transferred, in which case status “ok” is returned with no data request following or until the update ends with some error. The error is indicated by a status code other than “ok”. The reasons for the failed update are:</p>
<ul class="simple">
<li><p>internal error</p></li>
<li><p>invalid parameter - e.g. data chunk with zero length, or data chunk has been skipped</p></li>
<li><p>not permitted - not started yet, or the whole update process has failed</p></li>
</ul>
<p>The size and the offset of the data already written to the flash by the update procedure so far are returned as a response on each call to <a class="reference internal" href="#dwm-cert-update-write"><span class="std std-ref">dwm_cert_update_write</span></a> until the update is completed.</p>
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
Input</div>
<ul class="simple">
<li><p class="sd-card-text">offset: 32-bit unsigned integer (<em>Certificate data offset.</em>)</p></li>
<li><p class="sd-card-text">data: from 4 to 32 bytes (<em>Certificate data chunk currently being uploaded, up to 32 bytes.</em>)</p></li>
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
<li><p class="sd-card-text">offset: 32-bit unsigned integer (<em>Expected offset of next data chunk.</em>)</p></li>
<li><p class="sd-card-text">size: 32-bit unsigned integer (<em>Expected size of next data chunk.</em>)</p></li>
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
<tr class="row-odd"><td rowspan="2"><p>0x3B</p></td>
<td rowspan="2"><p>0x24</p></td>
<td><p>offset</p></td>
<td><p>data chunk</p></td>
</tr>
<tr class="row-even"><td><p>0x00 0x00
0x00 0x00</p></td>
<td><p>0xA5 0xA5 0xA5
0xA5 0xA5 0xA5
0xA5 0xA5 ….
0xA5 0xA5 0xA5
0xA5</p></td>
</tr>
</tbody>
</table>
<p>Type 0x3B (59 dec) means command <a class="reference internal" href="#dwm-cert-update-write"><span class="std std-ref">dwm_cert_update_write</span></a></p>
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
<td><p>type</p></td>
<td><p>Length</p></td>
<td colspan="2"><p>Value</p></td>
</tr>
<tr class="row-odd"><td rowspan="2"><p>0x40</p></td>
<td rowspan="2"><p>0x01</p></td>
<td rowspan="2"><p>0x00</p></td>
<td rowspan="2"><p>0x7E</p></td>
<td rowspan="2"><p>0x08</p></td>
<td><p>offset</p></td>
<td><p>size</p></td>
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
<div class="line">Type 0x40 means status code</div>
<div class="line">Type 0x7E (126 dec) means data request</div>
</div>
</div>


           </div>
