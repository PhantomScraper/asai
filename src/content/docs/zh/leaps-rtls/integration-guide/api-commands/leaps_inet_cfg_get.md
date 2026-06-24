---
title: "leaps_inet_cfg_get"
lang: zh
slug: "leaps-rtls/integration-guide/api-commands/leaps_inet_cfg_get"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/leaps-rtls/integration-guide/api-commands/leaps_inet_cfg_get/"
order: 284
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-inet-cfg-get">
<span id="id1"></span><h1>leaps_inet_cfg_get</h1>
<p>Gets the current local network interface configuration.</p>
<hr class="docutils">
<p><strong>Example</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 11%">
<col style="width: 11%">
<col style="width: 78%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV Request</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Type</p></td>
<td><p>Length</p></td>
<td><p>Value</p></td>
</tr>
<tr class="row-odd"><td><p>0x99</p></td>
<td><p>0x00</p></td>
<td><p>None</p></td>
</tr>
</tbody>
</table>
<p>Type 0x99 (153) means command leaps_inet_cfg_get</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 9%">
<col style="width: 7%">
<col style="width: 7%">
<col style="width: 7%">
<col style="width: 7%">
<col style="width: 62%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="6"><p>TLV response</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="2"><p>Type</p></td>
<td rowspan="2"><p>Length</p></td>
<td rowspan="2"><p>Value</p></td>
<td rowspan="2"><p>Type</p></td>
<td rowspan="2"><p>Length</p></td>
<td><p>Value</p></td>
</tr>
<tr class="row-odd"><td><p>16-byte payload, same layout as leaps_inet_cfg_set input.</p></td>
</tr>
<tr class="row-even"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
<td><p>0x7B</p></td>
<td><p>0x10</p></td>
<td><p>01 00 00 00 0A 01 A8 C0 00 FF FF FF 01 01 A8 C0</p></td>
</tr>
</tbody>
</table>
<p>Type 0x40 means status code</p>
<p>Type 0x7B (123) means TLV_TYPE_INET_CFG</p>
</div>


           </div>
