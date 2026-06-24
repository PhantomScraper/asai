---
title: "PANS PRO 演示"
lang: zh
slug: "pans-pro-rtls/quick-start-guide/panspro-rtls-setup"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/pans-pro-rtls/quick-start-guide/panspro-rtls-setup/"
order: 88
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="pans-pro-demo">
<span id="id1"></span><h1>PANS PRO 演示</h1>
<p><strong>准备设置</strong></p>
<img alt="../../../_images/qsg_set_up.png" class="align-center" src="/docs-assets/zh-cn/_images/qsg_set_up.png">
<ol class="arabic simple">
<li><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/infrastructure/pans-pro-manager#pans-pro-manager"><span class="std std-ref">PANS PRO Manager</span></a> 应用程序已安装在 Android 设备上。</p></li>
<li><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/infrastructure/leaps-center#pans-pro-center"><span class="std std-ref">LEAPS Center</span></a> 应用程序安装在 PC 上。</p></li>
<li><p>至少四个 LC4 设备（锚节点）和一个 LC8 设备（标签节点）。</p></li>
<li><p>一个 LC5 设备（网关节点）。</p></li>
<li><p>为设备供电的电池或微型 USB 电缆。</p></li>
<li><p><em>推荐</em>: 夹子或带相机固定架的三脚架，用于固定主播设备。</p></li>
<li><p><em>推荐</em>： 一台 Raspberry Pi 3B 或更新版本，或者一台 PC, 数据服务器和网络应用程序安装。</p></li>
<li><p><em>可选</em>: 电脑上安装 Putty, Teraterm, minicom 或你喜欢的终端应用程序。</p></li>
</ol>
<p><strong>设置时间：</strong> 少于 5 分钟</p>
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-3 sd-row-cols-xs-3 sd-row-cols-sm-3 sd-row-cols-md-3 sd-row-cols-lg-3 docutils">
<div class="sd-col sd-d-flex-row docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm sd-card-hover sd-text-center custom-card docutils">
<div class="sd-card-body docutils">
<a class="reference internal image-reference" href="../../../_images/lc4a_front_view.png"><img alt="../../../_images/lc4a_front_view.png" src="/docs-assets/zh-cn/_images/lc4a_front_view.png" style="width: 131.76px; height: 189.26999999999998px;"></a>
<p class="sd-card-text"><span class="red-text">LC4 设备</span></p>
</div>
<a class="sd-stretched-link reference internal" href="/docs/zh/pans-pro-rtls/specification/lc4a-specification#lc4a-specification"><span class="std std-ref"></span></a></div>
</div>
<div class="sd-col sd-d-flex-row docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm sd-card-hover sd-text-center custom-card docutils">
<div class="sd-card-body docutils">
<a class="reference internal image-reference" href="../../../_images/lc5.png"><img alt="../../../_images/lc5.png" src="/docs-assets/zh-cn/_images/lc5.png" style="width: 204.8px; height: 184.8px;"></a>
<p class="sd-card-text"><span class="red-text">LC5 设备</span></p>
</div>
<a class="sd-stretched-link reference internal" href="/docs/zh/pans-pro-rtls/specification/lc5a-specification#lc5a-specification"><span class="std std-ref"></span></a></div>
</div>
<div class="sd-col sd-d-flex-row docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm sd-card-hover sd-text-center custom-card docutils">
<div class="sd-card-body docutils">
<a class="reference internal image-reference" href="../../../_images/lc8.png"><img alt="../../../_images/lc8.png" src="/docs-assets/zh-cn/_images/lc8.png" style="width: 117.2px; height: 182.0px;"></a>
<p class="sd-card-text"><span class="red-text">LC8 设备</span></p>
</div>
<a class="sd-stretched-link reference internal" href="/docs/zh/pans-pro-rtls/specification/lc8a-specification#lc8a-specification"><span class="std std-ref"></span></a></div>
</div>
</div>
</div>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-0" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-0">
电话快速入门</label><div class="sd-tab-content docutils">
<p><strong>概览</strong></p>
<p>这个设置演示了使用 <span class="red-text">Two Way Ranging (TWR)</span> 技术进行实时导航, 跟踪和双向数据遥测。</p>
<p><strong>典型应用</strong>： 室内导航, 资产追踪，以及支持上下行链路的实时数据遥测。</p>
<p><strong>设置说明</strong></p>
<ol class="arabic">
<li><p>开启已刷新最新固件的设备。</p>
<ul class="simple">
<li><p>静态安装的设备将作为锚点，为标签提供位置信息。</p></li>
<li><p>移动设备将作为双向测距模式下配置的标签。</p></li>
</ul>
</li>
<li><p>请参阅 <a class="reference internal" href="/docs/zh/pans-pro-rtls/infrastructure/pans-pro-manager#pans-pro-manager"><span class="std std-ref">PANS PRO Manager</span></a> 部分的详细指南. 以下是快速步骤。</p>
<p>2.1. 使用用户名 <code class="docutils literal notranslate"><span class="pre">admin</span></code> 和密码 <code class="docutils literal notranslate"><span class="pre">admin</span></code> 登录。</p>
<p>2.2. 登录成功后，点击主页上的 <code class="docutils literal notranslate"><span class="pre">Start</span> <span class="pre">Device</span> <span class="pre">Discovery</span></code> 功能。</p>
<p>2.3。 将发现的设备分配到网络。 输入一个网络名称，继续并将所有设备分配到这个网络。</p>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/ppm-home-page.jpg"><img alt="../../../_images/ppm-home-page.jpg" src="/docs-assets/zh-cn/_images/ppm-home-page.jpg" style="width: 32%;"></a>
<a class="reference internal image-reference" href="../../../_images/ppm-assign-network6.jpg"><img alt="../../../_images/ppm-assign-network6.jpg" src="/docs-assets/zh-cn/_images/ppm-assign-network6.jpg" style="width: 32%;"></a>
<a class="reference internal image-reference" href="../../../_images/ppm-network-1.jpg"><img alt="../../../_images/ppm-network-1.jpg" src="/docs-assets/zh-cn/_images/ppm-network-1.jpg" style="width: 32%;"></a>
</div></blockquote>
<p>2.4。 将其中一个被发现的设备配置为启动器锚点 (ANI)，并启用启动器模式。</p>
<p>2.5。 将三个被发现的设备配置为锚节点 (AN)，但不启用启动器模式。</p>
<p>2.6. 有了四个锚节点 (AN)，你可以手动配置位置。</p>
<blockquote>
<div><ul class="simple">
<li><p>请在 <a class="reference internal" href="/docs/zh/pans-pro-rtls/infrastructure/pans-pro-manager#pans-pro-manager"><span class="std std-ref">PANS PRO Manager</span></a> 中查看自动定位功能，以轻松放置锚点。</p></li>
</ul>
</div></blockquote>
<p>2.7。 将一个设备配置为标签节点 (TN)，并使用默认的 <code class="docutils literal notranslate"><span class="pre">NORMAL</span> <span class="pre">UPDATE</span> <span class="pre">RATE</span></code> 和 <code class="docutils literal notranslate"><span class="pre">STATIONARY</span> <span class="pre">UPDATE</span> <span class="pre">RATE</span></code>。</p>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/ppm-device-configure-b.jpg"><img alt="../../../_images/ppm-device-configure-b.jpg" src="/docs-assets/zh-cn/_images/ppm-device-configure-b.jpg" style="width: 32%;"></a>
<a class="reference internal image-reference" href="../../../_images/anchor-initiator-node-disable.png"><img alt="../../../_images/anchor-initiator-node-disable.png" src="/docs-assets/zh-cn/_images/anchor-initiator-node-disable.png" style="width: 32%;"></a>
<a class="reference internal image-reference" href="../../../_images/ppm-device-configure-a.jpg"><img alt="../../../_images/ppm-device-configure-a.jpg" src="/docs-assets/zh-cn/_images/ppm-device-configure-a.jpg" style="width: 32%;"></a>
</div></blockquote>
<p>2.8. 完成发现和配置后，网络可视化可以在 <a class="reference internal" href="/docs/zh/pans-pro-rtls/infrastructure/pans-pro-manager#pans-pro-manager"><span class="std std-ref">PANS PRO Manager</span></a> 应用程序上以 2D 网格或 3D 网格显示。</p>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/ppm-grib-2d-0.jpg"><img alt="../../../_images/ppm-grib-2d-0.jpg" src="/docs-assets/zh-cn/_images/ppm-grib-2d-0.jpg" style="width: 40%;"></a>
<a class="reference internal image-reference" href="../../../_images/ppm-grib-3d-0.jpg"><img alt="../../../_images/ppm-grib-3d-0.jpg" src="/docs-assets/zh-cn/_images/ppm-grib-3d-0.jpg" style="width: 40%;"></a>
</div></blockquote>
</li>
</ol>
</div>
<input id="sd-tab-item-1" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-1">
网络快速入门</label><div class="sd-tab-content docutils">
<p><strong>概览</strong></p>
<p>本节将指导如何设置 PANS PRO RTLS 网络，以便在 <a class="reference internal" href="/docs/zh/pans-pro-rtls/infrastructure/leaps-center#pans-pro-center"><span class="std std-ref">LEAPS Center</span></a> 上显示. 为了成功设置 PANS PRO RTLS 网络，请确保必要的硬件和软件。</p>
<p><strong>说明</strong>：</p>
<ol class="arabic">
<li><p>准备网络：</p>
<ul class="simple">
<li><p>使用 <code class="docutils literal notranslate"><span class="pre">PANS</span> <span class="pre">PRO</span> <span class="pre">Manage</span></code> 中的 <code class="docutils literal notranslate"><span class="pre">电话快速入门</span></code> 选项卡所描述的配置来配置网络。</p></li>
</ul>
</li>
<li><p>设置网关板： 使用 <code class="docutils literal notranslate"><span class="pre">PANS</span> <span class="pre">PRO</span> <span class="pre">Docker</span></code> 或 <code class="docutils literal notranslate"><span class="pre">PANS</span> <span class="pre">PRO</span> <span class="pre">Raspberry</span> <span class="pre">Pi</span></code>。</p>
<ul class="simple">
<li><p><cite>注意：如果板子上还没有最新的固件，请刷新最新的固件</cite>。</p></li>
</ul>
<p><strong>网关配置</strong></p>
<div class="line-block">
<div class="line">可以通过 USB 连接设备，并使用板载 shell 命令进行配置。</div>
<div class="line">按下双 Enter 键，启用 shell 命令模式。</div>
</div>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/advanced_001.png"><img alt="../../../_images/advanced_001.png" class="align-center" src="/docs-assets/zh-cn/_images/advanced_001.png" style="width: 303.40000000000003px; height: 320.0px;"></a>
</div></blockquote>
<p>2.1。 UWB 网络配置</p>
<blockquote>
<div><ul>
<li><p>配置网络 ID</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; nis</span>
<span class="go">usage: nis PANID</span>
</pre></div>
</div>
</div></blockquote>
</li>
<li><p>配置设备成为网关</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; nmg</span>
<span class="go">ok</span>
</pre></div>
</div>
</div></blockquote>
</li>
</ul>
<p>或</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; acs leds 1 uwb 2</span>
<span class="go">ok</span>
</pre></div>
</div>
</div></blockquote>
</div></blockquote>
<p>2.2。 设备 IP 地址配置</p>
<blockquote>
<div><p>默认为 DHCP（动态 IP 地址），除非需要，否则无需配置。</p>
<ul>
<li><p>使用方法</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; ipv4</span>
<span class="go">usage: ipv4 [static|dynamic] [addr STRING] [mask STRING] [gw STRING]</span>
</pre></div>
</div>
<div class="admonition note">
<p class="admonition-title">注解</p>
<p>配置成功后，设备将被重置。</p>
</div>
</div></blockquote>
</li>
<li><p>静态IP地址配置</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; ipv4 addr 192.168.1.100 static</span>
<span class="go">ipv4 ok(0)</span>
</pre></div>
</div>
</div></blockquote>
</li>
<li><p>网络掩码配置</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; ipv4 mask 255.255.255.0</span>
<span class="go">ipv4 ok(0)</span>
</pre></div>
</div>
</div></blockquote>
</li>
<li><p>启用之前配置的静态 IP 地址</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; ipv4 static</span>
<span class="go">ipv4 ok(0)</span>
</pre></div>
</div>
</div></blockquote>
</li>
<li><p>启用 DHCP</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; ipv4 dynamic</span>
<span class="go">ipv4 ok(0)</span>
</pre></div>
</div>
</div></blockquote>
</li>
<li><p>一步完成所有配置</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; ipv4 addr 192.168.1.100 mask 255.255.255.0 static ipv4 ok(0)</span>
</pre></div>
</div>
</div></blockquote>
</li>
</ul>
</div></blockquote>
<p>2.3。 配置 LEAPS Server连接</p>
<blockquote>
<div><ul>
<li><p>使用方法</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; peer</span>
<span class="go">usage: peer [addr STRING] [port NUM] [tls 0|1]</span>
</pre></div>
</div>
<div class="admonition note">
<p class="admonition-title">注解</p>
<p>配置成功后，设备将被重置。</p>
</div>
</div></blockquote>
</li>
<li><p>配置与 IP 地址为 192.168.200.1, 端口为 7777 的 LEAPS Server的连接</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; peer addr 192.168.200.1 port 7777 tls 0</span>
<span class="go">peer ok(0)</span>
</pre></div>
</div>
</div></blockquote>
</li>
<li><p>禁用 TLS</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; peer tls 0</span>
<span class="go">peer ok(0)</span>
</pre></div>
</div>
</div></blockquote>
</li>
<li><p>启用 TLS</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; peer tls 1</span>
<span class="go">peer ok(0)</span>
</pre></div>
</div>
</div></blockquote>
</li>
<li><p>LEAS Server主机和 TLS 的组合配置</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; peer host example.com tls 1</span>
<span class="go">peer ok(0)</span>
</pre></div>
</div>
</div></blockquote>
</li>
<li><p>禁用 TLS 时系统的正确状态</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; si</span>
<span class="go">[000081.971 INF] sys: fw1 fw_ver=x01030000 cfg_ver=x00030000</span>
<span class="go">[000081.976 INF] inet: up tls=off addr=192.168.1.100 mask=255.255.255.0 gw=192.168.200.1 (dynamic)</span>
<span class="go">[000081.983 INF] inet: peer=192.168.200.1:7777 (-)</span>
<span class="go">[000081.987 INF] uwb: panid=x0000 addr=xDECA84B1B8544434</span>
<span class="go">[000081.992 INF] uwbmac: connected</span>
<span class="go">[000081.997 INF] mode: gn (act)</span>
<span class="go">[000082.000 INF] cfg: enc=0 ble=1 leds=1 fwup=0 label=ID4434</span>
<span class="go">[000082.005 INF] enc: off (nokey)</span>
<span class="go">[000082.008 INF] gw: connected</span>
</pre></div>
</div>
</div></blockquote>
</li>
<li><p>启用 TLS 时系统的正确状态</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; si</span>
<span class="go">[000027.316 INF] sys: fw1 fw_ver=x01030000 cfg_ver=x00030000</span>
<span class="go">[000027.321 INF] inet: up tls=on addr=192.168.1.100 mask=255.255.255.0 gw=192.168.200.1 (dynamic)</span>
<span class="go">[000027.328 INF] inet: peer=123.123.123.123:7777(server.example.com)</span>
<span class="go">[000027.332 INF] uwb: panid=x0000 addr=xDECA84B1B8544434</span>
<span class="go">[000027.337 INF] uwbmac: connected</span>
<span class="go">[000027.342 INF] mode: gn (act)</span>
<span class="go">[000027.345 INF] cfg: enc=0 ble=1 leds=1 fwup=0 label=ID4434</span>
<span class="go">[000027.350 INF] enc: off (nokey)</span>
<span class="go">[000027.353 INF] gw: connected</span>
</pre></div>
</div>
</div></blockquote>
</li>
</ul>
</div></blockquote>
</li>
<li><p>打开 LEAPS Center</p>
<ul class="simple">
<li><p>通过 <code class="docutils literal notranslate"><span class="pre">PANS</span> <span class="pre">PRO</span> <span class="pre">Docker</span></code> 或 <code class="docutils literal notranslate"><span class="pre">PANS</span> <span class="pre">PRO</span> <span class="pre">Raspberry</span> <span class="pre">Pi</span></code> 启动。</p></li>
</ul>
</li>
<li><p>登录</p>
<ul class="simple">
<li><p>使用用户名 <code class="docutils literal notranslate"><span class="pre">admin</span></code> 和密码 <code class="docutils literal notranslate"><span class="pre">admin</span></code>。</p></li>
</ul>
<a class="reference internal image-reference" href="../../../_images/leaps_center_login.png"><img alt="../../../_images/leaps_center_login.png" class="align-center" src="/docs-assets/zh-cn/_images/leaps_center_login.png" style="width: 762.8000000000001px; height: 360.0px;"></a>
</li>
<li><p>选择网络</p>
<ul class="simple">
<li><p>点击左侧导航菜单中的``网络``。</p></li>
</ul>
</li>
<li><p>添加新网络</p>
<ul class="simple">
<li><p>提供 <strong>名称</strong> 和 <strong>ID</strong>。</p></li>
<li><p>选择 <strong>协议类型</strong> 为 <strong>PANS</strong>。</p></li>
<li><p>输入 <strong>主机</strong> 和 <strong>TCP 端口</strong>。</p></li>
<li><p>填写 <strong>用户名</strong>, <strong>密码</strong> 和 <strong>主题前缀</strong>。</p></li>
</ul>
</li>
<li><p>测试连接</p>
<ul class="simple">
<li><p>按下 <code class="docutils literal notranslate"><span class="pre">Test</span></code> 按钮检查连接，然后按下 <code class="docutils literal notranslate"><span class="pre">Save</span></code> 创建网络。</p></li>
</ul>
<a class="reference internal image-reference" href="../../../_images/leaps_center_pans.png"><img alt="../../../_images/leaps_center_pans.png" class="align-center" src="/docs-assets/zh-cn/_images/leaps_center_pans.png" style="width: 764.4000000000001px; height: 360.40000000000003px;"></a>
</li>
<li><p>完成后，网络可视化将在应用程序的二维和三维视图中显示。 更多信息，请参阅 <code class="docutils literal notranslate"><span class="pre">LEAPS</span> <span class="pre">Center</span></code> 配置和使用。</p></li>
</ol>
</div>
<input id="sd-tab-item-2" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-2">
高级</label><div class="sd-tab-content docutils">
<p>引用 <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/pans-pro-api#pans-pro-api"><span class="std std-ref">PANS PRO API</span></a>。</p>
</div>
<input id="sd-tab-item-3" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-3">
故障排除</label><div class="sd-tab-content docutils">
<ul class="simple">
<li><p>当低功耗Bluetooth (BLE) 和 LED 同时熄灭时，用户可能会错误地认为电路板无法运作。 在这种情况下，用户唯一的办法就是启动出厂重置（<a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/shell-api/sys#frst"><span class="std std-ref">frst</span></a>）命令。</p></li>
<li><p>请检查版本. 我们建议您使用最新的官方版本。</p></li>
</ul>
</div>
</div>
<div class="admonition note">
<p class="admonition-title">注解</p>
<ul class="simple">
<li><p>请参考软件基础架构，以进一步探索此演示的功能. 我们的支持包括 <a class="reference internal" href="/docs/zh/pans-pro-rtls/quick-start-guide/panspro-docker#panspro-docker"><span class="std std-ref">PANS PRO Docker</span></a> 和 <a class="reference internal" href="/docs/zh/pans-pro-rtls/quick-start-guide/panspro-rpi#panspro-rpi"><span class="std std-ref">PANS PRO Raspberry Pi</span></a>。</p></li>
<li><p>如果您对我们的产品有任何意见或问题，我们鼓励您访问我们的 <a class="reference external" href="https://forum.leapslabs.com">LEAPS 论坛</a>。</p></li>
</ul>
</div>
</div>


           </div>
