---
title: "MQTT 消息参考"
lang: zh
slug: "leaps-rtls/integration-guide/leaps-api/mqtt-message-reference"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/leaps-rtls/integration-guide/leaps-api/mqtt-message-reference/"
order: 79
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="mqtt-message-reference">
<span id="leaps-mqtt-message-reference"></span><h1>MQTT 消息参考</h1>
<hr class="docutils">
<div class="section" id="common">
<h2>常见</h2>
<div class="section" id="anchor-config">
<span id="id1"></span><h3>anchor_config</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 14%">
<col style="width: 35%">
<col style="width: 12%">
<col style="width: 39%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>领域</p></th>
<th class="head"><p>类型</p></th>
<th class="head"><p>标签</p></th>
<th class="head"><p>描述</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>启动器</p></td>
<td><p>bool</p></td>
<td><p>必填</p></td>
<td><p>UWB启动器模式启用。</p></td>
</tr>
<tr class="row-odd"><td><p>位置</p></td>
<td><p><a class="reference internal" href="#node-location"><span class="std std-ref">节点位置</span></a></p></td>
<td><p>必填</p></td>
<td><p>节点的位置。</p></td>
</tr>
<tr class="row-even"><td><p>使溃败</p></td>
<td><p><a class="reference internal" href="#routing-config"><span class="std std-ref">routing_config</span></a></p></td>
<td><p>必填</p></td>
<td><p>路由配置。</p></td>
</tr>
<tr class="row-odd"><td><p>桥</p></td>
<td><p>bool</p></td>
<td><p>可选</p></td>
<td><p>UWB桥接模式启用。</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="node-location">
<span id="id2"></span><h3>节点位置</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 6%">
<col style="width: 33%">
<col style="width: 7%">
<col style="width: 54%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>领域</p></th>
<th class="head"><p>类型</p></th>
<th class="head"><p>标签</p></th>
<th class="head"><p>描述</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>x</p></td>
<td><p>浮动</p></td>
<td><p>必填</p></td>
<td><p>X坐标，单位为米。</p></td>
</tr>
<tr class="row-odd"><td><p>y</p></td>
<td><p>浮动</p></td>
<td><p>必填</p></td>
<td><p>Y坐标，单位为米。</p></td>
</tr>
<tr class="row-even"><td><p>z</p></td>
<td><p>浮动</p></td>
<td><p>必填</p></td>
<td><p>Z坐标，单位为米。</p></td>
</tr>
<tr class="row-odd"><td><p>质量</p></td>
<td><p>uint32</p></td>
<td><p>必填</p></td>
<td><p>品质因数从0%到100%。</p></td>
</tr>
<tr class="row-even"><td><p>sd_x</p></td>
<td><p>浮动</p></td>
<td><p>可选</p></td>
<td><p>X坐标的标准偏差，单位为米。</p></td>
</tr>
<tr class="row-odd"><td><p>sd_y</p></td>
<td><p>浮动</p></td>
<td><p>可选</p></td>
<td><p>Y坐标的标准偏差，单位为米。</p></td>
</tr>
<tr class="row-even"><td><p>sd_z</p></td>
<td><p>浮动</p></td>
<td><p>可选</p></td>
<td><p>Z坐标的标准偏差，单位为米。</p></td>
</tr>
<tr class="row-odd"><td><p>r95</p></td>
<td><p>浮动</p></td>
<td><p>可选</p></td>
<td><p>R95的位置单位为米。</p></td>
</tr>
<tr class="row-even"><td><p>x_err</p></td>
<td><p>浮动</p></td>
<td><p>可选</p></td>
<td><p>X坐标与参考位置的误差，单位为米。</p></td>
</tr>
<tr class="row-odd"><td><p>y_err</p></td>
<td><p>浮动</p></td>
<td><p>可选</p></td>
<td><p>Y坐标与参考位置的误差，单位为米。</p></td>
</tr>
<tr class="row-even"><td><p>z_err</p></td>
<td><p>浮动</p></td>
<td><p>可选</p></td>
<td><p>Z坐标与参考位置的误差，单位为米。</p></td>
</tr>
<tr class="row-odd"><td><p>toa</p></td>
<td><p><a class="reference internal" href="#node-toa-measurement-statistics"><span class="std std-ref">node_toa_measurement_statistics</span></a></p></td>
<td><p>重复</p></td>
<td><p>到达时间测量统计。</p></td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="node-status">
<h3>节点状态</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 13%">
<col style="width: 22%">
<col style="width: 8%">
<col style="width: 57%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>领域</p></th>
<th class="head"><p>类型</p></th>
<th class="head"><p>标签</p></th>
<th class="head"><p>描述</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>起源</p></td>
<td><p><a class="reference internal" href="#origin-info"><span class="std std-ref">origin_info</span></a></p></td>
<td><p>重复</p></td>
<td><p>起源列表。</p></td>
</tr>
<tr class="row-odd"><td><p>轮廓</p></td>
<td><p><a class="reference internal" href="#uwb-profile"><span class="std std-ref">uwb_profile</span></a></p></td>
<td><p>可选</p></td>
<td><p>当前UWB配置文件。</p></td>
</tr>
<tr class="row-even"><td><p>uwb</p></td>
<td><p><a class="reference internal" href="#uwb-status"><span class="std std-ref">uwb_status</span></a></p></td>
<td><p>可选</p></td>
<td><p>UWB状态。</p></td>
</tr>
<tr class="row-odd"><td><p>传感器</p></td>
<td><p><a class="reference internal" href="#sensor-status"><span class="std std-ref">传感器状态</span></a></p></td>
<td><p>可选</p></td>
<td><p>传感器的状态。</p></td>
</tr>
<tr class="row-even"><td><p>route_active</p></td>
<td><p>bool</p></td>
<td><p>可选</p></td>
<td><p>指示网关是节点的路由候选。</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="node-toa-measurement-statistics">
<span id="id3"></span><h3>node_toa_measurement_statistics</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 12%">
<col style="width: 12%">
<col style="width: 11%">
<col style="width: 66%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>领域</p></th>
<th class="head"><p>类型</p></th>
<th class="head"><p>标签</p></th>
<th class="head"><p>描述</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>anchor_id</p></td>
<td><p>uint32</p></td>
<td><p>必填</p></td>
<td><p>锚点ID。</p></td>
</tr>
<tr class="row-odd"><td><p>sd_tdoa</p></td>
<td><p>浮动</p></td>
<td><p>必填</p></td>
<td><p>到达时间测量的标准偏差。</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="origin-info">
<span id="id4"></span><h3>origin_info</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 24%">
<col style="width: 24%">
<col style="width: 22%">
<col style="width: 30%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>领域</p></th>
<th class="head"><p>类型</p></th>
<th class="head"><p>标签</p></th>
<th class="head"><p>描述</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>本我</p></td>
<td><p>uint64</p></td>
<td><p>必填</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>hop_level</p></td>
<td><p>uint32</p></td>
<td><p>必填</p></td>
<td></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="sensor-status">
<span id="id5"></span><h3>传感器状态</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 12%">
<col style="width: 8%">
<col style="width: 7%">
<col style="width: 72%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>领域</p></th>
<th class="head"><p>类型</p></th>
<th class="head"><p>标签</p></th>
<th class="head"><p>描述</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>batt</p></td>
<td><p>uint32</p></td>
<td><p>必填</p></td>
<td><p>电池电量（mV）。</p></td>
</tr>
<tr class="row-odd"><td><p>batt_state</p></td>
<td><p>uint32</p></td>
<td><p>可选</p></td>
<td><p>Indicates the battery status, 0-Unknown | 1-Empty | 2-Low | 3-Medium | 4-Full.</p></td>
</tr>
<tr class="row-even"><td><p>temp</p></td>
<td><p>int32</p></td>
<td><p>必填</p></td>
<td><p>温度单位为度。</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="service-data">
<span id="id6"></span><h3>服务数据</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 4%">
<col style="width: 20%">
<col style="width: 7%">
<col style="width: 70%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>领域</p></th>
<th class="head"><p>类型</p></th>
<th class="head"><p>标签</p></th>
<th class="head"><p>描述</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>类型</p></td>
<td><p><a class="reference internal" href="#service-type"><span class="std std-ref">service_type</span></a></p></td>
<td><p>必填</p></td>
<td><p>服务请求的类型或响应的类型。请参考 <a class="reference internal" href="#service-type"><span class="std std-ref">service_type</span></a>。</p></td>
</tr>
<tr class="row-odd"><td><p>数据</p></td>
<td><p>字节</p></td>
<td><p>可选</p></td>
<td><p>编码为base64的不透明服务数据字节。</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="signup-request">
<span id="id7"></span><h3>signup_request</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 13%">
<col style="width: 34%">
<col style="width: 13%">
<col style="width: 39%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>领域</p></th>
<th class="head"><p>类型</p></th>
<th class="head"><p>标签</p></th>
<th class="head"><p>描述</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>发布</p></td>
<td><p><a class="reference internal" href="#version-info"><span class="std std-ref">version_info</span></a></p></td>
<td><p>可选</p></td>
<td><p>发布版本。</p></td>
</tr>
<tr class="row-odd"><td><p>固件</p></td>
<td><p><a class="reference internal" href="#version-info"><span class="std std-ref">version_info</span></a></p></td>
<td><p>重复</p></td>
<td><p>固件的版本。</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="signup-response">
<span id="id8"></span><h3>signup_response</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 12%">
<col style="width: 29%">
<col style="width: 12%">
<col style="width: 47%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>领域</p></th>
<th class="head"><p>类型</p></th>
<th class="head"><p>标签</p></th>
<th class="head"><p>描述</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>状态</p></td>
<td><p>bool</p></td>
<td><p>必填</p></td>
<td><p>注册的雕像/结果。</p></td>
</tr>
<tr class="row-odd"><td><p>固件</p></td>
<td><p><a class="reference internal" href="#version-info"><span class="std std-ref">version_info</span></a></p></td>
<td><p>必填</p></td>
<td><p>固件的当前版本。</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="tag-config">
<span id="id9"></span><h3>tag_config</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 20%">
<col style="width: 19%">
<col style="width: 7%">
<col style="width: 54%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>领域</p></th>
<th class="head"><p>类型</p></th>
<th class="head"><p>标签</p></th>
<th class="head"><p>描述</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>location_engine</p></td>
<td><p>bool</p></td>
<td><p>必填</p></td>
<td><p>内部定位引擎启用。</p></td>
</tr>
<tr class="row-odd"><td><p>low_power</p></td>
<td><p>bool</p></td>
<td><p>必填</p></td>
<td><p>低功耗模式启用。</p></td>
</tr>
<tr class="row-even"><td><p>stationary_detection</p></td>
<td><p>bool</p></td>
<td><p>必填</p></td>
<td><p>静止检测启用。</p></td>
</tr>
<tr class="row-odd"><td><p>update_rate_nominal</p></td>
<td><p>uint32</p></td>
<td><p>必填</p></td>
<td><p>标称更新率（以超帧间隔的倍数表示）。</p></td>
</tr>
<tr class="row-even"><td><p>update_rate_stationary</p></td>
<td><p>uint32</p></td>
<td><p>必填</p></td>
<td><p>超帧间隔倍数下的固定更新率。。</p></td>
</tr>
<tr class="row-odd"><td><p>reference_location</p></td>
<td><p><a class="reference internal" href="#node-location"><span class="std std-ref">节点位置</span></a></p></td>
<td><p>可选</p></td>
<td><p>标签的参考位置。</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="uwb-profile">
<span id="id10"></span><h3>uwb_profile</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 20%">
<col style="width: 16%">
<col style="width: 20%">
<col style="width: 44%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>领域</p></th>
<th class="head"><p>类型</p></th>
<th class="head"><p>标签</p></th>
<th class="head"><p>描述</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>sfn_range</p></td>
<td><p>uint32</p></td>
<td><p>必填</p></td>
<td><p>超帧编号范围。</p></td>
</tr>
<tr class="row-odd"><td><p>microseconds_per_sf</p></td>
<td><p>uint32</p></td>
<td><p>必填</p></td>
<td><p>每超帧微秒。</p></td>
</tr>
<tr class="row-even"><td><p>microseconds_per_slot</p></td>
<td><p>uint32</p></td>
<td><p>必填</p></td>
<td><p>每个插槽微秒。</p></td>
</tr>
<tr class="row-odd"><td><p>update_rate_default</p></td>
<td><p>uint32</p></td>
<td><p>必填</p></td>
<td><p>更新率是超帧的倍数。</p></td>
</tr>
<tr class="row-even"><td><p>uplink_latency</p></td>
<td><p>uint32</p></td>
<td><p>可选</p></td>
<td><p>在内部位置引擎处理已接收到的到达时间数据之前等待的时隙数。</p></td>
</tr>
<tr class="row-odd"><td><p>node_signup_optional</p></td>
<td><p>bool</p></td>
<td><p>可选</p></td>
<td><p>将此设置为 “true” 意味着任何边缘节点（非网关节点）都不需要注册，如果未设置此参数或将其设置为 “false”，则默认情况下需要注册。</p></td>
</tr>
<tr class="row-even"><td><p>延迟</p></td>
<td><p>uint32</p></td>
<td><p>可选</p></td>
<td><p>以太网延迟以超帧数表示，在发送下行链路时考虑延迟，如果未设置，则延迟应为0</p></td>
</tr>
<tr class="row-odd"><td><p>max_buffer_size_downlink</p></td>
<td><p>uint32</p></td>
<td><p>可选</p></td>
<td><p>如果没有设置，大小应该是无限的。</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="uwb-rf-config">
<span id="id11"></span><h3>uwb_rf_config</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 9%">
<col style="width: 10%">
<col style="width: 12%">
<col style="width: 69%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>领域</p></th>
<th class="head"><p>类型</p></th>
<th class="head"><p>标签</p></th>
<th class="head"><p>描述</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>chnl</p></td>
<td><p>uint32</p></td>
<td><p>必填</p></td>
<td><p>Channel configuration.</p></td>
</tr>
<tr class="row-odd"><td><p>rf_cpl</p></td>
<td><p>uint32</p></td>
<td><p>必填</p></td>
<td><p>RF compliance configuration.</p></td>
</tr>
<tr class="row-even"><td><p>pcode</p></td>
<td><p>uint32</p></td>
<td><p>可选</p></td>
<td><p>Preamble code configuration.</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="version-info">
<span id="id12"></span><h3>version_info</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 15%">
<col style="width: 27%">
<col style="width: 24%">
<col style="width: 33%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>领域</p></th>
<th class="head"><p>类型</p></th>
<th class="head"><p>标签</p></th>
<th class="head"><p>描述</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>maj</p></td>
<td><p>uint32</p></td>
<td><p>必填</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>min</p></td>
<td><p>uint32</p></td>
<td><p>必填</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p>patch</p></td>
<td><p>uint32</p></td>
<td><p>必填</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>var</p></td>
<td><p>uint32</p></td>
<td><p>可选</p></td>
<td></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="wifi-config">
<span id="id13"></span><h3>wifi_config</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 17%">
<col style="width: 41%">
<col style="width: 17%">
<col style="width: 24%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>领域</p></th>
<th class="head"><p>类型</p></th>
<th class="head"><p>标签</p></th>
<th class="head"><p>描述</p></th>
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
<td><p><a class="reference internal" href="#wifi-region"><span class="std std-ref">wifi_region</span></a></p></td>
<td><p>可选</p></td>
<td></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="interface-config">
<span id="id14"></span><h3>interface_config</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 32%">
<col style="width: 24%">
<col style="width: 44%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>名称</p></th>
<th class="head"><p>编号</p></th>
<th class="head"><p>描述</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>ETHERNET</p></td>
<td><p>0</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>WIFI</p></td>
<td><p>1</p></td>
<td></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="mac-address-type">
<span id="id15"></span><h3>mac_address_type</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 18%">
<col style="width: 7%">
<col style="width: 75%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>名称</p></th>
<th class="head"><p>编号</p></th>
<th class="head"><p>描述</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>空的</p></td>
<td><p>0</p></td>
<td><p>MAC地址为空，表示接口不存在。</p></td>
</tr>
<tr class="row-odd"><td><p>违约</p></td>
<td><p>1</p></td>
<td><p>默认MAC地址（无法更改）。</p></td>
</tr>
<tr class="row-even"><td><p>USER_SPECIFIED</p></td>
<td><p>2</p></td>
<td><p>用户指定的MAC地址（可以更改）。</p></td>
</tr>
<tr class="row-odd"><td><p>MUTABLE_DEFAULT</p></td>
<td><p>3</p></td>
<td><p>默认MAC地址，用户只能更改一次。</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="routing-config">
<span id="id16"></span><h3>routing_config</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 27%">
<col style="width: 14%">
<col style="width: 59%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>名称</p></th>
<th class="head"><p>编号</p></th>
<th class="head"><p>描述</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>ROUTING_OFF</p></td>
<td><p>0</p></td>
<td><p>UWB路由已关闭。</p></td>
</tr>
<tr class="row-odd"><td><p>ROUTING_ON</p></td>
<td><p>1</p></td>
<td><p>UWB路由处于活动状态。</p></td>
</tr>
<tr class="row-even"><td><p>ROUTING_AUTO</p></td>
<td><p>2</p></td>
<td><p>自动UWB路由。</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="service-type">
<span id="id17"></span><h3>service_type</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 22%">
<col style="width: 11%">
<col style="width: 67%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>名称</p></th>
<th class="head"><p>编号</p></th>
<th class="head"><p>描述</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>GET_CONFIG</p></td>
<td><p>0</p></td>
<td><p>请求发送配置。</p></td>
</tr>
<tr class="row-odd"><td><p>TLV_API_CMD</p></td>
<td><p>1</p></td>
<td><p>TLV API命令。</p></td>
</tr>
<tr class="row-even"><td><p>TLV_API_ACK</p></td>
<td><p>2</p></td>
<td><p>TLV API命令肯定确认。</p></td>
</tr>
<tr class="row-odd"><td><p>TLV_API_NACK</p></td>
<td><p>3</p></td>
<td><p>TLV API命令否定确认。</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="tls-config">
<span id="id18"></span><h3>tls_config</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 8%">
<col style="width: 5%">
<col style="width: 86%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>名称</p></th>
<th class="head"><p>编号</p></th>
<th class="head"><p>描述</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>关闭</p></td>
<td><p>0</p></td>
<td><p>TLS/SSL已关闭。</p></td>
</tr>
<tr class="row-odd"><td><p>服务器</p></td>
<td><p>1</p></td>
<td><p>服务器的TLS身份验证。</p></td>
</tr>
<tr class="row-even"><td><p>相互的</p></td>
<td><p>2</p></td>
<td><p>服务器和网关/客户端的双向TLS身份验证。</p></td>
</tr>
<tr class="row-odd"><td><p>SERVER_CN</p></td>
<td><p>3</p></td>
<td><p>通过检查“公用名称”对服务器进行TLS身份验证。</p></td>
</tr>
<tr class="row-even"><td><p>MUTUAL_CN</p></td>
<td><p>4</p></td>
<td><p>服务器和网关/客户端的双向TLS身份验证，并检查 “通用名称”。</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="uwb-mode-config">
<span id="id19"></span><h3>uwb_mode_config</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 48%">
<col style="width: 18%">
<col style="width: 33%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>名称</p></th>
<th class="head"><p>编号</p></th>
<th class="head"><p>描述</p></th>
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
<hr class="docutils">
</div>
<div class="section" id="uwb-status">
<span id="id20"></span><h3>uwb_status</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 24%">
<col style="width: 11%">
<col style="width: 65%">
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
<td><p>已断开与UWB网络的连接。</p></td>
</tr>
<tr class="row-odd"><td><p>已连接</p></td>
<td><p>1</p></td>
<td><p>连接到UWB网络。</p></td>
</tr>
<tr class="row-even"><td><p>CONNECTED_BH</p></td>
<td><p>2</p></td>
<td><p>连接，回程可能。</p></td>
</tr>
<tr class="row-odd"><td><p>UPDATING_FW</p></td>
<td><p>3</p></td>
<td><p>UWB固件更新正在进行中。</p></td>
</tr>
<tr class="row-even"><td><p>UWBS_INACTIVE</p></td>
<td><p>4</p></td>
<td><p>UWBS的数据没有来</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="wifi-region">
<span id="id21"></span><h3>wifi_region</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 43%">
<col style="width: 20%">
<col style="width: 37%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>名称</p></th>
<th class="head"><p>编号</p></th>
<th class="head"><p>描述</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>欧洲</p></td>
<td><p>0</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>北美</p></td>
<td><p>1</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p>亚洲</p></td>
<td><p>2</p></td>
<td></td>
</tr>
</tbody>
</table>
</div>
</div>
<hr class="docutils">
<div class="section" id="leaps-api">
<h2>leaps_api</h2>
<div class="section" id="leaps-api-inet-config">
<span id="id22"></span><h3>leaps_api.inet_config</h3>
<p>TCP/IP配置选项。</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 11%">
<col style="width: 49%">
<col style="width: 9%">
<col style="width: 30%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>领域</p></th>
<th class="head"><p>类型</p></th>
<th class="head"><p>标签</p></th>
<th class="head"><p>描述</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>ip</p></td>
<td><p><a class="reference internal" href="#leaps-api-ip-config"><span class="std std-ref">leaps_api.ip_config</span></a></p></td>
<td><p>重复</p></td>
<td><p>IP配置。</p></td>
</tr>
<tr class="row-odd"><td><p>dns</p></td>
<td><p>字符串</p></td>
<td><p>重复</p></td>
<td><p>DNS主机。</p></td>
</tr>
<tr class="row-even"><td><p>iface</p></td>
<td><p><a class="reference internal" href="#interface-config"><span class="std std-ref">interface_config</span></a></p></td>
<td><p>必填</p></td>
<td><p>界面选择。</p></td>
</tr>
<tr class="row-odd"><td><p>tls</p></td>
<td><p><a class="reference internal" href="#tls-config"><span class="std std-ref">tls_config</span></a></p></td>
<td><p>必填</p></td>
<td><p>TLS/SSL配置。</p></td>
</tr>
<tr class="row-even"><td><p>dhcp</p></td>
<td><p>bool</p></td>
<td><p>必填</p></td>
<td><p>DHCP已启用？</p></td>
</tr>
<tr class="row-odd"><td><p>mac_filter</p></td>
<td><p>bool</p></td>
<td><p>必填</p></td>
<td><p>MAC过滤器启用了吗？</p></td>
</tr>
<tr class="row-even"><td><p>服务器</p></td>
<td><p><a class="reference internal" href="#leaps-api-inet-config-server-config"><span class="std std-ref">leaps_api.inet_config.server_config</span></a></p></td>
<td><p>必填</p></td>
<td><p>Leaps Server配置。</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="leaps-api-inet-config-server-config">
<span id="id23"></span><h3>leaps_api.inet_config.server_config</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 9%">
<col style="width: 17%">
<col style="width: 15%">
<col style="width: 59%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>领域</p></th>
<th class="head"><p>类型</p></th>
<th class="head"><p>标签</p></th>
<th class="head"><p>描述</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>主办</p></td>
<td><p>字符串</p></td>
<td><p>必填</p></td>
<td><p>Leaps Server主机配置。</p></td>
</tr>
<tr class="row-odd"><td><p>端口</p></td>
<td><p>uint32</p></td>
<td><p>必填</p></td>
<td><p>Leaps Server端口配置。</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="leaps-api-ip-config">
<span id="id24"></span><h3>leaps_api.ip_config</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 16%">
<col style="width: 21%">
<col style="width: 19%">
<col style="width: 44%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>领域</p></th>
<th class="head"><p>类型</p></th>
<th class="head"><p>标签</p></th>
<th class="head"><p>描述</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>地址</p></td>
<td><p>字符串</p></td>
<td><p>必填</p></td>
<td><p>IP地址。</p></td>
</tr>
<tr class="row-odd"><td><p>面具</p></td>
<td><p>字符串</p></td>
<td><p>可选</p></td>
<td><p>IP地址掩码。</p></td>
</tr>
<tr class="row-even"><td><p>网关</p></td>
<td><p>字符串</p></td>
<td><p>可选</p></td>
<td><p>网关IP地址。</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="leaps-api-location">
<span id="id25"></span><h3>leaps_api.location</h3>
<p>Topic: {prefix}/{panId/}node/uplink/location/{deviceId}.</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 14%">
<col style="width: 34%">
<col style="width: 12%">
<col style="width: 40%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>领域</p></th>
<th class="head"><p>类型</p></th>
<th class="head"><p>标签</p></th>
<th class="head"><p>描述</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>位置</p></td>
<td><p><a class="reference internal" href="#node-location"><span class="std std-ref">节点位置</span></a></p></td>
<td><p>必填</p></td>
<td><p>设备的位置</p></td>
</tr>
<tr class="row-odd"><td><p>时间戳</p></td>
<td><p>uint64</p></td>
<td><p>可选</p></td>
<td><p>时间戳（微秒）。</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="leaps-api-mac-config">
<span id="id26"></span><h3>leaps_api.mac_config</h3>
<p>MAC地址的配置。</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 5%">
<col style="width: 23%">
<col style="width: 7%">
<col style="width: 66%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>领域</p></th>
<th class="head"><p>类型</p></th>
<th class="head"><p>标签</p></th>
<th class="head"><p>描述</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>地址</p></td>
<td><p>字符串</p></td>
<td><p>必填</p></td>
<td><p>以点表示的MAC地址。</p></td>
</tr>
<tr class="row-odd"><td><p>类型</p></td>
<td><p><a class="reference internal" href="#mac-address-type"><span class="std std-ref">mac_address_type</span></a></p></td>
<td><p>必填</p></td>
<td><p>MAC地址的类型。请参考 <a class="reference internal" href="#mac-address-type"><span class="std std-ref">mac_address_type</span></a>。</p></td>
</tr>
<tr class="row-even"><td><p>iface</p></td>
<td><p>字符串</p></td>
<td><p>必填</p></td>
<td><p>MAC地址所属的接口。请参阅 mac_address_interface。</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="leaps-api-node-config">
<span id="id27"></span><h3>leaps_api.node_config</h3>
<p>Topic: {prefix}/{panId/}{node|gateway}/{uplink|downlink}/config/{deviceId}.</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 13%">
<col style="width: 28%">
<col style="width: 7%">
<col style="width: 53%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>领域</p></th>
<th class="head"><p>类型</p></th>
<th class="head"><p>标签</p></th>
<th class="head"><p>描述</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>标签</p></td>
<td><p>字符串</p></td>
<td><p>必填</p></td>
<td><p>设备标签。</p></td>
</tr>
<tr class="row-odd"><td><p>uwb_mode</p></td>
<td><p><a class="reference internal" href="#uwb-mode-config"><span class="std std-ref">uwb_mode_config</span></a></p></td>
<td><p>必填</p></td>
<td><p>UWB模式配置。</p></td>
</tr>
<tr class="row-even"><td><p>ble</p></td>
<td><p>bool</p></td>
<td><p>必填</p></td>
<td><p>启用BLE？</p></td>
</tr>
<tr class="row-odd"><td><p>leds</p></td>
<td><p>bool</p></td>
<td><p>必填</p></td>
<td><p>LED已启用？</p></td>
</tr>
<tr class="row-even"><td><p>fw_update</p></td>
<td><p>bool</p></td>
<td><p>必填</p></td>
<td><p>固件更新已启用？</p></td>
</tr>
<tr class="row-odd"><td><p>锚点</p></td>
<td><p><a class="reference internal" href="#anchor-config"><span class="std std-ref">anchor_config</span></a></p></td>
<td><p>可选</p></td>
<td><p>锚的特定配置。</p></td>
</tr>
<tr class="row-even"><td><p>标签</p></td>
<td><p><a class="reference internal" href="#tag-config"><span class="std std-ref">tag_config</span></a></p></td>
<td><p>可选</p></td>
<td><p>标签特定配置。</p></td>
</tr>
<tr class="row-odd"><td><p>inet</p></td>
<td><p><a class="reference internal" href="#leaps-api-inet-config"><span class="std std-ref">leaps_api.inet_config</span></a></p></td>
<td><p>可选</p></td>
<td><p>TCP/IP配置</p></td>
</tr>
<tr class="row-even"><td><p>wifi</p></td>
<td><p><a class="reference internal" href="#wifi-config"><span class="std std-ref">wifi_config</span></a></p></td>
<td><p>可选</p></td>
<td><p>Wi-Fi配置。</p></td>
</tr>
<tr class="row-odd"><td><p>mac</p></td>
<td><p><a class="reference internal" href="#leaps-api-mac-config"><span class="std std-ref">leaps_api.mac_config</span></a></p></td>
<td><p>重复</p></td>
<td><p>MAC地址配置。</p></td>
</tr>
<tr class="row-even"><td><p>时间戳</p></td>
<td><p>uint64</p></td>
<td><p>可选</p></td>
<td><p>时间戳（微秒）。</p></td>
</tr>
<tr class="row-odd"><td><p>uwb_rf_config</p></td>
<td><p><a class="reference internal" href="#uwb-rf-config"><span class="std std-ref">uwb_rf_config</span></a></p></td>
<td><p>可选</p></td>
<td><p>UWB channel, preamble code and RF compliance configuration.</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="leaps-api-tdoa-external-le">
<span id="id28"></span><h3>leaps_api.tdoa_external_le</h3>
<p>Topic: {prefix}/{panId/}{node|gateway}/uplink/toa/{deviceId}.</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 20%">
<col style="width: 36%">
<col style="width: 9%">
<col style="width: 35%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>领域</p></th>
<th class="head"><p>类型</p></th>
<th class="head"><p>标签</p></th>
<th class="head"><p>描述</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>类型</p></td>
<td><p><a class="reference internal" href="#time-of-arrival-data-type"><span class="std std-ref">time_of_arrival_data_type</span></a></p></td>
<td><p>必填</p></td>
<td><p>Type of TOA data</p></td>
</tr>
<tr class="row-odd"><td><p>from</p></td>
<td><p>uint32</p></td>
<td><p>必填</p></td>
<td><p>Id of transmitting device</p></td>
</tr>
<tr class="row-even"><td><p>to</p></td>
<td><p>uint32</p></td>
<td><p>必填</p></td>
<td><p>Id of receiving device</p></td>
</tr>
<tr class="row-odd"><td><p>rx_timestamp</p></td>
<td><p>uint64</p></td>
<td><p>必填</p></td>
<td><p>Receive timestamp (uwb clock)</p></td>
</tr>
<tr class="row-even"><td><p>tx_timestamp</p></td>
<td><p>uint64</p></td>
<td><p>可选</p></td>
<td><p>Transmit timestamp (uwb clock)</p></td>
</tr>
<tr class="row-odd"><td><p>tag_blink_index</p></td>
<td><p>uint32</p></td>
<td><p>可选</p></td>
<td><p>Tag blink index</p></td>
</tr>
<tr class="row-even"><td><p>frame</p></td>
<td><p>uint32</p></td>
<td><p>必填</p></td>
<td><p>Frame number</p></td>
</tr>
<tr class="row-odd"><td><p>tn_stat</p></td>
<td><p>bool</p></td>
<td><p>可选</p></td>
<td><p>TN stationary status</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="time-of-arrival-data-type">
<span id="id29"></span><h3>time_of_arrival_data_type</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 27%">
<col style="width: 15%">
<col style="width: 59%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>名称</p></th>
<th class="head"><p>编号</p></th>
<th class="head"><p>描述</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>UNKNOWN</p></td>
<td><p>0</p></td>
<td><p>Unknown</p></td>
</tr>
<tr class="row-odd"><td><p>TWR</p></td>
<td><p>1</p></td>
<td><p>TWR</p></td>
</tr>
<tr class="row-even"><td><p>TDOA_BLINK</p></td>
<td><p>2</p></td>
<td><p>TDoA Blink</p></td>
</tr>
<tr class="row-odd"><td><p>TDOA_BCN</p></td>
<td><p>3</p></td>
<td><p>TDoA Beacon</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="leaps-api-server-status">
<span id="id30"></span><h3>leaps_api.server_status</h3>
<p>Leaps server status uplink topic: {prefix}/server/status.</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 7%">
<col style="width: 38%">
<col style="width: 7%">
<col style="width: 47%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>领域</p></th>
<th class="head"><p>类型</p></th>
<th class="head"><p>标签</p></th>
<th class="head"><p>描述</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>状态</p></td>
<td><p><a class="reference internal" href="#leaps-api-connection-state"><span class="std std-ref">leaps_api.connection_state</span></a></p></td>
<td><p>可选</p></td>
<td><p>Leaps server的状态。请参阅服务器状态。</p></td>
</tr>
<tr class="row-odd"><td><p>版本</p></td>
<td><p>字符串</p></td>
<td><p>可选</p></td>
<td><p>Leaps Server版本。</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="leaps-api-server-request">
<span id="id31"></span><h3>leaps_api.server_request</h3>
<p>Leaps server请求下行链路主题:｛prefix｝/server/request。</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 8%">
<col style="width: 34%">
<col style="width: 7%">
<col style="width: 51%">
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
<td><p><a class="reference internal" href="#leaps-api-server-request-type"><span class="std std-ref">leaps_api.server_request.type:</span></a></p></td>
<td><p>可选</p></td>
<td><p>Request to the Leaps server.</p></td>
</tr>
</tbody>
</table>
</div>
<div class="section" id="leaps-api-server-request-type">
<span id="id32"></span><h3>leaps_api.server_request.type:</h3>
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
<tr class="row-even"><td><p>REFRESH_TOPICS</p></td>
<td><p>0</p></td>
<td><p>DEPRECATED: Same as PUBLISH_ALL_TOPICS.</p></td>
</tr>
<tr class="row-odd"><td><p>PUBLISH_ALL_TOPICS</p></td>
<td><p>1</p></td>
<td><p>请求立即发布所有节点的所有消息。</p></td>
</tr>
</tbody>
</table>
</div>
<div class="section" id="leaps-api-service-data">
<span id="id33"></span><h3>leaps_api.service_data</h3>
<p>主题:｛前缀｝/｛panId/｝节点/｛上行链路|下行链路｝/服务/｛设备ID｝。</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 13%">
<col style="width: 31%">
<col style="width: 11%">
<col style="width: 46%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>领域</p></th>
<th class="head"><p>类型</p></th>
<th class="head"><p>标签</p></th>
<th class="head"><p>描述</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>类型</p></td>
<td><p><a class="reference internal" href="#service-type"><span class="std std-ref">service_type</span></a></p></td>
<td><p>必填</p></td>
<td><p>服务器数据的类型。</p></td>
</tr>
<tr class="row-odd"><td><p>数据</p></td>
<td><p>字节</p></td>
<td><p>可选</p></td>
<td><p>编码为base64的数据字节。</p></td>
</tr>
<tr class="row-even"><td><p>时间戳</p></td>
<td><p>uint64</p></td>
<td><p>可选</p></td>
<td><p>时间戳（微秒）。</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="leaps-api-status">
<span id="id34"></span><h3>leaps_api.status</h3>
<p>主题:｛前缀｝/｛panId｝/｛节点|网关｝/上行链路/状态/｛设备ID｝。</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 11%">
<col style="width: 15%">
<col style="width: 7%">
<col style="width: 67%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>领域</p></th>
<th class="head"><p>类型</p></th>
<th class="head"><p>标签</p></th>
<th class="head"><p>描述</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>现在</p></td>
<td><p>bool</p></td>
<td><p>必填</p></td>
<td><p>设备是否存在或缺失？</p></td>
</tr>
<tr class="row-odd"><td><p>下行链路</p></td>
<td><p>bool</p></td>
<td><p>可选</p></td>
<td><p>是否可以向设备发送下行链路？</p></td>
</tr>
<tr class="row-even"><td><p>uwb</p></td>
<td><p><a class="reference internal" href="#uwb-status"><span class="std std-ref">uwb_status</span></a></p></td>
<td><p>可选</p></td>
<td><p>UWB层的状态。</p></td>
</tr>
<tr class="row-odd"><td><p>batt</p></td>
<td><p>uint32</p></td>
<td><p>可选</p></td>
<td><p>Battery status in mV.</p></td>
</tr>
<tr class="row-even"><td><p>batt_state</p></td>
<td><p>uint32</p></td>
<td><p>可选</p></td>
<td><p>Indicates the battery status, 0-Unknown | 1-Empty | 2-Low | 3-Medium | 4-Full.</p></td>
</tr>
<tr class="row-odd"><td><p>temp</p></td>
<td><p>int32</p></td>
<td><p>可选</p></td>
<td><p>温度单位为度。</p></td>
</tr>
<tr class="row-even"><td><p>起源</p></td>
<td><p><a class="reference internal" href="#origin-info"><span class="std std-ref">origin_info</span></a></p></td>
<td><p>重复</p></td>
<td><p>UWB起源列表。</p></td>
</tr>
<tr class="row-odd"><td><p>轮廓</p></td>
<td><p><a class="reference internal" href="#uwb-profile"><span class="std std-ref">uwb_profile</span></a></p></td>
<td><p>可选</p></td>
<td><p>当前UWB配置文件状态。</p></td>
</tr>
<tr class="row-even"><td><p>时间戳</p></td>
<td><p>uint64</p></td>
<td><p>可选</p></td>
<td><p>时间戳（微秒）。</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="leaps-api-user-data">
<span id="id35"></span><h3>leaps_api.user_data</h3>
<p>主题:｛前缀｝/｛panId｝/节点/｛上行链路|下行链路｝/数据/｛设备ID｝。</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 15%">
<col style="width: 15%">
<col style="width: 14%">
<col style="width: 56%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>领域</p></th>
<th class="head"><p>类型</p></th>
<th class="head"><p>标签</p></th>
<th class="head"><p>描述</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>数据</p></td>
<td><p>字节</p></td>
<td><p>必填</p></td>
<td><p>编码为base64的数据字节。</p></td>
</tr>
<tr class="row-odd"><td><p>重写</p></td>
<td><p>bool</p></td>
<td><p>可选</p></td>
<td><p>Overwrite the pending data?</p></td>
</tr>
<tr class="row-even"><td><p>时间戳</p></td>
<td><p>uint64</p></td>
<td><p>可选</p></td>
<td><p>时间戳（微秒）。</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="leaps-api-mac-address-interface">
<span id="id36"></span><h3>leaps_api.mac_address_interface</h3>
<p>在MAC地址配置方面支持的接口。</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 32%">
<col style="width: 24%">
<col style="width: 44%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>名称</p></th>
<th class="head"><p>编号</p></th>
<th class="head"><p>描述</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>UWB</p></td>
<td><p>0</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>BLE</p></td>
<td><p>1</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p>ETHERNET</p></td>
<td><p>2</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p>WIFI</p></td>
<td><p>3</p></td>
<td></td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="leaps-api-connection-state">
<span id="id37"></span><h3>leaps_api.connection_state</h3>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 18%">
<col style="width: 9%">
<col style="width: 73%">
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
<td><p>Leaps server is disconnected from MQTT broker.</p></td>
</tr>
<tr class="row-odd"><td><p>已连接</p></td>
<td><p>1</p></td>
<td><p>Leaps server is connected to MQTT broker.</p></td>
</tr>
</tbody>
</table>
</div>
</div>
</div>


           </div>
