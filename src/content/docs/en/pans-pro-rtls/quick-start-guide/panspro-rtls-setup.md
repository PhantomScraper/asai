---
title: "PANS PRO Demo"
lang: en
slug: "pans-pro-rtls/quick-start-guide/panspro-rtls-setup"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/pans-pro-rtls/quick-start-guide/panspro-rtls-setup/"
order: 88
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="pans-pro-demo">
<span id="id1"></span><h1>PANS PRO Demo</h1>
<p><strong>Prepare for setup</strong></p>
<img alt="../../../_images/qsg_set_up.png" class="align-center" src="/docs-assets/_images/qsg_set_up.png">
<ol class="arabic simple">
<li><p><a class="reference internal" href="/docs/en/pans-pro-rtls/infrastructure/pans-pro-manager#pans-pro-manager"><span class="std std-ref">PANS PRO Manager</span></a> application installed on an Android device.</p></li>
<li><p><a class="reference internal" href="/docs/en/pans-pro-rtls/infrastructure/leaps-center#pans-pro-center"><span class="std std-ref">LEAPS Center</span></a> application installed on the PC.</p></li>
<li><p>At least four LC4 devices (Anchor Node) and one LC8 device (Tag Node).</p></li>
<li><p>One LC5 device (Gateway Node).</p></li>
<li><p>Batteries or Micro USB cables for powering the devices.</p></li>
<li><p><em>Recommended</em>: clamp or tripod with a camera mount for attachment of the Anchor devices.</p></li>
<li><p><em>Recommended</em>: A Raspberry Pi 3B or newer version or a PC, the data server, and the web application installation.</p></li>
<li><p><em>Optional</em>: Putty, Teraterm, minicom, or your favorite terminal application installed on your computer.</p></li>
</ol>
<p><strong>Setup time:</strong> less than 5 minutes</p>
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-3 sd-row-cols-xs-3 sd-row-cols-sm-3 sd-row-cols-md-3 sd-row-cols-lg-3 docutils">
<div class="sd-col sd-d-flex-row docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm sd-card-hover sd-text-center custom-card docutils">
<div class="sd-card-body docutils">
<a class="reference internal image-reference" href="../../../_images/lc4a_front_view.png"><img alt="../../../_images/lc4a_front_view.png" src="/docs-assets/_images/lc4a_front_view.png" style="width: 131.76px; height: 189.26999999999998px;"></a>
<p class="sd-card-text"><span class="red-text">LC4 device</span></p>
</div>
<a class="sd-stretched-link reference internal" href="/docs/en/pans-pro-rtls/specification/lc4a-specification#lc4a-specification"><span class="std std-ref"></span></a></div>
</div>
<div class="sd-col sd-d-flex-row docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm sd-card-hover sd-text-center custom-card docutils">
<div class="sd-card-body docutils">
<a class="reference internal image-reference" href="../../../_images/lc5.png"><img alt="../../../_images/lc5.png" src="/docs-assets/_images/lc5.png" style="width: 204.8px; height: 184.8px;"></a>
<p class="sd-card-text"><span class="red-text">LC5 device</span></p>
</div>
<a class="sd-stretched-link reference internal" href="/docs/en/pans-pro-rtls/specification/lc5a-specification#lc5a-specification"><span class="std std-ref"></span></a></div>
</div>
<div class="sd-col sd-d-flex-row docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm sd-card-hover sd-text-center custom-card docutils">
<div class="sd-card-body docutils">
<a class="reference internal image-reference" href="../../../_images/lc8.png"><img alt="../../../_images/lc8.png" src="/docs-assets/_images/lc8.png" style="width: 117.2px; height: 182.0px;"></a>
<p class="sd-card-text"><span class="red-text">LC8 device</span></p>
</div>
<a class="sd-stretched-link reference internal" href="/docs/en/pans-pro-rtls/specification/lc8a-specification#lc8a-specification"><span class="std std-ref"></span></a></div>
</div>
</div>
</div>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-0" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-0">
Quick Start with Phone</label><div class="sd-tab-content docutils">
<p><strong>Overview</strong></p>
<p>This setup demonstrates real-time navigation, tracking, and both ways of data telemetry using <span class="red-text">Two Way Ranging (TWR)</span> technology.</p>
<p><strong>Typical applications</strong>: Indoor navigation, asset tracking, and real-time data telemetry supporting uplink and downlink.</p>
<p><strong>Setup instructions</strong></p>
<ol class="arabic">
<li><p>Power ON the devices with already flashed the latest firmware.</p>
<ul class="simple">
<li><p>The statically mounted devices will function as Anchors, providing location information to the Tags.</p></li>
<li><p>The moving devices will function as Tags configured in Two-Way Ranging measurement mode.</p></li>
</ul>
</li>
<li><p>Please refer the detail guideline from the <a class="reference internal" href="/docs/en/pans-pro-rtls/infrastructure/pans-pro-manager#pans-pro-manager"><span class="std std-ref">PANS PRO Manager</span></a> section. Here are quick steps.</p>
<p>2.1. Log in using the username <code class="docutils literal notranslate"><span class="pre">admin</span></code> and the password <code class="docutils literal notranslate"><span class="pre">admin</span></code>.</p>
<p>2.2. Once logged in successfully, click on the <code class="docutils literal notranslate"><span class="pre">Start</span> <span class="pre">Device</span> <span class="pre">Discovery</span></code> function on the homepage.</p>
<p>2.3. Assign the discovered devices to the network. Enter a network name to continue and assign all devices to this network.</p>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/ppm-home-page.jpg"><img alt="../../../_images/ppm-home-page.jpg" src="/docs-assets/_images/ppm-home-page.jpg" style="width: 32%;"></a>
<a class="reference internal image-reference" href="../../../_images/ppm-assign-network6.jpg"><img alt="../../../_images/ppm-assign-network6.jpg" src="/docs-assets/_images/ppm-assign-network6.jpg" style="width: 32%;"></a>
<a class="reference internal image-reference" href="../../../_images/ppm-network-1.jpg"><img alt="../../../_images/ppm-network-1.jpg" src="/docs-assets/_images/ppm-network-1.jpg" style="width: 32%;"></a>
</div></blockquote>
<p>2.4. Configure one of the discovered devices as the Initiator Anchor Node (ANI) and enable Initiator Mode.</p>
<p>2.5. Configure three of the discovered devices as Anchor Nodes (AN) without enabling Initiator Mode.</p>
<p>2.6. With four Anchor Nodes (AN), you can configure the Position manually.</p>
<blockquote>
<div><ul class="simple">
<li><p>Check out the Auto-Positioning feature for easy anchor placement in <a class="reference internal" href="/docs/en/pans-pro-rtls/infrastructure/pans-pro-manager#pans-pro-manager"><span class="std std-ref">PANS PRO Manager</span></a>.</p></li>
</ul>
</div></blockquote>
<p>2.7. Configure one device as a Tag Node (TN) with the default <code class="docutils literal notranslate"><span class="pre">NORMAL</span> <span class="pre">UPDATE</span> <span class="pre">RATE</span></code> and <code class="docutils literal notranslate"><span class="pre">STATIONARY</span> <span class="pre">UPDATE</span> <span class="pre">RATE</span></code>.</p>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/ppm-device-configure-b.jpg"><img alt="../../../_images/ppm-device-configure-b.jpg" src="/docs-assets/_images/ppm-device-configure-b.jpg" style="width: 32%;"></a>
<a class="reference internal image-reference" href="../../../_images/anchor-initiator-node-disable.png"><img alt="../../../_images/anchor-initiator-node-disable.png" src="/docs-assets/_images/anchor-initiator-node-disable.png" style="width: 32%;"></a>
<a class="reference internal image-reference" href="../../../_images/ppm-device-configure-a.jpg"><img alt="../../../_images/ppm-device-configure-a.jpg" src="/docs-assets/_images/ppm-device-configure-a.jpg" style="width: 32%;"></a>
</div></blockquote>
<p>2.8. After completing the discovery and configuration, the network visualization can be displayed in 2D Grid or 3D Grid on the <a class="reference internal" href="/docs/en/pans-pro-rtls/infrastructure/pans-pro-manager#pans-pro-manager"><span class="std std-ref">PANS PRO Manager</span></a> application.</p>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/ppm-grib-2d-0.jpg"><img alt="../../../_images/ppm-grib-2d-0.jpg" src="/docs-assets/_images/ppm-grib-2d-0.jpg" style="width: 40%;"></a>
<a class="reference internal image-reference" href="../../../_images/ppm-grib-3d-0.jpg"><img alt="../../../_images/ppm-grib-3d-0.jpg" src="/docs-assets/_images/ppm-grib-3d-0.jpg" style="width: 40%;"></a>
</div></blockquote>
</li>
</ol>
</div>
<input id="sd-tab-item-1" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-1">
Quick Start with Web</label><div class="sd-tab-content docutils">
<p><strong>Overview</strong></p>
<p>On this section, the guideline will guide how to set up the PANS PRO RTLS network to display on the <a class="reference internal" href="/docs/en/pans-pro-rtls/infrastructure/leaps-center#pans-pro-center"><span class="std std-ref">LEAPS Center</span></a>.
In order to successfully set up the PANS PRO RLTS network, please ensure the essential hardware and software.</p>
<p><strong>Instructions</strong>:</p>
<ol class="arabic">
<li><p>Prepare the Network:</p>
<ul class="simple">
<li><p>Use the configuration via <code class="docutils literal notranslate"><span class="pre">PANS</span> <span class="pre">PRO</span> <span class="pre">Manage</span></code> as described in the <code class="docutils literal notranslate"><span class="pre">Quick</span> <span class="pre">Start</span> <span class="pre">with</span> <span class="pre">Phone</span></code> tab to configure the network.</p></li>
</ul>
</li>
<li><p>Set up the Gateway Board: Use either <code class="docutils literal notranslate"><span class="pre">PANS</span> <span class="pre">PRO</span> <span class="pre">Docker</span></code> or <code class="docutils literal notranslate"><span class="pre">PANS</span> <span class="pre">PRO</span> <span class="pre">Raspberry</span> <span class="pre">Pi</span></code>.</p>
<ul class="simple">
<li><p><cite>Note: Flash the latest firmware if it’s not already available on the board</cite>.</p></li>
</ul>
<p><strong>Gateway Configuration</strong></p>
<div class="line-block">
<div class="line">Configuration can be done by connecting the device via USB and using an on-board shell command.</div>
<div class="line">Press double Enter to enable the shell command mode.</div>
</div>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/advanced_001.png"><img alt="../../../_images/advanced_001.png" class="align-center" src="/docs-assets/_images/advanced_001.png" style="width: 303.40000000000003px; height: 320.0px;"></a>
</div></blockquote>
<p>2.1. UWB Networking Configuration</p>
<blockquote>
<div><ul>
<li><p>Configure network ID</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; nis</span>
<span class="go">usage: nis PANID</span>
</pre></div>
</div>
</div></blockquote>
</li>
<li><p>Configure device to become a Gateway</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; nmg</span>
<span class="go">ok</span>
</pre></div>
</div>
</div></blockquote>
</li>
</ul>
<p>or</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; acs leds 1 uwb 2</span>
<span class="go">ok</span>
</pre></div>
</div>
</div></blockquote>
</div></blockquote>
<p>2.2. Device IP Address Configuration</p>
<blockquote>
<div><p>Default is DHCP (dynamic IP address) so no need to configure unless needed.</p>
<ul>
<li><p>Usage</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; ipv4</span>
<span class="go">usage: ipv4 [static|dynamic] [addr STRING] [mask STRING] [gw STRING]</span>
</pre></div>
</div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>The device will be reset upon a successful configuration.</p>
</div>
</div></blockquote>
</li>
<li><p>Static IP address configuration</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; ipv4 addr 192.168.1.100 static</span>
<span class="go">ipv4 ok(0)</span>
</pre></div>
</div>
</div></blockquote>
</li>
<li><p>Network mask configuration</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; ipv4 mask 255.255.255.0</span>
<span class="go">ipv4 ok(0)</span>
</pre></div>
</div>
</div></blockquote>
</li>
<li><p>Enabling static IP address which has been configured previously</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; ipv4 static</span>
<span class="go">ipv4 ok(0)</span>
</pre></div>
</div>
</div></blockquote>
</li>
<li><p>Enabling DHCP</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; ipv4 dynamic</span>
<span class="go">ipv4 ok(0)</span>
</pre></div>
</div>
</div></blockquote>
</li>
<li><p>Configuring all in one step</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; ipv4 addr 192.168.1.100 mask 255.255.255.0 static ipv4 ok(0)</span>
</pre></div>
</div>
</div></blockquote>
</li>
</ul>
</div></blockquote>
<p>2.3. Configuring LEAPS Server connection</p>
<blockquote>
<div><ul>
<li><p>Usage</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; peer</span>
<span class="go">usage: peer [addr STRING] [port NUM] [tls 0|1]</span>
</pre></div>
</div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>The device will be reset upon a successful configuration.</p>
</div>
</div></blockquote>
</li>
<li><p>Configuring connection with the LEAPS Server at IP address 192.168.200.1 and on port 7777</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; peer addr 192.168.200.1 port 7777 tls 0</span>
<span class="go">peer ok(0)</span>
</pre></div>
</div>
</div></blockquote>
</li>
<li><p>Disable TLS</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; peer tls 0</span>
<span class="go">peer ok(0)</span>
</pre></div>
</div>
</div></blockquote>
</li>
<li><p>Enable TLS</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; peer tls 1</span>
<span class="go">peer ok(0)</span>
</pre></div>
</div>
</div></blockquote>
</li>
<li><p>Combined configuration of LEAS Server host and TLS</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; peer host example.com tls 1</span>
<span class="go">peer ok(0)</span>
</pre></div>
</div>
</div></blockquote>
</li>
<li><p>Correct status of the system when TLS is disabled</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; si</span>
<span class="go">[000081.971 INF] sys: fw1 fw_ver=x01030000 cfg_ver=x00030000</span>
<span class="go">[000081.976 INF] inet: up tls=off addr=192.168.1.100 mask=255.255.255.0 gw=192.168.200.1 (dynamic)</span>
<span class="go">[000081.983 INF] inet: peer=192.168.200.1:7777 (-)</span>
<span class="go">[000081.987 INF] uwb: panid=x0000 addr=xDECA84B1B8544434</span>
<span class="go">[000081.992 INF] uwbmac: connected</span>
<span class="go">[000081.997 INF] mode: gn (act)</span>
<span class="go">[000082.000 INF] cfg: enc=0 ble=1 leds=1 fwup=0 label=ID4434</span>
<span class="go">[000082.005 INF] enc: off (nokey)</span>
<span class="go">[000082.008 INF] gw: connected</span>
</pre></div>
</div>
</div></blockquote>
</li>
<li><p>Correct status of the system when TLS is enabled</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; si</span>
<span class="go">[000027.316 INF] sys: fw1 fw_ver=x01030000 cfg_ver=x00030000</span>
<span class="go">[000027.321 INF] inet: up tls=on addr=192.168.1.100 mask=255.255.255.0 gw=192.168.200.1 (dynamic)</span>
<span class="go">[000027.328 INF] inet: peer=123.123.123.123:7777(server.example.com)</span>
<span class="go">[000027.332 INF] uwb: panid=x0000 addr=xDECA84B1B8544434</span>
<span class="go">[000027.337 INF] uwbmac: connected</span>
<span class="go">[000027.342 INF] mode: gn (act)</span>
<span class="go">[000027.345 INF] cfg: enc=0 ble=1 leds=1 fwup=0 label=ID4434</span>
<span class="go">[000027.350 INF] enc: off (nokey)</span>
<span class="go">[000027.353 INF] gw: connected</span>
</pre></div>
</div>
</div></blockquote>
</li>
</ul>
</div></blockquote>
</li>
<li><p>Open LEAPS Center</p>
<ul class="simple">
<li><p>Launch it via <code class="docutils literal notranslate"><span class="pre">PANS</span> <span class="pre">PRO</span> <span class="pre">Docker</span></code> or <code class="docutils literal notranslate"><span class="pre">PANS</span> <span class="pre">PRO</span> <span class="pre">Raspberry</span> <span class="pre">Pi</span></code>.</p></li>
</ul>
</li>
<li><p>Log In</p>
<ul class="simple">
<li><p>Use the username <code class="docutils literal notranslate"><span class="pre">admin</span></code> and password <code class="docutils literal notranslate"><span class="pre">admin</span></code>.</p></li>
</ul>
<a class="reference internal image-reference" href="../../../_images/leaps_center_login.png"><img alt="../../../_images/leaps_center_login.png" class="align-center" src="/docs-assets/_images/leaps_center_login.png" style="width: 762.8000000000001px; height: 360.0px;"></a>
</li>
<li><p>Select Networks</p>
<ul class="simple">
<li><p>Click on <code class="docutils literal notranslate"><span class="pre">Networks</span></code> in the left navigation menu.</p></li>
</ul>
</li>
<li><p>Add New Network</p>
<ul class="simple">
<li><p>Provide a <strong>Name</strong> and <strong>ID</strong>.</p></li>
<li><p>Select <strong>Protocol Type</strong> as <strong>PANS</strong>.</p></li>
<li><p>Enter the <strong>Host</strong> and <strong>TCP Port</strong>.</p></li>
<li><p>Fill in the <strong>Username</strong>, <strong>Password</strong>, and <strong>Topic Prefix</strong>.</p></li>
</ul>
</li>
<li><p>Test the Connection</p>
<ul class="simple">
<li><p>Press the <code class="docutils literal notranslate"><span class="pre">Test</span></code> button to check the connection, then press <code class="docutils literal notranslate"><span class="pre">Save</span></code> to create the network.</p></li>
</ul>
<a class="reference internal image-reference" href="../../../_images/leaps_center_pans.png"><img alt="../../../_images/leaps_center_pans.png" class="align-center" src="/docs-assets/_images/leaps_center_pans.png" style="width: 764.4000000000001px; height: 360.40000000000003px;"></a>
</li>
<li><p>Once finished, the network visualization will be displayed in both 2D gird and 3D gird views in the application. For more information, see the <code class="docutils literal notranslate"><span class="pre">LEAPS</span> <span class="pre">Center</span></code> configuration and usage.</p></li>
</ol>
</div>
<input id="sd-tab-item-2" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-2">
Advanced</label><div class="sd-tab-content docutils">
<p>Reference to <a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/pans-pro-api#pans-pro-api"><span class="std std-ref">PANS PRO API</span></a>.</p>
</div>
<input id="sd-tab-item-3" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-3">
Troubleshooting</label><div class="sd-tab-content docutils">
<ul class="simple">
<li><p>When Bluetooth Low Energy (BLE) and the LED are both off, users may erroneously perceive the board as non-functional. In this scenario, the only recourse for the user is to initiate a Factory Reset (<a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/sys#frst"><span class="std std-ref">frst</span></a>) command.</p></li>
<li><p>Please check the version. We recommend you use the latest official version.</p></li>
</ul>
</div>
</div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<ul class="simple">
<li><p>Refer to the software infrastructure to further explore the power of this demo. Our support includes <a class="reference internal" href="/docs/en/pans-pro-rtls/quick-start-guide/panspro-docker#panspro-docker"><span class="std std-ref">PANS PRO Docker</span></a> and <a class="reference internal" href="/docs/en/pans-pro-rtls/quick-start-guide/panspro-rpi#panspro-rpi"><span class="std std-ref">PANS PRO Raspberry Pi</span></a>.</p></li>
<li><p>For any comments or questions about our products, we encourage you to visit our <a class="reference external" href="https://forum.leapslabs.com">LEAPS Forum</a>.</p></li>
</ul>
</div>
</div>


           </div>
