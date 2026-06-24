---
title: "LC4A Specification"
lang: en
slug: "pans-pro-rtls/specification/lc4a-specification"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/pans-pro-rtls/specification/lc4a-specification/"
order: 102
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="lc4a-specification">
<span id="id1"></span><h1>LC4A Specification</h1>
<p>This document provides technical details of the LC4A device. The LC4A device is a versatile hardware solution designed to function as either an Anchor Node (AN) or a Tag Node (TN) within a Real-Time Location System (RTLS). Its flexibility and adaptability make it  ideal  for various tracking and monitoring applications.</p>
<div class="sd-card sd-sphinx-override sd-mb-3 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<p class="sd-card-text">See also the <a class="reference external" href="/_static/_pdfversion/lc4a-datasheet.pdf">Technical Specification in PDF version</a></p>
</div>
</div>
<a class="reference internal image-reference" href="../../../_images/lc4a_front_view.png"><img alt="The Front view of the device" class="align-center" src="/docs-assets/_images/lc4a_front_view.png" style="width: 190.32px; height: 273.39px;"></a>
<div style="text-align: center; font-weight: bold;">
The Front view of the device.
</div><hr class="docutils">
<div class="section" id="key-features">
<h2>Key Features</h2>
<ul class="simple">
<li><p>Based on Qorvo’s <a class="reference external" href="https://www.qorvo.com/products/p/DWM1001C">DWM1001C</a> module that integrates <a class="reference external" href="https://www.qorvo.com/products/p/DW1000">DW1000</a>  Ultra-Wideband (UWB) transceiver IC and Nordic Semiconductor MCU with Bluetooth nRF52832:</p>
<ul>
<li><p>Ranging accuracy to within +-20cm.</p></li>
<li><p>UWB Channel 5 printed PCB antenna (6.5 GHz)</p></li>
<li><p>6.8 Mbps data rate IEEE 802.15.4-2011 UWB compliant</p></li>
<li><p>Integrates UWB and Bluetooth® antenna and all RF circuitry.</p></li>
<li><p>Integrated Motion sensor: 3-axis accelerometer.</p></li>
<li><p>Current consumption optimized for low-power sleep mode: &lt;15μA</p></li>
</ul>
</li>
<li><p>Contains a status LED and the UWB status LED.</p></li>
<li><p>Supplies the power from USB cable (5 VDC), or external source (7~32 VDC).</p></li>
<li><p>A complete software package free of charge that includes software infrastructure, configuration and visualization tools (with support for various platforms from Android, Windows, macOS, and Linux platforms).</p></li>
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
<tr class="row-odd"><th class="head"><p><strong>Parameter</strong></p></th>
<th class="head"><p>Value</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>VDC power supply</p></td>
<td><p>7 ˜ 32 @3W max</p></td>
</tr>
<tr class="row-odd"><td><p>USB (power and data)</p></td>
<td><p>5V @ 500mA max</p></td>
</tr>
<tr class="row-even"><td><p>Operating temperature</p></td>
<td><p>-40°C - +85°C</p></td>
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
<tr class="row-odd"><th class="head"><p><strong>Parameter</strong></p></th>
<th class="head"><p>Value</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Size</p></td>
<td><p>100 x 70 x 25 mm</p></td>
</tr>
<tr class="row-odd"><td><p>Weight</p></td>
<td><p>110g</p></td>
</tr>
<tr class="row-even"><td><p>Color</p></td>
<td><p>White</p></td>
</tr>
<tr class="row-odd"><td><p>Mounting</p></td>
<td><p>Connect any clamp mount with
1/4” screw ball head</p></td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="device-overview">
<h2>Device Overview</h2>
<a class="reference internal image-reference" href="../../../_images/lc4a_hardware_interfaces.png"><img alt="The Front view of the device" class="align-center" src="/docs-assets/_images/lc4a_hardware_interfaces.png" style="width: 652.8000000000001px; height: 373.6px;"></a>
<div style="text-align: center; font-weight: bold;">
The Hardware Interfaces of the device.
</div></div>
<hr class="docutils">
<div class="section" id="safety-instructions">
<h2>Safety Instructions</h2>
<ul class="simple">
<li><p>Do not expose devices to water or moisture while in operation.</p></li>
<li><p>Do not expose devices to heat from any source. The product is designed for reliable operation at industrial temperature.</p></li>
</ul>
</div>
<div class="section" id="warnings">
<h2>Warnings</h2>
<ul class="simple">
<li><p>This product shall only be connected to the external power supply rated at 7˜32DC, USB power, and a minimum current supply of 0.5 A.</p></li>
<li><p>Any external power supply used with this product shall comply with relevant regulations and standards applicable in the country of intended use.</p></li>
<li><p>There are no user-serviceable parts inside the product, and opening the unit will likely damage the product and invalidate the warranty.</p></li>
<li><p>The cables and connectors of all peripherals used with this product must have adequate insulation to meet t relevant safety requirements.</p></li>
</ul>
</div>
<div class="section" id="order-information">
<h2>Order Information</h2>
<ul class="simple">
<li><p>Part numbers: PP-LC4A/LR-LC4A</p></li>
<li><p>HS Code: 8517.69.9000</p></li>
<li><p>Packaging: paper box, 7 cm x 11 cm x 2.5 cm 0.09kg</p></li>
</ul>
</div>
</div>


           </div>
