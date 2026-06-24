---
title: "MQTT代理商"
lang: zh
slug: "pans-pro-rtls/infrastructure/mqtt-broker"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/pans-pro-rtls/infrastructure/mqtt-broker/"
order: 101
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="mqtt-broker">
<span id="pans-mqtt-broker"></span><h1>MQTT代理商</h1>
<p>MQTT代理是一个服务器，它接收所有客户端消息，然后将消息路由到适当的目标客户端。MQTT客户端是运行MQTT库并通过网络连接到MQTT代理的任何设备（从微控制器到功能齐全的服务器）。</p>
<p>LEAPS Mosquitto是一个开源MQTT代理，是docker镜像 <a class="reference external" href="https://hub.docker.com/_/eclipse-mosquitto">eclipse Mosquitto:1.5.11的副本</a> 其中集成的自定义 <code class="docutils literal notranslate"><span class="pre">mosquitto.conf</span></code> 文件位于 <code class="docutils literal notranslate"><span class="pre">/mosquito/config/mosquito.conf</span></code> 中。如需更多信息，请参阅 <a class="reference external" href="https://hub.docker.com/_/eclipse-mosquitto">日食蚊子</a></p>
<hr class="docutils">
<div class="section" id="installation">
<h2>安装</h2>
<div class="section" id="system-requirements">
<h3>系统要求</h3>
<div class="admonition note">
<p class="admonition-title">注解</p>
<p>Docker的系统要求因操作系统而异。</p>
<ul class="simple">
<li><p>对于Linux，您需要一个64位架构、兼容的内核版本和特定的内核功能。</p></li>
<li><p>在Windows上，在启用虚拟化的Windows 10上使用Docker Desktop</p></li>
<li><p>在macOS上，将Docker Desktop与macOS 10.13或更高版本一起使用。在硬件方面，建议至少有2GB的RAM，以及足够的CPU和磁盘空间。</p></li>
</ul>
<p>请参考 <a class="reference external" href="https://docs.docker.com/">Docker</a> 官方文件，了解最新细节</p>
</div>
</div>
<hr class="docutils">
<div class="section" id="instructions">
<h3>说明</h3>
<ol class="arabic simple">
<li><p>在电脑上安装 Docker</p></li>
</ol>
<blockquote>
<div><div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-0" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-0">
在 Linux 上</label><div class="sd-tab-content docutils">
<p><a class="reference external" href="https://docs.docker.com/desktop/install/linux-install/">在 Linux 上安装 Docker Desktop</a></p>
<p>此外，您还可以参考以下命令进行安装：</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">curl -fsSL https://get.docker.com -o get-docker.sh</span>
<span class="go">sudo sh ./get-docker.sh</span>
<span class="go">sudo usermod -aG docker $USER</span>
</pre></div>
</div>
</div>
<input id="sd-tab-item-1" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-1">
在Windows上</label><div class="sd-tab-content docutils">
<p><a class="reference external" href="https://docs.docker.com/desktop/install/windows-install/">在 Windows 上安装 Docker Desktop</a></p>
</div>
<input id="sd-tab-item-2" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-2">
在 macOS 上</label><div class="sd-tab-content docutils">
<p><a class="reference external" href="https://docs.docker.com/desktop/install/mac-install/">在macOS上安装Docker桌面</a></p>
</div>
</div>
</div></blockquote>
<ol class="arabic simple" start="2">
<li><p>在PC上打开命令提示符或终端窗口，然后安装LEAPS Mosquitto Docker软件包，运行:</p></li>
</ol>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">docker run -d -p 1883:1883/tcp -p 15675:15675 --name some_name leapslabs/leaps_mosquitto:latest mosquitto ---cfg /mosquitto/config/mosquitto.conf</span>
</pre></div>
</div>
<p>其中 <code class="docutils literal notranslate"><span class="pre">some_name</span></code> 是您要为容器分配的名称，<code class="docutils literal notranslate"><span class="pre">tag</span></code> 是指定您想要的 <code class="docutils literal notranslate"><span class="pre">leaps-mosquitto</span></code> 版本的标签。</p>
<ul class="simple">
<li><p>推荐的运行选项</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">--user</span> <span class="pre">$(id</span> <span class="pre">-u):$(id</span> <span class="pre">-g)</span></code> 在特定用户和组下运行实例。</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">--restart</span> <span class="pre">unless-stopped</span></code> 在服务器崩溃时自动重启实例。</p></li>
</ul>
</li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="3">
<li><p>LEAPS Mosquitto安装过程将开始。</p></li>
</ol>
<blockquote>
<div><p>例如，在 Ubuntu (Linux) 上：</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">docker run -d -p 1883:1883/tcp -p 15675:15675 --name leaps_mosquitto leapslabs/leaps_mosquitto:latest mosquitto ---cfg /mosquitto/config/mosquitto.conf</span>

<span class="go">Unable to find image 'leapslabs/leaps_mosquitto:latest' locally</span>
<span class="go">latest: Pulling from leapslabs/leaps_mosquitto</span>
<span class="go">f7dab3ab2d6e: Already exists</span>
<span class="go">2a0a6c9fa787: Already exists</span>
<span class="go">a211eff771d6: Already exists</span>
<span class="go">d362e2a9c11b: Already exists</span>
<span class="go">Digest: sha256:a97752d6e2d81e2701c7cd5f807eb4256322983f8aa3135da8235b647e6a9b4e</span>
<span class="go">Status: Downloaded newer image for leapslabs/leaps_mosquitto:latest</span>
<span class="go">1f526e755ad9a356c439003b93c200802628ae9bc046827e7327d0334804b565</span>
</pre></div>
</div>
</div></blockquote>
<ol class="arabic simple" start="4">
<li><p>确认安装成功，运行：</p></li>
</ol>
<blockquote>
<div><p>例如，在 Ubuntu (Linux) 上：</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">docker ps</span>

<span class="go">CONTAINER ID   IMAGE                      COMMAND                  CREATED          STATUS                          PORTS     NAMES</span>
<span class="go">b1145b72db35   leapslabs/leaps_mosquitto:latest  "sh -c 'cd /app &amp;&amp;  …"   37 seconds ago   11 seconds ago                            leaps_mosquitto</span>
</pre></div>
</div>
</div></blockquote>
<p>因此，您已在PC上成功安装并启动了LEAPS Mosquitto。</p>
</div>
</div>
<hr class="docutils">
<div class="section" id="getting-started">
<h2>开始</h2>
<div class="section" id="leaps-mosquitto-docker">
<h3>LEAPS Mosquitto Docker</h3>
<ul class="simple">
<li><p>启动LEAPS Mosquitto，运行: <code class="docutils literal notranslate"><span class="pre">docker</span> <span class="pre">Start</span> <span class="pre">LEAPS_Mosquitto</span></code></p></li>
<li><p>停止LEAPS Mosquitto，运行: <code class="docutils literal notranslate"><span class="pre">docker</span> <span class="pre">Stop</span> <span class="pre">LEAPS_Mosquitto</span></code></p></li>
<li><p>重启LEAPS Mosquitto，运行: <code class="docutils literal notranslate"><span class="pre">docker</span> <span class="pre">Restart</span> <span class="pre">LEAPS_Mosquitto</span></code></p></li>
<li><p>删除LEAPS Mosquitto，运行 <code class="docutils literal notranslate"><span class="pre">docker</span> <span class="pre">rm--强制LEAPS_Mosquitto</span></code></p></li>
</ul>
</div>
</div>
<hr class="docutils">
<div class="section" id="customized-options">
<h2>定制选项</h2>
<blockquote>
<div><p><strong>强制性选项</strong></p>
<blockquote>
<div><ul class="simple">
<li><p>端口1883-默认侦听器端口</p></li>
<li><p>监听器1884启用1884的监听器</p></li>
<li><p>听众15675启用听众15675</p></li>
</ul>
</div></blockquote>
<p><strong>推荐选项</strong></p>
<blockquote>
<div><ul class="simple">
<li><p>用户蚊子-取消root权限</p></li>
<li><p>max_inflight_messages 200-增加每个客户端的内斗QoS消息，因为一次可以发送的QoS1很少。</p></li>
<li><p>max_queued_messages 1000-将每个客户端队列中保存的QoS 1和2消息的最大数量增加到当前正在运行的数量之上。</p></li>
<li><p>allow_zero_length_clientid true-允许客户端ID为零长度</p></li>
<li><p>persistent_client_expiration 14d-针对设计不佳的客户端提供自动保护</p></li>
</ul>
</div></blockquote>
</div></blockquote>
</div>
<div class="section" id="troubleshooting">
<h2>故障排除</h2>
<ul class="simple">
<li><p>使用以下命令 <code class="docutils literal notranslate"><span class="pre">docker</span> <span class="pre">restart</span> <span class="pre">leaps_mosquitto</span></code> 重新启动leaps mosquitto。</p></li>
<li><p>检查LEAPS Mosquitto运行时的日志，打开docker桌面，选择LEAPS_Mosquitto容器。</p></li>
</ul>
</div>
</div>


           </div>
