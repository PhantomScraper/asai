---
title: "Locate Device using Angle-of-Arrival (AoA) Demo"
lang: en
slug: "udk/udk-start/locate-device-using-angle-of-arrival-demo"
section: "udk"
sourceUrl: "https://docs.leapslabs.com/udk/udk-start/locate-device-using-angle-of-arrival-demo/"
order: 84
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="locate-device-using-angle-of-arrival-aoa-demo">
<span id="anchor-lc"></span><h1>Locate Device using Angle-of-Arrival (AoA) Demo</h1>
<a class="reference internal image-reference" href="../../../_images/locate_device_using_angle-of-arrival_demo.png"><img alt="../../../_images/locate_device_using_angle-of-arrival_demo.png" class="align-right" src="/docs-assets/_images/locate_device_using_angle-of-arrival_demo.png" style="width: 216.0px; height: 245.88px;"></a>
<p><strong>Prepare for setup</strong></p>
<ol class="arabic simple">
<li><p><a class="reference internal" href="/docs/en/udk/udk-start/partner-application-aoa-app#anchor-ranging-aoa"><span class="std std-ref">UWB Ranging &amp; AoA Demo App</span></a> desktop program is installed on your computer.</p></li>
<li><p>One LC13 (gray) device and at least one LC14 (white) device.</p></li>
<li><p>USB-C data cables for the connected devices.</p></li>
<li><p><em>Optional:</em> <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> <em>application installed.</em></p></li>
<li><p><em>Optional: batteries for the Responder devices.</em></p></li>
</ol>
<p><strong>Setup time:</strong> less than 5 minutes</p>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-0" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-0">
Quick Start</label><div class="sd-tab-content docutils">
<p><strong>Overview</strong></p>
<p>This setup demonstrates <span class="red-text">FiRa compatibility</span> between devices. Distance and angle measurement shows the direction between the Initiator and the Responder devices in the desktop application.</p>
<p><strong>Typical applications</strong>: Access control, follow me, locate and track objects or devices within an indoor environment.</p>
<p><strong>Setup instructions</strong></p>
<ol class="arabic simple">
<li><p>Download and install the application on your computer.</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>See details in the <a class="reference internal" href="/docs/en/udk/udk-start/partner-application-aoa-app#anchor-ranging-aoa"><span class="std std-ref">UWB Ranging &amp; AoA Demo App</span></a> installation instructions.</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="2">
<li><p>Power <span class="red-text">ON</span> the LC13 and LC14 devices.</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>The LC13 will function as an Initiator, and the LC14(s) will function as a Responder(s) in this demo.</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="3">
<li><p>Configure the device into the <span class="red-text">Qorvo UCI mode</span> using one of the following options:</p></li>
</ol>
<blockquote>
<div><ol class="upperalpha simple">
<li><p>Configure the device using the button.</p></li>
</ol>
<blockquote>
<div><p>3.1. Press and hold the <a class="reference internal" href="/docs/en/udk/udk-start/device-hw-interfaces#uihwinterfaces"><span class="std std-ref">Button B</span></a> until you hear a beep sound and the <span class="green-text">GREEN LED</span> blinks.</p>
<p>3.2. If a <span class="red-text">RED</span> or <span class="blue-text">BLUE</span> color appears, please repeat step a.</p>
<p>3.3. When the device blinks <span class="green-text">GREEN LED</span> after the beep sound, the device is configured in the <span class="red-text">Qorvo UCI mode</span>.</p>
<img alt="../../../_images/leaps-config-to-qorvo-uci-mode.gif" class="align-center" src="/docs-assets/_images/leaps-config-to-qorvo-uci-mode.gif">
</div></blockquote>
<ol class="upperalpha simple" start="2">
<li><p>Configure using the demo selector in the <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a>:.</p></li>
</ol>
<blockquote>
<div><p>3.1. Open the <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> and select  the <span class="red-text">Demo Selector</span> from the main page.</p>
<p>3.2. select the <span class="red-text">Locate Device Using Angle-of-Arrival</span>.</p>
<p>3.3. A list of discovered devices via Bluetooth will appear on the list. Swipe down to update the list if needed.</p>
<p>3.4. Select the devices that will be used for the demo. The <span class="red-text">Required devices</span> on the top side indicates the amount of devices needed for the demo.</p>
<p>3.5. Press the <span class="red-text">SAVE</span> to configure the device(s) into the <span class="red-text">Qorvo UCI mode</span>.</p>
<p>3.6. Please check visually that the <span class="green-text">GREEN LED</span> blinks when the device starts.</p>
<img alt="../../../_images/qorvo-uwb-ranging-aoa.gif" class="align-center" src="/docs-assets/_images/qorvo-uwb-ranging-aoa.gif">
</div></blockquote>
</div></blockquote>
<ol class="arabic" start="4">
<li><p>Use USB-C data cables to connect the devices and use <a class="reference internal" href="/docs/en/udk/udk-start/device-hw-interfaces#hardware-interface"><span class="std std-ref">USB-C Data Port 1</span></a> to the PC.</p>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/connect-uwbrangingaoa-002.jpg"><img alt="../../../_images/connect-uwbrangingaoa-002.jpg" src="/docs-assets/_images/connect-uwbrangingaoa-002.jpg" style="width: 98%;"></a>
</div></blockquote>
</li>
</ol>
<blockquote>
<div><p><em>Optional: Plug the batteries into the Responder device(s) if you want to disconnect the device from the PC to move it freely after starting the demo.</em></p>
</div></blockquote>
<ol class="arabic" start="5">
<li><p>Open the <span class="red-text">UWB Ranging &amp; AoA Demo App</span> on your desktop. click the <span class="red-text">Next</span> to get into the device list.</p>
<ul class="simple">
<li><p>The USB connected devices will appear on the device list, which might take a few seconds. Review the list and identify the device(s) you want to use. By default, all the discovered devices via the USB will be selected.</p></li>
<li><p>Additional configuration per device or <span class="red-text">Fira Configuration</span> can be changed if needed. The default values should work fine to start with.</p></li>
</ul>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/uwb_ranging_and_aoa_demo_app_main.png"><img alt="../../../_images/uwb_ranging_and_aoa_demo_app_main.png" src="/docs-assets/_images/uwb_ranging_and_aoa_demo_app_main.png" style="width: 98%;"></a>
</div></blockquote>
</li>
<li><p>Press the <span class="red-text">Save and start</span> to start the demo. The following <span class="red-text">Real Time Location</span> window will display a coordinate map with distances and angles between the selected Initiator and Responder(s).</p>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/uwb_ranging_and_aoa_demo_app_location.png"><img alt="../../../_images/uwb_ranging_and_aoa_demo_app_location.png" src="/docs-assets/_images/uwb_ranging_and_aoa_demo_app_location.png" style="width: 98%;"></a>
</div></blockquote>
</li>
<li><p>The Responder device(s) can be unplugged from the PC if powered by a battery. That will allow moving the Responder freely for evaluation purposes. The device will need to be re-plugged into the PC using the <a class="reference internal" href="/docs/en/udk/udk-start/device-hw-interfaces#hardware-interface"><span class="std std-ref">USB-C Data Port 1</span></a> to start the session again.</p></li>
</ol>
<blockquote>
<div><img alt="../../../_images/leaps-connect-usb-port1.gif" class="align-center" src="/docs-assets/_images/leaps-connect-usb-port1.gif">
</div></blockquote>
<ol class="arabic simple" start="8">
<li><p>The UWB Ranging &amp; AoA Demo App offers a wide range of useful options for evaluation including</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>Real-Time Location displaying distance, angle and X-Y position.</p></li>
<li><p>Trend Over Time displaying in real-time distance and angle values.</p></li>
<li><p>Locate My Device displaying direction from the Initiator to the selected Responder.</p></li>
<li><p>Geofencing</p></li>
<li><p>Floorplan</p></li>
<li><p>Grid</p></li>
<li><p>Logging</p></li>
</ul>
</div></blockquote>
<p>Please refer to the <a class="reference internal" href="/docs/en/udk/udk-start/partner-application-aoa-app#anchor-ranging-aoa"><span class="std std-ref">UWB Ranging &amp; AoA Demo App</span></a> for more details.</p>
</div>
<input id="sd-tab-item-1" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-1">
Advanced</label><div class="sd-tab-content docutils">
<p><strong>Advanced setup</strong></p>
<p>Get ready for the advanced setup! We’ll tap into the terminal’s power to help you configure your device like a pro. Just follow these steps and you’ll be all set.</p>
<ol class="arabic simple">
<li><p>Use a USB-C Data Cable to connect the <a class="reference internal" href="/docs/en/udk/udk-start/device-hw-interfaces#hardware-interface"><span class="std std-ref">USB-C Data Port 1</span></a> or <a class="reference internal" href="/docs/en/udk/udk-start/device-hw-interfaces#hardware-interface"><span class="std std-ref">USB-C Data Port 2</span></a> of devices to your PC.</p></li>
</ol>
<blockquote>
<div><img alt="../../../_images/leaps-connect-usb-port1.gif" class="align-center" src="/docs-assets/_images/leaps-connect-usb-port1.gif">
</div></blockquote>
<ol class="arabic simple" start="2">
<li><p>Connect to a serial port using your desired terminal application, such as Putty, Teraterm, Minicom, or your favorite terminal application. We need to configure the baud rate to <span class="red-text">115200</span>.</p></li>
</ol>
<blockquote>
<div><p>For example use Minicom, on Ubuntu (Linux):</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">minicom</span> <span class="o">-</span><span class="n">b</span> <span class="mi">115200</span> <span class="o">-</span><span class="n">D</span> <span class="o">/</span><span class="n">dev</span><span class="o">/</span><span class="n">ttyACM0</span>
</pre></div>
</div>
</div></blockquote>
<ol class="arabic simple" start="3">
<li><p>Press <span class="red-text">double enter</span> on the shell console to access the command line control system</p></li>
</ol>
<blockquote>
<div><p>For example open <span class="red-text">/dev/ttyACM0</span> and press <span class="red-text">double enter</span>, on Ubuntu (Linux):</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>minicom -b 115200 -D /dev/ttyACM0

  Welcome to minicom 2.7.1

  OPTIONS: I18n
  Compiled on Dec 23 2019, 02:06:26.
  Port /dev/ttyACM0, 16:02:57

  Press CTRL-A Z for help on special keys



  Low Energy Accurate Positioning System

  FOR DEMO PURPOSE ONLY, NOT FOR SALE.

  Copyright :  2016-2023 LEAPS
  License   :  Please visit https://www.leapslabs.com/leaps-rtls-license
  Compiled  :  Jan  6 2024 09:38:07 (v0.15.0-ab84fb)

  Help      :  ? or help

  leaps&gt;
</pre></div>
</div>
</div></blockquote>
<ol class="arabic simple" start="4">
<li><p>Use the command <a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/fira#fuci"><span class="std std-ref">fuci</span></a> to update FiRa UCI mode.</p></li>
</ol>
<blockquote>
<div><div class="highlight-default notranslate"><div class="highlight"><pre><span></span>Low Energy Accurate Positioning System

FOR DEMO PURPOSE ONLY, NOT FOR SALE.

Copyright :  2016-2023 LEAPS
License   :  Please visit https://www.leapslabs.com/leaps-rtls-license
Compiled  :  Jan  6 2024 09:38:07 (v0.15.0-ab84fb)

Help      :  ? or help

leaps&gt;
leaps&gt; fuci
</pre></div>
</div>
<p>Please check visually that the <span class="green-text">GREEN LED</span> blinks when the device starts.</p>
<img alt="../../../_images/fuci-command.gif" class="align-center" src="/docs-assets/_images/fuci-command.gif">
</div></blockquote>
<ol class="arabic simple" start="5">
<li><p>Now successfully configured <span class="red-text">Qorvo UCI mode</span> Refer to the following steps on <a class="reference internal" href="#anchor-lc"><span class="std std-ref">Quick Start</span></a>.</p></li>
</ol>
</div>
<input id="sd-tab-item-2" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-2">
Troubleshooting</label><div class="sd-tab-content docutils">
<ol class="arabic">
<li><p>When Bluetooth Low Energy (BLE) and the LED are both off, users may erroneously perceive the board as non-functional. In this scenario, the only recourse for the user is to initiate a Factory Reset (<a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/sys#frst"><span class="std std-ref">frst</span></a>) command.</p></li>
<li><p>Here are some tips for fixing some issues related to the installation process.</p>
<ul class="simple">
<li><p>Please check the version. We recommend you use the latest official version.</p></li>
<li><p>Use the <span class="red-text">Reset devices to default</span> feature in Demo Selector on the <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> when you don’t know the current state of the devices. Refer to the following GIF Image.</p></li>
</ul>
<img alt="../../../_images/reset-devices-to-defaul-x2.gif" class="align-center" src="/docs-assets/_images/reset-devices-to-defaul-x2.gif">
</li>
</ol>
</div>
</div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<ul class="simple">
<li><p>For any comments or questions about our products, we encourage you to visit our <a class="reference external" href="https://forum.leapslabs.com">LEAPS Forum</a>.</p></li>
<li><p>For detail of known limitation and issue list, please refer section <a class="reference internal" href="/docs/en/udk/release#udk-releases"><span class="std std-ref">Releases</span></a></p></li>
</ul>
</div>
</div>


           </div>
