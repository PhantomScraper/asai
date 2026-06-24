---
title: "leaps_cfg_anchor_set"
lang: en
slug: "leaps-rtls/integration-guide/api-commands/leaps-cfg-anchor-set"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/leaps-rtls/integration-guide/api-commands/leaps-cfg-anchor-set/"
order: 225
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-cfg-anchor-set">
<span id="id1"></span><h1>leaps_cfg_anchor_set</h1>
<p>Configure node as anchor with given options.
Encryption can’t be enabled if the encryption
key is not set. This call requires reset for a new configuration to take
effect (<a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/api-commands/leaps-reset#leaps-reset"><span class="std std-ref">leaps_reset</span></a>). Enabling encryption on initiator will cause
automatic enabling of encryption of all nodes that have the same
encryption key set (<a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/api-commands/leaps-enc-key-set#leaps-enc-key-set"><span class="std std-ref">leaps_enc_key_set</span></a>). This
allows encryption for the whole network that has the same pan ID
(network ID) and the same encryption key remotely from one place.</p>
<p>This call does a write to internal flash in case of new value being set,
hence should not be used frequently and can take in worst case hundreds
of milliseconds!</p>
<hr class="docutils">
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
Input</div>
<ul class="simple">
<li><p class="sd-card-text">initiator: 1-bit (<em>‘0’ | ‘1’ - Initiator role enable</em>)</p></li>
<li><p class="sd-card-text">gateway: 1-bit (<em>‘0’ | ‘1’ - Gateway role enable</em>)</p></li>
<li><p class="sd-card-text">enc_en: 1-bit (<em>‘0’ | ‘1’ - encryption enable</em>)</p></li>
<li><p class="sd-card-text">led_en: 1-bit (<em>‘0’ | ‘1’ - general purpose LEDs enable</em>)</p></li>
<li><p class="sd-card-text">ble_en: 1-bit (<em>‘0’ | ‘1’ - BLE enable</em>)</p></li>
<li><p class="sd-card-text">uwb_mode: 2-bits (<em>0-off, 1-passive, 2-active</em>)</p></li>
<li><p class="sd-card-text">fw_update_en: 1-bit (<em>‘0’ | ‘1’- Firmware update enable</em>)</p></li>
<li><p class="sd-card-text">profile_id: 3-bits (<em>ID of the profile</em>)</p></li>
<li><p class="sd-card-text">clock_reference: 1-bit (<em>enables clock reference on the node</em>)</p></li>
<li><p class="sd-card-text">uwb_act_ble: 1-bit (<em>enables uwb activation over ble on the node</em>)</p></li>
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
</ul>
</div>
</div>
</div>
</div>
</div>
<hr class="docutils">
<blockquote>
<div><div class="admonition note">
<p class="admonition-title">Note</p>
<p><strong>uwb_bh_routing</strong>: Available only when the firmware is compiled with UWB routing backhaul:</p>
<p>Value : ‘0’ | ‘1’ | ‘2’</p>
<ul class="simple">
<li><p>0- OFF - anchor will not become a routing anchor</p></li>
<li><p>1- ON - anchor will be preferred by the routing algorithm to be chosen as a routing anchor</p></li>
<li><p>2- AUTO - Whether anchor becomes routing or not depends entirely on the routing algorithm</p></li>
</ul>
</div>
</div></blockquote>
<hr class="docutils">
<p><strong>Example</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 13%">
<col style="width: 8%">
<col style="width: 23%">
<col style="width: 28%">
<col style="width: 29%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="5"><p>TLV response</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="2"><p>Type</p></td>
<td rowspan="2"><p>Length</p></td>
<td colspan="3"><p>Value</p></td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line">(bit 7) initiator</div>
<div class="line">(bit 6) gateway</div>
<div class="line">(bit 5) enc_en</div>
<div class="line">(bit 4) led_en</div>
<div class="line">(bit 3) ble_en</div>
<div class="line">(bit 2) fw_update_en</div>
<div class="line">(bits 0-1) uwb_mode</div>
</div>
</td>
<td><div class="line-block">
<div class="line">(bits 2-7) reserved</div>
<div class="line">(bits 0-1) uwb_bh_routing:</div>
<div class="line">0 - OFF</div>
<div class="line">1 - ON</div>
<div class="line">2 - AUTO</div>
</div>
</td>
<td><div class="line-block">
<div class="line">(bits 0-2) profile id</div>
<div class="line">(bit 3) clock reference</div>
<div class="line">(bit 4) uwb activation ble</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>0x07</p></td>
<td><p>0x03</p></td>
<td><p>0x9C</p></td>
<td><p>0x02</p></td>
<td><p>0x02</p></td>
</tr>
</tbody>
</table>
<p>Type 0x07 means command leaps_cfg_anchor_set</p>
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
