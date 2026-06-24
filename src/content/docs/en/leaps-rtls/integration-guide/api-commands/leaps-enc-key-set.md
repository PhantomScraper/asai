---
title: "leaps_enc_key_set"
lang: en
slug: "leaps-rtls/integration-guide/api-commands/leaps-enc-key-set"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/leaps-rtls/integration-guide/api-commands/leaps-enc-key-set/"
order: 262
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-enc-key-set">
<span id="id1"></span><h1>leaps_enc_key_set</h1>
<p>Sets encryption key. The key is stored in nonvolatile memory. The key
that consists of just zeros is considered as invalid. If the key is set,
the node can enable encryption automatically. Automatic enabling of the
encryption is triggered via UWB network when the node detects encrypted
message and is capable of decrypting messages with the key. BLE option
is disabled when encryption is enabled automatically. The encryption can
be disabled by clearing the key
(<a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/api-commands/leaps-enc-key-clear#leaps-enc-key-clear"><span class="std std-ref">leaps_enc_key_clear</span></a>).</p>
<p>This call writes to internal flash in case of new value being set, hence
should not be used frequently and can take in worst case hundreds of
milliseconds! Requires reset for new configuration to take effect.
`</p>
<hr class="docutils">
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
Input</div>
<ul class="simple">
<li><p class="sd-card-text">16-byte value (<em>the encryption key</em>)</p></li>
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
<p><strong>Example</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV
request</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Type</p></td>
<td><p>Length</p></td>
<td><p>Value</p></td>
</tr>
<tr class="row-odd"><td><p>0x3C</p></td>
<td><p>0x10</p></td>
<td><p>0x00 0x11
0x22 0x33
0x44 0x55
0x66 0x77
0x88 0x99
0xAA 0xBB
0xCC 0xDD
0xEE 0xFF</p></td>
</tr>
</tbody>
</table>
<p>Type 0x3C means command leaps_enc_key_set</p>
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
