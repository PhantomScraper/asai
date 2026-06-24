---
title: "dwm_cert_update_start"
lang: en
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-cert-update-start"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/pans-pro-rtls/integration-guide/api-commands/dwm-cert-update-start/"
order: 172
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-cert-update-start">
<span id="id1"></span><h1>dwm_cert_update_start</h1>
<p>This call is available only on the ethernet gateway. It starts the certificate update process and should be called at the
beginning before any call to <a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/api-commands/dwm-cert-update-write#dwm-cert-update-write"><span class="std std-ref">dwm_cert_update_write</span></a>. The request returns command status = “ok” if accepted followed
by the first data request. User should respond to the data request with the <a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/api-commands/dwm-cert-update-write#dwm-cert-update-write"><span class="std std-ref">dwm_cert_update_write</span></a>. The update
is not started if refused. Reasons for refused certificate update are:</p>
<ul class="simple">
<li><p>not permitted - invalid size of the certificate to be uploaded</p></li>
<li><p>internal error</p></li>
<li><p>invalid parameter - the ID of the certificate to be uploaded is unknown</p></li>
</ul>
<p>Certificate must be in der format.</p>
<p><strong>C code example</strong></p>
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
Input</div>
<ul class="simple">
<li><p class="sd-card-text">cert_type: 8-bit unsigned integer (<em>Certificate identifier/type, 0 - CA certificate, 1 - my certificate, 2 - my private key.</em>)</p></li>
<li><p class="sd-card-text">size: 32-bit unsigned integer (<em>Total size of the certificate to be uploaded, up to 2048 bytes.</em>)</p></li>
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
<li><p class="sd-card-text"><a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">Status code</span></a></p></li>
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
<tr class="row-odd"><td rowspan="2"><p>0x36</p></td>
<td rowspan="2"><p>0x05</p></td>
<td><p>certificate type
to upload</p></td>
<td><p>size</p></td>
</tr>
<tr class="row-even"><td><p>0x00</p></td>
<td><p>0xC4 0x26 0x00
0x00</p></td>
</tr>
</tbody>
</table>
<p>Type 0x36 (54 dec) means command <a class="reference internal" href="#dwm-cert-update-start"><span class="std std-ref">dwm_cert_update_start</span></a></p>
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
<td><p>0xE4
0x03
0x00
0x00</p></td>
</tr>
</tbody>
</table>
<div class="line-block">
<div class="line">Type 0x40 means status code</div>
<div class="line">Type 0x7E (126) means data request</div>
</div>
</div>


           </div>
