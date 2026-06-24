---
title: "Uplink TDoA RTLS Demo"
lang: en
slug: "udk/udk-start/uplink-tdoa-rtls-demo"
section: "udk"
sourceUrl: "https://docs.leapslabs.com/udk/udk-start/uplink-tdoa-rtls-demo/"
order: 43
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="uplink-tdoa-rtls-demo">
<span id="id1"></span><h1>Uplink TDoA RTLS Demo</h1>
<a class="reference internal image-reference" href="../../../_images/uplink_tdoa_rtls_demo.png"><img alt="../../../_images/uplink_tdoa_rtls_demo.png" class="align-right" src="/docs-assets/_images/uplink_tdoa_rtls_demo.png" style="width: 252.00000000000003px; height: 278.04px;"></a>
<p><strong>Prepare for setup</strong></p>
<ol class="arabic simple">
<li><p><a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> application installed.</p></li>
<li><p>A Raspberry Pi 3B or newer version or a PC for data server and the web application installation.</p></li>
<li><p>At least five LC14 devices.</p></li>
<li><p>Batteries or USB-C cables for powering the devices.</p></li>
<li><p><em>Recommended: clamp or tripod with a camera mount for attachment of the Anchor devices.</em></p></li>
<li><p><em>Optional: Putty, Teraterm, minicom or your favorite terminal application installed on your computer.</em></p></li>
</ol>
<p><strong>Setup time:</strong> less than 5 minutes</p>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-0" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-0">
Quick Start</label><div class="sd-tab-content docutils">
<p><strong>Overview</strong></p>
<p>This setup demonstrates real-time tracking of the Tag with high accuracy using the <span class="red-text">Uplink Time Difference of Arrival (UL-TDoA)</span> technology.</p>
<p><strong>Typical applications</strong>: Asset and people tracking.</p>
<p><strong>Setup instructions</strong></p>
<ol class="arabic simple">
<li><p>Power <span class="red-text">ON</span> the devices.</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>The statically mounted devices will function as Anchors, providing location information to the Tags.</p></li>
<li><p>The moving devices will function as Tags configured in Uplink TDoA measurement mode.</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="2">
<li><p>Configure using the Demo Selector in the <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a>:</p></li>
</ol>
<blockquote>
<div><p>2.1. Open the LEAPS Manager and select the <span class="red-text">Demo Selector</span> from the main page.</p>
<p>2.2. Select the <span class="red-text">Uplink TDoA RTLS</span>.</p>
<p>2.3. A list of discovered devices via Bluetooth will appear on the list. Swipe down to update the list if needed.</p>
<p>2.4. Select the devices that will be used for the demo. The <span class="red-text">anchors</span> and <span class="red-text">tags</span> on the top side indicate the amount of devices needed for the demo.</p>
<p>2.5. Press the <span class="red-text">SAVE</span> to configure the device(s) into the LEAPS RTLS mode, networking <span class="red-text">profile 5 (supports UL-TDoA)</span>.</p>
<p>2.6. A pop-up window Anchor Configuration will appear to offer the options to configure the Anchor’s positions. select the <span class="red-text">Manual</span> or <span class="red-text">Keep current position</span> depending on the need, then Press the <span class="red-text">OK</span>.</p>
<ul class="simple">
<li><p><em>Auto positioning is currently not available for profile 5.</em></p></li>
</ul>
<p>2.7. Please check visually that the <span class="red-text">RED LED</span> blinks when the device starts.</p>
</div></blockquote>
<ol class="arabic simple" start="3">
<li><p>When the devices are configured successfully, the LEAPS Demo Network window will appear with a list of configured nodes.</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p><em>Recommended: Use the alarm feature to identify the device, and move it to the correct physical location.</em></p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="4">
<li><p>Open the <span class="red-text">Grid</span>, located at the top drop-down menu (select <span class="red-text">Network Details</span>), is for visualization of the devices and their positions.</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>Please refer to the <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> for more details on how to use the application to configure and visualize the nodes and network.</p></li>
</ul>
</div></blockquote>
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
<li><p>Press <span class="red-text">Double enter</span> on the shell console to access the command line control system.</p></li>
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

  Copyright :  2016-2024 LEAPS
  License   :  Please visit https://www.leapslabs.com/leaps-rtls-licee
  Compiled  :  Nov  4 2024 12:30:29 (v0.16.4-a916a6

  Help      :  ? or help

  leaps&gt;
</pre></div>
</div>
</div></blockquote>
<ol class="arabic simple" start="4">
<li><p>Configure for each device, do the following steps:</p></li>
</ol>
<blockquote>
<div><ol class="loweralpha simple">
<li><p>Reset devices to default, run the <span class="red-text">frst</span> command. (optional)</p></li>
</ol>
<blockquote>
<div><div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ leaps&gt; frst
frst ok
</pre></div>
</div>
</div></blockquote>
<img alt="../../../_images/reset-command.gif" class="align-center" src="/docs-assets/_images/reset-command.gif">
<p><em>(Monitor and wait for the device to reset successfully. Then press double enter to access the command line control system.)</em></p>
<ol class="loweralpha simple" start="2">
<li><p>Use the command <span class="red-text">nps 5</span> to configure <span class="red-text">profile 5 (supports UL-TDoA)</span> for each device.</p></li>
</ol>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ leaps&gt; nps 5
nps: ok
</pre></div>
</div>
<ol class="loweralpha simple" start="3">
<li><p>Use the <span class="red-text">nis</span> command to configure all devices in a network.</p></li>
</ol>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ leaps&gt; nis 0x1234
nis: ok
</pre></div>
</div>
<ul class="simple">
<li><p><strong>Then, it is neccessary to reset the device to update the configuration</strong>. Use the <span class="red-text">reset</span> command to reset the device.</p></li>
</ul>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ leaps&gt; reset
reset ok
</pre></div>
</div>
</div></blockquote>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>In this example, we will configure an <strong>anchor with enable initiator</strong>, <strong>3 anchors</strong>, and <strong>a tag</strong>.</p>
</div>
<ol class="arabic simple" start="5">
<li><p>Configure the mode for each anchor and tag.</p></li>
</ol>
<blockquote>
<div><ul>
<li><p>To configure an <span class="red-text">anchor with enable initiator</span>, use the command <span class="red-text">nmi</span> to configure a device.</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ leaps&gt; nmi
</pre></div>
</div>
<p><em>Then, the device will reset, and to access the command line control system again, press double enter.</em></p>
</li>
<li><p>To configure <span class="red-text">3 anchors</span>, use the command <span class="red-text">nma</span> to configure 3 devices to anchor mode, but do not enable initiator.</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ leaps&gt; nma
</pre></div>
</div>
<p><em>Then, the device will reset, and to access the command line control system again, press double enter.</em></p>
</li>
<li><p>To configure <span class="red-text">a tag</span>, use the command <span class="red-text">nmt</span> to configure a device to tag mode</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ leaps&gt; nmt
</pre></div>
</div>
<p><em>Then, the device will reset, and to access the command line control system again, press double enter.</em></p>
</li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="6">
<li><p>Configure the clock reference for one of the anchors.</p></li>
</ol>
<blockquote>
<div><ul>
<li><p>At least one anchor is configured.</p></li>
<li><p>To configure an <span class="red-text">anchor with enable clock reference</span>, use the command <span class="red-text">acs cr</span> to configure a device.</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ leaps&gt; acs cr 1
</pre></div>
</div>
</li>
<li><p><strong>Then, it is neccessary to reset the device need to reset the device to update the configuration</strong>. Use the <span class="red-text">reset</span> command to reset the device.</p></li>
</ul>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ leaps&gt; reset
reset ok
</pre></div>
</div>
</div></blockquote>
<ol class="arabic simple" start="7">
<li><p>Configure the actual position for each anchor.</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>To get the position use <span class="red-text">pg</span> command and to set the position use <span class="red-text">ps</span> command for each anchor.</p></li>
<li><p>In this example, we will configure 4 anchors are placed 3 meter apart and arranged in a square shape:</p></li>
</ul>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-3" name="sd-tab-set-1" type="radio">
<label class="sd-tab-label" for="sd-tab-item-3">
Anchor 1 (enable initiator)</label><div class="sd-tab-content docutils">
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">leaps</span><span class="o">&gt;</span> <span class="n">ps</span> <span class="mi">3000</span> <span class="mi">3000</span> <span class="mi">0</span>
<span class="n">ps</span><span class="p">:</span> <span class="n">ok</span>
<span class="n">leaps</span><span class="o">&gt;</span> <span class="n">pg</span>
<span class="n">pg</span><span class="p">:</span> <span class="n">x</span><span class="p">:</span><span class="mi">5000</span> <span class="n">y</span><span class="p">:</span><span class="mi">5000</span> <span class="n">z</span><span class="p">:</span><span class="mi">0</span> <span class="n">qf</span><span class="p">:</span><span class="mi">100</span>
<span class="n">leaps</span><span class="o">&gt;</span>
</pre></div>
</div>
</div>
<input id="sd-tab-item-4" name="sd-tab-set-1" type="radio">
<label class="sd-tab-label" for="sd-tab-item-4">
Anchor 2</label><div class="sd-tab-content docutils">
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">leaps</span><span class="o">&gt;</span> <span class="n">ps</span> <span class="mi">0</span> <span class="mi">0</span> <span class="mi">0</span>
<span class="n">ps</span><span class="p">:</span> <span class="n">ok</span>
<span class="n">leaps</span><span class="o">&gt;</span> <span class="n">pg</span>
<span class="n">pg</span><span class="p">:</span> <span class="n">x</span><span class="p">:</span><span class="mi">0</span> <span class="n">y</span><span class="p">:</span><span class="mi">0</span> <span class="n">z</span><span class="p">:</span><span class="mi">0</span> <span class="n">qf</span><span class="p">:</span><span class="mi">100</span>
<span class="n">leaps</span><span class="o">&gt;</span>
</pre></div>
</div>
</div>
<input id="sd-tab-item-5" name="sd-tab-set-1" type="radio">
<label class="sd-tab-label" for="sd-tab-item-5">
Anchor 3</label><div class="sd-tab-content docutils">
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">leaps</span><span class="o">&gt;</span> <span class="n">ps</span> <span class="mi">3000</span> <span class="mi">0</span> <span class="mi">0</span>
<span class="n">ps</span><span class="p">:</span> <span class="n">ok</span>
<span class="n">leaps</span><span class="o">&gt;</span> <span class="n">pg</span>
<span class="n">pg</span><span class="p">:</span> <span class="n">x</span><span class="p">:</span><span class="mi">3000</span> <span class="n">y</span><span class="p">:</span><span class="mi">0</span> <span class="n">z</span><span class="p">:</span><span class="mi">0</span> <span class="n">qf</span><span class="p">:</span><span class="mi">100</span>
<span class="n">leaps</span><span class="o">&gt;</span>
</pre></div>
</div>
</div>
<input id="sd-tab-item-6" name="sd-tab-set-1" type="radio">
<label class="sd-tab-label" for="sd-tab-item-6">
Anchor 4</label><div class="sd-tab-content docutils">
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">leaps</span><span class="o">&gt;</span> <span class="n">ps</span> <span class="mi">0</span> <span class="mi">3000</span> <span class="mi">0</span>
<span class="n">ps</span><span class="p">:</span> <span class="n">ok</span>
<span class="n">leaps</span><span class="o">&gt;</span> <span class="n">pg</span>
<span class="n">pg</span><span class="p">:</span> <span class="n">x</span><span class="p">:</span><span class="mi">0</span> <span class="n">y</span><span class="p">:</span><span class="mi">3000</span> <span class="n">z</span><span class="p">:</span><span class="mi">0</span> <span class="n">qf</span><span class="p">:</span><span class="mi">100</span>
<span class="n">leaps</span><span class="o">&gt;</span>
</pre></div>
</div>
</div>
</div>
<ul class="simple">
<li><p>After successfully configuring the anchors, move it to the correct physical location 1 meter apart.</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="8">
<li><p>Configuration for each tag allows the use of <span class="red-text">UL-TDoA</span> technology for measurement.</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>To configure, use the <span class="red-text">tcs mode 1</span> command for a tag.</p></li>
</ul>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ leaps&gt; tcs mode 1
tcs: ok
</pre></div>
</div>
<ul class="simple">
<li><p><strong>Then, it is neccessary to reset the device to update the configuration</strong>. Use the <span class="red-text">reset</span> command to reset the device.</p></li>
</ul>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ leaps&gt; reset
reset ok
</pre></div>
</div>
</div></blockquote>
<ol class="arabic simple" start="9">
<li><p>By default <span class="red-text">normal update rate</span> is 0.1s/ 10Hz and <span class="red-text">stationary update rate</span> is 5.0s/ 0.2Hz. To increase speed, use <span class="red-text">urs</span> command.</p></li>
</ol>
<blockquote>
<div><p>For example, configure <span class="red-text">normal update rate</span> to 0.1s/ 10Hz and, <span class="red-text">stationary update rate</span> is 0.1s/ 10Hz. Run the following command:</p>
<blockquote>
<div><div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ leaps&gt; urs 1 1
urs: ok
</pre></div>
</div>
</div></blockquote>
</div></blockquote>
<ol class="arabic simple" start="10">
<li><p>In steps 5, 7 and, 8 can use the <span class="red-text">si</span> command to verify whether the mode, profile, and network configurations are correct. (optional)</p></li>
</ol>
<blockquote>
<div><p>For example on 4 anchors and a tag:</p>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-7" name="sd-tab-set-2" type="radio">
<label class="sd-tab-label" for="sd-tab-item-7">
Anchor 1 (enable initiator)</label><div class="sd-tab-content docutils">
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">mode:</span> <span class="pre">ani</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">panid=x1234</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prof=5</span></code></p></li>
</ul>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>leaps&gt; nps 5
nps: ok
leaps&gt; nis 0x1234
nis: ok
leaps&gt; nmi


Low Energy Accurate Positioning System

FOR DEMO PURPOSE ONLY, NOT FOR SALE.

Copyright :  2016-2024 LEAPS
License   :  Please visit https://www.leapslabs.com/leaps-rtls-licee
Compiled  :  Nov  4 2024 12:30:29 (v0.16.4-a916a6

Help      :  ? or help

leaps&gt;si
[000412.823 INF] release: LEAPS RTLS v0.16.4-a916a6
[000412.824 INF] sys: main main_ver=x02040001 cfg_ver=x01040000 batt=none board=LC14_B
[000412.824 INF] uwb: ch9 prf64 plen128 pac8 txcode9 rxcode9 baud6800 phrmodeext phrratestd sfdtypeieee4a sfdto129 stsmodeoff stslen64 pdoamodem0
[000412.825 INF] uwb: tx_pwr=x34/xD6D6D6D6 sts:shr:phr:data=24.2:24.2:24.2:24.2[dB] cpl=FCC/ETSI pgcnt=232 temp=25
[000412.826 INF] uwb: lna=1 pa=0 rf1=1 rf2=0 xtaltrim=37 tx_delay=16436 rx_delay=16436
[000412.827 INF] uwb: panid=x1234 addr=xDECAD674FD208EAA
[000412.828 INF] mode: ani (act,real)
[000412.851 INF] uwbmac: connected prof=5 (manual)
[000412.851 INF] uwbmac: bh disconnected
[000412.852 INF] cfg: sync=0 fwup=1 ble=1 leds=1 init=1 uab=1 bh=auto bh_stat=off cr=0 upd_rate_stat=30 label=ID8EAA
[000412.852 INF] enc: off
[000412.872 INF] ble: addr=F0:26:43:8B:52:4A
leaps&gt;
</pre></div>
</div>
</div>
<input id="sd-tab-item-8" name="sd-tab-set-2" type="radio">
<label class="sd-tab-label" for="sd-tab-item-8">
Anchor 2</label><div class="sd-tab-content docutils">
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">mode:</span> <span class="pre">an</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">panid=x1234</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prof=5</span></code></p></li>
</ul>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>leaps&gt; nps 5
nps: ok
leaps&gt; nis 0x1234
nis: ok
leaps&gt; nma


Low Energy Accurate Positioning System

FOR DEMO PURPOSE ONLY, NOT FOR SALE.

Copyright :  2016-2024 LEAPS
License   :  Please visit https://www.leapslabs.com/leaps-rtls-licee
Compiled  :  Nov  4 2024 12:30:29 (v0.16.4-a916a6

Help      :  ? or help

leaps&gt;si
[000454.748 INF] release: LEAPS RTLS v0.16.4-a916a6
[000454.749 INF] sys: main main_ver=x02040001 cfg_ver=x01040000 batt=none board=LC14_B
[000454.749 INF] uwb: ch9 prf64 plen128 pac8 txcode9 rxcode9 baud6800 phrmodeext phrratestd sfdtypeieee4a sfdto129 stsmodeoff stslen64 pdoamodem0
[000454.750 INF] uwb: tx_pwr=x34/xCECECECE sts:shr:phr:data=23.4:23.4:23.4:23.4[dB] cpl=FCC/ETSI pgcnt=238 temp=25
[000454.751 INF] uwb: lna=1 pa=0 rf1=1 rf2=0 xtaltrim=32 tx_delay=16426 rx_delay=16426
[000454.752 INF] uwb: panid=x1234 addr=xDECA229121E05886
[000454.753 INF] mode: an (act,-)
[000454.766 INF] uwbmac: connected prof=5 (manual)
[000454.766 INF] uwbmac: bh disconnected
[000454.767 INF] cfg: sync=0 fwup=1 ble=1 leds=1 init=0 uab=1 bh=auto bh_stat=off cr=0 upd_rate_stat=30 label=ID5886
[000454.797 INF] enc: off
[000454.798 INF] ble: addr=FD:3F:4A:2F:BD:F0
leaps&gt;
</pre></div>
</div>
</div>
<input id="sd-tab-item-9" name="sd-tab-set-2" type="radio">
<label class="sd-tab-label" for="sd-tab-item-9">
Anchor 3</label><div class="sd-tab-content docutils">
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">mode:</span> <span class="pre">an</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">panid=x1234</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prof=5</span></code></p></li>
</ul>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>leaps&gt; nps 5
nps: ok
leaps&gt; nis 0x1234
nis: ok
leaps&gt; nma


Low Energy Accurate Positioning System

FOR DEMO PURPOSE ONLY, NOT FOR SALE.

Copyright :  2016-2024 LEAPS
License   :  Please visit https://www.leapslabs.com/leaps-rtls-licee
Compiled  :  Nov  4 2024 12:30:29 (v0.16.4-a916a6

Help      :  ? or help

leaps&gt; si
[000496.390 INF] release: LEAPS RTLS v0.16.4-a916a6
[000496.390 INF] sys: main main_ver=x02040001 cfg_ver=x01040000 batt=none board=LC14_B
[000496.390 INF] uwb: ch9 prf64 plen128 pac8 txcode9 rxcode9 baud6800 phrmodeext phrratestd sfdtypeieee4a sfdto129 stsmodeoff stslen64 pdoamodem0
[000496.391 INF] uwb: tx_pwr=x34/xC6C6C6C6 sts:shr:phr:data=22.6:22.6:22.6:22.6[dB] cpl=FCC/ETSI pgcnt=236 temp=25
[000496.392 INF] uwb: lna=1 pa=0 rf1=1 rf2=0 xtaltrim=32 tx_delay=16431 rx_delay=16431
[000496.393 INF] uwb: panid=x1234 addr=xDECAED5BC8B1468D
[000496.394 INF] mode: an (act,-)
[000496.413 INF] uwbmac: connected prof=5 (manual)
[000496.414 INF] uwbmac: bh disconnected
[000496.414 INF] cfg: sync=0 fwup=1 ble=1 leds=1 init=0 uab=1 bh=auto bh_stat=off cr=0 upd_rate_stat=30 label=ID468D
[000496.438 INF] enc: off
[000496.439 INF] ble: addr=F3:D9:66:75:93:EB
leaps&gt;
</pre></div>
</div>
</div>
<input id="sd-tab-item-10" name="sd-tab-set-2" type="radio">
<label class="sd-tab-label" for="sd-tab-item-10">
Anchor 4</label><div class="sd-tab-content docutils">
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">mode:</span> <span class="pre">an</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">panid=x1234</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prof=5</span></code></p></li>
</ul>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>leaps&gt; nps 5
nps: ok
leaps&gt; nis 0x1234
nis: ok
leaps&gt; nma


Low Energy Accurate Positioning System

FOR DEMO PURPOSE ONLY, NOT FOR SALE.

Copyright :  2016-2024 LEAPS
License   :  Please visit https://www.leapslabs.com/leaps-rtls-licee
Compiled  :  Nov  4 2024 12:30:29 (v0.16.4-a916a6

Help      :  ? or help

leaps&gt; si
[000535.583 INF] release: LEAPS RTLS v0.16.4-a916a6
[000535.583 INF] sys: main main_ver=x02040001 cfg_ver=x01040000 batt=none board=LC14_B
[000535.584 INF] uwb: ch9 prf64 plen128 pac8 txcode9 rxcode9 baud6800 phrmodeext phrratestd sfdtypeieee4a sfdto129 stsmodeoff stslen64 pdoamodem0
[000535.585 INF] uwb: tx_pwr=x34/xEEEEEEEE sts:shr:phr:data=26.5:26.5:26.5:26.5[dB] cpl=FCC/ETSI pgcnt=245 temp=25
[000535.586 INF] uwb: lna=1 pa=0 rf1=1 rf2=0 xtaltrim=32 tx_delay=16436 rx_delay=16436
[000535.587 INF] uwb: panid=x1234 addr=xDECA7A20DFE04F2E
[000535.588 INF] mode: an (act,-)
[000535.599 INF] uwbmac: connected prof=5 (manual)
[000535.599 INF] uwbmac: bh disconnected
[000535.632 INF] cfg: sync=0 fwup=1 ble=1 leds=1 init=0 uab=1 bh=auto bh_stat=off cr=0 upd_rate_stat=30 label=ID4F2E
[000535.632 INF] enc: off
[000535.633 INF] ble: addr=C8:D9:F3:F1:7D:CE
leaps&gt;
</pre></div>
</div>
</div>
<input id="sd-tab-item-11" name="sd-tab-set-2" type="radio">
<label class="sd-tab-label" for="sd-tab-item-11">
Tag</label><div class="sd-tab-content docutils">
<ul class="simple">
<li><p>By default configuration, the device will be in <span class="red-text">TWR mode</span>. If it was in another mode, we would use the <span class="red-text">tcs mode 0</span> command.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mode:</span> <span class="pre">tn</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">panid=x1234</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prof=2</span></code></p></li>
</ul>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>leaps&gt; nps 2
nps: ok
leaps&gt; nis 0x1234
nis: ok
leaps&gt; nmt


Low Energy Accurate Positioning System

FOR DEMO PURPOSE ONLY, NOT FOR SALE.

Copyright :  2016-2024 LEAPS
License   :  Please visit https://www.leapslabs.com/leaps-rtls-licee
Compiled  :  Nov  4 2024 12:30:29 (v0.16.4-a916a6

Help      :  ? or help

leaps&gt; urs 1 1
urs: ok
leaps&gt; si
[000248.294 INF] release: LEAPS RTLS v0.16.4-a916a6
[000248.294 INF] sys: main main_ver=x02040001 cfg_ver=x01040000 batt=none board=LC13_B
[000248.294 INF] uwb: ch9 prf64 plen128 pac8 txcode9 rxcode9 baud6800 phrmodeext phrratestd sfdtypeieee4a sfdto129 stsmodeoff stslen64 pdoamodem0
[000248.295 INF] uwb: tx_pwr=x34/xCDCDCDCD sts:shr:phr:data=21.7:21.7:21.7:21.7[dB] cpl=FCC/ETSI pgcnt=234 temp=25
[000248.295 INF] uwb: lna=1 pa=0 rf1=1 rf2=1 xtaltrim=13 tx_delay=16443 rx_delay=16443
[000248.295 INF] uwb: panid=x1234 addr=xDECA2B16DD209705
[000248.299 INF] mode: tn (act,tdoa,np,le)
[000248.314 INF] uwbmac: disconnected prof=5 (manual)
[000248.314 INF] uwbmac: bh disconnected
[000248.314 INF] cfg: sync=0 fwup=1 ble=1 leds=1 le=1 lp=0 uab=1 stat_det=1 (sens=2) mode=1 upd_rate_norm=1 upd_rate_stat=1 label=ID9705
[000248.342 INF] enc: off
[000248.342 INF] ble: addr=E0:2C:84:68:AD:16
leaps&gt;
</pre></div>
</div>
</div>
</div>
</div></blockquote>
<ol class="arabic simple" start="11">
<li><p>To see a list of anchors in range and connected to the device itself, use the <span class="red-text">la</span> command. (optional)</p></li>
</ol>
<blockquote>
<div><p>For example on an anchor 1 (enable initiator):</p>
<blockquote>
<div><div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">leaps</span><span class="o">&gt;</span> <span class="n">la</span>
<span class="p">[</span><span class="mf">000414.009</span> <span class="n">INF</span><span class="p">]</span> <span class="n">AN</span><span class="p">:</span> <span class="n">cnt</span><span class="o">=</span><span class="mi">4</span> <span class="n">seq</span><span class="o">=</span><span class="n">x03</span>
<span class="p">[</span><span class="mf">000414.009</span> <span class="n">INF</span><span class="p">]</span>     <span class="mi">0</span><span class="p">)</span> <span class="nb">id</span><span class="o">=</span><span class="mi">8</span><span class="n">EAA</span> <span class="n">seat</span><span class="o">=</span><span class="mi">0</span> <span class="n">clk_lvl</span><span class="o">=</span><span class="mi">0</span> <span class="n">seens</span><span class="o">=</span><span class="mi">0</span> <span class="n">rssi</span><span class="o">=-</span><span class="mi">127</span> <span class="n">cl</span><span class="o">=</span><span class="mi">00000039</span> <span class="n">nbr</span><span class="o">=</span><span class="mi">00000039</span> <span class="n">pos</span><span class="o">=</span><span class="mf">3.00</span><span class="p">:</span><span class="mf">3.00</span><span class="p">:</span><span class="mf">0.00</span>
<span class="p">[</span><span class="mf">000414.010</span> <span class="n">INF</span><span class="p">]</span>     <span class="mi">1</span><span class="p">)</span> <span class="nb">id</span><span class="o">=</span><span class="mi">4</span><span class="n">F2E</span> <span class="n">seat</span><span class="o">=</span><span class="mi">4</span> <span class="n">clk_lvl</span><span class="o">=</span><span class="mi">1</span> <span class="n">seens</span><span class="o">=</span><span class="mi">212</span> <span class="n">rssi</span><span class="o">=-</span><span class="mi">127</span> <span class="n">cl</span><span class="o">=</span><span class="mi">00000039</span> <span class="n">nbr</span><span class="o">=</span><span class="mi">00000000</span> <span class="n">pos</span><span class="o">=</span><span class="mf">0.00</span><span class="p">:</span><span class="mf">3.00</span><span class="p">:</span><span class="mf">0.00</span>
<span class="p">[</span><span class="mf">000414.011</span> <span class="n">INF</span><span class="p">]</span>     <span class="mi">2</span><span class="p">)</span> <span class="nb">id</span><span class="o">=</span><span class="mi">5886</span> <span class="n">seat</span><span class="o">=</span><span class="mi">5</span> <span class="n">clk_lvl</span><span class="o">=</span><span class="mi">1</span> <span class="n">seens</span><span class="o">=</span><span class="mi">178</span> <span class="n">rssi</span><span class="o">=-</span><span class="mi">127</span> <span class="n">cl</span><span class="o">=</span><span class="mi">00000039</span> <span class="n">nbr</span><span class="o">=</span><span class="mi">00000000</span> <span class="n">pos</span><span class="o">=</span><span class="mf">3.00</span><span class="p">:</span><span class="mf">0.00</span><span class="p">:</span><span class="mf">0.00</span>
<span class="p">[</span><span class="mf">000414.012</span> <span class="n">INF</span><span class="p">]</span>     <span class="mi">3</span><span class="p">)</span> <span class="nb">id</span><span class="o">=</span><span class="mi">468</span><span class="n">D</span> <span class="n">seat</span><span class="o">=</span><span class="mi">3</span> <span class="n">clk_lvl</span><span class="o">=</span><span class="mi">1</span> <span class="n">seens</span><span class="o">=</span><span class="mi">145</span> <span class="n">rssi</span><span class="o">=-</span><span class="mi">127</span> <span class="n">cl</span><span class="o">=</span><span class="mi">00000039</span> <span class="n">nbr</span><span class="o">=</span><span class="mi">00000000</span> <span class="n">pos</span><span class="o">=</span><span class="mf">0.00</span><span class="p">:</span><span class="mf">0.00</span><span class="p">:</span><span class="mf">0.00</span>
<span class="p">[</span><span class="mf">000414.012</span> <span class="n">INF</span><span class="p">]</span>
<span class="n">leaps</span><span class="o">&gt;</span>
</pre></div>
</div>
</div></blockquote>
</div></blockquote>
<ol class="arabic" start="12">
<li><p>After completing all configuration. We can use the <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a>, to visualization of the devices and their positions.</p>
<a class="reference internal image-reference" href="../../../_images/twrrtlsanddatatelemetrydemo-advanced-01.jpeg"><img alt="../../../_images/twrrtlsanddatatelemetrydemo-advanced-01.jpeg" src="/docs-assets/_images/twrrtlsanddatatelemetrydemo-advanced-01.jpeg" style="width: 32%;"></a>
<a class="reference internal image-reference" href="../../../_images/twrrtlsanddatatelemetrydemo-advanced-02.jpeg"><img alt="../../../_images/twrrtlsanddatatelemetrydemo-advanced-02.jpeg" src="/docs-assets/_images/twrrtlsanddatatelemetrydemo-advanced-02.jpeg" style="width: 32%;"></a>
<a class="reference internal image-reference" href="../../../_images/twrrtlsanddatatelemetrydemo-advanced-03.jpeg"><img alt="../../../_images/twrrtlsanddatatelemetrydemo-advanced-03.jpeg" src="/docs-assets/_images/twrrtlsanddatatelemetrydemo-advanced-03.jpeg" style="width: 32%;"></a>
</li>
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
<p><strong>Data flow</strong>: When the tag blinks, the anchors receive blinks and send the TX/RX timestamps of blink to Leaps server via Leaps Gateway. Leaps server uses the timestamps collected from Anchors to calculate Tag’s position and publish the position to MQTT broker.</p>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/uplink_tdoa_rtls_demo.png"><img alt="../../../_images/uplink_tdoa_rtls_demo.png" class="align-right" src="/docs-assets/_images/uplink_tdoa_rtls_demo.png" style="width: 360.0px; height: 397.20000000000005px;"></a>
</div></blockquote>
<p><strong>Infrastructure setup</strong></p>
<blockquote>
<div><ol class="arabic simple">
<li><p>Device Configuration</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>As above, use LM in Quick Start or Shell in Advanced to configure the devices.</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="2">
<li><p>Setting Up Raspberry Pis</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>Install all Raspberry Pis using the LEAPS-RPI-IMAGE.</p></li>
<li><p>Each corresponding anchor connects to a Raspberry Pi, so at least 4 Raspberry Pis are required.</p></li>
<li><p>The image includes the setup and configuration for the <code class="docutils literal notranslate"><span class="pre">LEAPS</span> <span class="pre">Gateway</span></code>, <code class="docutils literal notranslate"><span class="pre">LEAPS</span> <span class="pre">Server</span></code>, <code class="docutils literal notranslate"><span class="pre">LEAPS</span> <span class="pre">Center</span></code>, and <code class="docutils literal notranslate"><span class="pre">Mosquitto</span> <span class="pre">MQTT</span> <span class="pre">Broker</span></code>.</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="3">
<li><p>Connecting Raspberry Pis</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>Connect all Raspberry Pis to the Router to ensure they are on the same LAN.</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="4">
<li><p>LEAPS Server Setup</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>Choose any Raspberry Pi to run the <code class="docutils literal notranslate"><span class="pre">LEAPS</span> <span class="pre">Server</span></code> and check its IP address. To obtain the IP address, use the ifconfig command.</p></li>
</ul>
<img alt="../../../_images/uplinktdoartlsdemo-ip-address.png" class="align-center" src="/docs-assets/_images/uplinktdoartlsdemo-ip-address.png">
</div></blockquote>
<ol class="arabic simple" start="5">
<li><p>Updating Configuration</p></li>
</ol>
<blockquote>
<div><ul>
<li><p>Using the IP address of the chosen Raspberry Pi, update the <code class="docutils literal notranslate"><span class="pre">leaps-server-host</span></code> configuration in <code class="docutils literal notranslate"><span class="pre">/usr/share/LEAPS-DOCKER-LINUX/leaps-gateway-hub/data/leaps-gateway.conf</span></code> for all LEAPS Gateways on all Raspberry Pis.</p>
<ul class="simple">
<li><p>For example:</p></li>
</ul>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">leaps</span><span class="o">-</span><span class="n">server</span><span class="o">-</span><span class="n">host</span> <span class="o">=</span> <span class="mf">192.168.1.8</span>
</pre></div>
</div>
</li>
</ul>
<img alt="../../../_images/uplinktdoartlsdemo-leaps-gateway.png" class="align-center" src="/docs-assets/_images/uplinktdoartlsdemo-leaps-gateway.png">
<img alt="../../../_images/uplinktdoartlsdemo-leaps-gateway.png" class="align-center" src="/docs-assets/_images/uplinktdoartlsdemo-leaps-gateway.png">
<ul class="simple">
<li><p>Save the configuration and restart the <code class="docutils literal notranslate"><span class="pre">LEAPS</span> <span class="pre">Gateway</span></code> with the following command:</p></li>
</ul>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">sudo</span> <span class="n">docker</span> <span class="n">restart</span> <span class="n">leaps_gateway</span>
</pre></div>
</div>
<ul class="simple">
<li><p>Then, restart the <code class="docutils literal notranslate"><span class="pre">LEAPS</span> <span class="pre">Server</span></code> with the following command:</p></li>
</ul>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">sudo</span> <span class="n">service</span> <span class="n">leaps</span><span class="o">-</span><span class="n">server</span> <span class="n">restart</span>
</pre></div>
</div>
</div></blockquote>
<ol class="arabic simple" start="6">
<li><p>Monitoring the System</p></li>
</ol>
<blockquote>
<div><ul>
<li><p>Once the gateway is ready, monitor the system status using:</p></li>
<li><p>For example:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">mosquitto_sub</span> <span class="o">-</span><span class="n">h</span> <span class="mf">192.168.1.8</span> <span class="o">-</span><span class="n">p</span> <span class="mi">1883</span> <span class="o">-</span><span class="n">t</span> <span class="s1">'#'</span> <span class="o">-</span><span class="n">v</span>
</pre></div>
</div>
</li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="7">
<li><p>Configuring Leaps Center</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>For example: Open a web browser and navigate to: <code class="docutils literal notranslate"><span class="pre">192.168.1.8/2</span></code></p></li>
<li><p>This can be accessed directly on the Raspberry Pi or on a PC connected to the LEAPS-AP network broadcasted by the Raspberry Pi with the password <code class="docutils literal notranslate"><span class="pre">Leaps1234</span></code>.</p></li>
<li><p>If on a LAN network, you can also use another computer’s web browser to access the Raspberry Pi’s IP address.</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="8">
<li><p>Network Configuration</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>In the <code class="docutils literal notranslate"><span class="pre">LEAPS</span> <span class="pre">Center</span></code>, configure the network settings to match the network ID of the gateway board you have connected.</p></li>
</ul>
<img alt="../../../_images/uplinktdoartlsdemo-leaps-center.png" class="align-center" src="/docs-assets/_images/uplinktdoartlsdemo-leaps-center.png">
</div></blockquote>
<p>Now the system has been successfully set up and configured the system. Enjoy using it!</p>
</div></blockquote>
<div class="admonition note">
<p class="admonition-title">Note</p>
<ul class="simple">
<li><p>Refer to the software infrastructure to further explore the power of this demo. Our support includes <a class="reference internal" href="/docs/en/udk/udk-start/infrastructure-docker#leaps-docker"><span class="std std-ref">LEAPS Docker</span></a>, <a class="reference internal" href="/docs/en/udk/udk-start/infrastructure-vmware#leaps-vmware"><span class="std std-ref">LEAPS VMWare</span></a> and, <a class="reference internal" href="/docs/en/udk/udk-start/infrastructure-rpi#leaps-raspberrypi"><span class="std std-ref">LEAPS Raspberry Pi</span></a>.</p></li>
<li><p>For any comments or questions about our products, we encourage you to visit our <a class="reference external" href="https://forum.leapslabs.com">LEAPS Forum</a>.</p></li>
<li><p>For detail of known limitation and issue list, please refer section <a class="reference internal" href="/docs/en/udk/release#udk-releases"><span class="std std-ref">Releases</span></a>.</p></li>
</ul>
</div>
</div>


           </div>
