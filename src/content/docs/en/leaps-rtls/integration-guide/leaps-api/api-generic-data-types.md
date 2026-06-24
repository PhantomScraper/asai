---
title: "API Generic Data Types"
lang: en
slug: "leaps-rtls/integration-guide/leaps-api/api-generic-data-types"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/leaps-rtls/integration-guide/leaps-api/api-generic-data-types/"
order: 145
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <section id="api-generic-data-types">
<h1>API Generic Data Types</h1>
<section id="id">
<h2>ID</h2>
<p>Node IDentifier. This is a unique 64-bit number. It is derived from a
fixed prefix 0xDECA, MCU unique Chip ID and DW1000/DW3000 unique Part ID in
this format: 0xDECA + 28 bits MCU unique Chip ID + 20 bits DW1000 unique
Part ID.</p>
<div class="sd-card sd-sphinx-override sd-mb-3 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<p class="sd-card-text"><strong>id</strong> = 64-bit integer</p>
</div>
</div>
<hr class="docutils">
</section>
<section id="status-code">
<span id="statuscode"></span><h2>Status Code</h2>
<p>Status code returned by every command.</p>
<div class="sd-card sd-sphinx-override sd-mb-3 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<ul class="simple">
<li><p class="sd-card-text">‘0’ (<em>ok</em>)</p></li>
<li><p class="sd-card-text">‘1’ (<em>unknown command or broken tlv frame</em>)</p></li>
<li><p class="sd-card-text">‘2’ (<em>internal error</em>)</p></li>
<li><p class="sd-card-text">‘3’ (<em>invalid parameter</em>)</p></li>
<li><p class="sd-card-text">‘4’ (<em>busy</em>)</p></li>
<li><p class="sd-card-text">‘5’ (<em>operation not permitted</em>)</p></li>
<li><p class="sd-card-text">‘6’ (<em>checksum error</em>)</p></li>
<li><p class="sd-card-text">‘7’ (<em>IO error</em>)</p></li>
<li><p class="sd-card-text">‘8’ (<em>not supported</em>)</p></li>
<li><p class="sd-card-text">‘9’ (<em>reset required and command needs to be sent again</em>)</p></li>
</ul>
</div>
</div>
<hr class="docutils">
</section>
<section id="position">
<span id="id1"></span><h2>Position</h2>
<p>Position of the node (anchor or tag).</p>
<div class="sd-card sd-sphinx-override sd-mb-3 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<ul class="simple">
<li><p class="sd-card-text"><strong>In CARTESIAN coordinate, position = x, y, z, pqf</strong> (<em>position coordinates</em>)</p>
<ul>
<li><p class="sd-card-text"><strong>x</strong> = 32-bit integer (<em>in millimeters</em>)</p></li>
<li><p class="sd-card-text"><strong>y</strong> = 32-bit integer (<em>in millimeters</em>)</p></li>
<li><p class="sd-card-text"><strong>z</strong> = 32-bit integer (<em>in millimeters</em>)</p></li>
<li><p class="sd-card-text"><strong>pqf</strong> = 8-bit integer (<em>position quality factor in percents</em>)</p></li>
</ul>
</li>
<li><p class="sd-card-text"><strong>In WGS84 coordinate, position = lat, lon, 0, pqf</strong> (<em>position coordinates</em>)</p>
<ul>
<li><p class="sd-card-text"><strong>lat</strong> = 32-bit integer (WGS84 latitude x10^7)</p></li>
<li><p class="sd-card-text"><strong>lon</strong> = 32-bit integer (WGS84 latitude x10^7)</p></li>
<li><p class="sd-card-text"><strong>0</strong></p></li>
<li><p class="sd-card-text"><strong>pqf</strong> = 8-bit integer (<em>position quality factor in percents</em>)</p></li>
</ul>
</li>
</ul>
</div>
</div>
<hr class="docutils">
</section>
<section id="gpio-idx">
<span id="gpioidx"></span><h2>gpio_idx</h2>
<p>Index of GPIO pins available to the user by input PX.Y, where:</p>
<ul class="simple">
<li><p>X: port number</p></li>
<li><p>Y: pin index</p></li>
</ul>
<p>Please refer to the number/index for the specific device in the list below.</p>
<ul class="simple">
<li><p>DWM1001: P0.08, P0.12, P0.13, P0.15, P0.23, P0.27</p></li>
<li><p>DWM3001: P0.06, P0.12, P0.13, P0.17, P0.20, P0.21, P1.00, P1.01, P1.05, P1.09</p></li>
<li><p>LC13/LC14 (2AB): P0.11, P0.12, P0.13, P0.14, P1.7, P1.14</p></li>
</ul>
</section>
<hr class="docutils">
<section id="fw-version">
<h2>fw_version</h2>
<div class="sd-card sd-sphinx-override sd-mb-3 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<ul class="simple">
<li><p class="sd-card-text"><strong>fw_version</strong> = <strong>maj</strong>, <strong>min, patch, ver</strong> (<em>firmware version</em>)</p>
<ul>
<li><p class="sd-card-text"><strong>maj</strong> = 8-bit number (<em>MAJOR</em>)</p></li>
<li><p class="sd-card-text"><strong>min</strong> = 8-bit number (<em>MINOR</em>)</p></li>
<li><p class="sd-card-text"><strong>patch</strong> = 8-bit number (<em>PATCH</em>)</p></li>
<li><p class="sd-card-text"><strong>ver</strong> = res, var</p></li>
<li><p class="sd-card-text"><strong>res</strong> = 4-bit number (<em>RESERVED</em>)</p></li>
<li><p class="sd-card-text"><strong>var</strong> = 4-bit number (<em>VARIANT</em>)</p></li>
</ul>
</li>
</ul>
</div>
</div>
</section>
</section>


           </div>
