---
title: "MQTT 连接器"
lang: zh
slug: "pans-pro-rtls/integration-guide/mqtt-connector"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/pans-pro-rtls/integration-guide/mqtt-connector/"
order: 74
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="mqtt-connector">
<span id="pans-mqtt-connector"></span><h1>MQTT 连接器</h1>
<p>本章介绍 MQTT Connector 的特定信息. 上行链路主题中的 Pan ID（网络 ID）是可选的，可以通过调整配置设置来排除。</p>
<hr class="docutils">
<div class="section" id="uplink">
<span id="pp-uplink"></span><h2>上行链路</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 34%">
<col style="width: 66%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>主题</strong></p></th>
<th class="head"><p><strong>描述</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>{prefix}/server</p></td>
<td><div class="line-block">
<div class="line">Leaps Server 的最后遗嘱。 当服务器与代理断开连接时，将发布空信息。</div>
</div>
<ul class="simple">
<li><p>保留 = 对</p></li>
<li><p>qos = 1</p></li>
</ul>
</td>
</tr>
</tbody>
</table>
<hr class="docutils">
<table class="custom-table docutils align-default" id="pp-gatewaystatusandconfig">
<colgroup>
<col style="width: 34%">
<col style="width: 66%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>主题</strong></p></th>
<th class="head"><p><strong>描述</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>{prefix}/gateway/{device
Id}/uplink</p></td>
<td><div class="line-block">
<div class="line">设备配置信息。</div>
<div class="line">参见 <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/mqtt-message-reference#pans-gatewaystatusandconfig"><span class="std std-ref">网关状态和配置</span></a>。</div>
</div>
<ul class="simple">
<li><p>保留 = 对</p></li>
<li><p>qos = 1</p></li>
</ul>
<div class="line-block">
<div class="line"><strong>示例</strong>：</div>
<div class="line">话题: dwm/gateway/deca1e1cef720714/uplink</div>
</div>
<div class="highlight-json notranslate"><div class="highlight"><pre><span></span><span class="p">{</span>
<span class="w"> </span><span class="nt">"networkId"</span><span class="p">:</span><span class="w"> </span><span class="mi">1</span><span class="p">,</span>
<span class="w"> </span><span class="nt">"bridgeNodeId"</span><span class="p">:</span>
<span class="w"> </span><span class="s2">"-2393067142368852204"</span><span class="p">,</span>
<span class="w"> </span><span class="nt">"version"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">  </span><span class="nt">"release"</span><span class="p">:</span><span class="w"> </span><span class="s2">"2.2.2"</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"firmware"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">   </span><span class="s2">"1.4.2.0"</span><span class="p">,</span>
<span class="w">   </span><span class="s2">"1.4.8.1"</span>
<span class="w">  </span><span class="p">]</span>
<span class="w"> </span><span class="p">},</span>
<span class="w"> </span><span class="nt">"uwb"</span><span class="p">:</span><span class="w"> </span><span class="s2">"CONNECTED_BH"</span><span class="p">,</span>
<span class="w"> </span><span class="nt">"configuration"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">  </span><span class="nt">"ipAddress"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">   </span><span class="s2">"10.0.1.10"</span>
<span class="w">  </span><span class="p">],</span>
<span class="w">  </span><span class="nt">"ipMask"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">   </span><span class="s2">"255.255.255.0"</span>
<span class="w">  </span><span class="p">],</span>
<span class="w">  </span><span class="nt">"ipGateway"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">   </span><span class="s2">"10.0.1.138"</span>
<span class="w">  </span><span class="p">],</span>
<span class="w">  </span><span class="nt">"dns"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">   </span><span class="s2">"8.8.8.8"</span>
<span class="w">  </span><span class="p">],</span>
<span class="w">  </span><span class="nt">"interface"</span><span class="p">:</span><span class="w"> </span><span class="s2">"ETHERNET"</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"dhcp"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"tls"</span><span class="p">:</span><span class="w"> </span><span class="s2">"OFF"</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"server"</span><span class="p">:</span><span class="w"> </span><span class="s2">"10.0.1.13"</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"port"</span><span class="p">:</span><span class="w"> </span><span class="mi">7777</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"macFilter"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"label"</span><span class="p">:</span><span class="w"> </span><span class="s2">"0714"</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"uwbMode"</span><span class="p">:</span>
<span class="w">  </span><span class="s2">"UWB_MODE_ACTIVE"</span><span class="p">,</span><span class="w"> </span><span class="nt">"leds"</span><span class="p">:</span>
<span class="w">  </span><span class="kc">true</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"uwbFirmwareUpdate"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"initiator"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"uwbBridge"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"position"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">   </span><span class="nt">"x"</span><span class="p">:</span><span class="w"> </span><span class="mf">-0.2</span><span class="p">,</span>
<span class="w">   </span><span class="nt">"y"</span><span class="p">:</span><span class="w"> </span><span class="mf">0.5</span><span class="p">,</span>
<span class="w">   </span><span class="nt">"z"</span><span class="p">:</span><span class="w"> </span><span class="mi">1</span><span class="p">,</span>
<span class="w">   </span><span class="nt">"quality"</span><span class="p">:</span><span class="w"> </span><span class="mi">100</span>
<span class="w">  </span><span class="p">},</span>
<span class="w">  </span><span class="nt">"mac"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">   </span><span class="p">{</span>
<span class="w">    </span><span class="nt">"address"</span><span class="p">:</span>
<span class="w">    </span><span class="s2">"1e:1c:ef:72:07:14"</span><span class="p">,</span><span class="w"> </span><span class="nt">"type"</span><span class="p">:</span>
<span class="w">    </span><span class="s2">"UWB, Mutable Default"</span>
<span class="w">   </span><span class="p">},</span>
<span class="w">   </span><span class="p">{</span>
<span class="w">    </span><span class="nt">"address"</span><span class="p">:</span>
<span class="w">    </span><span class="s2">"dd:04:ed:c5:c7:f5"</span><span class="p">,</span><span class="w"> </span><span class="nt">"type"</span><span class="p">:</span>
<span class="w">    </span><span class="s2">"BLE, Mutable Default"</span>
<span class="w">   </span><span class="p">},</span>
<span class="w">   </span><span class="p">{</span>
<span class="w">    </span><span class="nt">"address"</span><span class="p">:</span>
<span class="w">    </span><span class="s2">"02:04:25:30:30:35"</span><span class="p">,</span><span class="w"> </span><span class="nt">"type"</span><span class="p">:</span>
<span class="w">    </span><span class="s2">"Ethernet, Mutable Default"</span>
<span class="w">   </span><span class="p">},</span>
<span class="w">   </span><span class="p">{</span>
<span class="w">    </span><span class="nt">"address"</span><span class="p">:</span>
<span class="w">    </span><span class="s2">"00:00:00:00:00:00"</span><span class="p">,</span><span class="w"> </span><span class="nt">"type"</span><span class="p">:</span>
<span class="w">    </span><span class="s2">"Wi-Fi, Empty"</span>
<span class="w">   </span><span class="p">}</span>
<span class="w">  </span><span class="p">]</span>
<span class="w"> </span><span class="p">},</span>
<span class="w"> </span><span class="nt">"timestamp"</span><span class="p">:</span><span class="s2">"1679494386282429"</span>
<span class="p">}</span>
</pre></div>
</div>
</td>
</tr>
</tbody>
</table>
<hr class="docutils">
<table class="custom-table docutils align-default" id="pp-nodestatusuplink">
<colgroup>
<col style="width: 34%">
<col style="width: 66%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>主题</strong></p></th>
<th class="head"><p><strong>描述</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>{prefix}/node/{deviceId}/
uplink/status</p></td>
<td><p>设备状态. 此主题只读. 参见 <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/mqtt-message-reference#pans-nodestatusuplink"><span class="std std-ref">NodeStatusUplink</span></a>。</p>
<ul class="simple">
<li><p>保留 = 对</p></li>
<li><p>qos = 1</p></li>
</ul>
<div class="line-block">
<div class="line"><strong>示例</strong>：</div>
<div class="line">topic:  dwm/node/0f07/uplink/status</div>
</div>
<div class="highlight-json notranslate"><div class="highlight"><pre><span></span><span class="p">{</span>
<span class="w"> </span><span class="nt">"present"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span><span class="p">,</span>
<span class="w"> </span><span class="nt">"downlink"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span><span class="p">,</span>
<span class="w"> </span><span class="nt">"batt"</span><span class="p">:</span><span class="w"> </span><span class="mi">100</span><span class="p">,</span>
<span class="w"> </span><span class="nt">"temp"</span><span class="p">:</span><span class="w"> </span><span class="mi">25</span><span class="p">,</span>
<span class="w"> </span><span class="nt">"batt_state"</span><span class="p">:</span><span class="mi">0</span><span class="p">,</span>
<span class="w"> </span><span class="nt">"timestamp"</span><span class="p">:</span><span class="s2">"1679494411479191"</span>
<span class="p">}</span>
</pre></div>
</div>
</td>
</tr>
</tbody>
</table>
<hr class="docutils">
<table class="custom-table docutils align-default" id="pp-nodeconfiguplink">
<colgroup>
<col style="width: 34%">
<col style="width: 66%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>主题</strong></p></th>
<th class="head"><p><strong>描述</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>{prefix}/node/{deviceId}/
uplink/config</p></td>
<td><blockquote>
<div><p>参见 <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/mqtt-message-reference#nodeconfiguplink"><span class="std std-ref">节点配置链接</span></a>。</p>
<ul class="simple">
<li><p>保留 = 对</p></li>
<li><p>qos = 1</p></li>
</ul>
<div class="line-block">
<div class="line"><strong>示例</strong>：</div>
<div class="line">topic: dwm/node/0f07/uplink/config</div>
</div>
</div></blockquote>
<div class="highlight-json notranslate"><div class="highlight"><pre><span></span><span class="p">{</span>
<span class="w"> </span><span class="nt">"configuration"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">  </span><span class="nt">"label"</span><span class="p">:</span><span class="w"> </span><span class="s2">"DW0F07"</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"nodeType"</span><span class="p">:</span><span class="w"> </span><span class="s2">"ANCHOR"</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"ble"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"leds"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"uwbFirmwareUpdate"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"anchor"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">   </span><span class="nt">"initiator"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span><span class="p">,</span>
<span class="w">   </span><span class="nt">"position"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="nt">"x"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span>
<span class="w">    </span><span class="nt">"y"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span>
<span class="w">    </span><span class="nt">"z"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span>
<span class="w">    </span><span class="nt">"quality"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span>
<span class="w">   </span><span class="p">},</span>
<span class="w">   </span><span class="nt">"routingConfig"</span><span class="p">:</span>
<span class="w">   </span><span class="s2">"ROUTING_CFG_OFF"</span><span class="p">,</span>
<span class="w">   </span><span class="nt">"routingStatus"</span><span class="p">:</span>
<span class="w">   </span><span class="s2">"ROUTING_STAT_INACTIVE"</span>
<span class="w">  </span><span class="p">}</span>
<span class="w"> </span><span class="p">},</span>
<span class="w"> </span><span class="nt">"timestamp"</span><span class="p">:</span><span class="s2">"1679494543479526"</span>
<span class="p">}</span>
</pre></div>
</div>
</td>
</tr>
</tbody>
</table>
<hr class="docutils">
<table class="custom-table docutils align-default" id="pp-superframenumber">
<colgroup>
<col style="width: 34%">
<col style="width: 66%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>主题</strong></p></th>
<th class="head"><p><strong>描述</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>{prefix}/node/{deviceId}/
uplink/data</p></td>
<td><ul class="simple">
<li><p>保留=假</p></li>
<li><p>qos = 1</p></li>
</ul>
<div class="line-block">
<div class="line"><strong>示例</strong>：</div>
<div class="line">topic: dwm/node/0012/uplink/data</div>
</div>
<div class="highlight-json notranslate"><div class="highlight"><pre><span></span><span class="p">{</span>
<span class="w"> </span><span class="nt">"data"</span><span class="p">:</span><span class="w"> </span><span class="s2">"q80="</span><span class="p">,</span>
<span class="w"> </span><span class="nt">"superFrameNumber"</span><span class="p">:</span><span class="w"> </span><span class="mi">673</span><span class="p">,</span>
<span class="w"> </span><span class="nt">"timestamp"</span><span class="p">:</span><span class="s2">"1679495576782275"</span>
<span class="p">}</span>

<span class="p">{</span>
<span class="w"> </span><span class="nt">"data"</span><span class="p">:</span><span class="w"> </span><span class="s2">"ASNFZ4mrze8="</span><span class="p">,</span>
<span class="w"> </span><span class="nt">"superFrameNumber"</span><span class="p">:</span><span class="w"> </span><span class="mi">1028</span><span class="p">,</span>
<span class="w"> </span><span class="nt">"timestamp"</span><span class="p">:</span><span class="s2">"1679495612282922"</span>
<span class="p">}</span>
</pre></div>
</div>
</td>
</tr>
</tbody>
</table>
<hr class="docutils">
<table class="custom-table docutils align-default" id="pp-payloads">
<colgroup>
<col style="width: 34%">
<col style="width: 66%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>主题</strong></p></th>
<th class="head"><p><strong>描述</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>{prefix}/node/{deviceId}/
uplink/service</p></td>
<td><ul class="simple">
<li><p>保留=假</p></li>
<li><p>qos = 1</p></li>
</ul>
<div class="line-block">
<div class="line"><strong>示例</strong>：</div>
<div class="line">topic:
dwm/node/204c/uplink/service</div>
</div>
<div class="highlight-json notranslate"><div class="highlight"><pre><span></span><span class="p">{</span>
<span class="w">  </span><span class="nt">"type"</span><span class="p">:</span><span class="w"> </span><span class="s2">"TLV_API_ACK"</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"data"</span><span class="p">:</span><span class="w"> </span><span class="s2">"QAEARgJexA=="</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"timestamp"</span><span class="p">:</span><span class="s2">"1679495457581967"</span>
<span class="p">}</span>
</pre></div>
</div>
</td>
</tr>
</tbody>
</table>
<hr class="docutils">
<table class="custom-table docutils align-default" id="pp-uplink-location">
<colgroup>
<col style="width: 34%">
<col style="width: 66%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>主题</strong></p></th>
<th class="head"><p><strong>描述</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>{prefix}/node/{deviceId}/
uplink/location</p></td>
<td><blockquote>
<div><p>参见 <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/mqtt-message-reference#pans-nodelocationuplink"><span class="std std-ref">节点位置链接</span></a>。</p>
<ul class="simple">
<li><p>保留 = 对</p></li>
<li><p>qos = 0</p></li>
</ul>
<div class="line-block">
<div class="line"><strong>示例</strong>：</div>
<div class="line">topic:
dwm/node/aa01/uplink/location</div>
</div>
</div></blockquote>
<div class="highlight-json notranslate"><div class="highlight"><pre><span></span><span class="w"> </span><span class="p">{</span>
<span class="w">  </span><span class="nt">"position"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">   </span><span class="nt">"x"</span><span class="p">:</span><span class="w"> </span><span class="mf">3.25238609</span><span class="p">,</span>
<span class="w">   </span><span class="nt">"y"</span><span class="p">:</span><span class="w"> </span><span class="mf">-0.00895162672</span><span class="p">,</span>
<span class="w">   </span><span class="nt">"z"</span><span class="p">:</span><span class="w"> </span><span class="mf">0.42510426</span><span class="p">,</span>
<span class="w">   </span><span class="nt">"quality"</span><span class="p">:</span><span class="w"> </span><span class="mi">21</span>
<span class="w">  </span><span class="p">},</span>
<span class="w">  </span><span class="nt">"superFrameNumber"</span><span class="p">:</span><span class="w"> </span><span class="mi">1144</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"timestamp"</span><span class="p">:</span><span class="s2">"1679495047880989"</span>
<span class="p">}</span>
</pre></div>
</div>
</td>
</tr>
</tbody>
</table>
<hr class="docutils">
</div>
<div class="section" id="downlink">
<span id="pp-downlink"></span><h2>下行链路</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 34%">
<col style="width: 66%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>主题</strong></p></th>
<th class="head"><p><strong>描述</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>{prefix}/server</p></td>
<td><p>向 LEAPS Server发出请求. 参见 <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/mqtt-message-reference#pans-servermessage"><span class="std std-ref">服务器消息</span></a>。</p>
<div class="line-block">
<div class="line"><strong>示例</strong>：</div>
<div class="line">topic: dwm/server</div>
</div>
<div class="highlight-json notranslate"><div class="highlight"><pre><span></span><span class="p">{</span>
<span class="w"> </span><span class="nt">"request"</span><span class="p">:</span><span class="s2">"REFRESH_TOPICS"</span>
<span class="p">}</span>
</pre></div>
</div>
</td>
</tr>
</tbody>
</table>
<hr class="docutils">
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 34%">
<col style="width: 66%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>主题</strong></p></th>
<th class="head"><p><strong>描述</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>{prefix}/gateway/{devi
ceId}/downlink</p></td>
<td><p>参见 <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/mqtt-message-reference#pans-gatewaystatusandconfig"><span class="std std-ref">网关状态和配置</span></a>。</p>
<div class="line-block">
<div class="line"><strong>示例</strong>：</div>
<div class="line">topic:
dwm/gateway/DECAFA9FC2B38B86/downlink</div>
</div>
<div class="highlight-json notranslate"><div class="highlight"><pre><span></span><span class="p">{</span>
<span class="w"> </span><span class="nt">"configuration"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">  </span><span class="nt">"ipAddress"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">   </span><span class="s2">"10.0.0.202"</span><span class="p">,</span>
<span class="w">   </span><span class="s2">"2001:0db8:85a3::1319:8a2e:0370:7344"</span>
<span class="w">  </span><span class="p">],</span>
<span class="w">  </span><span class="nt">"ipMask"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">   </span><span class="s2">"255.255.255.0"</span><span class="p">,</span>
<span class="w">   </span><span class="s2">"64"</span>
<span class="w">  </span><span class="p">],</span>
<span class="w">  </span><span class="nt">"ipGateway"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">   </span><span class="s2">"10.0.0.1"</span><span class="p">,</span>
<span class="w">   </span><span class="s2">"fe80::1"</span>
<span class="w">  </span><span class="p">],</span>
<span class="w">  </span><span class="nt">"dns"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">   </span><span class="s2">"8.8.8.8"</span><span class="p">,</span>
<span class="w">   </span><span class="s2">"2001:4860:4860::8888"</span>
<span class="w">  </span><span class="p">],</span>
<span class="w">  </span><span class="nt">"dhcp"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"interface"</span><span class="p">:</span><span class="w"> </span><span class="s2">"ETHERNET"</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"tls"</span><span class="p">:</span><span class="w"> </span><span class="s2">"OFF"</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"server"</span><span class="p">:</span><span class="w"> </span><span class="s2">"10.0.0.35"</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"port"</span><span class="p">:</span><span class="w"> </span><span class="mi">7777</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"macFilter"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"wifi"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">   </span><span class="nt">"ssid"</span><span class="p">:</span><span class="w"> </span><span class="s2">"mywifi"</span><span class="p">,</span>
<span class="w">   </span><span class="nt">"password"</span><span class="p">:</span><span class="w"> </span><span class="s2">"pass"</span><span class="p">,</span>
<span class="w">   </span><span class="nt">"region"</span><span class="p">:</span><span class="w"> </span><span class="s2">"EUROPE"</span>
<span class="w">  </span><span class="p">},</span>
<span class="w">  </span><span class="nt">"label"</span><span class="p">:</span><span class="w"> </span><span class="s2">"0123456789abcdef"</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"uwbMode"</span><span class="p">:</span>
<span class="w">  </span><span class="s2">"UWB_MODE_ACTIVE"</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"leds"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"uwbFirmwareUpdate"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"initiator"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"uwbBridge"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"position"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">   </span><span class="nt">"x"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span>
<span class="w">   </span><span class="nt">"y"</span><span class="p">:</span><span class="w"> </span><span class="mi">1</span><span class="p">,</span>
<span class="w">   </span><span class="nt">"z"</span><span class="p">:</span><span class="w"> </span><span class="mf">2.5</span><span class="p">,</span>
<span class="w">   </span><span class="nt">"quality"</span><span class="p">:</span><span class="w"> </span><span class="mi">100</span>
<span class="w">  </span><span class="p">}</span>
<span class="w"> </span><span class="p">}</span>
<span class="p">}</span>
</pre></div>
</div>
</td>
</tr>
</tbody>
</table>
<hr class="docutils">
<table class="custom-table docutils align-default" id="pp-nodeconfigdownlink">
<colgroup>
<col style="width: 34%">
<col style="width: 66%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>主题</strong></p></th>
<th class="head"><p><strong>描述</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>{prefix}/node/{deviceI
d}/downlink/config</p></td>
<td><p>参见 <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/mqtt-message-reference#nodeconfigdownlink"><span class="std std-ref">节点配置下行链路</span></a>。</p>
<div class="line-block">
<div class="line"><strong>示例</strong>：</div>
<div class="line">topic:
dwm/node/0f07/downlink/config</div>
</div>
<div class="highlight-json notranslate"><div class="highlight"><pre><span></span><span class="p">{</span>
<span class="w"> </span><span class="nt">"configuration"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">  </span><span class="nt">"label"</span><span class="p">:</span><span class="w"> </span><span class="s2">"DW0F07"</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"nodeType"</span><span class="p">:</span><span class="w"> </span><span class="s2">"ANCHOR"</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"ble"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"leds"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"uwbFirmwareUpdate"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"anchor"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">   </span><span class="nt">"initiator"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span><span class="p">,</span>
<span class="w">   </span><span class="nt">"position"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="nt">"x"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span>
<span class="w">    </span><span class="nt">"y"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span>
<span class="w">    </span><span class="nt">"z"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span>
<span class="w">    </span><span class="nt">"quality"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span>
<span class="w">   </span><span class="p">},</span>
<span class="w">   </span><span class="nt">"routingConfig"</span><span class="p">:</span>
<span class="w">   </span><span class="s2">"ROUTING_CFG_OFF"</span><span class="p">,</span>
<span class="w">   </span><span class="nt">"routingStatus"</span><span class="p">:</span>
<span class="w">   </span><span class="s2">"ROUTING_STAT_INACTIVE"</span>
<span class="w">  </span><span class="p">}</span>
<span class="w"> </span><span class="p">}</span>
<span class="p">}</span>
</pre></div>
</div>
</td>
</tr>
</tbody>
</table>
<hr class="docutils">
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 34%">
<col style="width: 66%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>主题</strong></p></th>
<th class="head"><p><strong>描述</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>{prefix}/node/{deviceI
d}/downlink/service</p></td>
<td><p>参见 <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/mqtt-message-reference#pans-nodeservicedownlink"><span class="std std-ref">NodeServiceDownlink</span></a>。</p>
<div class="line-block">
<div class="line"><strong>示例</strong>：</div>
<div class="line">topic: dwm/node/204c/downlink/service</div>
</div>
<div class="highlight-json notranslate"><div class="highlight"><pre><span></span><span class="p">{</span>
<span class="w"> </span><span class="nt">"data"</span><span class="p">:</span><span class="w"> </span><span class="s2">"CAA="</span><span class="p">,</span>
<span class="w"> </span><span class="nt">"type"</span><span class="p">:</span><span class="w"> </span><span class="s2">"TLV_API_CMD"</span>
<span class="p">}</span>
</pre></div>
</div>
</td>
</tr>
</tbody>
</table>
<hr class="docutils">
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 34%">
<col style="width: 66%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>主题</strong></p></th>
<th class="head"><p><strong>描述</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>topic: dwm/node/204c/downlink/service</p></td>
<td><div class="line-block">
<div class="line"><strong>示例</strong>：</div>
<div class="line">topic: dwm/node/204c/downlink/data</div>
</div>
<div class="highlight-json notranslate"><div class="highlight"><pre><span></span><span class="p">{</span>
<span class="w"> </span><span class="nt">"data"</span><span class="p">:</span><span class="w"> </span><span class="s2">"QUJDREVGR0hJSktMTU5PUFFSU1Q="</span><span class="p">,</span>
<span class="w"> </span><span class="nt">"overwrite"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span>
<span class="p">}</span>
</pre></div>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</div>


           </div>
