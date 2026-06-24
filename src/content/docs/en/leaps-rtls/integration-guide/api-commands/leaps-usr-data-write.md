---
title: "leaps_usr_data_write"
lang: en
slug: "leaps-rtls/integration-guide/api-commands/leaps-usr-data-write"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/leaps-rtls/integration-guide/api-commands/leaps-usr-data-write/"
order: 272
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-usr-data-write">
<span id="id1"></span><h1>leaps_usr_data_write</h1>
<p>Write custom user data to non volatile memory or send the data over
UWB or BLE interface.
To receive notifications on new user data or to read user data refer to <a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/api-commands/leaps-usr-data-read#leaps-usr-data-read"><span class="std std-ref">leaps_usr_data_read</span></a>.</p>
<hr class="docutils">
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
Input</div>
<blockquote>
<div><ul>
<li><p class="sd-card-text">data</p></li>
<li><p class="sd-card-text">type: 2 bits (<em>user data type, ‘0’ means write user data to the UWB interface, ‘1’ means write user data to the BLE interface, ‘2’ means write user data to non volatile memory</em>)</p></li>
<li><p class="sd-card-text">flags: overwrite, test</p></li>
<li><p class="sd-card-text">overwrite: 1 bit</p>
<blockquote>
<div><ul class="simple">
<li><p class="sd-card-text">‘0’ means do not overwrite</p></li>
<li><p class="sd-card-text">‘1’ means overwrite data currently being sent</p></li>
</ul>
</div></blockquote>
</li>
<li><p class="sd-card-text">test: 1 bit (Applies only when type=0)</p>
<blockquote>
<div><ul class="simple">
<li><p class="sd-card-text">‘0’ means test data is disabled</p></li>
<li><p class="sd-card-text">‘1’ means device will send test user data (maximum size with first 4 bytes being frame counter). The input data length must be 4 and the input data is parsed as the number of test frames to send.</p></li>
</ul>
</div></blockquote>
</li>
</ul>
</div></blockquote>
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
</ul>
<blockquote>
<div><p class="sd-card-text">‘Busy’ - Previous data are not yet sent, try again or send with overwrite flag set to 1.</p>
<p class="sd-card-text">‘Invalid parameter’ - Size of the user data is too high or the type of the usr data is unknown.</p>
<p class="sd-card-text">‘Internal error’ - Unexpected internal error.</p>
<p class="sd-card-text">BLE</p>
<blockquote>
<div><p class="sd-card-text">‘Not permitted’ - No active connection on the BLE interface.</p>
</div></blockquote>
</div></blockquote>
</div>
</div>
</div>
</div>
</div>
<hr class="docutils">
<p>Example (write UWB user data)</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 9%">
<col style="width: 12%">
<col style="width: 33%">
<col style="width: 46%">
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
<td><div class="line-block">
<div class="line">flags</div>
<div class="line">(bits 0-1) type</div>
<div class="line">(bit 2) overwrite</div>
<div class="line">(bit 3) test</div>
<div class="line">(bits 4-7) reserved</div>
</div>
</td>
<td><p>UWB, BLE user data - max 26
bytes
non-volatile memory user data
- max 250 bytes</p></td>
</tr>
<tr class="row-even"><td><p>0x1A</p></td>
<td><p>0x23</p></td>
<td><p>0x00</p></td>
<td><p>0x01 0x02 0x03 …. 0x23 0x22</p></td>
</tr>
</tbody>
</table>
<p>Type 0x1A (26 dec) means command leaps_usr_data_write</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 34%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV response</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Type</p></td>
<td><p>Length</p></td>
<td><p>Value</p></td>
</tr>
<tr class="row-odd"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>Type 0x40 means <a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/leaps-api/api-generic-data-types#statuscode"><span class="std std-ref">Status Code</span></a> of the command</p>
<p>Example (write test UWB user data)</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 9%">
<col style="width: 12%">
<col style="width: 33%">
<col style="width: 46%">
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
<td><div class="line-block">
<div class="line">flags</div>
<div class="line">(bits 0-1) type</div>
<div class="line">(bit 2) overwrite</div>
<div class="line">(bit 3) test</div>
<div class="line">(bits 4-7) reserved</div>
</div>
</td>
<td><p>Data length must be 4 bytes
Number of frames to be sent
(e.g 10 frames -
0x0A 0x00 0x00 0x00)</p></td>
</tr>
<tr class="row-even"><td><p>0x1A</p></td>
<td><p>0x05</p></td>
<td><p>0x0C</p></td>
<td><p>0x0A 0x00 0x00 0x00</p></td>
</tr>
</tbody>
</table>
<p>Type 0x1A (26 dec) means command leaps_usr_data_write</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 34%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV response</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Type</p></td>
<td><p>Length</p></td>
<td><p>Value</p></td>
</tr>
<tr class="row-odd"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>Type 0x40 means <a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/leaps-api/api-generic-data-types#statuscode"><span class="std std-ref">Status Code</span></a> of the command</p>
<p>Example (overwrite BLE user data)</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 9%">
<col style="width: 12%">
<col style="width: 33%">
<col style="width: 46%">
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
<td><div class="line-block">
<div class="line">flags</div>
<div class="line">(bits 0-1) type</div>
<div class="line">(bit 2) overwrite</div>
<div class="line">(bit 3) test</div>
<div class="line">(bits 4-7) reserved</div>
</div>
</td>
<td><p>BLE user data
max 34 bytes</p></td>
</tr>
<tr class="row-even"><td><p>0x1A</p></td>
<td><p>0x23</p></td>
<td><p>0x05</p></td>
<td><p>0x01 0x02 0x03 …. 0x23 0x22</p></td>
</tr>
</tbody>
</table>
<p>Type 0x1A (26 dec) means command leaps_usr_data_write</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 34%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV response</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Type</p></td>
<td><p>Length</p></td>
<td><p>Value</p></td>
</tr>
<tr class="row-odd"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>Type 0x40 means <a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/leaps-api/api-generic-data-types#statuscode"><span class="std std-ref">Status Code</span></a> of the command</p>
<p>Example (write user data to non volatile memory)</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 9%">
<col style="width: 12%">
<col style="width: 33%">
<col style="width: 46%">
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
<td><div class="line-block">
<div class="line">flags</div>
<div class="line">(bits 0-1) type</div>
<div class="line">(bit 2) overwrite</div>
<div class="line">(bit 3) test</div>
<div class="line">(bits 4-7) reserved</div>
</div>
</td>
<td><p>non-volatile memory user data -
max 250 bytes</p></td>
</tr>
<tr class="row-even"><td><p>0x1A</p></td>
<td><p>0x23</p></td>
<td><p>0x02</p></td>
<td><p>0x01 0x02 0x03 …. 0xFA</p></td>
</tr>
</tbody>
</table>
<p>Type 0x1A (26 dec) means command leaps_usr_data_write</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 34%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV response</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Type</p></td>
<td><p>Length</p></td>
<td><p>Value</p></td>
</tr>
<tr class="row-odd"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>Type 0x40 means <a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/leaps-api/api-generic-data-types#statuscode"><span class="std std-ref">Status Code</span></a> of the command</p>
</div>


           </div>
