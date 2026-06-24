---
title: "leaps_hw_ver_set_once"
lang: en
slug: "leaps-rtls/integration-guide/api-commands/leaps-hw-ver-set-once"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/leaps-rtls/integration-guide/api-commands/leaps-hw-ver-set-once/"
order: 261
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-hw-ver-set-once">
<span id="id1"></span><h1>leaps_hw_ver_set_once</h1>
<p>Set the hardware version in the write-once memory. Hardware version
cannot be changed after it is successfully set by this call! The size of
the HW version buffer is 2, which means that the version number can be
written at most 2 times after the buffer is full. The 2nd HW version has
higher priority than the 1st HW version. The attempt to write the 2nd HW
version that is equal to the 1st HW version is refused as invalid
parameter.</p>
<hr class="docutils">
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
Input</div>
<ul class="simple">
<li><p class="sd-card-text"><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/leaps-api/api-generic-data-types#statuscode"><span class="std std-ref">Status Code</span></a></p></li>
<li><p class="sd-card-text">hw_version: 32-bits integer</p></li>
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
<li><p class="sd-card-text">(<em>none</em>)</p></li>
</ul>
</div>
</div>
</div>
</div>
</div>
<hr class="docutils">
<p>SPI/UART example</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 31%">
<col style="width: 37%">
<col style="width: 31%">
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
<tr class="row-odd"><td rowspan="2"><p>0x84</p></td>
<td rowspan="2"><p>0x04</p></td>
<td><p>Hardware
version
in little
endian
(e.g.
0x
02100111)</p></td>
</tr>
<tr class="row-even"><td><p>0x11 0x01
0x10 0x02</p></td>
</tr>
</tbody>
</table>
<p>Type 0x84 (132 dec) means command <a class="reference internal" href="#leaps-hw-ver-set-once"><span class="std std-ref">leaps_hw_ver_set_once</span></a></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 30%">
<col style="width: 30%">
<col style="width: 40%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV Response</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Type</p></td>
<td><p>Length</p></td>
<td><p>Value (see error
codes)</p></td>
</tr>
<tr class="row-odd"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>Type 0x40 means err_code of the previous command</p>
</div>


           </div>
