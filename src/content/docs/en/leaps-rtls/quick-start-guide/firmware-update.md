---
title: "Firmware Update"
lang: en
slug: "leaps-rtls/quick-start-guide/firmware-update"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/leaps-rtls/quick-start-guide/firmware-update/"
order: 62
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="firmware-update">
<span id="leaps-qsg-fw-update"></span><h1>Firmware Update</h1>
<p>This section describes ways to update the firmware. We support many different ways, such as via  <span class="red-text">Bluetooth</span>, <span class="red-text">MSD</span>, <span class="red-text">WebUSB</span>, <span class="red-text">Serial-COM</span> or <span class="red-text">OpenOCD</span>.</p>
<p>For more detailed information, select the method you want to use below:</p>
<div class="sd-tab-set docutils" id="uidocker">
<input checked="checked" id="sd-tab-item-0" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-0">
Bluetooth</label><div class="sd-tab-content docutils">
<div class="figure align-right" id="id4">
<a class="reference internal image-reference" href="../../../_images/leaps-manager-qr-code.png"><img alt="../../../_images/leaps-manager-qr-code.png" src="/docs-assets/_images/leaps-manager-qr-code.png" style="width: 112.5px; height: 112.5px;"></a>
<p class="caption"><span class="caption-text"><a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> on <a class="reference external" href="https://play.google.com/store/apps/details?id=global.leaps.manager.leaps&amp;hl=en_GB&amp;gl=US">Google Play</a></span></p>
</div>
<p><strong>Prepare for setup</strong></p>
<ul class="simple">
<li><p>At least one device.</p></li>
<li><p><a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> application installed on an Android device.</p></li>
</ul>
<div class="admonition note">
<p class="admonition-title">Note</p>
<ul class="simple">
<li><p>Ensure connection during the update process and avoid moving too far when the connection is Bluetooth.</p></li>
<li><p>Firmware update speed will depend on the Bluetooth device. For example, Bluetooth 4.2 and Bluetooth 5.0 have data rates of 1Mbps versus 2Mbps, respectively.</p></li>
</ul>
</div>
<p><strong>Step-by-step instructions on how to update via Bluetooth:</strong></p>
<p>1. Open the <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> application, then navigate to the <span class="red-text">Demo Selector</span>.
Additionally, you can navigate to the created network to update the devices in the network.</p>
<ol class="arabic" start="2">
<li><p>Access firmware status. Tap the <span class="red-text">options menu</span> (<em>represented as three vertical dots</em>) within the application. Look for the <span class="red-text">Firmware status</span> option and select it.</p>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/firmware-update9.jpg"><img alt="../../../_images/firmware-update9.jpg" src="/docs-assets/_images/firmware-update9.jpg" style="width: 45%;"></a>
<a class="reference internal image-reference" href="../../../_images/firmware-update10.jpg"><img alt="../../../_images/firmware-update10.jpg" src="/docs-assets/_images/firmware-update10.jpg" style="width: 45%;"></a>
<div class="line-block">
<div class="line"><br></div>
</div>
</div></blockquote>
</li>
<li><p>Choose the devices to update.</p></li>
</ol>
<blockquote>
<div><ul>
<li><p>From the list of devices presented, select the one you want to update the firmware.</p></li>
<li><p>The <span class="red-text">Update</span> button is located in the lower left corner of the app’s interface. click it to initiate the firmware update process for the selected device.</p>
<a class="reference internal image-reference" href="../../../_images/firmware-update8.jpg"><img alt="../../../_images/firmware-update8.jpg" src="/docs-assets/_images/firmware-update8.jpg" style="width: 45%;"></a>
<a class="reference internal image-reference" href="../../../_images/firmware-update5.jpg"><img alt="../../../_images/firmware-update5.jpg" src="/docs-assets/_images/firmware-update5.jpg" style="width: 45%;"></a>
<div class="line-block">
<div class="line"><br></div>
</div>
</li>
</ul>
</div></blockquote>
<ol class="arabic" start="4">
<li><p>The app will provide visual indicators or progress bars to show how the update is proceeding. Be patient and let the update process run its course.</p>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/firmware-update7.jpg"><img alt="../../../_images/firmware-update7.jpg" src="/docs-assets/_images/firmware-update7.jpg" style="width: 45%;"></a>
<a class="reference internal image-reference" href="../../../_images/firmware-update1.jpg"><img alt="../../../_images/firmware-update1.jpg" src="/docs-assets/_images/firmware-update1.jpg" style="width: 45%;"></a>
<div class="line-block">
<div class="line"><br></div>
</div>
</div></blockquote>
</li>
<li><p>Once the update is complete, you will see <span class="red-text">status is done</span>. Additionally, the device will beep to indicate the update’s success. The board will automatically reset itself as part of the process.</p>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/firmware-update3.jpg"><img alt="../../../_images/firmware-update3.jpg" src="/docs-assets/_images/firmware-update3.jpg" style="width: 45%;"></a>
<a class="reference internal image-reference" href="../../../_images/firmware-update2.jpg"><img alt="../../../_images/firmware-update2.jpg" src="/docs-assets/_images/firmware-update2.jpg" style="width: 45%;"></a>
</div></blockquote>
</li>
</ol>
<p>The device successfully updated the firmware. Enjoy the latest features and improvements.</p>
</div>
<input id="sd-tab-item-1" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-1">
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
<div><img alt="../../../_images/leaps-connect-usb-port2.gif" class="align-center" src="/docs-assets/_images/leaps-connect-usb-port2.gif">
</div></blockquote>
<ol class="arabic simple" start="2">
<li><p>Once connected, the LEAPS MSD drive will appear on your PC. Open the LEAPS MSD drive.</p></li>
</ol>
<blockquote>
<div><p>For example, on Windows:</p>
<a class="reference internal image-reference" href="../../../_images/msd-win-01.png"><img alt="../../../_images/msd-win-01.png" class="align-center" src="/docs-assets/_images/msd-win-01.png" style="width: 90%;"></a>
</div></blockquote>
<ol class="arabic simple" start="3">
<li><p>Download the <a class="reference external" href="https://drive.google.com/file/d/1xJHntgObdPIMpkB6PaLDRbXqNP3-WZt8/view?usp=drive_link">LEAPS-UWBS-Firmware-v1.1.0.zip</a> file to your PC. Use a program like WinZip or 7-Zip to extract the contents of the downloaded file.</p></li>
<li><p>Locate the binary file at <code class="docutils literal notranslate"><span class="pre">LEAPS-UWBS-Firmware-v1.1.0/LEAPS-UWBS-Firmware-OpenOCD/udk-leaps-uwbs-v1.1.0.bin</span></code>. Copy this file to the LEAPS MSD drive.</p></li>
</ol>
<blockquote>
<div><p>For example, on Windows:</p>
<a class="reference internal image-reference" href="../../../_images/msd-win-02.png"><img alt="../../../_images/msd-win-02.png" class="align-center" src="/docs-assets/_images/msd-win-02.png" style="width: 60%;"></a>
</div></blockquote>
<ol class="arabic simple" start="5">
<li><p>Wait for the copying and flashing process, until the copying is successful. The board will automatically reset as part of the process, the RGB LEDs will light up and the hardware will beep to indicate a successful update.</p></li>
</ol>
<p>The device successfully updated the firmware. Enjoy the latest features and improvements.</p>
</div>
<input id="sd-tab-item-2" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-2">
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
<div><img alt="../../../_images/leaps-connect-usb-port2.gif" class="align-center" src="/docs-assets/_images/leaps-connect-usb-port2.gif">
</div></blockquote>
<ol class="arabic simple" start="4">
<li><p>Download and Extract the package to your PC. Use a program like WinZip or 7-Zip to extract the downloaded <a class="reference external" href="https://drive.google.com/file/d/1xJHntgObdPIMpkB6PaLDRbXqNP3-WZt8/view?usp=drive_link">LEAPS-UWBS-Firmware-v1.1.0.zip</a> file.</p></li>
<li><p>Open Website <a class="reference external" href="https://armmbed.github.io/dapjs/examples/daplink-flash/web.html">DAPLink Flash</a> .</p></li>
</ol>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/daplink-flash-web02.png"><img alt="../../../_images/daplink-flash-web02.png" class="align-center" src="/docs-assets/_images/daplink-flash-web02.png" style="width: 90%;"></a>
</div></blockquote>
<ol class="arabic simple" start="6">
<li><p>Click <span class="red-text">Choose a firmware image</span> and go to select binary file at <code class="docutils literal notranslate"><span class="pre">LEAPS-UWBS-Firmware-v1.1.0/LEAPS-UWBS-Firmware-OpenOCD/udk-leaps-uwbs-v1.1.0.hex</span></code>.</p></li>
</ol>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/daplink-flash-web03.png"><img alt="../../../_images/daplink-flash-web03.png" class="align-center" src="/docs-assets/_images/daplink-flash-web03.png" style="width: 90%;"></a>
</div></blockquote>
<ol class="arabic simple" start="5">
<li><p>Click the <span class="red-text">SELECT DEVICE</span> button then select the DAPLink CMSIS-DAP port that is connected to the PC .</p></li>
</ol>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/daplink-flash-web05.png"><img alt="../../../_images/daplink-flash-web05.png" class="align-center" src="/docs-assets/_images/daplink-flash-web05.png" style="width: 90%;"></a>
</div></blockquote>
<ol class="arabic simple" start="6">
<li><p>After selecting a firmware image, the binary file flashing process will begin. Make sure the hardware is connected throughout the process.</p></li>
</ol>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/daplink-flash-web06.png"><img alt="../../../_images/daplink-flash-web06.png" class="align-center" src="/docs-assets/_images/daplink-flash-web06.png" style="width: 90%;"></a>
</div></blockquote>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>Some unexpected problems may appear, please disconnect the board from the computer and start again.</p>
</div>
<ol class="arabic simple" start="7">
<li><p>After the <span class="red-text">Flash completed!</span>. The board will automatically reset as part of the process, the RGB LEDs will light up and the hardware will beep to indicate a successful update.</p></li>
</ol>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/daplink-flash-web07.png"><img alt="../../../_images/daplink-flash-web07.png" class="align-center" src="/docs-assets/_images/daplink-flash-web07.png" style="width: 90%;"></a>
</div></blockquote>
<p>The device successfully updated the firmware. Enjoy the latest features and improvements.</p>
</div>
<input id="sd-tab-item-3" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-3">
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
<input id="sd-tab-item-4" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-4">
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
<div><img alt="../../../_images/leaps-connect-usb-port2.gif" class="align-center" src="/docs-assets/_images/leaps-connect-usb-port2.gif">
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
