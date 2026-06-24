---
title: "固件更新"
lang: zh
slug: "leaps-rtls/integration-guide/firmware-update"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/leaps-rtls/integration-guide/firmware-update/"
order: 68
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="firmware-update">
<span id="lr-firmware-update"></span><h1>固件更新</h1>
<p>本节提供有关如何更新固件的说明。我们支持多种方式，例如通过 <span class="red-text">SEGGER J-Link</span>, <span class="red-text">OpenOCD</span> 或 <span class="red-text">Serial-COM</span>。</p>
<div class="admonition note">
<p class="admonition-title">注解</p>
<ul class="simple">
<li><p>在更新过程中保持连接，并使用正确的 <span class="red-text">装置</span> 和 <span class="red-text">界面</span>。</p></li>
<li><p><a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/leaps-uwbs#leapsuwbs"><span class="std std-ref">LEAPS UWBS</span></a> 还支持通过BLE进行固件更新，有关更多详细信息，请参阅 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-manager#leaps-manager-fup-over-ble"><span class="std std-ref">通过BLE进行固件更新</span></a>。</p></li>
</ul>
</div>
<p>更多详细信息，请在下面选择您要使用的方法:</p>
<div class="sd-tab-set docutils" id="uidocker">
<input checked="checked" id="sd-tab-item-0" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-0">
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
<input checked="checked" id="sd-tab-item-3" name="sd-tab-set-1" type="radio">
<label class="sd-tab-label" for="sd-tab-item-3">
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
<input id="sd-tab-item-4" name="sd-tab-set-1" type="radio">
<label class="sd-tab-label" for="sd-tab-item-4">
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
<input id="sd-tab-item-5" name="sd-tab-set-1" type="radio">
<label class="sd-tab-label" for="sd-tab-item-5">
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
<input checked="checked" id="sd-tab-item-6" name="sd-tab-set-2" type="radio">
<label class="sd-tab-label" for="sd-tab-item-6">
J-Link图形用户界面（J-Flash Lite）</label><div class="sd-tab-content docutils">
<ul class="simple">
<li><p>确保安装了最新的 J-Link 软件和文档包。</p></li>
<li><p>将J-Link连接到电脑</p></li>
<li><p>将目标系统连接到J-Link</p></li>
<li><p>启动J-Flash Lite</p></li>
</ul>
<a class="reference internal image-reference" href="../../../_images/jflashliteexe03.png"><img alt="../../../_images/jflashliteexe03.png" class="align-center" src="/docs-assets/zh-cn/_images/jflashliteexe03.png" style="width: 541.0px; height: 114.0px;"></a>
<ul class="simple">
<li><p>选择设备, 调试接口和通信速度</p></li>
<li><p>选择文件并点击编程设备或点击擦除芯片</p></li>
<li><p>J-Flash Lite执行请求的操作</p></li>
</ul>
<a class="reference internal image-reference" href="../../../_images/jflashliteexe04.png"><img alt="../../../_images/jflashliteexe04.png" class="align-center" src="/docs-assets/zh-cn/_images/jflashliteexe04.png" style="width: 513.0px; height: 588.0px;"></a>
</div>
<input id="sd-tab-item-7" name="sd-tab-set-2" type="radio">
<label class="sd-tab-label" for="sd-tab-item-7">
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
<input id="sd-tab-item-1" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-1">
OpenOCD</label><div class="sd-tab-content docutils">
<p><strong>准备设置</strong></p>
<ul class="simple">
<li><p>至少一个设备。</p></li>
<li><p>一个软件包包含一个脚本和一个二进制文件，用于更新。</p></li>
<li><p>Installed <a class="reference external" href="https://openocd.org/pages/getting-openocd.html">OpenOCD</a>.</p></li>
</ul>
<p><strong>关于如何通过OpenOCD（片上开放调试器）进行更新的分步说明</strong></p>
<ol class="arabic simple">
<li><p>安装OpenOCD调试器</p></li>
</ol>
<blockquote>
<div><div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-8" name="sd-tab-set-3" type="radio">
<label class="sd-tab-label" for="sd-tab-item-8">
Windows</label><div class="sd-tab-content docutils">
<ul class="simple">
<li><p>下载 <a class="reference external" href="https://github.com/xpack-dev-tools/openocd-xpack/releases">xPack OpenOCD软件包</a> 对于Windows。</p></li>
<li><p>解压缩到 <code class="docutils literal notranslate"><span class="pre">C:\xpack-openocd-0.11.0-1</span></code> 文件夹。</p></li>
<li><p>添加路径: <code class="docutils literal notranslate"><span class="pre">C:\xpack-openocd-0.11.0-1\bin</span></code> 到你的 Windows 用户路径环境变量。</p></li>
</ul>
</div>
<input id="sd-tab-item-9" name="sd-tab-set-3" type="radio">
<label class="sd-tab-label" for="sd-tab-item-9">
macOS</label><div class="sd-tab-content docutils">
<ul class="simple">
<li><p>下载 <a class="reference external" href="https://github.com/xpack-dev-tools/openocd-xpack/releases">xPack OpenOCD软件包</a> 适用于macOS。</p></li>
<li><p>解压缩包并安装到本地。</p></li>
</ul>
<p>例如，要安装xpack-openocd-0.11.0-1-linux-arm.tar.gz文件，请使用以下命令:</p>
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
<li><p>下载 <a class="reference external" href="https://github.com/xpack-dev-tools/openocd-xpack/releases">xPack OpenOCD软件包</a> 对于GNU/Linux。</p></li>
<li><p>解压缩包并安装到本地。</p></li>
</ul>
<p>例如，在Ubuntu（Linux）上，要安装xpack-openocd-0.11.0-1-Linux-arm.tar.gz文件，请使用以下命令:</p>
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
<li><p>检查OpenOCD版本</p></li>
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
<li><p>下载软件包并将其解压缩到您的PC。</p></li>
</ol>
<blockquote>
<div><p>UDK板示例:使用WinZip或7-Zip等程序提取下载的 <cite>待定义</cite> 文件。</p>
</div></blockquote>
<ol class="arabic simple" start="4">
<li><p>打开你喜欢的终端应用程序。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>在 linux 或 macOS 上，类似 <span class="red-text">Terminal</span> 应用程序。</p></li>
<li><p>在Windows中，类似 <span class="red-text">Powershell</span> 应用程序。</p></li>
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
<li><p>使用电缆将设备连接到电脑。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>UDK板示例:使用USB-C数据线将设备的 <a class="reference internal" href="/docs/zh/udk/udk-start/device-hw-interfaces#hardware-interface"><span class="std std-ref">USB-C数据端口2</span></a> 连接到PC。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="7">
<li><p>执行脚本自动更新固件。</p></li>
</ol>
<blockquote>
<div><div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-11" name="sd-tab-set-4" type="radio">
<label class="sd-tab-label" for="sd-tab-item-11">
Windows</label><div class="sd-tab-content docutils">
<p>在 Windows 上，使用 <span class="red-text">udk-leaps-uwbs-firmware.bat</span> 命令。</p>
</div>
<input id="sd-tab-item-12" name="sd-tab-set-4" type="radio">
<label class="sd-tab-label" for="sd-tab-item-12">
macOS</label><div class="sd-tab-content docutils">
<p>在macOS上，使用 <span class="red-text">udk-leaps-uwbs-firmware.sh</span> 命令。</p>
</div>
<input id="sd-tab-item-13" name="sd-tab-set-4" type="radio">
<label class="sd-tab-label" for="sd-tab-item-13">
GNU/Linux</label><div class="sd-tab-content docutils">
<p>在GNU/Linux上，使用 <span class="red-text">udk-leaps-uwbs-firmware.sh</span> 命令。</p>
</div>
</div>
<p>例如，在 Ubuntu (Linux) 上：</p>
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
<li><p>更新完成后，电路板会自动复位。</p></li>
</ol>
</div>
<input id="sd-tab-item-2" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-2">
LEAPS-COM</label><div class="sd-tab-content docutils">
<p><strong>Install LEAPS-COM tool</strong></p>
<p>Follow instructions in section describing <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/leaps-api/leaps-com/how-to-install#install-leapscom"><span class="std std-ref">how to install LEAPS-COM</span></a>.</p>
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
<p>Connect USB data cable to the <a class="reference internal" href="/docs/zh/udk/udk-start/device-hw-interfaces#hardware-interface"><span class="std std-ref">USB port</span></a>.
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
<p>Before update, make sure that BLE is enabled on the devices (see section <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/leaps-api/leaps-com/cmd-execution#discovering-leaps-devices"><span class="std std-ref">Discovering devices</span></a> for more details).
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
<p>Connect USB data cable to the <a class="reference internal" href="/docs/zh/udk/udk-start/device-hw-interfaces#hardware-interface"><span class="std std-ref">Serial port</span></a>.
Execute following command to update Firmware and Extended-Loader over the serial ports.</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">$ </span>python3<span class="w"> </span>-m<span class="w"> </span>leapscom<span class="w"> </span>--dev<span class="w"> </span>/dev/ttyACM0<span class="w"> </span>/dev/ttyACM1<span class="w"> </span>/dev/ttyACM2<span class="w"> </span>--main<span class="w"> </span>main.bin<span class="w"> </span>--eldr<span class="w"> </span>eldr.bin
</pre></div>
</div>
</div>
</div>
</div>
</div>
<p><strong>验证固件并确认成功</strong></p>
<blockquote>
<div><p>打开你喜欢的终端应用程序,</p>
<blockquote>
<div><ul class="simple">
<li><p>在GNU/Linux或macOS上，如 <span class="red-text">终端</span> 应用程序。</p></li>
<li><p>在Windows中，类似 <span class="red-text">Powershell</span> 应用程序。</p></li>
</ul>
</div></blockquote>
<p>例如，在 Ubuntu (Linux) 上，打开 minicom 并按下双回车键：</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">minicom</span> <span class="o">-</span><span class="n">b</span> <span class="mi">115200</span> <span class="o">-</span><span class="n">D</span> <span class="o">/</span><span class="n">dev</span><span class="o">/</span><span class="n">ttyACM0</span>
</pre></div>
</div>
<a class="reference internal image-reference" href="../../../_images/jflashliteexe05.png"><img alt="../../../_images/jflashliteexe05.png" class="align-center" src="/docs-assets/zh-cn/_images/jflashliteexe05.png" style="width: 663.0px; height: 418.0px;"></a>
</div></blockquote>
<hr class="docutils">
<p>对于连接，让我们首先看一下 <a class="reference external" href="https://www.qorvo.com/products/p/DWM1001-DEV">DWM1001-DEV</a> 的主要组件的概述以及 <a class="reference external" href="https://www.qorvo.com/products/p/DWM3001CDK">DWM3001CDK</a> 开发工具包。</p>
<div class="admonition note">
<p class="admonition-title">注解</p>
<p>有关UDK套件，请参阅 <a class="reference internal" href="/docs/zh/udk/udk-start/device-hw-interfaces#hardware-interface"><span class="std std-ref">硬件接口</span></a> 一节中的详细信息</p>
</div>
<a class="reference internal image-reference" href="../../../_images/dwm1001_io.png"><img alt="../../../_images/dwm1001_io.png" class="align-center" src="/docs-assets/zh-cn/_images/dwm1001_io.png" style="width: 696.8000000000001px; height: 357.6px;"></a>
<a class="reference internal image-reference" href="../../../_images/dwm3001c_io.png"><img alt="../../../_images/dwm3001c_io.png" class="align-center" src="/docs-assets/zh-cn/_images/dwm3001c_io.png" style="width: 630.0px; height: 630.0px;"></a>
</div>


           </div>
