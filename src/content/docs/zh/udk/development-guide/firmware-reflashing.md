---
title: "编程/升级固件"
lang: zh
slug: "udk/development-guide/firmware-reflashing"
section: "udk"
sourceUrl: "https://docs.leapslabs.com/zh-cn/udk/development-guide/firmware-reflashing/"
order: 46
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="programming-upgrading-firmware">
<span id="flashingfirmware"></span><h1>编程/升级固件</h1>
<p>本节提供有关如何更新固件的说明. 我们支持多种方式，例如通过 <span class="red-text">MSD</span>, <span class="red-text">WebUSB</span>, <span class="red-text">Serial-COM</span>, <span class="red-text">OpenOCD</span> 或 <span class="red-text">SEGGER J-Link</span>。</p>
<div class="admonition note">
<p class="admonition-title">注解</p>
<p>在更新过程中保持连接，并使用正确的 <span class="red-text">装置</span> 和 <span class="red-text">界面</span>。</p>
</div>
<p>更多详细信息，请在下面选择您要使用的方法:</p>
<div class="sd-tab-set docutils" id="uidocker">
<input checked="checked" id="sd-tab-item-0" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-0">
MSD</label><div class="sd-tab-content docutils">
<p><strong>准备设置</strong></p>
<ul class="simple">
<li><p>至少一个设备。</p></li>
<li><p>要更新的二进制文件。</p></li>
</ul>
<p><strong>关于如何通过 MSD 进行更新的分步说明</strong></p>
<ol class="arabic simple">
<li><p>使用 USB-C 数据线将设备的 <a class="reference internal" href="/docs/zh/udk/udk-start/device-hw-interfaces#hardware-interface"><span class="std std-ref">USB-C Data Port 2</span></a> 连接到 PC。</p></li>
</ol>
<blockquote>
<div><img alt="../../../_images/leaps-connect-usb-port2.gif" class="styled-image align-center" src="/docs-assets/zh-cn/_images/leaps-connect-usb-port2.gif">
</div></blockquote>
<ol class="arabic simple" start="2">
<li><p>连接完成后，LEAPS MSD驱动器会出现在你的PC上。 打开LEAPS MSD驱动器。</p></li>
</ol>
<blockquote>
<div><p>例如，在 Windows 上：</p>
<a class="styled-image reference internal image-reference" href="../../../_images/msd-win-01.png"><img alt="../../../_images/msd-win-01.png" class="styled-image align-center" src="/docs-assets/zh-cn/_images/msd-win-01.png" style="width: 90%;"></a>
</div></blockquote>
<ol class="arabic simple" start="3">
<li><p>下载 <a class="reference external" href="https://drive.google.com/file/d/1xJHntgObdPIMpkB6PaLDRbXqNP3-WZt8/view?usp=drive_link">LEAPS-UWBS-Firmware-v1.1.0.zip</a> 文件到您的PC. 使用WinZip或7-Zip等程序解压缩下载文件的内容。</p></li>
<li><p>找到位于 <code class="docutils literal notranslate"><span class="pre">LEAPS-UWBS-Firmware-v1.1.0/LEAPS-UWBS-Firmware-OpenOCD/udk-leaps-uwbs-v1.1.0.bin</span></code> 的二进制文件. 将此文件复制到 LEAPS MSD 驱动器。</p></li>
</ol>
<blockquote>
<div><p>例如，在 Windows 上：</p>
<a class="styled-image reference internal image-reference" href="../../../_images/msd-win-02.png"><img alt="../../../_images/msd-win-02.png" class="styled-image align-center" src="/docs-assets/zh-cn/_images/msd-win-02.png" style="width: 60%;"></a>
</div></blockquote>
<ol class="arabic simple">
<li><p>等待复制和闪存过程，直到复制成功。 在这个过程中，电路板会自动复位，RGB LED 会亮起，硬件会发出哔哔声，表示更新成功。</p></li>
</ol>
<p>设备成功更新了固件. 享受最新的功能和改进。</p>
</div>
<input id="sd-tab-item-1" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-1">
WebUSB</label><div class="sd-tab-content docutils">
<p><strong>准备设置</strong></p>
<ul class="simple">
<li><p>至少一个设备。</p></li>
<li><p>要更新的二进制文件。</p></li>
</ul>
<p><strong>分步说明如何通过 WebUSB 进行更新</strong></p>
<ol class="arabic simple">
<li><p>下载并安装 Node.js。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>请访问 Node.js 官方网站 <a class="reference external" href="https://nodejs.org/en/download">https://nodejs.org/en/download</a>。</p></li>
<li><p>下载推荐的 Node.js 版本。</p></li>
<li><p>运行下载的安装程序，并按照安装提示完成安装。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="2">
<li><p>安装依赖项。</p></li>
</ol>
<blockquote>
<div><ul>
<li><p>在计算机上打开你喜欢的终端应用程序。</p>
<ul class="simple">
<li><p>在 linux 或 macOS 上，类似 <span class="red-text">Terminal</span> 应用程序。</p></li>
<li><p>在 Windows 上，类似 <span class="red-text">Powershell</span> 应用程序。</p></li>
</ul>
</li>
<li><p>要安装 webusb 依赖关系，请运行以下命令:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">npm</span> <span class="n">install</span> <span class="n">webusb</span>
</pre></div>
</div>
</li>
<li><p>接下来，运行以下命令安装 usb 依赖项：</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">npm</span> <span class="n">install</span> <span class="n">usb</span>
</pre></div>
</div>
</li>
<li><p>最后，使用以下命令安装 node-hid 依赖关系：</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">npm</span> <span class="n">install</span> <span class="n">node</span><span class="o">-</span><span class="n">hid</span>
</pre></div>
</div>
</li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="3">
<li><p>使用 USB-C 数据线将设备的 <a class="reference internal" href="/docs/zh/udk/udk-start/device-hw-interfaces#hardware-interface"><span class="std std-ref">USB-C Data Port 2</span></a> 连接到 PC。</p></li>
</ol>
<blockquote>
<div><img alt="../../../_images/leaps-connect-usb-port2.gif" class="styled-image align-center" src="/docs-assets/zh-cn/_images/leaps-connect-usb-port2.gif">
</div></blockquote>
<ol class="arabic simple" start="4">
<li><p>下载并解压缩软件包到你的电脑. 使用 WinZip 或 7-Zip 等程序解压缩下载的 <a class="reference external" href="https://drive.google.com/file/d/1xJHntgObdPIMpkB6PaLDRbXqNP3-WZt8/view?usp=drive_link">LEAPS-UWBS-Firmware-v1.1.0.zip</a> 文件。</p></li>
<li><p>打开网站 <a class="reference external" href="https://armmbed.github.io/dapjs/examples/daplink-flash/web.html">DAPLink Flash</a> 。</p></li>
</ol>
<blockquote>
<div><a class="styled-image reference internal image-reference" href="../../../_images/daplink-flash-web02.png"><img alt="../../../_images/daplink-flash-web02.png" class="styled-image align-center" src="/docs-assets/zh-cn/_images/daplink-flash-web02.png" style="width: 90%;"></a>
</div></blockquote>
<ol class="arabic simple" start="6">
<li><p>点击 <span class="red-text">Choose a firmware image</span> 并转到 <code class="docutils literal notranslate"><span class="pre">LEAPS-UWBS-Firmware-v1.1.0/LEAPS-UWBS-Firmware-OpenOCD/udk-leaps-uwbs-v1.1.0.hex</span></code> 选择二进制文件。</p></li>
</ol>
<blockquote>
<div><a class="styled-image reference internal image-reference" href="../../../_images/daplink-flash-web03.png"><img alt="../../../_images/daplink-flash-web03.png" class="styled-image align-center" src="/docs-assets/zh-cn/_images/daplink-flash-web03.png" style="width: 90%;"></a>
</div></blockquote>
<ol class="arabic simple" start="7">
<li><p>点击 <span class="red-text">SELECT DEVICE</span> 按钮，然后选择连接到 PC 的 DAPLink CMSIS-DAP 端口。</p></li>
</ol>
<blockquote>
<div><a class="styled-image reference internal image-reference" href="../../../_images/daplink-flash-web05.png"><img alt="../../../_images/daplink-flash-web05.png" class="styled-image align-center" src="/docs-assets/zh-cn/_images/daplink-flash-web05.png" style="width: 90%;"></a>
</div></blockquote>
<ol class="arabic simple" start="8">
<li><p>选择固件映像后，二进制文件闪存程序将开始。 在整个过程中，请确保硬件已连接。</p></li>
</ol>
<blockquote>
<div><a class="styled-image reference internal image-reference" href="../../../_images/daplink-flash-web06.png"><img alt="../../../_images/daplink-flash-web06.png" class="styled-image align-center" src="/docs-assets/zh-cn/_images/daplink-flash-web06.png" style="width: 90%;"></a>
</div></blockquote>
<div class="admonition note">
<p class="admonition-title">注解</p>
<p>可能会出现一些意想不到的问题，请断开电路板与电脑的连接，然后重新开始。</p>
</div>
<ol class="arabic simple">
<li><p>在 <span class="red-text">Flash completed!</span> 作为过程的一部分，电路板会自动复位，RGB LED 灯会亮起，硬件会发出哔哔声，表示更新成功。</p></li>
</ol>
<blockquote>
<div><a class="styled-image reference internal image-reference" href="../../../_images/daplink-flash-web07.png"><img alt="../../../_images/daplink-flash-web07.png" class="styled-image align-center" src="/docs-assets/zh-cn/_images/daplink-flash-web07.png" style="width: 90%;"></a>
</div></blockquote>
<p>设备成功更新了固件. 享受最新的功能和改进。</p>
</div>
<input id="sd-tab-item-2" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-2">
串口-COM</label><div class="sd-tab-content docutils">
<p><strong>您需要：</strong></p>
<ul class="simple">
<li><p>至少一个通过 USB 端口连接的设备。</p></li>
<li><p>软件包中包含的脚本和固件二进制文件。</p></li>
<li><p>您系统上安装的 <a class="reference external" href="https://www.python.org/downloads/">python3</a>。</p></li>
</ul>
<p><strong>关于如何通过串口-COM 进行更新的分步说明:</strong></p>
<ol class="arabic simple">
<li><p>下载并解压缩软件包到你的电脑. 使用 WinZip 或 7-Zip 等程序解压缩下载的 <a class="reference external" href="https://drive.google.com/file/d/1xJHntgObdPIMpkB6PaLDRbXqNP3-WZt8/view?usp=drive_link">LEAPS-UWBS-Firmware-v1.1.0.zip</a> 文件。</p></li>
<li><p>打开你喜欢的终端应用程序。</p></li>
</ol>
<ul class="simple">
<li><p>在 linux 或 macOS 上，类似 <span class="red-text">Terminal</span> 应用程序。</p></li>
<li><p>在 Windows 上，类似 <span class="red-text">Powershell</span> 应用程序。</p></li>
</ul>
<ol class="arabic simple" start="3">
<li><p>导航到包含解压缩软件包的文件夹。</p></li>
<li><p>安装 python 依赖项。</p></li>
</ol>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">$ </span>pip<span class="w"> </span>install<span class="w"> </span>pyserial<span class="w"> </span>libusb<span class="w"> </span>tqdm
</pre></div>
</div>
<p>如果 <code class="docutils literal notranslate"><span class="pre">libusb</span></code> 出现错误，请尝试以下操作 <code class="docutils literal notranslate"><span class="pre">sudo</span> <span class="pre">pip</span> <span class="pre">install</span> <span class="pre">libusb</span> <span class="pre">--break-system-package</span></code></p>
<ol class="arabic simple" start="5">
<li><p>可以选择使用两个 port 之一进行更新。</p></li>
</ol>
<p>如果使用 <a class="reference internal" href="/docs/zh/udk/udk-start/device-hw-interfaces#hardware-interface"><span class="std std-ref">USB-C Data Port 1</span></a> ，你可以独立更新 ELDR 二进制文件和 MAIN 二进制文件. 相反，如果使用 <a class="reference internal" href="/docs/zh/udk/udk-start/device-hw-interfaces#hardware-interface"><span class="std std-ref">USB-C Data Port 2</span></a>，则可以同时连续更新多个设备。</p>
<ol class="upperalpha">
<li><p>使用 USB-C 数据线连接设备的 <a class="reference internal" href="/docs/zh/udk/udk-start/device-hw-interfaces#hardware-interface"><span class="std std-ref">USB-C Data Port 1</span></a>。</p>
<blockquote>
<div><img alt="../../../_images/leaps-connect-usb-port1.gif" class="align-center" src="/docs-assets/zh-cn/_images/leaps-connect-usb-port1.gif">
<p>运行以下命令更新 ELDR 和 MAIN 二进制文件。</p>
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
<li><p>使用 USB-C 数据线连接设备的 <a class="reference internal" href="/docs/zh/udk/udk-start/device-hw-interfaces#hardware-interface"><span class="std std-ref">USB-C Data Port 2</span></a>. 运行以下命令更新 ELDR 或 MAIN 二进制文件：</p>
<blockquote>
<div><img alt="../../../_images/leaps-connect-usb-port2.gif" class="align-center" src="/docs-assets/zh-cn/_images/leaps-connect-usb-port2.gif">
<div class="admonition note">
<p class="admonition-title">注解</p>
<p>可能需要安装 udev <a class="reference internal" href="/docs/zh/udk/udk-start/device-hw-interfaces#hardware-interface"><span class="std std-ref">USB-C Data Port 2</span></a> 更新固件. 可以参考类 Debian 发行版的 <a class="reference external" href="https://github.com/NordicSemiconductor/nrf-udev/tree/main">udev 规则安装</a>。</p>
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
<li><p>等待更新完成。</p></li>
<li><p>更新完成后，板子会自动重置。</p></li>
</ol>
<p>设备成功更新了固件. 享受最新的功能和改进。</p>
</div>
<input id="sd-tab-item-3" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-3">
OpenOCD</label><div class="sd-tab-content docutils">
<p><strong>准备设置</strong></p>
<ul class="simple">
<li><p>至少一个设备。</p></li>
<li><p>一个软件包包括一个脚本和一个二进制文件，用于更新。</p></li>
<li><p>已安装 <a class="reference external" href="https://github.com/xpack-dev-tools/openocd-xpack/releases">OpenOCD</a>。</p></li>
</ul>
<p><strong>关于如何通过OpenOCD（片上开放调试器）进行更新的分步说明</strong></p>
<ol class="arabic simple">
<li><p>安装 OpenOCD 调试器。</p></li>
</ol>
<blockquote>
<div><ol class="upperalpha simple">
<li><p>在 Windows 上安装 OpenOCD</p></li>
</ol>
<blockquote>
<div><ol class="loweralpha simple">
<li><p>下载适用于 Windows 的二进制压缩文件。</p></li>
<li><p>解压缩到 <code class="docutils literal notranslate"><span class="pre">C:\xpack-openocd-0.11.0-1</span></code> 文件夹。</p></li>
<li><p>添加路径: <code class="docutils literal notranslate"><span class="pre">C:\xpack-openocd-0.11.0-1\bin</span></code> 到你的 Windows 用户路径环境变量。</p></li>
</ol>
</div></blockquote>
<ol class="upperalpha simple" start="2">
<li><p>在 Linux 或 macOS 上安装 OpenOCD。</p></li>
</ol>
<blockquote>
<div><ol class="loweralpha simple">
<li><p>下载用于 <a class="reference external" href="https://github.com/xpack-dev-tools/openocd-xpack/releases">Linux 的二进制压缩包</a> 。</p></li>
<li><p>解压缩包并安装到本地。</p></li>
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
<li><p>检查 OpenOCD 版本。</p></li>
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
<li><p>下载并解压缩软件包到你的电脑. 使用 WinZip 或 7-Zip 等程序解压缩下载的 <a class="reference external" href="https://drive.google.com/file/d/1xJHntgObdPIMpkB6PaLDRbXqNP3-WZt8/view?usp=drive_link">LEAPS-UWBS-Firmware-v1.1.0.zip</a> 文件。</p></li>
<li><p>打开你喜欢的终端应用程序。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>在 linux 或 macOS 上，类似 <span class="red-text">Terminal</span> 应用程序。</p></li>
<li><p>在 Windows 上，类似 <span class="red-text">Powershell</span> 应用程序。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="5">
<li><p>导航到包含解压缩软件包的文件夹。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p><span class="red-text">cd</span> 转 <span class="red-text">/path/to/LEAPS-UWBS-Firmware-OpenOCD</span>。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="6">
<li><p>使用 USB-C 数据线将设备的 <a class="reference internal" href="/docs/zh/udk/udk-start/device-hw-interfaces#hardware-interface"><span class="std std-ref">USB-C Data Port 2</span></a> 连接到 PC。</p></li>
</ol>
<blockquote>
<div><img alt="../../../_images/leaps-connect-usb-port2.gif" class="styled-image align-center" src="/docs-assets/zh-cn/_images/leaps-connect-usb-port2.gif">
</div></blockquote>
<ol class="arabic simple" start="7">
<li><p>执行脚本自动更新固件。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>在 linux 或 macOS 上，使用 <span class="red-text">udk-leaps-uwbs-firmware.sh</span> 命令。</p></li>
<li><p>在 Windows 上，使用 <span class="red-text">udk-leaps-uwbs-firmware.bat</span> 命令。</p></li>
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
<li><p>更新完成后，设备会发出哔哔声，表示更新成功。 作为更新过程的一部分，电路板会自动复位。</p></li>
</ol>
<p>设备成功更新了固件. 享受最新的功能和改进。</p>
<p><strong>故障排除</strong></p>
<p>如果出现 “错误:无法找到控制核心的 MEM-AP”。</p>
<blockquote>
<div><img alt="../../../_images/firmware-update-error.png" class="align-center" src="/docs-assets/zh-cn/_images/firmware-update-error.png">
</div></blockquote>
<p>请执行以下命令还原：</p>
<blockquote>
<div><div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">openocd</span> <span class="o">-</span><span class="n">f</span> <span class="o">./</span><span class="n">openocd</span><span class="o">-</span><span class="n">swd</span><span class="o">-</span><span class="n">nrf52</span><span class="o">.</span><span class="n">cfg</span> <span class="o">-</span><span class="n">c</span> <span class="s2">"init;nrf52833_workaround;exit_debug_mode;shutdown;sleep 250"</span>
</pre></div>
</div>
</div></blockquote>
<p>然后继续执行 <code class="docutils literal notranslate"><span class="pre">./udk-leaps-uwbs-firmware.sh</span></code>。</p>
</div>
<input id="sd-tab-item-4" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-4">
SEGGER J-Link</label><div class="sd-tab-content docutils">
<p><strong>准备设置</strong></p>
<ul class="simple">
<li><p>至少一个设备。</p></li>
<li><p>要更新的二进制文件. (.hex 或 .bin)</p></li>
<li><p>已安装 <a class="reference external" href="https://www.segger.com/downloads/jlink/#J-LinkSoftwareAndDocumentationPack">SEGGER J-Link</a>。</p></li>
</ul>
<p><strong>关于如何通过 SEGGER J-Link 更新的分步说明</strong></p>
<ol class="arabic simple">
<li><p>安装世纪佳缘 J-Link。</p></li>
</ol>
<blockquote>
<div><div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-5" name="sd-tab-set-1" type="radio">
<label class="sd-tab-label" for="sd-tab-item-5">
Windows</label><div class="sd-tab-content docutils">
<p>找到名为 <code class="docutils literal notranslate"><span class="pre">JLink_Windows_V766_x86_64.exe</span></code> 的Windows下载文件。</p>
<ul class="simple">
<li><p>双击该文件，启动安装程序。</p></li>
<li><p>出现提示时，输入管理密码。</p></li>
<li><p>请阅读并接受许可条款。</p></li>
<li><p>接受默认的安装目标文件夹，通常位于 <code class="docutils literal notranslate"><span class="pre">C:\Program</span> <span class="pre">Files</span> <span class="pre">(x86)\SEGGER\JLink</span></code></p></li>
<li><p>继续接受默认USB驱动程序。</p></li>
</ul>
<p>安装完成后，你会发现系统文件夹中安装了一个文件夹和一组驱动程序文件。 请注意，每次新安装时，这些文件都会被覆盖。</p>
</div>
<input id="sd-tab-item-6" name="sd-tab-set-1" type="radio">
<label class="sd-tab-label" for="sd-tab-item-6">
macOS</label><div class="sd-tab-content docutils">
<p>找到名为 <code class="docutils literal notranslate"><span class="pre">JLink_macOSX_V766_x86_64.pkg</span></code> 的 macOS 下载文件。</p>
<blockquote>
<div><ul class="simple">
<li><p>双击该文件，启动安装程序。</p></li>
<li><p>请阅读并接受许可条款。</p></li>
<li><p>根据提示输入管理密码。 在应用程序文件夹中写入内容需要此密码。</p></li>
</ul>
</div></blockquote>
<p>安装完成后，你会在以下位置找到一个文件夹:<code class="docutils literal notranslate"><span class="pre">/Applications/SEGGER/JLink_V766/</span></code>。 请记住，每个版本都会有不同的文件夹。 这个文件夹会储存与应用程序相关的所有可执行文件和程序库。</p>
</div>
<input id="sd-tab-item-7" name="sd-tab-set-1" type="radio">
<label class="sd-tab-label" for="sd-tab-item-7">
GNU/Linux</label><div class="sd-tab-content docutils">
<p>访问 GNU/Linux 版的 SEGGER 下载站点，并找到所需的软件包. 选择 32/64 位版本。</p>
<blockquote>
<div><ul class="simple">
<li><p>最好下载。tgz文件，并保存到你的电脑里。</p></li>
<li><p>打开终端窗口。</p></li>
</ul>
</div></blockquote>
<p>例如，在Ubuntu (Linux)上，要安装64位.tgz文件，请使用以下命令：</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">mkdir</span> <span class="o">-</span><span class="n">p</span> <span class="o">~/</span><span class="n">opt</span><span class="o">/</span><span class="n">SEGGER</span>
<span class="n">cd</span> <span class="o">~/</span><span class="n">opt</span><span class="o">/</span><span class="n">SEGGER</span>
<span class="n">tar</span> <span class="n">xf</span> <span class="o">~/</span><span class="n">Downloads</span><span class="o">/</span><span class="n">JLink_Linux_V766_x86_64</span><span class="o">.</span><span class="n">tgz</span>
<span class="n">chmod</span> <span class="n">a</span><span class="o">-</span><span class="n">w</span> <span class="o">~/</span><span class="n">opt</span><span class="o">/</span><span class="n">SEGGER</span><span class="o">/</span><span class="n">JLink_Linux_V766_x86_64</span>
<span class="n">ls</span> <span class="o">-</span><span class="n">l</span> <span class="o">~/</span><span class="n">opt</span><span class="o">/</span><span class="n">SEGGER</span><span class="o">/</span><span class="n">JLink_Linux_V766_x86_64</span>
</pre></div>
</div>
<p>执行上述命令后：</p>
<blockquote>
<div><ul class="simple">
<li><p>将在`~/opt/SEGGER`创建一个文件夹。</p></li>
<li><p>下载的.tgz文件内容将被解压缩到`~/opt/SEGGER`文件夹。</p></li>
<li><p><cite>JLink_Linux_V766_x86_64</cite> 文件的权限将被修改。</p></li>
<li><p>可以通过检查 <cite>~/opt/SEGGER/JLink_Linux_V766_x86_64</cite> 文件夹的内容来验证安装。</p></li>
</ul>
</div></blockquote>
<p>请注意，每次新安装时，系统文件夹中的现有文件都会被覆盖。</p>
</div>
</div>
</div></blockquote>
<ol class="arabic simple" start="2">
<li><p>打开SEGGER J-Link，然后闪存二进制文件。</p></li>
</ol>
<blockquote>
<div><div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-8" name="sd-tab-set-2" type="radio">
<label class="sd-tab-label" for="sd-tab-item-8">
J-Link GUI (J-Flash Lite)</label><div class="sd-tab-content docutils">
<ul class="simple">
<li><p>确保安装了最新的 J-Link 软件和文档包。</p></li>
<li><p>将J-Link连接到电脑</p></li>
<li><p>将目标系统连接到J-Link</p></li>
<li><p>启动J-Flash Lite</p></li>
</ul>
<a class="styled-image reference internal image-reference" href="../../../_images/jflashliteexe01.png"><img alt="../../../_images/jflashliteexe01.png" class="styled-image align-center" src="/docs-assets/zh-cn/_images/jflashliteexe01.png" style="width: 542.0px; height: 114.0px;"></a>
<ul class="simple">
<li><p>选择设备, 调试接口和通信速度</p></li>
<li><p>选择文件并点击编程设备或点击擦除芯片</p></li>
<li><p>J-Flash Lite执行请求的操作</p></li>
</ul>
<a class="styled-image reference internal image-reference" href="../../../_images/jflashliteexe02.png"><img alt="../../../_images/jflashliteexe02.png" class="styled-image align-center" src="/docs-assets/zh-cn/_images/jflashliteexe02.png" style="width: 511.0px; height: 576.0px;"></a>
</div>
<input id="sd-tab-item-9" name="sd-tab-set-2" type="radio">
<label class="sd-tab-label" for="sd-tab-item-9">
J-Link指挥官（JLink.exe/JLinkExe）</label><div class="sd-tab-content docutils">
<ul class="simple">
<li><p>确保安装了最新的 J-Link 软件和文档包。</p></li>
<li><p>将J-Link连接到 PC。</p></li>
<li><p>将目标系统连接到J-Link</p></li>
<li><p>启动 J-Link Commander。</p></li>
<li><p>输入以下命令：</p></li>
<li><p>J-Link&gt; device &lt;devicename&gt; // 有关已知设备的列表，请参阅此处</p></li>
<li><p>J-Link&gt; r</p></li>
<li><p>J-Link&gt; h</p></li>
<li><p>J-Link&gt; loadbin &lt;PathToBinFile&gt;, &lt;programmingaddress&gt;</p></li>
<li><p>J-Link Commander 执行 flash下载，并在成功后打印出时间统计。</p></li>
</ul>
</div>
</div>
<p>更新完成后，电路板会自动复位。</p>
</div></blockquote>
</div>
</div>
<p><strong>验证固件并确认成功</strong></p>
<blockquote>
<div><p>打开你喜欢的终端应用程序,</p>
<blockquote>
<div><ul class="simple">
<li><p>在 GNU/Linux 或 macOS 上，如 <span class="red-text">Terminal</span> 应用程序。</p></li>
<li><p>在Windows中，类似 <span class="red-text">Powershell</span> 应用程序。</p></li>
</ul>
</div></blockquote>
<p>例如，在 Ubuntu (Linux) 上，打开 minicom 并按下双回车键：</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">minicom</span> <span class="o">-</span><span class="n">b</span> <span class="mi">115200</span> <span class="o">-</span><span class="n">D</span> <span class="o">/</span><span class="n">dev</span><span class="o">/</span><span class="n">ttyACM0</span>
</pre></div>
</div>
<a class="styled-image reference internal image-reference" href="../../../_images/jflashliteexe05.png"><img alt="../../../_images/jflashliteexe05.png" class="styled-image align-center" src="/docs-assets/zh-cn/_images/jflashliteexe05.png" style="width: 663.0px; height: 418.0px;"></a>
</div></blockquote>
</div>


           </div>
