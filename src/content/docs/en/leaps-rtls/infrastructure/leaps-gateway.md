---
title: "LEAPS Gateway"
lang: en
slug: "leaps-rtls/infrastructure/leaps-gateway"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/leaps-rtls/infrastructure/leaps-gateway/"
order: 71
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-gateway">
<span id="leapsgateway"></span><h1>LEAPS Gateway</h1>
<p>LEAPS Gateway serves as a gateway between the UWB and the TCP/IP networks.</p>
<hr class="docutils">
<div class="section" id="key-features">
<h2>Key Features</h2>
<ul class="simple">
<li><p>The LEAPS Gateway communicates on one side with the LEAPS UWBS via the generic LEAPS API, SPI, or USB and on the other side with the LEAPS Server via the TCP/IP.</p></li>
<li><p>Depending on the LEAPS UWB networking profile, it provides a medium for transferring the uplink and downlink location and telemetry data of the Anchors and Tags to and from the MQTT Broker.</p></li>
<li><p>The interconnection with the UWBS is done via the SPI on a dedicated LEAPS Gateway embedded device. When the interconnection with the LEAPS UWBS is done via the USB, like in the case of the UDK devices, LEAPS Gateway runs on a Linux platform as a daemon service.</p></li>
</ul>
</div>
<hr class="docutils">
<div class="section" id="installation">
<h2>Installation</h2>
<div class="section" id="system-requirements">
<h3>System Requirements</h3>
<p>Docker’s system requirements vary based on the operating system.</p>
<ul class="simple">
<li><p>For Linux, you need a 64-bit architecture, a compatible kernel version, and specific kernel features.</p></li>
<li><p>On Windows, use Docker Desktop on Windows 10 with virtualization enabled.</p></li>
<li><p>On macOS, use Docker Desktop with macOS 10.13 or newer. In terms of hardware, a minimum of 2GB RAM is recommended, along with sufficient CPU and disk space.</p></li>
</ul>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>Refer to <a class="reference external" href="https://docs.docker.com/">Docker</a> official documentation for up-to-date details.</p>
</div>
</div>
<hr class="docutils">
<div class="section" id="instructions">
<h3>Instructions</h3>
<ol class="arabic simple">
<li><p>Install Docker on your PC</p></li>
</ol>
<blockquote>
<div><div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-0" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-0">
On Linux</label><div class="sd-tab-content docutils">
<p><a class="reference external" href="https://docs.docker.com/desktop/install/linux-install/">Install Docker Desktop on Linux</a></p>
<p>Additionally, you can refer to the following commands to install:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">curl -fsSL https://get.docker.com -o get-docker.sh</span>
<span class="go">sudo sh ./get-docker.sh</span>
<span class="go">sudo usermod -aG docker $USER</span>
</pre></div>
</div>
</div>
<input id="sd-tab-item-1" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-1">
On Windows</label><div class="sd-tab-content docutils">
<p><a class="reference external" href="https://docs.docker.com/desktop/install/windows-install/">Install Docker Desktop on Windows</a></p>
</div>
</div>
</div></blockquote>
<ol class="arabic simple" start="2">
<li><p>Create folder <code class="docutils literal notranslate"><span class="pre">leaps_gateway_hub</span></code> and subfolder <code class="docutils literal notranslate"><span class="pre">data</span></code>. Then, add the <code class="docutils literal notranslate"><span class="pre">leaps-gateway.conf</span></code> configuration file in <code class="docutils literal notranslate"><span class="pre">leaps_gateway_hub/data</span></code>.</p></li>
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
<li><p>Open a command prompt or terminal window on your PC.</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>Navigate to the folder where you created the configuration file.</p></li>
</ul>
<p>For example, on Ubuntu (Linux):</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">cd leaps_gateway_hub/</span>
</pre></div>
</div>
</div></blockquote>
<ol class="arabic simple" start="4">
<li><p>Install the LEAPS Gateway Docker packages, run:</p></li>
</ol>
<blockquote>
<div><div class="admonition note">
<p class="admonition-title">Note</p>
<p>LEAPS Gateway requires the use of a USB port. Therefore, users need to run with admin rights to mount and use USB on the docker container.</p>
</div>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">sudo docker run -d -it --name some_name --privileged -v /dev/bus/usb:/dev/bus/usb -v /path/to/data/data/:/app/data/ leapslabs/leaps_gateway:tag /app/leaps_gateway --cfg /app/data/leaps_gateway.conf</span>
</pre></div>
</div>
<p>Where <code class="docutils literal notranslate"><span class="pre">some_name</span></code> is the name you want to assign to your container, and the <code class="docutils literal notranslate"><span class="pre">tag</span></code> specifies the <code class="docutils literal notranslate"><span class="pre">leaps-gateway</span></code> version you want.</p>
<ul class="simple">
<li><p>Recommended run options</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">--user</span> <span class="pre">$(id</span> <span class="pre">-u):$(id</span> <span class="pre">-g)</span></code> Run the instance under a specific user and group.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">--restart</span> <span class="pre">unless-stopped</span></code> Restart automatically the instance in case the server would crash.</p></li>
</ul>
</li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="5">
<li><p>The LEAPS Gateway installation process will begin.</p></li>
</ol>
<blockquote>
<div><p>For example, on Ubuntu (Linux):</p>
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
<li><p>Verify that the installation is successful, run:</p></li>
</ol>
<blockquote>
<div><p>For example, on Ubuntu (Linux):</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">sudo docker ps</span>

<span class="go">CONTAINER ID   IMAGE                    COMMAND                  CREATED          STATUS                          PORTS     NAMES</span>
<span class="go">b1145b72db35   leapslabs/leaps_gateway:latest   "sh -c 'cd /app &amp;&amp;  …"   37 seconds ago   11 seconds ago                           leaps_gateway</span>
</pre></div>
</div>
</div></blockquote>
<p>So, you have successfully installed and started LEAPS Gateway on PC.</p>
</div>
</div>
<hr class="docutils">
<div class="section" id="getting-started">
<h2>Getting started</h2>
<div class="section" id="leaps-gateway-docker">
<h3>LEAPS Gateway Docker</h3>
<ul class="simple">
<li><p>Start LEAPS Gateway, run: <code class="docutils literal notranslate"><span class="pre">sudo</span> <span class="pre">docker</span> <span class="pre">start</span> <span class="pre">leaps_gateway</span></code></p></li>
<li><p>Stop LEAPS Gateway, run: <code class="docutils literal notranslate"><span class="pre">sudo</span> <span class="pre">docker</span> <span class="pre">stop</span> <span class="pre">leaps_gateway</span></code></p></li>
<li><p>Restart LEAPS Gateway, run: <code class="docutils literal notranslate"><span class="pre">sudo</span> <span class="pre">docker</span> <span class="pre">restart</span> <span class="pre">leaps_gateway</span></code></p></li>
<li><p>Remove LEAPS Gateway, run <code class="docutils literal notranslate"><span class="pre">sudo</span> <span class="pre">docker</span> <span class="pre">rm</span> <span class="pre">--force</span> <span class="pre">leaps_gateway</span></code></p></li>
</ul>
</div>
<hr class="docutils">
<div class="section" id="network-configuration">
<h3>Network Configuration</h3>
<ul>
<li><p>Logging</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp"># </span>Logging<span class="w"> </span>level,<span class="w"> </span>default<span class="w"> </span>is<span class="w"> </span><span class="m">3</span><span class="w"> </span><span class="o">(</span><span class="nv">0</span><span class="o">=</span>none,<span class="w"> </span><span class="nv">1</span><span class="o">=</span>error,<span class="w"> </span><span class="nv">2</span><span class="o">=</span>warning,<span class="w"> </span><span class="nv">3</span><span class="o">=</span>info,<span class="w"> </span><span class="nv">4</span><span class="o">=</span>debug,<span class="w"> </span><span class="nv">5</span><span class="o">=</span>verbose<span class="o">)</span>.
<span class="go">log-level = 0</span>

<span class="gp"># </span>Path<span class="w"> </span>to<span class="w"> </span>log<span class="w"> </span>file.<span class="w"> </span>Comment<span class="w"> </span>out<span class="w"> </span>to<span class="w"> </span>disable<span class="w"> </span>logging<span class="w"> </span>to<span class="w"> </span>file<span class="w"> </span><span class="o">(</span>log<span class="w"> </span>to<span class="w"> </span>stdio<span class="w"> </span>instead<span class="o">)</span>.
<span class="go">log-file = leaps-gateway.log</span>
</pre></div>
</div>
</li>
<li><p>LEAPS Server host</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp"># </span>Default:<span class="w"> </span>localhost
<span class="go">leaps-server-host = 192.168.1.1 # Your Computer's IP Address</span>

<span class="gp"># </span>LEAPS<span class="w"> </span>Server<span class="w"> </span>port
<span class="gp"># </span>Default:<span class="w"> </span><span class="m">7777</span>
<span class="go">leaps-server-port = 7777</span>
</pre></div>
</div>
</li>
<li><p>UWBS USB Device VID/PID</p>
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
<li><p>UWBS device configurations</p>
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
<h2>Troubleshooting</h2>
<ul class="simple">
<li><p>Use the following command <code class="docutils literal notranslate"><span class="pre">sudo</span> <span class="pre">docker</span> <span class="pre">restart</span> <span class="pre">leaps_gateway</span></code> to restart LEAPS Gateway.</p></li>
<li><p>On windows, repeat the USB/IP attach WSL 2 to connect the USB device. (<code class="docutils literal notranslate"><span class="pre">usbipd</span> <span class="pre">wsl</span> <span class="pre">attach</span> <span class="pre">--busid</span> <span class="pre">&lt;busid&gt;</span></code>)</p></li>
</ul>
</div>
</div>


           </div>
