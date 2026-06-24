---
title: "TWR RTLS 和数据遥测演示"
lang: zh
slug: "udk/udk-start/twr-rtls-and-data-telemetry-demo"
section: "udk"
sourceUrl: "https://docs.leapslabs.com/zh-cn/udk/udk-start/twr-rtls-and-data-telemetry-demo/"
order: 42
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="twr-rtls-and-data-telemetry-demo">
<span id="id1"></span><h1>TWR RTLS 和数据遥测演示</h1>
<p><strong>准备设置</strong></p>
<a class="reference internal image-reference" href="../../../_images/twr_rtls_and_data_telemetry_demo.png"><img alt="../../../_images/twr_rtls_and_data_telemetry_demo.png" class="align-right" src="/docs-assets/zh-cn/_images/twr_rtls_and_data_telemetry_demo.png" style="width: 396.0px; height: 202.84px;"></a>
<ol class="arabic simple">
<li><p><a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> 应用程序已安装。</p></li>
<li><p>至少五个LC14设备。</p></li>
<li><p>用于为设备供电的电池或USB-C电缆。</p></li>
<li><p><em>推荐:带相机支架的夹子或三脚架，用于安装主播设备*</em></p></li>
<li><p><em>建议使用一台Raspberry Pi 3B或更新版本，或者一台 PC, 数据服务器和网络应用程序安装。</em></p></li>
<li><p><em>可选: Putty, Teraterm, minicom或安装在计算机上的您最喜欢的终端应用程序</em></p></li>
</ol>
<p><strong>设置时间：</strong> 少于 5 分钟</p>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-0" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-0">
快速启动</label><div class="sd-tab-content docutils">
<p><strong>概览</strong></p>
<p>此设置演示了使用 <span class="red-text">双向测距 (TWR)</span> 技术的实时导航, 跟踪和双向数据遥测。 它演示了使用DL TDoA技术对无限数量的标签进行实时导航。</p>
<p><strong>典型应用</strong>:室内导航, 资产追踪和实时数据遥测，支持上行和下行链路。</p>
<p><strong>设置说明</strong></p>
<ol class="arabic simple">
<li><p>启动 <span class="red-text">ON</span> 设备。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>静态安装的设备将作为锚点，为标签提供位置信息。</p></li>
<li><p>移动设备将作为配置为双向测距测量模式的标签。</p></li>
</ul>
</div></blockquote>
<ol class="arabic" start="2">
<li><p>使用 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> 中的演示选择器进行配置:</p>
<p>2.1.打开 LEAPS Manager，从主页面选择:red:<cite>Demo Selector</cite>。</p>
<p>2.2. 选择 <span class="red-text">TWR RTLS和数据遥测</span>。</p>
<p>2.3. 通过Bluetooth发现的设备列表会出现在列表上. 如有需要，向下滑动以更新列表。</p>
<p>2.4. 选择用于演示的设备. 顶部的 <span class="red-text">anchors</span> 和 <span class="red-text">tags</span> 表示演示所需的设备数量。</p>
<p>2.5. 按下 <span class="red-text">SAVE</span> 键，将设备配置为 LEAPS RTLS 模式，联网 <span class="red-text">配置文件2（支持 TWR+UL / DL-Data, DL-TDoA）</span>。</p>
<p>2.6。 将出现一个弹出窗口“锚点配置”，提供配置锚点位置的选项。根据需要选择 <span class="red-text">手动</span>, <span class="red-text">自动定位</span> 或 <span class="red-text">保持当前位置</span>，然后按 <span class="red-text">OK</span>。</p>
<p>2.7. 请目测设备启动时 <span class="red-text">RED LED</span> 是否闪烁。</p>
</li>
</ol>
<blockquote>
<div><img alt="../../../_images/twrrtlsanddatatelemetrydemo-manual.gif" class="align-center" src="/docs-assets/zh-cn/_images/twrrtlsanddatatelemetrydemo-manual.gif">
</div></blockquote>
<ol class="arabic simple" start="3">
<li><p>当设备配置成功后，LEAPS演示网络窗口会出现已配置节点的列表。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p><em>推荐使用:使用警报功能来识别设备，并将其移动到正确的物理位置</em></p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="4">
<li><p>打开位于顶端下拉菜单的 <span class="red-text">Grid</span> 网格，用于显示设备及其位置。</p></li>
</ol>
<blockquote>
<div><img alt="../../../_images/downlinktdoartlsdemo-2d.gif" class="align-center" src="/docs-assets/zh-cn/_images/downlinktdoartlsdemo-2d.gif">
<p><em>(在 GIF 图像中，锚点是配置好的，并相隔 1 米放置)</em></p>
<ul class="simple">
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
<li><p>使用你想要的终端应用程序，如Putty, Teraterm, Minicom或你最喜欢的终端应用程序，连接到串行端口. 我们需要将波特率设置为 <span class="red-text">115200</span>。</p></li>
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
<div><p>例如，在Ubuntu (Linux)上打开 <span class="red-text">/dev/ttyACM0</span>，然后按 <span class="red-text">double enter</span>:</p>
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
<p><em>(监控并等待设备重置成功. 然后按下双回车键，进入命令行控制系统.)</em></p>
<ol class="loweralpha simple" start="2">
<li><p>使用 <span class="red-text">nps 2</span> 命令为每个设备配置 <span class="red-text">配置文件 2 (支持 TWR+UL / DL-Data, DL-TDoA)</span>。</p></li>
</ol>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ leaps&gt; nps 2
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
<li><p><strong>然后，需要重置设备以更新配置</strong>. 使用 <span class="red-text">reset</span> 命令来重置设备。</p></li>
</ul>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ leaps&gt; reset
reset ok
</pre></div>
</div>
</div></blockquote>
<div class="admonition note">
<p class="admonition-title">注解</p>
<p>在本例中，我们将配置一个 <strong>锚点，并启用启动器</strong>, <strong>3锚点</strong> 和 <strong>一个标签</strong>。</p>
</div>
<ol class="arabic simple" start="5">
<li><p>为每个锚点和标签配置模式。</p></li>
</ol>
<blockquote>
<div><ul>
<li><p>要配置 <span class="red-text">anchor with enable initiator</span>,请使用 <span class="red-text">nmi</span> 命令配置设备。</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ leaps&gt; nmi
</pre></div>
</div>
<p><em>然后，设备将重置，要再次访问命令行控制系统，请按双回车键。</em></p>
</li>
<li><p>要配置 <span class="red-text">3 anchors</span>，请使用 <span class="red-text">nma</span> 命令将 3 台设备配置为锚点模式，但不要启用启动器。</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ leaps&gt; nma
</pre></div>
</div>
<p><em>然后，设备将重置，要再次访问命令行控制系统，请按双回车键。</em></p>
</li>
<li><p>要配置 <span class="red-text">a tag</span>，使用 <span class="red-text">nmt</span> 命令将一个设备配置为标签模式。</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ leaps&gt; nmt
</pre></div>
</div>
<p><em>然后，设备将重置，要再次访问命令行控制系统，请按双回车键。</em></p>
</li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="6">
<li><p>为其中一个锚点配置时钟基准。</p></li>
</ol>
<blockquote>
<div><ul>
<li><p>至少配置了一个锚点。</p></li>
<li><p>要配置 <span class="red-text">带有启用时钟参考的锚点</span>，请使用命令 <span class="red-text">acs cr</span> 配置设备。</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ leaps&gt; acs cr 1
</pre></div>
</div>
</li>
<li><p><strong>然后，需要重置设备. 需要重置设备以更新配置</strong>. 使用 <span class="red-text">reset</span> 命令重置设备。</p></li>
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
<li><p>要获取位置，请使用 <span class="red-text">pg</span> 命令，要为每个锚点设置位置，请为每个锚点使用 <span class="red-text">ps</span> 命令。</p></li>
<li><p>在这个例子中，我们将配置4个锚，它们相距1米，排列成方形：</p></li>
</ul>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-4" name="sd-tab-set-1" type="radio">
<label class="sd-tab-label" for="sd-tab-item-4">
锚点 1 (启用启动器)</label><div class="sd-tab-content docutils">
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">leaps</span><span class="o">&gt;</span> <span class="n">ps</span> <span class="mi">1000</span> <span class="mi">1000</span> <span class="mi">0</span>
<span class="n">ps</span><span class="p">:</span> <span class="n">ok</span>
<span class="n">leaps</span><span class="o">&gt;</span> <span class="n">pg</span>
<span class="n">pg</span><span class="p">:</span> <span class="n">x</span><span class="p">:</span><span class="mi">1000</span> <span class="n">y</span><span class="p">:</span><span class="mi">1000</span> <span class="n">z</span><span class="p">:</span><span class="mi">0</span> <span class="n">qf</span><span class="p">:</span><span class="mi">100</span>
<span class="n">leaps</span><span class="o">&gt;</span>
</pre></div>
</div>
</div>
<input id="sd-tab-item-5" name="sd-tab-set-1" type="radio">
<label class="sd-tab-label" for="sd-tab-item-5">
锚点 2</label><div class="sd-tab-content docutils">
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">leaps</span><span class="o">&gt;</span> <span class="n">ps</span> <span class="mi">0</span> <span class="mi">0</span> <span class="mi">0</span>
<span class="n">ps</span><span class="p">:</span> <span class="n">ok</span>
<span class="n">leaps</span><span class="o">&gt;</span> <span class="n">pg</span>
<span class="n">pg</span><span class="p">:</span> <span class="n">x</span><span class="p">:</span><span class="mi">0</span> <span class="n">y</span><span class="p">:</span><span class="mi">0</span> <span class="n">z</span><span class="p">:</span><span class="mi">0</span> <span class="n">qf</span><span class="p">:</span><span class="mi">100</span>
<span class="n">leaps</span><span class="o">&gt;</span>
</pre></div>
</div>
</div>
<input id="sd-tab-item-6" name="sd-tab-set-1" type="radio">
<label class="sd-tab-label" for="sd-tab-item-6">
锚点 3</label><div class="sd-tab-content docutils">
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">leaps</span><span class="o">&gt;</span> <span class="n">ps</span> <span class="mi">1000</span> <span class="mi">0</span> <span class="mi">0</span>
<span class="n">ps</span><span class="p">:</span> <span class="n">ok</span>
<span class="n">leaps</span><span class="o">&gt;</span> <span class="n">pg</span>
<span class="n">pg</span><span class="p">:</span> <span class="n">x</span><span class="p">:</span><span class="mi">1000</span> <span class="n">y</span><span class="p">:</span><span class="mi">0</span> <span class="n">z</span><span class="p">:</span><span class="mi">0</span> <span class="n">qf</span><span class="p">:</span><span class="mi">100</span>
<span class="n">leaps</span><span class="o">&gt;</span>
</pre></div>
</div>
</div>
<input id="sd-tab-item-7" name="sd-tab-set-1" type="radio">
<label class="sd-tab-label" for="sd-tab-item-7">
锚点 4</label><div class="sd-tab-content docutils">
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">leaps</span><span class="o">&gt;</span> <span class="n">ps</span> <span class="mi">0</span> <span class="mi">1000</span> <span class="mi">0</span>
<span class="n">ps</span><span class="p">:</span> <span class="n">ok</span>
<span class="n">leaps</span><span class="o">&gt;</span> <span class="n">pg</span>
<span class="n">pg</span><span class="p">:</span> <span class="n">x</span><span class="p">:</span><span class="mi">0</span> <span class="n">y</span><span class="p">:</span><span class="mi">1000</span> <span class="n">z</span><span class="p">:</span><span class="mi">0</span> <span class="n">qf</span><span class="p">:</span><span class="mi">100</span>
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
<li><p>每个标签的配置允许使用 <span class="red-text">TWR</span> 技术进行测量。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>使用 <span class="red-text">tcs mode 0</span> 命令对标签进行配置。</p></li>
</ul>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ leaps&gt; tcs mode 0
tcs: ok
</pre></div>
</div>
<ul class="simple">
<li><p><strong>然后，需要重置设备以更新配置</strong>. 使用 <span class="red-text">reset</span> 命令来重置设备。</p></li>
</ul>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ leaps&gt; reset
reset ok
</pre></div>
</div>
</div></blockquote>
<ol class="arabic simple" start="9">
<li><p>默认情况下 <span class="red-text">normal update rate</span> 为 0.1s/ 10Hz，<span class="red-text">stationary update rate</span> 为 5.0s/ 0.2Hz. 要提高速度，请使用 <span class="red-text">urs</span> 命令。</p></li>
</ol>
<blockquote>
<div><p>例如，配置 <span class="red-text">normal update rate</span> 为0.1s/ 10Hz，而 <span class="red-text">stationary update rate</span> 为0.1s/ 10Hz. 运行以下命令:</p>
<blockquote>
<div><div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ leaps&gt; urs 1 1
urs: ok
</pre></div>
</div>
</div></blockquote>
</div></blockquote>
<ol class="arabic simple" start="10">
<li><p>在步骤 5, 6, 7 和 8 中，可以使用 <span class="red-text">si</span> 命令来验证模式, 配置文件和网络配置是否正确。 (可选)</p></li>
</ol>
<blockquote>
<div><p>例如 4 个锚点和一个标签：</p>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-8" name="sd-tab-set-2" type="radio">
<label class="sd-tab-label" for="sd-tab-item-8">
锚点 1 (启用启动器)</label><div class="sd-tab-content docutils">
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">mode:</span> <span class="pre">ani</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">panid=x1234</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prof=2</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cr=1</span></code></p></li>
</ul>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>leaps&gt; nps 2
nps: ok
leaps&gt; nis 0x1234
nis: ok
leaps&gt; acs cr 1
nis: ok
leaps&gt; nmi


Low Energy Accurate Positioning System

FOR DEMO PURPOSE ONLY, NOT FOR SALE.

Copyright :  2016-2023 LEAPS
License   :  Please visit https://www.leapslabs.com/leaps-rtls-license
Compiled  :  Jan  6 2024 09:38:07 (v0.15.0-ab84fb)

Help      :  ? or help

leaps&gt;si
[000011.796 INF] release: LEAPS RTLS v0.15.0-ab84fb
[000011.796 INF] sys: main main_ver=x02000001 cfg_ver=x01040000 batt=none board=LC14_B
[000011.796 INF] uwb: ch9 prf64 plen128 pac8 txcode9 rxcode9 baud6800 phrmodeext phrratestd sfdtypeieee4a sfdto129 stsmodeoff stslen64 pdoamodem0
[000011.797 INF] uwb: tx_pwr=x34/xFAFAFAFA sts:shr:phr:data=27.7:27.7:27.7:27.7[dB] cpl=FCC/ETSI pgcnt=234 temp=25
[000011.797 INF] uwb: lna=1 pa=0 rf1=1 rf2=0 xtaltrim=27 tx_delay=16438 rx_delay=16438
[000011.798 INF] uwb: panid=x1234 addr=xDECA0E27530083A2
[000011.801 INF] mode: ani (act,real)
[000011.813 INF] uwbmac: connected prof=2 (manual)
[000011.813 INF] uwbmac: bh disconnected
[000011.813 INF] cfg: sync=0 fwup=1 ble=1 leds=1 init=1 uab=1 bh=auto bh_stat=off cr=1 upd_rate_stat=30 label=ID83A2
[000011.845 INF] enc: off
[000011.845 INF] ble: addr=F8:64:22:75:6C:F7
leaps&gt;
</pre></div>
</div>
</div>
<input id="sd-tab-item-9" name="sd-tab-set-2" type="radio">
<label class="sd-tab-label" for="sd-tab-item-9">
锚点 2</label><div class="sd-tab-content docutils">
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">mode:</span> <span class="pre">an</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">panid=x1234</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prof=2</span></code></p></li>
</ul>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>leaps&gt; nps 2
nps: ok
leaps&gt; nis 0x1234
nis: ok
leaps&gt; nma


Low Energy Accurate Positioning System

FOR DEMO PURPOSE ONLY, NOT FOR SALE.

Copyright :  2016-2023 LEAPS
License   :  Please visit https://www.leapslabs.com/leaps-rtls-license
Compiled  :  Jan  6 2024 09:38:07 (v0.15.0-ab84fb)

Help      :  ? or help

leaps&gt;si
[000014.484 INF] release: LEAPS RTLS v0.15.0-ab84fb
[000014.484 INF] sys: main main_ver=x02000001 cfg_ver=x01040000 batt=none board=LC14_B
[000014.485 INF] uwb: ch9 prf64 plen128 pac8 txcode9 rxcode9 baud6800 phrmodeext phrratestd sfdtypeieee4a sfdto129 stsmodeoff stslen64 pdoamodem0
[000014.485 INF] uwb: tx_pwr=x34/xE6E6E6E6 sts:shr:phr:data=25.8:25.8:25.8:25.8[dB] cpl=FCC/ETSI pgcnt=233 temp=25
[000014.486 INF] uwb: lna=1 pa=0 rf1=1 rf2=0 xtaltrim=32 tx_delay=16438 rx_delay=16438
[000014.486 INF] uwb: panid=x1234 addr=xDECA9DD29FD0CBBB
[000014.490 INF] mode: an (act,-)
[000014.502 INF] uwbmac: connected prof=2 (manual)
[000014.502 INF] uwbmac: bh disconnected
[000014.502 INF] cfg: sync=0 fwup=1 ble=1 leds=1 init=0 uab=1 bh=auto bh_stat=off cr=0 upd_rate_stat=30 label=IDCBBB
[000014.532 INF] enc: off
[000014.532 INF] ble: addr=E6:92:A3:6B:05:21
leaps&gt;
</pre></div>
</div>
</div>
<input id="sd-tab-item-10" name="sd-tab-set-2" type="radio">
<label class="sd-tab-label" for="sd-tab-item-10">
锚点 3</label><div class="sd-tab-content docutils">
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">mode:</span> <span class="pre">an</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">panid=x1234</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prof=2</span></code></p></li>
</ul>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>leaps&gt; nps 2
nps: ok
leaps&gt; nis 0x1234
nis: ok
leaps&gt; nma


Low Energy Accurate Positioning System

FOR DEMO PURPOSE ONLY, NOT FOR SALE.

Copyright :  2016-2023 LEAPS
License   :  Please visit https://www.leapslabs.com/leaps-rtls-license
Compiled  :  Jan  6 2024 09:38:07 (v0.15.0-ab84fb)

Help      :  ? or help

leaps&gt; si
[000007.647 INF] release: LEAPS RTLS v0.15.0-ab84fb
[000007.647 INF] sys: main main_ver=x02000001 cfg_ver=x01040000 batt=42%:1785mV:discharging board=LC14_B
[000007.648 INF] uwb: ch9 prf64 plen128 pac8 txcode9 rxcode9 baud6800 phrmodeext phrratestd sfdtypeieee4a sfdto129 stsmodeoff stslen64 pdoamodem0
[000007.648 INF] uwb: tx_pwr=x34/xEEEEEEEE sts:shr:phr:data=26.5:26.5:26.5:26.5[dB] cpl=FCC/ETSI pgcnt=245 temp=25
[000007.649 INF] uwb: lna=1 pa=0 rf1=1 rf2=0 xtaltrim=32 tx_delay=16436 rx_delay=16436
[000007.649 INF] uwb: panid=x1234 addr=xDECA7A20DFE04F2E
[000007.667 INF] mode: an (act,-)
[000007.668 INF] uwbmac: connected prof=2 (manual)
[000007.668 INF] uwbmac: bh disconnected
[000007.668 INF] cfg: sync=0 fwup=1 ble=1 leds=1 init=0 uab=1 bh=auto bh_stat=off cr=0 upd_rate_stat=30 label=ID4F2E
[000007.692 INF] enc: off
[000007.692 INF] ble: addr=C8:D9:F3:F1:7D:CE
leaps&gt;
</pre></div>
</div>
</div>
<input id="sd-tab-item-11" name="sd-tab-set-2" type="radio">
<label class="sd-tab-label" for="sd-tab-item-11">
锚点 4</label><div class="sd-tab-content docutils">
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">mode:</span> <span class="pre">an</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">panid=x1234</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prof=2</span></code></p></li>
</ul>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>leaps&gt; nps 2
nps: ok
leaps&gt; nis 0x1234
nis: ok
leaps&gt; nma


Low Energy Accurate Positioning System

FOR DEMO PURPOSE ONLY, NOT FOR SALE.

Copyright :  2016-2023 LEAPS
License   :  Please visit https://www.leapslabs.com/leaps-rtls-license
Compiled  :  Jan  6 2024 09:38:07 (v0.15.0-ab84fb)

Help      :  ? or help

leaps&gt; si
[000027.150 INF] release: LEAPS RTLS v0.15.0-ab84fb
[000027.150 INF] sys: main main_ver=x02000001 cfg_ver=x01040000 batt=none board=LC14_B
[000027.151 INF] uwb: ch9 prf64 plen128 pac8 txcode9 rxcode9 baud6800 phrmodeext phrratestd sfdtypeieee4a sfdto129 stsmodeoff stslen64 pdoamodem0
[000027.151 INF] uwb: tx_pwr=x34/xC6C6C6C6 sts:shr:phr:data=22.6:22.6:22.6:22.6[dB] cpl=FCC/ETSI pgcnt=236 temp=25
[000027.152 INF] uwb: lna=1 pa=0 rf1=1 rf2=0 xtaltrim=32 tx_delay=16431 rx_delay=16431
[000027.152 INF] uwb: panid=x1234 addr=xDECAED5BC8B1468D
[000027.155 INF] mode: an (act,-)
[000027.170 INF] uwbmac: connected prof=2 (manual)
[000027.170 INF] uwbmac: bh disconnected
[000027.170 INF] cfg: sync=0 fwup=1 ble=1 leds=1 init=0 uab=1 bh=auto bh_stat=off cr=0 upd_rate_stat=30 label=ID468D
[000027.199 INF] enc: off
[000027.199 INF] ble: addr=F3:D9:66:75:93:EB
leaps&gt;
</pre></div>
</div>
</div>
<input id="sd-tab-item-12" name="sd-tab-set-2" type="radio">
<label class="sd-tab-label" for="sd-tab-item-12">
标签</label><div class="sd-tab-content docutils">
<ul class="simple">
<li><p>根据默认配置，设备将处于 <span class="red-text">TWR mode</span> 模式. 如果处于其他模式，我们将使用 <span class="red-text">tcs mode 0</span> 命令。</p></li>
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

Copyright :  2016-2023 LEAPS
License   :  Please visit https://www.leapslabs.com/leaps-rtls-license
Compiled  :  Jan  6 2024 09:38:07 (v0.15.0-ab84fb)

Help      :  ? or help

leaps&gt; urs 1 1
urs: ok
leaps&gt; si
[000010.225 INF] release: LEAPS RTLS v0.15.0-ab84fb
[000010.225 INF] sys: main main_ver=x02000001 cfg_ver=x01040000 batt=none board=LC14_B
[000010.226 INF] uwb: ch9 prf64 plen128 pac8 txcode9 rxcode9 baud6800 phrmodeext phrratestd sfdtypeieee4a sfdto129 stsmodeoff stslen64 pdoamodem0
[000010.226 INF] uwb: tx_pwr=x34/xB6B6B6B6 sts:shr:phr:data=21.1:21.1:21.1:21.1[dB] cpl=FCC/ETSI pgcnt=231 temp=25
[000010.226 INF] uwb: lna=1 pa=0 rf1=1 rf2=0 xtaltrim=43 tx_delay=16434 rx_delay=16434
[000010.227 INF] uwb: panid=x1234 addr=xDECA80CB2C558A11
[000010.230 INF] mode: tn (act,twr,np,le)
[000010.246 INF] uwbmac: connected prof=2 (manual)
[000010.246 INF] uwbmac: bh disconnected
[000010.247 INF] cfg: sync=0 fwup=1 ble=1 leds=1 le=1 lp=0 uab=1 stat_det=1 (sens=2) mode=0 upd_rate_norm=1 upd_rate_stat=1 label=ID8A11
[000010.274 INF] enc: off
[000010.274 INF] ble: addr=E8:BB:0A:C9:93:4E
leaps&gt;
</pre></div>
</div>
</div>
</div>
</div></blockquote>
<ol class="arabic simple" start="11">
<li><p>要查看范围内与设备本身相连的锚点列表，请使用 <span class="red-text">la</span> (可选)</p></li>
</ol>
<blockquote>
<div><p>例如在锚点 1 上（启用启动器）：</p>
<blockquote>
<div><div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">leaps</span><span class="o">&gt;</span> <span class="n">la</span>
<span class="p">[</span><span class="mf">000025.454</span> <span class="n">INF</span><span class="p">]</span> <span class="n">AN</span><span class="p">:</span> <span class="n">cnt</span><span class="o">=</span><span class="mi">4</span> <span class="n">seq</span><span class="o">=</span><span class="n">x03</span>
<span class="p">[</span><span class="mf">000025.454</span> <span class="n">INF</span><span class="p">]</span>     <span class="mi">0</span><span class="p">)</span> <span class="nb">id</span><span class="o">=</span><span class="mi">83</span><span class="n">A2</span> <span class="n">seat</span><span class="o">=</span><span class="mi">0</span> <span class="n">clk_lvl</span><span class="o">=</span><span class="mi">0</span> <span class="n">seens</span><span class="o">=</span><span class="mi">0</span> <span class="n">rssi</span><span class="o">=-</span><span class="mi">127</span> <span class="n">cl</span><span class="o">=</span><span class="mi">0000000</span><span class="n">F</span> <span class="n">nbr</span><span class="o">=</span><span class="mi">0000000</span><span class="n">F</span> <span class="n">pos</span><span class="o">=</span><span class="mf">1.00</span><span class="p">:</span><span class="mf">1.00</span><span class="p">:</span><span class="mf">0.00</span>
<span class="p">[</span><span class="mf">000025.454</span> <span class="n">INF</span><span class="p">]</span>     <span class="mi">1</span><span class="p">)</span> <span class="nb">id</span><span class="o">=</span><span class="mi">468</span><span class="n">D</span> <span class="n">seat</span><span class="o">=</span><span class="mi">2</span> <span class="n">clk_lvl</span><span class="o">=</span><span class="mi">1</span> <span class="n">seens</span><span class="o">=</span><span class="mi">81</span> <span class="n">rssi</span><span class="o">=-</span><span class="mi">55</span> <span class="n">cl</span><span class="o">=</span><span class="mi">0000000</span><span class="n">F</span> <span class="n">nbr</span><span class="o">=</span><span class="mi">00000000</span> <span class="n">pos</span><span class="o">=</span><span class="mf">0.00</span><span class="p">:</span><span class="mf">1.00</span><span class="p">:</span><span class="mf">0.00</span>
<span class="p">[</span><span class="mf">000025.455</span> <span class="n">INF</span><span class="p">]</span>     <span class="mi">2</span><span class="p">)</span> <span class="nb">id</span><span class="o">=</span><span class="mi">4</span><span class="n">F2E</span> <span class="n">seat</span><span class="o">=</span><span class="mi">3</span> <span class="n">clk_lvl</span><span class="o">=</span><span class="mi">1</span> <span class="n">seens</span><span class="o">=</span><span class="mi">67</span> <span class="n">rssi</span><span class="o">=-</span><span class="mi">55</span> <span class="n">cl</span><span class="o">=</span><span class="mi">0000000</span><span class="n">F</span> <span class="n">nbr</span><span class="o">=</span><span class="mi">00000000</span> <span class="n">pos</span><span class="o">=</span><span class="mf">1.00</span><span class="p">:</span><span class="mf">0.00</span><span class="p">:</span><span class="mf">0.00</span>
<span class="p">[</span><span class="mf">000025.455</span> <span class="n">INF</span><span class="p">]</span>     <span class="mi">3</span><span class="p">)</span> <span class="nb">id</span><span class="o">=</span><span class="n">CBBB</span> <span class="n">seat</span><span class="o">=</span><span class="mi">1</span> <span class="n">clk_lvl</span><span class="o">=</span><span class="mi">1</span> <span class="n">seens</span><span class="o">=</span><span class="mi">111</span> <span class="n">rssi</span><span class="o">=-</span><span class="mi">55</span> <span class="n">cl</span><span class="o">=</span><span class="mi">0000000</span><span class="n">F</span> <span class="n">nbr</span><span class="o">=</span><span class="mi">00000000</span> <span class="n">pos</span><span class="o">=</span><span class="mf">0.00</span><span class="p">:</span><span class="mf">0.00</span><span class="p">:</span><span class="mf">0.00</span>
<span class="p">[</span><span class="mf">000025.456</span> <span class="n">INF</span><span class="p">]</span>
</pre></div>
</div>
</div></blockquote>
</div></blockquote>
<ol class="arabic simple" start="12">
<li><p>完成所有配置后. 打开标签的 shell 控制台，使用 <span class="red-text">les</span> 命令查看标签位置。</p></li>
</ol>
<blockquote>
<div><p>例如在 Tag 上，位置会实时更新和显示：</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ leaps&gt; les
  leaps&gt; POS[0.34,0.18,0.70,50] CBBB[0.00,0.00,0.00,100]=0.79 4F2E[1.00,0.00,0.00,100]=0.98 468D[0.00,1.00,0.00,100]=1.12 83A2[1.00,1.00,0.00,100]=0.87
  POS[0.34,0.19,0.71,50] CBBB[0.00,0.00,0.00,100]=0.81 4F2E[1.00,0.00,0.00,100]=0.99 468D[0.00,1.00,0.00,100]=1.13 83A2[1.00,1.00,0.00,100]=0.87
  POS[0.34,0.20,0.70,49] CBBB[0.00,0.00,0.00,100]=0.81 4F2E[1.00,0.00,0.00,100]=0.98 468D[0.00,1.00,0.00,100]=1.12 83A2[1.00,1.00,0.00,100]=0.87
  POS[0.35,0.23,0.73,50] CBBB[0.00,0.00,0.00,100]=0.84 4F2E[1.00,0.00,0.00,100]=1.00 468D[0.00,1.00,0.00,100]=1.12 83A2[1.00,1.00,0.00,100]=0.87
  POS[0.36,0.22,0.74,51] CBBB[0.00,0.00,0.00,100]=0.85 4F2E[1.00,0.00,0.00,100]=1.00 468D[0.00,1.00,0.00,100]=1.13 83A2[1.00,1.00,0.00,100]=0.88
  POS[0.37,0.22,0.74,52] CBBB[0.00,0.00,0.00,100]=0.85 4F2E[1.00,0.00,0.00,100]=1.00 468D[0.00,1.00,0.00,100]=1.13 83A2[1.00,1.00,0.00,100]=0.90
  POS[0.37,0.22,0.73,52] CBBB[0.00,0.00,0.00,100]=0.85 4F2E[1.00,0.00,0.00,100]=0.99 468D[0.00,1.00,0.00,100]=1.13 83A2[1.00,1.00,0.00,100]=0.88
  POS[0.36,0.21,0.73,51] CBBB[0.00,0.00,0.00,100]=0.84 4F2E[1.00,0.00,0.00,100]=0.99 468D[0.00,1.00,0.00,100]=1.13 83A2[1.00,1.00,0.00,100]=0.89
  POS[0.33,0.21,0.73,51] CBBB[0.00,0.00,0.00,100]=0.83 4F2E[1.00,0.00,0.00,100]=1.02 468D[0.00,1.00,0.00,100]=1.12 83A2[1.00,1.00,0.00,100]=0.89
  POS[0.33,0.20,0.72,50] CBBB[0.00,0.00,0.00,100]=0.81 4F2E[1.00,0.00,0.00,100]=1.00 468D[0.00,1.00,0.00,100]=1.12 83A2[1.00,1.00,0.00,100]=0.91
  POS[0.34,0.22,0.72,50] CBBB[0.00,0.00,0.00,100]=0.83 4F2E[1.00,0.00,0.00,100]=1.00 468D[0.00,1.00,0.00,100]=1.11 83A2[1.00,1.00,0.00,100]=0.92
  POS[0.36,0.22,0.71,50] CBBB[0.00,0.00,0.00,100]=0.83 4F2E[1.00,0.00,0.00,100]=0.98 468D[0.00,1.00,0.00,100]=1.12 83A2[1.00,1.00,0.00,100]=0.91
  ...
</pre></div>
</div>
</div></blockquote>
<ol class="arabic" start="12">
<li><p>此外，我们还可以使用 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> 来可视化设备及其位置。</p>
<a class="reference internal image-reference" href="../../../_images/twrrtlsanddatatelemetrydemo-advanced-01.jpeg"><img alt="../../../_images/twrrtlsanddatatelemetrydemo-advanced-01.jpeg" src="/docs-assets/zh-cn/_images/twrrtlsanddatatelemetrydemo-advanced-01.jpeg" style="width: 32%;"></a>
<a class="reference internal image-reference" href="../../../_images/twrrtlsanddatatelemetrydemo-advanced-02.jpeg"><img alt="../../../_images/twrrtlsanddatatelemetrydemo-advanced-02.jpeg" src="/docs-assets/zh-cn/_images/twrrtlsanddatatelemetrydemo-advanced-02.jpeg" style="width: 32%;"></a>
<a class="reference internal image-reference" href="../../../_images/twrrtlsanddatatelemetrydemo-advanced-03.jpeg"><img alt="../../../_images/twrrtlsanddatatelemetrydemo-advanced-03.jpeg" src="/docs-assets/zh-cn/_images/twrrtlsanddatatelemetrydemo-advanced-03.jpeg" style="width: 32%;"></a>
</li>
</ol>
<p>现在系统已经成功设置和配置。 祝您使用愉快！</p>
</div>
<input id="sd-tab-item-2" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-2">
Setup with Multiple Gateways</label><div class="sd-tab-content docutils">
<ol class="arabic">
<li><p>设置 <a class="reference internal" href="/docs/zh/udk/udk-start/infrastructure-rpi#leaps-raspberrypi"><span class="std std-ref">LEAPS Raspberry Pi</span></a></p>
<ul class="simple">
<li><p>使用 LEAPS-RPI-IMAGE 安装所有 Raspberry Pis。</p></li>
<li><p>每个对应的锚点连接到一个 Raspberry Pi，因此至少需要 4 个 Raspberry Pi。</p></li>
<li><p>该镜像包含了 <code class="docutils literal notranslate"><span class="pre">LEAPS</span> <span class="pre">Gateway</span></code>, <code class="docutils literal notranslate"><span class="pre">LEAPS</span> <span class="pre">Server</span></code>, <code class="docutils literal notranslate"><span class="pre">LEAPS</span> <span class="pre">Center</span></code> 和 <code class="docutils literal notranslate"><span class="pre">Mosquitto</span> <span class="pre">MQTT</span> <span class="pre">Broker</span></code> 的设置和配置。</p></li>
</ul>
</li>
<li><p>连接Raspberry Pis</p>
<ul class="simple">
<li><p>将所有 Raspberry Pis 连接到路由器，确保它们在同一个局域网内。</p></li>
</ul>
</li>
<li><p>LEAPS Server设置</p>
<ul class="simple">
<li><p>选择任何一台 Raspberry Pi 来运行 <code class="docutils literal notranslate"><span class="pre">LEAPS</span> <span class="pre">Server</span></code>，并检查其 IP 地址. 要获取 IP 地址，请使用 ifconfig 命令。</p></li>
<li><p>例如</p></li>
</ul>
<blockquote>
<div><img alt="../../../_images/uplinktdoartlsdemo-ip-address.png" class="align-center" src="/docs-assets/zh-cn/_images/uplinktdoartlsdemo-ip-address.png">
</div></blockquote>
</li>
<li><p>更新配置</p>
<ul>
<li><p>使用所选 Raspberry Pi 的 IP 地址，为所有 Raspberry Pi 上的所有 LEAPS Gateway更新 <code class="docutils literal notranslate"><span class="pre">/usr/share/LEAPS-DOCKER-LINUX/leaps-gateway-hub/data/leaps-gateway.conf</span></code> 中的 <code class="docutils literal notranslate"><span class="pre">leaps-server-host</span></code> 配置。</p></li>
<li><p>例如</p>
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
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">sudo</span> <span class="n">docker</span> <span class="n">restart</span> <span class="n">leaps_server</span>
</pre></div>
</div>
</li>
<li><p>监控系统</p>
<ul class="simple">
<li><p>网关准备就绪后，使用</p></li>
<li><p>例如</p></li>
</ul>
<blockquote>
<div><div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">mosquitto_sub</span> <span class="o">-</span><span class="n">h</span> <span class="mf">192.168.1.8</span> <span class="o">-</span><span class="n">p</span> <span class="mi">1883</span> <span class="o">-</span><span class="n">t</span> <span class="s1">'#'</span> <span class="o">-</span><span class="n">v</span>
</pre></div>
</div>
</div></blockquote>
</li>
<li><p>配置Leaps Center</p>
<ul class="simple">
<li><p>例如:打开网络浏览器并导航到 <code class="docutils literal notranslate"><span class="pre">192.168.1.8/2</span></code></p></li>
<li><p>这可以直接在 Raspberry Pi 上访问，或者在连接到由 Raspberry Pi 以 <code class="docutils literal notranslate"><span class="pre">Leaps1234</span></code> 密码广播的 LEAPS-AP 网络的 PC 上访问。</p></li>
<li><p>如果在局域网中，你也可以使用另一台电脑的网页浏览器来访问 Raspberry Pi 的 IP 地址。</p></li>
</ul>
</li>
<li><p>网络配置</p>
<ul class="simple">
<li><p>在 <code class="docutils literal notranslate"><span class="pre">LEAPS</span> <span class="pre">Center</span></code> 中，配置网络设置，以匹配所连接的网关板的网络 ID。</p></li>
</ul>
<img alt="../../../_images/docker_leaps_center_network.png" class="align-center" src="/docs-assets/zh-cn/_images/docker_leaps_center_network.png">
</li>
</ol>
<p>现在系统已经成功设置和配置。 祝您使用愉快！</p>
</div>
<input id="sd-tab-item-3" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-3">
故障排除</label><div class="sd-tab-content docutils">
<ol class="arabic">
<li><p>当低功耗Bluetooth (BLE) 和 LED 同时熄灭时，用户可能会错误地认为电路板无法运作。 在这种情况下，用户唯一的办法就是启动出厂重置（<a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/shell-api/sys#frst"><span class="std std-ref">frst</span></a>）命令。</p></li>
<li><p>以下是一些修复与安装过程有关的问题的提示。</p>
<ul class="simple">
<li><p>请检查版本. 我们建议您使用最新的官方版本。</p></li>
<li><p>当您不知道设备的当前状态时，请使用 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> 上演示选择器中的 <span class="red-text">将设备重置为默认值</span> 功能. 请参阅以下GIF图像。</p></li>
</ul>
<img alt="../../../_images/reset-devices-to-defaul-x2.gif" class="align-center" src="/docs-assets/zh-cn/_images/reset-devices-to-defaul-x2.gif">
</li>
</ol>
</div>
</div>
<p><strong>快速启动 LEAPS Center</strong></p>
<blockquote>
<div><ul class="simple">
<li><p>请参考软件基础架构，以进一步探索此演示的功能. 我们的支持包括 <a class="reference internal" href="/docs/zh/udk/udk-start/infrastructure-docker#leaps-docker"><span class="std std-ref">LEAPS Docker</span></a>, <a class="reference internal" href="/docs/zh/udk/udk-start/infrastructure-vmware#leaps-vmware"><span class="std std-ref">LEAPS VMWare</span></a> 和 <a class="reference internal" href="/docs/zh/udk/udk-start/infrastructure-rpi#leaps-raspberrypi"><span class="std std-ref">LEAPS Raspberry Pi</span></a>。</p></li>
</ul>
</div></blockquote>
<div class="admonition note">
<p class="admonition-title">注解</p>
<ul class="simple">
<li><p>如果您对我们的产品有任何意见或问题，我们鼓励您访问我们的 <a class="reference external" href="https://forum.leapslabs.com">LEAPS 论坛</a>。</p></li>
<li><p>有关已知限制和问题列表的详情，请参阅 <a class="reference internal" href="/docs/zh/udk/release#udk-releases"><span class="std std-ref">发布</span></a> 部分。</p></li>
</ul>
</div>
</div>


           </div>
