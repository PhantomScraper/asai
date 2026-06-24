---
title: "LEAPS VMWare"
lang: zh
slug: "leaps-rtls/quick-start-guide/leaps_vmware"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/leaps-rtls/quick-start-guide/leaps_vmware/"
order: 63
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-vmware">
<span id="leaps-qsg-vmware"></span><h1>LEAPS VMWare</h1>
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
<p>安装快捷方便，只需进行一次。</p>
<p id="uivmware"><strong>系统要求</strong></p>
<blockquote>
<div><ul class="simple">
<li><p>台式机设备。</p></li>
<li><p><em>推荐： 一套 UDK (至少五个设备) 来验证。</em></p></li>
<li><p><em>推荐: 为设备供电的电池或 USB-C 电缆。</em></p></li>
<li><p><em>推荐:</em> <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> <em>用于配置设备.</em></p></li>
</ul>
</div></blockquote>
<p><strong>设置说明</strong></p>
<ol class="arabic simple">
<li><p>下载并安装 VMware Player 或 VMware Workstation。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>请访问以下链接，下载所需的软件。</p>
<ul>
<li><p><a class="reference external" href="https://www.vmware.com/uk/products/workstation-player.html">VMware Workstation 播放器</a>。</p></li>
<li><p><a class="reference external" href="https://www.vmware.com/products/workstation-pro/workstation-pro-evaluation.html">VMware Workstation Pro</a>.</p></li>
</ul>
</li>
<li><p>选择与你的操作系统兼容的版本，并按照提供的安装说明进行安装。</p></li>
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
<li><p>提取 VMWare 档案。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>使用 WinZip 或 7-Zip 等程序解压缩下载的 LEAPS VMWare 压缩文件。</p></li>
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
<li><p>浏览解压缩的文件，找到 。ova 文件。</p></li>
<li><p>打开 VMware 应用程序，转到 <span class="red-text">File</span> ” <span class="red-text">导入设备</span>。</p></li>
<li><p>浏览到 。ova 文件，然后点击打开。</p></li>
<li><p>为虚拟机键入一个名称，键入或浏览到虚拟机文件的目录，然后点击导入。</p></li>
<li><p>点击 <span class="red-text">输入</span> 按钮开始导入过程。如果导入失败，请点击重试再试一次，或者点击取消取消导入。</p></li>
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
<li><p>导入完成后，选择导入的虚拟机，然后点击 <span class="red-text">开始</span> 按钮启动它。</p></li>
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
<li><p>默认帐号是 <code class="docutils literal notranslate"><span class="pre">leaps</span></code>，密码是 <code class="docutils literal notranslate"><span class="pre">leaps</span></code>。</p></li>
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
<li><p>默认情况下，网络ID将是 <code class="docutils literal notranslate"><span class="pre">0x1234</span></code>。</p></li>
<li><p>在本例中，需要连接 ID 为 <code class="docutils literal notranslate"><span class="pre">0x83A2</span></code> 的网关板。</p></li>
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
<li><p>将 USB-C 数据线插入电脑上的 <a class="reference internal" href="/docs/zh/udk/udk-start/device-hw-interfaces#hardware-interface"><span class="std std-ref">USB-C数据端口1</span></a>.确保连接稳定。</p>
<img alt="../../../_images/leaps-connect-usb-port1.gif" class="align-center" src="/docs-assets/zh-cn/_images/leaps-connect-usb-port1.gif">
</li>
<li><p>在运行中的 VMWare 中，导航到 <span class="red-text">虚拟机</span> » <span class="red-text">可拆卸设备.</span></p></li>
<li><p>如果在网关模式下连接成功，将听到两声哔哔声作为确认。</p></li>
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
<li><p>使用 <span class="red-text">mosquitto_sub</span> 命令来检查系统状态.这个命令会连接到 Mosquitto MQTT 代理，并显示所有收到的信息。</p></li>
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
<li><p>步骤6中的 IP 地址.如果未显示.使用 <code class="docutils literal notranslate"><span class="pre">sudo</span> <span class="pre">ifconfig</span></code> 命令检查</p>
<ul>
<li><p>本例中为 <code class="docutils literal notranslate"><span class="pre">192.168.26.151</span></code>。</p></li>
</ul>
</li>
</ul>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/windows_vmware_ip_address.png"><img alt="../../../_images/windows_vmware_ip_address.png" src="/docs-assets/zh-cn/_images/windows_vmware_ip_address.png" style="width: 600.5999999999999px; height: 487.2px;"></a>
</div>
<ul>
<li><p>如果无法检查 IP 地址，也可以更改如下配置</p>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/vmware-set-nat.png"><img alt="../../../_images/vmware-set-nat.png" src="/docs-assets/zh-cn/_images/vmware-set-nat.png" style="width: 525.6999999999999px; height: 510.29999999999995px;"></a>
</div>
<ul class="simple">
<li><p>然后，使用 <code class="docutils literal notranslate"><span class="pre">sudo</span> <span class="pre">ifconfig</span></code> 命令进行检查. 本例中为 <code class="docutils literal notranslate"><span class="pre">192.168.146.145</span></code>。</p></li>
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
<li><p>使用您电脑的网页浏览器。</p></li>
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
<li><p>使用用户名 <span class="red-text">admin</span> 和密码 <span class="red-text">admin</span> 登录。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="12">
<li><p><a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> 上的网络。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>检查 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> 中的网络设置，以匹配您所连接的网关板卡的网络 ID。</p></li>
</ul>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/vmware_leaps_center_network.png"><img alt="../../../_images/vmware_leaps_center_network.png" src="/docs-assets/zh-cn/_images/vmware_leaps_center_network.png" style="width: 764.4000000000001px; height: 373.20000000000005px;"></a>
</div>
<ul class="simple">
<li><p>请参阅 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> 和 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> 了解更多关于如何使用应用程序来配置和可视化节点和网络的详情。</p></li>
</ul>
</div></blockquote>
<p>现在系统已经成功设置和配置。 祝您使用愉快！</p>
</div>


           </div>
