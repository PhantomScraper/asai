---
title: "leaps_autopos_start"
lang: en
slug: "leaps-rtls/integration-guide/api-commands/leaps-autopos-start"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/leaps-rtls/integration-guide/api-commands/leaps-autopos-start/"
order: 237
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-autopos-start">
<span id="id1"></span><h1>leaps_autopos_start</h1>
<p>Starts auto-positioning measurement/procedure. The auto-positioning can
be started only on the real initiator, otherwise it if refused and error
code is returned. Successful auto-positioning procedure ends with set of
distances generated as an event. The event “location ready” has to be
enabled prior to the start by <a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/api-commands/leaps-int-cfg-set#leaps-int-cfg-set"><span class="std std-ref">leaps_int_cfg_set</span></a> or <a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/api-commands/leaps-ble-evt-cfg-set#leaps-ble-evt-cfg-set"><span class="std std-ref">leaps_ble_evt_cfg_set</span></a>.</p>
<hr class="docutils">
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
Input</div>
<ul class="simple">
<li><p class="sd-card-text">(<em>none</em>)</p></li>
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
<col style="width: 54%">
<col style="width: 46%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="2"><p>TLV Request</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Type</p></td>
<td><p>Length</p></td>
</tr>
<tr class="row-odd"><td><p>0x09</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>Type 0x09 means command leaps_autopos_start</p>
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
