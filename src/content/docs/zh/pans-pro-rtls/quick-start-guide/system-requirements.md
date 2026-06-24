---
title: "系统要求"
lang: zh
slug: "pans-pro-rtls/quick-start-guide/system-requirements"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/pans-pro-rtls/quick-start-guide/system-requirements/"
order: 87
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="system-requirements">
<span id="qsg-system-requirements"></span><h1>系统要求</h1>
<p>以下部分详细介绍了在开始使用 <a class="reference internal" href="/docs/zh/pans-pro-rtls#pans-pro-rtls"><span class="std std-ref">PANS PRO RTLS</span></a> 的RTLS（实时定位系统）演示前所需的软件和硬件。 请注意，某些项目是可选的，并非所有演示都必须进行。</p>
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
<th class="head"><p><strong>说明</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>UWB设备</p></td>
<td><p>6+</p></td>
<td><p>必填</p></td>
<td><ul class="simple">
<li><p>至少四个 <code class="docutils literal notranslate"><span class="pre">LC4设备</span></code> (锚节点)</p></li>
<li><p>至少一个 <code class="docutils literal notranslate"><span class="pre">LC8</span> <span class="pre">设备</span></code> (标签节点)</p></li>
<li><p>至少一个 <code class="docutils literal notranslate"><span class="pre">LC5</span> <span class="pre">device</span></code> (标签节点)</p></li>
</ul>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line">微型 USB</div>
<div class="line">电缆</div>
</div>
</td>
<td><p>5</p></td>
<td><p>必填</p></td>
<td><blockquote>
<div><a class="reference internal image-reference" href="../../../_images/micro-usb.webp"><img alt="../../../_images/micro-usb.webp" class="align-right" src="/docs-assets/zh-cn/_images/micro-usb.webp" style="width: 89.94px; height: 89.94px;"></a>
</div></blockquote>
<p>为设备供电、与 PC 进行数据交换或重新刷新固件。重新刷新电路板是可选项，设备从生产开始就已编程。</p>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line">USB-C</div>
<div class="line">电缆</div>
</div>
</td>
<td><p>1</p></td>
<td><p>可选</p></td>
<td><blockquote>
<div><a class="reference internal image-reference" href="../../../_images/usb-c.jpg"><img alt="../../../_images/usb-c.jpg" class="align-right" src="/docs-assets/zh-cn/_images/usb-c.jpg" style="width: 91.0px; height: 91.0px;"></a>
</div></blockquote>
<p>为设备供电、与 PC 进行数据交换或重新刷新固件。重新刷新电路板是可选项，设备从生产开始就已编程。</p>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line">USB墙</div>
<div class="line">适配器</div>
</div>
</td>
<td><p>5+</p></td>
<td><p>推荐</p></td>
<td><blockquote>
<div><a class="reference internal image-reference" href="../../../_images/usb-wall-charger.jpg"><img alt="../../../_images/usb-wall-charger.jpg" class="align-right" src="/docs-assets/zh-cn/_images/usb-wall-charger.jpg" style="width: 96.0px; height: 96.0px;"></a>
</div></blockquote>
<p>一种紧凑型设备，可连接标准墙面电源插座，提供一个或多个 USB 端口，为电子设备充电或供电。</p>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line">安卓</div>
<div class="line">设备</div>
<div class="line"><br></div>
</div>
</td>
<td><p>1</p></td>
<td><p>推荐</p></td>
<td><blockquote>
<div><a class="reference internal image-reference" href="../../../_images/samsung-a7.png"><img alt="../../../_images/samsung-a7.png" class="align-right" src="/docs-assets/zh-cn/_images/samsung-a7.png" style="width: 99.80000000000001px; height: 99.80000000000001px;"></a>
</div></blockquote>
<p>用于运行 <a class="reference internal" href="/docs/zh/pans-pro-rtls/infrastructure/leaps-server#pans-pro-server"><span class="std std-ref">LEAPS Server</span></a>，这是一个Android应用程序，可用于使用Bluetooth或 MQTT 配置设备和可视化网络. 需要 6.0 或更高版本的 Android 操作系统。</p>
</td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line">桌面</div>
<div class="line">设备</div>
</div>
</td>
<td><p>1</p></td>
<td><p>可选</p></td>
<td><blockquote>
<div><a class="reference internal image-reference" href="../../../_images/desktop-device.png"><img alt="../../../_images/desktop-device.png" class="align-right" src="/docs-assets/zh-cn/_images/desktop-device.png" style="width: 99.89999999999999px; height: 88.02px;"></a>
</div></blockquote>
<p>用户可用于多种用途：运行包含网络服务器应用程序(<a class="reference internal" href="/docs/zh/pans-pro-rtls/infrastructure/leaps-center#pans-pro-center"><span class="std std-ref">LEAPS Center</span></a>, <a class="reference internal" href="/docs/zh/pans-pro-rtls/infrastructure/leaps-server#pans-pro-server"><span class="std std-ref">LEAPS Server</span></a> 和 MQTT Broker)的 VirtualBox 映像，支持 Windows, macOS 和 Linux 操作系统. 此外，它也可用于通过USB/UART/Bluetooth更新设备，以及通过 USB/UART/Bluetooth与设备通信。</p>
</td>
</tr>
<tr class="row-even"><td><div class="line-block">
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
<p>用于快速设置带有网络服务器应用程序的网关，包括LEAPS Server, LEAPS Center和MQTT Broker. 此外，它还可用于使用USB/UART/Bluetooth更新设备。</p>
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
<th class="head"><p>说明</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/pans-pro-uwbs#pans-pro-uwbs"><span class="std std-ref">PANS PRO UWBS</span></a></p></td>
<td><p>-</p></td>
<td><p>可选</p></td>
<td><p>PANS PRO 超宽带 Sus 系统固件。</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/infrastructure/pans-pro-manager#pans-pro-manager"><span class="std std-ref">PANS PRO Manager</span></a></p></td>
<td><p>-</p></td>
<td><p>可选</p></td>
<td><p>一个 Android 应用程序，可使用Bluetooth或MQTT进行设备配置和网络可视化。</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/infrastructure/leaps-server#pans-pro-server"><span class="std std-ref">LEAPS Server</span></a></p></td>
<td><p>-</p></td>
<td><p>可选</p></td>
<td><p>一个Linux守护进程应用程序，充当UWB网络的中央数据中心，负责通过MQTT代理将数据聚合到外部系统或从外部系统传输数据。</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/infrastructure/leaps-center#pans-pro-center"><span class="std std-ref">LEAPS Center</span></a></p></td>
<td><p>-</p></td>
<td><p>可选</p></td>
<td><p>用于配置和可视化UWB网络的Web应用程序。</p></td>
</tr>
</tbody>
</table>
<div class="section" id="third-party-applications-and-tools">
<h3>第三方应用和工具</h3>
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
<th class="head"><p>说明</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><a class="reference external" href="https://mosquitto.org/download/">Mosquitto MQTT Broker</a></p></td>
<td><p>2.0.11</p></td>
<td><p>可选</p></td>
<td><p>Mosquitto 是一个 MQTT v5.0/v3.1.1/v3.1 代理. Mosquitto 的推荐版本是 2.0.11。</p></td>
</tr>
</tbody>
</table>
</div>
</div>
</div>


           </div>
