---
title: "与 iPhone 的附近交互演示"
lang: zh
slug: "udk/udk-start/nearby-interaction-demo-with-an-iphone"
section: "udk"
sourceUrl: "https://docs.leapslabs.com/zh-cn/udk/udk-start/nearby-interaction-demo-with-an-iphone/"
order: 107
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="nearby-interaction-demo-with-an-iphone">
<span id="anchor-ni"></span><h1>与 iPhone 的附近交互演示</h1>
<a class="reference internal image-reference" href="../../../_images/nearby_interaction_demo_with_an_iphone.png"><img alt="../../../_images/nearby_interaction_demo_with_an_iphone.png" class="align-right" src="/docs-assets/zh-cn/_images/nearby_interaction_demo_with_an_iphone.png" style="width: 252.00000000000003px; height: 211.26000000000002px;"></a>
<p><strong>准备设置</strong></p>
<ol class="arabic simple">
<li><p><a class="reference internal" href="/docs/zh/udk/udk-start/partner-application-nearby-interaction#anchor-ni-app"><span class="std std-ref">Qorvo 附近的互动</span></a> （前景模式）或 <a class="reference internal" href="/docs/zh/udk/udk-start/partner-application-nearby-interaction-background#anchor-nib-app"><span class="std std-ref">Qorvo NI 背景</span></a> 应用程序已安装在 iPhone 上（型号:iPhone 11, 12 和 13）。</p></li>
<li><p>至少一个 LC14 (白色) 设备。</p></li>
<li><p><em>可选:</em> <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> <em>已安装应用程序。</em></p></li>
<li><p><em>可选:设备电池。</em></p></li>
</ol>
<p><strong>设置时间：</strong> 少于 5 分钟</p>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-0" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-0">
快速入门</label><div class="sd-tab-content docutils">
<p><strong>概览</strong></p>
<p>此设置展示了 <span class="red-text">近距离交互</span> 和 <span class="red-text">FiRa 与智能</span> 手机的兼容性. 距离和角度测量可在智能手机应用中显示配件的方向。</p>
<p><strong>典型应用</strong>:查找我的物品, 跟随我, 智能遥控, 门禁控制。</p>
<p><strong>设置说明</strong></p>
<ol class="arabic simple">
<li><p>在 iPhone 上下载并安装以下应用程序。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p><a class="reference internal" href="/docs/zh/udk/udk-start/partner-application-nearby-interaction#anchor-ni-app"><span class="std std-ref">Qorvo 附近的互动</span></a> 应用程序（前台模式）。</p></li>
<li><p><a class="reference internal" href="/docs/zh/udk/udk-start/partner-application-nearby-interaction-background#anchor-nib-app"><span class="std std-ref">Qorvo NI 背景</span></a> 应用程序（后台模式）。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="2">
<li><p>电源 <span class="red-text">ON</span> 一个或多个 LC14 (白色) 设备。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>LC14 (多个) 将在 QNI (Qorvo 附近互动) 演示中充当配件。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="3">
<li><p>使用下列选项之一，将设备配置为 <span class="red-text">QNI mode模式</span>：</p></li>
</ol>
<blockquote>
<div><ol class="upperalpha simple">
<li><p>使用按钮配置设备。</p></li>
</ol>
<blockquote>
<div><p>3.1. 按住 <a class="reference internal" href="/docs/zh/udk/udk-start/device-hw-interfaces#uihwinterfaces"><span class="std std-ref">Button B</span></a> 直到听到哔哔声，并且 <span class="blue-text">BLUE LED</span> 闪烁。</p>
<p>3.2. 如果出现 <span class="red-text">RED</span> 或 <span class="green-text">GREEN</span> 颜色，请重复步骤 a。</p>
<p>3.3. 当设备在哔声后闪烁 <span class="blue-text">BLUE LED</span> 时，设备被配置为 <span class="red-text">QNI 模式</span>。</p>
<img alt="../../../_images/leaps-config-to-qorvo-ni-mode.gif" class="align-center" src="/docs-assets/zh-cn/_images/leaps-config-to-qorvo-ni-mode.gif">
</div></blockquote>
<ol class="upperalpha simple" start="2">
<li><p>使用 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> 中的演示选择器进行配置。</p></li>
</ol>
<blockquote>
<div><p>3.1. 打开 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> 并从主页选择 <span class="red-text">Demo Selector</span>。</p>
<p>3.2. 选择 <span class="red-text">与iPhone的近距离互动</span>。</p>
<p>3.3. 通过Bluetooth发现的设备列表将出现在列表中. 如果需要，向下滑动即可更新列表。</p>
<p>3.4. 选择用于 QNI 演示的设备. 顶部的 <span class="red-text">Required devices</span> 表示演示所需的设备数量。</p>
<p>3.5. 按下 <span class="red-text">SAVE</span> 将设备配置到 <span class="red-text">QNI模式</span>。</p>
<p>3.6. 请目测设备启动时 <span class="blue-text">BLUE LED</span> 是否闪烁。</p>
<img alt="../../../_images/qorvo-nearby-interaction.gif" class="align-center" src="/docs-assets/zh-cn/_images/qorvo-nearby-interaction.gif">
</div></blockquote>
</div></blockquote>
<ol class="arabic simple" start="4">
<li><p>在iPhone上打开 <span class="red-text">Qorvo Nearby Interaction</span> 或 <span class="red-text">QorvoNIBackground</span> 应用程序。</p></li>
</ol>
<blockquote>
<div><ul>
<li><p>打开 Qorvo Nearby Interaction 应用程序后，它会立即使用 QNI BLE 服务扫描附近的配件。</p></li>
<li><p>当找到QNI配件并将其添加到列表中时。 请 <span class="red-text">选择并连接</span> 到您要开始附近互动的配件。 支持多个连接。</p>
<img alt="../../../_images/nearby-interaction-demo.gif" class="align-center" src="/docs-assets/zh-cn/_images/nearby-interaction-demo.gif">
</li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="5">
<li><p><span class="red-text">近距离交互背景模式</span> 要求配件与iPhone设备配对。</p></li>
</ol>
<blockquote>
<div><ul>
<li><p>当首次与设备连接时，以及当应用程序首次启动 NI 会话时，它会请求用户批准使用附近的交互。</p></li>
<li><p>一旦配件与 iPhone 配对成功，在配件与 iPhone 之间的未来互动中，就不再需要配对和权限访问。</p>
<a class="reference internal image-reference" href="../../../_images/qorvo_ni_pair_request_demo.png"><img alt="../../../_images/qorvo_ni_pair_request_demo.png" src="/docs-assets/zh-cn/_images/qorvo_ni_pair_request_demo.png" style="width: 49%;"></a>
<a class="reference internal image-reference" href="../../../_images/qorvo_ni_background_pair_request_demo.jpg"><img alt="../../../_images/qorvo_ni_background_pair_request_demo.jpg" src="/docs-assets/zh-cn/_images/qorvo_ni_background_pair_request_demo.jpg" style="width: 49%;"></a>
</li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="6">
<li><p>iPhone 将开始与配件进行测距，并在每一轮测距后显示 iPhone 与配件之间的测量距离。</p></li>
</ol>
<blockquote>
<div><ul>
<li><p>在 <span class="red-text">Qorvo NI Background</span> 应用程序使用 <span class="red-text">NI Background</span> 模式的情况下，更新率会比 NI Foreground 模式低 1/3. 即使 iPhone 的显示屏关闭，也会在后台进行测距。</p></li>
<li><p>在 <span class="red-text">Qorvo Nearby Interaction</span> 应用程序使用 <span class="red-text">NI Foreground</span> 模式的情况下，还将显示从 iPhone 到配件的角度和方向. 测量值是从 iPhone 的角度测量的. 当你改变设备的方向时，应用程序还可以提供一个增强视图，利用 iPhone 的摄像头和显示屏来定位配件。</p>
<a class="reference internal image-reference" href="../../../_images/qorvo_nearby_interaction_application_example.png"><img alt="../../../_images/qorvo_nearby_interaction_application_example.png" src="/docs-assets/zh-cn/_images/qorvo_nearby_interaction_application_example.png" style="width: 49%;"></a>
<a class="reference internal image-reference" href="../../../_images/qorvo_ni_backgroud_example.jpg"><img alt="../../../_images/qorvo_ni_backgroud_example.jpg" src="/docs-assets/zh-cn/_images/qorvo_ni_backgroud_example.jpg" style="width: 49%;"></a>
</li>
</ul>
</div></blockquote>
<p>更多详情，请参阅 <a class="reference internal" href="/docs/zh/udk/udk-start/partner-application-nearby-interaction#anchor-ni-app"><span class="std std-ref">Qorvo 附近的互动</span></a> 或 <a class="reference internal" href="/docs/zh/udk/udk-start/partner-application-nearby-interaction-background#anchor-nib-app"><span class="std std-ref">Qorvo NI 背景</span></a> 应用程序。</p>
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
<div><img alt="../../../_images/leaps-connect-usb-port2.gif" class="align-center" src="/docs-assets/zh-cn/_images/leaps-connect-usb-port2.gif">
</div></blockquote>
<ol class="arabic simple" start="2">
<li><p>使用你想要的终端应用程序，如 Putty, Teraterm, Minicom 或你最喜欢的终端应用程序，连接到串行端口. 我们需要将波特率设置为 <span class="red-text">115200</span>。</p></li>
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
<li><p>使用 <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/shell-api/fira#fniq"><span class="std std-ref">fniq</span></a> 命令更新附近交互模式。</p></li>
</ol>
<blockquote>
<div><div class="highlight-default notranslate"><div class="highlight"><pre><span></span>Low Energy Accurate Positioning System

FOR DEMO PURPOSE ONLY, NOT FOR SALE.

Copyright :  2016-2023 LEAPS
License   :  Please visit https://www.leapslabs.com/leaps-rtls-license
Compiled  :  Jan  6 2024 09:38:07 (v0.15.0-ab84fb)

Help      :  ? or help

leaps&gt;
leaps&gt; fniq
</pre></div>
</div>
<p>届时，请目测设备启动时 <span class="blue-text">BLUE LED</span> 是否闪烁。</p>
<img alt="../../../_images/fniq-command.gif" class="align-center" src="/docs-assets/zh-cn/_images/fniq-command.gif">
</div></blockquote>
<ol class="arabic simple" start="5">
<li><p>现在成功配置了 <span class="red-text">QNI 模式</span>，请参考接下来的 <a class="reference internal" href="#anchor-ni"><span class="std std-ref">Quick Start</span></a> 步骤。</p></li>
</ol>
</div>
<input id="sd-tab-item-2" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-2">
故障排除</label><div class="sd-tab-content docutils">
<ol class="arabic">
<li><p>当低功耗Bluetooth (BLE) 和 LED 同时熄灭时，用户可能会错误地认为电路板无法运作。 在这种情况下，用户唯一的办法就是启动出厂重置（<a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/shell-api/sys#frst"><span class="std std-ref">frst</span></a>）命令。</p></li>
<li><p>以下是一些修复与安装过程有关的问题的提示</p>
<ul class="simple">
<li><p>请检查版本. 我们建议您使用最新的官方版本。</p></li>
<li><p>当你不知道设备的当前状态时，请使用 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> 演示选择器中的 <span class="red-text">Reset devices to default</span> 功能. 请参考下面的 GIF 图片。</p></li>
</ul>
<img alt="../../../_images/reset-devices-to-defaul-x2.gif" class="align-center" src="/docs-assets/zh-cn/_images/reset-devices-to-defaul-x2.gif">
</li>
</ol>
</div>
</div>
<div class="admonition note">
<p class="admonition-title">注解</p>
<ul class="simple">
<li><p>如果您对我们的产品有任何意见或问题，请访问我们的 <a class="reference external" href="https://forum.leapslabs.com">LEAPS 论坛</a>。</p></li>
<li><p>有关已知限制和问题列表的详情，请参阅 <a class="reference internal" href="/docs/zh/udk/release#udk-releases"><span class="std std-ref">发布</span></a> 部分。</p></li>
</ul>
</div>
</div>


           </div>
