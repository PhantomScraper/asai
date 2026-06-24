---
title: "上行链路 TDoA RTLS 演示"
lang: zh
slug: "udk/udk-start/uplink-tdoa-rtls-demo"
section: "udk"
sourceUrl: "https://docs.leapslabs.com/zh-cn/udk/udk-start/uplink-tdoa-rtls-demo/"
order: 43
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="uplink-tdoa-rtls-demo">
<span id="id1"></span><h1>上行链路 TDoA RTLS 演示</h1>
<a class="reference internal image-reference" href="../../../_images/uplink_tdoa_rtls_demo.png"><img alt="../../../_images/uplink_tdoa_rtls_demo.png" class="align-right" src="/docs-assets/zh-cn/_images/uplink_tdoa_rtls_demo.png" style="width: 252.00000000000003px; height: 278.04px;"></a>
<p><strong>准备设置</strong></p>
<ol class="arabic simple">
<li><p><a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> 应用程序已安装。</p></li>
<li><p>一台Raspberry Pi 3B或更新版本，或一台用于安装数据服务器和网络应用程序的 PC。</p></li>
<li><p>至少五台LC14设备。</p></li>
<li><p>用于为设备供电的电池或USB-C电缆。</p></li>
<li><p><em>推荐：夹具或带相机支架的三脚架，用于安装主播设备</em></p></li>
<li><p><em>可选： Putty, Teraterm, minicom 或计算机上安装的您最喜欢的终端应用程序</em></p></li>
</ol>
<p><strong>设置时间：</strong> 少于 5 分钟</p>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-0" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-0">
快速入门</label><div class="sd-tab-content docutils">
<p><strong>概览</strong></p>
<p>该设置展示了使用 <span class="red-text">上行链路到达时间差 (UL-TDoA)</span> 技术对标签进行高精度的实时追踪。</p>
<p><strong>典型应用</strong>：资产和人员跟踪。</p>
<p><strong>设置说明</strong></p>
<ol class="arabic simple">
<li><p>Power <span class="red-text">ON</span> 设备。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>设备静态安装的设备将作为锚点，为标签提供位置信息。</p></li>
<li><p>移动设备将作为上行链路TDoA测量模式下配置的标签。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="2">
<li><p>使用 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> 中的演示选择器进行配置:</p></li>
</ol>
<blockquote>
<div><p>2.1。 打开LEAPS Manager，从主页中选择 <span class="red-text">演示选择器</span>。</p>
<p>选择 <span class="red-text">上行链路TDoA RTLS</span>。</p>
<p>2.3。 通过Bluetooth发现的设备列表将显示在列表中。 如果需要，向下滑动以更新列表。</p>
<p>2.4. 选择用于演示的设备. 顶部的 <span class="red-text">anchors</span> 和 <span class="red-text">tags</span> 表示演示所需的设备数量。</p>
<p>2.5. 按下 <span class="red-text">SAVE</span> 将设备配置为 LEAPS RTLS 模式，联网 <span class="red-text">配置文件 5 (支持 UL-TDoA)</span>。</p>
<p>2.6。 弹出的锚点配置窗口会提供锚点位置的配置选项，根据需要选择 <span class="red-text">手册</span> 或 <span class="red-text">保持当前位置</span>，然后按下 <span class="red-text">OK</span>。</p>
<ul class="simple">
<li><p><em>自动定位目前不适用于配置文件 5.</em>。</p></li>
</ul>
<p>2.7. 请目测设备启动时 <span class="red-text">RED LED</span> 是否闪烁。</p>
</div></blockquote>
<ol class="arabic simple" start="3">
<li><p>当设备配置成功后，LEAPS演示网络窗口会出现已配置节点的列表</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p><em>推荐: 使用 使用警报功能来识别设备，并将其移动到正确的物理位置</em></p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="4">
<li><p>打开位于顶端下拉菜单的 <span class="red-text">Grid</span> 网格，用于显示设备及其位置。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>请参阅 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a>，了解如何使用应用程序来配置和可视化节点和网络。</p></li>
</ul>
</div></blockquote>
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
<li><p>使用你想要的终端应用程序，例如 Putty, Teraterm, Minicom 或你最喜欢的终端应用程序，连接到串行端口. 我们需要将波特率设置为 <span class="red-text">115200</span>。</p></li>
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

  Copyright :  2016-2024 LEAPS
  License   :  Please visit https://www.leapslabs.com/leaps-rtls-licee
  Compiled  :  Nov  4 2024 12:30:29 (v0.16.4-a916a6

  Help      :  ? or help

  leaps&gt;
</pre></div>
</div>
</div></blockquote>
<ol class="arabic simple" start="4">
<li><p>为每个设备进行配置，请执行以下步骤:</p></li>
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
<li><p>使用 <span class="red-text">nps 5</span> 命令，为每个设备配置 <span class="red-text">配置文件5 (支持 UL-TDoA)</span>。</p></li>
</ol>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ leaps&gt; nps 5
nps: ok
</pre></div>
</div>
<ol class="loweralpha simple" start="3">
<li><p>使用 <span class="red-text">nis</span> 命令来配置网络中的所有设备。</p></li>
</ol>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ leaps&gt; nis 0x1234
nis: ok
</pre></div>
</div>
<ul class="simple">
<li><p><strong>然后，需要重置设备以更新配置</strong>. 使用 <span class="red-text">reset</span> 命令重置设备。</p></li>
</ul>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ leaps&gt; reset
reset ok
</pre></div>
</div>
</div></blockquote>
<div class="admonition note">
<p class="admonition-title">注解</p>
<p>在这个例子里，我们将配置一个**锚点和启用启动器**，<strong>3锚点</strong>，以及**一个标签**。</p>
</div>
<ol class="arabic simple" start="5">
<li><p>为每个锚点和标签配置模式。</p></li>
</ol>
<blockquote>
<div><ul>
<li><p>要配置 <span class="red-text">使用启用启动器锚定</span>，请使用 <span class="red-text">nmi</span> 命令配置设备。</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ leaps&gt; nmi
</pre></div>
</div>
<p><em>然后，设备将重置，要再次进入命令行控制系统，请按双回车键。</em></p>
</li>
<li><p>要配置 <span class="red-text">3 锚点</span>，请使用 <span class="red-text">nma</span> 命令将 3 台设备配置为锚点模式，但不要启用启动器。</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ leaps&gt; nma
</pre></div>
</div>
<p><em>然后，设备将重置，要再次进入命令行控制系统，请按双回车键。</em></p>
</li>
<li><p>要配置 <span class="red-text">a tag</span>，使用 <span class="red-text">nmt</span> 命令将一个设备配置为标签模式。</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ leaps&gt; nmt
</pre></div>
</div>
<p><em>然后，设备将重置，要再次进入命令行控制系统，请按双回车键。</em></p>
</li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="6">
<li><p>为其中一个锚点配置时钟基准。</p></li>
</ol>
<blockquote>
<div><ul>
<li><p>至少配置了一个锚点。</p></li>
<li><p>要配置 <span class="red-text">带有启用时钟参考的锚点</span>，请使用 <span class="red-text">acs cr</span> 命令配置设备。</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ leaps&gt; acs cr 1
</pre></div>
</div>
</li>
<li><p><strong>然后，有必要重置设备.需要重置设备以更新配置</strong>.使用 <span class="red-text">reset</span> 命令重置设备。</p></li>
</ul>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ leaps&gt; reset
reset ok
</pre></div>
</div>
</div></blockquote>
<ol class="arabic simple" start="7">
<li><p>配置每个锚点的实际位置。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>使用 <span class="red-text">pg</span> 命令获取位置，使用 <span class="red-text">ps</span> 命令设置每个锚点的位置。</p></li>
<li><p>在这个例子中，我们将配置 4 个锚点，每个锚点相距 3 米，呈正方形排列：</p></li>
</ul>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-3" name="sd-tab-set-1" type="radio">
<label class="sd-tab-label" for="sd-tab-item-3">
锚点 1 (启用启动器)</label><div class="sd-tab-content docutils">
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">leaps</span><span class="o">&gt;</span> <span class="n">ps</span> <span class="mi">3000</span> <span class="mi">3000</span> <span class="mi">0</span>
<span class="n">ps</span><span class="p">:</span> <span class="n">ok</span>
<span class="n">leaps</span><span class="o">&gt;</span> <span class="n">pg</span>
<span class="n">pg</span><span class="p">:</span> <span class="n">x</span><span class="p">:</span><span class="mi">5000</span> <span class="n">y</span><span class="p">:</span><span class="mi">5000</span> <span class="n">z</span><span class="p">:</span><span class="mi">0</span> <span class="n">qf</span><span class="p">:</span><span class="mi">100</span>
<span class="n">leaps</span><span class="o">&gt;</span>
</pre></div>
</div>
</div>
<input id="sd-tab-item-4" name="sd-tab-set-1" type="radio">
<label class="sd-tab-label" for="sd-tab-item-4">
锚点 2</label><div class="sd-tab-content docutils">
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">leaps</span><span class="o">&gt;</span> <span class="n">ps</span> <span class="mi">0</span> <span class="mi">0</span> <span class="mi">0</span>
<span class="n">ps</span><span class="p">:</span> <span class="n">ok</span>
<span class="n">leaps</span><span class="o">&gt;</span> <span class="n">pg</span>
<span class="n">pg</span><span class="p">:</span> <span class="n">x</span><span class="p">:</span><span class="mi">0</span> <span class="n">y</span><span class="p">:</span><span class="mi">0</span> <span class="n">z</span><span class="p">:</span><span class="mi">0</span> <span class="n">qf</span><span class="p">:</span><span class="mi">100</span>
<span class="n">leaps</span><span class="o">&gt;</span>
</pre></div>
</div>
</div>
<input id="sd-tab-item-5" name="sd-tab-set-1" type="radio">
<label class="sd-tab-label" for="sd-tab-item-5">
锚点 3</label><div class="sd-tab-content docutils">
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">leaps</span><span class="o">&gt;</span> <span class="n">ps</span> <span class="mi">3000</span> <span class="mi">0</span> <span class="mi">0</span>
<span class="n">ps</span><span class="p">:</span> <span class="n">ok</span>
<span class="n">leaps</span><span class="o">&gt;</span> <span class="n">pg</span>
<span class="n">pg</span><span class="p">:</span> <span class="n">x</span><span class="p">:</span><span class="mi">3000</span> <span class="n">y</span><span class="p">:</span><span class="mi">0</span> <span class="n">z</span><span class="p">:</span><span class="mi">0</span> <span class="n">qf</span><span class="p">:</span><span class="mi">100</span>
<span class="n">leaps</span><span class="o">&gt;</span>
</pre></div>
</div>
</div>
<input id="sd-tab-item-6" name="sd-tab-set-1" type="radio">
<label class="sd-tab-label" for="sd-tab-item-6">
锚点 4</label><div class="sd-tab-content docutils">
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">leaps</span><span class="o">&gt;</span> <span class="n">ps</span> <span class="mi">0</span> <span class="mi">3000</span> <span class="mi">0</span>
<span class="n">ps</span><span class="p">:</span> <span class="n">ok</span>
<span class="n">leaps</span><span class="o">&gt;</span> <span class="n">pg</span>
<span class="n">pg</span><span class="p">:</span> <span class="n">x</span><span class="p">:</span><span class="mi">0</span> <span class="n">y</span><span class="p">:</span><span class="mi">3000</span> <span class="n">z</span><span class="p">:</span><span class="mi">0</span> <span class="n">qf</span><span class="p">:</span><span class="mi">100</span>
<span class="n">leaps</span><span class="o">&gt;</span>
</pre></div>
</div>
</div>
</div>
<ul class="simple">
<li><p>成功配置锚点后，将其移动到相距 1 米的正确物理位置。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="8">
<li><p>每个标签的配置允许使用 <span class="red-text">UL-TDoA</span> 技术进行测量。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>要进行配置，请对标签使用 <span class="red-text">tcs mode 1</span> 命令。</p></li>
</ul>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ leaps&gt; tcs mode 1
tcs: ok
</pre></div>
</div>
<ul class="simple">
<li><p><strong>然后，需要重置设备以更新配置</strong>. 使用 <span class="red-text">reset</span> 命令重置设备。</p></li>
</ul>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ leaps&gt; reset
reset ok
</pre></div>
</div>
</div></blockquote>
<ol class="arabic simple" start="9">
<li><p>默认情况下 <span class="red-text">正常更新率</span> 为 0.1s/ 10Hz，<span class="red-text">固定更新率</span> 为 5.0s/ 0.2Hz.要提高速度，请使用 <span class="red-text">urs</span> 命令。</p></li>
</ol>
<blockquote>
<div><p>例如，配置 <span class="red-text">正常更新率</span> 为 0.1s/ 10Hz，而 <span class="red-text">固定更新率</span> 为 0.1s/ 10Hz. 运行以下命令：</p>
<blockquote>
<div><div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ leaps&gt; urs 1 1
urs: ok
</pre></div>
</div>
</div></blockquote>
</div></blockquote>
<ol class="arabic simple" start="10">
<li><p>在步骤 5, 7 和 8 中，可以使用 <span class="red-text">si</span> 命令来验证模式, 配置文件和网络配置是否正确。 (可选)</p></li>
</ol>
<blockquote>
<div><p>例如在 4 个锚点和一个标签上：</p>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-7" name="sd-tab-set-2" type="radio">
<label class="sd-tab-label" for="sd-tab-item-7">
锚点 1 (启用启动器)</label><div class="sd-tab-content docutils">
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">mode:</span> <span class="pre">ani</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">panid=x1234</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prof=5</span></code></p></li>
</ul>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>leaps&gt; nps 5
nps: ok
leaps&gt; nis 0x1234
nis: ok
leaps&gt; nmi


Low Energy Accurate Positioning System

FOR DEMO PURPOSE ONLY, NOT FOR SALE.

Copyright :  2016-2024 LEAPS
License   :  Please visit https://www.leapslabs.com/leaps-rtls-licee
Compiled  :  Nov  4 2024 12:30:29 (v0.16.4-a916a6

Help      :  ? or help

leaps&gt;si
[000412.823 INF] release: LEAPS RTLS v0.16.4-a916a6
[000412.824 INF] sys: main main_ver=x02040001 cfg_ver=x01040000 batt=none board=LC14_B
[000412.824 INF] uwb: ch9 prf64 plen128 pac8 txcode9 rxcode9 baud6800 phrmodeext phrratestd sfdtypeieee4a sfdto129 stsmodeoff stslen64 pdoamodem0
[000412.825 INF] uwb: tx_pwr=x34/xD6D6D6D6 sts:shr:phr:data=24.2:24.2:24.2:24.2[dB] cpl=FCC/ETSI pgcnt=232 temp=25
[000412.826 INF] uwb: lna=1 pa=0 rf1=1 rf2=0 xtaltrim=37 tx_delay=16436 rx_delay=16436
[000412.827 INF] uwb: panid=x1234 addr=xDECAD674FD208EAA
[000412.828 INF] mode: ani (act,real)
[000412.851 INF] uwbmac: connected prof=5 (manual)
[000412.851 INF] uwbmac: bh disconnected
[000412.852 INF] cfg: sync=0 fwup=1 ble=1 leds=1 init=1 uab=1 bh=auto bh_stat=off cr=0 upd_rate_stat=30 label=ID8EAA
[000412.852 INF] enc: off
[000412.872 INF] ble: addr=F0:26:43:8B:52:4A
leaps&gt;
</pre></div>
</div>
</div>
<input id="sd-tab-item-8" name="sd-tab-set-2" type="radio">
<label class="sd-tab-label" for="sd-tab-item-8">
锚点 2</label><div class="sd-tab-content docutils">
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">mode:</span> <span class="pre">an</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">panid=x1234</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prof=5</span></code></p></li>
</ul>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>leaps&gt; nps 5
nps: ok
leaps&gt; nis 0x1234
nis: ok
leaps&gt; nma


Low Energy Accurate Positioning System

FOR DEMO PURPOSE ONLY, NOT FOR SALE.

Copyright :  2016-2024 LEAPS
License   :  Please visit https://www.leapslabs.com/leaps-rtls-licee
Compiled  :  Nov  4 2024 12:30:29 (v0.16.4-a916a6

Help      :  ? or help

leaps&gt;si
[000454.748 INF] release: LEAPS RTLS v0.16.4-a916a6
[000454.749 INF] sys: main main_ver=x02040001 cfg_ver=x01040000 batt=none board=LC14_B
[000454.749 INF] uwb: ch9 prf64 plen128 pac8 txcode9 rxcode9 baud6800 phrmodeext phrratestd sfdtypeieee4a sfdto129 stsmodeoff stslen64 pdoamodem0
[000454.750 INF] uwb: tx_pwr=x34/xCECECECE sts:shr:phr:data=23.4:23.4:23.4:23.4[dB] cpl=FCC/ETSI pgcnt=238 temp=25
[000454.751 INF] uwb: lna=1 pa=0 rf1=1 rf2=0 xtaltrim=32 tx_delay=16426 rx_delay=16426
[000454.752 INF] uwb: panid=x1234 addr=xDECA229121E05886
[000454.753 INF] mode: an (act,-)
[000454.766 INF] uwbmac: connected prof=5 (manual)
[000454.766 INF] uwbmac: bh disconnected
[000454.767 INF] cfg: sync=0 fwup=1 ble=1 leds=1 init=0 uab=1 bh=auto bh_stat=off cr=0 upd_rate_stat=30 label=ID5886
[000454.797 INF] enc: off
[000454.798 INF] ble: addr=FD:3F:4A:2F:BD:F0
leaps&gt;
</pre></div>
</div>
</div>
<input id="sd-tab-item-9" name="sd-tab-set-2" type="radio">
<label class="sd-tab-label" for="sd-tab-item-9">
锚点 3</label><div class="sd-tab-content docutils">
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">mode:</span> <span class="pre">an</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">panid=x1234</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prof=5</span></code></p></li>
</ul>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>leaps&gt; nps 5
nps: ok
leaps&gt; nis 0x1234
nis: ok
leaps&gt; nma


Low Energy Accurate Positioning System

FOR DEMO PURPOSE ONLY, NOT FOR SALE.

Copyright :  2016-2024 LEAPS
License   :  Please visit https://www.leapslabs.com/leaps-rtls-licee
Compiled  :  Nov  4 2024 12:30:29 (v0.16.4-a916a6

Help      :  ? or help

leaps&gt; si
[000496.390 INF] release: LEAPS RTLS v0.16.4-a916a6
[000496.390 INF] sys: main main_ver=x02040001 cfg_ver=x01040000 batt=none board=LC14_B
[000496.390 INF] uwb: ch9 prf64 plen128 pac8 txcode9 rxcode9 baud6800 phrmodeext phrratestd sfdtypeieee4a sfdto129 stsmodeoff stslen64 pdoamodem0
[000496.391 INF] uwb: tx_pwr=x34/xC6C6C6C6 sts:shr:phr:data=22.6:22.6:22.6:22.6[dB] cpl=FCC/ETSI pgcnt=236 temp=25
[000496.392 INF] uwb: lna=1 pa=0 rf1=1 rf2=0 xtaltrim=32 tx_delay=16431 rx_delay=16431
[000496.393 INF] uwb: panid=x1234 addr=xDECAED5BC8B1468D
[000496.394 INF] mode: an (act,-)
[000496.413 INF] uwbmac: connected prof=5 (manual)
[000496.414 INF] uwbmac: bh disconnected
[000496.414 INF] cfg: sync=0 fwup=1 ble=1 leds=1 init=0 uab=1 bh=auto bh_stat=off cr=0 upd_rate_stat=30 label=ID468D
[000496.438 INF] enc: off
[000496.439 INF] ble: addr=F3:D9:66:75:93:EB
leaps&gt;
</pre></div>
</div>
</div>
<input id="sd-tab-item-10" name="sd-tab-set-2" type="radio">
<label class="sd-tab-label" for="sd-tab-item-10">
锚点 4</label><div class="sd-tab-content docutils">
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">mode:</span> <span class="pre">an</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">panid=x1234</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prof=5</span></code></p></li>
</ul>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>leaps&gt; nps 5
nps: ok
leaps&gt; nis 0x1234
nis: ok
leaps&gt; nma


Low Energy Accurate Positioning System

FOR DEMO PURPOSE ONLY, NOT FOR SALE.

Copyright :  2016-2024 LEAPS
License   :  Please visit https://www.leapslabs.com/leaps-rtls-licee
Compiled  :  Nov  4 2024 12:30:29 (v0.16.4-a916a6

Help      :  ? or help

leaps&gt; si
[000535.583 INF] release: LEAPS RTLS v0.16.4-a916a6
[000535.583 INF] sys: main main_ver=x02040001 cfg_ver=x01040000 batt=none board=LC14_B
[000535.584 INF] uwb: ch9 prf64 plen128 pac8 txcode9 rxcode9 baud6800 phrmodeext phrratestd sfdtypeieee4a sfdto129 stsmodeoff stslen64 pdoamodem0
[000535.585 INF] uwb: tx_pwr=x34/xEEEEEEEE sts:shr:phr:data=26.5:26.5:26.5:26.5[dB] cpl=FCC/ETSI pgcnt=245 temp=25
[000535.586 INF] uwb: lna=1 pa=0 rf1=1 rf2=0 xtaltrim=32 tx_delay=16436 rx_delay=16436
[000535.587 INF] uwb: panid=x1234 addr=xDECA7A20DFE04F2E
[000535.588 INF] mode: an (act,-)
[000535.599 INF] uwbmac: connected prof=5 (manual)
[000535.599 INF] uwbmac: bh disconnected
[000535.632 INF] cfg: sync=0 fwup=1 ble=1 leds=1 init=0 uab=1 bh=auto bh_stat=off cr=0 upd_rate_stat=30 label=ID4F2E
[000535.632 INF] enc: off
[000535.633 INF] ble: addr=C8:D9:F3:F1:7D:CE
leaps&gt;
</pre></div>
</div>
</div>
<input id="sd-tab-item-11" name="sd-tab-set-2" type="radio">
<label class="sd-tab-label" for="sd-tab-item-11">
标签</label><div class="sd-tab-content docutils">
<ul class="simple">
<li><p>根据默认配置，设备将处于 <span class="red-text">TWR 模式</span>. 如果是其他模式，我们会使用 <span class="red-text">tcs mode 0</span> 命令。</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">mode:</span> <span class="pre">tn</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">panid=x1234</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prof=2</span></code></p></li>
</ul>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>leaps&gt; nps 2
nps: ok
leaps&gt; nis 0x1234
nis: ok
leaps&gt; nmt


Low Energy Accurate Positioning System

FOR DEMO PURPOSE ONLY, NOT FOR SALE.

Copyright :  2016-2024 LEAPS
License   :  Please visit https://www.leapslabs.com/leaps-rtls-licee
Compiled  :  Nov  4 2024 12:30:29 (v0.16.4-a916a6

Help      :  ? or help

leaps&gt; urs 1 1
urs: ok
leaps&gt; si
[000248.294 INF] release: LEAPS RTLS v0.16.4-a916a6
[000248.294 INF] sys: main main_ver=x02040001 cfg_ver=x01040000 batt=none board=LC13_B
[000248.294 INF] uwb: ch9 prf64 plen128 pac8 txcode9 rxcode9 baud6800 phrmodeext phrratestd sfdtypeieee4a sfdto129 stsmodeoff stslen64 pdoamodem0
[000248.295 INF] uwb: tx_pwr=x34/xCDCDCDCD sts:shr:phr:data=21.7:21.7:21.7:21.7[dB] cpl=FCC/ETSI pgcnt=234 temp=25
[000248.295 INF] uwb: lna=1 pa=0 rf1=1 rf2=1 xtaltrim=13 tx_delay=16443 rx_delay=16443
[000248.295 INF] uwb: panid=x1234 addr=xDECA2B16DD209705
[000248.299 INF] mode: tn (act,tdoa,np,le)
[000248.314 INF] uwbmac: disconnected prof=5 (manual)
[000248.314 INF] uwbmac: bh disconnected
[000248.314 INF] cfg: sync=0 fwup=1 ble=1 leds=1 le=1 lp=0 uab=1 stat_det=1 (sens=2) mode=1 upd_rate_norm=1 upd_rate_stat=1 label=ID9705
[000248.342 INF] enc: off
[000248.342 INF] ble: addr=E0:2C:84:68:AD:16
leaps&gt;
</pre></div>
</div>
</div>
</div>
</div></blockquote>
<ol class="arabic simple" start="11">
<li><p>要查看范围内连接到设备本身的锚点列表，请使用 <span class="red-text">la</span> 命令。 (可选)</p></li>
</ol>
<blockquote>
<div><p>例如在锚点 1 上（启用启动器）：</p>
<blockquote>
<div><div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">leaps</span><span class="o">&gt;</span> <span class="n">la</span>
<span class="p">[</span><span class="mf">000414.009</span> <span class="n">INF</span><span class="p">]</span> <span class="n">AN</span><span class="p">:</span> <span class="n">cnt</span><span class="o">=</span><span class="mi">4</span> <span class="n">seq</span><span class="o">=</span><span class="n">x03</span>
<span class="p">[</span><span class="mf">000414.009</span> <span class="n">INF</span><span class="p">]</span>     <span class="mi">0</span><span class="p">)</span> <span class="nb">id</span><span class="o">=</span><span class="mi">8</span><span class="n">EAA</span> <span class="n">seat</span><span class="o">=</span><span class="mi">0</span> <span class="n">clk_lvl</span><span class="o">=</span><span class="mi">0</span> <span class="n">seens</span><span class="o">=</span><span class="mi">0</span> <span class="n">rssi</span><span class="o">=-</span><span class="mi">127</span> <span class="n">cl</span><span class="o">=</span><span class="mi">00000039</span> <span class="n">nbr</span><span class="o">=</span><span class="mi">00000039</span> <span class="n">pos</span><span class="o">=</span><span class="mf">3.00</span><span class="p">:</span><span class="mf">3.00</span><span class="p">:</span><span class="mf">0.00</span>
<span class="p">[</span><span class="mf">000414.010</span> <span class="n">INF</span><span class="p">]</span>     <span class="mi">1</span><span class="p">)</span> <span class="nb">id</span><span class="o">=</span><span class="mi">4</span><span class="n">F2E</span> <span class="n">seat</span><span class="o">=</span><span class="mi">4</span> <span class="n">clk_lvl</span><span class="o">=</span><span class="mi">1</span> <span class="n">seens</span><span class="o">=</span><span class="mi">212</span> <span class="n">rssi</span><span class="o">=-</span><span class="mi">127</span> <span class="n">cl</span><span class="o">=</span><span class="mi">00000039</span> <span class="n">nbr</span><span class="o">=</span><span class="mi">00000000</span> <span class="n">pos</span><span class="o">=</span><span class="mf">0.00</span><span class="p">:</span><span class="mf">3.00</span><span class="p">:</span><span class="mf">0.00</span>
<span class="p">[</span><span class="mf">000414.011</span> <span class="n">INF</span><span class="p">]</span>     <span class="mi">2</span><span class="p">)</span> <span class="nb">id</span><span class="o">=</span><span class="mi">5886</span> <span class="n">seat</span><span class="o">=</span><span class="mi">5</span> <span class="n">clk_lvl</span><span class="o">=</span><span class="mi">1</span> <span class="n">seens</span><span class="o">=</span><span class="mi">178</span> <span class="n">rssi</span><span class="o">=-</span><span class="mi">127</span> <span class="n">cl</span><span class="o">=</span><span class="mi">00000039</span> <span class="n">nbr</span><span class="o">=</span><span class="mi">00000000</span> <span class="n">pos</span><span class="o">=</span><span class="mf">3.00</span><span class="p">:</span><span class="mf">0.00</span><span class="p">:</span><span class="mf">0.00</span>
<span class="p">[</span><span class="mf">000414.012</span> <span class="n">INF</span><span class="p">]</span>     <span class="mi">3</span><span class="p">)</span> <span class="nb">id</span><span class="o">=</span><span class="mi">468</span><span class="n">D</span> <span class="n">seat</span><span class="o">=</span><span class="mi">3</span> <span class="n">clk_lvl</span><span class="o">=</span><span class="mi">1</span> <span class="n">seens</span><span class="o">=</span><span class="mi">145</span> <span class="n">rssi</span><span class="o">=-</span><span class="mi">127</span> <span class="n">cl</span><span class="o">=</span><span class="mi">00000039</span> <span class="n">nbr</span><span class="o">=</span><span class="mi">00000000</span> <span class="n">pos</span><span class="o">=</span><span class="mf">0.00</span><span class="p">:</span><span class="mf">0.00</span><span class="p">:</span><span class="mf">0.00</span>
<span class="p">[</span><span class="mf">000414.012</span> <span class="n">INF</span><span class="p">]</span>
<span class="n">leaps</span><span class="o">&gt;</span>
</pre></div>
</div>
</div></blockquote>
</div></blockquote>
<ol class="arabic" start="12">
<li><p>完成所有配置后. 我们可以使用 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> 来可视化设备及其位置。</p>
<a class="reference internal image-reference" href="../../../_images/twrrtlsanddatatelemetrydemo-advanced-01.jpeg"><img alt="../../../_images/twrrtlsanddatatelemetrydemo-advanced-01.jpeg" src="/docs-assets/zh-cn/_images/twrrtlsanddatatelemetrydemo-advanced-01.jpeg" style="width: 32%;"></a>
<a class="reference internal image-reference" href="../../../_images/twrrtlsanddatatelemetrydemo-advanced-02.jpeg"><img alt="../../../_images/twrrtlsanddatatelemetrydemo-advanced-02.jpeg" src="/docs-assets/zh-cn/_images/twrrtlsanddatatelemetrydemo-advanced-02.jpeg" style="width: 32%;"></a>
<a class="reference internal image-reference" href="../../../_images/twrrtlsanddatatelemetrydemo-advanced-03.jpeg"><img alt="../../../_images/twrrtlsanddatatelemetrydemo-advanced-03.jpeg" src="/docs-assets/zh-cn/_images/twrrtlsanddatatelemetrydemo-advanced-03.jpeg" style="width: 32%;"></a>
</li>
</ol>
</div>
<input id="sd-tab-item-2" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-2">
故障排除</label><div class="sd-tab-content docutils">
<ol class="arabic">
<li><p>当低功耗Bluetooth (BLE) 和 LED 同时关闭时，用户可能会错误地认为电路板无法工作。在这种情况下，用户唯一的办法就是启动出厂重置 (<a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/shell-api/sys#frst"><span class="std std-ref">frst</span></a>) 命令。</p></li>
<li><p>这里有一些解决安装过程中相关问题的提示。</p>
<ul class="simple">
<li><p>请检查版本. 我们建议您使用最新的官方版本。</p></li>
<li><p>当你不知道设备的当前状态时，请在 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> 的演示选择器中使用 <span class="red-text">将设备重置为默认值</span> 功能. 请参考下面的 GIF 图片。</p></li>
</ul>
<img alt="../../../_images/reset-devices-to-defaul-x2.gif" class="align-center" src="/docs-assets/zh-cn/_images/reset-devices-to-defaul-x2.gif">
</li>
</ol>
</div>
</div>
<p><strong>数据流</strong>:当标签闪烁时，锚点会接收闪烁，并通过 Leaps Gateway向 Leaps Server发送闪烁的 TX/RX 时间戳。 Leaps Server使用从主播收集的时间戳来计算标签的位置，并将位置发布到 MQTT 代理。</p>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/uplink_tdoa_rtls_demo.png"><img alt="../../../_images/uplink_tdoa_rtls_demo.png" class="align-right" src="/docs-assets/zh-cn/_images/uplink_tdoa_rtls_demo.png" style="width: 360.0px; height: 397.20000000000005px;"></a>
</div></blockquote>
<p><strong>基础架构设置</strong></p>
<blockquote>
<div><ol class="arabic simple">
<li><p>设备配置</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>和上面一样，使用快速启动中的LM或高级中的Shell来配置设备。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="2">
<li><p>设置 Raspberry Pis</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>使用 LEAPS-RPI-IMAGE 安装所有 Raspberry Pis。</p></li>
<li><p>每个对应的锚点连接到一个 Raspberry Pi，因此至少需要 4 个 Raspberry Pi。</p></li>
<li><p>该镜像包含了 <code class="docutils literal notranslate"><span class="pre">LEAPS</span> <span class="pre">Gateway</span></code>, <code class="docutils literal notranslate"><span class="pre">LEAPS</span> <span class="pre">Server</span></code>, <code class="docutils literal notranslate"><span class="pre">LEAPS</span> <span class="pre">Center</span></code> 和 <code class="docutils literal notranslate"><span class="pre">Mosquitto</span> <span class="pre">MQTT</span> <span class="pre">Broker</span></code> 的设置和配置。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="3">
<li><p>连接Raspberry Pis</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>将所有 Raspberry Pis 连接到路由器，确保它们在同一个局域网内。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="4">
<li><p>LEAPS Server设置</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>选择任何一台 Raspberry Pi 来运行 <code class="docutils literal notranslate"><span class="pre">LEAPS</span> <span class="pre">Server</span></code>，并检查其 IP 地址. 要获取 IP 地址，请使用 ifconfig 命令。</p></li>
</ul>
<img alt="../../../_images/uplinktdoartlsdemo-ip-address.png" class="align-center" src="/docs-assets/zh-cn/_images/uplinktdoartlsdemo-ip-address.png">
</div></blockquote>
<ol class="arabic simple" start="5">
<li><p>更新配置</p></li>
</ol>
<blockquote>
<div><ul>
<li><p>使用所选 Raspberry Pi 的 IP 地址，为所有 Raspberry Pi 上的所有 LEAPS Gateway更新 <code class="docutils literal notranslate"><span class="pre">/etc/usr/share/LEAPS-DOCKER-LINUX/leaps-gateway-hub/data/leaps-gateway.conf</span></code> 中的 <code class="docutils literal notranslate"><span class="pre">leaps-server-host</span></code> 配置。</p>
<ul class="simple">
<li><p>例如</p></li>
</ul>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">leaps</span><span class="o">-</span><span class="n">server</span><span class="o">-</span><span class="n">host</span> <span class="o">=</span> <span class="mf">192.168.1.8</span>
</pre></div>
</div>
</li>
</ul>
<img alt="../../../_images/uplinktdoartlsdemo-leaps-gateway.png" class="align-center" src="/docs-assets/zh-cn/_images/uplinktdoartlsdemo-leaps-gateway.png">
<img alt="../../../_images/uplinktdoartlsdemo-leaps-gateway.png" class="align-center" src="/docs-assets/zh-cn/_images/uplinktdoartlsdemo-leaps-gateway.png">
<ul class="simple">
<li><p>保存配置，并使用以下命令重启 <code class="docutils literal notranslate"><span class="pre">LEAPS</span> <span class="pre">Gateway</span></code>：</p></li>
</ul>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">sudo</span> <span class="n">docker</span> <span class="n">restart</span> <span class="n">leaps_gateway</span>
</pre></div>
</div>
<ul class="simple">
<li><p>然后，用以下命令重启 <code class="docutils literal notranslate"><span class="pre">LEAPS</span> <span class="pre">Server</span></code>：</p></li>
</ul>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">sudo</span> <span class="n">service</span> <span class="n">leaps</span><span class="o">-</span><span class="n">server</span> <span class="n">restart</span>
</pre></div>
</div>
</div></blockquote>
<ol class="arabic simple" start="6">
<li><p>监控系统</p></li>
</ol>
<blockquote>
<div><ul>
<li><p>网关准备就绪后，使用</p></li>
<li><p>例如</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">mosquitto_sub</span> <span class="o">-</span><span class="n">h</span> <span class="mf">192.168.1.8</span> <span class="o">-</span><span class="n">p</span> <span class="mi">1883</span> <span class="o">-</span><span class="n">t</span> <span class="s1">'#'</span> <span class="o">-</span><span class="n">v</span>
</pre></div>
</div>
</li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="7">
<li><p>配置Leaps Center</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>例如:打开网络浏览器并导航到 <code class="docutils literal notranslate"><span class="pre">192.168.1.8/2</span></code></p></li>
<li><p>这可以直接在 Raspberry Pi 上访问，或者在连接到由 Raspberry Pi 以 <code class="docutils literal notranslate"><span class="pre">Leaps1234</span></code> 密码广播的 LEAPS-AP 网络的 PC 上访问。</p></li>
<li><p>如果在局域网中，你也可以使用另一台电脑的网页浏览器来访问 Raspberry Pi 的 IP 地址。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="8">
<li><p>网络配置</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>在 <code class="docutils literal notranslate"><span class="pre">LEAPS</span> <span class="pre">Center</span></code> 中，配置网络设置，以匹配所连接的网关板的网络 ID。</p></li>
</ul>
<img alt="../../../_images/uplinktdoartlsdemo-leaps-center.png" class="align-center" src="/docs-assets/zh-cn/_images/uplinktdoartlsdemo-leaps-center.png">
</div></blockquote>
<p>现在系统已经成功设置并配置好了。请尽情使用！</p>
</div></blockquote>
<div class="admonition note">
<p class="admonition-title">注解</p>
<ul class="simple">
<li><p>请参考软件基础架构，进一步探索此演示的强大功能. 我们的支持包括 <a class="reference internal" href="/docs/zh/udk/udk-start/infrastructure-docker#leaps-docker"><span class="std std-ref">LEAPS Docker</span></a>,  <a class="reference internal" href="/docs/zh/udk/udk-start/infrastructure-vmware#leaps-vmware"><span class="std std-ref">LEAPS VMWare</span></a> 和 <a class="reference internal" href="/docs/zh/udk/udk-start/infrastructure-rpi#leaps-raspberrypi"><span class="std std-ref">LEAPS Raspberry Pi</span></a>。</p></li>
<li><p>如果您对我们的产品有任何意见或问题，请访问我们的 <a class="reference external" href="https://forum.leapslabs.com">LEAPS 论坛</a>。</p></li>
<li><p>有关已知限制和问题列表的详情，请参阅 <a class="reference internal" href="/docs/zh/udk/release#udk-releases"><span class="std std-ref">发布</span></a> 部分。</p></li>
</ul>
</div>
</div>


           </div>
