---
title: "PANS PRO Docker"
lang: zh
slug: "pans-pro-rtls/quick-start-guide/panspro-docker"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/pans-pro-rtls/quick-start-guide/panspro-docker/"
order: 90
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="pans-pro-docker">
<span id="panspro-docker"></span><h1>PANS PRO Docker</h1>
<p>本页提供：</p>
<blockquote>
<div><ul class="simple">
<li><p>PANS PRO Docker 软件包。</p></li>
<li><p>有关系统要求的信息。</p></li>
<li><p>如何安装 PANS PRO Docker 的说明。</p></li>
</ul>
</div></blockquote>
<p>安装快速简单，只需要完成一次。</p>
<div class="admonition-disclaimer admonition">
<p class="admonition-title">免责声明</p>
<p><a class="reference internal" href="#panspro-docker"><span class="std std-ref">PANS PRO Docker</span></a> 仅供专业人士安装. 出于演示目的 <a class="reference internal" href="/docs/zh/pans-pro-rtls/quick-start-guide/panspro-rpi#panspro-rpi"><span class="std std-ref">PANS PRO Raspberry Pi</span></a> 是更好的选择。</p>
</div>
<p>访问官方的 Docker了解更多关于 <a class="reference external" href="https://docs.docker.com/">Docker</a>。</p>
<p><strong>系统要求</strong></p>
<blockquote>
<div><ul class="simple">
<li><p>系统需求请参考 <a class="reference external" href="https://docs.docker.com/desktop/install/windows-install/#system-requirements">Docker Desktop on Linux</a> 或 <a class="reference external" href="https://docs.docker.com/desktop/install/windows-install/#system-requirements">Docker Desktop on Windows</a>。</p></li>
<li><p>一个桌面设备： <strong>需要 2 GB 可用内存</strong>。</p></li>
<li><p>在windows上，安装 WSL 会永久占用 2GB 内存。它被分配给 Ubuntu WSL。</p></li>
<li><p><em>推荐： 一组设备（至少五台设备）进行验证。</em></p></li>
<li><p><em>建议：电池或微型 USB 电缆为设备供电。</em></p></li>
<li><p><em>推荐:</em> <a class="reference internal" href="/docs/zh/pans-pro-rtls/infrastructure/pans-pro-manager#pans-pro-manager"><span class="std std-ref">PANS PRO Manager</span></a> <em>用于配置设备.</em></p></li>
</ul>
</div></blockquote>
<p id="uidocker"><strong>设置说明</strong></p>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-0" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-0">
Linux</label><div class="sd-tab-content docutils">
<p>系统兼容AMD64, ARM64 和 ARM32 架构。</p>
<ol class="arabic simple">
<li><p>下载PANS PRO Docker</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>请通过 <a class="reference external" href="mailto:apps-support%40leapslabs.com">apps-support<span>@</span>leapslabs<span>.</span>com</a> 联系我们获取下载软件包。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="2">
<li><p>解压缩 PANS PRO Docker 档案</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>在终端中输入: <span class="red-text">$ unzip PANS-PRO-DOCKER-LINUX.zip -d /path/to/directory</span>。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="3">
<li><p>在你的操作系统上安装 Docker。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>运行 <span class="red-text">leaps_docker_install.sh</span> 脚本，在你的操作系统上安装。</p></li>
</ul>
<p>例如，在 Ubuntu (Linux) 上：</p>
<blockquote>
<div><div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">source</span> <span class="n">leaps_docker_install</span><span class="o">.</span><span class="n">sh</span>
</pre></div>
</div>
</div></blockquote>
<ul class="simple">
<li><p>安装完成后，重新启动操作系统，以确保 Docker 配置正确。</p></li>
<li><p>详细说明可以参考官方的 <a class="reference external" href="https://docs.docker.com/get-docker/">Docker文档</a>。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="4">
<li><p>更新正确的 IP 地址配置。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>更新 <cite>leaps-server.conf</cite> 中的 <cite>mqtt_host</cite> 指向网关板的 IP 地址. 通过 shell 获取地址。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="5">
<li><p>运行所有 LEAPS Docker 容器。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>执行 <span class="red-text">leaps_docker_run_all.sh</span> 脚本，它将为 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a>, <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-server#leapsserver"><span class="std std-ref">LEAPS Server</span></a> 和 Mosquitto (MQTT 代理) 拉取并运行所需的 Docker 容器。</p></li>
</ul>
<p>例如，在 Ubuntu (Linux) 上：</p>
<blockquote>
<div><div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">source</span> <span class="n">leaps_docker_run_all</span><span class="o">.</span><span class="n">sh</span>
</pre></div>
</div>
</div></blockquote>
<ul class="simple">
<li><p>执行 <span class="red-text">docker ps</span> 命令，确保所有容器都能成功启动并准备就绪。</p></li>
</ul>
<p>例如，在 Ubuntu (Linux) 上：</p>
<blockquote>
<div><div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">docker</span> <span class="n">ps</span>

<span class="n">CONTAINER</span> <span class="n">ID</span>   <span class="n">IMAGE</span>                       <span class="n">COMMAND</span>                  <span class="n">CREATED</span>          <span class="n">STATUS</span>          <span class="n">PORTS</span>                                              <span class="n">NAMES</span>
<span class="mi">6</span><span class="n">f2ae0c87d65</span>   <span class="n">leapslabs</span><span class="o">/</span><span class="n">leaps_mosquitto</span><span class="p">:</span><span class="n">latest</span>   <span class="s2">"/docker-entrypoint.…"</span>   <span class="mi">9</span> <span class="n">seconds</span> <span class="n">ago</span>    <span class="n">Up</span> <span class="mi">9</span> <span class="n">seconds</span>    <span class="mf">0.0.0.0</span><span class="p">:</span><span class="mi">1883</span><span class="o">-&gt;</span><span class="mi">1883</span><span class="o">/</span><span class="n">tcp</span><span class="p">,</span> <span class="mf">0.0.0.0</span><span class="p">:</span><span class="mi">15675</span><span class="o">-&gt;</span><span class="mi">15675</span><span class="o">/</span><span class="n">tcp</span>   <span class="n">leaps_mosquitto</span>
<span class="mi">3</span><span class="n">d84cad7a913</span>   <span class="n">leapslabs</span><span class="o">/</span><span class="n">leaps_server</span><span class="p">:</span><span class="n">latest</span>      <span class="s2">"/app/leaps-server -…"</span>   <span class="mi">10</span> <span class="n">seconds</span> <span class="n">ago</span>   <span class="n">Up</span> <span class="mi">9</span> <span class="n">seconds</span>    <span class="mf">0.0.0.0</span><span class="p">:</span><span class="mi">7777</span><span class="o">-&gt;</span><span class="mi">7777</span><span class="o">/</span><span class="n">tcp</span><span class="p">,</span> <span class="mf">0.0.0.0</span><span class="p">:</span><span class="mi">7777</span><span class="o">-&gt;</span><span class="mi">7777</span><span class="o">/</span><span class="n">udp</span>     <span class="n">leaps_server</span>
<span class="mi">633</span><span class="n">c97e96f6e</span>   <span class="n">leapslabs</span><span class="o">/</span><span class="n">leaps_center</span><span class="p">:</span><span class="n">latest</span>      <span class="s2">"sh -c 'cd /app &amp;&amp;  …"</span>   <span class="mi">10</span> <span class="n">seconds</span> <span class="n">ago</span>   <span class="n">Up</span> <span class="mi">10</span> <span class="n">seconds</span>   <span class="mi">80</span><span class="o">/</span><span class="n">tcp</span><span class="p">,</span> <span class="mf">0.0.0.0</span><span class="p">:</span><span class="mi">80</span><span class="o">-&gt;</span><span class="mi">8080</span><span class="o">/</span><span class="n">tcp</span>                       <span class="n">leaps_center</span>
</pre></div>
</div>
</div></blockquote>
</div></blockquote>
<ol class="arabic simple" start="6">
<li><p>按照 <a class="reference internal" href="/docs/zh/pans-pro-rtls/quick-start-guide/panspro-rtls-setup#pans-pro-demo"><span class="std std-ref">PANS PRO 演示</span></a> 中的方法准备网络，并连接网关板。</p></li>
<li><p>Mosquitto并检查信息 (可选)</p></li>
</ol>
<blockquote>
<div><ul>
<li><p>在你的系统上使用 mosquitto_sub 。</p></li>
<li><p>要检查消息，请在终端中使用以下命令（该命令将连接到 Mosquitto MQTT 代理，并显示收到的所有消息）。</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">mosquitto_sub</span> <span class="o">-</span><span class="n">p</span> <span class="mi">1883</span> <span class="o">-</span><span class="n">d</span> <span class="o">-</span><span class="n">v</span> <span class="o">-</span><span class="n">t</span> <span class="s1">'#'</span>
</pre></div>
</div>
</li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="8">
<li><p>通过 IP地址访问 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> 。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>使用电脑的网页浏览器。</p></li>
<li><p>输入IP地址或 <span class="red-text">localhost</span> 来访问 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> 。</p></li>
</ul>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/leaps_center_login.png"><img alt="../../../_images/leaps_center_login.png" src="/docs-assets/zh-cn/_images/leaps_center_login.png" style="width: 667.4499999999999px; height: 315.0px;"></a>
</div>
</div></blockquote>
<ol class="arabic simple" start="9">
<li><p>登录 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a>。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>以用户名 <span class="red-text">admin</span> 和密码 <span class="red-text">admin</span> 登录。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="10">
<li><p>使用 <a class="reference internal" href="/docs/zh/pans-pro-rtls/infrastructure/pans-pro-manager#pans-pro-manager"><span class="std std-ref">PANS PRO Manager</span></a> 准备网络。</p></li>
<li><p>在 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> 上配置网络。</p></li>
</ol>
<blockquote>
<div><ul>
<li><p>检查 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> 中的网络设置，以匹配您所连接的网关板卡的网络 ID。</p></li>
<li><p>检查配置为PC IP地址的主机是否正确。</p>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/leaps_center_pans.png"><img alt="../../../_images/leaps_center_pans.png" class="align-center" src="/docs-assets/zh-cn/_images/leaps_center_pans.png" style="width: 764.4000000000001px; height: 360.40000000000003px;"></a>
</div></blockquote>
</li>
<li><p>请参阅 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> 和 <a class="reference internal" href="/docs/zh/pans-pro-rtls/infrastructure/pans-pro-manager#pans-pro-manager"><span class="std std-ref">PANS PRO Manager</span></a> 了解更多关于如何使用应用程序来配置和可视化节点和网络的详情。</p></li>
</ul>
</div></blockquote>
<p>现在系统已经成功设置和配置。 祝您使用愉快！</p>
</div>
<input id="sd-tab-item-1" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-1">
Windows</label><div class="sd-tab-content docutils">
<ol class="arabic simple">
<li><p>下载 PANS PRO Docker。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>请通过 <a class="reference external" href="mailto:apps-support%40leapslabs.com">apps-support<span>@</span>leapslabs<span>.</span>com</a> 联系我们获取下载软件包。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="2">
<li><p>解压缩PANS PRO Docker档案。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>使用 WinZip 或 7-Zip 等程序解压缩下载的 PANS PRO Docker 压缩文件。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="3">
<li><p>在windows上安装 Docker Desktop。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>请按照 Docker 文档中提供的 <a class="reference external" href="https://docs.docker.com/desktop/install/windows-install/">Docker Windows 安装</a>”说明进行操作。</p></li>
<li><p>安装完成后，请重新启动windows系统，以确保所有更改生效。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="4">
<li><p>使用 PowerShell 更新 IP 地址的正确配置。</p></li>
<li><p>使用 PowerShell 运行所有 LEAPS Docker 容器。</p></li>
</ol>
<blockquote>
<div><ul>
<li><p>执行 <span class="red-text">leaps_docker_run_all.bat</span> 脚本，它将为 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a>, LEAPS Server和 Mosquitto (MQTT 代理) 拉取并运行所需的 Docker 容器。</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">./</span><span class="n">leaps_docker_run_all</span><span class="o">.</span><span class="n">bat</span>
</pre></div>
</div>
</li>
<li><p>确保所有容器都能成功启动并准备就绪。</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">CONTAINER</span> <span class="n">ID</span>   <span class="n">IMAGE</span>                       <span class="n">COMMAND</span>                  <span class="n">CREATED</span>          <span class="n">STATUS</span>          <span class="n">PORTS</span>                                              <span class="n">NAMES</span>
<span class="mi">6</span><span class="n">f2ae0c87d65</span>   <span class="n">leapslabs</span><span class="o">/</span><span class="n">leaps_mosquitto</span><span class="p">:</span><span class="n">latest</span>   <span class="s2">"/docker-entrypoint.…"</span>   <span class="mi">9</span> <span class="n">seconds</span> <span class="n">ago</span>    <span class="n">Up</span> <span class="mi">9</span> <span class="n">seconds</span>    <span class="mf">0.0.0.0</span><span class="p">:</span><span class="mi">1883</span><span class="o">-&gt;</span><span class="mi">1883</span><span class="o">/</span><span class="n">tcp</span><span class="p">,</span> <span class="mf">0.0.0.0</span><span class="p">:</span><span class="mi">15675</span><span class="o">-&gt;</span><span class="mi">15675</span><span class="o">/</span><span class="n">tcp</span>   <span class="n">leaps_mosquitto</span>
<span class="mi">3</span><span class="n">d84cad7a913</span>   <span class="n">leapslabs</span><span class="o">/</span><span class="n">leaps_server</span><span class="p">:</span><span class="n">latest</span>      <span class="s2">"/app/leaps-server -…"</span>   <span class="mi">11</span> <span class="n">seconds</span> <span class="n">ago</span>   <span class="n">Up</span> <span class="mi">11</span> <span class="n">seconds</span>    <span class="mf">0.0.0.0</span><span class="p">:</span><span class="mi">7777</span><span class="o">-&gt;</span><span class="mi">7777</span><span class="o">/</span><span class="n">tcp</span><span class="p">,</span> <span class="mf">0.0.0.0</span><span class="p">:</span><span class="mi">7777</span><span class="o">-&gt;</span><span class="mi">7777</span><span class="o">/</span><span class="n">udp</span>    <span class="n">leaps_server</span>
<span class="mi">633</span><span class="n">c97e96f6e</span>   <span class="n">leapslabs</span><span class="o">/</span><span class="n">leaps_center</span><span class="p">:</span><span class="n">latest</span>      <span class="s2">"sh -c 'cd /app &amp;&amp;  …"</span>   <span class="mi">12</span> <span class="n">seconds</span> <span class="n">ago</span>   <span class="n">Up</span> <span class="mi">12</span> <span class="n">seconds</span>   <span class="mi">80</span><span class="o">/</span><span class="n">tcp</span><span class="p">,</span> <span class="mf">0.0.0.0</span><span class="p">:</span><span class="mi">80</span><span class="o">-&gt;</span><span class="mi">8080</span><span class="o">/</span><span class="n">tcp</span>                       <span class="n">leaps_center</span>
</pre></div>
</div>
</li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="6">
<li><p>按照 <a class="reference internal" href="/docs/zh/pans-pro-rtls/quick-start-guide/panspro-rtls-setup#pans-pro-demo"><span class="std std-ref">PANS PRO 演示</span></a> 中的方法准备网络，并连接网关板。</p></li>
<li><p>通过 IP地址访问 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> 。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>使用电脑的网页浏览器。</p></li>
<li><p>输入IP地址或 <span class="red-text">localhost</span> 来访问 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> 。</p></li>
</ul>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/docker_leaps_center_login.png"><img alt="../../../_images/docker_leaps_center_login.png" src="/docs-assets/zh-cn/_images/docker_leaps_center_login.png" style="width: 762.4000000000001px; height: 370.8px;"></a>
</div>
</div></blockquote>
<ol class="arabic simple" start="8">
<li><p>登录 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a>。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>以用户名 <span class="red-text">admin</span> 和密码 <span class="red-text">admin</span> 登录。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="9">
<li><p>使用 <a class="reference internal" href="/docs/zh/pans-pro-rtls/infrastructure/pans-pro-manager#pans-pro-manager"><span class="std std-ref">PANS PRO Manager</span></a> 准备网络。</p></li>
<li><p>在 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> 上配置网络。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>检查 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> 中的网络设置，以匹配您所连接的网关板卡的网络 ID。</p></li>
<li><p>检查配置为PC IP地址的主机是否正确。</p></li>
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
</div>


           </div>
