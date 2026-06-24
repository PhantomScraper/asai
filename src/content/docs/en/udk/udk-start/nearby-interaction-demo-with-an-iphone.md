---
title: "Nearby Interaction Demo with an iPhone"
lang: en
slug: "udk/udk-start/nearby-interaction-demo-with-an-iphone"
section: "udk"
sourceUrl: "https://docs.leapslabs.com/udk/udk-start/nearby-interaction-demo-with-an-iphone/"
order: 107
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="nearby-interaction-demo-with-an-iphone">
<span id="anchor-ni"></span><h1>Nearby Interaction Demo with an iPhone</h1>
<a class="reference internal image-reference" href="../../../_images/nearby_interaction_demo_with_an_iphone.png"><img alt="../../../_images/nearby_interaction_demo_with_an_iphone.png" class="align-right" src="/docs-assets/_images/nearby_interaction_demo_with_an_iphone.png" style="width: 252.00000000000003px; height: 211.26000000000002px;"></a>
<p><strong>Prepare for setup</strong></p>
<ol class="arabic simple">
<li><p><a class="reference internal" href="/docs/en/udk/udk-start/partner-application-nearby-interaction#anchor-ni-app"><span class="std std-ref">Qorvo Nearby Interaction</span></a> (foreground mode) or <a class="reference internal" href="/docs/en/udk/udk-start/partner-application-nearby-interaction-background#anchor-nib-app"><span class="std std-ref">Qorvo NI Background</span></a> application installed on the iPhone (model: iPhone 11, 12 &amp; 13).</p></li>
<li><p>At least one LC14 (white) device.</p></li>
<li><p><em>Optional:</em> <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> <em>application installed.</em></p></li>
<li><p><em>Optional: batteries for the devices.</em></p></li>
</ol>
<p><strong>Setup time:</strong> less than 5 minutes</p>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-0" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-0">
Quick Start</label><div class="sd-tab-content docutils">
<p><strong>Overview</strong></p>
<p>This setup demonstrates <span class="red-text">Nearby Interaction</span> and <span class="red-text">FiRa compatibility</span> with a smartphone. Distance and angle measurement shows the accessory’s direction in the smartphone application.</p>
<p><strong>Typical applications</strong>: Find my things, follow me, smart remote control, access control.</p>
<p><strong>Setup instructions</strong></p>
<ol class="arabic simple">
<li><p>Download and install the following application on iPhone.</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p><a class="reference internal" href="/docs/en/udk/udk-start/partner-application-nearby-interaction#anchor-ni-app"><span class="std std-ref">Qorvo Nearby Interaction</span></a> application (foreground mode).</p></li>
<li><p><a class="reference internal" href="/docs/en/udk/udk-start/partner-application-nearby-interaction-background#anchor-nib-app"><span class="std std-ref">Qorvo NI Background</span></a> application (background mode).</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="2">
<li><p>Power <span class="red-text">ON</span> one or more LC14 (white) devices.</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>The LC14(s) will function as an accessory in the QNI (Qorvo Nearby Interaction) demo.</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="3">
<li><p>Configure the device into the <span class="red-text">QNI mode</span> using one of the following options:</p></li>
</ol>
<blockquote>
<div><ol class="upperalpha simple">
<li><p>Configure the device using the button.</p></li>
</ol>
<blockquote>
<div><p>3.1. Press and hold the <a class="reference internal" href="/docs/en/udk/udk-start/device-hw-interfaces#uihwinterfaces"><span class="std std-ref">Button B</span></a> until you hear a beep sound and the <span class="blue-text">BLUE LED</span> blinks.</p>
<p>3.2. If a <span class="red-text">RED</span> or <span class="green-text">GREEN</span> color appears, please repeat step a.</p>
<p>3.3. When the device blinks <span class="blue-text">BLUE LED</span> after the beep sound, the device is configured in the <span class="red-text">QNI mode</span>.</p>
<img alt="../../../_images/leaps-config-to-qorvo-ni-mode.gif" class="align-center" src="/docs-assets/_images/leaps-config-to-qorvo-ni-mode.gif">
</div></blockquote>
<ol class="upperalpha simple" start="2">
<li><p>Configure using the demo selector in the <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a>:.</p></li>
</ol>
<blockquote>
<div><p>3.1. Open the <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> and select  the <span class="red-text">Demo Selector</span> from the main page.</p>
<p>3.2. Select the <span class="red-text">Nearby Interaction with an iPhone</span>.</p>
<p>3.3. A list of discovered devices via Bluetooth will appear on the list. Swipe down to update the list if needed.</p>
<p>3.4. Select the devices that will be used for the QNI demo. The <span class="red-text">Required devices</span> on the top side indicate the amount of devices needed for the demo.</p>
<p>3.5. Press the <span class="red-text">SAVE</span> to configure the device(s) into the <span class="red-text">QNI mode</span>.</p>
<p>3.6. Please check visually that the <span class="blue-text">BLUE LED</span> blinks when the device starts.</p>
<img alt="../../../_images/qorvo-nearby-interaction.gif" class="align-center" src="/docs-assets/_images/qorvo-nearby-interaction.gif">
</div></blockquote>
</div></blockquote>
<ol class="arabic simple" start="4">
<li><p>Open the <span class="red-text">Qorvo Nearby Interaction</span> or <span class="red-text">Qorvo NI Background</span> application on your iPhone.</p></li>
</ol>
<blockquote>
<div><ul>
<li><p>Immediately after opening the Qorvo Nearby Interaction application, it will scan for nearby accessories using the QNI BLE service.</p></li>
<li><p>When a QNI accessory is found and added to the list. Please <span class="red-text">select and connect</span> to the accessory that you want to start the Nearby Interaction with. Multiple connections are supported.</p>
<img alt="../../../_images/nearby-interaction-demo.gif" class="align-center" src="/docs-assets/_images/nearby-interaction-demo.gif">
</li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="5">
<li><p><span class="red-text">Nearby Interaction Background mode</span> requires the accessory to be paired with the iPhone device.</p></li>
</ol>
<blockquote>
<div><ul>
<li><p>When connecting with a device for the first time and, when the application starts a NI session for the first time it will request user’s approval to use the Nearby Interaction.</p></li>
<li><p>Once the accessory is paired with the iPhone, no more pairing and permission access is required during future interaction between the accessory and the iPhone.</p>
<a class="reference internal image-reference" href="../../../_images/qorvo_ni_pair_request_demo.png"><img alt="../../../_images/qorvo_ni_pair_request_demo.png" src="/docs-assets/_images/qorvo_ni_pair_request_demo.png" style="width: 49%;"></a>
<a class="reference internal image-reference" href="../../../_images/qorvo_ni_background_pair_request_demo.jpg"><img alt="../../../_images/qorvo_ni_background_pair_request_demo.jpg" src="/docs-assets/_images/qorvo_ni_background_pair_request_demo.jpg" style="width: 49%;"></a>
</li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="6">
<li><p>The iPhone will start ranging with the accessory and display the measured distances between the iPhone and the accessory after every ranging round.</p></li>
</ol>
<blockquote>
<div><ul>
<li><p>In the case of the <span class="red-text">Qorvo NI Background</span> application, which uses the <span class="red-text">NI Background mode</span>, the update rate is lower, 1/3 compared to the NI Foreground mode. The ranging would happen in the background even when the display is turned off on the iPhone.</p></li>
<li><p>In the case of the <span class="red-text">Qorvo Nearby Interaction</span> application, which uses the <span class="red-text">NI Foreground mode</span>, will also display the angle and direction from the iPhone to the accessory. The measured values are from the iPhone perspective. As you change the device’s orientation, the application can also provide an augmented view to locate the accessory using the iPhone camera and display.</p>
<a class="reference internal image-reference" href="../../../_images/qorvo_nearby_interaction_application_example.png"><img alt="../../../_images/qorvo_nearby_interaction_application_example.png" src="/docs-assets/_images/qorvo_nearby_interaction_application_example.png" style="width: 49%;"></a>
<a class="reference internal image-reference" href="../../../_images/qorvo_ni_backgroud_example.jpg"><img alt="../../../_images/qorvo_ni_backgroud_example.jpg" src="/docs-assets/_images/qorvo_ni_backgroud_example.jpg" style="width: 49%;"></a>
</li>
</ul>
</div></blockquote>
<p>Please refer to the <a class="reference internal" href="/docs/en/udk/udk-start/partner-application-nearby-interaction#anchor-ni-app"><span class="std std-ref">Qorvo Nearby Interaction</span></a> or <a class="reference internal" href="/docs/en/udk/udk-start/partner-application-nearby-interaction-background#anchor-nib-app"><span class="std std-ref">Qorvo NI Background</span></a> application for more details.</p>
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
<div><img alt="../../../_images/leaps-connect-usb-port2.gif" class="align-center" src="/docs-assets/_images/leaps-connect-usb-port2.gif">
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
<li><p>Use the command <a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/fira#fniq"><span class="std std-ref">fniq</span></a> to update Nearby Interaction mode.</p></li>
</ol>
<blockquote>
<div><div class="highlight-default notranslate"><div class="highlight"><pre><span></span>Low Energy Accurate Positioning System

FOR DEMO PURPOSE ONLY, NOT FOR SALE.

Copyright :  2016-2023 LEAPS
License   :  Please visit https://www.leapslabs.com/leaps-rtls-license
Compiled  :  Jan  6 2024 09:38:07 (v0.15.0-ab84fb)

Help      :  ? or help

leaps&gt;
leaps&gt; fniq
</pre></div>
</div>
<p>At that time, please check visually that the <span class="blue-text">BLUE LED</span> blinks when the device starts.</p>
<img alt="../../../_images/fniq-command.gif" class="align-center" src="/docs-assets/_images/fniq-command.gif">
</div></blockquote>
<ol class="arabic simple" start="5">
<li><p>Now successfully configured <span class="red-text">QNI mode</span>, refer to the next steps on <a class="reference internal" href="#anchor-ni"><span class="std std-ref">Quick Start</span></a>.</p></li>
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
<li><p>For detail of known limitation and issue list, please refer section <a class="reference internal" href="/docs/en/udk/release#udk-releases"><span class="std std-ref">Releases</span></a>.</p></li>
</ul>
</div>
</div>


           </div>
