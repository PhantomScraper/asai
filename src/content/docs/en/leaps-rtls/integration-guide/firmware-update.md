---
title: "Firmware Update"
lang: en
slug: "leaps-rtls/integration-guide/firmware-update"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/leaps-rtls/integration-guide/firmware-update/"
order: 68
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="firmware-update">
<span id="lr-firmware-update"></span><h1>Firmware Update</h1>
<p>This section provides instructions on how to update the firmware. We support many ways, such as via <span class="red-text">SEGGER J-Link</span>, <span class="red-text">OpenOCD</span> or <span class="red-text">Serial-COM</span>.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<ul class="simple">
<li><p>Stay connected during the update process and use the correct <span class="red-text">Device</span> and <span class="red-text">Interface</span>.</p></li>
<li><p>The <a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/leaps-uwbs#leapsuwbs"><span class="std std-ref">LEAPS UWBS</span></a> also support firmware update over the BLE, refer <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-manager#leaps-manager-fup-over-ble"><span class="std std-ref">Firmware Update over BLE</span></a> for more detail information.</p></li>
</ul>
</div>
<p>For more detailed information, select the method you want to use below:</p>
<div class="sd-tab-set docutils" id="uidocker">
<input checked="checked" id="sd-tab-item-0" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-0">
SEGGER J-Link</label><div class="sd-tab-content docutils">
<p><strong>Prepare for setup</strong></p>
<ul class="simple">
<li><p>At least a device.</p></li>
<li><p>A binary file to update. (.hex or .bin)</p></li>
<li><p>Installed <a class="reference external" href="https://www.segger.com/downloads/jlink/#J-LinkSoftwareAndDocumentationPack">SEGGER J-Link</a>.</p></li>
</ul>
<p><strong>Step-by-step instructions on how to update via SEGGER J-Link</strong></p>
<ol class="arabic simple">
<li><p>Install the SEGGER J-Link.</p></li>
</ol>
<blockquote>
<div><div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-3" name="sd-tab-set-1" type="radio">
<label class="sd-tab-label" for="sd-tab-item-3">
Windows</label><div class="sd-tab-content docutils">
<p>Locate the Windows download file named <code class="docutils literal notranslate"><span class="pre">JLink_Windows_V766_x86_64.exe</span></code>.</p>
<ul class="simple">
<li><p>Double-click the file to initiate the installation process.</p></li>
<li><p>When prompted, enter the administrative password.</p></li>
<li><p>Please read and agree to the license terms by accepting them.</p></li>
<li><p>Accept the default destination folder for the installation, typically located at <code class="docutils literal notranslate"><span class="pre">C:\Program</span> <span class="pre">Files</span> <span class="pre">(x86)\SEGGER\JLink</span></code>.</p></li>
<li><p>Proceed with accepting the default USB driver.</p></li>
</ul>
<p>Upon completion of the installation, you will find a folder and a set of driver files installed in the system folders. Please note that with each new installation, these files will be overwritten.</p>
</div>
<input id="sd-tab-item-4" name="sd-tab-set-1" type="radio">
<label class="sd-tab-label" for="sd-tab-item-4">
macOS</label><div class="sd-tab-content docutils">
<p>Locate the macOS download file named <code class="docutils literal notranslate"><span class="pre">JLink_macOSX_V766_x86_64.pkg</span></code>.</p>
<blockquote>
<div><ul class="simple">
<li><p>Double-click the file to initiate the installation process.</p></li>
<li><p>Please read and agree to the license terms by accepting them.</p></li>
<li><p>Enter the administrative password when prompted. This password is required to write in the Applications folder.</p></li>
</ul>
</div></blockquote>
<p>After the installation, you will find a folder in the following location: <code class="docutils literal notranslate"><span class="pre">/Applications/SEGGER/JLink_V766/</span></code>. Please remember that each version will have a different folder. This folder will store all the executables and libraries associated with the application.</p>
</div>
<input id="sd-tab-item-5" name="sd-tab-set-1" type="radio">
<label class="sd-tab-label" for="sd-tab-item-5">
GNU/Linux</label><div class="sd-tab-content docutils">
<p>Visit the SEGGER download site for GNU/Linux and locate the desired package. Choose between 32/64-bit versions.</p>
<blockquote>
<div><ul class="simple">
<li><p>Preferably, download the .tgz file and save it to your computer.</p></li>
<li><p>Open a terminal window.</p></li>
</ul>
</div></blockquote>
<p>For example, on Ubuntu (Linux), to install the 64-bit .tgz file, use the following commands:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">mkdir</span> <span class="o">-</span><span class="n">p</span> <span class="o">~/</span><span class="n">opt</span><span class="o">/</span><span class="n">SEGGER</span>
<span class="n">cd</span> <span class="o">~/</span><span class="n">opt</span><span class="o">/</span><span class="n">SEGGER</span>
<span class="n">tar</span> <span class="n">xf</span> <span class="o">~/</span><span class="n">Downloads</span><span class="o">/</span><span class="n">JLink_Linux_V766_x86_64</span><span class="o">.</span><span class="n">tgz</span>
<span class="n">chmod</span> <span class="n">a</span><span class="o">-</span><span class="n">w</span> <span class="o">~/</span><span class="n">opt</span><span class="o">/</span><span class="n">SEGGER</span><span class="o">/</span><span class="n">JLink_Linux_V766_x86_64</span>
<span class="n">ls</span> <span class="o">-</span><span class="n">l</span> <span class="o">~/</span><span class="n">opt</span><span class="o">/</span><span class="n">SEGGER</span><span class="o">/</span><span class="n">JLink_Linux_V766_x86_64</span>
</pre></div>
</div>
<p>After executing the above commands:</p>
<blockquote>
<div><ul class="simple">
<li><p>A folder will be created at <cite>~/opt/SEGGER</cite>.</p></li>
<li><p>The contents of the downloaded .tgz file will be extracted to the <cite>~/opt/SEGGER</cite> folder.</p></li>
<li><p>The permissions of the <cite>JLink_Linux_V766_x86_64</cite> file will be modified.</p></li>
<li><p>Can verify the installation by checking the contents of the <cite>~/opt/SEGGER/JLink_Linux_V766_x86_64</cite> folder.</p></li>
</ul>
</div></blockquote>
<p>Please note that the installation will overwrite any existing files in the system folders during each new install.</p>
</div>
</div>
</div></blockquote>
<ol class="arabic simple" start="2">
<li><p>Open the SEGGER J-Link then flash the binary file.</p></li>
</ol>
<blockquote>
<div><div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-6" name="sd-tab-set-2" type="radio">
<label class="sd-tab-label" for="sd-tab-item-6">
J-Link GUI (J-Flash Lite)</label><div class="sd-tab-content docutils">
<ul class="simple">
<li><p>Make sure that the latest J-Link software &amp; documentation pack is installed.</p></li>
<li><p>Connect J-Link to the PC</p></li>
<li><p>Connect target system to J-Link</p></li>
<li><p>Start J-Flash Lite</p></li>
</ul>
<a class="reference internal image-reference" href="../../../_images/jflashliteexe03.png"><img alt="../../../_images/jflashliteexe03.png" class="align-center" src="/docs-assets/_images/jflashliteexe03.png" style="width: 541.0px; height: 114.0px;"></a>
<ul class="simple">
<li><p>Select device, debug interface and communication speed</p></li>
<li><p>Choose a file and click Program Device or click Erase Chip</p></li>
<li><p>J-Flash Lite performs the requested operation</p></li>
</ul>
<a class="reference internal image-reference" href="../../../_images/jflashliteexe04.png"><img alt="../../../_images/jflashliteexe04.png" class="align-center" src="/docs-assets/_images/jflashliteexe04.png" style="width: 513.0px; height: 588.0px;"></a>
</div>
<input id="sd-tab-item-7" name="sd-tab-set-2" type="radio">
<label class="sd-tab-label" for="sd-tab-item-7">
J-Link Commander (JLink.exe / JLinkExe)</label><div class="sd-tab-content docutils">
<ul class="simple">
<li><p>Make sure that the latest J-Link software &amp; documentation pack is installed.</p></li>
<li><p>Connect J-Link to the PC.</p></li>
<li><p>Connect target system to J-Link</p></li>
<li><p>Start J-Link Commander.</p></li>
<li><p>Type the following commands:</p></li>
<li><p>J-Link&gt; device &lt;devicename&gt; // For a list of known devices, please refer to here</p></li>
<li><p>J-Link&gt; r</p></li>
<li><p>J-Link&gt; h</p></li>
<li><p>J-Link&gt; loadbin &lt;PathToBinFile&gt;, &lt;programmingaddress&gt;</p></li>
<li><p>J-Link Commander executes the flash download and prints out the time statistics upon success.</p></li>
</ul>
</div>
</div>
<p>Once the update is complete, the board will automatically reset itself as part of the process.</p>
</div></blockquote>
</div>
<input id="sd-tab-item-1" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-1">
OpenOCD</label><div class="sd-tab-content docutils">
<p><strong>Prepare for setup</strong></p>
<ul class="simple">
<li><p>At least one device.</p></li>
<li><p>A package includes a script and a binary for the  update.</p></li>
<li><p>Installed <a class="reference external" href="https://openocd.org/pages/getting-openocd.html">OpenOCD</a>.</p></li>
</ul>
<p><strong>Step-by-step instructions on how to update via OpenOCD (Open On-Chip Debugger)</strong></p>
<ol class="arabic simple">
<li><p>Install the OpenOCD Debugger</p></li>
</ol>
<blockquote>
<div><div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-8" name="sd-tab-set-3" type="radio">
<label class="sd-tab-label" for="sd-tab-item-8">
Windows</label><div class="sd-tab-content docutils">
<ul class="simple">
<li><p>Download the <a class="reference external" href="https://github.com/xpack-dev-tools/openocd-xpack/releases">xPack OpenOCD package</a> for Windows.</p></li>
<li><p>Extract into the <code class="docutils literal notranslate"><span class="pre">C:\xpack-openocd-0.11.0-1</span></code> folder.</p></li>
<li><p>Add the path: <code class="docutils literal notranslate"><span class="pre">C:\xpack-openocd-0.11.0-1\bin</span></code> to your Windows User Path environment variable.</p></li>
</ul>
</div>
<input id="sd-tab-item-9" name="sd-tab-set-3" type="radio">
<label class="sd-tab-label" for="sd-tab-item-9">
macOS</label><div class="sd-tab-content docutils">
<ul class="simple">
<li><p>Download the <a class="reference external" href="https://github.com/xpack-dev-tools/openocd-xpack/releases">xPack OpenOCD package</a> for macOS.</p></li>
<li><p>Untar the tarball and install into local.</p></li>
</ul>
<p>For example, to install the xpack-openocd-0.11.0-1-linux-arm.tar.gz file, use the following commands:</p>
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
</div>
<input id="sd-tab-item-10" name="sd-tab-set-3" type="radio">
<label class="sd-tab-label" for="sd-tab-item-10">
GNU/Linux</label><div class="sd-tab-content docutils">
<ul class="simple">
<li><p>Download the <a class="reference external" href="https://github.com/xpack-dev-tools/openocd-xpack/releases">xPack OpenOCD package</a> for GNU/Linux.</p></li>
<li><p>Untar the tarball and install into local.</p></li>
</ul>
<p>For example, on Ubuntu (Linux), to install the xpack-openocd-0.11.0-1-linux-arm.tar.gz file, use the following commands:</p>
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
</div>
</div>
</div></blockquote>
<ol class="arabic simple" start="2">
<li><p>Check the OpenOCD version</p></li>
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
<li><p>Download and Extract the package to your PC.</p></li>
</ol>
<blockquote>
<div><p>Example with the UDK board: Use a program like WinZip or 7-Zip to extract the downloaded <cite>to be defined</cite> file.</p>
</div></blockquote>
<ol class="arabic simple" start="4">
<li><p>Open your favorite terminal application.</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>On linux or macOS, like <span class="red-text">Terminal</span> application.</p></li>
<li><p>On Windows, like <span class="red-text">Powershell</span> application.</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="5">
<li><p>Navigate to the folder containing the extracted package.</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p><span class="red-text">cd</span> to <span class="red-text">/path/to/LEAPS-UWBS-Firmware-OpenOCD</span></p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="6">
<li><p>Use the cable to connect the device to your PC.</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>Example with the UDK board: Use a USB-C Data Cable to connect the <a class="reference internal" href="/docs/en/udk/udk-start/device-hw-interfaces#hardware-interface"><span class="std std-ref">USB-C Data Port 2</span></a> of devices to your PC.</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="7">
<li><p>Execute the script to update the firmware automatically.</p></li>
</ol>
<blockquote>
<div><div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-11" name="sd-tab-set-4" type="radio">
<label class="sd-tab-label" for="sd-tab-item-11">
Windows</label><div class="sd-tab-content docutils">
<p>On Windows, Use the <span class="red-text">udk-leaps-uwbs-firmware.bat</span> command.</p>
</div>
<input id="sd-tab-item-12" name="sd-tab-set-4" type="radio">
<label class="sd-tab-label" for="sd-tab-item-12">
macOS</label><div class="sd-tab-content docutils">
<p>On macOS, Use the <span class="red-text">udk-leaps-uwbs-firmware.sh</span> command.</p>
</div>
<input id="sd-tab-item-13" name="sd-tab-set-4" type="radio">
<label class="sd-tab-label" for="sd-tab-item-13">
GNU/Linux</label><div class="sd-tab-content docutils">
<p>On GNU/Linux, Use the <span class="red-text">udk-leaps-uwbs-firmware.sh</span> command.</p>
</div>
</div>
<p>For example, on Ubuntu (Linux):</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>./udk-leaps-uwbs-firmware.sh
xPack OpenOCD, x86_64 Open On-Chip Debugger 0.11.0-00155-ge392e485e (2021-03-15-16:43)
Licensed under GNU GPL v2
For bug reports, read
  http://openocd.org/doc/doxygen/bugs.html
DEPRECATED! use 'adapter speed' not 'adapter_khz'
set_test_mode
Info : Using CMSIS-DAPv2 interface with VID:PID=0x0d28:0x0204, serial=01100E003602002e003f4146570120313238
Info : CMSIS-DAP: SWD Supported
Info : CMSIS-DAP: FW Version = 2.1.0
Info : CMSIS-DAP: Serial# = 01100E003602002e003f4146570120313238
Info : CMSIS-DAP: Interface Initialised (SWD)
Info : SWCLK/TCK = 1 SWDIO/TMS = 1 TDI = 0 TDO = 0 nTRST = 0 nRESET = 1
Info : CMSIS-DAP: Interface ready
Info : high-speed (adapter speed 10000) may be limited by adapter firmware.
Info : clock speed 10000 kHz
Info : SWD DPIDR 0x2ba01477
Info : nrf52.cpu: hardware has 6 breakpoints, 4 watchpoints
Info : starting gdb server for nrf52.cpu on 3333
Info : Listening on port 3333 for gdb connections
target halted due to debug-request, current mode: Thread
xPSR: 0x01000000 pc: 0x000031ec msp: 0x20003488
target halted due to debug-request, current mode: Thread
xPSR: 0x01000000 pc: 0xfffffffe msp: 0xfffffffc
Info : nRF52840-CKAA(build code: D0) 1024kB Flash, 256kB RAM
auto erase enabled
wrote 1048576 bytes from file leaps-rtls-all-2ab-v0.14-rc25.hex in 38.776192s (26.408 KiB/s)
</pre></div>
</div>
</div></blockquote>
<ol class="arabic simple" start="8">
<li><p>Once the update is complete, the board will automatically reset itself as part of the process.</p></li>
</ol>
</div>
<input id="sd-tab-item-2" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-2">
LEAPS-COM</label><div class="sd-tab-content docutils">
<p><strong>Install LEAPS-COM tool</strong></p>
<p>Follow instructions in section describing <a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/leaps-api/leaps-com/how-to-install#install-leapscom"><span class="std std-ref">how to install LEAPS-COM</span></a>.</p>
<p><strong>You will need</strong></p>
<ul class="simple">
<li><p>At least one device connected via the USB port or the serial port, alternatively, the device advertises on the BLE interface if enabled.</p></li>
<li><p>The firmware binary included in the package.</p></li>
<li><p>The <a class="reference external" href="https://www.python.org/downloads/">python3</a> installed on you system.</p></li>
</ul>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-14" name="sd-tab-set-5" type="radio">
<label class="sd-tab-label" for="sd-tab-item-14">
USB</label><div class="sd-tab-content docutils">
<p>Connect USB data cable to the <a class="reference internal" href="/docs/en/udk/udk-start/device-hw-interfaces#hardware-interface"><span class="std std-ref">USB port</span></a>.
Execute following command to update Firmware and Extended-Loader on the available devices that are connected on the USB interface.</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">$ </span>python3<span class="w"> </span>-m<span class="w"> </span>leapscom<span class="w"> </span>--usb<span class="w"> </span>--main<span class="w"> </span>main.bin<span class="w"> </span>--eldr<span class="w"> </span>eldr.bin
</pre></div>
</div>
<p>In order to update only certain devices you need to specify serial number.</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">$ </span>python3<span class="w"> </span>-m<span class="w"> </span>leapscom<span class="w"> </span>--usb<span class="w"> </span>630D46F2D51482FC<span class="w"> </span>7E1C5859C2ECF343<span class="w"> </span>--main<span class="w"> </span>main.bin<span class="w"> </span>--eldr<span class="w"> </span>eldr.bin
</pre></div>
</div>
</div>
<input id="sd-tab-item-15" name="sd-tab-set-5" type="radio">
<label class="sd-tab-label" for="sd-tab-item-15">
BLE</label><div class="sd-tab-content docutils">
<p>Before update, make sure that BLE is enabled on the devices (see section <a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/leaps-api/leaps-com/cmd-execution#discovering-leaps-devices"><span class="std std-ref">Discovering devices</span></a> for more details).
Execute following command to update Firmware and Extended-Loader of all the devices that are advertising on the BLE interface.</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">$ </span>python3<span class="w"> </span>-m<span class="w"> </span>leapscom<span class="w"> </span>--ble<span class="w"> </span>--main<span class="w"> </span>main.bin<span class="w"> </span>--eldr<span class="w"> </span>eldr.bin
</pre></div>
</div>
<p>In order to update only certain devices you need to specify the BLE address.</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">$ </span>python3<span class="w"> </span>-m<span class="w"> </span>leapscom<span class="w"> </span>--ble<span class="w"> </span>FE:40:B4:BC:D3:42<span class="w"> </span>E0:05:86:49:A9:40<span class="w"> </span>--main<span class="w"> </span>main.bin<span class="w"> </span>--eldr<span class="w"> </span>eldr.bin
</pre></div>
</div>
</div>
<input id="sd-tab-item-16" name="sd-tab-set-5" type="radio">
<label class="sd-tab-label" for="sd-tab-item-16">
Serial port</label><div class="sd-tab-content docutils">
<p>Connect USB data cable to the <a class="reference internal" href="/docs/en/udk/udk-start/device-hw-interfaces#hardware-interface"><span class="std std-ref">Serial port</span></a>.
Execute following command to update Firmware and Extended-Loader over the serial ports.</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">$ </span>python3<span class="w"> </span>-m<span class="w"> </span>leapscom<span class="w"> </span>--dev<span class="w"> </span>/dev/ttyACM0<span class="w"> </span>/dev/ttyACM1<span class="w"> </span>/dev/ttyACM2<span class="w"> </span>--main<span class="w"> </span>main.bin<span class="w"> </span>--eldr<span class="w"> </span>eldr.bin
</pre></div>
</div>
</div>
</div>
</div>
</div>
<p><strong>Verify the firmware and confirm success</strong></p>
<blockquote>
<div><p>Open your favorite terminal application,</p>
<blockquote>
<div><ul class="simple">
<li><p>On GNU/Linux or macOS, like <span class="red-text">Terminal</span> application.</p></li>
<li><p>On Windows, like <span class="red-text">Powershell</span> application.</p></li>
</ul>
</div></blockquote>
<p>For example, on Ubuntu (Linux), open minicom and press double enter:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">minicom</span> <span class="o">-</span><span class="n">b</span> <span class="mi">115200</span> <span class="o">-</span><span class="n">D</span> <span class="o">/</span><span class="n">dev</span><span class="o">/</span><span class="n">ttyACM0</span>
</pre></div>
</div>
<a class="reference internal image-reference" href="../../../_images/jflashliteexe05.png"><img alt="../../../_images/jflashliteexe05.png" class="align-center" src="/docs-assets/_images/jflashliteexe05.png" style="width: 663.0px; height: 418.0px;"></a>
</div></blockquote>
<hr class="docutils">
<p>For the connection, let’s first take a look at an overview of the main components of <a class="reference external" href="https://www.qorvo.com/products/p/DWM1001-DEV">DWM1001-DEV</a> and <a class="reference external" href="https://www.qorvo.com/products/p/DWM3001CDK">DWM3001CDK</a> development kit.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>For the UDK Kit, please refer to the detailed information in the <a class="reference internal" href="/docs/en/udk/udk-start/device-hw-interfaces#hardware-interface"><span class="std std-ref">Hardware Interfaces</span></a> section.</p>
</div>
<a class="reference internal image-reference" href="../../../_images/dwm1001_io.png"><img alt="../../../_images/dwm1001_io.png" class="align-center" src="/docs-assets/_images/dwm1001_io.png" style="width: 696.8000000000001px; height: 357.6px;"></a>
<a class="reference internal image-reference" href="../../../_images/dwm3001c_io.png"><img alt="../../../_images/dwm3001c_io.png" class="align-center" src="/docs-assets/_images/dwm3001c_io.png" style="width: 630.0px; height: 630.0px;"></a>
</div>


           </div>
