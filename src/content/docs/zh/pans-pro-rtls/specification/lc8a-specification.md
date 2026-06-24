---
title: "LC8A 规格"
lang: zh
slug: "pans-pro-rtls/specification/lc8a-specification"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/pans-pro-rtls/specification/lc8a-specification/"
order: 28
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="lc8a-specification">
<span id="id1"></span><h1>LC8A 规格</h1>
<p>本文档提供 LC8A 设备的技术细节。 LC8A 装置是一种多功能硬件解决方案，可在实时定位系统 (RTLS) 中作为标签节点 (TN) 或锚节点 (AN) 使用。 其灵活性和适应性使其成为各种追踪和监控应用的理想选择。</p>
<blockquote>
<div></div></blockquote>
<div class="sd-card sd-sphinx-override sd-mb-3 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<p class="sd-card-text">另请参阅 <a class="reference external" href="/_static/_pdfversion/lc8a-datasheet-zh_cn.pdf">技术规格的 PDF 版本</a></p>
</div>
</div>
<a class="reference internal image-reference" href="../../../_images/lc8a_front_view.png"><img alt="The Front view of the device" class="align-center" src="/docs-assets/zh-cn/_images/lc8a_front_view.png" style="width: 151.79999999999998px; height: 235.2px;"></a>
<div style="text-align: center; font-weight: bold;">
The Front view of the device.
</div><hr class="docutils">
<div class="section" id="key-features">
<h2>主要功能</h2>
<ul class="simple">
<li><p>基于 Qorvo 的 <a class="reference external" href="https://www.qorvo.com/products/p/DWM1001C">DWM1001C</a> 超宽带 (UWB) 模块 (<a class="reference external" href="https://www.qorvo.com/products/p/DW1000">DW1000</a> 超宽带 (UWB) 收发器 IC 和 Nordic Semiconductor nRF52832)：</p>
<ul>
<li><p>测距精度在 +-20cm 以内。</p></li>
<li><p>UWB 频道 5 印刷电路板天线 (6.5 GHz)</p></li>
<li><p>6.8 Mbps 数据传输速率，符合 IEEE 802.15.4-2011 UWB 标准。</p></li>
<li><p>集成 UWB 和 Bluetooth® 天线以及所有射频电路。</p></li>
<li><p>集成运动传感器:三轴加速计。</p></li>
<li><p>为低功耗睡眠模式优化的电流消耗： &lt;15μA</p></li>
</ul>
</li>
<li><p>三个功能按钮。</p></li>
<li><p>一个 RGB 主 LED 和两个侧边绿色 LED</p></li>
<li><p>触觉反馈</p></li>
<li><p>警报功能的蜂鸣器</p></li>
<li><p>免费软件配置和可视化工具（软件支持 iOS, Android, Windows, macOS 和 Linux 平台）。</p></li>
<li><p>一个开放的 <a class="reference external" href="https://docs.leapslabs.com/">在线文档</a> 和 <a class="reference external" href="https://forum.leapslabs.com">社区论坛</a>。</p></li>
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
<tr class="row-even"><td><p>USB (电源和数据)</p></td>
<td><p>最大 5V @ 500mA</p></td>
</tr>
<tr class="row-odd"><td><p>电池</p></td>
<td><p>3.7V @ 1Ah</p></td>
</tr>
<tr class="row-even"><td><p>工作温度 (不含电池)</p></td>
<td><p>-40°C - +85°C</p></td>
</tr>
<tr class="row-odd"><td><p>工作温度（带电池）</p></td>
<td><p>-20°C - +45°C</p></td>
</tr>
<tr class="row-even"><td><p>工作温度（充电）</p></td>
<td><p>0°C ˜ +40°C</p></td>
</tr>
<tr class="row-odd"><td><p>支持的 UWB 频道</p></td>
<td><p>UWB-CH5 - 6240-6739.2 MHz</p></td>
</tr>
<tr class="row-even"><td><p>UWB 发射功率</p></td>
<td><p>ETSI, FCC： 最大 -41.3 dBm/MHz</p></td>
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
<td><p>90 x 70 x 10 mm</p></td>
</tr>
<tr class="row-odd"><td><p>重量</p></td>
<td><p>80g</p></td>
</tr>
<tr class="row-even"><td><p>颜色</p></td>
<td><p>白色</p></td>
</tr>
<tr class="row-odd"><td><p>安装</p></td>
<td><p>徽章夹 (可选)</p></td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="device-overview">
<h2>设备概述</h2>
<a class="reference internal image-reference" href="../../../_images/lc8a_hardware_interfaces.png"><img alt="The Front view of the device" class="align-center" src="/docs-assets/zh-cn/_images/lc8a_hardware_interfaces.png" style="width: 346.40000000000003px; height: 293.6px;"></a>
<div style="text-align: center; font-weight: bold;">
The Hardware Interfaces of the device.
</div></div>
<hr class="docutils">
<div class="section" id="safety-instructions">
<h2>安全说明</h2>
<ul class="simple">
<li><p>运行时，请勿将设备暴露在水或潮湿环境中。</p></li>
<li><p>请勿将设备暴露在任何热源中。 本产品专为在工业温度下可靠运行而设计 <cite>1</cite>。 如果产品配有电池，则可在正常工作温度下使用`2`。 电池充电时的温度`3`受到内部保护（如果温度超出范围，电池充电将不会启动或推迟）。</p></li>
</ul>
</div>
<div class="section" id="warnings">
<h2>警告</h2>
<ul class="simple">
<li><p>本产品仅可连接至 USB 电源，且电流不得低于 0.5 A。</p></li>
<li><p>本产品使用的任何外接电源，均应符合预定使用国家的相关法规和标准。</p></li>
<li><p>本产品应在通风且无冷凝的环境下操作，操作时不应遮盖。</p></li>
<li><p>本产品内部没有可供用户维修的部件，打开本装置可能会损坏产品，并导致保修失效。</p></li>
<li><p>与本产品一起使用的所有外围设备的电缆和连接器，必须有足够的绝缘，以符合相关的安全要求。</p></li>
</ul>
</div>
<div class="section" id="order-information">
<h2>订单信息</h2>
<ul class="simple">
<li><p>部件号: PP-LC8A</p></li>
<li><p>HS Code: 8517.69.9000</p></li>
<li><p>包装:10个纸盒，17厘米 x 11厘米 x 12厘米，0.8千克</p></li>
</ul>
</div>
</div>


           </div>
