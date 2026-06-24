---
title: "固件更新"
lang: zh
slug: "pans-pro-rtls/quick-start-guide/firmware-update"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/pans-pro-rtls/quick-start-guide/firmware-update/"
order: 89
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="firmware-update">
<span id="qsg-firmware-update"></span><h1>固件更新</h1>
<p>本节介绍更新固件的方法。我们支持许多不同的方式，例如通过 <span class="red-text">Bluetooth</span>，<span class="red-text">SWD</span>，<span class="red-text">OpenOCD</span>，或 <span class="red-text">UWB</span>。</p>
<p>更多详细信息，请在下面选择您要使用的方法:</p>
<div class="sd-tab-set docutils" id="uidocker">
<input checked="checked" id="sd-tab-item-0" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-0">
Bluetooth</label><div class="sd-tab-content docutils">
<p><strong>通过Bluetooth接口</strong></p>
<p>如果想在网络运行时将整个网络更新为新的固件映像，只需通过Bluetooth更新启动器即可。然后，发起者将通过UWB无线电链路自动将新固件传播到所有其他设备。请注意，当启动器首先更新时，它将重新启动网络，当每个设备重新加入网络时，其固件将被更新。因此，在固件更新期间，执行更新的节点将“脱机”。</p>
<p>要开始使用，请下载 <a class="reference internal" href="/docs/zh/pans-pro-rtls/infrastructure/pans-pro-manager#pans-pro-manager"><span class="std std-ref">PANS PRO Manager</span></a> 应用程序（<a class="reference external" href="https://play.google.com/store/apps/details?id=global.leaps.manager.panspro&amp;hl=en">可在Google Play中获得</a>）</p>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/panspro-manager-qr-code.png"><img alt="../../../_images/panspro-manager-qr-code.png" src="/docs-assets/zh-cn/_images/panspro-manager-qr-code.png" style="width: 344.4px; height: 344.4px;"></a>
</div>
<ul class="simple">
<li><p>默认情况下，如果设置允许用户管理，则用户名为 <span class="red-text">admin</span> 的登录帐户和密码为 <span class="red-text">admin</span>。</p></li>
<li><p>访问固件状态。点击应用程序中的 <span class="red-text">选项菜单</span> （<em>表示为三个垂直点</em>）。</p></li>
<li><p>查找 <span class="red-text">Firmware status</span> 选项并选择它。</p></li>
<li><p>选择要更新的设备。</p></li>
</ul>
<a class="reference internal image-reference" href="../../../_images/ppm-network-menu.jpg"><img alt="../../../_images/ppm-network-menu.jpg" src="/docs-assets/zh-cn/_images/ppm-network-menu.jpg" style="width: 40%;"></a>
<a class="reference internal image-reference" href="../../../_images/ppm-firmware-update.jpg"><img alt="../../../_images/ppm-firmware-update.jpg" src="/docs-assets/zh-cn/_images/ppm-firmware-update.jpg" style="width: 40%;"></a>
</div>
<input id="sd-tab-item-1" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-1">
SWD</label><div class="sd-tab-content docutils">
<p><strong>使用SWD编程器进行固件更新</strong></p>
<blockquote>
<div><img alt="../../../_images/image92.png" src="/docs-assets/zh-cn/_images/image92.png">
</div></blockquote>
<p>DWM1001C在LC4/LC5上</p>
<blockquote>
<div><img alt="../../../_images/image101.png" src="/docs-assets/zh-cn/_images/image101.png">
</div></blockquote>
<p>未命名的董事会</p>
<blockquote>
<div><img alt="../../../_images/image111.png" src="/docs-assets/zh-cn/_images/image111.png">
</div></blockquote>
<p><strong>对二进制文件进行编程</strong></p>
<p>在电路板上闪烁出厂图像的必要步骤如下所述。为了重新刷新，有必要使用J-Link或CMIS-DAP编程器。在回流过程中，由于编程器连接器不供电，电路板必须通过USB或电池供电。</p>
<p>J-Flash Light软件工具可用于闪光图像。下面将描述这种方法。另一种方法是使用各种平台上可用的开源工具OpenOCD。PANS PRO软件包包含与OpenOCD一起使用的刷新脚本。</p>
<ol class="arabic">
<li><p>下载并安装Segger J-Flash Lite（J-Link软件套件）:<a class="reference external" href="https://www.segger.com/downloads/jlink/#J">https://www.segger.com/downloads/jlink/#J</a>-链接软件和文档包</p></li>
<li><p>使用微型USB数据线连接模块，如下所示。</p>
<ol class="arabic">
<li><p>LC5网关上DWM1001C模块固件刷新连接</p>
<a class="reference internal image-reference" href="../../../_images/image131.png"><img alt="../../../_images/image131.png" src="/docs-assets/zh-cn/_images/image131.png" style="width: 320.0px; height: 240.0px;"></a>
</li>
<li><p>LC5网关上主机MCU SAME70固件刷新连接</p>
<a class="reference internal image-reference" href="../../../_images/image141.png"><img alt="../../../_images/image141.png" src="/docs-assets/zh-cn/_images/image141.png" style="width: 320.0px; height: 240.0px;"></a>
</li>
</ol>
</li>
<li><p>打开J-Flash Lite。</p></li>
<li><p>选择nrf52832_XXAA作为DWM1001C的设备，SWD作为接口。主机MCU使用ATSAME70N19。使用默认速度1000，然后单击**“确定”**</p>
<a class="reference internal image-reference" href="../../../_images/image15.png"><img alt="../../../_images/image15.png" src="/docs-assets/zh-cn/_images/image15.png" style="width: 384.40000000000003px; height: 126.80000000000001px;"></a>
</li>
<li><p>点击“擦除芯片”进行完全芯片擦除。</p>
<a class="reference internal image-reference" href="../../../_images/image16.png"><img alt="../../../_images/image16.png" src="/docs-assets/zh-cn/_images/image16.png" style="width: 371.5px; height: 327.0px;"></a>
</li>
<li><p>在数据文件中，单击 “…” 并浏览到PANS PRO软件包中提供的十六进制文件进行闪存。然后单击 <strong>“程序设备”</strong> 。固件二进制兼容性</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>请通过 <a class="reference external" href="mailto:apps-support%40leapslabs.com">apps-support<span>@</span>leapslabs<span>.</span>com</a> 联系我们获取下载软件包。</p></li>
</ul>
</div></blockquote>
<table class="docutils align-default">
<colgroup>
<col style="width: 31%">
<col style="width: 36%">
<col style="width: 34%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>固件文件</strong></p></th>
<th class="head"><p><strong>目标</strong></p></th>
<th class="head"><p><strong>刷新地址</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>pan-pro-all-dwm1001c-vY.XX.hex</p></td>
<td><p>LC4标签和LC5网关上的DWM1001C模块</p></td>
<td><p>0x00000000</p></td>
</tr>
<tr class="row-odd"><td><p>pans-pro-all-lc5s-vY.XX.hex</p></td>
<td><p>LC5网关上的主机MCU SAME70</p></td>
<td><p>0x00400000</p></td>
</tr>
</tbody>
</table>
</div>
<input id="sd-tab-item-2" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-2">
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
<li><p>下载软件包并将其解压缩到PC. 使用WinZip或7-Zip等程序解压缩下载的文件。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>请通过 <a class="reference external" href="mailto:apps-support%40leapslabs.com">apps-support<span>@</span>leapslabs<span>.</span>com</a> 联系我们获取下载软件包。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="4">
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
<li><p><span class="red-text">cd</span> 到 <span class="red-text">/path/to/PANSPRO固件OpenOCD</span></p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="6">
<li><p>使用Micro USB数据线将设备的 <code class="docutils literal notranslate"><span class="pre">Micro</span> <span class="pre">USB数据端口</span></code> 连接到您的PC。</p></li>
<li><p>执行脚本自动更新固件。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>在linux或macOS上，使用 <span class="red-text">reflash-panspro-rtls-2ab.sh</span> 命令。</p></li>
<li><p>在Windows上，使用 <span class="red-text">reflash-panspro-rtls-2ab.bat</span> 命令。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="8">
<li><p>更新完成后，设备会发出哔哔声，表示更新成功。 作为更新过程的一部分，电路板会自动复位。</p></li>
</ol>
<p>设备成功更新了固件. 享受最新的功能和改进。</p>
</div>
<input id="sd-tab-item-3" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-3">
UWB</label><div class="sd-tab-content docutils">
<p>RTLS网络组建时，启动锚会指定网络所需的固件版本。 启用固件自动更新后，任何希望参与（加入）网络的设备都必须拥有相同的固件（版本号和校验和）。 如果新设备没有正确的固件，将按照下面的小节进行更新。</p>
<p><strong>通过UWB接口</strong></p>
<p>正如 DWM1001 系统概述[4]中所介绍的，节点会将自己的固件版本与想要加入的网络进行比较。 如果固件版本不同，节点会尝试在加入前更新固件。 固件更新功能可在配置中启用/禁用。 这里列出了节点将遵循的功能规则。</p>
<p><strong>标签:</strong></p>
<ul class="simple">
<li><p>启用后，标签将始终检查固件版本，并在开始测距之前，通过向网络中附近的锚节点发送更新请求，尝试将其固件版本与网络同步。</p></li>
<li><p>禁用时，标签将开始测距，而不检查固件版本。这可能会导致版本兼容性问题，必须非常小心地处理。</p></li>
</ul>
<p><strong>锚点:</strong></p>
<ul class="simple">
<li><p>启用后，在加入网络之前，锚点将检查固件版本，并通过向附近的锚点节点发送更新请求，尝试将其固件版本与网络同步。加入网络后，锚点将响应附近节点更新固件的请求。</p></li>
<li><p>禁用后，在加入网络之前，锚点将直接发送加入请求，而不检查固件版本。这可能会导致版本兼容性问题，必须非常小心地处理。加入网络后，锚点将忽略来自附近节点的固件更新请求。</p></li>
</ul>
</div>
</div>
</div>


           </div>
