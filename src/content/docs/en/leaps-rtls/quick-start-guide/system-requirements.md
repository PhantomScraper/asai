---
title: "System Requirements"
lang: en
slug: "leaps-rtls/quick-start-guide/system-requirements"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/leaps-rtls/quick-start-guide/system-requirements/"
order: 60
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="system-requirements">
<span id="leaps-qsg-system-requirements"></span><h1>System Requirements</h1>
<p>The following sections provide details on necessary software and hardware before starting
with RTLS (Real-time Location System) Demo for <a class="reference internal" href="/docs/en/leaps-rtls#leaps-rtls"><span class="std std-ref">LEAPS RTLS</span></a>.
Please be advised that certain items are optional and not mandatory for all the demonstrations.</p>
<div class="section" id="hardware">
<h2>Hardware</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 14%">
<col style="width: 12%">
<col style="width: 12%">
<col style="width: 63%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>Item</strong></p></th>
<th class="head"><p><strong>Quantity</strong></p></th>
<th class="head"><p><strong>Necessity</strong></p></th>
<th class="head"><p><strong>Description</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>UWB Device</p></td>
<td><p>5+</p></td>
<td><p>Mandatory</p></td>
<td><ul class="simple">
<li><p>At least three Anchor Node</p></li>
<li><p>At least one Tag Node</p></li>
<li><p>At least one Gateway Node</p></li>
</ul>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line">Micro USB</div>
<div class="line">Cable</div>
</div>
</td>
<td><p>6+</p></td>
<td><p>Optional</p></td>
<td><blockquote>
<div><a class="reference internal image-reference" href="../../../_images/micro-usb.webp"><img alt="../../../_images/micro-usb.webp" class="align-right" src="/docs-assets/_images/micro-usb.webp" style="width: 119.92px; height: 119.92px;"></a>
</div></blockquote>
<p>To power the devices, for data exchange with a PC, or to re-flash the
firmware. Re-flashing the board is optional, devices are programmed
from the production.</p>
</td>
</tr>
<tr class="row-even"><td><p>Battery</p></td>
<td><p>6+</p></td>
<td><p>Optional</p></td>
<td><div class="line-block">
<div class="line">To power the UWB device without using the micro USB cable.</div>
<div class="line">Recommended:</div>
</div>
<blockquote>
<div><ul class="simple">
<li><p>Fenix RCR123A (3.7V)</p></li>
<li><p>Keeppower RCR123A 3.7V (860 mAh &amp; included charger)</p></li>
</ul>
<p><a class="reference internal" href="../../../_images/battery-rcr123a.png"><img alt="Fenix" src="/docs-assets/_images/battery-rcr123a.png" style="width: 120.2px; height: 119.2px;"></a>  <a class="reference internal" href="../../../_images/keeppower-rcr123a.jpg"><img alt="keeppower" src="/docs-assets/_images/keeppower-rcr123a.jpg" style="width: 120.0px; height: 120.0px;"></a></p>
</div></blockquote>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line">Phone</div>
<div class="line">Device</div>
<div class="line"><br></div>
</div>
</td>
<td><p>1</p></td>
<td><p>Recommended</p></td>
<td><blockquote>
<div><a class="reference internal image-reference" href="../../../_images/samsung-a7.png"><img alt="../../../_images/samsung-a7.png" class="align-right" src="/docs-assets/_images/samsung-a7.png" style="width: 124.75px; height: 124.75px;"></a>
</div></blockquote>
<p>Used for running the <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a>, an application that
can be used to configure the devices and visualize of
the network using Bluetooth or MQTT.</p>
<ul class="simple">
<li><p><cite>Requires android OS version 6.0 or higher.</cite></p></li>
<li><p><cite>Requires iOS version 15 or newer.</cite></p></li>
</ul>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line">Desktop</div>
<div class="line">Device</div>
</div>
</td>
<td><p>1</p></td>
<td><p>Optional</p></td>
<td><blockquote>
<div><a class="reference internal image-reference" href="../../../_images/desktop-device.png"><img alt="../../../_images/desktop-device.png" class="align-right" src="/docs-assets/_images/desktop-device.png" style="width: 111.0px; height: 97.80000000000001px;"></a>
</div></blockquote>
<p>User for various purposes: for running a VirtualBox image that contains
the web server applications (<a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-gateway#leapsgateway"><span class="std std-ref">LEAPS Gateway</span></a>, <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-server#leapsserver"><span class="std std-ref">LEAPS Server</span></a>,
<a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> and MQTT Broker), supporting Windows, macOS and Linux
operating systems. Besides that, it can be used for for updating the
device using USB/UART/Bluetooth, for communication with the device via
USB/UART, for reprogramming of the UDK devices that contain the DAPLink
integrated and for development of custom applications using the UDK SDK.</p>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line">Raspberry</div>
<div class="line">Pi 3B</div>
<div class="line">or newer</div>
</div>
</td>
<td><p>1</p></td>
<td><p>Optional</p></td>
<td><blockquote>
<div><a class="reference internal image-reference" href="../../../_images/ras-pi-device.jpg"><img alt="../../../_images/ras-pi-device.jpg" class="align-right" src="/docs-assets/_images/ras-pi-device.jpg" style="width: 100.0px; height: 100.0px;"></a>
</div></blockquote>
<p>Used for fast setup of a gateway with web server applications, including
LEAPS Server, LEAPS Center and MQTT Broker. Besides that,
it can be used for updating the device using USB/UART/Bluetooth.</p>
</td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="software">
<h2>Software</h2>
<p>Below is the list of all software applications and tools that are essential for demonstration purposes.</p>
<table class="colwidths-given docutils align-default">
<colgroup>
<col style="width: 10%">
<col style="width: 10%">
<col style="width: 10%">
<col style="width: 70%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Item</p></th>
<th class="head"><p>Version</p></th>
<th class="head"><p>Necessity</p></th>
<th class="head"><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/leaps-uwbs#leapsuwbs"><span class="std std-ref">LEAPS UWBS</span></a></p></td>
<td><p>-</p></td>
<td><p>Optional</p></td>
<td><p>The LEAPS Ultra-Wideband Sus-System firmware. The UDK devices come with LEAPS UWBS preloaded from the production. The firmware is necessary only in case of firmware update or device recovery.</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a></p></td>
<td><p>-</p></td>
<td><p>Optional</p></td>
<td><p>An Android application that can be used for configuration of the devices and visualization of the network using Bluetooth or MQTT.</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-gateway#leapsgateway"><span class="std std-ref">LEAPS Gateway</span></a></p></td>
<td><p>-</p></td>
<td><p>Optional</p></td>
<td><p>A Linux daemon application that serves as a gateway between the LEAPS UWBS and the LEAPS Server and, hence the TCP/IP network.</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-server#leapsserver"><span class="std std-ref">LEAPS Server</span></a></p></td>
<td><p>-</p></td>
<td><p>Optional</p></td>
<td><p>A Linux daemon application that serves as a central data hub for the UWB network, responsible for aggregating and transmitting data to/from the external systems via the MQTT Broker.</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a></p></td>
<td><p>-</p></td>
<td><p>Optional</p></td>
<td><p>A Web application for configuration and visualization of the UWB network.</p></td>
</tr>
</tbody>
</table>
</div>
</div>


           </div>
