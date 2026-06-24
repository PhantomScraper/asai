---
title: "LEAPS Server"
lang: zh
slug: "pans-pro-rtls/infrastructure/leaps-server"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/pans-pro-rtls/infrastructure/leaps-server/"
order: 100
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-server">
<span id="pans-pro-server"></span><h1>LEAPS Server</h1>
<div class="section" id="introduction">
<h2>简介</h2>
<p>LEAPS Server是UWB网络的中央数据中心。它通过 <a class="reference external" href="https://mosquitto.org/">MQTT代理</a> 将所有网关设备与世界互连。</p>
</div>
<hr class="docutils">
<div class="section" id="key-features">
<h2>主要功能</h2>
<ul class="simple">
<li><p>它作为上行链路数据集中器、下行链路数据路由器、数据处理器、位置引擎、设备管理、设备访问控制和服务质量。</p></li>
<li><p>它通过连接器与世界通信。目前，支持的连接器是MQTT，包括对AWS的支持。</p></li>
<li><p><a class="reference internal" href="#pans-pro-server"><span class="std std-ref">LEAPS Server</span></a> 在Linux平台上作为守护进程服务运行。</p></li>
</ul>
</div>
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
<li><p>在Windows上，在启用虚拟化的Windows 10上使用Docker Desktop。</p></li>
<li><p>在 macOS 上，请使用配备 macOS 10.13 或更新版本的Docker Desktop. 在硬件方面，建议至少配备 2GB 内存以及足够的 CPU 和磁盘空间。</p></li>
</ul>
<p>有关最新详情，请参阅 <a class="reference external" href="https://docs.docker.com/">Docker</a> 官方文档。</p>
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
<li><p>创建文件夹 <code class="docutils literal notranslate"><span class="pre">leaps_server_hub</span></code> 和子文件夹 <code class="docutils literal notranslate"><span class="pre">data</span></code>。然后，在 <code class="docutils literal notranslate"><span class="pre">leaps_server_hub/data</span></code> 中添加 <code class="docutils literal notranslate"><span class="pre">leaps-server.conf</span></code> 配置文件。</p></li>
</ol>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">#</span><span class="c1">######################################################################</span>
<span class="gp"># </span>LEAPS<span class="w"> </span>Server<span class="w"> </span>settings
<span class="gp">#</span>

<span class="gp"># </span>-----------------------------------------------------------------
<span class="gp"># </span>Logging
<span class="gp"># </span>-----------------------------------------------------------------
<span class="go">log_level = 0 #  Logging level, default is 0 (0=none, 1=fatal, 2=error, 3=warning, 4=info, 5=debug, 6=verbose)</span>

<span class="gp"># </span>Path<span class="w"> </span>to<span class="w"> </span>log<span class="w"> </span>file.<span class="w"> </span>Comment<span class="w"> </span>out<span class="w"> </span>to<span class="w"> </span>disable<span class="w"> </span>logging<span class="w"> </span>to<span class="w"> </span>file<span class="w"> </span><span class="o">(</span>log<span class="w"> </span>to<span class="w"> </span>stdio<span class="w"> </span>instead<span class="o">)</span>.
<span class="gp"># </span><span class="nv">log</span><span class="w"> </span><span class="o">=</span><span class="w"> </span>leaps-server.log

<span class="gp"># </span>-----------------------------------------------------------------
<span class="gp"># </span>Certificate<span class="w"> </span>based<span class="w"> </span>SSL/TLS<span class="w"> </span>support
<span class="gp"># </span>-----------------------------------------------------------------
<span class="gp">#</span>
<span class="gp"># </span>cafile<span class="w"> </span>-<span class="w"> </span>Authority<span class="w"> </span>certificates<span class="w"> </span>that<span class="w"> </span>have<span class="w"> </span>signed<span class="w"> </span>your<span class="w"> </span>server<span class="w"> </span>certificate.
<span class="gp"># </span>certfile<span class="w"> </span>-<span class="w"> </span>Path<span class="w"> </span>to<span class="w"> </span>the<span class="w"> </span>PEM<span class="w"> </span>encoded<span class="w"> </span>server<span class="w"> </span>certificate.
<span class="gp"># </span>keyfile<span class="w"> </span>-<span class="w"> </span>Path<span class="w"> </span>to<span class="w"> </span>the<span class="w"> </span>PEM<span class="w"> </span>encoded<span class="w"> </span>keyfile.
<span class="gp"># </span>gw_auth<span class="w"> </span>-<span class="w"> </span>When<span class="w"> </span>using<span class="w"> </span>TLS<span class="w"> </span>on<span class="w"> </span>the<span class="w"> </span>interface<span class="w"> </span>with<span class="w"> </span>the<span class="w"> </span>gateways,<span class="w"> </span>this<span class="w"> </span>parameter<span class="w"> </span>configures<span class="w"> </span>TLS<span class="w"> </span>authentication<span class="w"> </span>between<span class="w"> </span>server<span class="w"> </span>and<span class="w"> </span>the<span class="w"> </span>gateway<span class="w"> </span><span class="o">(</span><span class="nv">0</span><span class="o">=</span>server<span class="w"> </span><span class="nv">1</span><span class="o">=</span>mutual<span class="o">)</span>.
<span class="gp">#</span>
<span class="gp"># </span><span class="nv">cafile</span><span class="w"> </span><span class="o">=</span><span class="w"> </span>/etc/leaps-server/cacert.pem
<span class="gp"># </span><span class="nv">certfile</span><span class="w"> </span><span class="o">=</span><span class="w"> </span>/etc/leaps-server/servercert.pem
<span class="gp"># </span><span class="nv">keyfile</span><span class="w"> </span><span class="o">=</span><span class="w"> </span>/etc/leaps-server/serverkey.pem
<span class="gp"># </span><span class="nv">gw_auth</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="m">0</span>

<span class="gp"># </span>Optional<span class="w"> </span>AES<span class="w"> </span><span class="m">128</span>-bit<span class="w"> </span>private<span class="w"> </span>key<span class="w"> </span>as<span class="w"> </span>hexadecimal<span class="w"> </span>number.<span class="w"> </span>If<span class="w"> </span>specified,<span class="w"> </span>the<span class="w"> </span>key<span class="w"> </span>is<span class="w"> </span>used<span class="w"> </span>to<span class="w"> </span>encrypt<span class="w"> </span>sensitive<span class="w"> </span>data
<span class="gp"># </span><span class="k">for</span><span class="w"> </span>example<span class="w"> </span>the<span class="w"> </span>WiFi<span class="w"> </span>password<span class="w"> </span>published<span class="w"> </span>on<span class="w"> </span>the<span class="w"> </span>MQTT<span class="w"> </span>interface.
<span class="gp"># </span><span class="nv">aes_128_key</span><span class="w"> </span><span class="o">=</span><span class="w"> </span>00112233445566778899aabbccddeeff

<span class="gp"># </span>-----------------------------------------------------------------
<span class="gp"># </span>MQTT<span class="w"> </span>Broker
<span class="gp"># </span>-----------------------------------------------------------------
<span class="gp"># </span>MQTT<span class="w"> </span>API<span class="w"> </span>variant<span class="w"> </span><span class="s2">"pans"</span><span class="w"> </span>or<span class="w"> </span><span class="s2">"leaps"</span>
<span class="go">mqtt_api = pans</span>

<span class="gp"># </span>include<span class="w"> </span>network<span class="w"> </span>ID<span class="w"> </span><span class="o">(</span>panid<span class="o">)</span><span class="w"> </span><span class="k">in</span><span class="w"> </span>the<span class="w"> </span>MQTT<span class="w"> </span>topics
<span class="go">mqtt_with_panid = true</span>

<span class="gp"># </span>Specifies<span class="w"> </span>an<span class="w"> </span><span class="nb">alias</span><span class="w"> </span><span class="k">for</span><span class="w"> </span>particular<span class="w"> </span>UWB<span class="w"> </span>network<span class="w"> </span>that<span class="w"> </span>is<span class="w"> </span><span class="k">then</span><span class="w"> </span>used<span class="w"> </span><span class="k">in</span><span class="w"> </span>the<span class="w"> </span>MQTT<span class="w"> </span>topic<span class="w"> </span>instead<span class="w"> </span>of<span class="w"> </span>the<span class="w"> </span>network<span class="w"> </span>ID<span class="w"> </span><span class="o">(</span>pan<span class="w"> </span>ID<span class="o">)</span><span class="w"> </span>.
<span class="gp"># </span>Parameter<span class="w"> </span>can<span class="w"> </span>be<span class="w"> </span>used<span class="w"> </span>multiple<span class="w"> </span><span class="nb">times</span><span class="w"> </span>and<span class="w"> </span>there<span class="w"> </span>might<span class="w"> </span>be<span class="w"> </span>multiple<span class="w"> </span>definitions<span class="w"> </span>separated<span class="w"> </span>by<span class="w"> </span>spaces<span class="w"> </span>which<span class="w"> </span>are<span class="w"> </span><span class="k">then</span><span class="w"> </span>added<span class="w"> </span>to<span class="w"> </span>the<span class="w"> </span>list<span class="w"> </span>of<span class="w"> </span>known<span class="w"> </span>aliases.
<span class="gp"># </span>Alias<span class="w"> </span>definitions<span class="w"> </span>must<span class="w"> </span>follow<span class="w"> </span>format<span class="w"> </span>&lt;ID&gt;:&lt;ALIAS_STRING&gt;.<span class="w"> </span>Multiple<span class="w"> </span>definitions<span class="w"> </span>must<span class="w"> </span>be<span class="w"> </span>separated<span class="w"> </span>with<span class="w"> </span>spaces.
<span class="gp"># </span>Network<span class="w"> </span>ID<span class="w"> </span><span class="o">(</span>PAN<span class="w"> </span>ID<span class="o">)</span><span class="w"> </span>can<span class="w"> </span>be<span class="w"> </span>hexadecimal<span class="w"> </span>number<span class="w"> </span><span class="o">(</span>withe<span class="w"> </span>prefix<span class="w"> </span><span class="se">\"</span>0x<span class="se">\"</span><span class="o">)</span><span class="w"> </span>or<span class="w"> </span>decimal<span class="w"> </span>number.
<span class="gp"># </span><span class="nv">mqtt_panid_alias</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="o">[</span><span class="m">123</span>:NetworkA<span class="o">]</span><span class="w"> </span><span class="o">[</span>0x0002:Net<span class="w"> </span>B<span class="o">]</span>
<span class="gp"># </span><span class="nv">mqtt_panid_alias</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="o">[</span>0XABCD:Network_C<span class="o">]</span>

<span class="go">mqtt_clid = 1</span>
<span class="go">mqtt_port = 1883</span>
<span class="go">mqtt_host = localhost # Or your Computer's IP Address</span>

<span class="gp"># </span>For<span class="w"> </span>PANS<span class="w"> </span>PRO<span class="w"> </span>RTLS
<span class="go">mqtt_user = pans</span>
<span class="go">mqtt_password = panspass</span>
<span class="go">mqtt_topic_prefix = pans</span>

<span class="gp"># </span>For<span class="w"> </span>PANS<span class="w"> </span>PRO<span class="w"> </span>RTLS
<span class="gp"># </span><span class="nv">mqtt_user</span><span class="w"> </span><span class="o">=</span><span class="w"> </span>dwmuser
<span class="gp"># </span><span class="nv">mqtt_password</span><span class="w"> </span><span class="o">=</span><span class="w"> </span>dwmpass
<span class="gp"># </span><span class="nv">mqtt_topic_prefix</span><span class="w"> </span><span class="o">=</span><span class="w"> </span>dwm

<span class="gp"># </span>Certificates<span class="w"> </span>used<span class="w"> </span>on<span class="w"> </span>MQTT<span class="w"> </span>interface
<span class="gp"># </span><span class="nv">mqtt_cafile</span><span class="w"> </span><span class="o">=</span><span class="w"> </span>/etc/leaps-server/cacert.pem
<span class="gp"># </span><span class="nv">mqtt_certfile</span><span class="w"> </span><span class="o">=</span><span class="w"> </span>/etc/leaps-server/servercert.pem
<span class="gp"># </span><span class="nv">mqtt_keyfile</span><span class="w"> </span><span class="o">=</span><span class="w"> </span>/etc/leaps-server/serverkey.pem

<span class="gp"># </span>Period<span class="w"> </span><span class="k">in</span><span class="w"> </span>seconds<span class="w"> </span>after<span class="w"> </span>which<span class="w"> </span>all<span class="w"> </span>retained<span class="w"> </span>topics<span class="w"> </span>are<span class="w"> </span>published<span class="w"> </span>regardless
<span class="gp"># </span>whether<span class="w"> </span>the<span class="w"> </span>content<span class="w"> </span>has<span class="w"> </span>changed<span class="w"> </span>or<span class="w"> </span>not.<span class="w"> </span>Disabled<span class="w"> </span>when<span class="w"> </span><span class="nb">set</span><span class="w"> </span>to<span class="w"> </span><span class="m">0</span>.<span class="w"> </span>Disabled<span class="w"> </span>by<span class="w"> </span>default.
<span class="gp">#</span><span class="nv">mqtt_refresh</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="m">0</span>

<span class="gp"># </span>-----------------------------------------------------------------
<span class="gp"># </span>Secondary<span class="w"> </span>MQTT<span class="w"> </span>Broker
<span class="gp"># </span>-----------------------------------------------------------------
<span class="gp">#</span>
<span class="gp"># </span><span class="nv">mqtt_clid_sec</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="m">2</span>
<span class="gp"># </span><span class="nv">mqtt_port_sec</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="m">1883</span>
<span class="gp"># </span><span class="nv">mqtt_host_sec</span><span class="w"> </span><span class="o">=</span>

<span class="gp"># </span>For<span class="w"> </span>PANS<span class="w"> </span>PRO<span class="w"> </span>RTLS
<span class="gp"># </span><span class="nv">mqtt_user_sec</span><span class="w"> </span><span class="o">=</span><span class="w"> </span>dwmuser
<span class="gp"># </span><span class="nv">mqtt_password_sec</span><span class="w"> </span><span class="o">=</span><span class="w"> </span>dwmpass

<span class="gp"># </span>Certificates<span class="w"> </span>used<span class="w"> </span>on<span class="w"> </span>MQTT<span class="w"> </span>interface
<span class="gp"># </span><span class="nv">mqtt_cafile_sec</span><span class="w"> </span><span class="o">=</span><span class="w"> </span>/etc/leaps-server/cacert.pem
<span class="gp"># </span><span class="nv">mqtt_certfile_sec</span><span class="w"> </span><span class="o">=</span><span class="w"> </span>/etc/leaps-server/servercert.pem
<span class="gp"># </span><span class="nv">mqtt_keyfile_sec</span><span class="w"> </span><span class="o">=</span><span class="w"> </span>/etc/leaps-server/serverkey.pem

<span class="gp"># </span>-----------------------------------------------------------------
<span class="gp"># </span>TCP
<span class="gp"># </span>-----------------------------------------------------------------
<span class="gp">#</span>
<span class="go">tcp_port = 7777</span>

<span class="gp"># </span>-----------------------------------------------------------------
<span class="gp"># </span>Other
<span class="gp"># </span>-----------------------------------------------------------------
<span class="gp"># </span>maximum<span class="w"> </span>number<span class="w"> </span>of<span class="w"> </span>attempts<span class="w"> </span>of<span class="w"> </span>configuration<span class="w"> </span>and<span class="w"> </span>service<span class="w"> </span>commands
<span class="gp"># </span><span class="nv">cmd_att</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="m">3</span>
</pre></div>
</div>
</div></blockquote>
<ol class="arabic simple" start="3">
<li><p>在电脑上打开命令提示符或终端窗口。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>导航到创建配置文件的文件夹。</p></li>
</ul>
<p>例如，在 Ubuntu (Linux) 上：</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">cd leaps_server_hub/</span>
</pre></div>
</div>
</div></blockquote>
<ol class="arabic simple" start="4">
<li><p>安装 LEAPS Server Docker 软件包并运行：</p></li>
</ol>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">docker run -d -p 7777:7777/tcp -p 7777:7777/udp --name some_name -v /path/to/data/data/:/app/data/ leapslabs/leaps_server:tag /app/leaps-server --cfg /app/data/leaps-server.conf</span>
</pre></div>
</div>
<p>其中 <code class="docutils literal notranslate"><span class="pre">some_name</span></code> 是您要分配给容器的名称，<code class="docutils literal notranslate"><span class="pre">tag</span></code> 是指定您想要的 <code class="docutils literal notranslate"><span class="pre">leaps-server</span></code> 版本的标签。</p>
<p>leaps_server实例正在使用端口 <code class="docutils literal notranslate"><span class="pre">7777</span></code> 与网关进行 <code class="docutils literal notranslate"><span class="pre">TCP</span></code> 和 <code class="docutils literal notranslate"><span class="pre">UDP</span></code> 通信，因此需要使用命令 <code class="docutils literal notranslate"><span class="pre">-p</span> <span class="pre">7777:7777/tcp</span> <span class="pre">-p</span> <span class="pre">7777:7777/udp</span></code> 将这些端口从主机重新映射到leaps_server实例。</p>
<p>除非需要，否则不建议更改端口号。如果需要修改，请相应地调整网关上的端口设置。</p>
<ul class="simple">
<li><p>推荐的运行选项</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">--user</span> <span class="pre">$(id</span> <span class="pre">-u):$(id</span> <span class="pre">-g)</span></code> 在特定用户和组下运行实例。</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">--restart</span> <span class="pre">unless-stopped</span></code> 自动重启实例，以防服务器崩溃。</p></li>
</ul>
</li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="5">
<li><p>LEAPS Server安装过程将开始。</p></li>
</ol>
<blockquote>
<div><p>例如，在 Ubuntu (Linux) 上：</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">docker run -d -p 7777:7777/tcp -p 7777:7777/udp --name leaps_server -v "$(pwd)"/data/:/app/data leapslabs/leaps_server:latest /app/leaps-server --cfg /app/data/leaps-server.conf</span>

<span class="go">Unable to find image 'leapslabs/leaps_server:latest' locally</span>
<span class="go">latest: Pulling from leapslabs/leaps_server</span>
<span class="go">a458657ccc71: Pull complete</span>
<span class="go">Digest: sha256:a19b127656d41d8607f043c2c83924e5b9a5cbd4dc23cfbed070be3b9cfc6b9a</span>
<span class="go">Status: Downloaded newer image for leapslabs/leaps_server:latest</span>
<span class="go">320d3768289874e063619f75faca7a24dd75a08884df8cd8fb2cc9b54c6f0a46</span>
</pre></div>
</div>
</div></blockquote>
<ol class="arabic simple" start="6">
<li><p>确认安装成功，运行：</p></li>
</ol>
<blockquote>
<div><p>例如，在 Ubuntu (Linux) 上：</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">docker ps</span>

<span class="go">CONTAINER ID   IMAGE                    COMMAND                  CREATED          STATUS                          PORTS     NAMES</span>
<span class="go">b1145b72db35   leapslabs/leaps_server:latest   "sh -c 'cd /app &amp;&amp;  …"   37 seconds ago   11 seconds ago                            leaps_server</span>
</pre></div>
</div>
</div></blockquote>
<p>因此，您已经在PC上成功安装并启动了LEAPS Server。</p>
</div>
</div>
<hr class="docutils">
<div class="section" id="getting-started">
<h2>开始</h2>
<div class="section" id="leaps-server-docker">
<h3>LEAPS Server Docker</h3>
<ul class="simple">
<li><p>启动LEAPS Server，运行:<code class="docutils literal notranslate"><span class="pre">docker</span> <span class="pre">start</span> <span class="pre">leaps_server</span></code></p></li>
<li><p>停止LEAPS Server，运行:<code class="docutils literal notranslate"><span class="pre">docker</span> <span class="pre">stop</span> <span class="pre">leaps_server</span></code></p></li>
<li><p>重启LEAPS Server，运行:<code class="docutils literal notranslate"><span class="pre">docker</span> <span class="pre">restart</span> <span class="pre">leaps_server</span></code></p></li>
<li><p>删除LEAPS Server，运行``docker rm –force leaps_server``</p></li>
</ul>
</div>
<hr class="docutils">
<div class="section" id="network-configuration">
<h3>网络配置</h3>
<ul>
<li><p>MQTT API变体“pans”或“leaps”</p></li>
<li><p>将LEAPS ID添加到已发布的主题中</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">mqtt_with_panid = true</span>

<span class="go">mqtt_clid = 1</span>
<span class="go">mqtt_port = 1883</span>
<span class="go">mqtt_host = localhost # Or your Computer's IP Address</span>
</pre></div>
</div>
</li>
<li><p>LEAPS RTLS帐户配置</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">mqtt_user = pansuser</span>
<span class="go">mqtt_password = panspass</span>
<span class="go">mqtt_topic_prefix = pans</span>
</pre></div>
</div>
</li>
<li><p>TCP端口为7777</p></li>
</ul>
</div>
</div>
<div class="section" id="troubleshooting">
<h2>故障排除</h2>
<ul class="simple">
<li><p>使用以下命令 <code class="docutils literal notranslate"><span class="pre">docker</span> <span class="pre">restart</span> <span class="pre">leaps_server</span></code> 重新启动LEAPS Server。</p></li>
<li><p>当 <a class="reference internal" href="#pans-pro-server"><span class="std std-ref">LEAPS Server</span></a> 运行时，检查日志，打开Docker桌面并选择leaps_server容器。</p></li>
</ul>
</div>
</div>


           </div>
