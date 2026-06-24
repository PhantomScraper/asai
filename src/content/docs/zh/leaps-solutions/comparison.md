---
title: "比较"
lang: zh
slug: "leaps-solutions/comparison"
section: "leaps-solutions"
sourceUrl: "https://docs.leapslabs.com/zh-cn/leaps-solutions/comparison/"
order: 8
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="comparison">
<span id="comparision"></span><h1>比较</h1>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 19%">
<col style="width: 32%">
<col style="width: 25%">
<col style="width: 24%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>项目</p></th>
<th class="head"><p><a class="reference internal" href="/docs/zh/leaps-rtls#leaps-rtls"><span class="std std-ref">LEAPS RTLS</span></a></p></th>
<th class="head"><p><a class="reference internal" href="/docs/zh/pans-pro-rtls#pans-pro-rtls"><span class="std std-ref">PANS PRO RTLS</span></a></p></th>
<th class="head"><p>PANS RTLS</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>支持的配置文件</p></td>
<td><p>配置文件2, 3, 4, 5</p></td>
<td><p>配置文件0</p></td>
<td><p>配置文件0</p></td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line">固件更新</div>
<div class="line">和维护</div>
</div>
</td>
<td><p>是</p></td>
<td><p>有限</p></td>
<td><p>不</p></td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line">用于生产</div>
<div class="line">部署</div>
</div>
</td>
<td><p>是</p></td>
<td><p>是</p></td>
<td><p>有限</p></td>
</tr>
<tr class="row-odd"><td><p>可扩展性</p></td>
<td><p>完全可扩展</p></td>
<td><p>完全可扩展 <a class="footnote-reference brackets" href="#note-0" id="id1">1</a></p></td>
<td><p>完全可扩展 <a class="footnote-reference brackets" href="#note-1" id="id2">2</a></p></td>
</tr>
<tr class="row-even"><td><p>定位能力</p></td>
<td><div class="line-block">
<div class="line">TWR <a class="footnote-reference brackets" href="#note-2" id="id3">3</a>,</div>
<div class="line">UL-TDoA <a class="footnote-reference brackets" href="#note-3" id="id4">4</a>,</div>
<div class="line">DL-TDoA <a class="footnote-reference brackets" href="#note-4" id="id5">5</a></div>
</div>
</td>
<td><p>仅限TWR</p></td>
<td><p>仅限TWR</p></td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line">最大。更新速率</div>
<div class="line">per tag <a class="footnote-reference brackets" href="#note-5" id="id6">6</a></div>
</div>
</td>
<td><div class="line-block">
<div class="line">TWR 高达 10 Hz</div>
<div class="line">UL-TDoA 最高 50 Hz</div>
<div class="line">DL-TDoA最高 50 Hz</div>
</div>
</td>
<td><p>TWR 高达 10 Hz</p></td>
<td><p>TWR 高达 10 Hz</p></td>
</tr>
<tr class="row-even"><td><p>总更新容量 <a class="footnote-reference brackets" href="#note-5" id="id7">6</a></p></td>
<td><div class="line-block">
<div class="line">TWR 最高 320 Hz</div>
<div class="line">UL-TDoA 最高 700 Hz</div>
<div class="line">DL-TDoA无限制</div>
</div>
</td>
<td><p>TWR 最高 150 Hz</p></td>
<td><p>TWR 最高 150 Hz</p></td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line">最大。 测量值</div>
<div class="line">每次更新</div>
</div>
</td>
<td><p>最多 30 <a class="footnote-reference brackets" href="#note-5" id="id8">6</a></p></td>
<td><p>4</p></td>
<td><p>4</p></td>
</tr>
<tr class="row-even"><td><p>数据服务器</p></td>
<td><p>高级</p></td>
<td><p>高级</p></td>
<td><p>基本 (重复过滤)</p></td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line">数据延迟</div>
<div class="line">服务器上</div>
</div>
</td>
<td><p>50 ms <a class="footnote-reference brackets" href="#note-5" id="id9">6</a></p></td>
<td><p>更新率 + 50ms</p></td>
<td><p>更新率 + 50ms</p></td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line">数据延迟</div>
<div class="line">在设备上</div>
</div>
</td>
<td><p>&lt; 10ms</p></td>
<td><p>&lt; 10ms</p></td>
<td><p>&lt; 10ms</p></td>
</tr>
<tr class="row-odd"><td><p>服务器应用程序接口</p></td>
<td><p>MQTT</p></td>
<td><p>MQTT</p></td>
<td><p>MQTT</p></td>
</tr>
<tr class="row-even"><td><p>设备 API</p></td>
<td><p>UART, SPI, USB, Bluetooth</p></td>
<td><p>UART, SPI, Bluetooth</p></td>
<td><p>UART, SPI, Bluetooth</p></td>
</tr>
<tr class="row-odd"><td><p>Bluetooth API</p></td>
<td><p>高级 (统一 API)</p></td>
<td><p>传统</p></td>
<td><p>传统</p></td>
</tr>
<tr class="row-even"><td><p>Bluetooth安全</p></td>
<td><p>是</p></td>
<td><p>不</p></td>
<td><p>不</p></td>
</tr>
<tr class="row-odd"><td><p>工具</p></td>
<td><p>用于 Android 和 iOS 的 LEAPS Manager.  <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> 用于 Windows/Linux/macOS 的 WebApp。</p></td>
<td><p>用于 Android 的 PANS PRO Manager. 适用于 Windows/Linux/macOS 的 LEAPS Center WebApp。</p></td>
<td><p>适用于 Android 的 DRTLS Manager. Windows/Linux/macOS 的 Basic WebApp。</p></td>
</tr>
<tr class="row-even"><td><div class="line-block">
<div class="line">兼容</div>
<div class="line">PANS RTLS</div>
</div>
</td>
<td><p>不</p></td>
<td><p>是</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-odd"><td><p>系统更新</p></td>
<td><p>是</p></td>
<td><p>错误修正</p></td>
<td><p>不</p></td>
</tr>
<tr class="row-even"><td><p>长期支持</p></td>
<td><p>是</p></td>
<td><p>错误修正</p></td>
<td><p>不</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
<dl class="footnote brackets">
<dt class="label" id="note-0"><span class="brackets"><a class="fn-backref" href="#id1">1</a></span></dt>
<dd><p>当使用 LC5A 工业网关时</p>
</dd>
<dt class="label" id="note-1"><span class="brackets"><a class="fn-backref" href="#id2">2</a></span></dt>
<dd><p>用户必须使用 Raspberry Pi 3B 作为网关设备</p>
</dd>
<dt class="label" id="note-2"><span class="brackets"><a class="fn-backref" href="#id3">3</a></span></dt>
<dd><p>双向测距</p>
</dd>
<dt class="label" id="note-3"><span class="brackets"><a class="fn-backref" href="#id4">4</a></span></dt>
<dd><p>上行链路到达时差</p>
</dd>
<dt class="label" id="note-4"><span class="brackets"><a class="fn-backref" href="#id5">5</a></span></dt>
<dd><p>下行链路到达时间差</p>
</dd>
<dt class="label" id="note-5"><span class="brackets">6</span><span class="fn-backref">(<a href="#id6">1</a>,<a href="#id7">2</a>,<a href="#id8">3</a>,<a href="#id9">4</a>)</span></dt>
<dd><p>取决于网络配置文件和测量模式</p>
</dd>
</dl>
<hr class="docutils">
</div>


           </div>
