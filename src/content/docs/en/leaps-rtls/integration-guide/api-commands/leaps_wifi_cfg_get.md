---
title: "leaps_wifi_cfg_get"
lang: en
slug: "leaps-rtls/integration-guide/api-commands/leaps_wifi_cfg_get"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/leaps-rtls/integration-guide/api-commands/leaps_wifi_cfg_get/"
order: 289
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-wifi-cfg-get">
<span id="id1"></span><h1>leaps_wifi_cfg_get</h1>
<p>Gets the current WiFi configuration.</p>
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
<tr class="row-odd"><td><p>0x9D</p></td>
<td><p>0x00</p></td>
<td><p>None</p></td>
</tr>
</tbody>
</table>
<p>Type 0x9D (157) means command leaps_wifi_cfg_get</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 7%">
<col style="width: 6%">
<col style="width: 6%">
<col style="width: 6%">
<col style="width: 6%">
<col style="width: 69%">
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
<tr class="row-odd"><td><p>variable-length payload, same layout as leaps_wifi_cfg_set input.</p></td>
</tr>
<tr class="row-even"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
<td><p>0x7D</p></td>
<td><p>0x1C</p></td>
<td><p>00 00 00 00 09 4D 79 4E 65 74 77 6F 72 6B 0D 4D 79 50 61 73 73 77 6F 72 64 31 32 33</p></td>
</tr>
</tbody>
</table>
<p>Type 0x40 means status code</p>
<p>Type 0x7D (125) means TLV_TYPE_WIFI_CFG</p>
</div>


           </div>
