---
title: "MQTT 消息参考"
lang: zh
slug: "pans-pro-rtls/integration-guide/mqtt-message-reference"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/pans-pro-rtls/integration-guide/mqtt-message-reference/"
order: 75
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="mqtt-message-reference">
<span id="pans-mqtt-message-reference"></span><h1>MQTT 消息参考</h1>
<p>本页描述每个 API 定义的细节</p>
<div class="section" id="anchorconfiguration">
<span id="id1"></span><h2>锚点配置</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>字段</strong></p></th>
<th class="head"><p><strong>类型</strong></p></th>
<th class="head"><p><strong>标签</strong></p></th>
<th class="head"><p><strong>描述</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>启动器</p></td>
<td><p>bool</p></td>
<td><p>必填</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>位置</p></td>
<td><p>位置</p></td>
<td><p>可选</p></td>
<td><p>锚点位置坐标</p></td>
</tr>
<tr class="row-even"><td><p>路由配置</p></td>
<td><p>路由锚点配置</p></td>
<td><p>必填</p></td>
<td><p>路由配置</p></td>
</tr>
<tr class="row-odd"><td><p>路由状态</p></td>
<td><p>路由锚点状态</p></td>
<td><p>可选</p></td>
<td><p>路由信息 - 仅对上行链路有效，只读</p></td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="fwversion">
<h2>Fw 版本</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>字段</strong></p></th>
<th class="head"><p><strong>类型</strong></p></th>
<th class="head"><p><strong>标签</strong></p></th>
<th class="head"><p><strong>描述</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>发布</p></td>
<td><p>字符串</p></td>
<td><p>可选</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>固件</p></td>
<td><p>字符串</p></td>
<td><p>重复</p></td>
<td></td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="kernelposition">
<h2>内核位置</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>字段</strong></p></th>
<th class="head"><p><strong>类型</strong></p></th>
<th class="head"><p><strong>标签</strong></p></th>
<th class="head"><p><strong>描述</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>x</p></td>
<td><p>字节</p></td>
<td><p>必填</p></td>
<td><div class="line-block">
<div class="line">坐标为不透明字节序列，内核驱动无法在内核空间中使用浮点运算</div>
</div>
</td>
</tr>
<tr class="row-odd"><td><p>y</p></td>
<td><p>字节</p></td>
<td><p>必填</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p>z</p></td>
<td><p>字节</p></td>
<td><p>必填</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>质量</p></td>
<td><p>uint32</p></td>
<td><p>必填</p></td>
<td><div class="line-block">
<div class="line">质量因子(0-100)，PB 使用可变长度编码，无需担心长度问题。</div>
</div>
</td>
</tr>
</tbody>
</table>
<hr class="docutils">
<p>MacConfig</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>字段</strong></p></th>
<th class="head"><p><strong>类型</strong></p></th>
<th class="head"><p><strong>标签</strong></p></th>
<th class="head"><p><strong>描述</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>地址</p></td>
<td><p>字符串</p></td>
<td><p>必填</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>类型</p></td>
<td><p>字符串</p></td>
<td><p>必填</p></td>
<td><p>空, 默认, 用户指定, 可变默认</p></td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="gatewayconfig">
<h2>网关配置</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>字段</strong></p></th>
<th class="head"><p><strong>类型</strong></p></th>
<th class="head"><p><strong>标签</strong></p></th>
<th class="head"><p><strong>描述</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>ip地址</p></td>
<td><p>字符串</p></td>
<td><p>重复</p></td>
<td><p>IP 地址, 掩码和 IP 网关列表</p></td>
</tr>
<tr class="row-odd"><td><p>ipMask</p></td>
<td><p>字符串</p></td>
<td><p>重复</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p>ip网关</p></td>
<td><p>字符串</p></td>
<td><p>重复</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>dns</p></td>
<td><p>字符串</p></td>
<td><p>重复</p></td>
<td><p>DNS</p>
<p>配置</p>
</td>
</tr>
<tr class="row-even"><td><p>界面</p></td>
<td><p>字符串</p></td>
<td><p>必填</p></td>
<td><p>接口类型 ETHERNET, WIFI, ..。</p></td>
</tr>
<tr class="row-odd"><td><p>dhcp</p></td>
<td><p>bool</p></td>
<td><p>必填</p></td>
<td><p>DHCP</p>
<p>配置</p>
</td>
</tr>
<tr class="row-even"><td><p>tls</p></td>
<td><p>字符串</p></td>
<td><p>必填</p></td>
<td><p>TLS 配置 OFF, SERVER, MUTUAL, SERVER_CN, MUTUAL_CN</p></td>
</tr>
<tr class="row-odd"><td><p>服务器</p></td>
<td><p>字符串</p></td>
<td><p>必填</p></td>
<td><p>服务器地址和端口</p></td>
</tr>
<tr class="row-even"><td><p>port</p></td>
<td><p>uint32</p></td>
<td><p>必填</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>mac过滤</p></td>
<td><p>bool</p></td>
<td><p>必填</p></td>
<td><p>MAC 过滤</p>
<p>配置</p>
</td>
</tr>
<tr class="row-even"><td><p>wifi</p></td>
<td><p>WifiConfig</p></td>
<td><p>可选</p></td>
<td><p>WIFI 配置，如果此字段出现在上行链路信息中，则 WIFI 是可用的，并且可以进行配置</p></td>
</tr>
<tr class="row-odd"><td><p>mac</p></td>
<td><p>MacConfig</p></td>
<td><p>重复</p></td>
<td><div class="line-block">
<div class="line">接口 MAC 地址的只读列表</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>标签</p></td>
<td><p>字符串</p></td>
<td><p>必填</p></td>
<td><p>UWB 节点标签</p></td>
</tr>
<tr class="row-odd"><td><p>uwbMode</p></td>
<td><p>UwbMode</p></td>
<td><p>必填</p></td>
<td><p>UWB 模式 0 - 离线，1 - 被动，2 - 主动</p></td>
</tr>
<tr class="row-even"><td><p>leds</p></td>
<td><p>bool</p></td>
<td><p>必填</p></td>
<td><p>启用或禁用 LED 指示灯</p></td>
</tr>
<tr class="row-odd"><td><p>uw
bFirmwareUpdate</p></td>
<td><p>bool</p></td>
<td><p>必填</p></td>
<td><p>启用/禁用固件更新</p></td>
</tr>
<tr class="row-even"><td><p>启动器</p></td>
<td><p>bool</p></td>
<td><p>必填</p></td>
<td><p>UWB 锚点启动器</p></td>
</tr>
<tr class="row-odd"><td><p>uwbBridge</p></td>
<td><p>bool</p></td>
<td><p>必填</p></td>
<td><p>UWB 桥接</p></td>
</tr>
<tr class="row-even"><td><p>位置</p></td>
<td><p>位置</p></td>
<td><p>必填</p></td>
<td><p>网关位置</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="gatewaystatusandconfig">
<span id="pans-gatewaystatusandconfig"></span><h2>网关状态和配置</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>字段</strong></p></th>
<th class="head"><p><strong>类型</strong></p></th>
<th class="head"><p><strong>标签</strong></p></th>
<th class="head"><p><strong>描述</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>networkId</p></td>
<td><p>uint32</p></td>
<td><p>可选</p></td>
<td><p>UWB网络 ID</p></td>
</tr>
<tr class="row-odd"><td><p>bridgeNodeId</p></td>
<td><p>sfixed64</p></td>
<td><p>可选</p></td>
<td><p>连接KD到服务器的桥接节点的标识</p></td>
</tr>
<tr class="row-even"><td><p>版本</p></td>
<td><p>Fw 版本</p></td>
<td><p>可选</p></td>
<td><p>固件版本号</p></td>
</tr>
<tr class="row-odd"><td><p>uwb</p></td>
<td><p>字符串</p></td>
<td><p>可选</p></td>
<td><dl class="simple">
<dt>UWB 状态：</dt><dd><p>已连接, 已连接_bh, 已断开, 正在更新_fw</p>
</dd>
</dl>
</td>
</tr>
<tr class="row-even"><td><p>配置</p></td>
<td><p>网关配置</p></td>
<td><p>可选</p></td>
<td><p>配置选项</p></td>
</tr>
<tr class="row-odd"><td><p>调试日志</p></td>
<td><p>调试日志</p></td>
<td><p>可选</p></td>
<td><p>将传递给网关</p></td>
</tr>
<tr class="row-even"><td><p>时间戳</p></td>
<td><p>uint64</p></td>
<td><p>可选</p></td>
<td><p>以微秒为单位的时间戳</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="nodeconfigdownlink">
<span id="id2"></span><h2>节点配置下行链路</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 24%">
<col style="width: 28%">
<col style="width: 24%">
<col style="width: 24%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>字段</strong></p></th>
<th class="head"><p><strong>类型</strong></p></th>
<th class="head"><p><strong>标签</strong></p></th>
<th class="head"><p><strong>描述</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>配置</p></td>
<td><p>节点配置</p></td>
<td><p>必填</p></td>
<td><p>可以从客户端更改的内容</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="nodeconfiguplink">
<span id="id3"></span><h2>节点配置链接</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 24%">
<col style="width: 28%">
<col style="width: 24%">
<col style="width: 24%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>字段</strong></p></th>
<th class="head"><p><strong>类型</strong></p></th>
<th class="head"><p><strong>标签</strong></p></th>
<th class="head"><p><strong>描述</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>配置</p></td>
<td><p>节点配置</p></td>
<td><p>必填</p></td>
<td><blockquote>
<div><p>可修改的</p>
</div></blockquote>
<p>可通过API修改配置</p>
</td>
</tr>
<tr class="row-odd"><td><p>时间戳</p></td>
<td><p>uint64</p></td>
<td><p>可选</p></td>
<td><p>以微秒为单位的时间戳</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="nodedatadownlink">
<span id="pans-nodedatadownlink"></span><h2>节点数据下行链路</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>字段</strong></p></th>
<th class="head"><p><strong>类型</strong></p></th>
<th class="head"><p><strong>标签</strong></p></th>
<th class="head"><p><strong>描述</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>数据</p></td>
<td><p>字节</p></td>
<td><p>必填</p></td>
<td><p>不透明数据（最多36字节）</p></td>
</tr>
<tr class="row-odd"><td><p>重写</p></td>
<td><p>bool</p></td>
<td><p>可选</p></td>
<td><p>标志</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="nodedatauplink">
<span id="pans-nodedatauplink"></span><h2>节点数据链接</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>字段</strong></p></th>
<th class="head"><p><strong>类型</strong></p></th>
<th class="head"><p><strong>标签</strong></p></th>
<th class="head"><p><strong>描述</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>数据</p></td>
<td><p>字节</p></td>
<td><p>必填</p></td>
<td><p>不透明数据（最多40字节）</p></td>
</tr>
<tr class="row-odd"><td><p>超级帧编号</p></td>
<td><p>uint32</p></td>
<td><p>可选</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p>时间戳</p></td>
<td><p>uint64</p></td>
<td><p>可选</p></td>
<td><p>以微秒为单位的时间戳</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="nodelocationuplink">
<span id="pans-nodelocationuplink"></span><h2>节点位置链接</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>字段</strong></p></th>
<th class="head"><p><strong>类型</strong></p></th>
<th class="head"><p><strong>标签</strong></p></th>
<th class="head"><p><strong>描述</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>位置</p></td>
<td><p>位置</p></td>
<td><p>必填</p></td>
<td><p>嵌入位置</p></td>
</tr>
<tr class="row-odd"><td><p>超级帧编号</p></td>
<td><p>uint32</p></td>
<td><p>可选</p></td>
<td><p>超帧</p></td>
</tr>
<tr class="row-even"><td><p>时间戳</p></td>
<td><p>uint64</p></td>
<td><p>可选</p></td>
<td><p>以微秒为单位的时间戳</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="nodeservicedownlink">
<span id="pans-nodeservicedownlink"></span><h2>NodeServiceDownlink</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>字段</strong></p></th>
<th class="head"><p><strong>类型</strong></p></th>
<th class="head"><p><strong>标签</strong></p></th>
<th class="head"><p><strong>描述</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>类型</p></td>
<td><p>字符串</p></td>
<td><p>必填</p></td>
<td><p>TLV_API</p></td>
</tr>
<tr class="row-odd"><td><p>数据</p></td>
<td><p>字节</p></td>
<td><p>必填</p></td>
<td><p>表示 API 调用的 TLV 编码二进制数据</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="nodeserviceuplink">
<span id="pans-nodeserviceuplink"></span><h2>NodeServiceUplink</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>字段</strong></p></th>
<th class="head"><p><strong>类型</strong></p></th>
<th class="head"><p><strong>标签</strong></p></th>
<th class="head"><p><strong>描述</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>类型</p></td>
<td><p>字符串</p></td>
<td><p>必填</p></td>
<td><p>TLV_API_ACK,
TLV_API_NACK</p></td>
</tr>
<tr class="row-odd"><td><p>数据</p></td>
<td><p>字节</p></td>
<td><p>可选</p></td>
<td><p>TLV 编码的API调用响应</p></td>
</tr>
<tr class="row-even"><td><p>时间戳</p></td>
<td><p>uint64</p></td>
<td><p>可选</p></td>
<td><p>以微秒为单位的时间戳</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="nodestatusuplink">
<span id="pans-nodestatusuplink"></span><h2>NodeStatusUplink</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>字段</strong></p></th>
<th class="head"><p><strong>类型</strong></p></th>
<th class="head"><p><strong>标签</strong></p></th>
<th class="head"><p><strong>描述</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>现在</p></td>
<td><p>bool</p></td>
<td><p>可选</p></td>
<td><p>存在时为 true，不存在时为 false</p></td>
</tr>
<tr class="row-odd"><td><p>下行链路</p></td>
<td><p>bool</p></td>
<td><p>可选</p></td>
<td><p>如果可能则为true，如果不可能则为false</p></td>
</tr>
<tr class="row-even"><td><p>lqi</p></td>
<td><p>uint32</p></td>
<td><p>可选</p></td>
<td><p>链接质量指示:  0=差 1=好</p></td>
</tr>
<tr class="row-odd"><td><p>batt</p></td>
<td><p>uint32</p></td>
<td><p>可选</p></td>
<td><p>电池电量（mV）。</p></td>
</tr>
<tr class="row-even"><td><p>batt_state</p></td>
<td><p>uint32</p></td>
<td><p>可选</p></td>
<td><p>Indicates the
battery
status,
0-Unknown</p>
<ul class="simple">
<li><p>1-Empty</p></li>
<li><p>2-Low</p></li>
<li><p>3-Medium</p></li>
<li><p>4-Full.</p></li>
</ul>
</td>
</tr>
<tr class="row-odd"><td><p>temp</p></td>
<td><p>uint32</p></td>
<td><p>可选</p></td>
<td><p>温度摄氏度</p></td>
</tr>
<tr class="row-even"><td><p>时间戳</p></td>
<td><p>uint64</p></td>
<td><p>可选</p></td>
<td><p>以微秒为单位的时间戳</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="nodeconfiguration">
<span id="pans-nodeconfiguration"></span><h2>NodeConfiguration</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 22%">
<col style="width: 34%">
<col style="width: 22%">
<col style="width: 22%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>字段</strong></p></th>
<th class="head"><p><strong>类型</strong></p></th>
<th class="head"><p><strong>标签</strong></p></th>
<th class="head"><p><strong>描述</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>标签</p></td>
<td><p>字符串</p></td>
<td><p>必填</p></td>
<td><p>通用配置属性</p></td>
</tr>
<tr class="row-odd"><td><p>nodeType</p></td>
<td><p>操作模式</p></td>
<td><p>必填</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p>ble</p></td>
<td><p>bool</p></td>
<td><p>必填</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>leds</p></td>
<td><p>bool</p></td>
<td><p>必填</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p>uw
bFirmwareUpdate</p></td>
<td><p>bool</p></td>
<td><p>必填</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>锚点</p></td>
<td><p>锚点配置</p></td>
<td><p>可选</p></td>
<td><p>either-or: 与操作模式锚点特定同步</p></td>
</tr>
<tr class="row-even"><td><p>标签</p></td>
<td><p>标签配置</p></td>
<td><p>可选</p></td>
<td><p>特定标签</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="position">
<span id="pans-position"></span><h2>位置</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>字段</strong></p></th>
<th class="head"><p><strong>类型</strong></p></th>
<th class="head"><p><strong>标签</strong></p></th>
<th class="head"><p><strong>描述</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>x</p></td>
<td><p>浮动</p></td>
<td><p>必填</p></td>
<td><p>坐标</p></td>
</tr>
<tr class="row-odd"><td><p>y</p></td>
<td><p>浮动</p></td>
<td><p>必填</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p>z</p></td>
<td><p>浮动</p></td>
<td><p>必填</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>质量</p></td>
<td><p>uint32</p></td>
<td><p>必填</p></td>
<td><div class="line-block">
<div class="line">质量因子(0-100)，PB 使用可变长度编码，无需担心长度问题。</div>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="tagconfiguration">
<h2>标签配置</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>字段</strong></p></th>
<th class="head"><p><strong>类型</strong></p></th>
<th class="head"><p><strong>标签</strong></p></th>
<th class="head"><p><strong>描述</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>静态检测</p></td>
<td><p>bool</p></td>
<td><p>必填</p></td>
<td><p>检测静止状态~加速计</p></td>
</tr>
<tr class="row-odd"><td><p>响应</p></td>
<td><p>bool</p></td>
<td><p>必填</p></td>
<td><p>响应模式~低功耗</p></td>
</tr>
<tr class="row-even"><td><p>定位引擎</p></td>
<td><p>bool</p></td>
<td><p>必填</p></td>
<td><p>定位？</p></td>
</tr>
<tr class="row-odd"><td><p>nomUpdateRate</p></td>
<td><p>uint32</p></td>
<td><p>必填</p></td>
<td><p>名义（常规）更新率</p></td>
</tr>
<tr class="row-even"><td><p>statUpdateRate</p></td>
<td><p>uint32</p></td>
<td><p>必填</p></td>
<td><p>静态更新率（如果启用了统计检测）</p></td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="wificonfig">
<h2>WifiConfig</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 25%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>字段</strong></p></th>
<th class="head"><p><strong>类型</strong></p></th>
<th class="head"><p><strong>标签</strong></p></th>
<th class="head"><p><strong>描述</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>ssid</p></td>
<td><p>字符串</p></td>
<td><p>必填</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>密码</p></td>
<td><p>字符串</p></td>
<td><p>必填</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p>地区</p></td>
<td><p>字符串</p></td>
<td><p>必填</p></td>
<td><p>EUROPE,
NORTH_AMERICA,
ASIA</p></td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="operatingfirmware">
<h2>操作固件</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>名称</strong></p></th>
<th class="head"><p><strong>编号</strong></p></th>
<th class="head"><p><strong>描述</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>FW1</p></td>
<td><p>0</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>FW2</p></td>
<td><p>1</p></td>
<td></td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="operationmode">
<h2>操作模式</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>名称</strong></p></th>
<th class="head"><p><strong>编号</strong></p></th>
<th class="head"><p><strong>描述</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>标签</p></td>
<td><p>0</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>锚点</p></td>
<td><p>1</p></td>
<td></td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="routinganchorconfiguration">
<h2>路由锚配置</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>名称</strong></p></th>
<th class="head"><p><strong>编号</strong></p></th>
<th class="head"><p><strong>描述</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>ROUTING_CFG_OFF</p></td>
<td><p>0</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>ROUTING_CFG_ON</p></td>
<td><p>1</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p>ROUTING_CFG_AUTO</p></td>
<td><p>2</p></td>
<td></td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="routinganchorstatus">
<h2>路由锚定状态</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>名称</strong></p></th>
<th class="head"><p><strong>编号</strong></p></th>
<th class="head"><p><strong>描述</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>ROUTING_STAT_INACTIVE</p></td>
<td><p>0</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>ROUTING_STAT_SELECTED</p></td>
<td><p>1</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p>ROUTING_STAT_ACTIVE</p></td>
<td><p>2</p></td>
<td></td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="uwbmode">
<h2>UwbMode</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>名称</strong></p></th>
<th class="head"><p><strong>编号</strong></p></th>
<th class="head"><p><strong>描述</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>UWB_MODE_OFFLINE</p></td>
<td><p>0</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>UWB_MODE_PASSIVE</p></td>
<td><p>1</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p>UWB_MODE_ACTIVE</p></td>
<td><p>2</p></td>
<td></td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="uwbstatus">
<h2>UwbStatus</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>名称</p></th>
<th class="head"><p>编号</p></th>
<th class="head"><p>描述</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>已断开连接</p></td>
<td><p>0</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>已连接</p></td>
<td><p>1</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p>CONNECTED_BH</p></td>
<td><p>2</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>UPDATING_FW</p></td>
<td><p>3</p></td>
<td></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="serverrequest">
<span id="id4"></span><h2>服务器请求</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 21%">
<col style="width: 7%">
<col style="width: 72%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>名称</p></th>
<th class="head"><p>编号</p></th>
<th class="head"><p>描述</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>服务器请求</p></td>
<td><p>0</p></td>
<td><p>请求立即发布所有节点的所有消息。</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="servermessage">
<span id="pans-servermessage"></span><h2>服务器消息</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 23%">
<col style="width: 23%">
<col style="width: 23%">
<col style="width: 31%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>领域</p></th>
<th class="head"><p>类型</p></th>
<th class="head"><p>标签</p></th>
<th class="head"><p>描述</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>请求</p></td>
<td><p>字符串</p></td>
<td><p>可选</p></td>
<td><p>Refer to
<a class="reference internal" href="#serverrequest"><span class="std std-ref">服务器请求</span></a></p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="servernodelist">
<span id="id5"></span><h2>服务器节点列表</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 11%">
<col style="width: 14%">
<col style="width: 12%">
<col style="width: 64%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>领域</p></th>
<th class="head"><p>类型</p></th>
<th class="head"><p>标签</p></th>
<th class="head"><p>描述</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>网络</p></td>
<td><p>uint32</p></td>
<td><p>必填</p></td>
<td><p>UWB网络panID。</p></td>
</tr>
<tr class="row-odd"><td><p>节点</p></td>
<td><p>字符串</p></td>
<td><p>重复</p></td>
<td><p>UWB节点ID/地址为十六进制数。</p></td>
</tr>
</tbody>
</table>
</div>
</div>


           </div>
