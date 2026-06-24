---
title: "LC8A Specification"
lang: en
slug: "pans-pro-rtls/specification/lc8a-specification"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/pans-pro-rtls/specification/lc8a-specification/"
order: 28
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="lc8a-specification">
<span id="id1"></span><h1>LC8A Specification</h1>
<p>This document provides technical details of the LC8A device. The LC8A device is a versatile hardware solution designed to function as either a Tag Node (TN)  or an Anchor Node (AN) within a Real-Time Location System (RTLS). Its flexibility and adaptability make it  ideal  for various tracking and monitoring applications.</p>
<blockquote>
<div></div></blockquote>
<div class="sd-card sd-sphinx-override sd-mb-3 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<p class="sd-card-text">See also the <a class="reference external" href="/_static/_pdfversion/lc8a-datasheet.pdf">Technical Specification in PDF version</a></p>
</div>
</div>
<a class="reference internal image-reference" href="../../../_images/lc8a_front_view.png"><img alt="The Front view of the device" class="align-center" src="/docs-assets/_images/lc8a_front_view.png" style="width: 151.79999999999998px; height: 235.2px;"></a>
<div style="text-align: center; font-weight: bold;">
The Front view of the device.
</div><hr class="docutils">
<div class="section" id="key-features">
<h2>Key Features</h2>
<ul class="simple">
<li><p>Based on Qorvo’s <a class="reference external" href="https://www.qorvo.com/products/p/DWM1001C">DWM1001C</a>  Ultra Wideband (UWB) module (<a class="reference external" href="https://www.qorvo.com/products/p/DW1000">DW1000</a> Ultra Wideband (UWB) transceiver IC and Nordic Semiconductor nRF52832):</p>
<ul>
<li><p>Ranging accuracy to within +-20cm.</p></li>
<li><p>UWB Channel 5 printed PCB antenna (6.5 GHz)</p></li>
<li><p>6.8 Mbps data rate IEEE 802.15.4-2011 UWB compliant</p></li>
<li><p>Integrates UWB and Bluetooth® antenna and all RF circuitry.</p></li>
<li><p>Integrated Motion sensor: 3-axis accelerometer.</p></li>
<li><p>Current consumption optimized for low-power sleep mode: &lt;15μA</p></li>
</ul>
</li>
<li><p>Three functional buttons.</p></li>
<li><p>One RGB main LED and two lateral green LEDs</p></li>
<li><p>Haptic feedback</p></li>
<li><p>Buzzer for alarm functions</p></li>
<li><p>Free software configuration and visualization tools (software support for iOS, Android, Windows, macOS, and Linux platforms).</p></li>
<li><p>An open <a class="reference external" href="/docs/en/index">online documentation</a> and <a class="reference external" href="https://forum.leapslabs.com">community forum</a>.</p></li>
</ul>
</div>
<hr class="docutils">
<div class="section" id="software-compatibility">
<h2>Software Compatibility</h2>
<p>It is compatible with <a class="reference internal" href="/docs/en/pans-pro-rtls#pans-pro-rtls"><span class="std std-ref">PANS PRO RTLS</span></a> and <a class="reference internal" href="/docs/en/leaps-rtls#leaps-rtls"><span class="std std-ref">LEAPS RTLS</span></a>.
The default firmware is <a class="reference internal" href="/docs/en/pans-pro-rtls#pans-pro-rtls"><span class="std std-ref">PANS PRO RTLS</span></a> supplied by the production.</p>
</div>
<div class="section" id="electrical-parameters">
<h2>Electrical Parameters</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 46%">
<col style="width: 54%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Parameter</p></th>
<th class="head"><p>Value</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>USB (power and data)</p></td>
<td><p>5V @ 500mA max</p></td>
</tr>
<tr class="row-odd"><td><p>Battery</p></td>
<td><p>3.7V @ 1Ah</p></td>
</tr>
<tr class="row-even"><td><p>Operating temperature
(without battery)</p></td>
<td><p>-40°C - +85°C</p></td>
</tr>
<tr class="row-odd"><td><p>Operating temperature
(with battery)</p></td>
<td><p>-20°C - +45°C</p></td>
</tr>
<tr class="row-even"><td><p>Operating temperature
(charging)</p></td>
<td><p>0°C ˜ +40°C</p></td>
</tr>
<tr class="row-odd"><td><p>UWB supported channels</p></td>
<td><p>UWB-CH5 - 6240–6739.2 MHz</p></td>
</tr>
<tr class="row-even"><td><p>UWB transmit powers</p></td>
<td><p>ETSI, FCC: -41.3 dBm/MHz max</p></td>
</tr>
</tbody>
</table>
</div>
<div class="section" id="mechanical-parameters">
<h2>Mechanical Parameters</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 46%">
<col style="width: 54%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Parameter</p></th>
<th class="head"><p>Value</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Size</p></td>
<td><p>90 x 70 x 10 mm</p></td>
</tr>
<tr class="row-odd"><td><p>Weight</p></td>
<td><p>80g</p></td>
</tr>
<tr class="row-even"><td><p>Color</p></td>
<td><p>White</p></td>
</tr>
<tr class="row-odd"><td><p>Mounting</p></td>
<td><p>Badge clip (optional)</p></td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="device-overview">
<h2>Device Overview</h2>
<a class="reference internal image-reference" href="../../../_images/lc8a_hardware_interfaces.png"><img alt="The Front view of the device" class="align-center" src="/docs-assets/_images/lc8a_hardware_interfaces.png" style="width: 346.40000000000003px; height: 293.6px;"></a>
<div style="text-align: center; font-weight: bold;">
The Hardware Interfaces of the device.
</div></div>
<hr class="docutils">
<div class="section" id="safety-instructions">
<h2>Safety Instructions</h2>
<ul class="simple">
<li><p>Do not expose devices to water or moisture while in operation.</p></li>
<li><p>Do not expose devices to heat from any source. The product is designed for reliable operation at industrial temperature`1`. If the product is equipped with a battery, it can be at normal operating temperature`2`. The temperature`3`, while the battery is charging, is internally protected (if the temperature is outside of the range, the battery charging will not start or will be postponed).</p></li>
</ul>
</div>
<div class="section" id="warnings">
<h2>Warnings</h2>
<ul class="simple">
<li><p>This product shall only be connected to the USB power and a minimum current supply of 0.5 A.</p></li>
<li><p>Any external power supply used with this product shall comply with relevant regulations and standards applicable in the country of intended use.</p></li>
<li><p>This product should be operated in a ventilated environment with a non-condensing environment and should not be covered when being operated.</p></li>
<li><p>There are no user-serviceable parts inside the product, and opening the unit will likely  damage the product and  invalidate the warranty.</p></li>
<li><p>The cables and connectors of all peripherals used with this product must have adequate insulation to  meet  relevant safety requirements.</p></li>
</ul>
</div>
<div class="section" id="order-information">
<h2>Order Information</h2>
<ul class="simple">
<li><p>Part number: PP-LC8A</p></li>
<li><p>HS Code: 8517.69.9000</p></li>
<li><p>Packaging: 10pcs in paper box, 17 cm x 11 cm x 12 cm 0.8kg</p></li>
</ul>
</div>
</div>


           </div>
