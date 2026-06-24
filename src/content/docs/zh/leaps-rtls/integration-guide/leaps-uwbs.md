---
title: "LEAPS UWBS"
lang: zh
slug: "leaps-rtls/integration-guide/leaps-uwbs"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/leaps-rtls/integration-guide/leaps-uwbs/"
order: 66
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-uwbs">
<span id="leapsuwbs"></span><h1>LEAPS UWBS</h1>
<p><a class="reference external" href="https://www.leapslabs.com/">LEAPS</a> UWBS是一个完全嵌入式和先进的UWB子系统，涵盖了广泛的用例。一个UWB子系统可配置为不同的模式和配置文件。UWBS可以作为锚点、标签或网关运行。网络配置文件具有高容量和低功耗的完全可扩展性。</p>
<hr class="docutils">
<div class="section" id="software-architecture">
<h2>软件架构</h2>
<div class="figure align-center" id="id1">
<a class="reference internal image-reference" href="../../../_images/leaps_uwbs.png"><img alt="../../../_images/leaps_uwbs.png" src="/docs-assets/zh-cn/_images/leaps_uwbs.png" style="width: 730.8000000000001px; height: 657.9px;"></a>
<p class="caption"><span class="caption-text"><a class="reference external" href="https://www.leapslabs.com/">LEAPS</a> UWBS架构</span></p>
</div>
</div>
<hr class="docutils">
<div class="section" id="key-features">
<h2>主要功能</h2>
<ul class="simple">
<li><p>多功能性使平衡系统需求、成本、部署时间和维护复杂性变得容易。应用范围从简单的距离接近到高速跟踪或无限接收器的导航。</p></li>
<li><p>它集成了一个复杂的UWBMAC，允许基础设施设备的自适应集群、空中时间重用、时隙分配等。可扩展、经过验证的碰撞检测、碰撞避免和碰撞解决使系统能够在复杂环境中稳健运行。</p></li>
<li><p>支持的测量技术包括 TWR, DL-TDoA 和 UL-TDoA. 集成的定位引擎允许设备在导航模式下使用DL-TDoA或TWR独立运行。</p></li>
<li><p>卓越的电源管理为TWR和TDoA模式提供了较长的电池寿命。</p></li>
</ul>
</div>
<hr class="docutils">
<div class="section" id="used-terminology">
<h2>使用术语</h2>
<ul class="simple">
<li><p><strong>锚点</strong>:有固定位置。</p></li>
<li><p><strong>标签</strong>:更改位置，在锚点的帮助下动态确定位置。</p></li>
<li><p><strong>网关</strong>:提供有关网络节点的状态信息（读取/自检），缓存节点信息，甚至可能收集数据和跟踪历史，为应用层提供与UWB网络元素交互的方法（也称为 <em>交互代理</em>）。</p></li>
<li><p><strong>节点</strong>:网络节点（锚点、标签、网关等）。</p></li>
<li><p><strong>LE</strong>:定位引擎。</p></li>
<li><p><strong>CORE_INT:</strong> 固件保留的GPIO引脚，用于通知用户新的UART/SPI接口事件。</p></li>
<li><p><strong>TLV:</strong> 类型长度值编码。</p></li>
<li><p><strong>UWBS</strong> UWB子系统。</p></li>
</ul>
</div>
<hr class="docutils">
<div class="section" id="uwb-rf">
<h2>超宽带射频</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 12%">
<col style="width: 17%">
<col style="width: 20%">
<col style="width: 20%">
<col style="width: 31%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"></th>
<th class="head"><p><a class="reference internal" href="/docs/zh/leaps-rtls#leaps-rtls"><span class="std std-ref">LEAPS RTLS</span></a> ,
<a class="reference internal" href="/docs/zh/pans-pro-rtls#pans-pro-rtls"><span class="std std-ref">PANS PRO RTLS</span></a> ,
PANS v2.0</p></th>
<th class="head"><p><a class="reference internal" href="/docs/zh/leaps-rtls#leaps-rtls"><span class="std std-ref">LEAPS RTLS</span></a>,
<a class="reference internal" href="/docs/zh/pans-pro-rtls#pans-pro-rtls"><span class="std std-ref">PANS PRO RTLS</span></a></p></th>
<th class="head"><p>Qorvo FiRa</p></th>
<th class="head"><p>自定义堆栈（DW3000 RF）</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>频道</p></td>
<td><p>5</p></td>
<td><p>5,9</p></td>
<td><p>9</p></td>
<td><p>5,9</p></td>
</tr>
<tr class="row-odd"><td><p>PRF</p></td>
<td><p>64M</p></td>
<td><p>64M</p></td>
<td><p>64M</p></td>
<td><p>16M, 64M</p></td>
</tr>
<tr class="row-even"><td><p>前导码长度</p></td>
<td><p>128</p></td>
<td><p>128</p></td>
<td><p>64</p></td>
<td><p>32, 64, 72, 128, 256, 512, 1024, 1536, 2048, 4096</p></td>
</tr>
<tr class="row-odd"><td><p>PAC Size</p></td>
<td><p>8</p></td>
<td><p>8</p></td>
<td><p>8</p></td>
<td><p>4, 8, 16, 32</p></td>
</tr>
<tr class="row-even"><td><p>Rx代码</p></td>
<td><p>9</p></td>
<td><p>9</p></td>
<td><p>9</p></td>
<td><p>1-29 (PRF16: 1-8; PRF64: 9-24)</p></td>
</tr>
<tr class="row-odd"><td><p>Tx代码</p></td>
<td><p>9</p></td>
<td><p>9</p></td>
<td><p>9</p></td>
<td><p>1-29 (PRF16: 1-8; PRF64: 9-24)</p></td>
</tr>
<tr class="row-even"><td><p>SFD类型</p></td>
<td><p>IEEE 802.15.4短8符号</p></td>
<td><p>IEEE 802.15.4短8符号</p></td>
<td><p>IEEE 802.15.4z定义了8个符号</p></td>
<td><p>IEEE 802.15.4短8符号、十波定义的8符号、十六波定义的16符号、IEEE 802.15.4z定义的8字符</p></td>
</tr>
<tr class="row-odd"><td><p>数据速率</p></td>
<td><p>6.8 Mbit/s</p></td>
<td><p>6.8 Mbit/s</p></td>
<td><p>6.8 Mbit/s</p></td>
<td><p>6.8Mbit/s, 850kbits/s</p></td>
</tr>
<tr class="row-even"><td><p>PHR模式</p></td>
<td><p>DW专有扩展帧PHR模式</p></td>
<td><p>DW专有扩展帧PHR模式</p></td>
<td><p>标准</p></td>
<td><p>标准、扩展（DW专有扩展帧PHR模式）</p></td>
</tr>
<tr class="row-odd"><td><p>PHR费率</p></td>
<td><p>标准</p></td>
<td><p>标准</p></td>
<td><p>标准</p></td>
<td><p>标准，PHR数据速率（6M81）</p></td>
</tr>
<tr class="row-even"><td><p>SFD超时</p></td>
<td><p>129</p></td>
<td><p>129</p></td>
<td><p>65</p></td>
<td><p>可配置</p></td>
</tr>
<tr class="row-odd"><td><p>STS模式</p></td>
<td><p><cite>-</cite></p></td>
<td><p>OFF</p></td>
<td><p>OFF</p></td>
<td><p>关闭，1，2，无数据，超确定性代码</p></td>
</tr>
<tr class="row-even"><td><p>STS长度</p></td>
<td><p><cite>-</cite></p></td>
<td><p>0</p></td>
<td><p>0</p></td>
<td><p>32, 64, 128, 256, 512, 1024, 2048</p></td>
</tr>
<tr class="row-odd"><td><p>PDOA模式</p></td>
<td><p><cite>-</cite></p></td>
<td><p>M0</p></td>
<td><p>M1</p></td>
<td><p>M0, M1, M3</p></td>
</tr>
<tr class="row-even"><td rowspan="2"><p>支持的硬件</p></td>
<td><p><cite>超宽带集成电路:</cite> DW1000</p></td>
<td><p><cite>超宽带集成电路:</cite> DW3000系列、QM33系列</p></td>
<td><p><cite>超宽带集成电路:</cite> DW3000系列、QM33系列</p></td>
<td><p><cite>超宽带集成电路:</cite> DW3000系列、QM33系列</p></td>
</tr>
<tr class="row-odd"><td><p><cite>模块:</cite> DWM1001C</p></td>
<td><p><cite>模块:</cite> DWM3001C，村田2AB型</p></td>
<td><p><cite>模块:</cite> DWM3001C，村田2AB型</p></td>
<td><p><cite>模块:</cite> DWM3001C，村田2AB型</p></td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="ble-rf">
<h2>BLE RF</h2>
<p>我们支持2M PHY，频带为2.4GHz，40个频道，间距为2MHz（更多详细信息请参见BLE规范5.3）。</p>
</div>
</div>


           </div>
