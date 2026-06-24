---
title: "Infrastructure-less proximity Demo"
lang: en
slug: "udk/udk-start/infrastructure-less-proximity-demo"
section: "udk"
sourceUrl: "https://docs.leapslabs.com/udk/udk-start/infrastructure-less-proximity-demo/"
order: 108
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="infrastructure-less-proximity-demo">
<span id="anchor-ilp"></span><h1>Infrastructure-less proximity Demo</h1>
<a class="reference internal image-reference" href="../../../_images/infrastructure-less_proximity_demo.png"><img alt="../../../_images/infrastructure-less_proximity_demo.png" class="align-right" src="/docs-assets/_images/infrastructure-less_proximity_demo.png" style="width: 180.0px; height: 204.9px;"></a>
<p><strong>Prepare for setup</strong></p>
<ol class="arabic simple">
<li><p><a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> application installed.</p></li>
<li><p>At least two LC14 or LC13 devices.</p></li>
<li><p>Batteries or USB-C cables for powering the devices.</p></li>
<li><p><em>Optional: Putty, Teraterm, minicom or your favorite terminal application installed on your computer.</em></p></li>
</ol>
<p><strong>Setup time:</strong> less than 2 minutes</p>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-0" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-0">
Quick Start</label><div class="sd-tab-content docutils">
<p><strong>Overview</strong></p>
<p>This demo demonstrates infrastructure-less proximity detection between the nodes based on <span class="red-text">Two Way Ranging (TWR)</span> measurement technique. Alarm is triggered by every node when nodes are in close proximity. The alarm uses LED, haptic motor or buzzer the threshold is configurable.</p>
<p><strong>Typical applications</strong>: Collision avoidance, social distancing, swarm coordination.</p>
<p><strong>Setup instructions</strong></p>
<ol class="arabic simple">
<li><p>Power <span class="red-text">ON</span> the devices.</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>The devices will function as independent Tags using Bluetooth to discover the surrounding devices and using UWB to measure distances to the discovered devices.</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="2">
<li><p>Configure using the Demo Selector in the <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a>:</p></li>
</ol>
<blockquote>
<div><p>2.1. Open the LEAPS Manager and select the <span class="red-text">Demo Selector</span> from the main page.</p>
<p>2.2. Select the <span class="red-text">Infrastructure-less Proximity</span>.</p>
<p>2.3. A list of discovered devices via Bluetooth will appear on the list. Swipe down to update the list if needed.</p>
<p>2.4. Select the devices that will be used for the demo. The <span class="red-text">nodes</span> on the top side indicate the amount of devices needed for the demo.</p>
<p>2.5. Press <span class="red-text">SAVE</span> to configure the device(s) into the LEAPS RTLS mode, Tag-Mesh networking profile.</p>
<p>2.6. Please check visually that the <span class="red-text">RED LED</span> blinks when the device starts.</p>
<img alt="../../../_images/infrastructure-less-proximity-demo.gif" class="align-center" src="/docs-assets/_images/infrastructure-less-proximity-demo.gif">
</div></blockquote>
<ol class="arabic simple" start="3">
<li><p>The devices are configured for the <a class="reference internal" href="#anchor-ilp"><span class="std std-ref">Infrastructure-less proximity Demo</span></a>.</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>By default, when the devices come within 2.5 meters of each other, an alarm will activate (indicated by a RED LED and buzzer). The intensity of the alarm will increase as the devices get closer.</p></li>
<li><p>Initially, the device will emit a low-intensity beep and will blink the RED LED. You can adjust the volume of the beeping using the up (<a class="reference internal" href="/docs/en/udk/udk-start/device-hw-interfaces#uihwinterfaces"><span class="std std-ref">Button B</span></a>) and down buttons (<a class="reference internal" href="/docs/en/udk/udk-start/device-hw-interfaces#uihwinterfaces"><span class="std std-ref">Button A</span></a>), and vibration is also enabled.</p></li>
<li><p>In the demonstration outlined below, the device has two proximity thresholds: the first threshold is set at 0.2 meters, and the second at 0.5 meters.</p></li>
</ul>
<img alt="../../../_images/infrastructure-less-proximity-demo-01.gif" class="align-center" src="/docs-assets/_images/infrastructure-less-proximity-demo-01.gif">
</div></blockquote>
<p>Please refer to the <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> for more details on how to use the application to configure and visualize the nodes and network.</p>
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
<li><p>Connect to a serial port using your desired terminal application, such as Putty, Teraterm, Minicom, or your favortie terminal application. We need to configure the baud rate to <span class="red-text">115200</span>.</p></li>
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
<li><p>Configure each device by following steps:</p></li>
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
<li><p>Use the command <span class="red-text">nps 4</span> to configure <span class="red-text">profile 4 (support Tag Mesh Proximity)</span> for each device.</p></li>
</ol>
<blockquote>
<div><div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ leaps&gt; nps 4
nps: ok
</pre></div>
</div>
</div></blockquote>
<ol class="loweralpha simple" start="3">
<li><p>Use the <span class="red-text">nis</span> command to configure all devices in a network.</p></li>
</ol>
<blockquote>
<div><div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ leaps&gt; nis 0x1234
nis: ok
</pre></div>
</div>
</div></blockquote>
<ol class="loweralpha simple" start="4">
<li><p>Use the command <span class="red-text">nmt</span> to update tag mode.</p></li>
</ol>
<blockquote>
<div><div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ leaps&gt; nmt
</pre></div>
</div>
</div></blockquote>
<p><em>(Then monitor and wait for the device to configure successfully. Then press double enter to access the command line control system again.)</em></p>
<ol class="loweralpha simple" start="5">
<li><p>Use the <span class="red-text">si</span> command to verify configurations such as mode, profile and network.</p></li>
</ol>
<blockquote>
<div><div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">leaps</span><span class="o">&gt;</span> <span class="n">si</span>
<span class="p">[</span><span class="mf">000028.754</span> <span class="n">INF</span><span class="p">]</span> <span class="n">release</span><span class="p">:</span> <span class="n">LEAPS</span> <span class="n">RTLS</span> <span class="n">v0</span><span class="mf">.15.0</span><span class="o">-</span><span class="n">ab84fb</span>
<span class="p">[</span><span class="mf">000028.754</span> <span class="n">INF</span><span class="p">]</span> <span class="n">sys</span><span class="p">:</span> <span class="n">main</span> <span class="n">main_ver</span><span class="o">=</span><span class="n">x02000001</span> <span class="n">cfg_ver</span><span class="o">=</span><span class="n">x01040000</span> <span class="n">batt</span><span class="o">=</span><span class="n">none</span> <span class="n">board</span><span class="o">=</span><span class="n">LC14_B</span>
<span class="p">[</span><span class="mf">000028.754</span> <span class="n">INF</span><span class="p">]</span> <span class="n">uwb</span><span class="p">:</span> <span class="n">ch9</span> <span class="n">prf64</span> <span class="n">plen128</span> <span class="n">pac8</span> <span class="n">txcode9</span> <span class="n">rxcode9</span> <span class="n">baud6800</span> <span class="n">phrmodeext</span> <span class="n">phrratestd</span> <span class="n">sfdtypeieee4a</span> <span class="n">sfdto10</span>
<span class="p">[</span><span class="mf">000028.754</span> <span class="n">INF</span><span class="p">]</span> <span class="n">uwb</span><span class="p">:</span> <span class="n">tx_pwr</span><span class="o">=</span><span class="n">x34</span><span class="o">/</span><span class="n">xC6C6C6C6</span> <span class="n">sts</span><span class="p">:</span><span class="n">shr</span><span class="p">:</span><span class="n">phr</span><span class="p">:</span><span class="n">data</span><span class="o">=</span><span class="mf">22.6</span><span class="p">:</span><span class="mf">22.6</span><span class="p">:</span><span class="mf">22.6</span><span class="p">:</span><span class="mf">22.6</span><span class="p">[</span><span class="n">dB</span><span class="p">]</span> <span class="n">cpl</span><span class="o">=</span><span class="n">FCC</span><span class="o">/</span><span class="n">ETSI</span> <span class="n">pgcnt</span><span class="o">=</span><span class="mi">236</span> <span class="n">temp</span><span class="o">=</span><span class="mi">5</span>
<span class="p">[</span><span class="mf">000028.755</span> <span class="n">INF</span><span class="p">]</span> <span class="n">uwb</span><span class="p">:</span> <span class="n">lna</span><span class="o">=</span><span class="mi">1</span> <span class="n">pa</span><span class="o">=</span><span class="mi">0</span> <span class="n">rf1</span><span class="o">=</span><span class="mi">1</span> <span class="n">rf2</span><span class="o">=</span><span class="mi">0</span> <span class="n">xtaltrim</span><span class="o">=</span><span class="mi">32</span> <span class="n">tx_delay</span><span class="o">=</span><span class="mi">16431</span> <span class="n">rx_delay</span><span class="o">=</span><span class="mi">16431</span>
<span class="p">[</span><span class="mf">000028.755</span> <span class="n">INF</span><span class="p">]</span> <span class="n">uwb</span><span class="p">:</span> <span class="n">panid</span><span class="o">=</span><span class="n">x1234</span> <span class="n">addr</span><span class="o">=</span><span class="n">xDECAED5BC8B1468D</span>
<span class="p">[</span><span class="mf">000028.758</span> <span class="n">INF</span><span class="p">]</span> <span class="n">mode</span><span class="p">:</span> <span class="n">tn</span> <span class="p">(</span><span class="n">act</span><span class="p">,</span><span class="n">twr</span><span class="p">,</span><span class="n">np</span><span class="p">,</span><span class="n">le</span><span class="p">)</span>
<span class="p">[</span><span class="mf">000028.774</span> <span class="n">INF</span><span class="p">]</span> <span class="n">uwbmac</span><span class="p">:</span> <span class="n">connected</span> <span class="n">prof</span><span class="o">=</span><span class="mi">4</span> <span class="p">(</span><span class="n">manual</span><span class="p">)</span>
<span class="p">[</span><span class="mf">000028.774</span> <span class="n">INF</span><span class="p">]</span> <span class="n">uwbmac</span><span class="p">:</span> <span class="n">bh</span> <span class="n">disconnected</span>
<span class="p">[</span><span class="mf">000028.774</span> <span class="n">INF</span><span class="p">]</span> <span class="n">cfg</span><span class="p">:</span> <span class="n">sync</span><span class="o">=</span><span class="mi">0</span> <span class="n">fwup</span><span class="o">=</span><span class="mi">1</span> <span class="n">ble</span><span class="o">=</span><span class="mi">1</span> <span class="n">leds</span><span class="o">=</span><span class="mi">1</span> <span class="n">le</span><span class="o">=</span><span class="mi">1</span> <span class="n">lp</span><span class="o">=</span><span class="mi">0</span> <span class="n">uab</span><span class="o">=</span><span class="mi">1</span> <span class="n">stat_det</span><span class="o">=</span><span class="mi">1</span> <span class="p">(</span><span class="n">sens</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span> <span class="n">mode</span><span class="o">=</span><span class="mi">0</span> <span class="n">upd_rate_norm</span><span class="o">=</span><span class="mi">1</span> <span class="n">upd_D</span>
<span class="p">[</span><span class="mf">000028.802</span> <span class="n">INF</span><span class="p">]</span> <span class="n">enc</span><span class="p">:</span> <span class="n">off</span>
<span class="p">[</span><span class="mf">000028.802</span> <span class="n">INF</span><span class="p">]</span> <span class="n">ble</span><span class="p">:</span> <span class="n">addr</span><span class="o">=</span><span class="n">F3</span><span class="p">:</span><span class="n">D9</span><span class="p">:</span><span class="mi">66</span><span class="p">:</span><span class="mi">75</span><span class="p">:</span><span class="mi">93</span><span class="p">:</span><span class="n">EB</span>
<span class="n">leaps</span><span class="o">&gt;</span>
</pre></div>
</div>
</div></blockquote>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">mode:</span> <span class="pre">tn</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">panid=x1234</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prof=4</span></code></p></li>
</ul>
<ol class="loweralpha simple" start="6">
<li><p>Please check visually that the <span class="red-text">RED LED</span> blinks when the device starts.</p></li>
</ol>
</div></blockquote>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>In this example, we will configure <strong>2 tags</strong>.</p>
</div>
<ol class="arabic simple" start="5">
<li><p>After configuring the device, it will scan all devices via BLE. If the device is within the allowable distance, it will automatically reactivate UWB and measure the distance to each other.</p></li>
</ol>
<blockquote>
<div><p>Use the <span class="red-text">ln</span> command to show all devices. This can be used with all UDK devices.</p>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-3" name="sd-tab-set-1" type="radio">
<label class="sd-tab-label" for="sd-tab-item-3">
Tag 1</label><div class="sd-tab-content docutils">
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ leaps&gt; ln
[000005.713 INF] TN: cnt=2 size=100
[000005.713 INF]   0) id=468D dist=0.40,xDD
[000005.713 INF]   1) id=4F2E dist=0.00,xBD
[000005.713 INF]
</pre></div>
</div>
</div>
<input id="sd-tab-item-4" name="sd-tab-set-1" type="radio">
<label class="sd-tab-label" for="sd-tab-item-4">
Tag 2</label><div class="sd-tab-content docutils">
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ leaps&gt; ln
[000033.319 INF] TN: cnt=2 size=100
[000033.319 INF]   0) id=468D dist=0.00,x00
[000033.320 INF]   1) id=4F2E dist=0.44,x66
[000033.320 INF]
</pre></div>
</div>
</div>
</div>
</div></blockquote>
<ol class="arabic simple" start="6">
<li><p>In the <a class="reference internal" href="#anchor-ilp"><span class="std std-ref">Infrastructure-less proximity Demo</span></a>.</p></li>
</ol>
<blockquote>
<div><ul>
<li><p>By default, when the devices come within 2.5 meters of each other, an alarm will activate (indicated by a RED LED and buzzer). The intensity of the alarm will increase as the devices get closer.</p></li>
<li><p>Initially, the device will emit a low-intensity beep and will blink the RED LED. You can adjust the volume of the beeping using the up (<a class="reference internal" href="/docs/en/udk/udk-start/device-hw-interfaces#uihwinterfaces"><span class="std std-ref">Button B</span></a>) and down buttons (<a class="reference internal" href="/docs/en/udk/udk-start/device-hw-interfaces#uihwinterfaces"><span class="std std-ref">Button A</span></a>), and vibration is also enabled.</p></li>
<li><p>Users can view and configure this distance through 2 commands: <span class="red-text">dacg</span> command and, <span class="red-text">dacs</span> command.</p>
<p>For example, to  view and configure 2 thresholds 0.2 meter and, 0.5 meter. Run the following command:</p>
<blockquote>
<div><ul class="simple">
<li><p>To  view:</p></li>
</ul>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ leaps&gt; dacg
dacg: thold_1=200 thold_2=500 mincon=2 minnocon=2 opt=7
</pre></div>
</div>
<ul class="simple">
<li><p>To  configure:</p></li>
</ul>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ leaps&gt; dacs 200 500 2 2 7
dacs: ok
</pre></div>
</div>
</div></blockquote>
<p>In the GIF Image below, the device is configured with thresholds 1 is 0.2 meter and, thresholds 2 is 0.5 meter.</p>
<img alt="../../../_images/infrastructure-less-proximity-demo-01.gif" class="align-center" src="/docs-assets/_images/infrastructure-less-proximity-demo-01.gif">
</li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="7">
<li><p>After the configuration, you can open the shell console for the Tag and view the Tag position using the <span class="red-text">les</span> command.</p></li>
</ol>
<blockquote>
<div><div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ leaps&gt; les
  leaps&gt; POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.54
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.57
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.58
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.59
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.51
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.47
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.43
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.40
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.35
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.32
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.31
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.29
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.27
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.22
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.19
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.16
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.14
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.12
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.09
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.08
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.05
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.09
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.11
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.13
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.15
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.17
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.19
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.21
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.23
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.42
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.51
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.56
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.60
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.62
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.64
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.67
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.69
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.71
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.73
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.73
</pre></div>
</div>
</div></blockquote>
<p>Now the system has been successfully set up and configured the system. Enjoy using it!</p>
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
<div class="admonition caution">
<p class="admonition-title">Caution</p>
<p><strong>Related to Profile 4 (support Tag Mesh Proximity)</strong></p>
<ul class="simple">
<li><p>When the device is in Anchor or Initiator mode, users must not switch to profile 4 (support Tag Mesh Proximity).</p></li>
<li><p>The configured Update Rate value must be limited to the range x1 to x10.</p></li>
</ul>
</div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<ul class="simple">
<li><p>The distance thresholds are configurable via the API.</p></li>
<li><p>For any comments or questions about our products, we encourage you to visit our <a class="reference external" href="https://forum.leapslabs.com">LEAPS Forum</a>.</p></li>
<li><p>For detail of known limitation and issue list, please refer section <a class="reference internal" href="/docs/en/udk/release#udk-releases"><span class="std std-ref">Releases</span></a>.</p></li>
</ul>
</div>
</div>


           </div>
