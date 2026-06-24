---
title: "BLE 接口"
lang: zh
slug: "pans-pro-rtls/integration-guide/ble-inteface"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/pans-pro-rtls/integration-guide/ble-inteface/"
order: 97
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="ble-interface">
<span id="pans-ble-interface"></span><h1>BLE 接口</h1>
<p>在 BLE API 设计中，DWM 模块作为 BLE 外围设备，可以通过 API 与 BLE 中央设备通信. 本文档介绍了 BLE 中央设备可用于通信的 API. 此外，还提供了 Android 应用程序和 PANS PRO Manager 来使用 BLE API。</p>
<p>BLE 中央装置可直接与网络节点连接，以设置和检索参数。 它需要单独连接到每个设备进行配置/控制。</p>
<p>在 BLE 方案中，提供正常的 GATT 操作，包括读取, 写入和通知。</p>
<blockquote>
<div><div class="figure align-default">
<a class="reference internal image-reference" href="../../../_images/image31.png"><img alt="../../../_images/image31.png" src="/docs-assets/zh-cn/_images/image31.png" style="width: 5.70833in; height: 2.01111in;"></a>
</div>
</div></blockquote>
<p>上图显示，DWM1001 BLE 事件处理程序将 GATT 操作转换为通用 API 命令。 同时，当发生 BLE 相关事件时，BLE 事件处理程序会向 BLE 客户端发送相应的通知。</p>
<p>详细的 BLE API 介绍，请参阅 <em>BLE API</em> 章节。</p>
<hr class="docutils">
<div class="section" id="le-gatt-model">
<h2>LE GATT模型</h2>
<p><strong>网络节点服务</strong> 的UUID为 <strong>680c21d9-c946-4c1f-9c11-baa1c21329e7</strong>. 根据 BLE 规范的建议，所有特征值均以小字尾编码。</p>
<div class="section" id="network-node-characteristics">
<h3>网络节点特征</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 28%">
<col style="width: 15%">
<col style="width: 11%">
<col style="width: 38%">
<col style="width: 8%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>uuid</p></th>
<th class="head"><p>名称</p></th>
<th class="head"><p>长度</p></th>
<th class="head"><p>价值</p></th>
<th class="head"><p>标志</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>“标准 GAP 服务，标签 0x2A00”</p></td>
<td><p>标签</p></td>
<td><p>Var</p></td>
<td><p>UTF-8 编码字符串</p></td>
<td><p>RW</p></td>
</tr>
<tr class="row-odd"><td><p>3f0afd88-7770-46b0-b5e7-9fc099598964</p></td>
<td><p>操作模式</p></td>
<td><p>2字节</p></td>
<td><p>有关数据编码的详情，请参阅下面的章节</p></td>
<td><p>RW</p></td>
</tr>
<tr class="row-even"><td><p>80f9d8bc-3bff-45bb-a181-2d6a37991208</p></td>
<td><p>网络 ID</p></td>
<td><p>2字节</p></td>
<td><p>网络的唯一标识 (PAN ID)</p></td>
<td><p>RW</p></td>
</tr>
<tr class="row-odd"><td><p>a02b947e-df97-4516-996a-1882521e0ead</p></td>
<td><p>位置数据模式</p></td>
<td><p>1字节</p></td>
<td><p>0 - 位置 1 - 距离 2 - 位置 + 距离</p></td>
<td><p>RW</p></td>
</tr>
<tr class="row-even"><td><p>003bbdf2-c634-4b3d-ab56-7ec889b89a37</p></td>
<td><p>位置数据</p></td>
<td><p>最大106字节</p></td>
<td><p>有关数据编码的详情，请参阅下面的章节</p></td>
<td><p>RO</p></td>
</tr>
<tr class="row-odd"><td><p>f4a67d7d-379d-4183-9c03-4b6ea5103291</p></td>
<td><p>代理位置</p></td>
<td><p>最大 76 字节</p></td>
<td><p>模块用于通知 BLE 中心的新标签位置</p></td>
<td><p>RO</p></td>
</tr>
<tr class="row-even"><td><p>1e63b1eb-d4ed-444e-af54-c1e965192501</p></td>
<td><p>设备信息</p></td>
<td><p>29 字节</p></td>
<td><p>节点 ID (8 字节), 硬件版本 (4 字节), FW1 版本 (4 字节), FW2 版本 (4 字节), FW1 校验和 (4 字节), FW2 校验和 (4 字节), RDonly 操作标志 (1 字节)</p></td>
<td><p>RO</p></td>
</tr>
<tr class="row-odd"><td><p>1e630001-d4ed-444e-af54-c1e965192501
[PANS PRO]</p></td>
<td><p>设备状态</p></td>
<td><p>8字节</p></td>
<td><p>正常运行时间（4 字节，无符号整数），电池电量（1 字节，无符号整数），保留（1 字节），温度（2 字节，整数）</p></td>
<td><p>RO</p></td>
</tr>
<tr class="row-even"><td><p>0eb2bc59-baf1-4c1c-8535-8a0204c69de5</p></td>
<td><p>统计</p></td>
<td><p>120字节</p></td>
<td><p>节点统计</p></td>
<td><p>RO</p></td>
</tr>
<tr class="row-odd"><td><p>5955aa10-e085-4030-8aa6-bdfac89ac32b</p></td>
<td><p>FW 更新推送</p></td>
<td><p>最多 37 字节</p></td>
<td><p>用于向模块（BLE 外围设备）发送结构化数据（FW 更新数据包），其大小根据最大传输单位（MTU）设置。 有关数据编码的详情，请参阅以下部分。</p></td>
<td><p>WO</p></td>
</tr>
<tr class="row-even"><td><p>9eed0e27-09c0-4d1c-bd92-7c441daba850</p></td>
<td><p>FW更新投票</p></td>
<td><p>9字节</p></td>
<td><p>模块用作 BLE 中心的响应/通知。 有关数据编码的详情，请参阅以下部分。</p></td>
<td><p>RO</p></td>
</tr>
<tr class="row-odd"><td><p>ed83b848-da03-4a0a-a2dc-8b401080e473</p></td>
<td><p>断开连接</p></td>
<td><p>1字节</p></td>
<td><p>用于通过写入 value=1 来明确断开与 BLE 外围设备的连接（因 Android 行为而产生的变通方法）</p></td>
<td><p>WO</p></td>
</tr>
<tr class="row-even"><td><p>“5b10c428-af2f-486f-aee1-9dbd79b6bccb [已修改PANS PRO]”</p></td>
<td><p>锚点列表</p></td>
<td><p>65字节</p></td>
<td><p>计数（1 字节）, 节点 ID 列表（2 字节）, RSSI（1 字节）, 位置（1 字节） 列表中最多 16 个元素</p></td>
<td><p>RO</p></td>
</tr>
<tr class="row-odd"><td><p>9d5ab03b-cbf8-4ae5-9f11-63e45f538ada</p></td>
<td><p>AES 密钥</p></td>
<td><p>16字节</p></td>
<td><p>AES 对称密钥 将在 R2 中实现</p></td>
<td><p>RW</p></td>
</tr>
</tbody>
</table>
<div class="admonition note">
<p class="admonition-title">注解</p>
<p>标签特性是一个特殊特性。 它是标准 “名称” 特性（0x2A00）下标准强制 GAP 服务（0x1800）的一部分。</p>
</div>
</div>
<div class="section" id="operation-mode-characteristic">
<h3>操作模式特性</h3>
<p>运行模式特征为 2 个字节，包含节点的配置信息。 格式定义如下:</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 50%">
<col style="width: 50%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="2"><p><strong>第 1 个字节（第 7 位降为 0）</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Bit</p></td>
<td><p>价值</p></td>
</tr>
<tr class="row-odd"><td><p>7</p></td>
<td><p>标签 (0)，锚 (#。</p></td>
</tr>
<tr class="row-even"><td><p>6 - 5</p></td>
<td><p>UWB - 关闭 (0)，被动 (#。)，主动 (2)</p></td>
</tr>
<tr class="row-odd"><td><p>4</p></td>
<td><p>固件 1（0），固件 2（#。</p></td>
</tr>
<tr class="row-even"><td><p>3</p></td>
<td><p>启动加速度计 (0, #。</p></td>
</tr>
<tr class="row-odd"><td><p>2</p></td>
<td><p>启用 LED 指示灯 (0, #。</p></td>
</tr>
<tr class="row-even"><td><p>1</p></td>
<td><p>启用固件更新 (0, #。</p></td>
</tr>
<tr class="row-odd"><td><p>0</p></td>
<td><p>启用 BLE (0,#。</p></td>
</tr>
</tbody>
</table>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 46%">
<col style="width: 54%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="2"><p><strong>第 2 字节（第 7 位降为 0）</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Bit</p></td>
<td><p>价值</p></td>
</tr>
<tr class="row-odd"><td><p>7</p></td>
<td><p>启用启动器，特定锚点（0，#。</p></td>
</tr>
<tr class="row-even"><td><p>6</p></td>
<td><p>启用低功耗模式，特定标签（0, #。</p></td>
</tr>
<tr class="row-odd"><td><p>5</p></td>
<td><p>启用位置引擎，特定标签（0, #。</p></td>
</tr>
<tr class="row-even"><td><p>4 - 0</p></td>
<td><p>保留</p></td>
</tr>
</tbody>
</table>
</div>
<div class="section" id="location-data-characteristic">
<h3>位置数据特征</h3>
<p>位置数据特征可包含位置, 距离或两者. 位置和距离的格式定义如下：</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 47%">
<col style="width: 53%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>类型（1 字节）</p></th>
<th class="head"><p>价值</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>0 - 仅位置</p></td>
<td><p>X,Y,Z坐标（各 4 字节）+ 质量因子（1 字节），大小:13 字节</p></td>
</tr>
<tr class="row-odd"><td><p>1 - 距离</p></td>
<td><p>第一个字节是距离计数（1 字节）。</p>
<p>节点 ID（2 字节）, 距离（4 字节）和质量因子（1 字节）的序列。</p>
<p>最大值包含 15 个元素，大小：8 - 106。</p>
</td>
</tr>
<tr class="row-even"><td><p>2 - 位置和距离</p></td>
<td><p>编码位置（如上所述，13 字节） 编码距离（如上所述，8 - 29 字节） - 位置和距离由标签发送，测距锚的数量最多为 4 个。</p></td>
</tr>
</tbody>
</table>
<div class="admonition note">
<p class="admonition-title">注解</p>
<p>特征值可能完全为空（长度为零），这意味着既没有已知的位置，也没有已知的距离。</p>
</div>
<div class="admonition note">
<p class="admonition-title">注解</p>
<p>虽然定位数据模式包括位置和距离，但在位置未知的情况下，仍有可能在特征值中只接收距离。</p>
</div>
</div>
<hr class="docutils">
<div class="section" id="proxy-positions-characteristic">
<h3>代理位置特性</h3>
<p>提供此特性是为了克服同时连接节点到 BLE 中央（移动设备）的限制。 被动节点会使用此特性来串流/通知标签位置更新。</p>
<p>此特性的数据编码如下:</p>
<ul class="simple">
<li><p>1字节：元素数量（最多5个）</p></li>
<li><p>[序列] 标记位置：2 字节节点 ID，13 字节位置</p></li>
</ul>
<p>因此，5 个标签位置的最大长度为 76 字节。</p>
</div>
<hr class="docutils">
<div class="section" id="anchor-specific-characteristics">
<h3>锚点特有的特征</h3>
<p>锚点可以在称为 ‘关接器’和‘启动器’的特殊模式下运作。 这两种模式是正交的，互不影响。 关接标志是只读的，而用户可以设置启动器。 此外，每个锚点在其群组内都有一个席位编号。</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 20%">
<col style="width: 20%">
<col style="width: 20%">
<col style="width: 20%">
<col style="width: 20%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>UUID</p></th>
<th class="head"><p>名称</p></th>
<th class="head"><p>长度</p></th>
<th class="head"><p>价值</p></th>
<th class="head"><p>标志</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><strong>3f0af
d88-7770-46
b0-b5
e7-9fc09959
8964</strong></p></td>
<td><p>操作模式 (见上文)</p></td>
<td><p>2字节</p></td>
<td><p>第 2 个字节的第 7 位：</p>
<p>启动器使能(0，#.(详见 “操作模式” 小节),</p>
</td>
<td><p>RW</p></td>
</tr>
<tr class="row-odd"><td><p><strong>1e63
b1eb-d4ed-4
44e-a
f54-c1e9651
92501</strong></p></td>
<td><p>设备信息（见上文）</p></td>
<td></td>
<td><p>仅限 RD</p>
<p>操作标志: BXXXXXXX B:网关 1/0</p>
</td>
<td><p>RO</p></td>
</tr>
<tr class="row-even"><td><p><strong>f0f26c
9b-2c8c-49a
c-ab6
0-fe03def1b
40c</strong></p></td>
<td><dl class="simple">
<dt>持续</dt><dd><p>位置</p>
</dd>
</dl>
</td>
<td><p>13字节</p></td>
<td><blockquote>
<div><p>X,Y,Z</p>
</div></blockquote>
<p>每个 4 字节精度 + 质量因子（1 字节，值 1 - 100）的坐标</p>
</td>
<td><p>WO</p></td>
</tr>
<tr class="row-odd"><td><p><strong>28d0
1d60-89de-4
bfa-b
6e9-651ba59
6232c</strong></p></td>
<td><p>MAC 统计</p></td>
<td><p>4字节</p></td>
<td><p>保留用于内部调试 MAC 统计</p></td>
<td><p>RO</p></td>
</tr>
<tr class="row-even"><td><p><strong>17b16
13e-98f2-44
36-bc
de-23af17a1
0c72</strong></p></td>
<td><p>集群信息</p></td>
<td><p>5字节</p></td>
<td><p>席位编号（1字节）/群集地图（2字节）/群集邻居地图（2字节）</p></td>
<td><p>RO</p></td>
</tr>
<tr class="row-odd"><td><p><strong>5b10c4
28-af2f-486
f-aee
1-9dbd79b6b
ccb</strong>
<strong>[Not in
PANS</strong>
<strong>PRO]</strong></p></td>
<td><p>锚点列表</p></td>
<td><p>65字节</p></td>
<td><p>计数（1 字节），节点 ID 列表（2 字节），RSSI（1 字节），席位（1 字节） 列表中最多 16 个元素 [PANS PRO 中不再提供，因为它不再针对特定锚点]</p></td>
<td><p>RO</p></td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="tag-specific-characteristics">
<h3>标签特定特征</h3>
<p>每个标签都会根据周围 4 个锚点发送的信息来确定自己的位置。 标签会提供关于如何计算其位置的完整信息（只读）。</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 20%">
<col style="width: 20%">
<col style="width: 20%">
<col style="width: 20%">
<col style="width: 20%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>UUID</p></th>
<th class="head"><p>名称</p></th>
<th class="head"><p>长度</p></th>
<th class="head"><p>价值</p></th>
<th class="head"><p>标志</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><strong>3f0a
fd88-7770-4
6b0-
b5e7-9fc099
598964</strong></p></td>
<td><p>操作模式 (见上文)</p></td>
<td><p>2字节</p></td>
<td><p>第 2 个字节中的第 6 位:启用低功耗模式（0，#。 第 2 个字节中的第 5 位：位置引擎启用（0，#。 详见操作模式特性小节）</p></td>
<td><p>RW</p></td>
</tr>
<tr class="row-odd"><td><p><strong>7bd4
7f30-5602-4
389
-b069-83057
31308b6</strong></p></td>
<td><p>更新率</p></td>
<td><p>8字节</p></td>
<td><p>布局： U1 (4 字节), U2 (4 字节) 移动时每 <em>U1</em> 毫秒广播一次新位置，静止时每 <em>U2</em> 毫秒广播一次新位置。</p></td>
<td><p>RW</p></td>
</tr>
</tbody>
</table>
</div>
</div>
<hr class="docutils">
<div class="section" id="ble-auto-positioning">
<h2>BLE 自动定位</h2>
<p>BLE API 也能启动自动定位程序。 自动定位过程会在移动设备上完成（计算位置）。 BLE API 可启动距离测量和检索。 工作流程如下:</p>
<ol class="arabic">
<li><p>测量:</p>
<blockquote>
<div><ol class="loweralpha simple">
<li><p>找到并验证启动器（节点必须是 <em>真正的启动器</em>，<em>而不仅仅是</em> 配置 <em>为启动器</em>）。</p></li>
<li><p>启动程序/网络已进入测量距离模式：</p>
<ol class="lowerroman simple">
<li><p>确保位置数据模式被配置为距离或位置和距离。</p></li>
<li><p>开始观测位置数据特征（设置ccccd通知）。</p></li>
<li><p>接收来自启动器的所有测量距离，并将测量距离保存到矩阵中。</p></li>
<li><p>停止观测。</p></li>
</ol>
</li>
<li><p>检索所有其他（非启动器）节点的距离:</p>
<ol class="lowerroman simple">
<li><p>连接。</p></li>
<li><p>确保位置数据模式配置为距离或位置和距离。</p></li>
<li><p>直接读取存储在位置数据特征中的值，并将测量的距离保存到矩阵中</p></li>
<li><p>断开连接。</p></li>
</ol>
</li>
</ol>
</div></blockquote>
</li>
<li><p>评估:评估测量距离, 检查正交性并计算位置。</p></li>
<li><p>将计算出的位置保存到节点（应用户要求）。</p></li>
</ol>
</div>
<hr class="docutils">
<div class="section" id="ble-advertisements">
<h2>BLE 广告</h2>
<p>BLE 广告是外围设备让他人知道其存在的常用方式。 根据 BLE 规范，广播有效载荷由三连串组成，即 [长度, 类型, &lt;数据&gt;]。 锚点和标签将广播有关其 <strong>存在和运行模式</strong> 的基本信息。 BLE 广告的长度不足以同时包含位置信息。</p>
<p>在BLE广告中，使用了 31 字节:</p>
<ul class="simple">
<li><p>3 字节为强制标志（一个 AD 三字节）。</p></li>
<li><p>应用程序可以使用剩余的 28 个字节来填写 AD 记录（每条记录有 2 个字节的长度+类型开销）。</p></li>
</ul>
<div class="section" id="presence-broadcast">
<h3>存在广播</h3>
<p>DWM 模块上的 BLE 采用可连接的非定向模式工作。 它发布的存在广播包含服务可用性和一些服务数据。 存在广播遵循 BLE 广告帧结构，使用 28 个字节来呈现信息。</p>
<p>由于 “存在” 是一个将可连接标志设置为 true 的广播，因此这里必须包含一个 8 字节的本地名称 AD 短记录，以克服潜在的 Android BLE 堆栈错误（如 <em>[1]</em> 所述）。 其余字节填充服务数据: 2 字节的 AD 记录头, 16 字节的 UUID, 1 字节的缩短操作模式和 1 字节的更改计数器。</p>
<p>存在广播帧共有 3 + 20 + 8 字节，即 31字节（共31字节）。</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 42%">
<col style="width: 58%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>AD三字节 - 部件标识</strong></p></th>
<th class="head"><p><strong>价值</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>LEN</p></td>
<td><p>0x02</p></td>
</tr>
<tr class="row-odd"><td><p>类型</p></td>
<td><p>0x01 (标志)</p></td>
</tr>
<tr class="row-even"><td><p>价值</p></td>
<td><p>设备/广告标志 - 可连接</p></td>
</tr>
<tr class="row-odd"><td><p>LEN</p></td>
<td><p>0x13（十进制为 19）</p></td>
</tr>
<tr class="row-even"><td><p>类型</p></td>
<td><p>0x21 (SERVICE_DAT).</p></td>
</tr>
<tr class="row-odd"><td rowspan="3"><p>价值</p></td>
<td><dl class="simple">
<dt>680c21d9-c946-4c1f-9c11-baa1c21329e7</dt><dd><p>（16 字节）</p>
</dd>
</dl>
</td>
</tr>
<tr class="row-even"><td><p>Bit layout: OXXEFFUU （1 字节） O - 运行模式（标记 0，锚 #. XX - 保留 E - 错误指示 FF - 标志:启动器, 网关 UU - UWB:关闭 (0), 被动 (#.), 主动 (2)</p></td>
</tr>
<tr class="row-odd"><td><p>更改计数器（1 字节） - 每次更改特征时，更改计数器都会更改（节点统计除外，特别是标签:位置数据#。。</p></td>
</tr>
<tr class="row-even"><td><p>LEN</p></td>
<td><p>0x07 (最大值)</p></td>
</tr>
<tr class="row-odd"><td><p>类型</p></td>
<td><p>0x08 (本地名称缩写)</p></td>
</tr>
<tr class="row-even"><td><p>价值</p></td>
<td><p>根据 GATT 规范定义的设备本地名称的前 6 字母（或更少）。</p></td>
</tr>
</tbody>
</table>
</div>
</div>
<hr class="docutils">
<div class="section" id="ble-firmware-update">
<h2>BLE 固件更新</h2>
<p>固件更新功能用于更新模块的固件. 它可以通过 UWB 或 BLE 执行. 本节将介绍 BLE 的控制和数据流。</p>
<p>在固件更新过程中，<strong>固件更新推送</strong> 和 <strong>固件更新轮询</strong> 这两个特性用于实现请求/响应协议。</p>
<p><strong>启动 FW 更新</strong></p>
<p>步骤：</p>
<ol class="arabic simple">
<li><p>移动设备*（BLE 中央）会在 <strong>FW 更新轮询</strong> 特征变化（CCCD）时设置指示。</p></li>
<li><p><em>移动设备</em> 通过向 <strong>FW更新推送</strong> 特性发送更新请求/offer数据包，询问网络节点是否愿意执行更新。 该初始化数据包包含固件版本, 校验和以及固件二进制总大小（以字节为单位）。 这个过程是可靠的写入，也称为带响应的写入。</p></li>
</ol>
<ol class="arabic simple" start="3">
<li><p>在两种情况下，<em>网络节点</em> 会对 <em>固件更新轮询</em> 作出有指示的响应:</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>情况1:是,“给我发送第一个数据缓冲区”。 更多信息，请参阅 <em>传输FW二进制</em> 章节；</p></li>
<li><p>情况 2:否，并且 <em>错误代码</em> 提供了拒绝原因。</p></li>
</ul>
</div></blockquote>
<p>错误状态:</p>
<p><strong>移动设备</strong>:收到明确的 “NO” 指示以及错误代码/原因。 <strong>解决方法</strong>： <em>移动设备</em> 在 <em>FW 更新轮询</em> 上禁用 CCCD 指示，并将拒绝原因通知上层。 <strong>网络节点</strong>： 突然断开连接 <strong>解决方法</strong>： 离开 FW 更新模式并重置当前状态，就像 FW 更新没有发生一样。 <strong>移动设备</strong>： 检测到连接已关闭。 <strong>解决方法</strong>： 重试。 如果在 FW 更新初始化 30 秒后仍未成功，则向上层报告。 让用户根据要求重新启动固件更新。</p>
<hr class="docutils">
<div class="section" id="transmitting-the-fw-binary">
<h3>传输 FW 二进制文件</h3>
<p>本节受 <em>[2]</em> 启发。</p>
<p>网络节点启动数据传输，并准确地告诉移动设备它需要哪个数据缓冲区。 这种通信是通过 <em>FW 缓冲区请求</em>：大小和偏移量来完成的。 移动设备使用写命令开始以小块形式发送所请求的缓冲区，不需要回应，因此不涉及完整的往返。 基本分块大小等于 MTU，以适合单个传输数据包。 小块包括：</p>
<ul class="simple">
<li><p>数据:大小应四舍五入为 2 的幂。 当前的数据块大小设置为 32 字节。</p></li>
<li><p>相对偏移（从最开始）:4 字节。</p></li>
<li><p>信息类型标识: FIRMWARE_DATA_CHUNK (= 0x1):1字节</p></li>
</ul>
<p>网络节点完全驱动数据传输。 数据缓冲发送完毕后，移动设备等待进一步的指令。 在传输过程中，网络节点通常会按顺序一个接一个地请求数据缓冲区，以获得固件的连续字节序列。 例如，如果出现异常情况，特别是当前缓冲区传输失败时，节点可能会请求一个意外的缓冲区。</p>
<p>错误状态:</p>
<p><strong>网络节点</strong>:接收数据时缺少数据块（非连续序列），或数据块顺序不对。 <strong>解决方法</strong>:发送 <em>FW 缓冲请求</em>，指定丢失的数据块和缓冲区的其余部分。 <strong>移动设备</strong>：在数据传输过程中收到 <em>FW 缓冲请求</em>。 <strong>解决方法</strong>:停止发送数据，将当前偏移量设置为 <em>FW 缓冲请求</em> 中的偏移量，然后重新开始数据传输。</p>
</div>
<hr class="docutils">
<div class="section" id="finishing-the-transmission">
<h3>完成传输</h3>
<p>一旦成功接收到最后一个数据缓冲区，网络节点将通过 <em>FW更新轮询</em> 的指示，告知移动设备已收到完整的二进制固件。</p>
<p>收到后，移动设备会</p>
<ul class="simple">
<li><p>断开与网络节点的连接。</p></li>
<li><p>等待 500 毫秒。</p></li>
<li><p>尝试再次连接网络节点并检查其固件状态。</p></li>
</ul>
</div>
<hr class="docutils">
<div class="section" id="fw-update-push-poll-format">
<h3>固件更新推送/轮询格式</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 28%">
<col style="width: 14%">
<col style="width: 14%">
<col style="width: 15%">
<col style="width: 16%">
<col style="width: 14%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="6"><p>FW 更新推送</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>更新提议/请求- 固件元</p></td>
<td><p>类型 == 0 (1 字节)</p></td>
<td><p>HW版本 (4 字节)</p></td>
<td><p>FW版本 (4 字节)</p></td>
<td><p>FW 校验和 (4 字节)</p></td>
<td><p>大小 (4 字节)</p></td>
</tr>
<tr class="row-odd"><td><p>固件数据块</p></td>
<td><p>类型 == 1 (1 字节)</p></td>
<td><p>偏移量（4 字节）</p></td>
<td colspan="3"><p>数据（最多 32 字节）</p></td>
</tr>
</tbody>
</table>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 34%">
<col style="width: 34%">
<col style="width: 18%">
<col style="width: 15%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="4"><p>FW更新投票</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>固件缓冲请求</p></td>
<td><p>类型 == 1 (1 字节)</p></td>
<td><p>偏移量（4 字节）</p></td>
<td><p>大小 (4 字节)</p></td>
</tr>
<tr class="row-odd"><td><p>信号</p></td>
<td><p>类型 == 0 (拒绝上传), 2 (上传完成), 3 (保存失败) 14 (保存失败, 校验和无效) (1 字节)</p></td>
<td colspan="2"><p>0 字节</p></td>
</tr>
</tbody>
</table>
</div>
</div>
</div>


           </div>
