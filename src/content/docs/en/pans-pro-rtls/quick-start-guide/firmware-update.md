---
title: "Firmware Update"
lang: en
slug: "pans-pro-rtls/quick-start-guide/firmware-update"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/pans-pro-rtls/quick-start-guide/firmware-update/"
order: 89
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="firmware-update">
<span id="qsg-firmware-update"></span><h1>Firmware Update</h1>
<p>This section describes ways to update the firmware. We support many different ways, such as via <span class="red-text">Bluetooth</span>, <span class="red-text">SWD</span>, <span class="red-text">OpenOCD</span>, or <span class="red-text">UWB</span>.</p>
<p>For more detailed information, select the method you want to use below:</p>
<div class="sd-tab-set docutils" id="uidocker">
<input checked="checked" id="sd-tab-item-0" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-0">
Bluetooth</label><div class="sd-tab-content docutils">
<p><strong>Via Bluetooth Interface</strong></p>
<p>If one wants to update the entire network to a new firmware image while the network is operational, it is sufficient
just to update the initiator via Bluetooth. The initiator will then automatically propagate the new firmware to all
other devices over the UWB radio link.
Note that as the initiator is updated first, it will restart the network, and as each device rejoins the network,
its firmware will be updated. Thus, during the FW update, the nodes performing the update will be “offline”.</p>
<p>To get started, please download the <a class="reference internal" href="/docs/en/pans-pro-rtls/infrastructure/pans-pro-manager#pans-pro-manager"><span class="std std-ref">PANS PRO Manager</span></a> application (<a class="reference external" href="https://play.google.com/store/apps/details?id=global.leaps.manager.panspro&amp;hl=en">available in the Google Play</a>)</p>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/panspro-manager-qr-code.png"><img alt="../../../_images/panspro-manager-qr-code.png" src="/docs-assets/_images/panspro-manager-qr-code.png" style="width: 344.4px; height: 344.4px;"></a>
</div>
<ul class="simple">
<li><p>By default, a login account with username is <span class="red-text">admin</span> and password is <span class="red-text">admin</span> in case settings enable user management.</p></li>
<li><p>Access firmware status. Tap the <span class="red-text">options menu</span> (<em>represented as three vertical dots</em>) within the application.</p></li>
<li><p>Look for the <span class="red-text">Firmware status</span> option and select it.</p></li>
<li><p>Choose the devices to update.</p></li>
</ul>
<a class="reference internal image-reference" href="../../../_images/ppm-network-menu.jpg"><img alt="../../../_images/ppm-network-menu.jpg" src="/docs-assets/_images/ppm-network-menu.jpg" style="width: 40%;"></a>
<a class="reference internal image-reference" href="../../../_images/ppm-firmware-update.jpg"><img alt="../../../_images/ppm-firmware-update.jpg" src="/docs-assets/_images/ppm-firmware-update.jpg" style="width: 40%;"></a>
</div>
<input id="sd-tab-item-1" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-1">
SWD</label><div class="sd-tab-content docutils">
<p><strong>Firmware update using SWD programmer</strong></p>
<blockquote>
<div><img alt="../../../_images/image92.png" src="/docs-assets/_images/image92.png">
</div></blockquote>
<p>DWM1001C on LC4/LC5</p>
<blockquote>
<div><img alt="../../../_images/image101.png" src="/docs-assets/_images/image101.png">
</div></blockquote>
<p>Unnamed board</p>
<blockquote>
<div><img alt="../../../_images/image111.png" src="/docs-assets/_images/image111.png">
</div></blockquote>
<p><strong>Programming the binary</strong></p>
<p>The necessary steps to flash the factory image on the boards are
described below. In order to reflash it is necessary to use J-Link or
CMSIS-DAP programmers. The boards have to be powered via USB or via
battery during the reflash as the programmer connector does not
supply the power.</p>
<p>The J-Flash Light software tool can be used to flash the image. This
method will be described below. An alternative way is to use the open
source tool OpenOCD which is available on various platforms. The PANS
PRO software package contains reflash scripts to be used with
OpenOCD.</p>
<ol class="arabic">
<li><p>Download and install Segger J-Flash Lite (J-Link software suite): <a class="reference external" href="https://www.segger.com/downloads/jlink/#J-LinkSoftwareAndDocumentationPack">https://www.segger.com/downloads/jlink/#J-LinkSoftwareAndDocumentationPack</a></p></li>
<li><p>Connect the module with a micro USB data cable as shown below.</p>
<ol class="arabic">
<li><p>Connection for firmware reflash of the DWM1001C module on LC5 Gateway</p>
<a class="reference internal image-reference" href="../../../_images/image131.png"><img alt="../../../_images/image131.png" src="/docs-assets/_images/image131.png" style="width: 320.0px; height: 240.0px;"></a>
</li>
<li><p>Connection for firmware reflash of the host MCU SAME70 on LC5 Gateway</p>
<a class="reference internal image-reference" href="../../../_images/image141.png"><img alt="../../../_images/image141.png" src="/docs-assets/_images/image141.png" style="width: 320.0px; height: 240.0px;"></a>
</li>
</ol>
</li>
<li><p>Open J-Flash Lite.</p></li>
<li><p>Choose nrf52832_XXAA as Device and SWD as interface for the DWM1001C.
For the host MCU use ATSAME70N19. Use default speed 1000 and click <strong>“OK”</strong></p>
<a class="reference internal image-reference" href="../../../_images/image15.png"><img alt="../../../_images/image15.png" src="/docs-assets/_images/image15.png" style="width: 384.40000000000003px; height: 126.80000000000001px;"></a>
</li>
<li><p>Click “Erase Chip” to do a full chip erase.</p>
<a class="reference internal image-reference" href="../../../_images/image16.png"><img alt="../../../_images/image16.png" src="/docs-assets/_images/image16.png" style="width: 371.5px; height: 327.0px;"></a>
</li>
<li><p>In Data File, click “…” and browse to the hex file provided in the PANS PRO
Software package to flash. Then click <strong>“Program Device”</strong>. Firmware binaries
compatibility</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>Please contact us for the download package at <a class="reference external" href="mailto:apps-support%40leapslabs.com">apps-support<span>@</span>leapslabs<span>.</span>com</a>.</p></li>
</ul>
</div></blockquote>
<table class="docutils align-default">
<colgroup>
<col style="width: 31%">
<col style="width: 36%">
<col style="width: 34%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>Firmware file</strong></p></th>
<th class="head"><p><strong>Target</strong></p></th>
<th class="head"><p><strong>Reflash address</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>pan-pro-all-dwm1001c-vY.XX.hex</p></td>
<td><p>DWM1001C module on LC4 Tag
and LC5 Gateway</p></td>
<td><p>0x00000000</p></td>
</tr>
<tr class="row-odd"><td><p>pans-pro-all-lc5s-vY.XX.hex</p></td>
<td><p>Host MCU SAME70 on LC5 Gateway</p></td>
<td><p>0x00400000</p></td>
</tr>
</tbody>
</table>
</div>
<input id="sd-tab-item-2" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-2">
OpenOCD</label><div class="sd-tab-content docutils">
<p><strong>Prepare for setup</strong></p>
<ul class="simple">
<li><p>At least one device.</p></li>
<li><p>A package includes a script and a binary for the  update.</p></li>
<li><p>Installed <a class="reference external" href="https://github.com/xpack-dev-tools/openocd-xpack/releases">OpenOCD</a>.</p></li>
</ul>
<p><strong>Step-by-step instructions on how to update via OpenOCD (Open On-Chip Debugger):</strong></p>
<ol class="arabic simple">
<li><p>Installing the OpenOCD Debugger.</p></li>
</ol>
<blockquote>
<div><ol class="upperalpha simple">
<li><p>Installing OpenOCD on Windows.</p></li>
</ol>
<blockquote>
<div><ol class="loweralpha simple">
<li><p>Download the binary zip file for Windows.</p></li>
<li><p>Extract into the <code class="docutils literal notranslate"><span class="pre">C:\xpack-openocd-0.11.0-1</span></code> folder.</p></li>
<li><p>Add the path: <code class="docutils literal notranslate"><span class="pre">C:\xpack-openocd-0.11.0-1\bin</span></code> to your Windows User Path environment variable.</p></li>
</ol>
</div></blockquote>
<ol class="upperalpha simple" start="2">
<li><p>Installing OpenOCD on Linux or macOS.</p></li>
</ol>
<blockquote>
<div><ol class="loweralpha simple">
<li><p>Download the <a class="reference external" href="https://github.com/xpack-dev-tools/openocd-xpack/releases">binary tarball for Linux</a> .</p></li>
<li><p>Untar the tarball and install into local.</p></li>
</ol>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>mkdir -p ~/.local/xPacks/openocd
cd ~/.local/xPacks/openocd
tar -zxvf ~/Downloads/xpack-openocd-0.11.0-1-linux-arm.tar.gz (with PC’s AMD core, using … linux-x64.tar.gz with PC’s Intel core)
....
sudo chmod -R -w xpack-openocd-0.11.0-1/
~/.local/xPacks/openocd/xpack-openocd-0.11.0-1/bin/openocd --version
export PATH="~/.local/xPacks/openocd/xpack-openocd-0.11.0-1/bin/:$PATH"
cd ~
source .bashrc
</pre></div>
</div>
</div></blockquote>
</div></blockquote>
<ol class="arabic simple" start="2">
<li><p>Check the OpenOCD version.</p></li>
</ol>
<blockquote>
<div><div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">openocd</span> <span class="o">--</span><span class="n">version</span>
<span class="n">xPack</span> <span class="n">OpenOCD</span><span class="p">,</span> <span class="n">x86_64</span> <span class="n">Open</span> <span class="n">On</span><span class="o">-</span><span class="n">Chip</span> <span class="n">Debugger</span> <span class="mf">0.11.0</span><span class="o">-</span><span class="mi">00155</span><span class="o">-</span><span class="n">ge392e485e</span> <span class="p">(</span><span class="mi">2021</span><span class="o">-</span><span class="mi">03</span><span class="o">-</span><span class="mi">15</span><span class="o">-</span><span class="mi">16</span><span class="p">:</span><span class="mi">43</span><span class="p">)</span>
<span class="n">Licensed</span> <span class="n">under</span> <span class="n">GNU</span> <span class="n">GPL</span> <span class="n">v2</span>
<span class="n">For</span> <span class="n">bug</span> <span class="n">reports</span><span class="p">,</span> <span class="n">read</span>
  <span class="n">http</span><span class="p">:</span><span class="o">//</span><span class="n">openocd</span><span class="o">.</span><span class="n">org</span><span class="o">/</span><span class="n">doc</span><span class="o">/</span><span class="n">doxygen</span><span class="o">/</span><span class="n">bugs</span><span class="o">.</span><span class="n">html</span>
</pre></div>
</div>
</div></blockquote>
<ol class="arabic simple" start="3">
<li><p>Download and Extract the package to your PC. Use a program like WinZip or 7-Zip to extract the downloaded file.</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>Please contact us for the download package at <a class="reference external" href="mailto:apps-support%40leapslabs.com">apps-support<span>@</span>leapslabs<span>.</span>com</a>.</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="4">
<li><p>Open your favorite terminal application.</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>On linux or macOS, like <span class="red-text">Terminal</span> application.</p></li>
<li><p>On Windows, like <span class="red-text">Powershell</span>.</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="5">
<li><p>Navigate to the folder containing the extracted package.</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p><span class="red-text">cd</span> to <span class="red-text">/path/to/PANSPRO-Firmware-OpenOCD</span></p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="6">
<li><p>Use a Micro USB data cable to connect the <code class="docutils literal notranslate"><span class="pre">Micro</span> <span class="pre">USB</span> <span class="pre">Data</span> <span class="pre">Port</span></code> of devices to your PC.</p></li>
<li><p>Execute the script to update the firmware automatically.</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>On linux or macOS, Use the <span class="red-text">reflash-panspro-rtls-2ab.sh</span> command.</p></li>
<li><p>On Windows, Use the <span class="red-text">reflash-panspro-rtls-2ab.bat</span> command.</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="8">
<li><p>Once the update is complete, the device will beep to indicate the update’s success. The board will automatically reset itself as part of the process.</p></li>
</ol>
<p>The device successfully updated the firmware. Enjoy the latest features and improvements.</p>
</div>
<input id="sd-tab-item-3" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-3">
UWB</label><div class="sd-tab-content docutils">
<p>When the RTLS network is forming, the initiator anchor specifies the firmware version necessary for the network.
When an automatic FW update is enabled, any device wishing to participate (join) the network must have the same
firmware (version number and the checksum). If a new device does not have the correct firmware, it will be updated
as per the subsections below.</p>
<p><strong>Via UWB Interface</strong></p>
<p>As introduced in the DWM1001 System Overview [4], the nodes will compare their firmware version to the network they
want to join. If the firmware version is different, the nodes will try to update their firmware before joining. This
firmware update function can be enabled/disabled in the configuration. Here, it lists the rules of the function that
the nodes will follow.</p>
<p><strong>Tag:</strong></p>
<ul class="simple">
<li><p>When enabled, the tag will always check the firmware version and try to synchronize its firmware version with the network by sending the update request to the nearby anchor nodes in the network before it starts ranging.</p></li>
<li><p>When disabled, the tag will start ranging without checking the firmware version. This can lead to version compatibility problems and must be dealt with very carefully.</p></li>
</ul>
<p><strong>Anchor:</strong></p>
<ul class="simple">
<li><p>When enabled, before joining the network, the anchor will check the firmware version and try to synchronize its firmware version with the network by sending the update request to the nearby anchor nodes. After having joined the network, the anchor will respond to nearby nodes’ requests to update their firmware.</p></li>
<li><p>When disabled, before joining the network, the anchor will directly send the join request and not check the firmware version. This can lead to version compatibility problems and must be dealt with very carefully. After having joined the network, the anchor will ignore the firmware update requests from the nearby nodes.</p></li>
</ul>
</div>
</div>
</div>


           </div>
