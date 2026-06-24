---
title: "LEAPS MQTT 连接器"
lang: zh
slug: "leaps-rtls/integration-guide/leaps-api/leaps-mqtt-connector"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/leaps-rtls/integration-guide/leaps-api/leaps-mqtt-connector/"
order: 78
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-mqtt-connector">
<span id="id1"></span><h1>LEAPS MQTT 连接器</h1>
<p>本章描述 LEAPS MQTT 连接器的特定信息。 上行链路主题中的 Pan ID（网络 ID）是可选的，可以通过调整配置设置来排除。</p>
<hr class="docutils">
<div class="section" id="uplink">
<span id="lr-uplink-gw"></span><h2>上行链路</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 45%">
<col style="width: 55%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>主题</p></th>
<th class="head"><p>描述</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>{prefix}/{panId}/gateway/uplink/status/{deviceId}</p></td>
<td><div class="line-block">
<div class="line">网关状态信息。</div>
<div class="line">Refer to <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/leaps-api/mqtt-message-reference#leaps-api-status"><span class="std std-ref">leaps_api.status</span></a></div>
</div>
<ul class="simple">
<li><p>保留=假</p></li>
<li><p>qos = 1</p></li>
</ul>
<div class="line-block">
<div class="line">示例:</div>
<div class="line">topic: leaps/0001/gateway/uplink/status/deca1e1cef720714</div>
</div>
<div class="highlight-json notranslate"><div class="highlight"><pre><span></span><span class="p">{</span>
<span class="w">  </span><span class="nt">"present"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"downlink"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"uwb"</span><span class="p">:</span><span class="nt">"CONNECTED"</span>
<span class="w">  </span><span class="nt">"origins"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">    </span><span class="p">{</span>
<span class="w">      </span><span class="nt">"id"</span><span class="p">:</span><span class="w"> </span><span class="s2">"4096"</span><span class="p">,</span>
<span class="w">      </span><span class="nt">"hop_level"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span>
<span class="w">    </span><span class="p">}</span>
<span class="w">  </span><span class="p">],</span>
<span class="w">  </span><span class="nt">"profile"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="nt">"sfn_range"</span><span class="p">:</span><span class="w"> </span><span class="mi">1440</span><span class="p">,</span>
<span class="w">    </span><span class="nt">"microseconds_per_sf"</span><span class="p">:</span><span class="w"> </span><span class="mi">100000</span><span class="p">,</span>
<span class="w">    </span><span class="nt">"microseconds_per_slot"</span><span class="p">:</span><span class="w"> </span><span class="mi">500</span><span class="p">,</span>
<span class="w">    </span><span class="nt">"update_rate_default"</span><span class="p">:</span><span class="w"> </span><span class="mi">120</span><span class="p">,</span>
<span class="w">    </span><span class="nt">"node_signup_optional"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span><span class="p">,</span>
<span class="w">    </span><span class="nt">"latency"</span><span class="p">:</span><span class="w"> </span><span class="mi">2</span><span class="p">,</span>
<span class="w">    </span><span class="nt">"max_buffer_size_downlink"</span><span class="p">:</span><span class="w"> </span><span class="mi">1024</span>
<span class="w">  </span><span class="p">},</span>
<span class="w">  </span><span class="nt">"timestamp"</span><span class="p">:</span><span class="w"> </span><span class="s2">"1681398574409278"</span>
<span class="p">}</span>
</pre></div>
</div>
</td>
</tr>
</tbody>
</table>
<hr class="docutils">
<table class="custom-table docutils align-default" id="lr-configuration-message">
<colgroup>
<col style="width: 45%">
<col style="width: 55%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>主题</p></th>
<th class="head"><p>描述</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>{prefix}/{panId}/gateway/uplink/config/{deviceId}</p></td>
<td><div class="line-block">
<div class="line">设备配置信息。</div>
<div class="line">Refer to <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/leaps-api/mqtt-message-reference#leaps-api-node-config"><span class="std std-ref">leaps_api.node_config</span></a></div>
</div>
<ul class="simple">
<li><p>保留=假</p></li>
<li><p>qos = 1</p></li>
</ul>
<div class="line-block">
<div class="line">示例:</div>
<div class="line">topic: leaps/0001/gateway/uplink/config/deca1e1cef720714</div>
</div>
<div class="highlight-json notranslate"><div class="highlight"><pre><span></span><span class="p">{</span>
<span class="w">  </span><span class="nt">"label"</span><span class="p">:</span><span class="w"> </span><span class="s2">"DWC81B"</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"uwb_mode"</span><span class="p">:</span><span class="w"> </span><span class="s2">"UWB_MODE_ACTIVE"</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"ble"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"leds"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"fw_update"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"anchor"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="nt">"initiator"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span><span class="p">,</span>
<span class="w">    </span><span class="nt">"location"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">      </span><span class="nt">"x"</span><span class="p">:</span><span class="w"> </span><span class="mf">5.51</span><span class="p">,</span>
<span class="w">      </span><span class="nt">"y"</span><span class="p">:</span><span class="w"> </span><span class="mf">7.01</span><span class="p">,</span>
<span class="w">      </span><span class="nt">"z"</span><span class="p">:</span><span class="w"> </span><span class="mf">2.51</span><span class="p">,</span>
<span class="w">      </span><span class="nt">"quality"</span><span class="p">:</span><span class="w"> </span><span class="mi">100</span>
<span class="w">    </span><span class="p">},</span>
<span class="w">    </span><span class="nt">"routing"</span><span class="p">:</span><span class="w"> </span><span class="s2">"ROUTING_OFF"</span><span class="p">,</span>
<span class="w">    </span><span class="nt">"bridge"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span>
<span class="w">  </span><span class="p">},</span>
<span class="w">  </span><span class="nt">"inet"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="nt">"ip"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">      </span><span class="p">{</span>
<span class="w">        </span><span class="nt">"addr"</span><span class="p">:</span><span class="w"> </span><span class="s2">"10.0.0.249"</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"mask"</span><span class="p">:</span><span class="w"> </span><span class="s2">"255.255.255.0"</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"gateway"</span><span class="p">:</span><span class="w"> </span><span class="s2">"10.0.0.1"</span>
<span class="w">      </span><span class="p">}</span>
<span class="w">    </span><span class="p">],</span>
<span class="w">    </span><span class="nt">"iface"</span><span class="p">:</span><span class="w"> </span><span class="s2">"WIFI"</span><span class="p">,</span>
<span class="w">    </span><span class="nt">"tls"</span><span class="p">:</span><span class="w"> </span><span class="s2">"OFF"</span><span class="p">,</span>
<span class="w">    </span><span class="nt">"dhcp"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span><span class="p">,</span>
<span class="w">    </span><span class="nt">"mac_filter"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span><span class="p">,</span>
<span class="w">    </span><span class="nt">"server"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">      </span><span class="nt">"host"</span><span class="p">:</span><span class="w"> </span><span class="s2">"10.0.0.35"</span><span class="p">,</span>
<span class="w">      </span><span class="nt">"port"</span><span class="p">:</span><span class="w"> </span><span class="mi">7777</span>
<span class="w">    </span><span class="p">}</span>
<span class="w">  </span><span class="p">},</span>
<span class="w">  </span><span class="nt">"wifi"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="nt">"ssid"</span><span class="p">:</span><span class="w"> </span><span class="s2">"LEAPS"</span><span class="p">,</span>
<span class="w">    </span><span class="nt">"password"</span><span class="p">:</span><span class="w"> </span><span class="s2">"Lpass"</span><span class="p">,</span>
<span class="w">    </span><span class="nt">"region"</span><span class="p">:</span><span class="w"> </span><span class="s2">"EUROPE"</span>
<span class="w">  </span><span class="p">},</span>
<span class="w">  </span><span class="nt">"mac"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">    </span><span class="p">{</span>
<span class="w">      </span><span class="nt">"addr"</span><span class="p">:</span><span class="w"> </span><span class="s2">"a1:f7:63:73:c8:1b"</span><span class="p">,</span>
<span class="w">      </span><span class="nt">"type"</span><span class="p">:</span><span class="w"> </span><span class="s2">"MUTABLE_DEFAULT"</span><span class="p">,</span>
<span class="w">      </span><span class="nt">"iface"</span><span class="p">:</span><span class="w"> </span><span class="s2">"UWB"</span>
<span class="w">    </span><span class="p">},</span>
<span class="w">    </span><span class="p">{</span>
<span class="w">      </span><span class="nt">"addr"</span><span class="p">:</span><span class="w"> </span><span class="s2">"00:00:00:00:00:00"</span><span class="p">,</span>
<span class="w">      </span><span class="nt">"type"</span><span class="p">:</span><span class="w"> </span><span class="s2">"EMPTY"</span><span class="p">,</span>
<span class="w">      </span><span class="nt">"iface"</span><span class="p">:</span><span class="w"> </span><span class="s2">"BLE"</span>
<span class="w">    </span><span class="p">},</span>
<span class="w">    </span><span class="p">{</span>
<span class="w">      </span><span class="nt">"addr"</span><span class="p">:</span><span class="w"> </span><span class="s2">"02:04:25:30:31:31"</span><span class="p">,</span>
<span class="w">      </span><span class="nt">"type"</span><span class="p">:</span><span class="w"> </span><span class="s2">"MUTABLE_DEFAULT"</span><span class="p">,</span>
<span class="w">      </span><span class="nt">"iface"</span><span class="p">:</span><span class="w"> </span><span class="s2">"ETHERNET"</span>
<span class="w">    </span><span class="p">},</span>
<span class="w">    </span><span class="p">{</span>
<span class="w">      </span><span class="nt">"addr"</span><span class="p">:</span><span class="w"> </span><span class="s2">"f8:f0:05:76:11:f3"</span><span class="p">,</span>
<span class="w">      </span><span class="nt">"type"</span><span class="p">:</span><span class="w"> </span><span class="s2">"MUTABLE_DEFAULT"</span><span class="p">,</span>
<span class="w">      </span><span class="nt">"iface"</span><span class="p">:</span><span class="w"> </span><span class="s2">"WIFI"</span>
<span class="w">    </span><span class="p">}</span>
<span class="w">  </span><span class="p">],</span>
<span class="w">  </span><span class="nt">"timestamp"</span><span class="p">:</span><span class="w"> </span><span class="s2">"1685324882484362"</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"uwb_rf"</span><span class="p">:</span>
<span class="w">    </span><span class="p">{</span>
<span class="w">      </span><span class="nt">"chnl"</span><span class="p">:</span><span class="mi">9</span><span class="p">,</span>
<span class="w">      </span><span class="nt">"rf_cpl"</span><span class="p">:</span><span class="mi">2</span><span class="p">,</span>
<span class="w">      </span><span class="nt">"pcode"</span><span class="p">:</span><span class="mi">10</span>
<span class="w">    </span><span class="p">}</span>
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
<col style="width: 45%">
<col style="width: 55%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>主题</p></th>
<th class="head"><p>描述</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>{prefix}/{panId}/node/uplink/status/{deviceId}</p></td>
<td><div class="line-block">
<div class="line">设备状态。 本主题为只读。</div>
<div class="line">Refer to <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/leaps-api/mqtt-message-reference#leaps-api-status"><span class="std std-ref">leaps_api.status</span></a></div>
</div>
<ul class="simple">
<li><p>保留=假</p></li>
<li><p>qos = 1</p></li>
</ul>
<div class="line-block">
<div class="line">示例:</div>
<div class="line">topic: leaps/1234/node/uplink/status/419b</div>
</div>
<div class="highlight-json notranslate"><div class="highlight"><pre><span></span><span class="p">{</span>
<span class="w">  </span><span class="nt">"present"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"downlink"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"batt"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"temp"</span><span class="p">:</span><span class="w"> </span><span class="mi">34</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"batt_state"</span><span class="p">:</span><span class="mi">1</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"timestamp"</span><span class="p">:</span><span class="s2">"1755336445063828"</span>
<span class="p">}</span>
</pre></div>
</div>
</td>
</tr>
</tbody>
</table>
<hr class="docutils">
<table class="custom-table docutils align-default" id="lr-configuration-message-01">
<colgroup>
<col style="width: 45%">
<col style="width: 55%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>主题</p></th>
<th class="head"><p>描述</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>{prefix}/{panId}/node/uplink/config/{deviceId}</p></td>
<td><div class="line-block">
<div class="line">设备配置信息。</div>
<div class="line">Refer to <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/leaps-api/mqtt-message-reference#leaps-api-node-config"><span class="std std-ref">leaps_api.node_config</span></a></div>
</div>
<ul class="simple">
<li><p>保留=假</p></li>
<li><p>qos = 1</p></li>
</ul>
<div class="line-block">
<div class="line">示例1:</div>
<div class="line">topic: leaps/0001/node/uplink/config/0f07</div>
</div>
<div class="highlight-json notranslate"><div class="highlight"><pre><span></span><span class="p">{</span>
<span class="w">  </span><span class="nt">"label"</span><span class="p">:</span><span class="w"> </span><span class="s2">"DW0F07"</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"uwb_mode"</span><span class="p">:</span><span class="w"> </span><span class="s2">"UWB_MODE_ACTIVE"</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"ble"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"leds"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"fw_update"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"anchor"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="nt">"initiator"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span><span class="p">,</span>
<span class="w">    </span><span class="nt">"location"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">      </span><span class="nt">"x"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span>
<span class="w">      </span><span class="nt">"y"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span>
<span class="w">      </span><span class="nt">"z"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span>
<span class="w">      </span><span class="nt">"quality"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span>
<span class="w">    </span><span class="p">},</span>
<span class="w">    </span><span class="nt">"routing"</span><span class="p">:</span><span class="w"> </span><span class="s2">"ROUTING_OFF"</span>
<span class="w">  </span><span class="p">},</span>
<span class="w">  </span><span class="nt">"timestamp"</span><span class="p">:</span><span class="w"> </span><span class="s2">"1681395435098551"</span>
<span class="p">}</span>
</pre></div>
</div>
<div class="line-block">
<div class="line">示例2:</div>
<div class="line">topic: leaps/0001/node/uplink/config/4439</div>
</div>
<div class="highlight-json notranslate"><div class="highlight"><pre><span></span><span class="p">{</span>
<span class="w">  </span><span class="nt">"label"</span><span class="p">:</span><span class="w"> </span><span class="s2">"ID4439"</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"uwb_mode"</span><span class="p">:</span><span class="w"> </span><span class="s2">"UWB_MODE_ACTIVE"</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"ble"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"leds"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"fw_update"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"tag"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="nt">"location_engine"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span><span class="p">,</span>
<span class="w">    </span><span class="nt">"low_power"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span><span class="p">,</span>
<span class="w">    </span><span class="nt">"stationary_detection"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span><span class="p">,</span>
<span class="w">    </span><span class="nt">"update_rate_nominal"</span><span class="p">:</span><span class="w"> </span><span class="mi">1</span><span class="p">,</span>
<span class="w">    </span><span class="nt">"update_rate_stationary"</span><span class="p">:</span><span class="w"> </span><span class="mi">10</span>
<span class="w">  </span><span class="p">},</span>
<span class="w">  </span><span class="nt">"timestamp"</span><span class="p">:</span><span class="w"> </span><span class="s2">"1685521957332504"</span>
<span class="p">}</span>
</pre></div>
</div>
</td>
</tr>
</tbody>
</table>
<hr class="docutils">
<table class="custom-table docutils align-default" id="lr-data-message-01">
<colgroup>
<col style="width: 46%">
<col style="width: 54%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>主题</p></th>
<th class="head"><p>描述</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><div class="line-block">
<div class="line">{prefix}/{panId}/node/uplink/data/{deviceId}</div>
<div class="line">或</div>
<div class="line">{prefix}/{panId}/gateway/uplink/data/{deviceId}</div>
</div>
</td>
<td><blockquote>
<div><p>Refer to <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/leaps-api/mqtt-message-reference#leaps-api-user-data"><span class="std std-ref">leaps_api.user_data</span></a></p>
<ul class="simple">
<li><p>保留=假</p></li>
<li><p>qos = 1</p></li>
</ul>
</div></blockquote>
<div class="line-block">
<div class="line">示例:</div>
<div class="line">topic: leaps/0001/node/uplink/data/0f07</div>
<div class="line">或</div>
<div class="line">topic: leaps/1234/gateway/uplink/data/deca1d45c870c485</div>
</div>
<div class="highlight-json notranslate"><div class="highlight"><pre><span></span><span class="p">{</span>
<span class="w">  </span><span class="nt">"data"</span><span class="p">:</span><span class="w"> </span><span class="s2">"ASNFZ4mrze8="</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"timestamp"</span><span class="p">:</span><span class="w"> </span><span class="s2">"1681396647102782"</span>
<span class="p">}</span>
</pre></div>
</div>
</td>
</tr>
</tbody>
</table>
<hr class="docutils">
<table class="custom-table docutils align-default" id="lr-service-message-01">
<colgroup>
<col style="width: 47%">
<col style="width: 53%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>主题</p></th>
<th class="head"><p>描述</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><div class="line-block">
<div class="line">{prefix}/{panId}/node/uplink/service/{deviceId}</div>
<div class="line">或</div>
<div class="line">{prefix}/{panId}/gateway/uplink/service/{deviceId}</div>
</div>
</td>
<td><p>Refer to <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/leaps-api/mqtt-message-reference#leaps-api-service-data"><span class="std std-ref">leaps_api.service_data</span></a></p>
<ul class="simple">
<li><p>保留=假</p></li>
<li><p>qos = 1</p></li>
</ul>
<div class="line-block">
<div class="line">示例:</div>
<div class="line">topic: leaps/0001/node/uplink/service/0f07</div>
<div class="line">或</div>
<div class="line">topic: leaps/1234/gateway/uplink/service/deca1d45c870c485</div>
</div>
<div class="highlight-json notranslate"><div class="highlight"><pre><span></span><span class="p">{</span>
<span class="w">  </span><span class="nt">"type"</span><span class="p">:</span><span class="w"> </span><span class="s2">"TLV_API_ACK"</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"data"</span><span class="p">:</span><span class="w"> </span><span class="s2">"QAEARgJexA=="</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"timestamp"</span><span class="p">:</span><span class="w"> </span><span class="s2">"1679495457581967"</span>
<span class="p">}</span>
</pre></div>
</div>
</td>
</tr>
</tbody>
</table>
<hr class="docutils">
<table class="custom-table docutils align-default" id="lr-uplink-location">
<colgroup>
<col style="width: 45%">
<col style="width: 55%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>主题</p></th>
<th class="head"><p>描述</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>{prefix}/{panId}/node/uplink/location/{deviceId}</p></td>
<td><p>Refer to <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/leaps-api/mqtt-message-reference#leaps-api-location"><span class="std std-ref">leaps_api.location</span></a></p>
<ul class="simple">
<li><p>保留=假</p></li>
<li><p>qos = 0</p></li>
</ul>
<div class="line-block">
<div class="line">示例:</div>
<div class="line">topic: leaps/0001/node/uplink/location/0012</div>
</div>
<div class="highlight-json notranslate"><div class="highlight"><pre><span></span><span class="p">{</span>
<span class="w">  </span><span class="nt">"location"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="nt">"x"</span><span class="p">:</span><span class="w"> </span><span class="mf">3.10048366</span><span class="p">,</span>
<span class="w">    </span><span class="nt">"y"</span><span class="p">:</span><span class="w"> </span><span class="mf">-0.51273495</span><span class="p">,</span>
<span class="w">    </span><span class="nt">"z"</span><span class="p">:</span><span class="w"> </span><span class="mf">0.867216647</span><span class="p">,</span>
<span class="w">    </span><span class="nt">"quality"</span><span class="p">:</span><span class="w"> </span><span class="mi">46</span><span class="p">,</span>
<span class="w">    </span><span class="nt">"statistics"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">      </span><span class="nt">"sd_x"</span><span class="p">:</span><span class="mf">0.0756242275</span><span class="p">,</span>
<span class="w">      </span><span class="nt">"sd_y"</span><span class="p">:</span><span class="mf">0.0554805398</span><span class="p">,</span>
<span class="w">      </span><span class="nt">"sd_z"</span><span class="p">:</span><span class="mi">0</span><span class="p">,</span>
<span class="w">      </span><span class="nt">"r95"</span><span class="p">:</span><span class="mf">0.178031936</span><span class="p">,</span>
<span class="w">      </span><span class="nt">"x_err"</span><span class="p">:</span><span class="s2">"NaN"</span><span class="p">,</span>
<span class="w">      </span><span class="nt">"y_err"</span><span class="p">:</span><span class="s2">"NaN"</span><span class="p">,</span>
<span class="w">      </span><span class="nt">"z_err"</span><span class="p">:</span><span class="s2">"NaN"</span><span class="p">,</span>
<span class="w">      </span><span class="nt">"toa"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">          </span><span class="nt">"anchor_id"</span><span class="p">:</span><span class="mi">39392</span><span class="p">,</span>
<span class="w">          </span><span class="nt">"sd_toa"</span><span class="p">:</span><span class="mf">0.103431724</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">          </span><span class="nt">"anchor_id"</span><span class="p">:</span><span class="mi">39390</span><span class="p">,</span>
<span class="w">          </span><span class="nt">"sd_toa"</span><span class="p">:</span><span class="mf">0.127849624</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">          </span><span class="nt">"anchor_id"</span><span class="p">:</span><span class="mi">39386</span><span class="p">,</span>
<span class="w">          </span><span class="nt">"sd_toa"</span><span class="p">:</span><span class="mf">2.77350712</span>
<span class="w">        </span><span class="p">},</span>
<span class="w">        </span><span class="p">{</span>
<span class="w">          </span><span class="nt">"anchor_id"</span><span class="p">:</span><span class="mi">39384</span><span class="p">,</span>
<span class="w">          </span><span class="nt">"sd_toa"</span><span class="p">:</span><span class="mi">0</span>
<span class="w">        </span><span class="p">}</span>
<span class="w">      </span><span class="p">]</span>
<span class="w">    </span><span class="p">}</span>
<span class="w">  </span><span class="p">},</span>
<span class="w">  </span><span class="nt">"timestamp"</span><span class="p">:</span><span class="w"> </span><span class="s2">"1681481433825962"</span>
<span class="p">}</span>
</pre></div>
</div>
</td>
</tr>
</tbody>
</table>
<hr class="docutils">
<p id="lr-tdoa-external-le">Regarding the valid data, there will be 2 types of TDOA data: blink (TDOA_BLINK) and beacon (TDOA_BCN).
TDOA_BLINK is TN-to-AN and TDOA_BCN is AN-to-AN.</p>
<div class="admonition note">
<p class="admonition-title">注解</p>
<ul class="simple">
<li><p>All timestamps are 40-bit value with the unit of [15.65ps]</p></li>
<li><p>All BCNs and BLINKs with the same “frame” value belong to the same UWBMAC frame</p></li>
<li><p>All BLINK data with the same “tag_blink_index”, “frame”, and “from” values are from the same blink received at different ANs</p></li>
</ul>
</div>
<p>Example of TDOA_BCN:</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 47%">
<col style="width: 53%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>主题</p></th>
<th class="head"><p>描述</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>{prefix}/{panId/}{node|gateway}/uplink/toa/{deviceId}</p></td>
<td><p>Refer to <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/leaps-api/mqtt-message-reference#leaps-api-tdoa-external-le"><span class="std std-ref">leaps_api.tdoa_external_le</span></a></p>
<ul class="simple">
<li><p>保留=假</p></li>
<li><p>qos = 0</p></li>
</ul>
<div class="line-block">
<div class="line">示例:</div>
<div class="line">topic: leaps/0000/gateway/uplink/toa/decadd27cfe5d225</div>
</div>
<div class="highlight-json notranslate"><div class="highlight"><pre><span></span><span class="p">{</span>
<span class="w">   </span><span class="nt">"type"</span><span class="p">:</span><span class="s2">"TDOA_BCN"</span><span class="p">,</span>
<span class="w">   </span><span class="nt">"from"</span><span class="p">:</span><span class="mi">53797</span><span class="p">,</span>
<span class="w">   </span><span class="nt">"to"</span><span class="p">:</span><span class="mi">37773</span><span class="p">,</span>
<span class="w">   </span><span class="nt">"rx_timestamp"</span><span class="p">:</span><span class="s2">"146806405508"</span><span class="p">,</span>
<span class="w">   </span><span class="nt">"tx_timestamp"</span><span class="p">:</span><span class="s2">"265259305492"</span><span class="p">,</span>
<span class="w">   </span><span class="nt">"frame"</span><span class="p">:</span><span class="mi">643</span>
<span class="p">}</span>
</pre></div>
</div>
</td>
</tr>
</tbody>
</table>
<div class="admonition hint">
<p class="admonition-title">提示</p>
<ul class="simple">
<li><p>“from” = ID of the AN transmitting the BCN (tx AN) in decimal</p></li>
<li><p>“to” = ID of the AN receiving the BCN (rx AN) in decimal</p></li>
<li><p>“rx_timestamp” = raw BCN reception time on the rx AN</p></li>
<li><p>“tx_timestamp” = raw BCN transmitting time on the tx AN</p></li>
<li><p>“frame” = frame number of the BCN</p></li>
</ul>
</div>
<p>Example of TDOA_BLINK:</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 47%">
<col style="width: 53%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>主题</p></th>
<th class="head"><p>描述</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>{prefix}/{panId/}{node|gateway}/uplink/toa/{deviceId}</p></td>
<td><p>Refer to <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/leaps-api/mqtt-message-reference#leaps-api-tdoa-external-le"><span class="std std-ref">leaps_api.tdoa_external_le</span></a></p>
<ul class="simple">
<li><p>保留=假</p></li>
<li><p>qos = 0</p></li>
</ul>
<div class="line-block">
<div class="line">示例:</div>
<div class="line">topic: leaps/0000/node/uplink/toa/00b0</div>
</div>
<div class="highlight-json notranslate"><div class="highlight"><pre><span></span><span class="p">{</span>
<span class="w">   </span><span class="nt">"type"</span><span class="p">:</span><span class="s2">"TDOA_BLINK"</span><span class="p">,</span>
<span class="w">   </span><span class="nt">"from"</span><span class="p">:</span><span class="mi">176</span><span class="p">,</span>
<span class="w">   </span><span class="nt">"to"</span><span class="p">:</span><span class="mi">37773</span><span class="p">,</span>
<span class="w">   </span><span class="nt">"rx_timestamp"</span><span class="p">:</span><span class="s2">"150407701305"</span><span class="p">,</span>
<span class="w">   </span><span class="nt">"tag_blink_index"</span><span class="p">:</span><span class="mi">908</span><span class="p">,</span>
<span class="w">   </span><span class="nt">"frame"</span><span class="p">:</span><span class="mi">643</span><span class="p">,</span>
<span class="w">   </span><span class="nt">"tn_stat"</span><span class="p">:</span><span class="kc">true</span>
<span class="p">}</span>
</pre></div>
</div>
</td>
</tr>
</tbody>
</table>
<div class="admonition hint">
<p class="admonition-title">提示</p>
<ul class="simple">
<li><p>“from” = ID of the TN transmitting the BLINK in decimal</p></li>
<li><p>“to” = ID of the AN receiving the BLINK (rx AN) in decimal</p></li>
<li><p>“rx_timestamp” = raw BLINK reception time on the rx AN</p></li>
<li><p>“tag_blink_index” = blink index, used for blink identification.</p></li>
<li><p>“frame” = frame number of the BLINK</p></li>
<li><p>“tn_stat” = TN stationary status. (true = TN is stationary, false = TN is moving)</p></li>
</ul>
</div>
</div>
<hr class="docutils">
<div class="section" id="downlink">
<h2>下行链路</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 46%">
<col style="width: 54%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>主题</p></th>
<th class="head"><p>描述</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>{prefix}/{panId}/gateway/downlink/config/{deviceId}</p></td>
<td><div class="line-block">
<div class="line">Refer to <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/leaps-api/mqtt-message-reference#leaps-api-node-config"><span class="std std-ref">leaps_api.node_config</span></a></div>
</div>
<div class="line-block">
<div class="line">示例:</div>
<div class="line">topic: leaps/0001/gateway/downlink/config/DECAFA9FC2B38B86</div>
</div>
<div class="highlight-json notranslate"><div class="highlight"><pre><span></span><span class="p">{</span>
<span class="w">  </span><span class="nt">"label"</span><span class="p">:</span><span class="w"> </span><span class="s2">"DW590F-nWIFI"</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"uwb_mode"</span><span class="p">:</span><span class="w"> </span><span class="s2">"UWB_MODE_ACTIVE"</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"ble"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"leds"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"fw_update"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"anchor"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="nt">"initiator"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span><span class="p">,</span>
<span class="w">    </span><span class="nt">"location"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">      </span><span class="nt">"x"</span><span class="p">:</span><span class="w"> </span><span class="mi">-2</span><span class="p">,</span>
<span class="w">      </span><span class="nt">"y"</span><span class="p">:</span><span class="w"> </span><span class="mi">1</span><span class="p">,</span>
<span class="w">      </span><span class="nt">"z"</span><span class="p">:</span><span class="w"> </span><span class="mi">1</span><span class="p">,</span>
<span class="w">      </span><span class="nt">"quality"</span><span class="p">:</span><span class="w"> </span><span class="mi">100</span>
<span class="w">    </span><span class="p">},</span>
<span class="w">    </span><span class="nt">"routing"</span><span class="p">:</span><span class="w"> </span><span class="s2">"ROUTING_OFF"</span><span class="p">,</span>
<span class="w">    </span><span class="nt">"bridge"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span>
<span class="w">  </span><span class="p">},</span>
<span class="w">  </span><span class="nt">"inet"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="nt">"ip"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">      </span><span class="p">{</span>
<span class="w">        </span><span class="nt">"addr"</span><span class="p">:</span><span class="w"> </span><span class="s2">"10.0.0.130"</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"mask"</span><span class="p">:</span><span class="w"> </span><span class="s2">"255.255.255.0"</span><span class="p">,</span>
<span class="w">        </span><span class="nt">"gateway"</span><span class="p">:</span><span class="w"> </span><span class="s2">"10.0.0.1"</span>
<span class="w">      </span><span class="p">}</span>
<span class="w">    </span><span class="p">],</span>
<span class="w">    </span><span class="nt">"dns"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">      </span><span class="s2">"8.8.8.8"</span>
<span class="w">    </span><span class="p">],</span>
<span class="w">    </span><span class="nt">"iface"</span><span class="p">:</span><span class="w"> </span><span class="s2">"ETHERNET"</span><span class="p">,</span>
<span class="w">    </span><span class="nt">"tls"</span><span class="p">:</span><span class="w"> </span><span class="s2">"OFF"</span><span class="p">,</span>
<span class="w">    </span><span class="nt">"dhcp"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span><span class="p">,</span>
<span class="w">    </span><span class="nt">"mac_filter"</span><span class="p">:</span><span class="w"> </span><span class="kc">false</span><span class="p">,</span>
<span class="w">    </span><span class="nt">"server"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">      </span><span class="nt">"host"</span><span class="p">:</span><span class="w"> </span><span class="s2">"10.0.0.35"</span><span class="p">,</span>
<span class="w">      </span><span class="nt">"port"</span><span class="p">:</span><span class="w"> </span><span class="mi">7777</span>
<span class="w">    </span><span class="p">}</span>
<span class="w">  </span><span class="p">},</span>
<span class="w">  </span><span class="nt">"uwb_rf"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="nt">"chnl"</span><span class="p">:</span><span class="mi">9</span><span class="p">,</span>
<span class="w">    </span><span class="nt">"rf_cpl"</span><span class="p">:</span><span class="mi">2</span><span class="p">,</span>
<span class="w">    </span><span class="nt">"pcode"</span><span class="p">:</span><span class="mi">10</span>
<span class="w">  </span><span class="p">}</span>
<span class="w">  </span><span class="nt">"wifi"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="nt">"ssid"</span><span class="p">:</span><span class="w"> </span><span class="s2">"LEAPS"</span><span class="p">,</span>
<span class="w">    </span><span class="nt">"password"</span><span class="p">:</span><span class="w"> </span><span class="s2">"mypass"</span><span class="p">,</span>
<span class="w">    </span><span class="nt">"region"</span><span class="p">:</span><span class="w"> </span><span class="s2">"ASIA"</span>
<span class="w">  </span><span class="p">}</span>
<span class="p">}</span>
</pre></div>
</div>
</td>
</tr>
</tbody>
</table>
<hr class="docutils">
<table class="custom-table docutils align-default" id="lr-user-data">
<colgroup>
<col style="width: 47%">
<col style="width: 53%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>主题</p></th>
<th class="head"><p>描述</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><div class="line-block">
<div class="line">{prefix}/{panId}/gateway/downlink/service/{deviceId}</div>
<div class="line">或</div>
<div class="line">{prefix}/{panId}/node/downlink/service/{deviceId}</div>
</div>
</td>
<td><div class="line-block">
<div class="line">Refer to <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/leaps-api/mqtt-message-reference#leaps-api-service-data"><span class="std std-ref">leaps_api.service_data</span></a></div>
</div>
<div class="line-block">
<div class="line">示例:</div>
<div class="line">topic: leaps/0001/gateway/downlink/service/DECAFA9FC2B38B86</div>
<div class="line">或</div>
<div class="line">topic: leaps/0001/node/downlink/service/0f07</div>
</div>
<div class="highlight-json notranslate"><div class="highlight"><pre><span></span><span class="p">{</span>
<span class="w">  </span><span class="nt">"data"</span><span class="p">:</span><span class="w"> </span><span class="s2">"CAA="</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"type"</span><span class="p">:</span><span class="w"> </span><span class="s2">"TLV_API_CMD"</span>
<span class="p">}</span>
</pre></div>
</div>
<div class="highlight-json notranslate"><div class="highlight"><pre><span></span><span class="p">{</span>
<span class="w">  </span><span class="nt">"data"</span><span class="p">:</span><span class="w"> </span><span class="s2">"hQQHAAX/"</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"type"</span><span class="p">:</span><span class="w"> </span><span class="s2">"TLV_API_CMD"</span>
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
<col style="width: 47%">
<col style="width: 53%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>主题</p></th>
<th class="head"><p>描述</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><div class="line-block">
<div class="line">{prefix}/{panId}/gateway/downlink/data/{deviceId}</div>
<div class="line">或</div>
<div class="line">{prefix}/{panId}/node/downlink/data/{deviceId}</div>
</div>
</td>
<td><div class="line-block">
<div class="line">Refer to <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/leaps-api/mqtt-message-reference#leaps-api-user-data"><span class="std std-ref">leaps_api.user_data</span></a></div>
</div>
<div class="line-block">
<div class="line">示例:</div>
<div class="line">topic: leaps/0001/gateway/downlink/data/DECAFA9FC2B38B86</div>
<div class="line">或</div>
<div class="line">topic: leaps/0001/node/downlink/data/0f07</div>
</div>
<div class="highlight-json notranslate"><div class="highlight"><pre><span></span><span class="p">{</span>
<span class="w">  </span><span class="nt">"data"</span><span class="p">:</span><span class="w"> </span><span class="s2">"QUJDREVGR0hJSktMTU5PUFFSU1Q="</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"overwrite"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span>
<span class="p">}</span>
</pre></div>
</div>
<div class="highlight-json notranslate"><div class="highlight"><pre><span></span><span class="p">{</span>
<span class="w">  </span><span class="nt">"data"</span><span class="p">:</span><span class="w"> </span><span class="s2">"QUJDREVGR0hJSktMTU5PUFFSU1Q="</span>
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
<col style="width: 47%">
<col style="width: 53%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>主题</p></th>
<th class="head"><p>描述</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>{prefix}/{panId}/node/downlink/config/{deviceId}</p></td>
<td><div class="line-block">
<div class="line">Refer to <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/leaps-api/mqtt-message-reference#leaps-api-node-config"><span class="std std-ref">leaps_api.node_config</span></a></div>
</div>
<div class="line-block">
<div class="line">示例:</div>
<div class="line">topic: leaps/0001/node/downlink/config/0f07</div>
</div>
<div class="highlight-json notranslate"><div class="highlight"><pre><span></span><span class="p">{</span>
<span class="w">  </span><span class="nt">"label"</span><span class="p">:</span><span class="w"> </span><span class="s2">"DW0F07"</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"uwb_mode"</span><span class="p">:</span><span class="w"> </span><span class="s2">"UWB_MODE_ACTIVE"</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"ble"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"leds"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"fw_update"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"anchor"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="nt">"initiator"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span><span class="p">,</span>
<span class="w">    </span><span class="nt">"location"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">      </span><span class="nt">"x"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span>
<span class="w">      </span><span class="nt">"y"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span>
<span class="w">      </span><span class="nt">"z"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span>
<span class="w">      </span><span class="nt">"quality"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span>
<span class="w">    </span><span class="p">},</span>
<span class="w">    </span><span class="nt">"routing"</span><span class="p">:</span><span class="w"> </span><span class="s2">"ROUTING_OFF"</span>
<span class="w">  </span><span class="p">}</span>
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
