---
title: "Programming/Upgrading firmware"
lang: en
slug: "udk/development-guide/firmware-reflashing"
section: "udk"
sourceUrl: "https://docs.leapslabs.com/udk/development-guide/firmware-reflashing/"
order: 46
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="programming-upgrading-firmware">
<span id="flashingfirmware"></span><h1>Programming/Upgrading firmware</h1>
<p>This section provides instructions on how to update the firmware. We support many ways, such as via <span class="red-text">MSD</span>, <span class="red-text">WebUSB</span>, <span class="red-text">Serial-COM</span>, <span class="red-text">OpenOCD</span> or <span class="red-text">SEGGER J-Link</span>.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>Stay connected during the update process and use the correct <span class="red-text">Device</span> and <span class="red-text">Interface</span>.</p>
</div>
<p>For more detailed information, select the method you want to use below:</p>
<div class="sd-tab-set docutils" id="uidocker">
<input checked="checked" id="sd-tab-item-0" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-0">
MSD</label><div class="sd-tab-content docutils">
<p><strong>Prepare for setup</strong></p>
<ul class="simple">
<li><p>At least one device.</p></li>
<li><p>A binary file to update.</p></li>
</ul>
<p><strong>Step-by-step instructions on how to update via MSD</strong></p>
<ol class="arabic simple">
<li><p>Use a USB-C Data Cable to connect the <a class="reference internal" href="/docs/en/udk/udk-start/device-hw-interfaces#hardware-interface"><span class="std std-ref">USB-C Data Port 2</span></a> of devices to the PC.</p></li>
</ol>
<blockquote>
<div><img alt="../../../_images/leaps-connect-usb-port2.gif" class="styled-image align-center" src="/docs-assets/_images/leaps-connect-usb-port2.gif">
</div></blockquote>
<ol class="arabic simple" start="2">
<li><p>Once connected, the LEAPS MSD drive will appear on your PC. Open the LEAPS MSD drive.</p></li>
</ol>
<blockquote>
<div><p>For example, on Windows:</p>
<a class="styled-image reference internal image-reference" href="../../../_images/msd-win-01.png"><img alt="../../../_images/msd-win-01.png" class="styled-image align-center" src="/docs-assets/_images/msd-win-01.png" style="width: 90%;"></a>
</div></blockquote>
<ol class="arabic simple" start="3">
<li><p>Download the <a class="reference external" href="https://drive.google.com/file/d/1xJHntgObdPIMpkB6PaLDRbXqNP3-WZt8/view?usp=drive_link">LEAPS-UWBS-Firmware-v1.1.0.zip</a> file to your PC. Use a program like WinZip or 7-Zip to extract the contents of the downloaded file.</p></li>
<li><p>Locate the binary file at <code class="docutils literal notranslate"><span class="pre">LEAPS-UWBS-Firmware-v1.1.0/LEAPS-UWBS-Firmware-OpenOCD/udk-leaps-uwbs-v1.1.0.bin</span></code>. Copy this file to the LEAPS MSD drive.</p></li>
</ol>
<blockquote>
<div><p>For example, on Windows:</p>
<a class="styled-image reference internal image-reference" href="../../../_images/msd-win-02.png"><img alt="../../../_images/msd-win-02.png" class="styled-image align-center" src="/docs-assets/_images/msd-win-02.png" style="width: 60%;"></a>
</div></blockquote>
<ol class="arabic simple">
<li><p>Wait for the copying and flashing process, until the copying is successful. The board will automatically reset as part of the process, the RGB LEDs will light up and the hardware will beep to indicate a successful update.</p></li>
</ol>
<p>The device successfully updated the firmware. Enjoy the latest features and improvements.</p>
</div>
<input id="sd-tab-item-1" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-1">
WebUSB</label><div class="sd-tab-content docutils">
<p><strong>Prepare for setup</strong></p>
<ul class="simple">
<li><p>At least one device.</p></li>
<li><p>A binary file to update.</p></li>
</ul>
<p><strong>Step-by-step instructions on how to update via WebUSB</strong></p>
<ol class="arabic simple">
<li><p>Download and Install Node.js.</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>Go to the official Node.js website at <a class="reference external" href="https://nodejs.org/en/download">https://nodejs.org/en/download</a>.</p></li>
<li><p>Download the recommended version of Node.js.</p></li>
<li><p>Run the downloaded installer and follow the installation prompts to complete the installation.</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="2">
<li><p>Install Dependencies.</p></li>
</ol>
<blockquote>
<div><ul>
<li><p>Open your favorite terminal application on your computer.</p>
<ul class="simple">
<li><p>On linux or macOS, like <span class="red-text">Terminal</span> application.</p></li>
<li><p>On Windows, like <span class="red-text">Powershell</span>.</p></li>
</ul>
</li>
<li><p>To install the webusb dependency, run the following command:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">npm</span> <span class="n">install</span> <span class="n">webusb</span>
</pre></div>
</div>
</li>
<li><p>Next, install the usb dependency by running the following command:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">npm</span> <span class="n">install</span> <span class="n">usb</span>
</pre></div>
</div>
</li>
<li><p>Finally, install the node-hid dependency using the following command:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">npm</span> <span class="n">install</span> <span class="n">node</span><span class="o">-</span><span class="n">hid</span>
</pre></div>
</div>
</li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="3">
<li><p>Use a USB-C Data Cable to connect the <a class="reference internal" href="/docs/en/udk/udk-start/device-hw-interfaces#hardware-interface"><span class="std std-ref">USB-C Data Port 2</span></a> of devices to the PC.</p></li>
</ol>
<blockquote>
<div><img alt="../../../_images/leaps-connect-usb-port2.gif" class="styled-image align-center" src="/docs-assets/_images/leaps-connect-usb-port2.gif">
</div></blockquote>
<ol class="arabic simple" start="4">
<li><p>Download and Extract the package to your PC. Use a program like WinZip or 7-Zip to extract the downloaded <a class="reference external" href="https://drive.google.com/file/d/1xJHntgObdPIMpkB6PaLDRbXqNP3-WZt8/view?usp=drive_link">LEAPS-UWBS-Firmware-v1.1.0.zip</a> file.</p></li>
<li><p>Open Website <a class="reference external" href="https://armmbed.github.io/dapjs/examples/daplink-flash/web.html">DAPLink Flash</a> .</p></li>
</ol>
<blockquote>
<div><a class="styled-image reference internal image-reference" href="../../../_images/daplink-flash-web02.png"><img alt="../../../_images/daplink-flash-web02.png" class="styled-image align-center" src="/docs-assets/_images/daplink-flash-web02.png" style="width: 90%;"></a>
</div></blockquote>
<ol class="arabic simple" start="6">
<li><p>Click <span class="red-text">Choose a firmware image</span> and go to select binary file at <code class="docutils literal notranslate"><span class="pre">LEAPS-UWBS-Firmware-v1.1.0/LEAPS-UWBS-Firmware-OpenOCD/udk-leaps-uwbs-v1.1.0.hex</span></code>.</p></li>
</ol>
<blockquote>
<div><a class="styled-image reference internal image-reference" href="../../../_images/daplink-flash-web03.png"><img alt="../../../_images/daplink-flash-web03.png" class="styled-image align-center" src="/docs-assets/_images/daplink-flash-web03.png" style="width: 90%;"></a>
</div></blockquote>
<ol class="arabic simple" start="7">
<li><p>Click the <span class="red-text">SELECT DEVICE</span> button then select the DAPLink CMSIS-DAP port that is connected to the PC .</p></li>
</ol>
<blockquote>
<div><a class="styled-image reference internal image-reference" href="../../../_images/daplink-flash-web05.png"><img alt="../../../_images/daplink-flash-web05.png" class="styled-image align-center" src="/docs-assets/_images/daplink-flash-web05.png" style="width: 90%;"></a>
</div></blockquote>
<ol class="arabic simple" start="8">
<li><p>After selecting a firmware image, the binary file flashing process will begin. Make sure the hardware is connected throughout the process.</p></li>
</ol>
<blockquote>
<div><a class="styled-image reference internal image-reference" href="../../../_images/daplink-flash-web06.png"><img alt="../../../_images/daplink-flash-web06.png" class="styled-image align-center" src="/docs-assets/_images/daplink-flash-web06.png" style="width: 90%;"></a>
</div></blockquote>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>Some unexpected problems may appear, please disconnect the board from the computer and start again.</p>
</div>
<ol class="arabic simple">
<li><p>After the <span class="red-text">Flash completed!</span>. The board will automatically reset as part of the process, the RGB LEDs will light up and the hardware will beep to indicate a successful update.</p></li>
</ol>
<blockquote>
<div><a class="styled-image reference internal image-reference" href="../../../_images/daplink-flash-web07.png"><img alt="../../../_images/daplink-flash-web07.png" class="styled-image align-center" src="/docs-assets/_images/daplink-flash-web07.png" style="width: 90%;"></a>
</div></blockquote>
<p>The device successfully updated the firmware. Enjoy the latest features and improvements.</p>
</div>
<input id="sd-tab-item-2" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-2">
Serial-COM</label><div class="sd-tab-content docutils">
<p><strong>You will need:</strong></p>
<ul class="simple">
<li><p>At least one device connected via the USB port.</p></li>
<li><p>The script and the firmware binary included in the package.</p></li>
<li><p>The <a class="reference external" href="https://www.python.org/downloads/">python3</a> installed on you system.</p></li>
</ul>
<p><strong>Step-by-step instructions on how to update via Serial-COM:</strong></p>
<ol class="arabic simple">
<li><p>Download and Extract the package to your PC. Use a program like WinZip or 7-Zip to extract the downloaded <a class="reference external" href="https://drive.google.com/file/d/1xJHntgObdPIMpkB6PaLDRbXqNP3-WZt8/view?usp=drive_link">LEAPS-UWBS-Firmware-v1.1.0.zip</a> file.</p></li>
<li><p>Open your favorite terminal application.</p></li>
</ol>
<ul class="simple">
<li><p>On linux or macOS, like <span class="red-text">Terminal</span> application.</p></li>
<li><p>On Windows, like <span class="red-text">Powershell</span>.</p></li>
</ul>
<ol class="arabic simple" start="3">
<li><p>Navigate to the folder containing the extracted package.</p></li>
<li><p>Install python dependencies.</p></li>
</ol>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">$ </span>pip<span class="w"> </span>install<span class="w"> </span>pyserial<span class="w"> </span>libusb<span class="w"> </span>tqdm
</pre></div>
</div>
<p>If there is an error with <code class="docutils literal notranslate"><span class="pre">libusb</span></code> try this: <code class="docutils literal notranslate"><span class="pre">sudo</span> <span class="pre">pip</span> <span class="pre">install</span> <span class="pre">libusb</span> <span class="pre">--break-system-package</span></code></p>
<ol class="arabic simple" start="5">
<li><p>Can choose to use one of two ports for the update.</p></li>
</ol>
<p>If using <a class="reference internal" href="/docs/en/udk/udk-start/device-hw-interfaces#hardware-interface"><span class="std std-ref">USB-C Data Port 1</span></a>, you can update ELDR binaries and MAIN binaries independently. On the contrary, if you use <a class="reference internal" href="/docs/en/udk/udk-start/device-hw-interfaces#hardware-interface"><span class="std std-ref">USB-C Data Port 2</span></a> you can update multiple devices continuously at the same time.</p>
<ol class="upperalpha">
<li><p>Use USB-C Data Cable to connect the <a class="reference internal" href="/docs/en/udk/udk-start/device-hw-interfaces#hardware-interface"><span class="std std-ref">USB-C Data Port 1</span></a> of the device.</p>
<blockquote>
<div><img alt="../../../_images/leaps-connect-usb-port1.gif" class="align-center" src="/docs-assets/_images/leaps-connect-usb-port1.gif">
<p>Run the following command to update the ELDR and the MAIN binaries.</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>~/LEAPS-UWBS-Firmware-Serial-COM$ sudo python3 ./udk-leaps-uwbs-serial-com.py --main ./udk-leaps-uwbs-fira-v0.15.0-rc8.bin --eldr ./udk-leaps-uwbs-eldr-v0.15.0-rc8.bin
03:11:55 Device 01/02 (SerialNumber=3DB15A2CCB8053C8): Reset
03:11:55 Device 02/02 (SerialNumber=904AD29FD29D2452): Reset
15:12:15 Device 01/02 (SerialNumber=904AD29FD29D2452): Uploading MAIN: 100%|████████████████████████████| 716192/716192 [00:16&lt;00:00, 44623.94it/s]
15:12:15 Device 02/02 (SerialNumber=3DB15A2CCB8053C8): Uploading MAIN: 100%|████████████████████████████| 716192/716192 [00:16&lt;00:00, 44630.31it/s]
15:12:37 Device 01/02 (SerialNumber=904AD29FD29D2452): Uploading ELDR: 100%|████████████████████████████| 235748/235748 [00:05&lt;00:00, 42419.44it/s]
15:12:37 Device 02/02 (SerialNumber=3DB15A2CCB8053C8): Uploading ELDR: 100%|████████████████████████████| 235748/235748 [00:05&lt;00:00, 42498.01it/s]
03:12:43 Resetting devices
</pre></div>
</div>
</div></blockquote>
</li>
<li><p>Use a USB-C Data Cable to connect the <a class="reference internal" href="/docs/en/udk/udk-start/device-hw-interfaces#hardware-interface"><span class="std std-ref">USB-C Data Port 2</span></a> of the device. Run the following command to update either the ELDR or the MAIN binary:</p>
<blockquote>
<div><img alt="../../../_images/leaps-connect-usb-port2.gif" class="align-center" src="/docs-assets/_images/leaps-connect-usb-port2.gif">
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>Might need to install the udev rules to be able to update the firmware over the <a class="reference internal" href="/docs/en/udk/udk-start/device-hw-interfaces#hardware-interface"><span class="std std-ref">USB-C Data Port 2</span></a>.
Can refer to the <a class="reference external" href="https://github.com/NordicSemiconductor/nrf-udev/tree/main">udev rules installation</a> for the Debian-like distributions.</p>
</div>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>~/LEAPS-UWBS-Firmware-Serial-COM$ python3 ./udk-leaps-uwbs-serial-com.py -d /dev/ttyACM0 --eldr ./udk-leaps-uwbs-eldr-v0.15.0-rc8.bin
02:54:30 Resetting device
02:54:33 Uploading file /home/leaps/LEAPS-UWBS-Firmware-v0.15.0/LEAPS-UWBS-Firmware-Serial-COM/udk-leaps-uwbs-eldr-v0.15.0-rc8.bin (235748 bytes)
100%|████████████████████████████| 235748/235748 [00:28&lt;00:00, 8129.43it/s]
02:55:07 Ok (upload time = 34.70 seconds)
02:55:10 Resetting device

~/LEAPS-UWBS-Firmware-Serial-COM$ python3 ./udk-leaps-uwbs-serial-com.py -d /dev/ttyACM0 --main ./udk-leaps-uwbs-fira-v0.15.0-rc8.bin
02:56:25 Resetting device
02:56:28 Uploading file /home/leaps/LEAPS-UWBS-Firmware-v0.15.0/LEAPS-UWBS-Firmware-Serial-COM/udk-leaps-uwbs-fira-v0.15.0-rc8.bin (716192 bytes)
100%|████████████████████████████| 716192/716192 [01:27&lt;00:00, 8175.81it/s]
02:58:11 Ok (upload time = 102.74 seconds)
02:58:14 Resetting device
</pre></div>
</div>
</div></blockquote>
</li>
</ol>
<ol class="arabic simple" start="6">
<li><p>Wait for the update to finish.</p></li>
<li><p>Once the update is complete, the board will automatically reset as part of the process.</p></li>
</ol>
<p>The device successfully updated the firmware. Enjoy the latest features and improvements.</p>
</div>
<input id="sd-tab-item-3" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-3">
OpenOCD</label><div class="sd-tab-content docutils">
<p><strong>Prepare for setup</strong></p>
<ul class="simple">
<li><p>At least one device.</p></li>
<li><p>A package includes a script and a binary for the update.</p></li>
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
<li><p>Download and Extract the package to your PC. Use a program like WinZip or 7-Zip to extract the downloaded <a class="reference external" href="https://drive.google.com/file/d/1xJHntgObdPIMpkB6PaLDRbXqNP3-WZt8/view?usp=drive_link">LEAPS-UWBS-Firmware-v1.1.0.zip</a> file.</p></li>
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
<li><p><span class="red-text">cd</span> to <span class="red-text">/path/to/LEAPS-UWBS-Firmware-OpenOCD</span></p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="6">
<li><p>Use a USB-C data cable to connect the <a class="reference internal" href="/docs/en/udk/udk-start/device-hw-interfaces#hardware-interface"><span class="std std-ref">USB-C Data Port 2</span></a> of devices to your PC.</p></li>
</ol>
<blockquote>
<div><img alt="../../../_images/leaps-connect-usb-port2.gif" class="styled-image align-center" src="/docs-assets/_images/leaps-connect-usb-port2.gif">
</div></blockquote>
<ol class="arabic simple" start="7">
<li><p>Execute the script to update the firmware automatically.</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>On linux or macOS, Use the <span class="red-text">udk-leaps-uwbs-firmware.sh</span> command.</p></li>
<li><p>On Windows, Use the <span class="red-text">udk-leaps-uwbs-firmware.bat</span> command.</p></li>
</ul>
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
Info : High speed (adapter speed 10000) may be limited by adapter firmware.
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
<li><p>Once the update is complete, the device will beep to indicate the update’s success. The board will automatically reset itself as part of the process.</p></li>
</ol>
<p>The device successfully updated the firmware. Enjoy the latest features and improvements.</p>
<p><strong>Troubleshooting</strong></p>
<p>In case of “Error: Could not find MEM-AP to control the core”.</p>
<blockquote>
<div><img alt="../../../_images/firmware-update-error.png" class="align-center" src="/docs-assets/_images/firmware-update-error.png">
</div></blockquote>
<p>Please execute the following command to restore:</p>
<blockquote>
<div><div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">openocd</span> <span class="o">-</span><span class="n">f</span> <span class="o">./</span><span class="n">openocd</span><span class="o">-</span><span class="n">swd</span><span class="o">-</span><span class="n">nrf52</span><span class="o">.</span><span class="n">cfg</span> <span class="o">-</span><span class="n">c</span> <span class="s2">"init;nrf52833_workaround;exit_debug_mode;shutdown;sleep 250"</span>
</pre></div>
</div>
</div></blockquote>
<p>Then continue execute <code class="docutils literal notranslate"><span class="pre">./udk-leaps-uwbs-firmware.sh</span></code>.</p>
</div>
<input id="sd-tab-item-4" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-4">
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
<input checked="checked" id="sd-tab-item-5" name="sd-tab-set-1" type="radio">
<label class="sd-tab-label" for="sd-tab-item-5">
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
<input id="sd-tab-item-6" name="sd-tab-set-1" type="radio">
<label class="sd-tab-label" for="sd-tab-item-6">
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
<input id="sd-tab-item-7" name="sd-tab-set-1" type="radio">
<label class="sd-tab-label" for="sd-tab-item-7">
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
<li><p>Open the SEGGER J-Link, then flash the binary file.</p></li>
</ol>
<blockquote>
<div><div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-8" name="sd-tab-set-2" type="radio">
<label class="sd-tab-label" for="sd-tab-item-8">
J-Link GUI (J-Flash Lite)</label><div class="sd-tab-content docutils">
<ul class="simple">
<li><p>Make sure that the latest J-Link software &amp; documentation pack is installed.</p></li>
<li><p>Connect J-Link to the PC</p></li>
<li><p>Connect target system to J-Link</p></li>
<li><p>Start J-Flash Lite</p></li>
</ul>
<a class="styled-image reference internal image-reference" href="../../../_images/jflashliteexe01.png"><img alt="../../../_images/jflashliteexe01.png" class="styled-image align-center" src="/docs-assets/_images/jflashliteexe01.png" style="width: 542.0px; height: 114.0px;"></a>
<ul class="simple">
<li><p>Select device, debug interface and communication speed</p></li>
<li><p>Choose a file and click Program Device or click Erase Chip</p></li>
<li><p>J-Flash Lite performs the requested operation</p></li>
</ul>
<a class="styled-image reference internal image-reference" href="../../../_images/jflashliteexe02.png"><img alt="../../../_images/jflashliteexe02.png" class="styled-image align-center" src="/docs-assets/_images/jflashliteexe02.png" style="width: 511.0px; height: 576.0px;"></a>
</div>
<input id="sd-tab-item-9" name="sd-tab-set-2" type="radio">
<label class="sd-tab-label" for="sd-tab-item-9">
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
</div>
<p><strong>Verify the firmware and confirm success</strong></p>
<blockquote>
<div><p>Open your favorite terminal application,</p>
<blockquote>
<div><ul class="simple">
<li><p>On GNU/Linux or macOS like <span class="red-text">Terminal</span> application.</p></li>
<li><p>On Windows, like <span class="red-text">Powershell</span> application.</p></li>
</ul>
</div></blockquote>
<p>For example, on Ubuntu (Linux), open minicom and press double enter:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">minicom</span> <span class="o">-</span><span class="n">b</span> <span class="mi">115200</span> <span class="o">-</span><span class="n">D</span> <span class="o">/</span><span class="n">dev</span><span class="o">/</span><span class="n">ttyACM0</span>
</pre></div>
</div>
<a class="styled-image reference internal image-reference" href="../../../_images/jflashliteexe05.png"><img alt="../../../_images/jflashliteexe05.png" class="styled-image align-center" src="/docs-assets/_images/jflashliteexe05.png" style="width: 663.0px; height: 418.0px;"></a>
</div></blockquote>
</div>


           </div>
