---
title: "leaps_pos_get"
lang: en
slug: "leaps-rtls/integration-guide/api-commands/leaps-pos-get"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/leaps-rtls/integration-guide/api-commands/leaps-pos-get/"
order: 228
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <section id="leaps-pos-get">
<span id="id1"></span><h1>leaps_pos_get</h1>
<p>Obtain the actual position of the node.</p>
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
Input</div>
<ul class="simple">
<li><p class="sd-card-text">(none)</p></li>
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
<li><p class="sd-card-text"><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/leaps-api/api-generic-data-types#position"><span class="std std-ref">Position</span></a></p></li>
</ul>
</div>
</div>
</div>
</div>
</div>
<p><strong>Example</strong></p>
<table class="custom-table docutils align-default">
<thead>
<tr class="row-odd"><th class="head"><p>TLV Request</p></th>
<th class="head"></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Type</p></td>
<td><p>Length</p></td>
</tr>
<tr class="row-odd"><td><p>0x02</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>Type 0x02 means command leaps_pos_get</p>
<table class="custom-table docutils align-default">
<thead>
<tr class="row-odd"><th class="head" colspan="9"><p>TLV response</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="2"><p>Type</p></td>
<td rowspan="2"><p>Length</p></td>
<td rowspan="2"><p>Value</p></td>
<td rowspan="2"><p>Type</p></td>
<td rowspan="2"><p>Length</p></td>
<td colspan="4"><p>Value</p></td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line">int32_t -</div>
<div class="line">in little</div>
<div class="line">endian is</div>
<div class="line">x coordinate</div>
<div class="line">in millimeters</div>
<div class="line">/ WGS84</div>
<div class="line">latitude x10^7</div>
<div class="line"><br></div>
</div>
</td>
<td><div class="line-block">
<div class="line">int32_t -</div>
<div class="line">in little</div>
<div class="line">endian is</div>
<div class="line">y coordinate</div>
<div class="line">in millimeters</div>
<div class="line">/ WGS84</div>
<div class="line">longitude x10^7</div>
<div class="line"><br></div>
</div>
</td>
<td><div class="line-block">
<div class="line">int32_t -</div>
<div class="line">in little</div>
<div class="line">endian is</div>
<div class="line">z coordinate</div>
<div class="line">in millimeters</div>
<div class="line">in millimeters</div>
<div class="line">/ 0 in WGS84</div>
<div class="line">coordinate</div>
</div>
</td>
<td><div class="line-block">
<div class="line">uint8_t -</div>
<div class="line">position</div>
<div class="line">quality</div>
<div class="line">factor in</div>
<div class="line">percents (0-100)</div>
<div class="line"><br></div>
<div class="line"><br></div>
<div class="line"><br></div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
<td><p>0x41</p></td>
<td><p>0x0D</p></td>
<td colspan="4"><p>0x4b
0x0a
0x00
0x00
0x1f
0x04
0x00
0x00
0x9c
0x0e
0x00
0x00
0x64</p></td>
</tr>
</tbody>
</table>
<p>Type 0x40 means status code</p>
<p>Type 0x41 means position (x,y,z,pqf)</p>
</section>


           </div>
