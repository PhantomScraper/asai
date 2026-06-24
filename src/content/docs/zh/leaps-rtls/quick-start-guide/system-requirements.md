---
title: "系统要求"
lang: zh
slug: "leaps-rtls/quick-start-guide/system-requirements"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/leaps-rtls/quick-start-guide/system-requirements/"
order: 60
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="system-requirements">
<span id="leaps-qsg-system-requirements"></span><h1>系统要求</h1>
<p>以下部分提供了在开始使用RTLS（实时定位系统）演示之前所需的软件和硬件的详细信息 <a class="reference internal" href="/docs/zh/leaps-rtls#leaps-rtls"><span class="std std-ref">LEAPS RTLS</span></a>。请注意，某些项目是可选的，并非所有演示都是强制性的。</p>
<div class="section" id="hardware">
<h2>硬件</h2>
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
<tr class="row-even"><td><p>UWB设备</p></td>
<td><p>5+</p></td>
<td><p>必填</p></td>
<td><ul class="simple">
<li><p>至少三个锚节点</p></li>
<li><p>至少一个标记节点</p></li>
<li><p>至少一个网关节点</p></li>
</ul>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line">微型 USB</div>
<div class="line">电缆</div>
</div>
</td>
<td><p>6+</p></td>
<td><p>可选</p></td>
<td><blockquote>
<div><a class="reference internal image-reference" href="../../../_images/micro-usb.webp"><img alt="../../../_images/micro-usb.webp" class="align-right" src="/docs-assets/zh-cn/_images/micro-usb.webp" style="width: 119.92px; height: 119.92px;"></a>
</div></blockquote>
<p>为设备供电、与PC进行数据交换或重新刷新固件。重新刷新电路板是可选的，设备从生产开始编程。</p>
</td>
</tr>
<tr class="row-even"><td><p>电池</p></td>
<td><p>6+</p></td>
<td><p>可选</p></td>
<td><div class="line-block">
<div class="line">不使用微型USB电缆为UWB设备供电。</div>
<div class="line">推荐:</div>
</div>
<blockquote>
<div><ul class="simple">
<li><p>Fenix RCR123A (3.7V)</p></li>
<li><p>保持电源RCR123A 3.7V（860毫安时，含充电器）</p></li>
</ul>
<p><a class="reference internal" href="../../../_images/battery-rcr123a.png"><img alt="Fenix" src="/docs-assets/zh-cn/_images/battery-rcr123a.png" style="width: 120.2px; height: 119.2px;"></a>  <a class="reference internal" href="../../../_images/keeppower-rcr123a.jpg"><img alt="keeppower" src="/docs-assets/zh-cn/_images/keeppower-rcr123a.jpg" style="width: 120.0px; height: 120.0px;"></a></p>
</div></blockquote>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line">Phone</div>
<div class="line">设备</div>
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
<p>用于快速设置带有web服务器应用程序的网关，包括LEAPS server、LEAPS Center和MQTT Broker。此外，它还可以用于使用USB/UART/Bluetooth更新设备。</p>
</td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="software">
<h2>软件</h2>
<p>以下是演示所需的所有软件应用程序和工具的列表。</p>
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
<td><p>一个 Android 应用程序，可使用Bluetooth或MQTT进行设备配置和网络可视化。</p></td>
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
</tbody>
</table>
</div>
</div>


           </div>
