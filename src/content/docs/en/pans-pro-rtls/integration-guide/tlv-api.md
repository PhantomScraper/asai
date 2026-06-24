---
title: "TLV API"
lang: en
slug: "pans-pro-rtls/integration-guide/tlv-api"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/pans-pro-rtls/integration-guide/tlv-api/"
order: 122
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="tlv-api">
<h1>TLV API</h1>
<p>The TLV (Type-Length-Value) format is used in the DWM module API.
Data in TLV format always begins with the type byte, followed by the length byte, and then followed by a variable number of value bytes (ranging from 0 to 253), as specified by the length byte.
Table 1 shows an example of TLV format data, where the type byte is 0x28, the length byte is 0x02, and, as declared by the length byte, the value field consists of two bytes: 0x0D and 0x01.</p>
<p>In the DWM1001 firmware, both the SPI and UART APIs use the TLV format for data transmission.
Users should refer to the TLV type list to understand the meaning of type bytes.
For each specific command or response, the value field has a different length to provide the corresponding information.</p>
<p><strong>TLV format data example</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 63%">
<col style="width: 11%">
<col style="width: 13%">
<col style="width: 13%">
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
<tr class="row-odd"><td><p><strong>pin index</strong></p></td>
<td><p><strong>pin value</strong></p></td>
</tr>
<tr class="row-even"><td><p>0x28</p></td>
<td><p>0x02</p></td>
<td><p>0x0D</p></td>
<td><p>0x01</p></td>
</tr>
</tbody>
</table>
<p>Detail information of each API, please read the following pages:</p>
<div class="toctree-wrapper compound">
<ul>
<li class="toctree-l1"><a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/generic-api-information">Generic API Information</a></li>
<li class="toctree-l1"><a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/api-command-list">API Command List</a></li>
</ul>
</div>
</div>


           </div>
