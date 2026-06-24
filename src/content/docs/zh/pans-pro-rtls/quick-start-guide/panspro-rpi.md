---
title: "PANS PRO Raspberry Pi"
lang: zh
slug: "pans-pro-rtls/quick-start-guide/panspro-rpi"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/pans-pro-rtls/quick-start-guide/panspro-rpi/"
order: 91
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="pans-pro-raspberry-pi">
<span id="panspro-rpi"></span><h1>PANS PRO Raspberry Pi</h1>
<p>本页提供：</p>
<blockquote>
<div><ul class="simple">
<li><p>PANS PRO Raspberry Pi 软件包。</p></li>
<li><p>有关系统要求的信息。</p></li>
<li><p>如何安装PANS PRO Raspberry Pi的说明。</p></li>
</ul>
</div></blockquote>
<p>安装快速简单，只需要完成一次。</p>
<p id="uiraspberrypi"><span class="red-text">开始之前:记住备份 SD 卡中任何你想要保留的重要文件，因为格式化时所有数据都将被永久覆盖。</span></p>
<p><strong>系统要求</strong></p>
<blockquote>
<div><ul class="simple">
<li><p>Raspberry Pi 3B 或更新版本。</p></li>
<li><p><em>推荐： 一组设备（至少五台设备）进行验证。</em></p></li>
<li><p><em>建议：电池或微型 USB 电缆为设备供电。</em></p></li>
<li><p><em>推荐:</em> <a class="reference internal" href="/docs/zh/pans-pro-rtls/infrastructure/pans-pro-manager#pans-pro-manager"><span class="std std-ref">PANS PRO Manager</span></a> <em>用于配置设备.</em></p></li>
</ul>
</div></blockquote>
<p><strong>设置说明</strong></p>
<ol class="arabic simple">
<li><p>下载 PANS PRO Raspberry Pi 镜像。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>请通过 <a class="reference external" href="mailto:apps-support%40leapslabs.com">apps-support<span>@</span>leapslabs<span>.</span>com</a> 联系我们获取下载软件包。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="2">
<li><p>解压缩 PANS PRO Raspberry Pi 档案。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>使用 WinZip 或 7-Zip 等程序解压缩下载的 PANS PRO Raspberry Pi 压缩文件。</p></li>
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
<li><p>安装 PANS PRO Raspberry Pi 镜像。</p></li>
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
<li><p>选择 <cite>使用自定义</cite>,然后选择你想要安装的 PANS PRO Raspberry Pi 镜像。</p></li>
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
<li><p>一旦选择了 PANS PRO Raspberry Pi Image 和 SD 卡，一个新的 <span class="red-text">WRITE</span> 按钮就会出现。</p></li>
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
<li><p>开始使用 PANS PRO。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>从电脑或笔记本电脑中取出SD卡，并将其插入 Raspberry Pi。</p></li>
<li><p>确保你的 Raspberry Pi 处于开机状态。</p></li>
<li><p>PANS PRO系统已安装并配置为与你的 Raspberry Pi 一起启动。</p></li>
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
<li><p>使用 <a class="reference internal" href="/docs/zh/pans-pro-rtls/infrastructure/pans-pro-manager#pans-pro-manager"><span class="std std-ref">PANS PRO Manager</span></a> 准备网络，并确定 <code class="docutils literal notranslate"><span class="pre">网络</span> <span class="pre">ID</span></code>。</p></li>
<li><p>配置并连接网关板。</p></li>
</ol>
<blockquote>
<div><p>11.1. 打开配置文件。</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">sudo nano /usr/share/LEAPS-DOCKER-LINUX/leaps-server-hub/data/leaps-server.conf</span>
</pre></div>
</div>
</div></blockquote>
<p>11.2. 更新 LEAPS Server配置。</p>
<blockquote>
<div><ul class="simple">
<li><p>将 MQTT API 变体更改为 “平移”：</p></li>
</ul>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">mqtt_api = pans</span>
</pre></div>
</div>
</div></blockquote>
<p>11.3. 重新启动 LEAPS Server。</p>
<blockquote>
<div><ul class="simple">
<li><p>保存更改后，重新启动服务:</p></li>
</ul>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">sudo docker restart leaps_server</span>
</pre></div>
</div>
</div></blockquote>
<p>11.4。 确认 LEAPS Server状态。</p>
<blockquote>
<div><ul class="simple">
<li><p>检查正在运行的 Docker 容器的状态：</p></li>
</ul>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">leaps@raspberrypi:~ $ </span>sudo<span class="w"> </span>docker<span class="w"> </span>ps
<span class="go">CONTAINER ID        IMAGE                           COMMAND                  CREATED        STATUS              PORTS                                                  NAMES</span>
<span class="go">68c33d70bc07        leapslabs/leaps_server:udk    "/app/leaps-server -..." 6 days ago     Up 15 minutes       0.0.0.0:7777-&gt;7777/tcp, 0.0.0.0:7777-&gt;7777/udp, :::7777-&gt;7777/tcp, :::7777-&gt;7777/udp   leaps_server</span>
<span class="go">38092ca7b1b1        leapslabs/leaps_center:udk     "sh -c 'cd /app &amp;&amp; ..." 6 days ago     Up 15 minutes       80/tcp, 0.0.0.0:80-&gt;8080/tcp, [::]:80-&gt;8080/tcp                    leaps_center</span>
</pre></div>
</div>
</div></blockquote>
<p>11.5。 Raspberry PI以太网直接连接到网关板，或与网关板连接到单独的交换机。</p>
<blockquote>
<div><ul class="simple">
<li><p>IP 地址 192.168.200.1</p></li>
<li><p>网络掩码:255.255.255.0</p></li>
</ul>
<p>注意：它可以连接到你的普通交换机/路由器，但 IP 地址可能会冲突。 Raspberry PI 的以太网配置如下</p>
</div></blockquote>
<p>11.6。 检查网关板上的网络 ID 是否与 UWB 网络匹配。 请进一步参阅 “网络快速入门” 中的 “网关配置”。</p>
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
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/leaps_center_login.png"><img alt="../../../_images/leaps_center_login.png" src="/docs-assets/zh-cn/_images/leaps_center_login.png" style="width: 762.8000000000001px; height: 360.0px;"></a>
</div>
</div></blockquote>
<ol class="arabic simple" start="14">
<li><p>登录 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a>。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>以用户名 <span class="red-text">admin</span> 和密码 <span class="red-text">admin</span> 登录。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="15">
<li><p>在 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> 上配置网络。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>检查 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> 中的网络设置，以匹配您所连接的网关板卡的网络 ID。</p></li>
</ul>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/leaps_center_pans.png"><img alt="../../../_images/leaps_center_pans.png" src="/docs-assets/zh-cn/_images/leaps_center_pans.png" style="width: 764.4000000000001px; height: 360.40000000000003px;"></a>
</div>
<ul class="simple">
<li><p>请参阅 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> 和 <a class="reference internal" href="/docs/zh/pans-pro-rtls/infrastructure/pans-pro-manager#pans-pro-manager"><span class="std std-ref">PANS PRO Manager</span></a> 了解更多关于如何使用应用程序来配置和可视化节点和网络的详情。</p></li>
</ul>
</div></blockquote>
<p>现在系统已经成功设置和配置。 祝您使用愉快！</p>
</div>


           </div>
