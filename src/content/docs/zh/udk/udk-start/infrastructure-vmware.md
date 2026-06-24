---
title: "LEAPS VMWare"
lang: zh
slug: "udk/udk-start/infrastructure-vmware"
section: "udk"
sourceUrl: "https://docs.leapslabs.com/zh-cn/udk/udk-start/infrastructure-vmware/"
order: 39
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-vmware">
<span id="id1"></span><h1>LEAPS VMWare</h1>
<blockquote>
<div><p>本页提供：</p>
<blockquote>
<div><ul class="simple">
<li><p>LEAPS VMWare 软件包。</p></li>
<li><p>有关系统要求的信息。</p></li>
<li><p>如何安装 LEAPS VMWare 的说明。</p></li>
</ul>
</div></blockquote>
</div></blockquote>
<p>安装快速简单，只需要完成一次。</p>
<p id="uivmware"><strong>系统要求</strong></p>
<blockquote>
<div><ul class="simple">
<li><p>台式设备。</p></li>
<li><p><em>推荐： 一组UDK (至少五台设备) 进行验证。</em></p></li>
<li><p><em>推荐：电池或USB-C电缆为设备供电</em></p></li>
<li><p><em>推荐：</em> <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> <em>配置设备</em></p></li>
</ul>
</div></blockquote>
<p><strong>设置说明</strong></p>
<ol class="arabic simple">
<li><p>下载并安装 VMware Player 或 VMware Workstation。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>访问以下链接下载所需软件。</p>
<ul>
<li><p><a class="reference external" href="https://www.vmware.com/uk/products/workstation-player.html">VMware 工作站播放器</a>。</p></li>
<li><p><a class="reference external" href="https://www.vmware.com/products/workstation-pro/workstation-pro-evaluation.html">VMware 工作站播 Pro</a>。</p></li>
</ul>
</li>
<li><p>选择与您的操作系统兼容的版本，并按照提供的安装说明进行操作。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="2">
<li><p>下载 LEAPS VMWare。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>LEAPS VMWare: <a class="reference external" href="https://drive.google.com/file/d/1By5GRLJCnKrMETvIk7INXXEKKhFTtli4/view?usp=drive_link">LEAPS-VMM-IMAGE-v1.1.0.zip</a>.</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="3">
<li><p>提取VMWare存档。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>使用WinZip或7-Zip等程序提取下载的LEAPS VMWare Zip文件。</p></li>
</ul>
</div></blockquote>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/extract_the_vmware_archive.png"><img alt="../../../_images/extract_the_vmware_archive.png" src="/docs-assets/zh-cn/_images/extract_the_vmware_archive.png" style="width: 463.0px; height: 262.0px;"></a>
</div>
<ol class="arabic simple" start="4">
<li><p>导入设备。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>导航到提取的文件并找到.ova文件。</p></li>
<li><p>打开VMware应用程序，然后转到 <span class="red-text">文件</span> » <span class="red-text">导入设备</span>。</p></li>
<li><p>浏览到。ova文件，然后单击“打开。</p></li>
<li><p>键入虚拟机的名称，键入或浏览到虚拟机文件的目录，然后单击“导入。</p></li>
<li><p>单击 <span class="red-text">导入</span> 按钮开始导入过程。 如果导入失败，请单击“重试”重试，或单击“取消”取消导入。</p></li>
</ul>
</div></blockquote>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/import_the_appliance.png"><img alt="../../../_images/import_the_appliance.png" src="/docs-assets/zh-cn/_images/import_the_appliance.png" style="width: 697.9px; height: 477.4px;"></a>
</div>
<ol class="arabic simple" start="5">
<li><p>启动 VMWare。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>导入完成后，选择导入的虚拟机，然后单击 <span class="red-text">Start</span> 按钮启动它。</p></li>
</ul>
</div></blockquote>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/start_the_vmware.png"><img alt="../../../_images/start_the_vmware.png" src="/docs-assets/zh-cn/_images/start_the_vmware.png" style="width: 760.9px; height: 476.7px;"></a>
</div>
<ol class="arabic simple" start="6">
<li><p>等待系统启动。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>请耐心等待几分钟，让整个系统完成启动。</p></li>
<li><p>默认情况下，帐户为 <code class="docutils literal notranslate"><span class="pre">leaps</span></code>，密码为 <code class="docutils literal notranslate"><span class="pre">leaps</span></code>。</p></li>
</ul>
</div></blockquote>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/windows_vmware.png"><img alt="../../../_images/windows_vmware.png" src="/docs-assets/zh-cn/_images/windows_vmware.png" style="width: 600.5999999999999px; height: 487.2px;"></a>
</div>
<ol class="arabic simple" start="7">
<li><p>使用 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> 来准备网络。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>配置演示: <a class="reference internal" href="/docs/zh/udk/udk-start/twr-rtls-and-data-telemetry-demo#twr-rtls-and-data-telemetry-demo"><span class="std std-ref">TWR RTLS 和数据遥测演示</span></a> 或 <a class="reference internal" href="/docs/zh/udk/udk-start/uplink-tdoa-rtls-demo#uplink-tdoa-rtls-demo"><span class="std std-ref">上行链路 TDoA RTLS 演示</span></a>。</p></li>
<li><p>默认情况下，网络ID为 <code class="docutils literal notranslate"><span class="pre">0x1234</span></code>。</p></li>
<li><p>对于此示例，需要连接 ID 为 <code class="docutils literal notranslate"><span class="pre">0x83A2</span></code> 的网关板。</p></li>
</ul>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/vmware_network_demo01.jpg"><img alt="../../../_images/vmware_network_demo01.jpg" src="/docs-assets/zh-cn/_images/vmware_network_demo01.jpg" style="width: 360.0px; height: 800.0px;"></a>
</div>
</div></blockquote>
<ol class="arabic simple" start="8">
<li><p>使用 USB-C 数据线将网关板连接到电脑。</p></li>
</ol>
<blockquote>
<div><ul>
<li><p>将USB-C数据线插入电脑上的 <a class="reference internal" href="/docs/zh/udk/udk-start/device-hw-interfaces#hardware-interface"><span class="std std-ref">USB-C数据端口1</span></a> 确保连接稳定。</p>
<img alt="../../../_images/leaps-connect-usb-port1.gif" class="align-center" src="/docs-assets/zh-cn/_images/leaps-connect-usb-port1.gif">
</li>
<li><p>在正在运行的VMWare中，导航到 <span class="red-text">虚拟机</span>» <span class="red-text">Removable Devices</span></p></li>
<li><p>如果以网关模式成功连接，将听到两声蜂鸣声作为确认。</p></li>
</ul>
</div></blockquote>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/connect_the_gateway_board.png"><img alt="../../../_images/connect_the_gateway_board.png" src="/docs-assets/zh-cn/_images/connect_the_gateway_board.png" style="width: 718.1999999999999px; height: 488.59999999999997px;"></a>
</div>
<ol class="arabic simple" start="9">
<li><p>检查系统状态。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>在 VMWare 中打开终端或命令提示符。</p></li>
<li><p>使用 <span class="red-text">mosquitto_sub</span> 命令检查系统状态.此命令将连接到Mosquitto MQTT代理并显示收到的所有消息。</p></li>
</ul>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">mosquitto_sub</span> <span class="o">-</span><span class="n">p</span> <span class="mi">1883</span> <span class="o">-</span><span class="n">d</span> <span class="o">-</span><span class="n">v</span> <span class="o">-</span><span class="n">t</span> <span class="s1">'#'</span>
</pre></div>
</div>
</div></blockquote>
<ol class="arabic simple" start="10">
<li><p>检查 IP 地址。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>步骤6中的IP地址. 如果未显示. 使用命令 <code class="docutils literal notranslate"><span class="pre">sudo</span> <span class="pre">ifconfig</span></code> 进行检查</p>
<ul>
<li><p>对于这个例子，是 <code class="docutils literal notranslate"><span class="pre">192.168.26.151</span></code>。</p></li>
</ul>
</li>
</ul>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/windows_vmware_ip_address.png"><img alt="../../../_images/windows_vmware_ip_address.png" src="/docs-assets/zh-cn/_images/windows_vmware_ip_address.png" style="width: 600.5999999999999px; height: 487.2px;"></a>
</div>
<ul>
<li><p>或者，如果无法检查 IP 地址，可以按如下方式更改配置。</p>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/vmware-set-nat.png"><img alt="../../../_images/vmware-set-nat.png" src="/docs-assets/zh-cn/_images/vmware-set-nat.png" style="width: 525.6999999999999px; height: 510.29999999999995px;"></a>
</div>
<ul class="simple">
<li><p>然后，使用命令“sudo ifconfig”进行检查. 这个例子是 <code class="docutils literal notranslate"><span class="pre">192.168.146.145</span></code>。</p></li>
</ul>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/vmware-sudo-ipconfig.png"><img alt="../../../_images/vmware-sudo-ipconfig.png" src="/docs-assets/zh-cn/_images/vmware-sudo-ipconfig.png" style="width: 557.1999999999999px; height: 457.79999999999995px;"></a>
</div>
</li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="10">
<li><p>访问 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a>。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>使用计算机的网络浏览器。</p></li>
<li><p>输入 LEAPS VMware 的 IP 地址，以访问 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> 。</p></li>
</ul>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/vmware_leaps_center_login.png"><img alt="../../../_images/vmware_leaps_center_login.png" src="/docs-assets/zh-cn/_images/vmware_leaps_center_login.png" style="width: 762.4000000000001px; height: 370.8px;"></a>
</div>
</div></blockquote>
<ol class="arabic simple" start="11">
<li><p>登录 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a>。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>登录时用户名为 <span class="red-text">admin</span>，密码为 <span class="red-text">admin</span>。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="12">
<li><p>网络位于 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a>。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>检查 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> 中的网络设置，以匹配您连接的网关板的网络ID。</p></li>
</ul>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/vmware_leaps_center_network.png"><img alt="../../../_images/vmware_leaps_center_network.png" src="/docs-assets/zh-cn/_images/vmware_leaps_center_network.png" style="width: 764.4000000000001px; height: 373.20000000000005px;"></a>
</div>
<ul class="simple">
<li><p>有关如何使用应用程序配置和可视化节点和网络的更多详细信息，请参阅 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> 和 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a>。</p></li>
</ul>
</div></blockquote>
<p>现在系统已成功设置并配置。 享受使用它！</p>
</div>


           </div>
