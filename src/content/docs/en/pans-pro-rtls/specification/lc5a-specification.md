---
title: "LC5A Specification"
lang: en
slug: "pans-pro-rtls/specification/lc5a-specification"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/pans-pro-rtls/specification/lc5a-specification/"
order: 103
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="lc5a-specification">
<span id="id1"></span><h1>LC5A Specification</h1>
<p>This document provides technical details of the LC5A device. The LC5A device is a hardware solution designed to function as a Gateway Node within a Real-Time Location System (RTLS). Its flexibility and adaptability make it  ideal  for various tracking and monitoring applications.</p>
<blockquote>
<div></div></blockquote>
<div class="sd-card sd-sphinx-override sd-mb-3 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<p class="sd-card-text">See also the <a class="reference external" href="/_static/_pdfversion/lc5a-datasheet.pdf">Technical Specification in PDF version</a></p>
</div>
</div>
<a class="reference internal image-reference" href="../../../_images/lc5a_front_view.png"><img alt="The Front view of the device" class="align-center" src="/docs-assets/_images/lc5a_front_view.png" style="width: 231.20000000000002px; height: 230.4px;"></a>
<div style="text-align: center; font-weight: bold;">
The Front view of the device.
</div><hr class="docutils">
<div class="section" id="key-features">
<h2>Key Features</h2>
<p>The host MCU is based on the Microchip’s <a class="reference external" href="https://www.microchip.com/en-us/solutions/displays/embedded-graphics-solutions/mcu-guided-selection-tool-for-graphics/sam-e70-series">MCU SAM E70</a>, a high-performance 32-bit Arm® Cortex®-M7 processor that provides connectivity via 10/100 Ethernet MAC with IEEE 1588.
An integrated ATWINC1500 Wifi module - a low-power consumption 802.11 b/g/n IoT (Internet of Things) module, Specifically optimized for low-power IoT applications, and Supports IEEE 802.11 WEP, WPA and WPA2 security.
The Ultra-Wideband Sub-system runs on Qorvo’s <a class="reference external" href="https://www.qorvo.com/products/p/DWM1001C">DWM1001C</a> module that integrates <a class="reference external" href="https://www.qorvo.com/products/p/DW1000">DW1000</a> Ultra-Wideband (UWB) transceiver IC and Nordic Semiconductor MCU with Bluetooth nRF52832:</p>
<blockquote>
<div><ul class="simple">
<li><p>Ranging accuracy to within +-20cm.</p></li>
<li><p>UWB Channel 5 printed PCB antenna (6.5 GHz)</p></li>
<li><p>6.8 Mbps data rate IEEE 802.15.4-2011 UWB compliant.</p></li>
<li><p>Integrates UWB and Bluetooth® antenna and all RF circuitry.</p></li>
<li><p>Integrated Motion sensor: 3-axis accelerometer.</p></li>
</ul>
</div></blockquote>
<ul class="simple">
<li><p>Supports Ethernet or WIFI connectivity with the <a class="reference internal" href="/docs/en/pans-pro-rtls/infrastructure/leaps-server#pans-pro-server"><span class="std std-ref">LEAPS Server</span></a>.</p></li>
<li><p>Contains a status LED and the UWB status LED.</p></li>
<li><p>Supplies the power from a USB cable (5 VDC) or an external source (7~32 VDC).</p></li>
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
<tr class="row-odd"><th class="head"><p>Parameter</p></th>
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
<tr class="row-even"><td><p>PoE</p></td>
<td><p>802.3AF, 4W max</p></td>
</tr>
<tr class="row-odd"><td><p>Operating temperature</p></td>
<td><p>-40°C - +85°C</p></td>
</tr>
<tr class="row-even"><td><p>UWB supported channels</p></td>
<td><p>UWB-CH5 - 6240–6739.2 MHz</p></td>
</tr>
<tr class="row-odd"><td><p>UWB transmit powers</p></td>
<td><p>ETSI, FCC: -41.3 dBm/MHz max</p></td>
</tr>
<tr class="row-even"><td><p>WIFI Frequency Range</p></td>
<td><p>Single band 2.4GHz b/g/n IoT</p></td>
</tr>
<tr class="row-odd"><td><p>WIFI RX Sensitivity</p></td>
<td><p>-95 dBm</p></td>
</tr>
<tr class="row-even"><td><p>WIFI TX Output Power</p></td>
<td><p>18.5 dBm</p></td>
</tr>
<tr class="row-odd"><td><p>WIFI Encryption</p></td>
<td><p>WEP, WPA-TKIP, WPA2, CCMP-AES</p></td>
</tr>
<tr class="row-even"><td><p>WIFI Country Code</p></td>
<td><p>01 (world safe)</p></td>
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
<td><p>100 x 100 x 35 mm</p></td>
</tr>
<tr class="row-odd"><td><p>Weight</p></td>
<td><p>110g</p></td>
</tr>
<tr class="row-even"><td><p>Color</p></td>
<td><p>White</p></td>
</tr>
<tr class="row-odd"><td><p>Mounting</p></td>
<td><p>Connect any clamp mount with 1/4”
screw ball head</p></td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="device-overview">
<h2>Device Overview</h2>
<a class="reference internal image-reference" href="../../../_images/lc5a_hardware_interfaces.png"><img alt="The Front view of the device" class="align-center" src="/docs-assets/_images/lc5a_hardware_interfaces.png" style="width: 502.40000000000003px; height: 293.6px;"></a>
<div style="text-align: center; font-weight: bold;">
The Hardware Interfaces of the device.
</div></div>
<hr class="docutils">
<div class="section" id="safety-instructions">
<h2>Safety Instructions</h2>
<ul class="simple">
<li><p>Do not expose devices to water or moisture while  in operation.</p></li>
<li><p>Do not expose devices to heat from any source. The product is designed for reliable operation at industrial temperature.</p></li>
</ul>
</div>
<div class="section" id="warnings">
<h2>Warnings</h2>
<ul class="simple">
<li><p>This product shall only be connected to the external power supply rated at 7˜32DC, USB power, and a minimum current supply of  0.5 A.</p></li>
<li><p>Any external power supply used with this product shall comply with relevant regulations and standards applicable in the country of intended use.</p></li>
<li><p>This product should be operated in a ventilated environment with a non-condensing environment and should not be covered when being operated.</p></li>
<li><p>There are no user-serviceable parts inside the product, and opening the unit will likely  damage the product and l invalidate the warranty.</p></li>
<li><p>The cables and connectors of all peripherals used with this product must have adequate insulation to  meet  relevant safety requirements.</p></li>
</ul>
</div>
<div class="section" id="order-information">
<h2>Order Information</h2>
<ul class="simple">
<li><p>Part number: PP-LC5A / LR-LC5A</p></li>
<li><p>HS Code: 8517.69.9000</p></li>
<li><p>Packaging: paper box,1.5 cm x 10 cm x 4 cm 0.15kg</p></li>
</ul>
</div>
</div>


           </div>
