---
title: "System Requirements"
lang: en
slug: "pans-pro-rtls/quick-start-guide/system-requirements"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/pans-pro-rtls/quick-start-guide/system-requirements/"
order: 87
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="system-requirements">
<span id="qsg-system-requirements"></span><h1>System Requirements</h1>
<p>The following sections provide details on necessary software and hardware before starting with RTLS (Real-time Location System) Demo for <a class="reference internal" href="/docs/en/pans-pro-rtls#pans-pro-rtls"><span class="std std-ref">PANS PRO RTLS</span></a>.
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
<td><p>6+</p></td>
<td><p>Mandatory</p></td>
<td><ul class="simple">
<li><p>At least four <code class="docutils literal notranslate"><span class="pre">LC4</span> <span class="pre">devices</span></code> (Anchor Node)</p></li>
<li><p>At least one <code class="docutils literal notranslate"><span class="pre">LC8</span> <span class="pre">device</span></code> (Tag Node)</p></li>
<li><p>At least one <code class="docutils literal notranslate"><span class="pre">LC5</span> <span class="pre">device</span></code> (Gateway Node).</p></li>
</ul>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line">Micro USB</div>
<div class="line">Cable</div>
</div>
</td>
<td><p>5</p></td>
<td><p>Mandatory</p></td>
<td><blockquote>
<div><a class="reference internal image-reference" href="../../../_images/micro-usb.webp"><img alt="../../../_images/micro-usb.webp" class="align-right" src="/docs-assets/_images/micro-usb.webp" style="width: 89.94px; height: 89.94px;"></a>
</div></blockquote>
<p>To power the devices, for data exchange with a PC, or to re-flash the
firmware. Re-flashing the board is optional, devices are programmed
from the production.</p>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line">USB-C</div>
<div class="line">Cable</div>
</div>
</td>
<td><p>1</p></td>
<td><p>Optional</p></td>
<td><blockquote>
<div><a class="reference internal image-reference" href="../../../_images/usb-c.jpg"><img alt="../../../_images/usb-c.jpg" class="align-right" src="/docs-assets/_images/usb-c.jpg" style="width: 91.0px; height: 91.0px;"></a>
</div></blockquote>
<p>To power the devices, for data exchange with a PC, or to re-flash the
firmware. Re-flashing the board is optional, devices are programmed
from the production.</p>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line">USB Wall</div>
<div class="line">Adapter</div>
</div>
</td>
<td><p>5+</p></td>
<td><p>Recommended</p></td>
<td><blockquote>
<div><a class="reference internal image-reference" href="../../../_images/usb-wall-charger.jpg"><img alt="../../../_images/usb-wall-charger.jpg" class="align-right" src="/docs-assets/_images/usb-wall-charger.jpg" style="width: 96.0px; height: 96.0px;"></a>
</div></blockquote>
<p>A compact device that connects to a standard wall power outlet and
provides one or more USB ports to charge or power electronic devices.</p>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line">Android</div>
<div class="line">Device</div>
<div class="line"><br></div>
</div>
</td>
<td><p>1</p></td>
<td><p>Recommended</p></td>
<td><blockquote>
<div><a class="reference internal image-reference" href="../../../_images/samsung-a7.png"><img alt="../../../_images/samsung-a7.png" class="align-right" src="/docs-assets/_images/samsung-a7.png" style="width: 99.80000000000001px; height: 99.80000000000001px;"></a>
</div></blockquote>
<p>Used for running the <a class="reference internal" href="/docs/en/pans-pro-rtls/infrastructure/leaps-server#pans-pro-server"><span class="std std-ref">LEAPS Server</span></a>, an Android application that
can be used to configure the devices and visualize of
the network using Bluetooth or MQTT.
Requires Android OS version 6.0 or higher.</p>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line">Desktop</div>
<div class="line">Device</div>
</div>
</td>
<td><p>1</p></td>
<td><p>Optional</p></td>
<td><blockquote>
<div><a class="reference internal image-reference" href="../../../_images/desktop-device.png"><img alt="../../../_images/desktop-device.png" class="align-right" src="/docs-assets/_images/desktop-device.png" style="width: 99.89999999999999px; height: 88.02px;"></a>
</div></blockquote>
<p>User for various purposes: for running a VirtualBox image that contains
the web server applications (<a class="reference internal" href="/docs/en/pans-pro-rtls/infrastructure/leaps-center#pans-pro-center"><span class="std std-ref">LEAPS Center</span></a>,
<a class="reference internal" href="/docs/en/pans-pro-rtls/infrastructure/leaps-server#pans-pro-server"><span class="std std-ref">LEAPS Server</span></a>, and MQTT Broker), supporting Windows, macOS and
Linux operating systems. Besides that, it can be used for for updating the
device using USB/UART/Bluetooth, for communication with the device via
USB/UART/Bluetooth.</p>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
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
<tr class="row-even"><td><p><a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/pans-pro-uwbs#pans-pro-uwbs"><span class="std std-ref">PANS PRO UWBS</span></a></p></td>
<td><p>-</p></td>
<td><p>Optional</p></td>
<td><p>The PANS PRO Ultra-Wideband Sus-System firmware.</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/en/pans-pro-rtls/infrastructure/pans-pro-manager#pans-pro-manager"><span class="std std-ref">PANS PRO Manager</span></a></p></td>
<td><p>-</p></td>
<td><p>Optional</p></td>
<td><p>An Android application that can be used for configuration of the devices and visualization of the network using Bluetooth or MQTT.</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/en/pans-pro-rtls/infrastructure/leaps-server#pans-pro-server"><span class="std std-ref">LEAPS Server</span></a></p></td>
<td><p>-</p></td>
<td><p>Optional</p></td>
<td><p>A Linux daemon application that serves as a central data hub for the UWB network, responsible for aggregating and transmitting data to/from the external systems via the MQTT Broker.</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/en/pans-pro-rtls/infrastructure/leaps-center#pans-pro-center"><span class="std std-ref">LEAPS Center</span></a></p></td>
<td><p>-</p></td>
<td><p>Optional</p></td>
<td><p>A Web application for configuration and visualization of the UWB network.</p></td>
</tr>
</tbody>
</table>
<div class="section" id="third-party-applications-and-tools">
<h3>Third-party Applications and Tools</h3>
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
<tr class="row-even"><td><p><a class="reference external" href="https://mosquitto.org/download/">Mosquitto MQTT Broker</a></p></td>
<td><p>2.0.11</p></td>
<td><p>Optional</p></td>
<td><p>Mosquitto is an MQTT v5.0/v3.1.1/v3.1 broker. The recommended version of Mosquitto is 2.0.11.</p></td>
</tr>
</tbody>
</table>
</div>
</div>
</div>


           </div>
