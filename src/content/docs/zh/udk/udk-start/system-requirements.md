---
title: "系统要求"
lang: zh
slug: "udk/udk-start/system-requirements"
section: "udk"
sourceUrl: "https://docs.leapslabs.com/zh-cn/udk/udk-start/system-requirements/"
order: 33
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="system-requirements">
<span id="id1"></span><h1>系统要求</h1>
<hr class="docutils">
<div class="section" id="hardware">
<h2>硬件</h2>
<p>下表列出了设置即将到来的部分演示所需的基本硬件。请注意，某些项目是可选的，并非所有演示都是强制性的。</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 14%">
<col style="width: 12%">
<col style="width: 12%">
<col style="width: 63%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>项目</strong></p></th>
<th class="head"><p><strong>数量</strong></p></th>
<th class="head"><p><strong>必要性</strong></p></th>
<th class="head"><p><strong>描述</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>UDK套件</p></td>
<td><p>1+</p></td>
<td><p>必填</p></td>
<td><blockquote>
<div><a class="reference internal image-reference" href="../../../_images/udk_kit_box.png"><img alt="../../../_images/udk_kit_box.png" class="align-right" src="/docs-assets/zh-cn/_images/udk_kit_box.png" style="width: 167.4px; height: 98.1px;"></a>
</div></blockquote>
<p>每个套件包括一个LC13设备（带AoA天线）、五个LC14设备（带非AoA天线的）和2条USB C型数据线。</p>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line">USB-C</div>
<div class="line">数据</div>
<div class="line">电缆</div>
</div>
</td>
<td><p>2+（取决于演示）</p></td>
<td><p>可选</p></td>
<td><blockquote>
<div><a class="reference internal image-reference" href="../../../_images/usb-c-data-cable.png"><img alt="../../../_images/usb-c-data-cable.png" class="align-right" src="/docs-assets/zh-cn/_images/usb-c-data-cable.png" style="width: 172.0px; height: 89.0px;"></a>
</div></blockquote>
<p>为UDK设备供电，与PC进行数据交换，或重新刷新固件。注:UDK盒子中有2根USB-C数据线。重新刷新电路板是可选的。设备从生产开始编程。</p>
</td>
</tr>
<tr class="row-even"><td><p>电池</p></td>
<td><p>6+（取决于演示）</p></td>
<td><p>可选</p></td>
<td><div class="line-block">
<div class="line">T不使用USB-C电缆为UDK设备供电。</div>
<div class="line">推荐:</div>
</div>
<blockquote>
<div><ul class="simple">
<li><p>Fenix RCR123A (3.7V)</p></li>
<li><p>保持电源RCR123A 3.7V（860毫安时，含充电器）</p></li>
</ul>
<p><a class="reference internal" href="../../../_images/battery-rcr123a.png"><img alt="Fenix" src="/docs-assets/zh-cn/_images/battery-rcr123a.png" style="width: 150.25px; height: 149.0px;"></a>  <a class="reference internal" href="../../../_images/keeppower-rcr123a.jpg"><img alt="keeppower" src="/docs-assets/zh-cn/_images/keeppower-rcr123a.jpg" style="width: 144.0px; height: 144.0px;"></a></p>
</div></blockquote>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line">夹具或</div>
<div class="line">三脚架</div>
<div class="line">照相机</div>
<div class="line">攀登</div>
</div>
</td>
<td><p>4+</p></td>
<td><p>推荐</p></td>
<td><blockquote>
<div><a class="reference internal image-reference" href="../../../_images/super-clamp-mount.jpg"><img alt="../../../_images/super-clamp-mount.jpg" class="align-right" src="/docs-assets/zh-cn/_images/super-clamp-mount.jpg" style="width: 160.0px; height: 160.0px;"></a>
</div></blockquote>
<div class="line-block">
<div class="line">用于连接RTLS演示中的锚点设备。</div>
<div class="line">推荐: <a class="reference external" href="https://www.smallrig.com/clamp-mount-v1-w-ball-head-mount-and-coolclamp-1124.html">Super Clamp Mount</a></div>
</div>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line">Phone</div>
<div class="line">Device <a class="footnote-reference brackets" href="#note" id="id2">1</a></div>
<div class="line"><br></div>
</div>
</td>
<td><p>1</p></td>
<td><p>推荐</p></td>
<td><blockquote>
<div><a class="reference internal image-reference" href="../../../_images/samsung-a7.png"><img alt="../../../_images/samsung-a7.png" class="align-right" src="/docs-assets/zh-cn/_images/samsung-a7.png" style="width: 124.75px; height: 124.75px;"></a>
</div></blockquote>
<p>用于运行 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a>，这是一个可用于配置设备并使用Bluetooth或MQTT可视化网络的应用程序</p>
<ul class="simple">
<li><p><cite>需要Android操作系统6.0或更高版本</cite></p></li>
<li><p><cite>需要iOS版本15或更高版本。</cite></p></li>
</ul>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line">iOS</div>
<div class="line">设备</div>
</div>
</td>
<td><p>1</p></td>
<td><p>可选</p></td>
<td><blockquote>
<div><a class="reference internal image-reference" href="../../../_images/iso-device.jpeg"><img alt="../../../_images/iso-device.jpeg" class="align-right" src="/docs-assets/zh-cn/_images/iso-device.jpeg" style="width: 120.0px; height: 120.0px;"></a>
</div></blockquote>
<p>用于运行 <a class="reference internal" href="/docs/zh/udk/udk-start/partner-application-nearby-interaction#anchor-ni-app"><span class="std std-ref">Qorvo 附近的互动</span></a> 应用程序，这是一个与附近交互附件（UDK）通信并显示距离和方向的iOS应用程序。需要配备U1芯片和iOS 16或更高版本的iPhone。</p>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line">桌面</div>
<div class="line">设备</div>
</div>
</td>
<td><p>1</p></td>
<td><p>可选</p></td>
<td><blockquote>
<div><a class="reference internal image-reference" href="../../../_images/desktop-device.png"><img alt="../../../_images/desktop-device.png" class="align-right" src="/docs-assets/zh-cn/_images/desktop-device.png" style="width: 111.0px; height: 97.80000000000001px;"></a>
</div></blockquote>
<p>用于各种目的的用户:用于运行包含web服务器应用程序的VirtualBox映像（<a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-gateway#leapsgateway"><span class="std std-ref">LEAPS Gateway</span></a>，<a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-server#leapsserver"><span class="std std-ref">LEAPS Server</span></a>，<a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> 和MQTT Broker），支持Windows、macOS和Linux操作系统。此外，它还可用于使用USB/UART/Bluetooth更新设备，通过USB/UART与设备通信，对包含集成DAPLink的UDK设备进行重新编程，以及使用UDK SDK开发自定义应用程序。</p>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line">树莓</div>
<div class="line">Pi 3B</div>
<div class="line">或更新</div>
</div>
</td>
<td><p>1</p></td>
<td><p>可选</p></td>
<td><blockquote>
<div><a class="reference internal image-reference" href="../../../_images/ras-pi-device.jpg"><img alt="../../../_images/ras-pi-device.jpg" class="align-right" src="/docs-assets/zh-cn/_images/ras-pi-device.jpg" style="width: 100.0px; height: 100.0px;"></a>
</div></blockquote>
<p>用于快速设置具有web服务器应用程序的网关，包括LEAPS Gateway、LEAPS Server、LEAPS Center和MQTT代理。除此之外，它还可以用于使用USB/UART/Bluetooth更新设备，通过USB/UART与设备通信，对包含集成DAPLink的UDK设备进行重新编程。</p>
</td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="software">
<h2>软件</h2>
<p>Be以下是用于演示和UDK开发的所有软件应用程序和工具的列表。</p>
<hr class="docutils">
<div class="section" id="leaps-applications-and-tools">
<h3>LEAPS应用程序和工具</h3>
<table class="colwidths-given docutils align-default">
<colgroup>
<col style="width: 10%">
<col style="width: 10%">
<col style="width: 10%">
<col style="width: 70%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>项目</p></th>
<th class="head"><p>版本</p></th>
<th class="head"><p>必要性</p></th>
<th class="head"><p>描述</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/leaps-uwbs#leapsuwbs"><span class="std std-ref">LEAPS UWBS</span></a></p></td>
<td><p>-</p></td>
<td><p>可选</p></td>
<td><p>LEAPS超宽带Sus系统固件。UDK设备在生产时预装了LEAPS UWBS。仅在固件更新或设备恢复时才需要固件。</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a></p></td>
<td><p>-</p></td>
<td><p>可选</p></td>
<td><p>一个 Android 应用程序，可用于使用Bluetooth或MQTT配置设备和可视化网络。</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-gateway#leapsgateway"><span class="std std-ref">LEAPS Gateway</span></a></p></td>
<td><p>-</p></td>
<td><p>可选</p></td>
<td><p>一个Linux守护进程应用程序，充当LEAPS UWBS和LEAPS Server之间的关梁，从而连接TCP/IP网络。</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-server#leapsserver"><span class="std std-ref">LEAPS Server</span></a></p></td>
<td><p>-</p></td>
<td><p>可选</p></td>
<td><p>一个Linux守护进程应用程序，充当UWB网络的中央数据中心，负责通过MQTT代理将数据聚合到外部系统或从外部系统传输数据。</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a></p></td>
<td><p>-</p></td>
<td><p>可选</p></td>
<td><p>用于配置和可视化UWB网络的Web应用程序。</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/zh/udk/development-guide/udk-sdk-getting-started#udksdk"><span class="std std-ref">从 SDK 开始</span></a></p></td>
<td><p>-</p></td>
<td><p>可选</p></td>
<td><p>UDK SDK（软件开发工具包）基于Zephyr RTOS，可用于评估和开发定制的超宽带应用程序。</p></td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="partner-applications-and-tools">
<h3>合作伙伴应用程序和工具</h3>
<table class="colwidths-given docutils align-default">
<colgroup>
<col style="width: 10%">
<col style="width: 10%">
<col style="width: 10%">
<col style="width: 70%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>项目</p></th>
<th class="head"><p>版本</p></th>
<th class="head"><p>必要性</p></th>
<th class="head"><p>描述</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/zh/udk/udk-start/partner-application-aoa-app#anchor-ranging-aoa"><span class="std std-ref">UWB 测距与 AoA 演示应用程序</span></a></p></td>
<td><p>-</p></td>
<td><p>可选</p></td>
<td><p>Qorvo®桌面应用程序，演示Qorvo FiRa兼容设备的功能。它允许配置设备，并在桌面上可视化双向测距、到达角度和位置数据。该应用程序支持Windows、macOS和Linux操作系统。</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/zh/udk/udk-start/partner-application-nearby-interaction#anchor-ni-app"><span class="std std-ref">Qorvo 附近的互动</span></a></p></td>
<td><p>-</p></td>
<td><p>可选</p></td>
<td><p>Qorvo®Nearby Interaction和Qorvo™NI Background应用程序，允许用户使用Apple Nearby Interactions框架轻松评估Qorvo超宽带技术。该应用程序可在App Store上获得。</p></td>
</tr>
</tbody>
</table>
</div>
<div class="section" id="third-party-applications-and-tools">
<h3>第三方应用程序和工具</h3>
<table class="colwidths-given docutils align-default">
<colgroup>
<col style="width: 10%">
<col style="width: 10%">
<col style="width: 10%">
<col style="width: 70%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>项目</p></th>
<th class="head"><p>版本</p></th>
<th class="head"><p>必要性</p></th>
<th class="head"><p>描述</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><a class="reference external" href="https://mosquitto.org/download/">Mosquitto MQTT代理</a></p></td>
<td><p>2.0.11</p></td>
<td><p>可选</p></td>
<td><p>Mosquitto 是一个 MQTT v5.0/v3.1.1/v3.1 代理. Mosquitto 的推荐版本是 2.0.11。</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
<dl class="footnote brackets">
<dt class="label" id="note"><span class="brackets"><a class="fn-backref" href="#id2">1</a></span></dt>
<dd><p>测试设备:三星A7、三星Galaxy A21S、三星Galaxy A2</p>
</dd>
</dl>
</div>
</div>
</div>


           </div>
