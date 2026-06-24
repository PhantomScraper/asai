---
title: "Firmware Update"
lang: en
slug: "pans-pro-rtls/integration-guide/firmware-update"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/pans-pro-rtls/integration-guide/firmware-update/"
order: 94
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="firmware-update">
<span id="pans-pro-fw-update"></span><h1>Firmware Update</h1>
<p>When the RTLS network is forming, the initiator anchor specifies the firmware version
necessary for the network. When an automatic FW update is enabled, any device wishing
to participate (join) the network must have the same firmware (version number and the checksum).
If a new device does not have the correct firmware, it will be updated as per the subsections below.</p>
<div class="section" id="firmware-update-via-bluetooth">
<h2>Firmware update via Bluetooth</h2>
<p>If one wants to update the entire network to a new firmware image while the network is operational,
it is sufficient just to update the initiator via Bluetooth. The initiator will then automatically
propagate the new firmware to all other devices over the UWB radio link.
Note that as the initiator is updated first, it will restart the network,
and as each device rejoins the network, its firmware will be updated.
Thus, during the FW update, the nodes performing the updat will be “offline”.</p>
</div>
<div class="section" id="firmware-update-via-uwb">
<h2>Firmware update via UWB</h2>
<p>As introduced in the DWM1001 System Overview [4], the nodes will compare their
firmware version to the network they want to join. If the firmware version is different,
the nodes will try to update their firmware before joining.
This firmware update function can be enabled/disabled in the configuration.
Here, it lists the rules of the function that the nodes will follow.</p>
<p><strong>Tag:</strong></p>
<ul class="simple">
<li><p>When enabled, the tag will always check the firmware version and try to synchronise its firmware version with the network by sending the update request to the nearby anchor nodes in the network before it starts ranging.</p></li>
<li><p>When disabled, the tag will start ranging without checking the firmware version. This can lead to version compatibility problems and must be dealt with very carefully.</p></li>
</ul>
<p><strong>Anchor:</strong></p>
<ul class="simple">
<li><p>When enabled, before joining the network, the anchor will check the firmware version and try to synchronise its firmware version with the network by sending the update request to the nearby anchor nodes. After having joined the network, the anchor will respond to nearby nodes’ requests to update their firmware.</p></li>
<li><p>When disabled, before joining the network, the anchor will directly send the join request and not check the firmware version. This can lead to version compatibility problems and must be dealt with very carefully. After having joined the network, the anchor will ignore the firmware update requests from the nearby nodes.</p></li>
</ul>
</div>
<hr class="docutils">
<div class="section" id="firmware-update-via-uart">
<h2>Firmware update via UART</h2>
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
</div>


           </div>
