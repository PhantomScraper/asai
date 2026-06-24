---
title: "LEAPS Raspberry Pi"
lang: zh
slug: "leaps-rtls/quick-start-guide/infrastructure-rpi"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/leaps-rtls/quick-start-guide/infrastructure-rpi/"
order: 65
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-raspberry-pi">
<span id="leaps-qsg-infrastructure-rpi"></span><h1>LEAPS Raspberry Pi</h1>
<p>本页提供：</p>
<blockquote>
<div><ul class="simple">
<li><p>LEAPS Raspberry Pi 软件包。</p></li>
<li><p>有关系统要求的信息。</p></li>
<li><p>如何安装 LEAPS Raspberry Pi 的说明。</p></li>
</ul>
</div></blockquote>
<p>安装快速简单，只需要完成一次。</p>
<p id="uiraspberrypi"><span class="red-text">开始之前:记住备份 SD 卡中任何你想要保留的重要文件，因为格式化时所有数据都将被永久覆盖。</span></p>
<p><strong>系统要求</strong></p>
<blockquote>
<div><ul class="simple">
<li><p>Raspberry Pi 3B 或更新版本。</p></li>
<li><p><em>推荐： 一套 UDK (至少五个设备) 来验证。</em></p></li>
<li><p><em>推荐： 为设备供电的电池或 USB-C 电缆。</em></p></li>
<li><p><em>推荐:</em> <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> <em>用于配置设备.</em></p></li>
</ul>
</div></blockquote>
<p><strong>设置说明</strong></p>
<ol class="arabic simple">
<li><p>下载 LEAPS Raspberry Pi 镜像。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>LEAPS Docker: <a class="reference external" href="https://drive.google.com/file/d/1VmdslvrcuqN7vf6ppKKLfxMA2PENuYtT/view?usp=drive_link">LEAPS-RPI-IMAGE-v1.1.0.zip</a>.</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="2">
<li><p>提取 LEAPS Raspberry Pi 档案。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>使用 WinZip 或 7-Zip 等程序解压缩下载的 LEAPS Raspberry Pi 压缩文件。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="3">
<li><p>启动 Raspberry Pi 相机。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>您的操作系统可能会尝试阻止安装程序。</p></li>
<li><p><em>在windows上： 如果看到警告信息，请点击</em> <span class="red-text">More info</span> <em>和</em> <span class="red-text">Run anyway</span>。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="4">
<li><p>安装 LEAPS Raspberry Pi 镜像。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>将 SD卡插入电脑或笔记本电脑的 SD 卡插槽。</p></li>
<li><p>打开 Raspberry Pi 映像器。</p></li>
</ul>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/raspberry_pi_imager.png"><img alt="../../../_images/raspberry_pi_imager.png" src="/docs-assets/zh-cn/_images/raspberry_pi_imager.png" style="width: 541.6px; height: 363.20000000000005px;"></a>
</div>
<ul class="simple">
<li><p>选择 <cite>使用自定义</cite>，然后选择你想要安装的 LEAPS Raspberry Pi 镜像。</p></li>
</ul>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/raspberry_pi_image_use_custom.png"><img alt="../../../_images/raspberry_pi_image_use_custom.png" src="/docs-assets/zh-cn/_images/raspberry_pi_image_use_custom.png" style="width: 604.8000000000001px; height: 361.6px;"></a>
</div>
<ul class="simple">
<li><p>选择正确的 SD 卡来安装映像。 在不同的平台上,驱动器可能会有不同的显示方式。</p></li>
</ul>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/choose_the_correct_sd_card.png"><img alt="../../../_images/choose_the_correct_sd_card.png" src="/docs-assets/zh-cn/_images/choose_the_correct_sd_card.png" style="width: 604.8000000000001px; height: 359.20000000000005px;"></a>
</div>
<ul class="simple">
<li><p>请格外注意，根据硬盘的内存容量选择正确的硬盘。</p></li>
<li><p>一旦选择了 LEAPS Raspberry Pi Image 和 SD 卡，就会出现一个新的 <span class="red-text">WRITE</span> 按钮。</p></li>
</ul>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/raspberry_pi_image_write.png"><img alt="../../../_images/raspberry_pi_image_write.png" src="/docs-assets/zh-cn/_images/raspberry_pi_image_write.png" style="width: 607.2px; height: 360.8px;"></a>
</div>
<ul class="simple">
<li><p>点击 <span class="red-text">写</span> 按钮。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="5">
<li><p>写入并完成。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>等待 Raspberry Pi 相机完成写入过程。</p></li>
</ul>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/raspberry_pi_image_writing.png"><img alt="../../../_images/raspberry_pi_image_writing.png" src="/docs-assets/zh-cn/_images/raspberry_pi_image_writing.png" style="width: 605.6px; height: 362.40000000000003px;"></a>
</div>
<ul class="simple">
<li><p>收到确认信息后，你就可以安全地弹出 SD 卡了。</p></li>
</ul>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/raspberry_pi_image_confirm.png"><img alt="../../../_images/raspberry_pi_image_confirm.png" src="/docs-assets/zh-cn/_images/raspberry_pi_image_confirm.png" style="width: 604.8000000000001px; height: 362.40000000000003px;"></a>
</div>
</div></blockquote>
<ol class="arabic simple" start="6">
<li><p>开始使用LEAPS。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>从电脑或笔记本电脑中取出SD卡，并将其插入 Raspberry Pi。</p></li>
<li><p>确保你的 Raspberry Pi 处于开机状态。</p></li>
<li><p>LEAPS 系统已安装并配置为与你的 Raspberry Pi 一起启动。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="7">
<li><p>等待系统启动。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>请耐心等待几分钟，让整个系统完成启动。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="8">
<li><p>使用密码 <code class="docutils literal notranslate"><span class="pre">Leaps1234</span></code> 连接到 Raspberry Pi 广播的 <code class="docutils literal notranslate"><span class="pre">LEAPS-AP</span></code> 网络。</p></li>
</ol>
<blockquote>
<div><div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/connect_leaps_udk_network.png"><img alt="../../../_images/connect_leaps_udk_network.png" src="/docs-assets/zh-cn/_images/connect_leaps_udk_network.png" style="width: 234.0px; height: 64.5px;"></a>
</div>
</div></blockquote>
<ol class="arabic simple" start="9">
<li><p>SSH 进入 Raspberry Pi（可选）。</p></li>
</ol>
<blockquote>
<div><ul>
<li><p>在 PC 上（甚至是另一台 Raspberry Pi），打开 PowerShell 或 Terminal 窗口，然后输入以下命令，通过 SSH 连接 Raspberry Pi。</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">ssh</span> <span class="n">leaps</span><span class="o">@</span><span class="mf">192.168.200.1</span>
</pre></div>
</div>
</li>
<li><p>默认情况下，账户是 <code class="docutils literal notranslate"><span class="pre">leaps</span></code>，密码是 <code class="docutils literal notranslate"><span class="pre">leaps</span></code>。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="10">
<li><p>使用 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> 准备网络。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>配置演示: <a class="reference internal" href="/docs/zh/udk/udk-start/twr-rtls-and-data-telemetry-demo#twr-rtls-and-data-telemetry-demo"><span class="std std-ref">TWR RTLS 和数据遥测演示</span></a> 或 <a class="reference internal" href="/docs/zh/udk/udk-start/uplink-tdoa-rtls-demo#uplink-tdoa-rtls-demo"><span class="std std-ref">上行链路 TDoA RTLS 演示</span></a>。</p></li>
<li><p>默认情况下，网络ID将是 <code class="docutils literal notranslate"><span class="pre">0x1234</span></code>。</p></li>
<li><p>在本例中，你需要连接 ID 为 <code class="docutils literal notranslate"><span class="pre">0x83A2</span></code> 的网关板。</p></li>
</ul>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/raspberry_pi_network_demo01.jpg"><img alt="../../../_images/raspberry_pi_network_demo01.jpg" src="/docs-assets/zh-cn/_images/raspberry_pi_network_demo01.jpg" style="width: 360.0px; height: 800.0px;"></a>
</div>
</div></blockquote>
<ol class="arabic simple" start="11">
<li><p>与网关板连接。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>使用 USB-C 数据线将网关板连接到你的 Raspberry Pi。</p></li>
<li><p>将 USB-C 数据线插入 PC 上的 <a class="reference internal" href="/docs/zh/udk/udk-start/device-hw-interfaces#hardware-interface"><span class="std std-ref">USB-C Data Port 1</span></a>. 确保连接稳定。</p></li>
<li><p>如果在网关模式下成功连接，将听到两声哔哔声作为确认。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="12">
<li><p>检查系统状态（可选）。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>使用 <span class="red-text">mosquitto_sub</span> 命令来检查系统状态. 该命令将连接到 Mosquitto MQTT 代理，并显示所有收到的消息。</p></li>
</ul>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">mosquitto_sub</span> <span class="o">-</span><span class="n">p</span> <span class="mi">1883</span> <span class="o">-</span><span class="n">d</span> <span class="o">-</span><span class="n">v</span> <span class="o">-</span><span class="n">t</span> <span class="s1">'#'</span>
</pre></div>
</div>
</div></blockquote>
<ol class="arabic simple" start="13">
<li><p>访问 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a>。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>在网络浏览器中，访问 <span class="red-text">192.168.200.1/24</span> 的地址. (可以直接在 Raspberry Pi 上打开，或者在连接到 Raspberry Pi 广播的 <code class="docutils literal notranslate"><span class="pre">LEAPS-AP</span></code> 网络的 PC 上打开，密码为 <code class="docutils literal notranslate"><span class="pre">Leaps1234</span></code> - 第 9 步)</p></li>
<li><p>如果你在局域网中，请使用另一台电脑的网页浏览器来访问 Raspberry Pi 的 IP 地址。</p></li>
<li><p>在 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> 中配置网络设置，以匹配您所连接的网关板的网络 ID。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="14">
<li><p>登录 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a>。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>以用户名 <span class="red-text">admin</span> 和密码 <span class="red-text">admin</span> 登录。</p></li>
</ul>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/raspberry_leaps_center_login.png"><img alt="../../../_images/raspberry_leaps_center_login.png" src="/docs-assets/zh-cn/_images/raspberry_leaps_center_login.png" style="width: 762.4000000000001px; height: 370.8px;"></a>
</div>
</div></blockquote>
<ol class="arabic simple" start="15">
<li><p>在 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> 上配置网络。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>检查 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> 中的网络设置，以匹配您所连接的网关板卡的网络 ID。</p></li>
</ul>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/raspberry_pi_leaps_center_udk.png"><img alt="../../../_images/raspberry_pi_leaps_center_udk.png" src="/docs-assets/zh-cn/_images/raspberry_pi_leaps_center_udk.png" style="width: 764.4000000000001px; height: 373.20000000000005px;"></a>
</div>
<ul class="simple">
<li><p>请参阅 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> 和 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> 了解更多关于如何使用应用程序来配置和可视化节点和网络的详情。</p></li>
</ul>
</div></blockquote>
<p>现在系统已经成功设置和配置。 祝您使用愉快！</p>
<div class="admonition note">
<p class="admonition-title">注解</p>
<p><strong>如何重新配置任何网络</strong></p>
<ol class="arabic simple">
<li><p>关闭Raspberry Pi 上的 LEAPS-AP Wi-Fi AP</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>首先，确保关闭 Raspberry Pi 上的 Wi-Fi 接入点 (AP)。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="2">
<li><p>将 Raspberry Pi 连接到所需的网络</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>将你的 Raspberry Pi 连接到你想要使用的以太网或 Wi-Fi 网络。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="3">
<li><p>检查IP 地址</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>在 Raspberry Pi 上打开终端，使用 <code class="docutils literal notranslate"><span class="pre">ifconfig</span></code> 命令检查 IP 地址</p></li>
</ul>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/raspberry_pi_check_ip.png"><img alt="../../../_images/raspberry_pi_check_ip.png" src="/docs-assets/zh-cn/_images/raspberry_pi_check_ip.png" style="width: 413.0px; height: 297.5px;"></a>
</div>
<ul class="simple">
<li><p>记下 IP 地址，例如可能是 <code class="docutils literal notranslate"><span class="pre">192.168.0.104</span></code>。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="4">
<li><p>更新对应的 IP 地址</p></li>
</ol>
<blockquote>
<div><ul>
<li><p>打开 LEAPS Gateway的配置文件：</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">sudo</span> <span class="n">nano</span> <span class="o">/</span><span class="n">usr</span><span class="o">/</span><span class="n">share</span><span class="o">/</span><span class="n">LEAPS</span><span class="o">-</span><span class="n">DOCKER</span><span class="o">-</span><span class="n">LINUX</span><span class="o">/</span><span class="n">leaps</span><span class="o">-</span><span class="n">gateway</span><span class="o">-</span><span class="n">hub</span><span class="o">/</span><span class="n">data</span><span class="o">/</span><span class="n">leaps</span><span class="o">-</span><span class="n">gateway</span><span class="o">.</span><span class="n">conf</span>
</pre></div>
</div>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/raspberry_pi_leaps_gateway.png"><img alt="../../../_images/raspberry_pi_leaps_gateway.png" src="/docs-assets/zh-cn/_images/raspberry_pi_leaps_gateway.png" style="width: 386.5px; height: 271.0px;"></a>
</div>
</li>
<li><p>查找指定 IP 地址的行，并将其更改为 <code class="docutils literal notranslate"><span class="pre">192.168.0.104</span></code>。</p></li>
<li><p>接下来，打开 LEAPS server的配置文件:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">sudo</span> <span class="n">nano</span> <span class="o">/</span><span class="n">usr</span><span class="o">/</span><span class="n">share</span><span class="o">/</span><span class="n">LEAPS</span><span class="o">-</span><span class="n">DOCKER</span><span class="o">-</span><span class="n">LINUX</span><span class="o">/</span><span class="n">leaps</span><span class="o">-</span><span class="n">server</span><span class="o">-</span><span class="n">hub</span><span class="o">/</span><span class="n">data</span><span class="o">/</span><span class="n">leaps</span><span class="o">-</span><span class="n">server</span><span class="o">.</span><span class="n">conf</span>
</pre></div>
</div>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/raspberry_pi_leaps_server.png"><img alt="../../../_images/raspberry_pi_leaps_server.png" src="/docs-assets/zh-cn/_images/raspberry_pi_leaps_server.png" style="width: 387.5px; height: 268.5px;"></a>
</div>
</li>
<li><p>再次更新此文件，以反映新的 IP 地址 <code class="docutils literal notranslate"><span class="pre">192.168.0.104</span></code>。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="5">
<li><p>重新启动 LEAPS server和 LEAPS Gateway</p></li>
</ol>
<blockquote>
<div><ul>
<li><p>修改后，重新启动这两个服务：</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">sudo</span> <span class="n">docker</span> <span class="n">restart</span> <span class="n">leaps_server</span>
</pre></div>
</div>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">sudo</span> <span class="n">docker</span> <span class="n">restart</span> <span class="n">leaps_gateway</span>
</pre></div>
</div>
</li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="6">
<li><p>确认 LEAPS server和LEAPS Gateway工作正常</p></li>
</ol>
<blockquote>
<div><ul>
<li><p>检查正在运行的 Docker 容器的状态：</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>leaps@raspberrypi:~ $ sudo docker ps
CONTAINER ID   IMAGE                          COMMAND                  CREATED      STATUS          PORTS                                                                                  NAMES
b5bc1d479a04   leapslabs/leaps_gateway:udk   "/app/leaps-gateway …"   6 days ago   Up 15 minutes                                                                                          leaps_gateway
68c33d70bc07   leapslabs/leaps_server:udk    "/app/leaps-server -…"   6 days ago   Up 15 minutes   0.0.0.0:7777-&gt;7777/tcp, 0.0.0.0:7777-&gt;7777/udp, :::7777-&gt;7777/tcp, :::7777-&gt;7777/udp   leaps_server
38092ca7b1b1   leapslabs/leaps_center:udk    "sh -c 'cd /app &amp;&amp;  …"   6 days ago   Up 15 minutes   80/tcp, 0.0.0.0:80-&gt;8080/tcp, [::]:80-&gt;8080/tcp                                        leaps_center
</pre></div>
</div>
</li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="7">
<li><p>监控 MQTT 消息</p></li>
</ol>
<blockquote>
<div><ul>
<li><p>要监控 MQTT 消息，请使用:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">mosquitto_sub</span> <span class="o">-</span><span class="n">p</span> <span class="mi">1883</span> <span class="o">-</span><span class="n">d</span> <span class="o">-</span><span class="n">v</span> <span class="o">-</span><span class="n">t</span> <span class="s1">'#'</span>
</pre></div>
</div>
</li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="8">
<li><p>打开 LEAPS Center并更新主机</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>启动 LEAPS Center 应用程序，将主机地址更新为 <code class="docutils literal notranslate"><span class="pre">192.168.0.104</span></code>。</p></li>
<li><p>确保重新加载网络以应用更改。</p></li>
</ul>
</div></blockquote>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/raspberry_pi_leaps_center_reconfig.png"><img alt="../../../_images/raspberry_pi_leaps_center_reconfig.png" src="/docs-assets/zh-cn/_images/raspberry_pi_leaps_center_reconfig.png" style="width: 764.8000000000001px; height: 372.40000000000003px;"></a>
</div>
<div class="line-block">
<div class="line"><br></div>
</div>
</div>
<div class="admonition note">
<p class="admonition-title">注解</p>
<p><strong>如何为 Wi-Fi 接入点设置密码:LEAPS-AP</strong></p>
<blockquote>
<div><p>在 Raspberry Pi OS Bookworm 上设置接入点安全和密码:</p>
<blockquote>
<div><div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">sudo</span> <span class="n">nmcli</span> <span class="n">con</span> <span class="n">modify</span> <span class="n">hotspot</span> <span class="n">wifi</span><span class="o">-</span><span class="n">sec</span><span class="o">.</span><span class="n">key</span><span class="o">-</span><span class="n">mgmt</span> <span class="n">wpa</span><span class="o">-</span><span class="n">psk</span>
<span class="n">sudo</span> <span class="n">nmcli</span> <span class="n">con</span> <span class="n">modify</span> <span class="n">hotspot</span> <span class="n">wifi</span><span class="o">-</span><span class="n">sec</span><span class="o">.</span><span class="n">psk</span> <span class="s2">"Leaps1234"</span>
</pre></div>
</div>
</div></blockquote>
<p>在 Raspberry Pi OS Bullseye 及更早版本上设置接入点：</p>
<blockquote>
<div><ol class="arabic simple">
<li><p>编辑Hostapd配置. 使用此命令打开Hostapd配置文件：</p></li>
</ol>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">sudo</span> <span class="n">nano</span> <span class="o">/</span><span class="n">etc</span><span class="o">/</span><span class="n">hostapd</span><span class="o">/</span><span class="n">hostapd</span><span class="o">.</span><span class="n">conf</span>
</pre></div>
</div>
<ol class="arabic simple" start="2">
<li><p>在文件末尾添加以下参数：</p></li>
</ol>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">wpa</span><span class="o">=</span><span class="mi">2</span>
<span class="n">wpa_passphrase</span><span class="o">=</span><span class="n">Leaps1234</span>
<span class="n">wpa_key_mgmt</span><span class="o">=</span><span class="n">WPA</span><span class="o">-</span><span class="n">PSK</span>
<span class="n">wpa_pairwise</span><span class="o">=</span><span class="n">TKIP</span>
<span class="n">rsn_pairwise</span><span class="o">=</span><span class="n">CCMP</span>
</pre></div>
</div>
<ol class="arabic simple" start="3">
<li><p>保存并退出</p></li>
</ol>
<blockquote>
<div><p>按 <cite>CTRL + O</cite> 保存，然后按 <cite>CTRL + X</cite> 退出编辑器。</p>
</div></blockquote>
<ol class="arabic simple" start="4">
<li><p>重新启动你的 Raspberry Pi</p></li>
</ol>
<blockquote>
<div><p>要应用更改，请重启你的 Raspberry Pi。</p>
</div></blockquote>
</div></blockquote>
</div></blockquote>
</div>
<div class="admonition note">
<p class="admonition-title">注解</p>
<p><strong>Step-by-step instructions to expand the filesystem for LEAPS Raspberry Pi (For versions prior to v1.1.0)</strong></p>
<blockquote>
<div><ol class="arabic simple">
<li><p>Open raspi-config. From a terminal on your Raspberry Pi, run:</p></li>
</ol>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">sudo</span> <span class="n">raspi</span><span class="o">-</span><span class="n">config</span>
</pre></div>
</div>
<ol class="arabic simple" start="2">
<li><p>Navigate to Expand Filesystem. Use the arrow keys and Enter:</p></li>
</ol>
<p><code class="docutils literal notranslate"><span class="pre">Advanced</span> <span class="pre">Options</span></code> -&gt; <code class="docutils literal notranslate"><span class="pre">Expand</span> <span class="pre">Filesystem</span></code></p>
<ol class="arabic simple" start="3">
<li><p>Confirm Expansion. Select <code class="docutils literal notranslate"><span class="pre">OK</span></code> when prompted.</p></li>
</ol>
<p>You’ll see a message saying the root filesystem will be expanded on the next reboot</p>
<ol class="arabic simple" start="4">
<li><p>Reboot. When prompted, choose <code class="docutils literal notranslate"><span class="pre">Yes</span></code> to reboot</p></li>
</ol>
<p>(or manually reboot later with <code class="docutils literal notranslate"><span class="pre">sudo</span> <span class="pre">reboot</span></code>):</p>
<ol class="arabic simple" start="5">
<li><p>Verify (Optional). After reboot, confirm the disk is fully expanded:</p></li>
</ol>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">df</span> <span class="o">-</span><span class="n">h</span> <span class="o">/</span>
</pre></div>
</div>
</div></blockquote>
</div>
</div>


           </div>
