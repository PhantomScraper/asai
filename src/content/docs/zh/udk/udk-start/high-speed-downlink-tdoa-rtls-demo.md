---
title: "高速下行TDoA RTLS演示"
lang: zh
slug: "udk/udk-start/high-speed-downlink-tdoa-rtls-demo"
section: "udk"
sourceUrl: "https://docs.leapslabs.com/zh-cn/udk/udk-start/high-speed-downlink-tdoa-rtls-demo/"
order: 110
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="high-speed-downlink-tdoa-rtls-demo">
<span id="anchor-hsdtdoa"></span><h1>高速下行TDoA RTLS演示</h1>
<a class="reference internal image-reference" href="../../../_images/downlink_tdoa_rtls_demo.png"><img alt="../../../_images/downlink_tdoa_rtls_demo.png" class="align-right" src="/docs-assets/zh-cn/_images/downlink_tdoa_rtls_demo.png" style="width: 216.0px; height: 245.88px;"></a>
<p><strong>准备设置</strong></p>
<ol class="arabic simple">
<li><p><a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> 应用程序。</p></li>
<li><p>至少五台LC14设备。</p></li>
<li><p>用于为设备供电的电池或USB-C电缆。</p></li>
<li><p><em>建议:带相机支架的夹具或三脚架，用于连接锚定装置</em></p></li>
<li><p><em>可选: Putty, Teratem, minicom或您最喜欢的安装在计算机上的终端应用程序</em></p></li>
</ol>
<p><strong>设置时间：</strong> 少于 5 分钟</p>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-0" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-0">
快速入门</label><div class="sd-tab-content docutils">
<p><strong>概述</strong></p>
<p>此设置演示了使用 <span class="red-text">下行链路到达时间差 (DL TDoA)</span> 技术在仅接收模式下以完全隐私的方式对无限数量的标签进行高速实时导航。 每个标签可以独立于其他标签提供高达50 Hz的位置，并通过标签位置导航演示LEAPS Manager应用程序。</p>
<p><strong>典型应用</strong>:带地图的高速室内导航, 自主机器人和车辆导航，以及通过另一个通信信道发送位置数据的资产跟踪。</p>
<p><strong>设置说明</strong></p>
<ol class="arabic simple">
<li><p>Power <span class="red-text">ON</span> 设备。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>静态安装的设备将作为锚点，为标签提供位置信息。</p></li>
<li><p>移动设备将仅在接收模式下作为导航模式下配置的标签运行，不进行传输（类似GNSS模式）。</p></li>
<li><p>标签的数量没有限制。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="2">
<li><p>使用 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> 中的演示选择器进行配置:</p></li>
</ol>
<blockquote>
<div><p>2.1。 打开LEAPS Manager，从主页中选择 <span class="red-text">演示选择器</span>。</p>
<p>2.2. 选择 <span class="red-text">高速下行链路TDoA RTLS</span>。</p>
<p>2.3。 通过Bluetooth发现的设备列表将显示在列表中。 如果需要，向下滑动以更新列表。</p>
<p>选择将用于演示的设备。 顶部的 <span class="red-text">锚点</span> 和 <span class="red-text">标签</span> 表示演示所需的设备。</p>
<p>2.5.按 <span class="red-text">SAVE</span> 将设备配置为LEAPS RTLS模式，联网 <span class="red-text">配置文件3（支持高速DL TDoA）</span>。</p>
<p>2.6。 将出现一个弹出窗口“锚点配置”，提供配置锚点位置的选项。 根据需要选择 <span class="red-text">手动</span>, <span class="red-text">自动定位</span> 或 <span class="red-text">保持当前位置</span>，然后按 <span class="red-text">OK</span>。</p>
<p>2.7. 请目视检查设备启动时 <span class="red-text">RED LED</span> 是否闪烁。</p>
<img alt="../../../_images/highspeeddownlinktdoartlsdemo-manual.gif" class="align-center" src="/docs-assets/zh-cn/_images/highspeeddownlinktdoartlsdemo-manual.gif">
</div></blockquote>
<ol class="arabic simple" start="3">
<li><p>成功配置设备后，将出现LEAPS演示网络窗口，其中包含已配置节点的列表。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p><em>建议：使用报警功能识别设备，并将其移动到正确的物理位置</em></p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="4">
<li><p>打开位于顶部下拉菜单的 <span class="red-text">Grid</span>,用于可视化设备及其位置。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>将 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> 配置为 <span class="red-text">配置文件3 (support High-Speed DL-TDoA)</span> 但处于自动状态. 因此，我们可以在地图上看到标签的坐标。</p></li>
</ul>
<img alt="../../../_images/downlinktdoartlsdemo-2d.gif" class="align-center" src="/docs-assets/zh-cn/_images/downlinktdoartlsdemo-2d.gif">
<p><em>(在 GIF 图片中，锚点是配置好的，并相隔 1 米放置)</em></p>
<ul class="simple">
<li><p>请参阅 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a>，了解如何使用应用程序来配置和可视化节点与网络的更多细节。</p></li>
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
<li><p>使用你想要的终端应用程序，如 Putty, Teraterm, Minicom 或你最喜欢的终端应用程序，连接到串行端口. 我们需要配置波特率为 <span class="red-text">115200</span>。</p></li>
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
<li><p>使用 <span class="red-text">nps 3</span> 命令，为每个设备配置 <span class="red-text">配置文件 3 (支持高速 DL-TDoA)</span>。</p></li>
</ol>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ leaps&gt; nps 3
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
<p>在这个例子里，我们将配置一个 <strong>锚，启用启动器</strong>，<strong>3个锚</strong>，以及 <strong>一个标签</strong>。</p>
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
<p><em>然后，设备将重置，要再次访问命令行控制系统，请按双回车键。</em></p>
</li>
<li><p>要配置 <span class="red-text">3 anchors</span>，请使用 <span class="red-text">nma</span> 命令将 3 台设备配置为锚点模式，但不要启用启动器。</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ leaps&gt; nma
</pre></div>
</div>
<p><em>然后，设备将重置，要再次访问命令行控制系统，请按双回车键。</em></p>
</li>
<li><p>要配置 <span class="red-text">a tag</span>，使用 <span class="red-text">nmt</span> 命令将一个设备配置为 tag 模式。</p>
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
<li><p>要配置 <span class="red-text">带有启用时钟参考的锚点</span>，请使用 <span class="red-text">acs cr</span> 命令配置设备。</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ leaps&gt; acs cr 1
</pre></div>
</div>
</li>
<li><p><strong>然后，需要重置设备来更新配置</strong>. 使用 <span class="red-text">reset</span> 命令重置设备。</p></li>
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
<li><p>在本例中，我们将配置4锚点，每点之间相隔1米，呈正方形排列：</p></li>
</ul>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-3" name="sd-tab-set-1" type="radio">
<label class="sd-tab-label" for="sd-tab-item-3">
锚点 1 (启用启动器)</label><div class="sd-tab-content docutils">
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">leaps</span><span class="o">&gt;</span> <span class="n">ps</span> <span class="mi">1000</span> <span class="mi">1000</span> <span class="mi">0</span>
<span class="n">ps</span><span class="p">:</span> <span class="n">ok</span>
<span class="n">leaps</span><span class="o">&gt;</span> <span class="n">pg</span>
<span class="n">pg</span><span class="p">:</span> <span class="n">x</span><span class="p">:</span><span class="mi">1000</span> <span class="n">y</span><span class="p">:</span><span class="mi">0</span> <span class="n">z</span><span class="p">:</span><span class="mi">1000</span> <span class="n">qf</span><span class="p">:</span><span class="mi">100</span>
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
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">leaps</span><span class="o">&gt;</span> <span class="n">ps</span> <span class="mi">1000</span> <span class="mi">0</span> <span class="mi">0</span>
<span class="n">ps</span><span class="p">:</span> <span class="n">ok</span>
<span class="n">leaps</span><span class="o">&gt;</span> <span class="n">pg</span>
<span class="n">pg</span><span class="p">:</span> <span class="n">x</span><span class="p">:</span><span class="mi">1000</span> <span class="n">y</span><span class="p">:</span><span class="mi">0</span> <span class="n">z</span><span class="p">:</span><span class="mi">0</span> <span class="n">qf</span><span class="p">:</span><span class="mi">100</span>
<span class="n">leaps</span><span class="o">&gt;</span>
</pre></div>
</div>
</div>
<input id="sd-tab-item-6" name="sd-tab-set-1" type="radio">
<label class="sd-tab-label" for="sd-tab-item-6">
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
<li><p>此外，我们还可以使用 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> 来可视化设备及其位置。</p></li>
</ul>
<a class="reference internal image-reference" href="../../../_images/downlinktdoartlsdemo-anchors.jpeg"><img alt="../../../_images/downlinktdoartlsdemo-anchors.jpeg" class="align-center" src="/docs-assets/zh-cn/_images/downlinktdoartlsdemo-anchors.jpeg" style="width: 80%;"></a>
</div></blockquote>
<ol class="arabic simple" start="8">
<li><p>每个标签的配置允许使用 <span class="red-text">DL-TDoA</span> 技术进行测量。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>使用 <span class="red-text">tcs mode 2</span> 命令对标签进行配置。</p></li>
</ul>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ leaps&gt; tcs mode 2
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
<li><p>默认 <span class="red-text">normal update rate</span> 为 0.1s/ 10Hz，<span class="red-text">stationary update rate</span> 为 5.0s/ 0.2Hz. 要提高速度，请使用 <span class="red-text">urs</span> 命令。</p></li>
</ol>
<blockquote>
<div><p>例如，配置 <span class="red-text">正常更新率</span> 为 0.02s/ 50Hz，<span class="red-text">固定更新率</span> 为 0.02s/ 50Hz. 运行以下命令：</p>
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
<input checked="checked" id="sd-tab-item-7" name="sd-tab-set-2" type="radio">
<label class="sd-tab-label" for="sd-tab-item-7">
锚点 1 (启用启动器)</label><div class="sd-tab-content docutils">
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">mode:</span> <span class="pre">ani</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">panid=x1234</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prof=3</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cr=1</span></code></p></li>
</ul>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>leaps&gt; nps 3
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

leaps&gt; si
[000016.597 INF] release: LEAPS RTLS v0.15.0-ab84fb
[000016.597 INF] sys: main main_ver=x02000001 cfg_ver=x01040000 batt=none board=LC14_B
[000016.598 INF] uwb: ch9 prf64 plen128 pac8 txcode9 rxcode9 baud6800 phrmodeext phrratestd sfdtypeieee4a sfdto129 stsmodeoff stslen64 pdoamodem0
[000016.598 INF] uwb: tx_pwr=x34/xFAFAFAFA sts:shr:phr:data=27.7:27.7:27.7:27.7[dB] cpl=FCC/ETSI pgcnt=234 temp=25
[000016.599 INF] uwb: lna=1 pa=0 rf1=1 rf2=0 xtaltrim=27 tx_delay=16438 rx_delay=16438
[000016.599 INF] uwb: panid=x1234 addr=xDECA0E27530083A2
[000016.602 INF] mode: ani (act,real)
[000016.618 INF] uwbmac: connected prof=3 (manual)
[000016.618 INF] uwbmac: bh disconnected
[000016.618 INF] cfg: sync=0 fwup=1 ble=1 leds=1 init=1 uab=1 bh=auto bh_stat=off cr=1 upd_rate_stat=30 label=ID83A2
[000016.645 INF] enc: off
[000016.645 INF] ble: addr=F8:64:22:75:6C:F7
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
<li><p><code class="docutils literal notranslate"><span class="pre">prof=3</span></code></p></li>
</ul>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>leaps&gt; nps 3
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
[000005.559 INF] release: LEAPS RTLS v0.15.0-ab84fb
[000005.560 INF] sys: main main_ver=x02000001 cfg_ver=x01040000 batt=none board=LC14_B
[000005.560 INF] uwb: ch9 prf64 plen128 pac8 txcode9 rxcode9 baud6800 phrmodeext phrratestd sfdtypeieee4a sfdto129 stsmodeoff stslen64 pdoamodem0
[000005.560 INF] uwb: tx_pwr=x34/xE6E6E6E6 sts:shr:phr:data=25.8:25.8:25.8:25.8[dB] cpl=FCC/ETSI pgcnt=233 temp=25
[000005.561 INF] uwb: lna=1 pa=0 rf1=1 rf2=0 xtaltrim=32 tx_delay=16438 rx_delay=16438
[000005.561 INF] uwb: panid=x1234 addr=xDECA9DD29FD0CBBB
[000005.564 INF] mode: an (act,-)
[000005.580 INF] uwbmac: connected prof=3 (manual)
[000005.580 INF] uwbmac: bh disconnected
[000005.580 INF] cfg: sync=0 fwup=1 ble=1 leds=1 init=0 uab=1 bh=auto bh_stat=off cr=0 upd_rate_stat=30 label=IDCBBB
[000005.607 INF] enc: off
[000005.608 INF] ble: addr=E6:92:A3:6B:05:21
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
<li><p><code class="docutils literal notranslate"><span class="pre">prof=3</span></code></p></li>
</ul>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>leaps&gt; nps 3
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
[000011.647 INF] release: LEAPS RTLS v0.15.0-ab84fb
[000011.648 INF] sys: main main_ver=x02000001 cfg_ver=x01040000 batt=38%:1634mV:discharging board=LC14_B
[000011.648 INF] uwb: ch9 prf64 plen128 pac8 txcode9 rxcode9 baud6800 phrmodeext phrratestd sfdtypeieee4a sfdto129 stsmodeoff stslen64 pdoamodem0
[000011.648 INF] uwb: tx_pwr=x34/xEEEEEEEE sts:shr:phr:data=26.5:26.5:26.5:26.5[dB] cpl=FCC/ETSI pgcnt=245 temp=25
[000011.649 INF] uwb: lna=1 pa=0 rf1=1 rf2=0 xtaltrim=32 tx_delay=16436 rx_delay=16436
[000011.649 INF] uwb: panid=x1234 addr=xDECA7A20DFE04F2E
[000011.668 INF] mode: an (act,-)
[000011.668 INF] uwbmac: connected prof=3 (manual)
[000011.668 INF] uwbmac: bh disconnected
[000011.668 INF] cfg: sync=0 fwup=1 ble=1 leds=1 init=0 uab=1 bh=auto bh_stat=off cr=0 upd_rate_stat=30 label=ID4F2E
[000011.692 INF] enc: off
[000011.692 INF] ble: addr=C8:D9:F3:F1:7D:CE
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
<li><p><code class="docutils literal notranslate"><span class="pre">prof=2</span></code></p></li>
</ul>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>leaps&gt; nps 3
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
[000006.200 INF] release: LEAPS RTLS v0.15.0-ab84fb
[000006.200 INF] sys: main main_ver=x02000001 cfg_ver=x01040000 batt=none board=LC14_B
[000006.200 INF] uwb: ch9 prf64 plen128 pac8 txcode9 rxcode9 baud6800 phrmodeext phrratestd sfdtypeieee4a sfdto129 stsmodeoff stslen64 pdoamodem0
[000006.200 INF] uwb: tx_pwr=x34/xC6C6C6C6 sts:shr:phr:data=22.6:22.6:22.6:22.6[dB] cpl=FCC/ETSI pgcnt=236 temp=25
[000006.201 INF] uwb: lna=1 pa=0 rf1=1 rf2=0 xtaltrim=32 tx_delay=16431 rx_delay=16431
[000006.201 INF] uwb: panid=x1234 addr=xDECAED5BC8B1468D
[000006.205 INF] mode: an (act,-)
[000006.220 INF] uwbmac: connected prof=3 (manual)
[000006.220 INF] uwbmac: bh disconnected
[000006.220 INF] cfg: sync=0 fwup=1 ble=1 leds=1 init=0 uab=1 bh=auto bh_stat=off cr=0 upd_rate_stat=30 label=ID468D
[000006.249 INF] enc: off
[000006.249 INF] ble: addr=F3:D9:66:75:93:EB
leaps&gt;
</pre></div>
</div>
</div>
<input id="sd-tab-item-11" name="sd-tab-set-2" type="radio">
<label class="sd-tab-label" for="sd-tab-item-11">
标签</label><div class="sd-tab-content docutils">
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">mode:</span> <span class="pre">tn</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">panid=x1234</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prof=3</span></code></p></li>
</ul>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>leaps&gt; nps 3
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

leaps&gt; tcs mode 2
tcs: ok
leaps&gt; urs 1 1
urs: ok
leaps&gt; reset
reset ok


Low Energy Accurate Positioning System

FOR DEMO PURPOSE ONLY, NOT FOR SALE.

Copyright :  2016-2023 LEAPS
License   :  Please visit https://www.leapslabs.com/leaps-rtls-license
Compiled  :  Jan  6 2024 09:38:07 (v0.15.0-ab84fb)

Help      :  ? or help

leaps&gt; si
[000006.162 INF] release: LEAPS RTLS v0.15.0-ab84fb
[000006.162 INF] sys: main main_ver=x02000001 cfg_ver=x01040000 batt=none board=LC14_B
[000006.162 INF] uwb: ch9 prf64 plen128 pac8 txcode9 rxcode9 baud6800 phrmodeext phrratestd sfdtypeieee4a sfdto129 stsmodeoff stslen64 pdoamodem0
[000006.163 INF] uwb: tx_pwr=x34/xB6B6B6B6 sts:shr:phr:data=21.1:21.1:21.1:21.1[dB] cpl=FCC/ETSI pgcnt=231 temp=25
[000006.163 INF] uwb: lna=1 pa=0 rf1=1 rf2=0 xtaltrim=43 tx_delay=16434 rx_delay=16434
[000006.164 INF] uwb: panid=x1234 addr=xDECA80CB2C558A11
[000006.167 INF] mode: tn (act,rtdoa,np,le)
[000006.183 INF] uwbmac: connected prof=3 (manual)
[000006.183 INF] uwbmac: bh disconnected
[000006.183 INF] cfg: sync=0 fwup=1 ble=1 leds=1 le=1 lp=0 uab=1 stat_det=1 (sens=2) mode=2 upd_rate_norm=1 upd_rate_stat=1 label=ID8A11
[000006.210 INF] enc: off
[000006.211 INF] ble: addr=E8:BB:0A:C9:93:4E
leaps&gt;
</pre></div>
</div>
</div>
</div>
</div></blockquote>
<ol class="arabic simple" start="11">
<li><p>要查看当前连接到设备本身的锚点列表，请使用 <span class="red-text">la</span> 命令。 (可选)</p></li>
</ol>
<blockquote>
<div><p>例如在锚点 1 上（启用启动器）：</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">leaps</span><span class="o">&gt;</span> <span class="n">la</span>
<span class="p">[</span><span class="mf">000033.364</span> <span class="n">INF</span><span class="p">]</span> <span class="n">AN</span><span class="p">:</span> <span class="n">cnt</span><span class="o">=</span><span class="mi">4</span> <span class="n">seq</span><span class="o">=</span><span class="n">x03</span>
<span class="p">[</span><span class="mf">000033.364</span> <span class="n">INF</span><span class="p">]</span>     <span class="mi">0</span><span class="p">)</span> <span class="nb">id</span><span class="o">=</span><span class="mi">83</span><span class="n">A2</span> <span class="n">seat</span><span class="o">=</span><span class="mi">0</span> <span class="n">clk_lvl</span><span class="o">=</span><span class="mi">0</span> <span class="n">seens</span><span class="o">=</span><span class="mi">0</span> <span class="n">rssi</span><span class="o">=-</span><span class="mi">127</span> <span class="n">cl</span><span class="o">=</span><span class="mi">0000001</span><span class="n">D</span> <span class="n">nbr</span><span class="o">=</span><span class="mi">0000001</span><span class="n">D</span> <span class="n">pos</span><span class="o">=</span><span class="mf">1.00</span><span class="p">:</span><span class="mf">1.00</span><span class="p">:</span><span class="mf">0.00</span>
<span class="p">[</span><span class="mf">000033.364</span> <span class="n">INF</span><span class="p">]</span>     <span class="mi">1</span><span class="p">)</span> <span class="nb">id</span><span class="o">=</span><span class="mi">468</span><span class="n">D</span> <span class="n">seat</span><span class="o">=</span><span class="mi">4</span> <span class="n">clk_lvl</span><span class="o">=</span><span class="mi">1</span> <span class="n">seens</span><span class="o">=</span><span class="mi">235</span> <span class="n">rssi</span><span class="o">=-</span><span class="mi">55</span> <span class="n">cl</span><span class="o">=</span><span class="mi">0000001</span><span class="n">D</span> <span class="n">nbr</span><span class="o">=</span><span class="mi">00000000</span> <span class="n">pos</span><span class="o">=</span><span class="mf">0.00</span><span class="p">:</span><span class="mf">1.00</span><span class="p">:</span><span class="mf">0.00</span>
<span class="p">[</span><span class="mf">000033.365</span> <span class="n">INF</span><span class="p">]</span>     <span class="mi">2</span><span class="p">)</span> <span class="nb">id</span><span class="o">=</span><span class="mi">4</span><span class="n">F2E</span> <span class="n">seat</span><span class="o">=</span><span class="mi">2</span> <span class="n">clk_lvl</span><span class="o">=</span><span class="mi">1</span> <span class="n">seens</span><span class="o">=</span><span class="mi">193</span> <span class="n">rssi</span><span class="o">=-</span><span class="mi">55</span> <span class="n">cl</span><span class="o">=</span><span class="mi">0000001</span><span class="n">D</span> <span class="n">nbr</span><span class="o">=</span><span class="mi">00000000</span> <span class="n">pos</span><span class="o">=</span><span class="mf">1.00</span><span class="p">:</span><span class="mf">0.00</span><span class="p">:</span><span class="mf">0.00</span>
<span class="p">[</span><span class="mf">000033.365</span> <span class="n">INF</span><span class="p">]</span>     <span class="mi">3</span><span class="p">)</span> <span class="nb">id</span><span class="o">=</span><span class="n">CBBB</span> <span class="n">seat</span><span class="o">=</span><span class="mi">3</span> <span class="n">clk_lvl</span><span class="o">=</span><span class="mi">1</span> <span class="n">seens</span><span class="o">=</span><span class="mi">6</span> <span class="n">rssi</span><span class="o">=-</span><span class="mi">55</span> <span class="n">cl</span><span class="o">=</span><span class="mi">0000001</span><span class="n">D</span> <span class="n">nbr</span><span class="o">=</span><span class="mi">00000000</span> <span class="n">pos</span><span class="o">=</span><span class="mf">0.00</span><span class="p">:</span><span class="mf">0.00</span><span class="p">:</span><span class="mf">0.00</span>
<span class="p">[</span><span class="mf">000033.366</span> <span class="n">INF</span><span class="p">]</span>
</pre></div>
</div>
</div></blockquote>
<p>现在系统已经成功设置和配置。 祝您使用愉快！</p>
</div>
<input id="sd-tab-item-2" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-2">
故障排除</label><div class="sd-tab-content docutils">
<ol class="arabic">
<li><p>当低功耗Bluetooth (BLE) 和 LED 同时熄灭时，用户可能会错误地认为电路板无法运作。 在这种情况下，用户唯一的办法就是启动出厂重置（<a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/shell-api/sys#frst"><span class="std std-ref">frst</span></a>）命令。</p></li>
<li><p>这里有一些解决安装过程中相关问题的提示。</p>
<ul class="simple">
<li><p>请检查版本. 我们建议您使用最新的官方版本。</p></li>
<li><p>当您不知道设备的当前状态时，请使用 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> 演示选择器中的 <span class="red-text">Reset devices to default</span> 功能. 请参考下面的 GIF 图片。</p></li>
</ul>
<img alt="../../../_images/reset-devices-to-defaul-x2.gif" class="align-center" src="/docs-assets/zh-cn/_images/reset-devices-to-defaul-x2.gif">
</li>
</ol>
</div>
</div>
<div class="admonition note">
<p class="admonition-title">注解</p>
<ul class="simple">
<li><p>高速下行 TDoA RTLS Demo 位置数据将通过另一个通信通道发送。</p></li>
<li><p>如果您对我们的产品有任何意见或问题，请访问我们的 <a class="reference external" href="https://forum.leapslabs.com">LEAPS 论坛</a>。</p></li>
<li><p>有关已知限制和问题列表的详情，请参阅 <a class="reference internal" href="/docs/zh/udk/release#udk-releases"><span class="std std-ref">发布</span></a> 部分。</p></li>
</ul>
</div>
</div>


           </div>
