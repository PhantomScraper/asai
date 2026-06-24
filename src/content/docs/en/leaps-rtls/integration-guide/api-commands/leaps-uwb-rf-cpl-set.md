---
title: "leaps_uwb_rf_cpl_set"
lang: en
slug: "leaps-rtls/integration-guide/api-commands/leaps-uwb-rf-cpl-set"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/leaps-rtls/integration-guide/api-commands/leaps-uwb-rf-cpl-set/"
order: 273
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-uwb-rf-cpl-set">
<span id="id1"></span><h1>leaps_uwb_rf_cpl_set</h1>
<p>Sets UWB RF compliance together with the UWB channel. If UWB configuration parameters
like e.g. Tx power etc. are set using the <a class="reference external" href="#leaps_uwb_cfg_set">leaps_uwb_cfg_set</a>,
the UWB RF compliance is automatically set to “custom”. Reset is needed for the configuration to
take effect. The configuration is stored in the non volatile memory. Not all channels
are supported for all boards. ARIB RF compliance is supported only for UWB channel 9.</p>
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
Input</div>
<ul class="simple">
<li><p class="sd-card-text">uwb_channel: ‘2’ | ‘3’ | ‘5’ | ‘9’ (<em>UWB channel 2,3,5 is supported only for DW1000 boards, UWB channel 5,9 is supported only for DW3000 boards</em>)</p></li>
<li><p class="sd-card-text">rf_compliance: ‘0’ | ‘1’ | ‘2’ (<em>RF compliance option, 0 = FCC/ETSI, 1 = ETSI + 10dB, 2 = ARIB</em>)</p></li>
<li><p class="sd-card-text">pcode: ‘9’ | ‘10’ | ‘11’ | ‘12’ (<em>Tx/Rx Preamble Code, this is optional. If the user does not provide an input, the default value specified below will be used.</em>)</p>
<ul>
<li><p class="sd-card-text">Channel 2: Tx/Rx Preamble Code = 11</p></li>
<li><p class="sd-card-text">Channel 3: Tx/Rx Preamble Code = 12</p></li>
<li><p class="sd-card-text">Channel 5: Tx/Rx Preamble Code = 9</p></li>
<li><p class="sd-card-text">Channel 9: Tx/Rx Preamble Code = 11</p></li>
</ul>
</li>
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
<div class="admonition note">
<p class="admonition-title">Note</p>
<ul class="simple">
<li><p>Channel 2 and channel 3 support ‘0 = FCC/ETSI’ only</p></li>
<li><p>ARIB is supported only for channel 9.</p></li>
</ul>
</div>
<hr class="docutils">
<p><strong>Example</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 15%">
<col style="width: 15%">
<col style="width: 70%">
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
<tr class="row-odd"><td><p>byte 0:</p>
<blockquote>
<div><ul class="simple">
<li><p>Bits [7:4]: rf_compliance</p></li>
<li><p>Bits [3:0]: uwb_channel</p></li>
</ul>
</div></blockquote>
<p>byte 1: pcode</p>
</td>
</tr>
<tr class="row-even"><td><p>0x8A</p></td>
<td><p>0x02</p></td>
<td><p>0x29 0x0B</p></td>
</tr>
</tbody>
</table>
<p>Type 0x8A (138 dec) means command <a class="reference internal" href="#leaps-uwb-rf-cpl-set"><span class="std std-ref">leaps_uwb_rf_cpl_set</span></a></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 34%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV Reponse</p></th>
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
</div>


           </div>
