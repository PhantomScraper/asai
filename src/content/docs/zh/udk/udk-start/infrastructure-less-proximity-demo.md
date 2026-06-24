---
title: "无基础设施的邻近性演示"
lang: zh
slug: "udk/udk-start/infrastructure-less-proximity-demo"
section: "udk"
sourceUrl: "https://docs.leapslabs.com/zh-cn/udk/udk-start/infrastructure-less-proximity-demo/"
order: 108
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="infrastructure-less-proximity-demo">
<span id="anchor-ilp"></span><h1>无基础设施的邻近性演示</h1>
<a class="reference internal image-reference" href="../../../_images/infrastructure-less_proximity_demo.png"><img alt="../../../_images/infrastructure-less_proximity_demo.png" class="align-right" src="/docs-assets/zh-cn/_images/infrastructure-less_proximity_demo.png" style="width: 180.0px; height: 204.9px;"></a>
<p><strong>准备设置</strong></p>
<ol class="arabic simple">
<li><p><a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> 应用程序已安装。</p></li>
<li><p>至少两个 LC14 或 LC13 设备。</p></li>
<li><p>用于为设备供电的电池或USB-C电缆。</p></li>
<li><p><em>可选：电脑上安装的Putty,Teraterm, minicom或你最喜欢的终端应用程序</em></p></li>
</ol>
<p><strong>设置时间:</strong> 少于 2 分钟</p>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-0" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-0">
快速入门</label><div class="sd-tab-content docutils">
<p><strong>概览</strong></p>
<p>此演示基于 <span class="red-text">双向测距 (TWR)</span> 测量技术，展示了无基础设施的节点间近距离检测。 当节点非常接近时，每个节点都会触发警报。 警报使用 LED, 触觉马达或蜂鸣器，阈值可配置。</p>
<p><em>典型应用</em>:避免碰撞, 社会距离, 蜂群协调。</p>
<p><strong>设置说明</strong></p>
<ol class="arabic simple">
<li><p>启动 <span class="red-text">ON</span> 设备。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>这些设备将作为独立标签运行，使用Bluetooth发现周围的设备，并使用 UWB 测量与被发现设备的距离。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="2">
<li><p>使用 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> 中的演示选择器进行配置:</p></li>
</ol>
<blockquote>
<div><p>2.1。 打开LEAPS Manager，从主页面选择 <span class="red-text">演示选择器</span>。</p>
<p>2.2。 选择 <span class="red-text">无基础架构的近似性</span>。</p>
<p>2.3. 通过Bluetooth发现的设备列表会出现在列表中. 如果需要，向下滑动以更新列表。</p>
<p>2.4。 选择用于演示的设备。 上方的 <span class="red-text">nodes</span> 表示演示所需的设备数量。</p>
<p>2.5. 按下 <span class="red-text">SAVE</span> 键，将设备配置为 LEAPS RTLS 模式, Tag-Mesh 网络配置文件。</p>
<p>2.6. 请目测设备启动时 <span class="red-text">RED LED</span> 是否闪烁。</p>
<img alt="../../../_images/infrastructure-less-proximity-demo.gif" class="align-center" src="/docs-assets/zh-cn/_images/infrastructure-less-proximity-demo.gif">
</div></blockquote>
<ol class="arabic simple" start="3">
<li><p>设备配置为 <a class="reference internal" href="#anchor-ilp"><span class="std std-ref">无基础设施的邻近性演示</span></a>。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>默认情况下，当设备之间的距离在 2.5 米以内时，警报就会启动（由红色 LED 和蜂鸣器指示）。 警报的强度会随着设备的靠近而增加。</p></li>
<li><p>初始时，设备会发出低强度的蜂鸣声，并闪烁红色 LED 灯。 你可以使用上（<a class="reference internal" href="/docs/zh/udk/udk-start/device-hw-interfaces#uihwinterfaces"><span class="std std-ref">Button B</span></a>）和下（<a class="reference internal" href="/docs/zh/udk/udk-start/device-hw-interfaces#uihwinterfaces"><span class="std std-ref">Button A</span></a>）键来调整哔哔声的音量，振动也会启用。</p></li>
<li><p>在下面的演示中，设备有两个接近阈值：第一个阈值设置在 0.2 米，第二个设置在 0.5 米。</p></li>
</ul>
<img alt="../../../_images/infrastructure-less-proximity-demo-01.gif" class="align-center" src="/docs-assets/zh-cn/_images/infrastructure-less-proximity-demo-01.gif">
</div></blockquote>
<p>请参阅 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a>，了解如何使用应用程序来配置和可视化节点和网络的更多细节。</p>
</div>
<input id="sd-tab-item-1" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-1">
高级</label><div class="sd-tab-content docutils">
<p><strong>高级设置</strong></p>
<p>准备好进行高级设置！我们将利用终端的强大功能，帮助你像专业人士一样配置你的设备。 只需按照以下步骤，你就能完成所有设置。</p>
<ol class="arabic simple">
<li><p>使用 USB-C 数据线将设备的 <a class="reference internal" href="/docs/zh/udk/udk-start/device-hw-interfaces#hardware-interface"><span class="std std-ref">USB-C Data Port 1</span></a> 或 <a class="reference internal" href="/docs/zh/udk/udk-start/device-hw-interfaces#hardware-interface"><span class="std std-ref">USB-C Data Port 2</span></a> 连接到 PC。</p></li>
</ol>
<blockquote>
<div><img alt="../../../_images/leaps-connect-usb-port1.gif" class="align-center" src="/docs-assets/zh-cn/_images/leaps-connect-usb-port1.gif">
</div></blockquote>
<ol class="arabic simple" start="2">
<li><p>使用你想要的终端应用程序，如 Putty, Teraterm, Minicom 或你喜欢的终端应用程序，连接到串行端口. 我们需要将波特率设置为 <span class="red-text">115200</span>。</p></li>
</ol>
<blockquote>
<div><p>例如在 Ubuntu (Linux) 上使用 Minicom:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">minicom</span> <span class="o">-</span><span class="n">b</span> <span class="mi">115200</span> <span class="o">-</span><span class="n">D</span> <span class="o">/</span><span class="n">dev</span><span class="o">/</span><span class="n">ttyACM0</span>
</pre></div>
</div>
</div></blockquote>
<ol class="arabic simple" start="3">
<li><p>在 shell 控制台按下 <span class="red-text">双输入</span> 访问命令行控制系统</p></li>
</ol>
<blockquote>
<div><p>例如，在 Ubuntu (Linux) 上打开 <span class="red-text">/dev/ttyACM0</span> 并按下 <span class="red-text">双击回车键</span>:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>minicom -b 115200 -D /dev/ttyACM0

  Welcome to minicom 2.7.1

  OPTIONS: I18n
  Compiled on Dec 23 2019, 02:06:26.
  Port /dev/ttyACM0, 16:02:57

  Press CTRL-A Z for help on special keys



  Low Energy Accurate Positioning System

  FOR DEMO PURPOSE ONLY, NOT FOR SALE.

  Copyright :  2016-2023 LEAPS
  License   :  Please visit https://www.leapslabs.com/leaps-rtls-license
  Compiled  :  Jan  6 2024 09:38:07 (v0.15.0-ab84fb)

  Help      :  ? or help

  leaps&gt;
</pre></div>
</div>
</div></blockquote>
<ol class="arabic simple" start="4">
<li><p>按以下步骤配置每个设备：</p></li>
</ol>
<blockquote>
<div><ol class="loweralpha simple">
<li><p>将设备重置为默认设置，运行 <span class="red-text">frst</span> 命令. (可选)</p></li>
</ol>
<blockquote>
<div><div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ leaps&gt; frst
frst ok
</pre></div>
</div>
</div></blockquote>
<img alt="../../../_images/reset-command.gif" class="align-center" src="/docs-assets/zh-cn/_images/reset-command.gif">
<p><em>(监控并等待设备重置成功. 然后按双击回车键，进入命令行控制系统.)</em></p>
<ol class="loweralpha simple" start="2">
<li><p>使用 <span class="red-text">nps 4</span> 命令为每个设备配置 <span class="red-text">配置文件4（支持标签网状近程）.</span></p></li>
</ol>
<blockquote>
<div><div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ leaps&gt; nps 4
nps: ok
</pre></div>
</div>
</div></blockquote>
<ol class="loweralpha simple" start="3">
<li><p>使用 <span class="red-text">nis</span> 命令来配置网络中的所有设备。</p></li>
</ol>
<blockquote>
<div><div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ leaps&gt; nis 0x1234
nis: ok
</pre></div>
</div>
</div></blockquote>
<ol class="loweralpha simple" start="4">
<li><p>使用 <span class="red-text">nmt</span> 命令更新标签模式。</p></li>
</ol>
<blockquote>
<div><div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ leaps&gt; nmt
</pre></div>
</div>
</div></blockquote>
<p><em>(然后监控并等待设备配置成功. 然后按下双回车键，再次进入命令行控制系统. ）</em></p>
<ol class="loweralpha simple" start="5">
<li><p>使用 <span class="red-text">si</span> 命令来验证模式, 配置文件和网络等配置。</p></li>
</ol>
<blockquote>
<div><div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">leaps</span><span class="o">&gt;</span> <span class="n">si</span>
<span class="p">[</span><span class="mf">000028.754</span> <span class="n">INF</span><span class="p">]</span> <span class="n">release</span><span class="p">:</span> <span class="n">LEAPS</span> <span class="n">RTLS</span> <span class="n">v0</span><span class="mf">.15.0</span><span class="o">-</span><span class="n">ab84fb</span>
<span class="p">[</span><span class="mf">000028.754</span> <span class="n">INF</span><span class="p">]</span> <span class="n">sys</span><span class="p">:</span> <span class="n">main</span> <span class="n">main_ver</span><span class="o">=</span><span class="n">x02000001</span> <span class="n">cfg_ver</span><span class="o">=</span><span class="n">x01040000</span> <span class="n">batt</span><span class="o">=</span><span class="n">none</span> <span class="n">board</span><span class="o">=</span><span class="n">LC14_B</span>
<span class="p">[</span><span class="mf">000028.754</span> <span class="n">INF</span><span class="p">]</span> <span class="n">uwb</span><span class="p">:</span> <span class="n">ch9</span> <span class="n">prf64</span> <span class="n">plen128</span> <span class="n">pac8</span> <span class="n">txcode9</span> <span class="n">rxcode9</span> <span class="n">baud6800</span> <span class="n">phrmodeext</span> <span class="n">phrratestd</span> <span class="n">sfdtypeieee4a</span> <span class="n">sfdto10</span>
<span class="p">[</span><span class="mf">000028.754</span> <span class="n">INF</span><span class="p">]</span> <span class="n">uwb</span><span class="p">:</span> <span class="n">tx_pwr</span><span class="o">=</span><span class="n">x34</span><span class="o">/</span><span class="n">xC6C6C6C6</span> <span class="n">sts</span><span class="p">:</span><span class="n">shr</span><span class="p">:</span><span class="n">phr</span><span class="p">:</span><span class="n">data</span><span class="o">=</span><span class="mf">22.6</span><span class="p">:</span><span class="mf">22.6</span><span class="p">:</span><span class="mf">22.6</span><span class="p">:</span><span class="mf">22.6</span><span class="p">[</span><span class="n">dB</span><span class="p">]</span> <span class="n">cpl</span><span class="o">=</span><span class="n">FCC</span><span class="o">/</span><span class="n">ETSI</span> <span class="n">pgcnt</span><span class="o">=</span><span class="mi">236</span> <span class="n">temp</span><span class="o">=</span><span class="mi">5</span>
<span class="p">[</span><span class="mf">000028.755</span> <span class="n">INF</span><span class="p">]</span> <span class="n">uwb</span><span class="p">:</span> <span class="n">lna</span><span class="o">=</span><span class="mi">1</span> <span class="n">pa</span><span class="o">=</span><span class="mi">0</span> <span class="n">rf1</span><span class="o">=</span><span class="mi">1</span> <span class="n">rf2</span><span class="o">=</span><span class="mi">0</span> <span class="n">xtaltrim</span><span class="o">=</span><span class="mi">32</span> <span class="n">tx_delay</span><span class="o">=</span><span class="mi">16431</span> <span class="n">rx_delay</span><span class="o">=</span><span class="mi">16431</span>
<span class="p">[</span><span class="mf">000028.755</span> <span class="n">INF</span><span class="p">]</span> <span class="n">uwb</span><span class="p">:</span> <span class="n">panid</span><span class="o">=</span><span class="n">x1234</span> <span class="n">addr</span><span class="o">=</span><span class="n">xDECAED5BC8B1468D</span>
<span class="p">[</span><span class="mf">000028.758</span> <span class="n">INF</span><span class="p">]</span> <span class="n">mode</span><span class="p">:</span> <span class="n">tn</span> <span class="p">(</span><span class="n">act</span><span class="p">,</span><span class="n">twr</span><span class="p">,</span><span class="n">np</span><span class="p">,</span><span class="n">le</span><span class="p">)</span>
<span class="p">[</span><span class="mf">000028.774</span> <span class="n">INF</span><span class="p">]</span> <span class="n">uwbmac</span><span class="p">:</span> <span class="n">connected</span> <span class="n">prof</span><span class="o">=</span><span class="mi">4</span> <span class="p">(</span><span class="n">manual</span><span class="p">)</span>
<span class="p">[</span><span class="mf">000028.774</span> <span class="n">INF</span><span class="p">]</span> <span class="n">uwbmac</span><span class="p">:</span> <span class="n">bh</span> <span class="n">disconnected</span>
<span class="p">[</span><span class="mf">000028.774</span> <span class="n">INF</span><span class="p">]</span> <span class="n">cfg</span><span class="p">:</span> <span class="n">sync</span><span class="o">=</span><span class="mi">0</span> <span class="n">fwup</span><span class="o">=</span><span class="mi">1</span> <span class="n">ble</span><span class="o">=</span><span class="mi">1</span> <span class="n">leds</span><span class="o">=</span><span class="mi">1</span> <span class="n">le</span><span class="o">=</span><span class="mi">1</span> <span class="n">lp</span><span class="o">=</span><span class="mi">0</span> <span class="n">uab</span><span class="o">=</span><span class="mi">1</span> <span class="n">stat_det</span><span class="o">=</span><span class="mi">1</span> <span class="p">(</span><span class="n">sens</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span> <span class="n">mode</span><span class="o">=</span><span class="mi">0</span> <span class="n">upd_rate_norm</span><span class="o">=</span><span class="mi">1</span> <span class="n">upd_D</span>
<span class="p">[</span><span class="mf">000028.802</span> <span class="n">INF</span><span class="p">]</span> <span class="n">enc</span><span class="p">:</span> <span class="n">off</span>
<span class="p">[</span><span class="mf">000028.802</span> <span class="n">INF</span><span class="p">]</span> <span class="n">ble</span><span class="p">:</span> <span class="n">addr</span><span class="o">=</span><span class="n">F3</span><span class="p">:</span><span class="n">D9</span><span class="p">:</span><span class="mi">66</span><span class="p">:</span><span class="mi">75</span><span class="p">:</span><span class="mi">93</span><span class="p">:</span><span class="n">EB</span>
<span class="n">leaps</span><span class="o">&gt;</span>
</pre></div>
</div>
</div></blockquote>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">mode:</span> <span class="pre">tn</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">panid=x1234</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prof=4</span></code></p></li>
</ul>
<ol class="loweralpha simple" start="6">
<li><p>请目测设备启动时 <span class="red-text">RED LED</span> 是否闪烁。</p></li>
</ol>
</div></blockquote>
<div class="admonition note">
<p class="admonition-title">注解</p>
<p>在这个例子中，我们将配置 <strong>2 个标签</strong>。</p>
</div>
<ol class="arabic simple" start="5">
<li><p>配置设备后，它会通过 BLE 扫描所有设备。 如果设备在允许的距离内，它会自动重新激活 UWB 并测量彼此的距离。</p></li>
</ol>
<blockquote>
<div><p>使用 <span class="red-text">ln</span> 命令来显示所有设备. 这可以用于所有 UDK 设备。</p>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-3" name="sd-tab-set-1" type="radio">
<label class="sd-tab-label" for="sd-tab-item-3">
标签 1</label><div class="sd-tab-content docutils">
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ leaps&gt; ln
[000005.713 INF] TN: cnt=2 size=100
[000005.713 INF]   0) id=468D dist=0.40,xDD
[000005.713 INF]   1) id=4F2E dist=0.00,xBD
[000005.713 INF]
</pre></div>
</div>
</div>
<input id="sd-tab-item-4" name="sd-tab-set-1" type="radio">
<label class="sd-tab-label" for="sd-tab-item-4">
标签 2</label><div class="sd-tab-content docutils">
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ leaps&gt; ln
[000033.319 INF] TN: cnt=2 size=100
[000033.319 INF]   0) id=468D dist=0.00,x00
[000033.320 INF]   1) id=4F2E dist=0.44,x66
[000033.320 INF]
</pre></div>
</div>
</div>
</div>
</div></blockquote>
<ol class="arabic simple" start="6">
<li><p>在 <a class="reference internal" href="#anchor-ilp"><span class="std std-ref">无基础设施的邻近性演示</span></a> 中。</p></li>
</ol>
<blockquote>
<div><ul>
<li><p>默认情况下，当设备之间的距离在 2.5 米以内时，警报就会启动（由红色 LED 和蜂鸣器指示）。 警报的强度会随着设备的靠近而增加。</p></li>
<li><p>初始时，设备会发出低强度的蜂鸣声，并闪烁红色 LED 灯。 你可以使用上（<a class="reference internal" href="/docs/zh/udk/udk-start/device-hw-interfaces#uihwinterfaces"><span class="std std-ref">Button B</span></a>）和下（<a class="reference internal" href="/docs/zh/udk/udk-start/device-hw-interfaces#uihwinterfaces"><span class="std std-ref">Button A</span></a>）键来调整哔哔声的音量，振动也会启用。</p></li>
<li><p>用户可以通过两个命令来查看和配置这个距离: <span class="red-text">dacg</span> 命令和 <span class="red-text">dacs</span> 命令。</p>
<p>例如，要查看和配置2个阈值0.2米和0.5米. 运行以下命令：</p>
<blockquote>
<div><ul class="simple">
<li><p>查看：</p></li>
</ul>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ leaps&gt; dacg
dacg: thold_1=200 thold_2=500 mincon=2 minnocon=2 opt=7
</pre></div>
</div>
<ul class="simple">
<li><p>配置:</p></li>
</ul>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ leaps&gt; dacs 200 500 2 2 7
dacs: ok
</pre></div>
</div>
</div></blockquote>
<p>在下面的 GIF 图片中，设备配置的阈值1为0.2米，阈值2为0.5米。</p>
<img alt="../../../_images/infrastructure-less-proximity-demo-01.gif" class="align-center" src="/docs-assets/zh-cn/_images/infrastructure-less-proximity-demo-01.gif">
</li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="7">
<li><p>配置完成后，你可以打开标签的shell控制台，使用 <span class="red-text">les</span> 命令查看标签的位置。</p></li>
</ol>
<blockquote>
<div><div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ leaps&gt; les
  leaps&gt; POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.54
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.57
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.58
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.59
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.51
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.47
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.43
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.40
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.35
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.32
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.31
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.29
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.27
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.22
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.19
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.16
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.14
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.12
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.09
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.08
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.05
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.09
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.11
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.13
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.15
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.17
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.19
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.21
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.23
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.42
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.51
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.56
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.60
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.62
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.64
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.67
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.69
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.71
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.73
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.73
</pre></div>
</div>
</div></blockquote>
<p>现在系统已经成功设置和配置。 请尽情使用！</p>
</div>
<input id="sd-tab-item-2" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-2">
故障排除</label><div class="sd-tab-content docutils">
<ol class="arabic">
<li><p>当低功耗Bluetooth (BLE) 和 LED 同时熄灭时，用户可能会错误地认为电路板无法运作。 在这种情况下，用户唯一的办法就是启动出厂重置（<a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/shell-api/sys#frst"><span class="std std-ref">frst</span></a>）命令。</p></li>
<li><p>以下是一些修复与安装过程有关的问题的提示。</p>
<ul class="simple">
<li><p>请检查版本. 我们建议您使用最新的官方版本。</p></li>
<li><p>当你不知道设备的当前状态时，请使用 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> 演示选择器中的 <span class="red-text">将设备重置为默认值</span> 功能. 请参考下面的 GIF 图片。</p></li>
</ul>
<img alt="../../../_images/reset-devices-to-defaul-x2.gif" class="align-center" src="/docs-assets/zh-cn/_images/reset-devices-to-defaul-x2.gif">
</li>
</ol>
</div>
</div>
<div class="admonition caution">
<p class="admonition-title">小心</p>
<p><strong>Related to Profile 4 (support Tag Mesh Proximity)</strong></p>
<ul class="simple">
<li><p>当设备处于锚点或启动器模式时，用户不得切换到配置文件4（支持标签网格接近）。</p></li>
<li><p>配置的更新速率值应限制在x1。 x10以内。</p></li>
</ul>
</div>
<div class="admonition note">
<p class="admonition-title">注解</p>
<ul class="simple">
<li><p>距离阈值可通过API进行配置。</p></li>
<li><p>如果您对我们的产品有任何意见或问题，请访问我们的 <a class="reference external" href="https://forum.leapslabs.com">LEAPS 论坛</a>。</p></li>
<li><p>有关已知限制和问题列表的详情，请参阅 <a class="reference internal" href="/docs/zh/udk/release#udk-releases"><span class="std std-ref">发布</span></a> 部分。</p></li>
</ul>
</div>
</div>


           </div>
