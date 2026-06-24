---
title: "LEAPS Gateway"
lang: zh
slug: "leaps-rtls/infrastructure/leaps-gateway"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/leaps-rtls/infrastructure/leaps-gateway/"
order: 71
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-gateway">
<span id="leapsgateway"></span><h1>LEAPS Gateway</h1>
<p>LEAPS Gateway是 UWB 和 TCP/IP 网络之间的关梁。</p>
<hr class="docutils">
<div class="section" id="key-features">
<h2>主要功能</h2>
<ul class="simple">
<li><p>LEAPS Gateway一侧通过通用LEAPS API、SPI或USB与LEAPS UWBS通信，另一侧通过TCP/IP与LEAPS Server通信。</p></li>
<li><p>根据LEAPS UWB网络配置文件，它提供了一种媒介，用于向MQTT代理传输锚和标签的上行链路和下行链路位置以及遥测数据。</p></li>
<li><p>与UWBS的互连是通过专用LEAPS Gateway嵌入式设备上的SPI完成的。当与LEAPS UWBS的互连通过USB完成时，就像UDK设备的情况一样，LEAPS Gateway作为守护进程服务在Linux平台上运行。</p></li>
</ul>
</div>
<hr class="docutils">
<div class="section" id="installation">
<h2>安装</h2>
<div class="section" id="system-requirements">
<h3>系统要求</h3>
<p>Docker的系统要求因操作系统而异。</p>
<ul class="simple">
<li><p>对于 Linux，您需要 64 位架构, 兼容的内核版本和特定的内核功能。</p></li>
<li><p>在 Windows 上，在启用虚拟化的 Windows 10上使用 Docker Desktop</p></li>
<li><p>在 macOS 上，请使用配备 macOS 10.13 或更新版本的Docker Desktop. 在硬件方面，建议至少配备 2GB 内存以及足够的 CPU 和磁盘空间。</p></li>
</ul>
<div class="admonition note">
<p class="admonition-title">注解</p>
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
</div>
</div></blockquote>
<ol class="arabic simple" start="2">
<li><p>创建文件夹 <code class="docutils literal notranslate"><span class="pre">leaps_gateway_hub</span></code> 和子文件夹 <code class="docutils literal notranslate"><span class="pre">data</span></code>。然后，在 <code class="docutils literal notranslate"><span class="pre">leaps_gateway_hub/data</span></code> 中添加 <code class="docutils literal notranslate"><span class="pre">leaps-gateway.conf</span></code> 配置文件。。</p></li>
</ol>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">#</span><span class="c1">######################################################################</span>
<span class="gp"># </span>LEAPS<span class="w"> </span>Gateway<span class="w"> </span>settings
<span class="gp">#</span>

<span class="gp"># </span>-----------------------------------------------------------------
<span class="gp"># </span>Logging
<span class="gp"># </span>-----------------------------------------------------------------
<span class="go">log_level = 0 #  Logging level, default is 0 (0=none, 1=fatal, 2=error, 3=warning, 4=info, 5=debug, 6=verbose)</span>

<span class="gp"># </span>Path<span class="w"> </span>to<span class="w"> </span>log<span class="w"> </span>file.<span class="w"> </span>Comment<span class="w"> </span>out<span class="w"> </span>to<span class="w"> </span>disable<span class="w"> </span>logging<span class="w"> </span>to<span class="w"> </span>file<span class="w"> </span><span class="o">(</span>log<span class="w"> </span>to<span class="w"> </span>stdio<span class="w"> </span>instead<span class="o">)</span>.
<span class="gp"># </span>log-file<span class="w"> </span><span class="o">=</span><span class="w"> </span>leaps-gateway.log


<span class="gp"># </span>LEAPS<span class="w"> </span>Server<span class="w"> </span>host
<span class="gp"># </span>Default:<span class="w"> </span>localhost
<span class="go">leaps-server-host = localhost # Or your Computer's IP Address</span>

<span class="gp"># </span>LEAPS<span class="w"> </span>Server<span class="w"> </span>port
<span class="gp"># </span>Default:<span class="w"> </span><span class="m">7777</span>
<span class="go">leaps-server-port = 7777</span>

<span class="gp"># </span>-----------------------------------------------------------------
<span class="gp"># </span>UWBS<span class="w"> </span>USB<span class="w"> </span>Device<span class="w"> </span>VID/PID
<span class="gp"># </span>-----------------------------------------------------------------
<span class="gp">#</span>

<span class="gp"># </span>Vendor<span class="w"> </span>ID,<span class="w"> </span>default<span class="w"> </span>is<span class="w"> </span>0x1915,<span class="w"> </span>possible<span class="w"> </span>values<span class="w"> </span>are<span class="w"> </span><span class="o">(</span>0x1915-Nordic,<span class="w"> </span>0x04d8-Microchip<span class="o">)</span>
<span class="gp"># </span>Allowed<span class="w"> </span>values:<span class="w"> </span><span class="m">16</span>-bit<span class="w"> </span>number<span class="w"> </span><span class="k">in</span><span class="w"> </span>decimal,<span class="w"> </span>hexadecimal<span class="w"> </span>or<span class="w"> </span>octal<span class="w"> </span>format
<span class="gp"># </span>uwbs-usb-dev-vid<span class="w"> </span><span class="o">=</span><span class="w"> </span>0x04d8
<span class="go">uwbs-usb-dev-vid = 0x1915</span>

<span class="gp"># </span>Product<span class="w"> </span>ID,<span class="w"> </span>default<span class="w"> </span>is<span class="w"> </span>0xe8e3<span class="w"> </span><span class="k">for</span><span class="w"> </span>LEAPS<span class="w"> </span>RTLS<span class="w"> </span>devices
<span class="gp"># </span>Allowed<span class="w"> </span>values:<span class="w"> </span><span class="m">16</span>-bit<span class="w"> </span>number<span class="w"> </span><span class="k">in</span><span class="w"> </span>decimal,<span class="w"> </span>hexadecimal<span class="w"> </span>or<span class="w"> </span>octal<span class="w"> </span>format
<span class="go">uwbs-usb-dev-pid = 0xe8e3</span>

<span class="gp"># </span>-----------------------------------------------------------------
<span class="gp"># </span>UWBS<span class="w"> </span>device<span class="w"> </span>configurations
<span class="gp"># </span>-----------------------------------------------------------------
<span class="gp">#</span>

<span class="gp"># </span>Gateway<span class="w"> </span>mode
<span class="gp"># </span>Allowed<span class="w"> </span>values:<span class="w"> </span><span class="nv">0</span><span class="o">=</span>Disable<span class="w"> </span><span class="nv">1</span><span class="o">=</span>Enable
<span class="gp"># </span>Default:<span class="w"> </span><span class="o">(</span>keep-current<span class="o">)</span>
<span class="gp"># </span>uwbs-gateway<span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="m">0</span>

<span class="gp"># </span>Initiator<span class="w"> </span>mode
<span class="gp"># </span>Allowed<span class="w"> </span>values:<span class="w"> </span><span class="nv">0</span><span class="o">=</span>Disable<span class="w"> </span><span class="nv">1</span><span class="o">=</span>Enable
<span class="gp"># </span>Default:<span class="w"> </span><span class="o">(</span>keep-current<span class="o">)</span>
<span class="gp"># </span>uwbs-initiator<span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="m">0</span>

<span class="gp"># </span>UWBMAC<span class="w"> </span>Profile<span class="w"> </span>ID
<span class="gp"># </span>Default:<span class="w"> </span><span class="o">(</span>keep-current<span class="o">)</span>
<span class="gp"># </span>uwbs-profile-id<span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="m">0</span>

<span class="gp"># </span>LEDs<span class="w"> </span>mode
<span class="gp"># </span>Allowed<span class="w"> </span>values:<span class="w"> </span><span class="nv">0</span><span class="o">=</span>Disable<span class="w"> </span><span class="nv">1</span><span class="o">=</span>Enable
<span class="gp"># </span>Default:<span class="w"> </span><span class="o">(</span>keep-current<span class="o">)</span>
<span class="gp"># </span>uwbs-led<span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="m">1</span>

<span class="gp"># </span>UWB<span class="w"> </span>encryption
<span class="gp"># </span>Allowed<span class="w"> </span>values:<span class="w"> </span><span class="nv">0</span><span class="o">=</span>Disable<span class="w"> </span><span class="nv">1</span><span class="o">=</span>Enable
<span class="gp"># </span>Default:<span class="w"> </span><span class="o">(</span>keep-current<span class="o">)</span>
<span class="gp"># </span>uwbs-enc<span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="m">0</span>

<span class="gp"># </span>UWB<span class="w"> </span>firmware<span class="w"> </span>update
<span class="gp"># </span>Allowed<span class="w"> </span>values:<span class="w"> </span><span class="nv">0</span><span class="o">=</span>Disable<span class="w"> </span><span class="nv">1</span><span class="o">=</span>Enable
<span class="gp"># </span>Default:<span class="w"> </span><span class="o">(</span>keep-current<span class="o">)</span>
<span class="gp"># </span>uwbs-fwup<span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="m">0</span>

<span class="gp"># </span>UWB<span class="w"> </span>mode
<span class="gp"># </span>Allowed<span class="w"> </span>values:<span class="w"> </span><span class="nv">0</span><span class="o">=</span>Off<span class="w"> </span><span class="nv">1</span><span class="o">=</span>Passive<span class="w"> </span><span class="nv">2</span><span class="o">=</span>Active
<span class="gp"># </span>Default:<span class="w"> </span><span class="o">(</span>keep-current<span class="o">)</span>
<span class="gp"># </span>uwbs-uwb<span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="m">2</span>

<span class="gp"># </span>UWB<span class="w"> </span>Backhaul<span class="w"> </span>Routing
<span class="gp"># </span>Allowed<span class="w"> </span>values:<span class="w"> </span><span class="nv">0</span><span class="o">=</span>Off<span class="w"> </span><span class="nv">1</span><span class="o">=</span>On<span class="w"> </span><span class="nv">2</span><span class="o">=</span>Auto
<span class="gp"># </span>Default:<span class="w"> </span><span class="o">(</span>keep-current<span class="o">)</span>
<span class="go">uwbs-bh = 1</span>

<span class="gp"># </span>BLE
<span class="gp"># </span>Allowed<span class="w"> </span>values:<span class="w"> </span><span class="nv">0</span><span class="o">=</span>Off<span class="w"> </span><span class="nv">1</span><span class="o">=</span>On
<span class="gp"># </span>Default:<span class="w"> </span><span class="o">(</span>keep-current<span class="o">)</span>
<span class="gp"># </span>uwbs-ble<span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="m">1</span>

<span class="gp"># </span>UWB<span class="w"> </span>encryption<span class="w"> </span>key
<span class="gp"># </span>Allowed<span class="w"> </span>values:<span class="w"> </span><span class="m">128</span>-bit<span class="w"> </span>number<span class="w"> </span><span class="k">in</span><span class="w"> </span>hexadecimal<span class="w"> </span>format
<span class="gp"># </span>Default:<span class="w"> </span><span class="o">(</span>keep-current<span class="o">)</span>
<span class="gp"># </span>uwbs-enc-key<span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="m">11111111222222223333333344444444</span>

<span class="gp"># </span>UWB<span class="w"> </span>network<span class="w"> </span>PANID
<span class="gp"># </span>Allowed<span class="w"> </span>values:<span class="w"> </span><span class="m">16</span>-bit<span class="w"> </span>number<span class="w"> </span><span class="k">in</span><span class="w"> </span>decimal,<span class="w"> </span>hexadecimal<span class="w"> </span>or<span class="w"> </span>octal<span class="w"> </span>format
<span class="gp"># </span>Default:<span class="w"> </span><span class="o">(</span>keep-current<span class="o">)</span>
<span class="gp"># </span>uwbs-panid<span class="w"> </span><span class="o">=</span><span class="w"> </span>0x0000

<span class="gp"># </span>Device<span class="w"> </span>label
<span class="gp"># </span>Default:<span class="w"> </span><span class="o">(</span>keep-current<span class="o">)</span>
<span class="gp"># </span>uwbs-label<span class="w"> </span><span class="o">=</span><span class="w"> </span>gw-uwbs

<span class="gp"># </span>Device<span class="w"> </span>position<span class="w"> </span><span class="k">in</span><span class="w"> </span>mm<span class="w"> </span><span class="o">[</span>x,<span class="w"> </span>y,<span class="w"> </span>z<span class="o">]</span>
<span class="gp"># </span>Default:<span class="w"> </span><span class="o">(</span>keep-current<span class="o">)</span>
<span class="gp"># </span>uwbs-pos-x<span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="m">0</span>
<span class="gp"># </span>uwbs-pos-y<span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="m">0</span>
<span class="gp"># </span>uwbs-pos-z<span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="m">0</span>
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
<p>例如，在Ubuntu（Linux）上：</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">cd leaps_gateway_hub/</span>
</pre></div>
</div>
</div></blockquote>
<ol class="arabic simple" start="4">
<li><p>安装 LEAPS Gateway Docker 软件包并运行：</p></li>
</ol>
<blockquote>
<div><div class="admonition note">
<p class="admonition-title">注解</p>
<p>LEAPS Gateway需要使用USB端口。因此，用户需要以管理员权限运行才能在docker容器上挂载和使用USB。</p>
</div>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">sudo docker run -d -it --name some_name --privileged -v /dev/bus/usb:/dev/bus/usb -v /path/to/data/data/:/app/data/ leapslabs/leaps_gateway:tag /app/leaps_gateway --cfg /app/data/leaps_gateway.conf</span>
</pre></div>
</div>
<p>其中 <code class="docutils literal notranslate"><span class="pre">some_name</span></code> 是您要分配给容器的名称，<code class="docutils literal notranslate"><span class="pre">tag</span></code> 指定您想要的 <code class="docutils literal notranslate"><span class="pre">leaps-gateway</span></code> 版本。</p>
<ul class="simple">
<li><p>推荐的运行选项</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">--user</span> <span class="pre">$(id</span> <span class="pre">-u):$(id</span> <span class="pre">-g)</span></code> 在特定用户和组下运行实例。</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">--除非停止否则重新启动</span></code> 自动重新启动实例，以防服务器崩溃。</p></li>
</ul>
</li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="5">
<li><p>The LEAPS Gateway安装过程将开始。</p></li>
</ol>
<blockquote>
<div><p>例如，在Ubuntu（Linux）上：</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">sudo docker run -d -it --name leaps_gateway --privileged -v /dev/bus/usb:/dev/bus/usb -v "$(pwd)"/data/:/app/data leapslabs/leaps_gateway:latest /app/leaps-gateway -c /app/data/leaps-gateway.conf</span>

<span class="go">Unable to find image 'leapslabs/leaps_gateway:latest' locally</span>
<span class="go">latest: Pulling from leapslabs/leaps_gateway</span>
<span class="go">a458657ccc71: Pull complete</span>
<span class="go">Digest: sha256:a19b127656d41d8607f043c2c83924e5b9a5cbd4dc23cfbed070be3b9cfc6b9a</span>
<span class="go">Status: Downloaded newer image for leapslabs/leaps_gateway:latest</span>
<span class="go">320d3768289874e063619f75faca7a24dd75a08884df8cd8fb2cc9b54c6f0a46</span>
</pre></div>
</div>
</div></blockquote>
<ol class="arabic simple" start="6">
<li><p>确认安装成功，运行：</p></li>
</ol>
<blockquote>
<div><p>例如，在Ubuntu（Linux）上：</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">sudo docker ps</span>

<span class="go">CONTAINER ID   IMAGE                    COMMAND                  CREATED          STATUS                          PORTS     NAMES</span>
<span class="go">b1145b72db35   leapslabs/leaps_gateway:latest   "sh -c 'cd /app &amp;&amp;  …"   37 seconds ago   11 seconds ago                           leaps_gateway</span>
</pre></div>
</div>
</div></blockquote>
<p>因此，您已在PC上成功安装并启动 LEAPS Gateway 。</p>
</div>
</div>
<hr class="docutils">
<div class="section" id="getting-started">
<h2>开始</h2>
<div class="section" id="leaps-gateway-docker">
<h3>LEAPS Gateway Docker</h3>
<ul class="simple">
<li><p>启动LEAPS Gateway，运行: <code class="docutils literal notranslate"><span class="pre">sudo</span> <span class="pre">docker</span> <span class="pre">Start</span> <span class="pre">LEAPS_Gateway</span></code></p></li>
<li><p>停止LEAPS Gateway，运行: <code class="docutils literal notranslate"><span class="pre">sudo</span> <span class="pre">docker</span> <span class="pre">Stop-LEAPS_Gateway</span></code></p></li>
<li><p>重启LEAPS Gateway，运行: <code class="docutils literal notranslate"><span class="pre">sudo</span> <span class="pre">docker</span> <span class="pre">Restart</span> <span class="pre">LEAPS_Gateway</span></code></p></li>
<li><p>删除LEAPS Gateway，运行 <code class="docutils literal notranslate"><span class="pre">sudo</span> <span class="pre">docker</span> <span class="pre">rm--force</span> <span class="pre">LEAPS_Gateway</span></code></p></li>
</ul>
</div>
<hr class="docutils">
<div class="section" id="network-configuration">
<h3>网络配置</h3>
<ul>
<li><p>记录</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp"># </span>Logging<span class="w"> </span>level,<span class="w"> </span>default<span class="w"> </span>is<span class="w"> </span><span class="m">3</span><span class="w"> </span><span class="o">(</span><span class="nv">0</span><span class="o">=</span>none,<span class="w"> </span><span class="nv">1</span><span class="o">=</span>error,<span class="w"> </span><span class="nv">2</span><span class="o">=</span>warning,<span class="w"> </span><span class="nv">3</span><span class="o">=</span>info,<span class="w"> </span><span class="nv">4</span><span class="o">=</span>debug,<span class="w"> </span><span class="nv">5</span><span class="o">=</span>verbose<span class="o">)</span>.
<span class="go">log-level = 0</span>

<span class="gp"># </span>Path<span class="w"> </span>to<span class="w"> </span>log<span class="w"> </span>file.<span class="w"> </span>Comment<span class="w"> </span>out<span class="w"> </span>to<span class="w"> </span>disable<span class="w"> </span>logging<span class="w"> </span>to<span class="w"> </span>file<span class="w"> </span><span class="o">(</span>log<span class="w"> </span>to<span class="w"> </span>stdio<span class="w"> </span>instead<span class="o">)</span>.
<span class="go">log-file = leaps-gateway.log</span>
</pre></div>
</div>
</li>
<li><p>LEAPS Server主机</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp"># </span>Default:<span class="w"> </span>localhost
<span class="go">leaps-server-host = 192.168.1.1 # Your Computer's IP Address</span>

<span class="gp"># </span>LEAPS<span class="w"> </span>Server<span class="w"> </span>port
<span class="gp"># </span>Default:<span class="w"> </span><span class="m">7777</span>
<span class="go">leaps-server-port = 7777</span>
</pre></div>
</div>
</li>
<li><p>UWBS USB设备VID/PID</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp"># </span>Vendor<span class="w"> </span>ID,<span class="w"> </span>default<span class="w"> </span>is<span class="w"> </span>0x1915,<span class="w"> </span>possible<span class="w"> </span>values<span class="w"> </span>are<span class="w"> </span><span class="o">(</span>0x1915-Nordic,<span class="w"> </span>0x04d8-Microchip<span class="o">)</span>
<span class="gp"># </span>Allowed<span class="w"> </span>values:<span class="w"> </span><span class="m">16</span>-bit<span class="w"> </span>number<span class="w"> </span><span class="k">in</span><span class="w"> </span>decimal,<span class="w"> </span>hexadecimal<span class="w"> </span>or<span class="w"> </span>octal<span class="w"> </span>format
<span class="gp"># </span>uwbs-usb-dev-vid<span class="w"> </span><span class="o">=</span><span class="w"> </span>0x04d8
<span class="go">uwbs-usb-dev-vid = 0x1915</span>

<span class="gp"># </span>Product<span class="w"> </span>ID,<span class="w"> </span>default<span class="w"> </span>is<span class="w"> </span>0xe8e3<span class="w"> </span><span class="k">for</span><span class="w"> </span>LEAPS<span class="w"> </span>RTLS<span class="w"> </span>devices
<span class="gp"># </span>Allowed<span class="w"> </span>values:<span class="w"> </span><span class="m">16</span>-bit<span class="w"> </span>number<span class="w"> </span><span class="k">in</span><span class="w"> </span>decimal,<span class="w"> </span>hexadecimal<span class="w"> </span>or<span class="w"> </span>octal<span class="w"> </span>format
<span class="go">uwbs-usb-dev-pid = 0xe8e3</span>
</pre></div>
</div>
</li>
<li><p>UWBS设备配置</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp"># </span>Gateway<span class="w"> </span>mode
<span class="gp"># </span>Allowed<span class="w"> </span>values:<span class="w"> </span><span class="nv">0</span><span class="o">=</span>Disable<span class="w"> </span><span class="nv">1</span><span class="o">=</span>Enable
<span class="gp"># </span>Default:<span class="w"> </span><span class="o">(</span>keep-current<span class="o">)</span>
<span class="go">uwbs-gateway = 0</span>

<span class="gp"># </span>Initiator<span class="w"> </span>mode
<span class="gp"># </span>Allowed<span class="w"> </span>values:<span class="w"> </span><span class="nv">0</span><span class="o">=</span>Disable<span class="w"> </span><span class="nv">1</span><span class="o">=</span>Enable
<span class="gp"># </span>Default:<span class="w"> </span><span class="o">(</span>keep-current<span class="o">)</span>
<span class="go">uwbs-initiator = 0</span>

<span class="gp"># </span>UWBMAC<span class="w"> </span>Profile<span class="w"> </span>ID
<span class="gp"># </span>Default:<span class="w"> </span><span class="o">(</span>keep-current<span class="o">)</span>
<span class="go">uwbs-profile-id = 0</span>

<span class="gp"># </span>LEDs<span class="w"> </span>mode
<span class="gp"># </span>Allowed<span class="w"> </span>values:<span class="w"> </span><span class="nv">0</span><span class="o">=</span>Disable<span class="w"> </span><span class="nv">1</span><span class="o">=</span>Enable
<span class="gp"># </span>Default:<span class="w"> </span><span class="o">(</span>keep-current<span class="o">)</span>
<span class="go">uwbs-led = 1</span>

<span class="gp"># </span>UWB<span class="w"> </span>encryption
<span class="gp"># </span>Allowed<span class="w"> </span>values:<span class="w"> </span><span class="nv">0</span><span class="o">=</span>Disable<span class="w"> </span><span class="nv">1</span><span class="o">=</span>Enable
<span class="gp"># </span>Default:<span class="w"> </span><span class="o">(</span>keep-current<span class="o">)</span>
<span class="go">uwbs-enc = 0</span>

<span class="gp"># </span>UWB<span class="w"> </span>firmware<span class="w"> </span>update
<span class="gp"># </span>Allowed<span class="w"> </span>values:<span class="w"> </span><span class="nv">0</span><span class="o">=</span>Disable<span class="w"> </span><span class="nv">1</span><span class="o">=</span>Enable
<span class="gp"># </span>Default:<span class="w"> </span><span class="o">(</span>keep-current<span class="o">)</span>
<span class="go">uwbs-fwup = 0</span>

<span class="gp"># </span>UWB<span class="w"> </span>mode
<span class="gp"># </span>Allowed<span class="w"> </span>values:<span class="w"> </span><span class="nv">0</span><span class="o">=</span>Off<span class="w"> </span><span class="nv">1</span><span class="o">=</span>Passive<span class="w"> </span><span class="nv">2</span><span class="o">=</span>Active
<span class="gp"># </span>Default:<span class="w"> </span><span class="o">(</span>keep-current<span class="o">)</span>
<span class="go">uwbs-uwb = 2</span>

<span class="gp"># </span>UWB<span class="w"> </span>Backhaul<span class="w"> </span>Routing
<span class="gp"># </span>Allowed<span class="w"> </span>values:<span class="w"> </span><span class="nv">0</span><span class="o">=</span>Off<span class="w"> </span><span class="nv">1</span><span class="o">=</span>On<span class="w"> </span><span class="nv">2</span><span class="o">=</span>Auto
<span class="gp"># </span>Default:<span class="w"> </span><span class="o">(</span>keep-current<span class="o">)</span>
<span class="go">uwbs-bh = 1</span>

<span class="gp"># </span>BLE
<span class="gp"># </span>Allowed<span class="w"> </span>values:<span class="w"> </span><span class="nv">0</span><span class="o">=</span>Off<span class="w"> </span><span class="nv">1</span><span class="o">=</span>On
<span class="gp"># </span>Default:<span class="w"> </span><span class="o">(</span>keep-current<span class="o">)</span>
<span class="go">uwbs-ble = 1</span>

<span class="gp"># </span>UWB<span class="w"> </span>encryption<span class="w"> </span>key
<span class="gp"># </span>Allowed<span class="w"> </span>values:<span class="w"> </span><span class="m">128</span>-bit<span class="w"> </span>number<span class="w"> </span><span class="k">in</span><span class="w"> </span>hexadecimal<span class="w"> </span>format
<span class="gp"># </span>Default:<span class="w"> </span><span class="o">(</span>keep-current<span class="o">)</span>
<span class="go">uwbs-enc-key = 11111111222222223333333344444444</span>

<span class="gp"># </span>UWB<span class="w"> </span>network<span class="w"> </span>PANID
<span class="gp"># </span>Allowed<span class="w"> </span>values:<span class="w"> </span><span class="m">16</span>-bit<span class="w"> </span>number<span class="w"> </span><span class="k">in</span><span class="w"> </span>decimal,<span class="w"> </span>hexadecimal<span class="w"> </span>or<span class="w"> </span>octal<span class="w"> </span>format
<span class="gp"># </span>Default:<span class="w"> </span><span class="o">(</span>keep-current<span class="o">)</span>
<span class="go">uwbs-panid = 0x0000</span>

<span class="gp"># </span>Device<span class="w"> </span>label
<span class="gp"># </span>Default:<span class="w"> </span><span class="o">(</span>keep-current<span class="o">)</span>
<span class="go">uwbs-label = gw-uwbs</span>

<span class="gp"># </span>Device<span class="w"> </span>position<span class="w"> </span><span class="k">in</span><span class="w"> </span>mm<span class="w"> </span><span class="o">[</span>x,<span class="w"> </span>y,<span class="w"> </span>z<span class="o">]</span>
<span class="gp"># </span>Default:<span class="w"> </span><span class="o">(</span>keep-current<span class="o">)</span>
<span class="go">uwbs-pos-x = 0</span>
<span class="go">uwbs-pos-y = 0</span>
<span class="go">uwbs-pos-z = 0</span>
</pre></div>
</div>
</li>
</ul>
</div>
</div>
<hr class="docutils">
<div class="section" id="troubleshooting">
<h2>故障排除</h2>
<ul class="simple">
<li><p>使用以下命令 <code class="docutils literal notranslate"><span class="pre">sudo</span> <span class="pre">docker</span> <span class="pre">restart</span> <span class="pre">leaps_gateway</span></code> 重新启动LEAPS Gateway。</p></li>
<li><p>在windows上，重复USB/IP连接WSL 2以连接USB设备。（<code class="docutils literal notranslate"><span class="pre">usbipd</span> <span class="pre">wsl附加--busid&lt;busid&gt;</span></code>）</p></li>
</ul>
</div>
</div>


           </div>
