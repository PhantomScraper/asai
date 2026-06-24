---
title: "LC5A 规格"
lang: zh
slug: "pans-pro-rtls/specification/lc5a-specification"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/pans-pro-rtls/specification/lc5a-specification/"
order: 103
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="lc5a-specification">
<span id="id1"></span><h1>LC5A 规格</h1>
<p>本文档提供 LC5A 设备的技术细节。 LC5A 设备是一种硬件解决方案，设计用作实时定位系统 (RTLS) 中的网关节点。 其灵活性和适应性使其成为各种追踪和监控应用的理想选择。</p>
<blockquote>
<div></div></blockquote>
<div class="sd-card sd-sphinx-override sd-mb-3 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<p class="sd-card-text">另请参阅 <a class="reference external" href="/_static/_pdfversion/lc5a-datasheet-zh_cn.pdf">技术规格的 PDF 版本</a></p>
</div>
</div>
<a class="reference internal image-reference" href="../../../_images/lc5a_front_view.png"><img alt="The Front view of the device" class="align-center" src="/docs-assets/zh-cn/_images/lc5a_front_view.png" style="width: 231.20000000000002px; height: 230.4px;"></a>
<div style="text-align: center; font-weight: bold;">
The Front view of the device.
</div><hr class="docutils">
<div class="section" id="key-features">
<h2>主要功能</h2>
<p>主 MCU 基于 Microchip 的 <a class="reference external" href="https://www.microchip.com/en-us/solutions/displays/embedded-graphics-solutions/mcu-guided-selection-tool-for-graphics/sam-e70-series">MCU SAM E70</a>，这是一款高性能 32 位 Arm® Cortex®-M7 处理器，可通过符合 IEEE 1588 标准的 10/100 以太网 MAC 提供连接. 集成的 ATWINC1500 Wifi 模块–低功耗 802.11 b/g/n IoT（物联网）模块，专门针对低功耗 IoT 应用进行了优化，支持 IEEE 802.11 WEP, WPA 和 WPA2 安全性. 超宽带子系统在 Qorvo 的 <a class="reference external" href="https://www.qorvo.com/products/p/DWM1001C">DWM1001C</a> 模块上运行，该模块集成了 <a class="reference external" href="https://www.qorvo.com/products/p/DW1000">DW1000</a> 超宽带 (UWB) 收发器 IC 和带有Bluetooth nRF52832 的 Nordic Semiconductor MCU：</p>
<blockquote>
<div><ul class="simple">
<li><p>测距精度在 +-20cm 以内。</p></li>
<li><p>UWB 频道 5 印刷电路板天线 (6.5 GHz)</p></li>
<li><p>6.8 Mbps 数据传输率，符合 IEEE 802.15.4-2011 UWB 标准。</p></li>
<li><p>集成 UWB 和 Bluetooth® 天线以及所有射频电路。</p></li>
<li><p>集成运动传感器:三轴加速计。</p></li>
</ul>
</div></blockquote>
<ul class="simple">
<li><p>支持以太网或 WIFI 与 <a class="reference internal" href="/docs/zh/pans-pro-rtls/infrastructure/leaps-server#pans-pro-server"><span class="std std-ref">LEAPS Server</span></a> 连接。</p></li>
<li><p>包含状态 LED 和 UWB 状态 LED。</p></li>
<li><p>通过 USB 电缆（5 VDC）或外部电源（7~32 VDC）供电。</p></li>
<li><p>免费的完整软件包，包括软件基础架构, 配置和可视化工具（支持 Android, Windows, macOS 和 Linux 等各种平台）。</p></li>
<li><p>一个开放的 <a class="reference external" href="https://docs。leapslabs.com/">在线文档</a> 和 <a class="reference external" href="https://forum.leapslabs.com">社区论坛</a>。</p></li>
</ul>
</div>
<hr class="docutils">
<div class="section" id="software-compatibility">
<h2>软件兼容性</h2>
<p>它与 <a class="reference internal" href="/docs/zh/pans-pro-rtls#pans-pro-rtls"><span class="std std-ref">PANS PRO RTLS</span></a> 和 <a class="reference internal" href="/docs/zh/leaps-rtls#leaps-rtls"><span class="std std-ref">LEAPS RTLS</span></a> 兼容. 默认固件是由生产商提供的 <a class="reference internal" href="/docs/zh/pans-pro-rtls#pans-pro-rtls"><span class="std std-ref">PANS PRO RTLS</span></a>。</p>
</div>
<div class="section" id="electrical-parameters">
<h2>电气参数</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 46%">
<col style="width: 54%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>参数</p></th>
<th class="head"><p>价值</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>VDC直流电源</p></td>
<td><p>7 ˜ 32 @3W 最大值</p></td>
</tr>
<tr class="row-odd"><td><p>USB (电源和数据)</p></td>
<td><p>最大 5V @ 500mA</p></td>
</tr>
<tr class="row-even"><td><p>PoE</p></td>
<td><p>802.3AF，最大 4W</p></td>
</tr>
<tr class="row-odd"><td><p>工作温度</p></td>
<td><p>-40°C - +85°C</p></td>
</tr>
<tr class="row-even"><td><p>支持的 UWB 频道</p></td>
<td><p>UWB-CH5 - 6240-6739.2 MHz</p></td>
</tr>
<tr class="row-odd"><td><p>UWB 发射功率</p></td>
<td><p>ETSI, FCC： 最大 -41.3 dBm/MHz</p></td>
</tr>
<tr class="row-even"><td><p>WIFI频率范围</p></td>
<td><p>单频段 2.4GHz b/g/n 物联网</p></td>
</tr>
<tr class="row-odd"><td><p>WIFI 接收灵敏度</p></td>
<td><p>-95 dBm</p></td>
</tr>
<tr class="row-even"><td><p>WIFI TX 输出功率</p></td>
<td><p>18.5 dBm</p></td>
</tr>
<tr class="row-odd"><td><p>WIFI 加密</p></td>
<td><p>WEP, WPA-TKIP, WPA2, CCMP-AES</p></td>
</tr>
<tr class="row-even"><td><p>WIFI国家代码</p></td>
<td><p>01（世界安全）</p></td>
</tr>
</tbody>
</table>
</div>
<div class="section" id="mechanical-parameters">
<h2>机械参数</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 46%">
<col style="width: 54%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>参数</p></th>
<th class="head"><p>价值</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>大小</p></td>
<td><p>100 x 100 x 35 mm</p></td>
</tr>
<tr class="row-odd"><td><p>重量</p></td>
<td><p>110g</p></td>
</tr>
<tr class="row-even"><td><p>颜色</p></td>
<td><p>白色</p></td>
</tr>
<tr class="row-odd"><td><p>安装</p></td>
<td><p>连接任何带 1/4” 螺丝球形云台的夹具安装座</p></td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="device-overview">
<h2>设备概述</h2>
<a class="reference internal image-reference" href="../../../_images/lc5a_hardware_interfaces.png"><img alt="The Front view of the device" class="align-center" src="/docs-assets/zh-cn/_images/lc5a_hardware_interfaces.png" style="width: 502.40000000000003px; height: 293.6px;"></a>
<div style="text-align: center; font-weight: bold;">
The Hardware Interfaces of the device.
</div></div>
<hr class="docutils">
<div class="section" id="safety-instructions">
<h2>安全说明</h2>
<ul class="simple">
<li><p>运行时，请勿将设备暴露在水或潮湿环境中。</p></li>
<li><p>请勿将设备暴露在任何来源的热源中。 本产品专为在工业温度下可靠运行而设计。</p></li>
</ul>
</div>
<div class="section" id="warnings">
<h2>警告</h2>
<ul class="simple">
<li><p>本产品只能连接额定电流为 7˜32DC, USB 电源和最小电流为 0.5 A 的外部电源。</p></li>
<li><p>本产品使用的任何外接电源，均应符合预定使用国家的相关法规和标准。</p></li>
<li><p>本产品应在通风且无冷凝的环境下操作，操作时不应遮盖。</p></li>
<li><p>本产品内部没有可供用户维修的零件，打开本装置可能会损坏产品，并导致保修失效。</p></li>
<li><p>与本产品一起使用的所有外围设备的电缆和连接器，必须有足够的绝缘，以符合相关的安全要求。</p></li>
</ul>
</div>
<div class="section" id="order-information">
<h2>订单信息</h2>
<ul class="simple">
<li><p>部件号: PP-LC5A / LR-LC5A</p></li>
<li><p>HS Code: 8517.69.9000</p></li>
<li><p>包装: 纸盒, 1.5 cm x 10 cm x 4 cm 0.15 kg</p></li>
</ul>
</div>
</div>


           </div>
