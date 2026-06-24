---
title: "LEAPS Manager"
lang: en
slug: "leaps-rtls/infrastructure/leaps-manager"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/leaps-rtls/infrastructure/leaps-manager/"
order: 69
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-manager">
<span id="leapsmanager"></span><h1>LEAPS Manager</h1>
<p><a class="reference internal" href="#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> is an essential tool that provides device discovery, device configuration,
network configuration, network management and location visualization for
the UDK (<a class="reference external" href="/docs/en/UDK">All-in-One Ultra-Wideband Development Kit</a>)
and the LEAPS RTLS (an advanced Ultra-Wideband Real-Time Location System).</p>
<hr class="docutils">
<div class="section" id="key-features">
<h2>Key Features</h2>
<ul class="simple">
<li><p>The Demo Wizard allows an easy and super fast way to configure predefined demo setups of the kit.</p></li>
<li><p>The Grid in 2D and 3D provides real-time position updates and visualization of the devices in the network.</p></li>
<li><p>The communication with the devices are done via the BLE with support for up to 6 concurrent connections to maintain connection reliability.</p></li>
<li><p>When data centralization is used, the communication with the <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-server#leapsserver"><span class="std std-ref">LEAPS Server</span></a> via MQTT is available, allowing management and visualization of the devices for the whole network.</p></li>
<li><p>Other useful features include User Management, Firmware Update over BLE, Anchors Auto-Positioning, Position Logging and Debug Console.</p></li>
</ul>
<hr class="docutils">
<div class="section" id="system-environment">
<h3>System Environment</h3>
<p>The <a class="reference internal" href="#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> has been developed based on the Android API level 24 and subsequent versions. Refer to <a class="reference external" href="https://apilevels.com">apilevels</a></p>
<ul class="simple">
<li><p>Minimum android version: Android 7 (API 24)</p></li>
<li><p>Minimum memory: 100 MB (free disk space)</p></li>
<li><p>Minimum Bluetooth version: 4.2  (recommended 5.0 or newer)</p></li>
<li><p>Recommendation for a android device : Google Pixel 7 (equivalent devices)</p></li>
</ul>
<p>And the non-recommended device is <strong>Samsung Galaxy Tab A8</strong>, refer to the known issue list:</p>
<ul class="simple">
<li><p><a class="reference external" href="https://devzone.nordicsemi.com/f/nordic-q-a/88557/samsung-galaxy-tab-a8-does-not-work-with-nrf-mesh-android-app">Device does-not-work-with-nrf-mesh-android-app</a></p></li>
<li><p><a class="reference external" href="https://devzone.nordicsemi.com/f/nordic-q-a/89631/galaxy-tab-a8-sm-x200-connection-issues-with-gatt-error-133-after-multiple-connecting-failures">Connection-issues-with-gatt-error-133-after-multiple-connecting-failures</a></p></li>
</ul>
</div>
<hr class="docutils">
<div class="section" id="instruction">
<h3>Instruction</h3>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-0" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-0">
Android</label><div class="sd-tab-content docutils">
<p>To get started, please download the <a class="reference internal" href="#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> application (<a class="reference external" href="https://play.google.com/store/apps/details?id=global.leaps.manager.leaps&amp;hl=en_GB&amp;gl=US">available in the Google Play</a>)</p>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/leaps-manager-qr-code.png"><img alt="../../../_images/leaps-manager-qr-code.png" src="/docs-assets/_images/leaps-manager-qr-code.png" style="width: 337.5px; height: 337.5px;"></a>
</div>
</div>
<input id="sd-tab-item-1" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-1">
iOS</label><div class="sd-tab-content docutils">
<p>To get started, please download the <a class="reference internal" href="#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> application (<a class="reference external" href="https://apps.apple.com/vn/app/leaps-manager/id6737454926">available in the App Store</a>)</p>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/leaps-manager-ios-qr-code.png"><img alt="../../../_images/leaps-manager-ios-qr-code.png" src="/docs-assets/_images/leaps-manager-ios-qr-code.png" style="width: 344.09999999999997px; height: 344.09999999999997px;"></a>
</div>
</div>
</div>
</div>
</div>
<div class="section" id="getting-started">
<h2>Getting started</h2>
<p>By default, a login account with username is <span class="red-text">admin</span> and password is <span class="red-text">admin</span> in case settings enable user management.</p>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/leaps-manager-android-login.jpg"><img alt="../../../_images/leaps-manager-android-login.jpg" src="/docs-assets/_images/leaps-manager-android-login.jpg" style="width: 216.0px; height: 480.0px;"></a>
</div>
<div class="section" id="network-configuration">
<h3>Network Configuration</h3>
<p>Open the app then select the <span class="red-text">Start Device Discovery</span> if there are no assigned networks.
If a network already exists. Navigate to the <span class="red-text">Existing Networks</span>.</p>
<p>Here, the application begins to discover and scan all available networks and devices.</p>
<table class="custom-table-borderless docutils align-center">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../_images/leaps-manager-android-home.jpg"><img alt="lm1" src="/docs-assets/_images/leaps-manager-android-home.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/leaps-manager-android-tab-create-network.jpg"><img alt="lm2" src="/docs-assets/_images/leaps-manager-android-tab-create-network.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/leaps-manager-android-create-network.jpg"><img alt="lm3" src="/docs-assets/_images/leaps-manager-android-create-network.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
</tr>
</tbody>
</table>
<p>Wait for the discovery and scanning process to finish. You can specify a network if it is available but not assigned.
You can select and create devices and then assign them to specified networks.</p>
<table class="custom-table-borderless docutils align-center">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../_images/leaps-manager-android-assign-devices.jpg"><img alt="lm4" src="/docs-assets/_images/leaps-manager-android-assign-devices.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/leaps-manager-android-assigning-devices.jpg"><img alt="lm5" src="/docs-assets/_images/leaps-manager-android-assigning-devices.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/leaps-manager-android-created-network.jpg"><img alt="lm6" src="/docs-assets/_images/leaps-manager-android-created-network.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="node-configuration">
<h3>Node Configuration</h3>
<p>To configure a node, you need to assign the node to a specific network in advance. Select the network with the specified node to view network details.</p>
<p>Swipe the screen to scan, making sure there is a connection signal from the application to the device.</p>
<p>If the pencil icon is available, you can select it to configure the node.</p>
<table class="custom-table-borderless docutils align-center">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../_images/leaps-manager-android-leaps-demo-network.jpg"><img alt="lm7" src="/docs-assets/_images/leaps-manager-android-leaps-demo-network.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/leaps-manager-android-edit-anchor.jpg"><img alt="lm8" src="/docs-assets/_images/leaps-manager-android-edit-anchor.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/leaps-manager-android-edit-tag.jpg"><img alt="lm9" src="/docs-assets/_images/leaps-manager-android-edit-tag.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="demo-selector">
<h3>Demo Selector</h3>
<p>Navigate to the demo selector, then select the demo you want to configure:</p>
<ul class="simple">
<li><p>Nearby Interaction Demo with an iPhone</p></li>
<li><p>Locate Device using Angle-of-Arrival (AoA) Demo</p></li>
<li><p>Infrastructure-less proximity Demo</p></li>
<li><p>Downlink TDoA RTLS Demo</p></li>
<li><p>High-Speed Downlink TDoA RTLS Demo</p></li>
<li><p>TWR RTLS and Data Telemetry Demo</p></li>
</ul>
<p>Example: TWR RTLS and Data Telemetry Demo</p>
<table class="custom-table-borderless docutils align-center">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../_images/leaps-manager-android-demo-selector.jpg"><img alt="lm10" src="/docs-assets/_images/leaps-manager-android-demo-selector.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/leaps-manager-android-twr-rtls.jpg"><img alt="lm11" src="/docs-assets/_images/leaps-manager-android-twr-rtls.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/leaps-manager-android-config-auto.jpg"><img alt="lm12" src="/docs-assets/_images/leaps-manager-android-config-auto.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
</tr>
</tbody>
</table>
<table class="custom-table-borderless docutils align-center">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../_images/leaps-manager-android-auto-positioning.jpg"><img alt="lm13" src="/docs-assets/_images/leaps-manager-android-auto-positioning.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/leaps-manager-android-auto-positioning-measuring.jpg"><img alt="lm14" src="/docs-assets/_images/leaps-manager-android-auto-positioning-measuring.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/leaps-manager-android-auto-positioning-save.jpg"><img alt="lm15" src="/docs-assets/_images/leaps-manager-android-auto-positioning-save.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
</tr>
</tbody>
</table>
<table class="custom-table-borderless docutils align-center">
<colgroup>
<col style="width: 50%">
<col style="width: 50%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../_images/leaps-manager-android-leaps-demo-network.jpg"><img alt="lm16" src="/docs-assets/_images/leaps-manager-android-leaps-demo-network.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/leaps-manager-android-network-on-2D-grid.jpg"><img alt="lm17" src="/docs-assets/_images/leaps-manager-android-network-on-2D-grid.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="configuration-information-for-10db-lna-pa-settings">
<h3>Configuration Information for +10dB, LNA/PA Settings</h3>
<p>In demo, you’ll find detailed information about the +10dB Low Noise Amplifier (LNA) / Power Amplifier (PA) settings. This configuration is designed to optimize signal strength and quality for your specific application.</p>
<p>The configurations:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">FCC/ETSI</span> <span class="pre">on</span> <span class="pre">channel</span> <span class="pre">5</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ETSI+10</span> <span class="pre">dB</span> <span class="pre">on</span> <span class="pre">channel</span> <span class="pre">5</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">FCC/ETSI</span> <span class="pre">on</span> <span class="pre">channel</span> <span class="pre">9</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ETSI+10</span> <span class="pre">dB</span> <span class="pre">on</span> <span class="pre">channel</span> <span class="pre">9</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">Japan</span> <span class="pre">ARIB</span> <span class="pre">on</span> <span class="pre">channel</span> <span class="pre">9</span></code></p></li>
</ul>
<p>Available on demos:</p>
<ul class="simple">
<li><p>Infrastructure-less proximity Demo</p></li>
<li><p>Downlink TDoA RTLS Demo</p></li>
<li><p>High-Speed Downlink TDoA RTLS Demo</p></li>
<li><p>TWR RTLS and Data Telemetry Demo</p></li>
</ul>
<p>How to configuration:</p>
<ol class="arabic simple">
<li><p>Navigate to the top right corner of the demo screen.</p></li>
<li><p>Click on the 3 dots icon (menu icon).</p></li>
<li><p>Select the corresponding configuration option to view or select settings.</p></li>
</ol>
<table class="custom-table-borderless docutils align-center">
<colgroup>
<col style="width: 50%">
<col style="width: 50%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../_images/leaps-manager-android-fcc-etsi-ch9.jpg"><img alt="lm18" src="/docs-assets/_images/leaps-manager-android-fcc-etsi-ch9.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/leaps-manager-android-10dB-lna-pa-settings.jpg"><img alt="lm19" src="/docs-assets/_images/leaps-manager-android-10dB-lna-pa-settings.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="firmware-update-over-ble">
<span id="leaps-manager-fup-over-ble"></span><h3>Firmware Update over BLE</h3>
<blockquote>
<div><div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-2" name="sd-tab-set-1" type="radio">
<label class="sd-tab-label" for="sd-tab-item-2">
Default Package</label><div class="sd-tab-content docutils">
<p>Navigate to the <span class="red-text">Demo Selector</span>.
Additionally, you can navigate to the created network to update the devices in the network.</p>
<p>Access firmware status. Tap the <span class="red-text">options menu</span> (<em>represented as three vertical dots</em>) within the application. Look for the <span class="red-text">Firmware status</span> option and select it.</p>
<p>Choose the devices to update.</p>
<table class="custom-table-borderless docutils align-center">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../_images/leaps-manager-android-firmware-update-network.jpg"><img alt="lm20" src="/docs-assets/_images/leaps-manager-android-firmware-update-network.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/leaps-manager-android-demo-selector-firmware-update.jpg"><img alt="lm21" src="/docs-assets/_images/leaps-manager-android-demo-selector-firmware-update.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/leaps-manager-android-firmware-status.jpg"><img alt="lm22" src="/docs-assets/_images/leaps-manager-android-firmware-status.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
</tr>
</tbody>
</table>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>The speed of firmware up over BLE, that is around 1.6kBps</p>
</div>
<p>The app will provide visual indicators or progress bars to show how the update is proceeding. Be patient and let the update process run its course.</p>
<p>Once the update is complete, you will see the <span class="red-text">status is done</span>. Additionally, the device will emit two beeps to indicate the update’s success. The board will automatically reset itself as part of the process.</p>
<table class="custom-table-borderless docutils align-center">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../_images/leaps-manager-android-firmware-update-eldr.jpg"><img alt="lm23" src="/docs-assets/_images/leaps-manager-android-firmware-update-eldr.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/leaps-manager-android-firmware-update-main.jpg"><img alt="lm24" src="/docs-assets/_images/leaps-manager-android-firmware-update-main.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/leaps-manager-android-firmware-update-completed.jpg"><img alt="lm25" src="/docs-assets/_images/leaps-manager-android-firmware-update-completed.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
</tr>
</tbody>
</table>
</div>
<input id="sd-tab-item-3" name="sd-tab-set-1" type="radio">
<label class="sd-tab-label" for="sd-tab-item-3">
Selectable Package</label><div class="sd-tab-content docutils">
<ol class="arabic">
<li><p>Download the <a class="reference external" href="https://drive.google.com/file/d/12XES6qiCJDZ16JSx841OqcZfqSdy4OIJ/view">LEAPS-UWBS-Firmware-v1.1.0-package.zip</a> file to your PC. Use a program like WinZip or 7-Zip to extract the contents of the downloaded file.</p></li>
<li><p>Open the LM and navigate to the <span class="red-text">Demo Selector</span>. Additionally, you can navigate to the created network to update the devices in the network. Access firmware status. Tap the <span class="red-text">options menu</span> (<em>represented as three vertical dots</em>) within the application. Look for the <span class="red-text">Firmware status</span> option and select it.</p></li>
<li><p>In the top-right corner, click button to select the firmware Package.</p>
<table class="custom-table-borderless docutils align-center">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../_images/leaps-manager-home-page.jpg"><img alt="lm37" src="/docs-assets/_images/leaps-manager-home-page.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/leaps-manager-selecting-package.jpg"><img alt="lm38" src="/docs-assets/_images/leaps-manager-selecting-package.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/leaps-manager-selecting-package_001.jpg"><img alt="lm39" src="/docs-assets/_images/leaps-manager-selecting-package_001.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
</tr>
</tbody>
</table>
</li>
<li><p>After successfully selecting the package, choose the devices to update.</p>
<blockquote>
<div><p><a class="reference internal" href="../../../_images/leaps-manager-selecting-devices.jpg"><img alt="lm40" src="/docs-assets/_images/leaps-manager-selecting-devices.jpg" style="width: 216.0px; height: 480.0px;"></a></p>
</div></blockquote>
</li>
</ol>
<p>The app will provide visual indicators or progress bars to show how the update is proceeding. Be patient and let the update process run its course.</p>
<p>Once the update is complete, you will see the <span class="red-text">status is done</span>. Additionally, the device will emit two beeps to indicate the update’s success. The board will automatically reset itself as part of the process.</p>
</div>
</div>
</div></blockquote>
</div>
<div class="section" id="auto-positioning">
<h3>Auto-Positioning</h3>
<p><strong>1. Introduction</strong></p>
<p>This guide will help you understand how to effectively use this tool on application.</p>
<p>The auto-positioning feature allows you to accurately position nodes based on selected anchors. Proper setup is crucial for optimal performance.</p>
<ul class="simple">
<li><p>Introduction</p></li>
<li><p>Accessing auto-positioning</p></li>
<li><p>Selecting anchors</p></li>
<li><p>Configuring calculation modes</p></li>
<li><p>Starting measurements</p></li>
<li><p>Recalculating positions</p></li>
<li><p>Viewing and adjusting node positions on the Map</p></li>
<li><p>Saving configuration</p></li>
<li><p>FAQs</p></li>
</ul>
<p><strong>2. Accessing Auto-Positioning</strong></p>
<p>To access the auto-positioning feature, follow one of these methods based on your network status:</p>
<blockquote>
<div><ol class="upperalpha simple">
<li><p>Menu access</p></li>
</ol>
<ul class="simple">
<li><p>Tap the menu icon: Locate and tap the menu icon in the <code class="docutils literal notranslate"><span class="pre">right</span> <span class="pre">corner</span></code> of the screen.</p></li>
<li><p>Select the <code class="docutils literal notranslate"><span class="pre">Auto</span> <span class="pre">positioning</span></code> feature from the menu.</p></li>
</ul>
<ol class="upperalpha simple" start="2">
<li><p>Select auto-positioning</p></li>
</ol>
<ul class="simple">
<li><p>Access <code class="docutils literal notranslate"><span class="pre">Demo</span> <span class="pre">Selector</span></code>.</p></li>
<li><p>Choose the <code class="docutils literal notranslate"><span class="pre">Auto</span> <span class="pre">positioning</span></code> option from there.</p></li>
</ul>
</div></blockquote>
<table class="custom-table-borderless docutils align-center">
<colgroup>
<col style="width: 50%">
<col style="width: 50%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../_images/leaps-manager-auto-positioning-0.jpg"><img alt="lm26" src="/docs-assets/_images/leaps-manager-auto-positioning-0.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/leaps-manager-auto-positioning-1.jpg"><img alt="lm27" src="/docs-assets/_images/leaps-manager-auto-positioning-1.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
</tr>
</tbody>
</table>
<p><strong>3. Selecting Anchors</strong></p>
<a class="reference internal image-reference" href="../../../_images/leaps-manager-auto-positioning-2.jpg"><img alt="../../../_images/leaps-manager-auto-positioning-2.jpg" class="align-right" src="/docs-assets/_images/leaps-manager-auto-positioning-2.jpg" style="width: 237.60000000000002px; height: 528.0px;"></a>
<p>The application will display a list of anchors.</p>
<p>Select anchors:</p>
<blockquote>
<div><ul class="simple">
<li><p>Tick the checkboxes next to at least <code class="docutils literal notranslate"><span class="pre">2</span> <span class="pre">anchors</span></code>.</p></li>
<li><p>Ensure that <code class="docutils literal notranslate"><span class="pre">one</span> <span class="pre">anchor</span></code> is designated as the <code class="docutils literal notranslate"><span class="pre">initiator</span></code>.</p></li>
<li><p>The anchors must <code class="docutils literal notranslate"><span class="pre">stand</span></code> and face each other for accurate positioning.</p></li>
</ul>
</div></blockquote>
<p><strong>4. Configuring Calculation Modes</strong> (<strong>optional</strong>)</p>
<ul class="simple">
<li><p>Calculated mode: If all configurations are set to <code class="docutils literal notranslate"><span class="pre">Calculated</span></code> the application will automatically compute the node positions.</p></li>
<li><p>Manual mode: If set to <code class="docutils literal notranslate"><span class="pre">Manual</span></code> the positions will remain mostly fixed until you manually adjust or recalculate them.</p></li>
</ul>
<p><strong>5. Starting Measurements</strong></p>
<p>After selecting your anchors, click the <code class="docutils literal notranslate"><span class="pre">Measure</span></code> button to start the positioning process.</p>
<ul class="simple">
<li><p>Wait for completion: Allow the process to finish; you will receive position information for the selected nodes.</p></li>
</ul>
<table class="custom-table-borderless docutils align-center">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../_images/leaps-manager-auto-positioning-4.jpg"><img alt="lm28" src="/docs-assets/_images/leaps-manager-auto-positioning-4.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/leaps-manager-auto-positioning-5.jpg"><img alt="lm29" src="/docs-assets/_images/leaps-manager-auto-positioning-5.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/leaps-manager-auto-positioning-6.jpg"><img alt="lm30" src="/docs-assets/_images/leaps-manager-auto-positioning-6.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
</tr>
</tbody>
</table>
<p><strong>6. Recalculating Positions</strong> (<strong>optional</strong>)</p>
<ul class="simple">
<li><p>If you need to make adjustments, simply press the <code class="docutils literal notranslate"><span class="pre">Recalculate</span></code> button to redo the calculations.</p></li>
</ul>
<p><strong>7. Viewing and Adjusting Node Positions on the 2D grid</strong> (<strong>optional</strong>)</p>
<ol class="arabic simple">
<li><p>Access the map:</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>Tap the map icon in the <code class="docutils literal notranslate"><span class="pre">top</span> <span class="pre">right</span> <span class="pre">corner</span></code> to view live positions of the nodes.</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="2">
<li><p>Adjust node positions:</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">Rotate</span></code> nodes using the rotation feature.</p></li>
<li><p>Set a <code class="docutils literal notranslate"><span class="pre">specific</span> <span class="pre">position</span></code> for each node as needed.</p></li>
<li><p>Press the <code class="docutils literal notranslate"><span class="pre">hold</span></code> node to move nodes freely to any desired location.</p></li>
<li><p>You can also perform auto positioning or recalculate from this interface.</p></li>
</ul>
</div></blockquote>
<table class="custom-table-borderless docutils align-center">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../_images/leaps-manager-auto-positioning-8.jpg"><img alt="lm31" src="/docs-assets/_images/leaps-manager-auto-positioning-8.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/leaps-manager-auto-positioning-7.jpg"><img alt="lm32" src="/docs-assets/_images/leaps-manager-auto-positioning-7.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/leaps-manager-auto-positioning-9.jpg"><img alt="lm33" src="/docs-assets/_images/leaps-manager-auto-positioning-9.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
</tr>
</tbody>
</table>
<p><strong>8. Saving Configuration</strong></p>
<blockquote>
<div><ul class="simple">
<li><p>Once you are satisfied with the adjustments, press the <code class="docutils literal notranslate"><span class="pre">Save</span></code> button or save icon located in the <code class="docutils literal notranslate"><span class="pre">top</span> <span class="pre">toolbar</span></code> of the 2D grid.</p></li>
</ul>
<table class="custom-table-borderless docutils align-center">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../_images/leaps-manager-auto-positioning-10.jpg"><img alt="lm34" src="/docs-assets/_images/leaps-manager-auto-positioning-10.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/leaps-manager-auto-positioning-11.jpg"><img alt="lm35" src="/docs-assets/_images/leaps-manager-auto-positioning-11.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/leaps-manager-auto-positioning-12.jpg"><img alt="lm36" src="/docs-assets/_images/leaps-manager-auto-positioning-12.jpg" style="width: 216.0px; height: 480.0px;"></a></p></td>
</tr>
</tbody>
</table>
</div></blockquote>
<p>Back to the 2D grid to continue working on your network setup.</p>
<p><strong>FAQs</strong></p>
<ol class="arabic">
<li><div class="line-block">
<div class="line"><strong>Q:</strong> What if no anchors appear on the list?</div>
<div class="line"><strong>A:</strong> Ensure your network is active, and the anchors are properly configured in the environment.</div>
</div>
</li>
<li><div class="line-block">
<div class="line"><strong>Q:</strong> Can I use a single anchor for positioning?</div>
<div class="line"><strong>A:</strong> No, you must select at least two anchors for accurate results.</div>
</div>
</li>
</ol>
</div>
</div>
<hr class="docutils">
<div class="section" id="troubleshooting">
<h2>Troubleshooting</h2>
<ul class="simple">
<li><p>Always ensure the BLE connection is stable and the device is within coverage range.</p></li>
</ul>
</div>
</div>


           </div>
