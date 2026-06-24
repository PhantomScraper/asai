---
title: "PANS PRO Manager"
lang: en
slug: "pans-pro-rtls/infrastructure/pans-pro-manager"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/pans-pro-rtls/infrastructure/pans-pro-manager/"
order: 99
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="pans-pro-manager">
<span id="id1"></span><h1>PANS PRO Manager</h1>
<p>This page outlines the essential steps for using the PANS PRO Manager tool, specifically designed for Android devices.
It guides users through the configuration, setup, and management of Ultra-wideband devices, ensuring seamless integration
and operation within the PANS PRO RTLS system.</p>
<div class="section" id="key-features">
<h2>Key Features</h2>
<ul class="simple">
<li><p>Allowing management and visualization of the devices for the whole network.</p></li>
<li><p>The communication with the devices are done via the BLE with support for up to 6 concurrent connections to maintain connection reliability.</p></li>
<li><p>The Grid in 2D and 3D provides real-time position updates and visualization of the devices in the network.</p></li>
<li><p>Other useful features include Anchors Auto-Positioning, Firmware Update over BLE, User Management, and Position Logging.</p></li>
</ul>
<hr class="docutils">
<div class="section" id="system-environment">
<h3>System Environment</h3>
<p>The <a class="reference internal" href="#pans-pro-manager"><span class="std std-ref">PANS PRO Manager</span></a> has been developed based on the Android API <strong>level 24</strong> and subsequent versions. Refer to <a class="reference external" href="https://apilevels.com">apilevels</a></p>
<ul class="simple">
<li><p>Minimum android version: Android 7 (API 24)</p></li>
<li><p>Minimum memory: 100 MB (free disk space)</p></li>
<li><p>Minimum Bluetooth version: 4.2 (recommended 5.0 or newer)</p></li>
<li><p>Recommendation for a android device : Google Pixel 7 (equivalent devices)</p></li>
</ul>
</div>
<div class="section" id="instruction">
<h3>Instruction</h3>
<p>To get started, please download the <a class="reference internal" href="#pans-pro-manager"><span class="std std-ref">PANS PRO Manager</span></a> application (<a class="reference external" href="https://play.google.com/store/apps/details?id=global.leaps.manager.panspro&amp;hl=en">available in the Google Play</a>)</p>
<blockquote>
<div><div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/panspro-manager-qr-code.png"><img alt="../../../_images/panspro-manager-qr-code.png" src="/docs-assets/_images/panspro-manager-qr-code.png" style="width: 344.4px; height: 344.4px;"></a>
</div>
</div></blockquote>
</div>
</div>
<hr class="docutils">
<div class="section" id="getting-started">
<h2>Getting started</h2>
<p>To begin using the <a class="reference internal" href="#pans-pro-manager"><span class="std std-ref">PANS PRO Manager</span></a>, a login is required. By default, the username is
<span class="red-text">admin</span> and the password is <span class="red-text">admin</span>, provided that user management settings are enabled.</p>
<table class="custom-table-borderless docutils align-center">
<colgroup>
<col style="width: 50%">
<col style="width: 50%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../_images/ppm-login.jpg"><img alt="login1" src="/docs-assets/_images/ppm-login.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/ppm-login-admin.jpg"><img alt="login2" src="/docs-assets/_images/ppm-login-admin.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
<div class="section" id="menu">
<h3>Menu</h3>
<p>For further user customization options and to access the main features,
please navigate to the menu.</p>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/ppm-menu.jpg"><img alt="../../../_images/ppm-menu.jpg" class="align-center" src="/docs-assets/_images/ppm-menu.jpg" style="width: 216.0px; height: 480.0px;"></a>
</div></blockquote>
<hr class="docutils">
</div>
<div class="section" id="devices-discovery">
<span id="id2"></span><h3>Devices Discovery</h3>
<p>After successfully logging in, the home page will appear as shown in the <span class="red-text">left</span> image.
To quickly detect available network and devices in the area, initiate the <span class="red-text">Start Device Discovery</span> function from the home page.
Wait for the discovery and scanning process to finish. The discovered network and devices will be listed as shown in the <span class="red-text">right</span> image.</p>
<table class="custom-table-borderless docutils align-center">
<colgroup>
<col style="width: 50%">
<col style="width: 50%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../_images/ppm-home-page.jpg"><img alt="discovery1" src="/docs-assets/_images/ppm-home-page.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/ppm-assign-network1.jpg"><img alt="discovery2" src="/docs-assets/_images/ppm-assign-network1.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="network-configuration">
<h3>Network Configuration</h3>
<ul>
<li><p>Creating a Network</p>
<blockquote>
<div><ul class="simple">
<li><p>Choose the device you’d like to set up a network with.</p></li>
<li><p>A dialog box will pop up prompting you to input the network name.</p></li>
<li><p>Type in your desired network name.</p></li>
<li><p>The application will then create the network.</p></li>
</ul>
</div></blockquote>
</li>
</ul>
<table class="custom-table-borderless docutils align-center">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../_images/ppm-assign-network5.jpg"><img alt="nt1" src="/docs-assets/_images/ppm-assign-network5.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/ppm-assign-network6.jpg"><img alt="nt2" src="/docs-assets/_images/ppm-assign-network6.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/ppm-assign-network7.jpg"><img alt="nt3" src="/docs-assets/_images/ppm-assign-network7.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
</tr>
</tbody>
</table>
<ul>
<li><p>Assigning Multiple Devices</p>
<blockquote>
<div><ul class="simple">
<li><p>To add several devices to the network, press and hold on the device in the list.</p></li>
<li><p>Then the application will assign multiple devices.</p></li>
</ul>
</div></blockquote>
</li>
</ul>
<table class="custom-table-borderless docutils align-center">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../_images/ppm-assign-network8.jpg"><img alt="as1" src="/docs-assets/_images/ppm-assign-network8.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/ppm-assign-network9.jpg"><img alt="as2" src="/docs-assets/_images/ppm-assign-network9.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/ppm-assign-network11.jpg"><img alt="as3" src="/docs-assets/_images/ppm-assign-network11.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
</tr>
</tbody>
</table>
<ul class="simple">
<li><p>If the network is already available, please choose it.</p></li>
</ul>
<table class="custom-table-borderless docutils align-center">
<colgroup>
<col style="width: 50%">
<col style="width: 50%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../_images/ppm-network-2.jpg"><img alt="nw1" src="/docs-assets/_images/ppm-network-2.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/ppm-network-1.jpg"><img alt="nw2" src="/docs-assets/_images/ppm-network-1.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
</tr>
</tbody>
</table>
<ul>
<li><p>To view detailed information about the chosen device, click on the device. Detailed info will be displayed below.</p>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/ppm-network-3.jpg"><img alt="../../../_images/ppm-network-3.jpg" class="align-center" src="/docs-assets/_images/ppm-network-3.jpg" style="width: 216.0px; height: 480.0px;"></a>
</div></blockquote>
</li>
<li><p>To remove a device from the network, swipe the device to the right.</p>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/ppm-assign-network13.jpg"><img alt="../../../_images/ppm-assign-network13.jpg" class="align-center" src="/docs-assets/_images/ppm-assign-network13.jpg" style="width: 216.0px; height: 480.0px;"></a>
</div></blockquote>
</li>
</ul>
</div>
<hr class="docutils">
<div class="section" id="device-configuration">
<h3>Device Configuration</h3>
<p>To configure a node, you need to assign the node to a specific network in advance.</p>
<ul class="simple">
<li><p>Select the network with the specified node to view network details.</p></li>
<li><p>Swipe the screen to scan, making sure there is a connection signal from the application to the device.</p></li>
<li><p>If the pencil icon is available, you can select it to configure the node.</p></li>
</ul>
<p>The following two examples illustrate the configurations:</p>
<ul class="simple">
<li><p>The left device represents a <span class="red-text">tag node</span>, where the <span class="red-text">NORMAL UPDATE RATE</span> and <span class="red-text">STATIONARY UPDATE RATE</span> parameters are configurable.</p></li>
<li><p>The right device represents an <span class="red-text">anchor node</span>, where the <span class="red-text">POSITION (M)</span> parameter is configurable.</p></li>
</ul>
<table class="custom-table-borderless docutils align-center">
<colgroup>
<col style="width: 50%">
<col style="width: 50%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../_images/ppm-device-configure-a.jpg"><img alt="device1" src="/docs-assets/_images/ppm-device-configure-a.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/ppm-device-configure-b.jpg"><img alt="device2" src="/docs-assets/_images/ppm-device-configure-b.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="network-visualization">
<h3>Network Visualization</h3>
<p>The primary feature of the <a class="reference internal" href="#pans-pro-manager"><span class="std std-ref">PANS PRO Manager</span></a> tool is its capability to visualize the network’s accurate positions.
The following example illustrates the network representation in 2D mode.</p>
<table class="custom-table-borderless docutils align-center">
<colgroup>
<col style="width: 50%">
<col style="width: 50%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../_images/ppm-grib-2d-1.jpg"><img alt="2d1" src="/docs-assets/_images/ppm-grib-2d-1.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/ppm-grib-2d-3.jpg"><img alt="2d2" src="/docs-assets/_images/ppm-grib-2d-3.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
</tr>
</tbody>
</table>
<p>To display the network in 3D, the following example illustrates the network representation in 3D mode.</p>
<table class="custom-table-borderless docutils align-center">
<colgroup>
<col style="width: 50%">
<col style="width: 50%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../_images/ppm-grib-3d-0.jpg"><img alt="3d1" src="/docs-assets/_images/ppm-grib-3d-0.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/ppm-grib-3d-1.jpg"><img alt="3d2" src="/docs-assets/_images/ppm-grib-3d-1.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="position-logs">
<h3>Position Logs</h3>
<p>To display the details of each device in the network along with their static data,
the following example illustrates a device and its corresponding position.</p>
<a class="reference internal image-reference" href="../../../_images/ppm-positiong-logs.jpg"><img alt="../../../_images/ppm-positiong-logs.jpg" class="align-center" src="/docs-assets/_images/ppm-positiong-logs.jpg" style="width: 216.0px; height: 480.0px;"></a>
</div>
<hr class="docutils">
<div class="section" id="auto-positioning">
<h3>Auto-Positioning</h3>
<p>Another key feature, Auto-Positioning, assists users in quickly initializing the network automatically.</p>
<p>Access <span class="red-text">Auto positioning</span>. Tap the <span class="red-text">options menu</span> (<em>represented as three vertical dots</em>) within the application.</p>
<ul class="simple">
<li><p>The following example illustrates the results after completing the Auto-Positioning process.</p></li>
</ul>
<table class="custom-table-borderless docutils align-center">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../_images/ppm-network-menu.jpg"><img alt="am1" src="/docs-assets/_images/ppm-network-menu.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/ppm-auto-positioning-1.jpg"><img alt="am2" src="/docs-assets/_images/ppm-auto-positioning-1.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/ppm-auto-positioning-2.jpg"><img alt="am3" src="/docs-assets/_images/ppm-auto-positioning-2.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
</tr>
</tbody>
</table>
<ul class="simple">
<li><p>Wait for completion; you will receive position information for the nodes. Then press <span class="red-text">SAVE</span> to save the results.</p></li>
</ul>
<table class="custom-table-borderless docutils align-center">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../_images/ppm-auto-positioning-3.jpg"><img alt="au1" src="/docs-assets/_images/ppm-auto-positioning-3.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/ppm-auto-positioning-4.jpg"><img alt="au2" src="/docs-assets/_images/ppm-auto-positioning-4.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/ppm-auto-positioning-5.jpg"><img alt="au3" src="/docs-assets/_images/ppm-auto-positioning-5.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="firmware-update-over-ble">
<span id="id3"></span><h3>Firmware Update over BLE</h3>
<p>Access firmware status. Tap the <span class="red-text">options menu</span> (<em>represented as three vertical dots</em>) within the application.
Look for the <span class="red-text">Firmware status</span> option and select it.</p>
<p>Choose the devices to update.</p>
<table class="custom-table-borderless docutils align-center">
<colgroup>
<col style="width: 50%">
<col style="width: 50%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../_images/ppm-network-menu.jpg"><img alt="fw1" src="/docs-assets/_images/ppm-network-menu.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/ppm-firmware-update.jpg"><img alt="fw2" src="/docs-assets/_images/ppm-firmware-update.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
</tr>
</tbody>
</table>
</div>
</div>
<hr class="docutils">
<div class="section" id="troubleshooting">
<h2>Troubleshooting</h2>
<ul class="simple">
<li><p>Always ensure the BLE connection is stable, and the device is within coverage range.</p></li>
</ul>
</div>
</div>


           </div>
