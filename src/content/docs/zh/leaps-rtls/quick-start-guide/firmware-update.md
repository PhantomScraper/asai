---
title: "固件更新"
lang: zh
slug: "leaps-rtls/quick-start-guide/firmware-update"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/leaps-rtls/quick-start-guide/firmware-update/"
order: 62
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="firmware-update">
<span id="leaps-qsg-fw-update"></span><h1>固件更新</h1>
<p>本节介绍更新固件的方法. 我们支持多种不同的方式，例如 <span class="red-text">Bluetooth</span>, <span class="red-text">MSD</span>, <span class="red-text">WebUSB</span>, <span class="red-text">Serial-COM</span> 或 <span class="red-text">OpenOCD</span>。</p>
<p>更多详细信息，请在下面选择您要使用的方法:</p>
<div class="sd-tab-set docutils" id="uidocker">
<input checked="checked" id="sd-tab-item-0" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-0">
Bluetooth</label><div class="sd-tab-content docutils">
<div class="figure align-right" id="id4">
<a class="reference internal image-reference" href="../../../_images/leaps-manager-qr-code.png"><img alt="../../../_images/leaps-manager-qr-code.png" src="/docs-assets/zh-cn/_images/leaps-manager-qr-code.png" style="width: 112.5px; height: 112.5px;"></a>
<p class="caption"><span class="caption-text"><a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> on <a class="reference external" href="https://play.google.com/store/apps/details?id=global.leaps.manager.leaps&amp;hl=en_GB&amp;gl=US">Google Play</a></span></p>
</div>
<p><strong>准备设置</strong></p>
<ul class="simple">
<li><p>至少一个设备。</p></li>
<li><p>在 Android 设备上安装了 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> 应用程序。</p></li>
</ul>
<div class="admonition note">
<p class="admonition-title">注解</p>
<ul class="simple">
<li><p>确保更新过程中的连接，并避免在Bluetooth连接时移动太远。</p></li>
<li><p>固件更新速度取决于Bluetooth设备。 例如，Bluetooth 4.2 和Bluetooth 5.0 的数据传输速率分别为 1Mbps 和 2Mbps。</p></li>
</ul>
</div>
<p><strong>逐步说明如何通过Bluetooth进行更新:</strong></p>
<p>1.打开 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> 应用程序，然后导航到 <span class="red-text">Demo Selector</span>. 此外，你还可以导航到创建的网络，更新网络中的设备。</p>
<ol class="arabic" start="2">
<li><p>访问固件状态。点击应用程序中的 <span class="red-text">选项菜单</span> （<em>表示为三个垂直点</em>）。查找 <span class="red-text">固件状态</span> 选项并选择它。</p>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/firmware-update9.jpg"><img alt="../../../_images/firmware-update9.jpg" src="/docs-assets/zh-cn/_images/firmware-update9.jpg" style="width: 45%;"></a>
<a class="reference internal image-reference" href="../../../_images/firmware-update10.jpg"><img alt="../../../_images/firmware-update10.jpg" src="/docs-assets/zh-cn/_images/firmware-update10.jpg" style="width: 45%;"></a>
<div class="line-block">
<div class="line"><br></div>
</div>
</div></blockquote>
</li>
<li><p>选择要更新的设备。</p></li>
</ol>
<blockquote>
<div><ul>
<li><p>从显示的设备列表中，选择要更新固件的设备。</p></li>
<li><p>red: “更新” 按钮位于应用程序界面的左下角，点击它就可以启动所选设备的固件更新过程。</p>
<a class="reference internal image-reference" href="../../../_images/firmware-update8.jpg"><img alt="../../../_images/firmware-update8.jpg" src="/docs-assets/zh-cn/_images/firmware-update8.jpg" style="width: 45%;"></a>
<a class="reference internal image-reference" href="../../../_images/firmware-update5.jpg"><img alt="../../../_images/firmware-update5.jpg" src="/docs-assets/zh-cn/_images/firmware-update5.jpg" style="width: 45%;"></a>
<div class="line-block">
<div class="line"><br></div>
</div>
</li>
</ul>
</div></blockquote>
<ol class="arabic" start="4">
<li><p>应用程序将提供可视化指标或进度条，显示更新的进行情况. 请耐心等待更新过程。</p>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/firmware-update7.jpg"><img alt="../../../_images/firmware-update7.jpg" src="/docs-assets/zh-cn/_images/firmware-update7.jpg" style="width: 45%;"></a>
<a class="reference internal image-reference" href="../../../_images/firmware-update1.jpg"><img alt="../../../_images/firmware-update1.jpg" src="/docs-assets/zh-cn/_images/firmware-update1.jpg" style="width: 45%;"></a>
<div class="line-block">
<div class="line"><br></div>
</div>
</div></blockquote>
</li>
<li><p>更新完成后，你会看到 <span class="red-text">状态已完成</span>。 此外，设备会发出哔哔声，表示更新成功。 更新过程中，电路板会自动复位。</p>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/firmware-update3.jpg"><img alt="../../../_images/firmware-update3.jpg" src="/docs-assets/zh-cn/_images/firmware-update3.jpg" style="width: 45%;"></a>
<a class="reference internal image-reference" href="../../../_images/firmware-update2.jpg"><img alt="../../../_images/firmware-update2.jpg" src="/docs-assets/zh-cn/_images/firmware-update2.jpg" style="width: 45%;"></a>
</div></blockquote>
</li>
</ol>
<p>设备成功更新了固件. 享受最新的功能和改进。</p>
</div>
<input id="sd-tab-item-1" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-1">
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
<div><img alt="../../../_images/leaps-connect-usb-port2.gif" class="align-center" src="/docs-assets/zh-cn/_images/leaps-connect-usb-port2.gif">
</div></blockquote>
<ol class="arabic simple" start="2">
<li><p>连接后，LEAPS MSD 驱动器将出现在电脑上。 打开 LEAPS MSD 驱动器。</p></li>
</ol>
<blockquote>
<div><p>例如，在 Windows 上：</p>
<a class="reference internal image-reference" href="../../../_images/msd-win-01.png"><img alt="../../../_images/msd-win-01.png" class="align-center" src="/docs-assets/zh-cn/_images/msd-win-01.png" style="width: 90%;"></a>
</div></blockquote>
<ol class="arabic simple" start="3">
<li><p>下载 <a class="reference external" href="https://drive.google.com/file/d/1xJHntgObdPIMpkB6PaLDRbXqNP3-WZt8/view?usp=drive_link">LEAPS-UWBS-Firmware-v1.1.0.zip</a> 文件到你的电脑. 使用 WinZip 或 7-Zip 等程序解压缩下载的文件内容。</p></li>
<li><p>找到位于 <code class="docutils literal notranslate"><span class="pre">LEAPS-UWBS-Firmware-v1.1.0/LEAPS-UWBS-Firmware-OpenOCD/udk-leaps-uwbs-v1.1.0.bin</span></code> 的二进制文件. 将此文件复制到 LEAPS MSD 驱动器。</p></li>
</ol>
<blockquote>
<div><p>例如，在 Windows 上：</p>
<a class="reference internal image-reference" href="../../../_images/msd-win-02.png"><img alt="../../../_images/msd-win-02.png" class="align-center" src="/docs-assets/zh-cn/_images/msd-win-02.png" style="width: 60%;"></a>
</div></blockquote>
<ol class="arabic simple" start="5">
<li><p>等待复制和闪存过程，直到复制成功。 在这个过程中，电路板会自动复位，RGB LED 会亮起，硬件会发出哔哔声，表示更新成功。</p></li>
</ol>
<p>设备成功更新了固件. 享受最新的功能和改进。</p>
</div>
<input id="sd-tab-item-2" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-2">
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
<li><p>在电脑上打开你喜欢的终端应用程序。</p>
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
<div><img alt="../../../_images/leaps-connect-usb-port2.gif" class="align-center" src="/docs-assets/zh-cn/_images/leaps-connect-usb-port2.gif">
</div></blockquote>
<ol class="arabic simple" start="4">
<li><p>下载并解压缩软件包到你的电脑. 使用 WinZip 或 7-Zip 等程序解压缩下载的 <a class="reference external" href="https://drive.google.com/file/d/1xJHntgObdPIMpkB6PaLDRbXqNP3-WZt8/view?usp=drive_link">LEAPS-UWBS-Firmware-v1.1.0.zip</a> file。</p></li>
<li><p>打开网站 <a class="reference external" href="https://armmbed.github.io/dapjs/examples/daplink-flash/web.html">DAPLink Flash</a> 。</p></li>
</ol>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/daplink-flash-web02.png"><img alt="../../../_images/daplink-flash-web02.png" class="align-center" src="/docs-assets/zh-cn/_images/daplink-flash-web02.png" style="width: 90%;"></a>
</div></blockquote>
<ol class="arabic simple" start="6">
<li><p>点击 <span class="red-text">Choose a firmware image</span> 并转到 <code class="docutils literal notranslate"><span class="pre">LEAPS-UWBS-Firmware-v1.1.0/LEAPS-UWBS-Firmware-OpenOCD/udk-leaps-uwbs-v1.1.0.hex</span></code> 选择二进制文件。</p></li>
</ol>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/daplink-flash-web03.png"><img alt="../../../_images/daplink-flash-web03.png" class="align-center" src="/docs-assets/zh-cn/_images/daplink-flash-web03.png" style="width: 90%;"></a>
</div></blockquote>
<ol class="arabic simple" start="5">
<li><p>点击 <span class="red-text">SELECT DEVICE</span> 按钮，然后选择连接到 PC 的 DAPLink CMSIS-DAP 端口。</p></li>
</ol>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/daplink-flash-web05.png"><img alt="../../../_images/daplink-flash-web05.png" class="align-center" src="/docs-assets/zh-cn/_images/daplink-flash-web05.png" style="width: 90%;"></a>
</div></blockquote>
<ol class="arabic simple" start="6">
<li><p>选择固件映像后，二进制文件闪存程序将开始。 在整个过程中，请确保硬件连接正常。</p></li>
</ol>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/daplink-flash-web06.png"><img alt="../../../_images/daplink-flash-web06.png" class="align-center" src="/docs-assets/zh-cn/_images/daplink-flash-web06.png" style="width: 90%;"></a>
</div></blockquote>
<div class="admonition note">
<p class="admonition-title">注解</p>
<p>可能会出现一些意外问题，请断开电路板与电脑的连接，然后重新开始。</p>
</div>
<ol class="arabic simple" start="7">
<li><p>在发出 <span class="red-text">Flash completed!</span> (“刷新完成”) 之后. 电路板会自动复位，RGB LED 灯会亮起，硬件会发出哔哔声，表示更新成功。</p></li>
</ol>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/daplink-flash-web07.png"><img alt="../../../_images/daplink-flash-web07.png" class="align-center" src="/docs-assets/zh-cn/_images/daplink-flash-web07.png" style="width: 90%;"></a>
</div></blockquote>
<p>设备成功更新了固件. 享受最新的功能和改进。</p>
</div>
<input id="sd-tab-item-3" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-3">
Serial-COM</label><div class="sd-tab-content docutils">
<p><strong>您需要：</strong></p>
<ul class="simple">
<li><p>至少一个通过 USB 端口连接的设备。</p></li>
<li><p>软件包中包含的脚本和固件二进制文件。</p></li>
<li><p>您系统上安装的 <a class="reference external" href="https://www.python.org/downloads/">python3</a>。</p></li>
</ul>
<p><strong>分步说明如何通过串行-COM 进行更新：</strong></p>
<ol class="arabic simple">
<li><p>下载并解压缩软件包到你的电脑. 使用 WinZip 或 7-Zip 等程序解压缩下载的 <a class="reference external" href="https://drive.google.com/file/d/1xJHntgObdPIMpkB6PaLDRbXqNP3-WZt8/view?usp=drive_link">LEAPS-UWBS-Firmware-v1.1.0.zip</a> file。</p></li>
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
<p>如果 <code class="docutils literal notranslate"><span class="pre">libusb</span></code> 出现错误，请尝试以下操作 <code class="docutils literal notranslate"><span class="pre">sudo</span> <span class="pre">pip</span> <span class="pre">install</span> <span class="pre">libusb</span>&nbsp; <span class="pre">--break-system-package</span></code></p>
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
<p>可能需要安装 udev 规则才能通过 <a class="reference internal" href="/docs/zh/udk/udk-start/device-hw-interfaces#hardware-interface"><span class="std std-ref">USB-C Data Port 2</span></a> 更新固件. 可以参考类 Debian 发行版的 <a class="reference external" href="https://github.com/NordicSemiconductor/nrf-udev/tree/main">udev 规则安装</a>。</p>
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
<input id="sd-tab-item-4" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-4">
OpenOCD</label><div class="sd-tab-content docutils">
<p><strong>准备设置</strong></p>
<ul class="simple">
<li><p>至少一个设备。</p></li>
<li><p>一个软件包包含一个脚本和一个二进制文件，用于更新。</p></li>
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
<li><p>下载并解压缩软件包到你的电脑. 使用 WinZip 或 7-Zip 等程序解压缩下载的 <a class="reference external" href="https://drive.google.com/file/d/1xJHntgObdPIMpkB6PaLDRbXqNP3-WZt8/view?usp=drive_link">LEAPS-UWBS-Firmware-v1.1.0.zip</a> file。</p></li>
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
<li><p><span class="red-text">cd</span> 到 <span class="red-text">/path/to/LEAPS-UWBS-Firmware-OpenOCD</span>。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="6">
<li><p>使用 USB-C 数据线将 <a class="reference internal" href="/docs/zh/udk/udk-start/device-hw-interfaces#hardware-interface"><span class="std std-ref">USB-C Data Port 2</span></a> 的设备连接到 PC。</p></li>
</ol>
<blockquote>
<div><img alt="../../../_images/leaps-connect-usb-port2.gif" class="align-center" src="/docs-assets/zh-cn/_images/leaps-connect-usb-port2.gif">
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
</div>
<div class="admonition note">
<p class="admonition-title">注解</p>
<ul class="simple">
<li><p>如果您对我们的产品有任何意见或问题，我们鼓励您访问我们的 <a class="reference external" href="https://forum.leapslabs.com">LEAPS 论坛</a>。</p></li>
<li><p>有关已知限制和问题列表的详情，请参阅 <a class="reference internal" href="/docs/zh/udk/release#udk-releases"><span class="std std-ref">发布</span></a> 部分。</p></li>
</ul>
</div>
</div>


           </div>
