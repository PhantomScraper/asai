---
title: "LEAPS Docker"
lang: zh
slug: "udk/udk-start/infrastructure-docker"
section: "udk"
sourceUrl: "https://docs.leapslabs.com/zh-cn/udk/udk-start/infrastructure-docker/"
order: 40
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-docker">
<span id="id1"></span><h1>LEAPS Docker</h1>
<p>此页面提供：</p>
<blockquote>
<div><ul class="simple">
<li><p>LEAPS Docker 包。</p></li>
<li><p>有关系统要求的信息。</p></li>
<li><p>关于如何安装 LEAPS Docker 的说明。</p></li>
</ul>
</div></blockquote>
<p>安装快速简单，只需要完成一次。</p>
<p>访问官方 Docker了解更多关于 <a class="reference external" href="https://docs.docker.com/">Docker的信息</a>。</p>
<p><strong>系统要求</strong></p>
<blockquote>
<div><ul class="simple">
<li><p>系统要求遵循 <a class="reference external" href="https://docs.docker.com/desktop/install/windows-install/#system-requirements">Linux上的Docker桌面</a> 或 <a class="reference external" href="https://docs.docker.com/desktop/install/windows-install/#system-requirements">Windows上的 Docker桌面</a>。</p></li>
<li><p>桌面设备: <strong>需要2 GB的可用内存</strong>。</p></li>
<li><p>在windows上，安装 WSL 会永久占用 2GB 内存。它被分配给 Ubuntu WSL。</p></li>
<li><p><em>推荐: 一组UDK (至少五台设备) 进行验证。</em></p></li>
<li><p><em>推荐:电池或USB-C电缆为设备供电</em></p></li>
<li><p><em>推荐:</em> <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> <em>配置设备.</em></p></li>
</ul>
</div></blockquote>
<p id="uidocker"><strong>安装说明</strong></p>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-0" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-0">
Linux</label><div class="sd-tab-content docutils">
<p>该系统与AMD64, ARM64和ARM32架构兼容。</p>
<ol class="arabic simple">
<li><p>下载 LEAPS Docker</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>LEAPS Docker <a class="reference download internal" download="" href="../../../_downloads/ae97200ed08d464a52759cdc643e7c12/LEAPS-DOCKER-LINUX-v1.1.0.zip"><code class="xref download docutils literal notranslate"><span class="pre">LEAPS-DOCKER-LINUX-v1.1.0.zip</span></code></a>.</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="2">
<li><p>提取LEAPS Docker档案</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>键入终端： <span class="red-text">$ unzip LEAPS-DOCKER-LINUX-v1.1.0.zip -d /path/to/directory</span></p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="3">
<li><p>Install Docker on the operating system.</p></li>
</ol>
<blockquote>
<div><ul>
<li><p>在您的操作系统上安装 Docker。</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">source</span> <span class="n">leaps_docker_install</span><span class="o">.</span><span class="n">sh</span>
</pre></div>
</div>
</li>
<li><p>安装完成后，重新启动操作系统，以确保 Docker 配置正确。</p></li>
<li><p>有关详细说明，请参阅官方的 <a class="reference external" href="https://docs.docker.com/get-docker/">Docker文档</a></p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="4">
<li><p>使用IP地址更新正确的配置。</p></li>
</ol>
<blockquote>
<div><ul>
<li><p>使用 <span class="red-text">update_configuration_ip.sh</span> 脚本使用PC的ip地址更新系统的配置。例如，在 Ubuntu (Linux) 上：</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">source</span> <span class="n">update_configuration_ip</span><span class="o">.</span><span class="n">sh</span>
</pre></div>
</div>
</li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="5">
<li><p>运行所有 LEAPS Docker 容器。</p></li>
</ol>
<blockquote>
<div><ul>
<li><p>执行 <span class="red-text">leaps_docker_run_all.sh</span> 脚本，它将为 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a>, <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-server#leapsserver"><span class="std std-ref">LEAPS Server</span></a>, <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-gateway#leapsgateway"><span class="std std-ref">LEAPS Gateway</span></a> 和 Mosquitto (MQTT 代理) 拉取并运行所需的 Docker 容器。例如，在 Ubuntu (Linux) 上：</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">source</span> <span class="n">leaps_docker_run_all</span><span class="o">.</span><span class="n">sh</span>
</pre></div>
</div>
</li>
<li><p>执行 <span class="red-text">docker ps</span> 命令，确保所有容器都成功启动并准备好使用。在 Ubuntu (Linux) 上：</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">docker</span> <span class="n">ps</span>

<span class="n">CONTAINER</span> <span class="n">ID</span>   <span class="n">IMAGE</span>                       <span class="n">COMMAND</span>                  <span class="n">CREATED</span>          <span class="n">STATUS</span>          <span class="n">PORTS</span>                                              <span class="n">NAMES</span>
<span class="mi">6</span><span class="n">f2ae0c87d65</span>   <span class="n">leapslabs</span><span class="o">/</span><span class="n">leaps_mosquitto</span><span class="p">:</span><span class="n">udk</span>   <span class="s2">"/docker-entrypoint.…"</span>   <span class="mi">9</span> <span class="n">seconds</span> <span class="n">ago</span>    <span class="n">Up</span> <span class="mi">9</span> <span class="n">seconds</span>    <span class="mf">0.0.0.0</span><span class="p">:</span><span class="mi">1883</span><span class="o">-&gt;</span><span class="mi">1883</span><span class="o">/</span><span class="n">tcp</span><span class="p">,</span> <span class="mf">0.0.0.0</span><span class="p">:</span><span class="mi">15675</span><span class="o">-&gt;</span><span class="mi">15675</span><span class="o">/</span><span class="n">tcp</span>   <span class="n">leaps_mosquitto</span>
<span class="mi">3</span><span class="n">d84cad7a913</span>   <span class="n">leapslabs</span><span class="o">/</span><span class="n">leaps_server</span><span class="p">:</span><span class="n">udk</span>      <span class="s2">"/app/leaps-server -…"</span>   <span class="mi">10</span> <span class="n">seconds</span> <span class="n">ago</span>   <span class="n">Up</span> <span class="mi">9</span> <span class="n">seconds</span>    <span class="mf">0.0.0.0</span><span class="p">:</span><span class="mi">7777</span><span class="o">-&gt;</span><span class="mi">7777</span><span class="o">/</span><span class="n">tcp</span><span class="p">,</span> <span class="mf">0.0.0.0</span><span class="p">:</span><span class="mi">7777</span><span class="o">-&gt;</span><span class="mi">7777</span><span class="o">/</span><span class="n">udp</span>     <span class="n">leaps_server</span>
<span class="mi">633</span><span class="n">c97e96f6e</span>   <span class="n">leapslabs</span><span class="o">/</span><span class="n">leaps_center</span><span class="p">:</span><span class="n">udk</span>      <span class="s2">"sh -c 'cd /app &amp;&amp;  …"</span>   <span class="mi">10</span> <span class="n">seconds</span> <span class="n">ago</span>   <span class="n">Up</span> <span class="mi">10</span> <span class="n">seconds</span>   <span class="mi">80</span><span class="o">/</span><span class="n">tcp</span><span class="p">,</span> <span class="mf">0.0.0.0</span><span class="p">:</span><span class="mi">80</span><span class="o">-&gt;</span><span class="mi">8080</span><span class="o">/</span><span class="n">tcp</span>                       <span class="n">leaps_center</span>
</pre></div>
</div>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">sudo</span> <span class="n">docker</span> <span class="n">ps</span>

<span class="n">CONTAINER</span> <span class="n">ID</span>   <span class="n">IMAGE</span>                     <span class="n">COMMAND</span>                  <span class="n">CREATED</span>              <span class="n">STATUS</span>                          <span class="n">PORTS</span>     <span class="n">NAMES</span>
<span class="mi">6</span><span class="n">bb3bf42cb63</span>   <span class="n">leapslabs</span><span class="o">/</span><span class="n">leaps_gateway</span><span class="p">:</span><span class="n">udk</span>   <span class="s2">"/app/leaps-gateway …"</span>   <span class="n">About</span> <span class="n">a</span> <span class="n">minute</span> <span class="n">ago</span>   <span class="n">Up</span> <span class="n">About</span> <span class="n">a</span> <span class="n">minute</span>                         <span class="n">leaps_gateway</span>
</pre></div>
</div>
</li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="6">
<li><p>使用 USB-C 数据线将网关板连接到PC。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>将USB-C数据线插入电脑上的 <a class="reference internal" href="/docs/zh/udk/udk-start/device-hw-interfaces#hardware-interface"><span class="std std-ref">USB-C数据端口1</span></a> 确保连接稳定</p></li>
</ul>
<img alt="../../../_images/leaps-connect-usb-port1.gif" class="align-center" src="/docs-assets/zh-cn/_images/leaps-connect-usb-port1.gif">
</div></blockquote>
<ol class="arabic simple" start="7">
<li><p>Mosquitto和检查消息 (可选)</p></li>
</ol>
<blockquote>
<div><ul>
<li><p>在您的系统上使用 mosquitto_sub 。要检查消息，请在终端中使用以下命令</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">mosquitto_sub</span> <span class="o">-</span><span class="n">p</span> <span class="mi">1883</span> <span class="o">-</span><span class="n">d</span> <span class="o">-</span><span class="n">v</span> <span class="o">-</span><span class="n">t</span> <span class="s1">'#'</span>
</pre></div>
</div>
</li>
<li><p>此命令将连接到 Mosquitto MQTT 代理，并显示收到的所有消息。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="8">
<li><p>通过 IP地址访问 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> 。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>使用计算机的网络浏览器。</p></li>
<li><p>输入IP地址或 <span class="red-text">localhost</span> 以访问 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> 。</p></li>
</ul>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/docker_leaps_center_login.png"><img alt="../../../_images/docker_leaps_center_login.png" src="/docs-assets/zh-cn/_images/docker_leaps_center_login.png" style="width: 762.4000000000001px; height: 370.8px;"></a>
</div>
</div></blockquote>
<ol class="arabic simple" start="9">
<li><p>登录 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a>。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>登录时用户名为 <span class="red-text">admin</span> 密码为 <span class="red-text">admin</span>。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="10">
<li><p>使用 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> 来准备网络。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>配置演示: <a class="reference internal" href="/docs/zh/udk/udk-start/twr-rtls-and-data-telemetry-demo#twr-rtls-and-data-telemetry-demo"><span class="std std-ref">TWR RTLS 和数据遥测演示</span></a> 或 <a class="reference internal" href="/docs/zh/udk/udk-start/uplink-tdoa-rtls-demo#uplink-tdoa-rtls-demo"><span class="std std-ref">上行链路 TDoA RTLS 演示</span></a>。</p></li>
<li><p>默认情况下，网络ID将是 <code class="docutils literal notranslate"><span class="pre">0x1234</span></code>。</p></li>
<li><p>在本例中，需要连接 ID 为 <code class="docutils literal notranslate"><span class="pre">0x83A2</span></code> 的网关板。</p></li>
</ul>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/docker_network_demo01.jpg"><img alt="../../../_images/docker_network_demo01.jpg" src="/docs-assets/zh-cn/_images/docker_network_demo01.jpg" style="width: 360.0px; height: 800.0px;"></a>
</div>
</div></blockquote>
<ol class="arabic simple" start="11">
<li><p>在 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> 上配置网络。</p></li>
</ol>
<blockquote>
<div><ul>
<li><p>检查 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> 中的网络设置，以匹配您所连接的网关板卡的网络 ID。</p></li>
<li><p>检查配置为PC 的IP地址的主机是否正确。</p></li>
<li><p>本例中，网络 ID 为 <code class="docutils literal notranslate"><span class="pre">0x1234</span></code>，主机为 <code class="docutils literal notranslate"><span class="pre">192.168.1.12</span></code>。</p>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/docker_leaps_center_config_network.png"><img alt="../../../_images/docker_leaps_center_config_network.png" src="/docs-assets/zh-cn/_images/docker_leaps_center_config_network.png" style="width: 626.4000000000001px; height: 409.6px;"></a>
</div>
</li>
<li><p>请参阅 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> 和 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> 了解更多关于如何使用应用程序来配置和可视化节点和网络的详情。</p></li>
</ul>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/docker_leaps_center_network.png"><img alt="../../../_images/docker_leaps_center_network.png" src="/docs-assets/zh-cn/_images/docker_leaps_center_network.png" style="width: 764.4000000000001px; height: 373.20000000000005px;"></a>
</div>
</div></blockquote>
<p>现在系统已经成功设置和配置。 祝您使用愉快！</p>
</div>
<input id="sd-tab-item-1" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-1">
Windows</label><div class="sd-tab-content docutils">
<ol class="arabic simple">
<li><p>下载 LEAPS Docker。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>LEAPS Docker <a class="reference download internal" download="" href="../../../_downloads/0bfac2c46fb0b9265d7f58941736f12a/LEAPS-DOCKER-WINDOWS-v1.1.0.zip"><code class="xref download docutils literal notranslate"><span class="pre">LEAPS-DOCKER-WINDOWS-v1.1.0.zip</span></code></a>.</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="2">
<li><p>解压缩 LEAPS Docker 压缩包。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>使用 WinZip 或 7-Zip 等程序解压缩下载的 LEAPS Docker 压缩文件。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="3">
<li><p>在Windows上安装 Docker Desktop。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>请遵循 Docker 文档中关于 <a class="reference external" href="https://docs.docker.com/desktop/install/windows-install/">Docker Windows 安装</a> 的。</p></li>
<li><p>安装完成后，请重新启动你的Windows系统，以确保所有更改生效。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="4">
<li><p>使用 PowerShell 更新 IP 地址的正确配置。</p></li>
</ol>
<blockquote>
<div><ul>
<li><p>Use the <span class="red-text">update_configuration_ip.bat</span> script to update the system’s configuration with the PC’s IP address.</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">./</span><span class="n">update_configuration_ip</span><span class="o">.</span><span class="n">bat</span>
</pre></div>
</div>
</li>
<li><p>For this example, the leaps-server configuration is updated with the current IP address: <code class="docutils literal notranslate"><span class="pre">192.168.1.12</span></code>.</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="5">
<li><p>使用 PowerShell 运行所有 LEAPS Docker 容器。</p></li>
</ol>
<blockquote>
<div><ul>
<li><p>执行 <span class="red-text">leaps_docker_run_all.bat</span> 脚本，它会为 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a>, LEAPS Server, 和 Mosquitto (MQTT broker) 拉取并运行所需的 Docker 容器。</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">./</span><span class="n">leaps_docker_run_all</span><span class="o">.</span><span class="n">bat</span>
</pre></div>
</div>
</li>
<li><p>确保所有容器都能成功启动并准备就绪。</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">CONTAINER</span> <span class="n">ID</span>   <span class="n">IMAGE</span>                       <span class="n">COMMAND</span>                  <span class="n">CREATED</span>          <span class="n">STATUS</span>          <span class="n">PORTS</span>                                              <span class="n">NAMES</span>
<span class="mi">6</span><span class="n">f2ae0c87d65</span>   <span class="n">leapslabs</span><span class="o">/</span><span class="n">leaps_mosquitto</span><span class="p">:</span><span class="n">udk</span>   <span class="s2">"/docker-entrypoint.…"</span>   <span class="mi">9</span> <span class="n">seconds</span> <span class="n">ago</span>    <span class="n">Up</span> <span class="mi">9</span> <span class="n">seconds</span>    <span class="mf">0.0.0.0</span><span class="p">:</span><span class="mi">1883</span><span class="o">-&gt;</span><span class="mi">1883</span><span class="o">/</span><span class="n">tcp</span><span class="p">,</span> <span class="mf">0.0.0.0</span><span class="p">:</span><span class="mi">15675</span><span class="o">-&gt;</span><span class="mi">15675</span><span class="o">/</span><span class="n">tcp</span>   <span class="n">leaps_mosquitto</span>
<span class="mi">3</span><span class="n">d84cad7a913</span>   <span class="n">leapslabs</span><span class="o">/</span><span class="n">leaps_server</span><span class="p">:</span><span class="n">udk</span>      <span class="s2">"/app/leaps-server -…"</span>   <span class="mi">11</span> <span class="n">seconds</span> <span class="n">ago</span>   <span class="n">Up</span> <span class="mi">11</span> <span class="n">seconds</span>    <span class="mf">0.0.0.0</span><span class="p">:</span><span class="mi">7777</span><span class="o">-&gt;</span><span class="mi">7777</span><span class="o">/</span><span class="n">tcp</span><span class="p">,</span> <span class="mf">0.0.0.0</span><span class="p">:</span><span class="mi">7777</span><span class="o">-&gt;</span><span class="mi">7777</span><span class="o">/</span><span class="n">udp</span>    <span class="n">leaps_server</span>
<span class="mi">633</span><span class="n">c97e96f6e</span>   <span class="n">leapslabs</span><span class="o">/</span><span class="n">leaps_center</span><span class="p">:</span><span class="n">udk</span>      <span class="s2">"sh -c 'cd /app &amp;&amp;  …"</span>   <span class="mi">12</span> <span class="n">seconds</span> <span class="n">ago</span>   <span class="n">Up</span> <span class="mi">12</span> <span class="n">seconds</span>   <span class="mi">80</span><span class="o">/</span><span class="n">tcp</span><span class="p">,</span> <span class="mf">0.0.0.0</span><span class="p">:</span><span class="mi">80</span><span class="o">-&gt;</span><span class="mi">8080</span><span class="o">/</span><span class="n">tcp</span>                       <span class="n">leaps_center</span>
</pre></div>
</div>
</li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="6">
<li><p>Connect the <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-gateway#leapsgateway"><span class="std std-ref">LEAPS Gateway</span></a> use <code class="docutils literal notranslate"><span class="pre">Linux</span></code> or <code class="docutils literal notranslate"><span class="pre">Raspberry</span> <span class="pre">Pi</span></code>.</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>Make sure there is a connection to Windows.</p></li>
<li><p>Refer to <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-gateway#leapsgateway"><span class="std std-ref">LEAPS Gateway</span></a> setup on <code class="docutils literal notranslate"><span class="pre">Linux</span></code> or <code class="docutils literal notranslate"><span class="pre">Raspberry</span> <span class="pre">Pi</span></code> and, update the IP address accordingly. For example, <code class="docutils literal notranslate"><span class="pre">leaps-server-host</span></code> will be updated to <code class="docutils literal notranslate"><span class="pre">192.168.1.12</span></code>.</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="7">
<li><p>Mosquitto和检查消息 (可选)</p></li>
</ol>
<blockquote>
<div><ul>
<li><p>在您的系统上使用 mosquitto_sub 。要检查消息，请在终端中使用以下命令</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">mosquitto_sub</span> <span class="o">-</span><span class="n">p</span> <span class="mi">1883</span> <span class="o">-</span><span class="n">d</span> <span class="o">-</span><span class="n">v</span> <span class="o">-</span><span class="n">t</span> <span class="s1">'#'</span>
</pre></div>
</div>
</li>
<li><p>此命令将连接到 Mosquitto MQTT 代理，并显示收到的所有消息。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="8">
<li><p>通过 IP地址访问 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> 。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>使用计算机的网络浏览器。</p></li>
<li><p>输入IP地址或 <span class="red-text">localhost</span> 以访问 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> 。</p></li>
</ul>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/docker_leaps_center_login.png"><img alt="../../../_images/docker_leaps_center_login.png" src="/docs-assets/zh-cn/_images/docker_leaps_center_login.png" style="width: 762.4000000000001px; height: 370.8px;"></a>
</div>
</div></blockquote>
<ol class="arabic simple" start="9">
<li><p>登录 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a>。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>登录时用户名为 <span class="red-text">admin</span> 密码为 <span class="red-text">admin</span>。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="10">
<li><p>使用 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> 来准备网络。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>配置演示: <a class="reference internal" href="/docs/zh/udk/udk-start/twr-rtls-and-data-telemetry-demo#twr-rtls-and-data-telemetry-demo"><span class="std std-ref">TWR RTLS 和数据遥测演示</span></a> 或 <a class="reference internal" href="/docs/zh/udk/udk-start/uplink-tdoa-rtls-demo#uplink-tdoa-rtls-demo"><span class="std std-ref">上行链路 TDoA RTLS 演示</span></a>。</p></li>
<li><p>默认情况下，网络ID将是 <code class="docutils literal notranslate"><span class="pre">0x1234</span></code>。</p></li>
</ul>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/docker_network_demo01.jpg"><img alt="../../../_images/docker_network_demo01.jpg" src="/docs-assets/zh-cn/_images/docker_network_demo01.jpg" style="width: 360.0px; height: 800.0px;"></a>
</div>
</div></blockquote>
<ol class="arabic simple" start="11">
<li><p>在 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> 上配置网络。</p></li>
</ol>
<blockquote>
<div><ul>
<li><p>检查 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> 中的网络设置，以匹配您所连接的网关板卡的网络 ID。</p></li>
<li><p>检查配置为PC 的IP地址的主机是否正确。</p></li>
<li><p>本例中，网络 ID 为 <code class="docutils literal notranslate"><span class="pre">0x1234</span></code>，主机为 <code class="docutils literal notranslate"><span class="pre">192.168.1.12</span></code>。</p>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/docker_leaps_center_config_network.png"><img alt="../../../_images/docker_leaps_center_config_network.png" src="/docs-assets/zh-cn/_images/docker_leaps_center_config_network.png" style="width: 626.4000000000001px; height: 409.6px;"></a>
</div>
<ul class="simple">
<li><p>请参阅 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> 和 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> 了解更多关于如何使用应用程序来配置和可视化节点和网络的详情。</p></li>
</ul>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/docker_leaps_center_network.png"><img alt="../../../_images/docker_leaps_center_network.png" src="/docs-assets/zh-cn/_images/docker_leaps_center_network.png" style="width: 764.4000000000001px; height: 373.20000000000005px;"></a>
</div>
</li>
</ul>
</div></blockquote>
<p>现在系统已经成功设置和配置。 祝您使用愉快！</p>
</div>
</div>
</div>


           </div>
