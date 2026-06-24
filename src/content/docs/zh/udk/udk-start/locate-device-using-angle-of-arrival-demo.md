---
title: "使用到达角(AoA)定位设备演示"
lang: zh
slug: "udk/udk-start/locate-device-using-angle-of-arrival-demo"
section: "udk"
sourceUrl: "https://docs.leapslabs.com/zh-cn/udk/udk-start/locate-device-using-angle-of-arrival-demo/"
order: 84
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="locate-device-using-angle-of-arrival-aoa-demo">
<span id="anchor-lc"></span><h1>使用到达角(AoA)定位设备演示</h1>
<a class="reference internal image-reference" href="../../../_images/locate_device_using_angle-of-arrival_demo.png"><img alt="../../../_images/locate_device_using_angle-of-arrival_demo.png" class="align-right" src="/docs-assets/zh-cn/_images/locate_device_using_angle-of-arrival_demo.png" style="width: 216.0px; height: 245.88px;"></a>
<p><strong>准备设置</strong></p>
<ol class="arabic simple">
<li><p><a class="reference internal" href="/docs/zh/udk/udk-start/partner-application-aoa-app#anchor-ranging-aoa"><span class="std std-ref">UWB 测距与 AoA 演示应用程序</span></a> 桌面程序已安装在您的计算机上。</p></li>
<li><p>一个 LC13 (灰色) 设备和至少一个 LC14 (白色) 设备。</p></li>
<li><p>用于连接设备的 USB-C 数据线。</p></li>
<li><p><em>可选:</em> <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> <em>已安装应用程序。</em></p></li>
<li><p><em>可选:应答器设备的电池。</em></p></li>
</ol>
<p><strong>设置时间：</strong> 少于 5 分钟</p>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-0" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-0">
快速启动</label><div class="sd-tab-content docutils">
<p><strong>概览</strong></p>
<p>此设置展示了 <span class="red-text">FiRa设备</span> 之间的兼容性。 在桌面应用程序中，距离和角度测量显示了启动器和应答器设备之间的方向。</p>
<p><strong>典型应用</strong>:门禁控制, 跟踪, 定位和追踪室内环境中的物体或设备。</p>
<p><strong>设置说明</strong></p>
<ol class="arabic simple">
<li><p>下载并在您的电脑上安装应用程序。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>详情请参阅 <a class="reference internal" href="/docs/zh/udk/udk-start/partner-application-aoa-app#anchor-ranging-aoa"><span class="std std-ref">UWB 测距与 AoA 演示应用程序</span></a> 安装说明。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="2">
<li><p>为LC13和LC14设备 <span class="red-text">ON</span> 供电。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>在此演示中，LC13将作为启动器，而LC14将作为响应器。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="3">
<li><p>使用以下选项之一，将设备配置为 <span class="red-text">Qorvo UCI模式</span>:</p></li>
</ol>
<blockquote>
<div><ol class="upperalpha simple">
<li><p>使用按钮配置设备。</p></li>
</ol>
<blockquote>
<div><p>3.1. 按住 <a class="reference internal" href="/docs/zh/udk/udk-start/device-hw-interfaces#uihwinterfaces"><span class="std std-ref">Button B</span></a>，直到听到哔哔声，并且 <span class="green-text">GREEN LED</span> 闪烁。</p>
<p>3.2. 如果出现 <span class="red-text">RED</span> 或 <span class="blue-text">BLUE</span> 颜色，请重复步骤 a。</p>
<p>3.3. 当设备在哔声后闪烁 <span class="green-text">GREEN LED</span> 时，设备被配置为 <span class="red-text">Qorvo UCI mode</span>。</p>
<img alt="../../../_images/leaps-config-to-qorvo-uci-mode.gif" class="align-center" src="/docs-assets/zh-cn/_images/leaps-config-to-qorvo-uci-mode.gif">
</div></blockquote>
<ol class="upperalpha simple" start="2">
<li><p>使用 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> 中的演示选择器进行配置。</p></li>
</ol>
<blockquote>
<div><p>3.1. 打开 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> 并从主页选择 <span class="red-text">Demo Selector</span>。</p>
<p>3.2. 选择 <span class="red-text">使用到达角定位设备</span>。</p>
<p>3.3。 通过Bluetooth发现的设备列表会出现在列表中。 如果需要，向下滑动来更新列表。</p>
<p>3.4. 选择用于演示的设备. 顶部的 <span class="red-text">Required devices</span> 表示演示所需的设备数量。</p>
<p>3.5. 按下 <span class="red-text">SAVE</span> 将设备配置为 <span class="red-text">Qorvo UCI模式</span>。</p>
<p>3.6. 请目测设备启动时 <span class="green-text">GREEN LED</span> 是否闪烁。</p>
<img alt="../../../_images/qorvo-uwb-ranging-aoa.gif" class="align-center" src="/docs-assets/zh-cn/_images/qorvo-uwb-ranging-aoa.gif">
</div></blockquote>
</div></blockquote>
<ol class="arabic" start="4">
<li><p>使用USB-C数据线连接设备，并使用 <a class="reference internal" href="/docs/zh/udk/udk-start/device-hw-interfaces#hardware-interface"><span class="std std-ref">USB-C Data Port 1</span></a> 连接 PC。</p>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/connect-uwbrangingaoa-002.jpg"><img alt="../../../_images/connect-uwbrangingaoa-002.jpg" src="/docs-assets/zh-cn/_images/connect-uwbrangingaoa-002.jpg" style="width: 98%;"></a>
</div></blockquote>
</li>
</ol>
<blockquote>
<div><p><em>可选:如果您希望在启动演示程序后，将设备与电脑断开连接，以便自由移动，请将电池插入应答器设备</em>。</p>
</div></blockquote>
<ol class="arabic" start="5">
<li><p>在桌面上打开 <span class="red-text">UWB Ranging &amp; AoA Demo App</span>，点击 <span class="red-text">Next</span> 进入设备列表。</p>
<ul class="simple">
<li><p>USB 连接的设备将会出现在设备列表中，这可能需要几秒钟的时间。 查看列表并确定你要使用的设备。 默认情况下，所有通过 USB 发现的设备都会被选中。</p></li>
<li><p>如果需要，可以更改每个设备或 <span class="red-text">Fira Configuration</span> 的附加配置. 默认值应该可以正常工作。</p></li>
</ul>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/uwb_ranging_and_aoa_demo_app_main.png"><img alt="../../../_images/uwb_ranging_and_aoa_demo_app_main.png" src="/docs-assets/zh-cn/_images/uwb_ranging_and_aoa_demo_app_main.png" style="width: 98%;"></a>
</div></blockquote>
</li>
<li><p>按下 <span class="red-text">Save and start</span> 开始演示. 下面的 <span class="red-text">Real Time Location</span> 窗口会显示一个坐标地图，上面有选定的启动器和响应器之间的距离和角度。</p>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/uwb_ranging_and_aoa_demo_app_location.png"><img alt="../../../_images/uwb_ranging_and_aoa_demo_app_location.png" src="/docs-assets/zh-cn/_images/uwb_ranging_and_aoa_demo_app_location.png" style="width: 98%;"></a>
</div></blockquote>
</li>
<li><p>如果使用电池供电，可以将应答器设备从 PC 拔下. 这将允许为评估目的而自由移动应答器. 设备需要使用 <a class="reference internal" href="/docs/zh/udk/udk-start/device-hw-interfaces#hardware-interface"><span class="std std-ref">USB-C Data Port 1</span></a> 重新插入 PC，才能再次启动会话。</p></li>
</ol>
<blockquote>
<div><img alt="../../../_images/leaps-connect-usb-port1.gif" class="align-center" src="/docs-assets/zh-cn/_images/leaps-connect-usb-port1.gif">
</div></blockquote>
<ol class="arabic simple" start="8">
<li><p>UWB Ranging &amp; AoA Demo App提供多种有用的评估选项，包括</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>显示距离, 角度和X-Y位置的实时定位。</p></li>
<li><p>随时间变化的趋势，实时显示距离和角度值。</p></li>
<li><p>定位我的设备，显示从启动器到所选响应器的方向。</p></li>
<li><p>地理围栏</p></li>
<li><p>平面图</p></li>
<li><p>网格</p></li>
<li><p>记录</p></li>
</ul>
</div></blockquote>
<p>详情请参考 <a class="reference internal" href="/docs/zh/udk/udk-start/partner-application-aoa-app#anchor-ranging-aoa"><span class="std std-ref">UWB 测距与 AoA 演示应用程序</span></a>。</p>
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
<li><p>使用 <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/shell-api/fira#fuci"><span class="std std-ref">fuci</span></a> 命令更新 FiRa UCI 模式。</p></li>
</ol>
<blockquote>
<div><div class="highlight-default notranslate"><div class="highlight"><pre><span></span>Low Energy Accurate Positioning System

FOR DEMO PURPOSE ONLY, NOT FOR SALE.

Copyright :  2016-2023 LEAPS
License   :  Please visit https://www.leapslabs.com/leaps-rtls-license
Compiled  :  Jan  6 2024 09:38:07 (v0.15.0-ab84fb)

Help      :  ? or help

leaps&gt;
leaps&gt; fuci
</pre></div>
</div>
<p>请目测设备启动时 <span class="green-text">GREEN LED</span> 是否闪烁。</p>
<img alt="../../../_images/fuci-command.gif" class="align-center" src="/docs-assets/zh-cn/_images/fuci-command.gif">
</div></blockquote>
<ol class="arabic simple" start="5">
<li><p>现在成功配置 <span class="red-text">Qorvo UCI mode</span> 请参考以下步骤 <a class="reference internal" href="#anchor-lc"><span class="std std-ref">Quick Start</span></a>。</p></li>
</ol>
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
<li><p>如果您对我们的产品有任何意见或问题，请访问我们的 <a class="reference external" href="https://forum.leapslabs.com">LEAPS论坛</a>。</p></li>
<li><p>有关已知限制和问题列表的详情，请参阅 <a class="reference internal" href="/docs/zh/udk/release#udk-releases"><span class="std std-ref">发布</span></a> 部分。</p></li>
</ul>
</div>
</div>


           </div>
