---
title: "leaps_peer_cfg_get"
lang: ja
slug: "leaps-rtls/integration-guide/api-commands/leaps_peer_cfg_get"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/leaps-rtls/integration-guide/api-commands/leaps_peer_cfg_get/"
order: 286
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-peer-cfg-get">
<span id="id1"></span><h1>leaps_peer_cfg_get</h1>
<p>Gets the current peer server configuration.</p>
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
<tr class="row-odd"><td><p>0x9B</p></td>
<td><p>0x00</p></td>
<td><p>None</p></td>
</tr>
</tbody>
</table>
<p>Type 0x9B (155) means command leaps_peer_cfg_get</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 8%">
<col style="width: 6%">
<col style="width: 6%">
<col style="width: 6%">
<col style="width: 6%">
<col style="width: 67%">
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
<tr class="row-odd"><td><p>same layout as leaps_peer_cfg_set input.</p></td>
</tr>
<tr class="row-even"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
<td><p>0x7C</p></td>
<td><p>0x16</p></td>
<td><p>01 00 00 B3 22 10 6D 71 74 74 2E 65 78 61 6D 70 6C 65 2E 63 6F 6D</p></td>
</tr>
</tbody>
</table>
<p>Type 0x40 means status code</p>
<p>Type 0x7C (124) means TLV_TYPE_PEER_CFG</p>
</div>


           </div>
