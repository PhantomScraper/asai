---
title: "LC13和LC14规格"
lang: zh
slug: "udk/specification/lc13-lc14-specification"
section: "udk"
sourceUrl: "https://docs.leapslabs.com/zh-cn/udk/specification/lc13-lc14-specification/"
order: 54
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="lc13-and-lc14-specifications">
<h1>LC13和LC14规格</h1>
<hr class="docutils">
<div class="section" id="overview">
<h2>概述</h2>
<p>本节提供 LC13 和 LC14 设备的技术细节。 LC13/LC14 设备可用于创建锚节点 (AN), 锚启动器节点 (ANI), 标签节点 (TN) 和实时定位系统 (RTLS) 的网关。 它还兼容 FiRa 近距离交互和双向测距到达角（TWR-AoA）演示。 此外，此开放平台也可用于开发 UWB 或Bluetooth应用。</p>
</div>
<hr class="docutils">
<div class="section" id="key-features">
<h2>主要功能</h2>
<ul class="simple">
<li><p>基于村田 2AB SIP (MCU nRF52840 带Bluetooth, UWB QM33120W IC, LIS2DW 加速计, 晶体和内部电源调节器)。</p></li>
<li><p>Qorvo QM33120W - 超宽带 (UWB)：</p>
<ul>
<li><p>基于IEEE802.15.4z标准，并实现了增强的安全功能。</p></li>
<li><p>支持频道 5（6.5 GHz）和频道 9（8 GHz），符合 FCC, 日本 ARIB, ETSI 和 CE +10dB ETSI 的 UWB 射频标准。</p></li>
<li><p>集成了低噪声放大器(LNA)和功率放大器(PA)，以增加UWB范围（最远150米）。</p></li>
<li><p>集成了非静噪天线(LC14)和静噪天线(LC13)。</p></li>
<li><p>兼容FiRa™ PHY和MAC. 可与 Apple U1 芯片和Android FiRa兼容智能设备互操作。</p></li>
<li><p>向后兼容 DW1000 IEEE802.15.4a UWB IC 的通道 5。</p></li>
</ul>
</li>
<li><p>支持双向测距（MAC）, 到达时间差（TDoA）和到达相位差（PDoA）。</p></li>
<li><p>北欧半导体 nRF52840 - Bluetooth® 低能耗 (BLE) 5.3 射频技术，集成天线。</p></li>
<li><p>支持 NFC 标签天线连接器。</p></li>
<li><p>2 USB C端口集成了DAPLink编程器与虚拟COM，以及用于数据通信的USB设备接口。</p></li>
<li><p>另外，J-Link也可以通过板载的6针Tag Connect兼容连接器使用。</p></li>
<li><p>它包含 RGB LED, 2x <span class="green-text">GREEN</span> LED, 一个前置按钮, 两个侧边按钮, 一个用于 nRF52 USB 设备的 USB 接口, 一个蜂鸣器, 一个触觉马达以及用于连接外部传感器或 IO 的额外GPIO。</p></li>
</ul>
<div class="admonition note">
<p class="admonition-title">注解</p>
<p>请参阅 <a class="reference external" href="https://www.murata.com/en-global/products/connectivitymodule/ultra-wide-band/qorvo">Murata 2AB module</a> 和 <a class="reference external" href="https://www.qorvo.com/products/wireless-connectivity/ultra-wideband">Qorvo DW3000 IC</a> 页面了解更多详情。</p>
</div>
</div>
<hr class="docutils">
<div class="section" id="software-compatibility">
<h2>软件兼容性</h2>
<p>它兼容LEAPS UWBS, Qorvo FiRa兼容UWBS（近距离交互, TWR AoA）, PANS PRO UWBS和第三方协议栈（开放平台）. 默认的固件是LEAPS UWBS，以及 Qorvo FiRa 兼容的演示版。</p>
</div>
<hr class="docutils">
<div class="section" id="electrical-parameters">
<h2>电气参数</h2>
<table class="colwidths-given custom-table docutils align-default">
<colgroup>
<col style="width: 35%">
<col style="width: 65%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>参数</p></th>
<th class="head"><p>价值</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>电池供电</p></td>
<td><p>+3.7V (套件不含电池，建议使用Fenix RCR123A)</p></td>
</tr>
<tr class="row-odd"><td><p>USB C (电源和数据)</p></td>
<td><p>最大 5V @ 500mA</p></td>
</tr>
<tr class="row-even"><td><p>工作温度 (不含电池)</p></td>
<td><p>-40°C - +85°C</p></td>
</tr>
<tr class="row-odd"><td><p>工作温度（带电池）</p></td>
<td><p>-20°C - +45°C</p></td>
</tr>
<tr class="row-even"><td><p>支持的 UWB 频道</p></td>
<td><div class="line-block">
<div class="line">频道 5 (6240-6739.2 MHz, CF=6489.6 MHz)</div>
<div class="line">频道 9 (7738-8237.2 MHz, CF=7987.2 MHz, FiRa 兼容)</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><p>UWB 发射功率</p></td>
<td><div class="line-block">
<div class="line">FCC/ARIB/ETSI: -41.3 dBm/MHz max</div>
<div class="line">ETSI (+10 dB)：-31.3 dBm/MHz max</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>目标精度</p></td>
<td><div class="line-block">
<div class="line">测距精度: +/- 9 [cm]</div>
<div class="line">PDoA 精确度: +/- 5 [度]</div>
<div class="line">AoA 精确度:+/- 2.5 [度]</div>
</div>
</td>
</tr>
</tbody>
</table>
<div class="admonition note">
<p class="admonition-title">注解</p>
<ul class="simple">
<li><p>为实现最低功耗，请切断SWD_DIO跳线。 睡眠电流约为24uA @ 3.7V不切断时，睡眠电流约为270uA @ 3.7V。</p></li>
<li><p>要使用外部Jlink，请切断SWD_DIO跳线。</p></li>
<li><p>其他跳线可以保持不动。</p></li>
</ul>
</div>
</div>
<hr class="docutils">
<div class="section" id="mechanical-parameters">
<h2>机械参数</h2>
<table class="colwidths-given custom-table docutils align-default">
<colgroup>
<col style="width: 35%">
<col style="width: 65%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>参数</p></th>
<th class="head"><p>价值</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>尺寸</p></td>
<td><p>宽=72 x 高=120 x深=30毫米</p></td>
</tr>
<tr class="row-odd"><td><p>重量</p></td>
<td><div class="line-block">
<div class="line">不含电池: 82g</div>
<div class="line">带电池:101g</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>颜色</p></td>
<td><p>LC13 - 灰色, LC14 - 白色</p></td>
</tr>
<tr class="row-odd"><td><p>安装</p></td>
<td><p>兼容1/4”-20螺丝相机支架</p></td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="device-overview">
<h2>设备概述</h2>
<p>以下图片概述了LC13和LC14设备的主要组件。</p>
<p><strong>LC14设备的正面/背面视图</strong></p>
<p><a class="reference internal" href="../../../_images/for-buttons.png"><img alt="pic3" src="/docs-assets/zh-cn/_images/for-buttons.png" style="width: 47%;"></a>   <a class="reference internal" href="../../../_images/for-usb-type-c.png"><img alt="pic4" src="/docs-assets/zh-cn/_images/for-usb-type-c.png" style="width: 44%;"></a></p>
<hr class="docutils">
<p><strong>LC13 设备的正面/背面视图</strong></p>
<a class="reference internal image-reference" href="../../../_images/lc13_device.png"><img alt="../../../_images/lc13_device.png" class="align-center" src="/docs-assets/zh-cn/_images/lc13_device.png" style="width: 477.90000000000003px; height: 389.7px;"></a>
<hr class="docutils">
<p><strong>黑板顶视图</strong></p>
<table class="custom-table-borderless docutils align-center">
<colgroup>
<col style="width: 50%">
<col style="width: 50%">
</colgroup>
<tbody>
<tr class="row-odd"><td><p><a class="reference internal" href="../../../_images/lc14_b2-top-view.png"><img alt="pic1" src="/docs-assets/zh-cn/_images/lc14_b2-top-view.png" style="width: 100%;"></a></p></td>
<td><p><a class="reference internal" href="../../../_images/lc13_b2-top-view.png"><img alt="pic1" src="/docs-assets/zh-cn/_images/lc13_b2-top-view.png" style="width: 93%;"></a></p></td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="safety-instructions">
<h2>安全说明</h2>
<ul class="simple">
<li><p>操作时，请勿将设备暴露在水或湿气中。</p></li>
<li><p>请勿将设备暴露于任何热源。</p></li>
<li><p>请小心操作，避免产品受到机械或电气损坏。</p></li>
</ul>
</div>
<hr class="docutils">
<div class="section" id="warnings">
<h2>警告</h2>
<ul class="simple">
<li><p>本设备只能连接额定电压为5V/0.5A DC的外部电源或 3.7V 电池。</p></li>
<li><p>更换不正确类型的电池可能会破坏保护装置（例如，某些锂电池类型）。</p></li>
<li><p>将电池丢入火中或热炉中，或以机械方式压碎或切割电池，可能会导致爆炸。</p></li>
<li><p>将电池留在周围温度极高的环境中，可能会导致爆炸或易燃液体或气体泄漏。</p></li>
<li><p>将电池置于极低的气压下，可能会导致爆炸或易燃液体或气体泄漏。</p></li>
</ul>
</div>
<hr class="docutils">
<div class="section" id="important-notice">
<h2>重要通知</h2>
<ul class="simple">
<li><p>套件的硬件和软件仅用于演示目的。 如需获得工业级系统，请与我们联系，讨论具体需求和要求。</p></li>
<li><p>有关Qorvo软件工具的更多详细信息，例如Qorvo的FiRa兼容协议栈, Qorvo近距离交互和UWB测距及AoA演示应用，，请参阅 <a class="reference external" href="https://www.qorvo.com">Qorvo网站</a> 上的相应文档或资源。</p></li>
</ul>
<hr class="docutils">
</div>
</div>


           </div>
