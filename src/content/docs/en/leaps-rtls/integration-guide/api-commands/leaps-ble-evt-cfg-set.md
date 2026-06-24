---
title: "leaps_ble_evt_cfg_set"
lang: en
slug: "leaps-rtls/integration-guide/api-commands/leaps-ble-evt-cfg-set"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/leaps-rtls/integration-guide/api-commands/leaps-ble-evt-cfg-set/"
order: 224
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-ble-evt-cfg-set">
<span id="id1"></span><h1>leaps_ble_evt_cfg_set</h1>
<p>Enables/disables events on the BLE interface. This call does a write to
internal non-volatile memory in case of new value being set, hence
should not be used frequently and can take in worst case hundreds of
milliseconds!</p>
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
<tr class="row-even"><td rowspan="2"><p>Type</p></td>
<td rowspan="2"><p>Length</p></td>
<td><p>Value</p></td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line">(bits 10-15) reserved</div>
<div class="line">(bit 9) location ready event includes positions of ranging nodes</div>
<div class="line">(bit 8) location ready event includes my position</div>
<div class="line">(bits 3-7) reserved</div>
<div class="line">(bit 2) BLE user data ready event enable</div>
<div class="line">(bit 1) proxy position ready event enabled</div>
<div class="line">(bit 0) location ready event enabled</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>0x21</p></td>
<td><p>0x02</p></td>
<td><p>0x02 0x01</p></td>
</tr>
</tbody>
</table>
<p>Type 0x21 (33) means command leaps_ble_evt_cfg_set</p>
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
<p>Type 0x40 means status code</p>
</div>


           </div>
