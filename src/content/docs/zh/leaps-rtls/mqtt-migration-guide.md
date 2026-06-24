---
title: "MQTT Migration Guide"
lang: zh
slug: "leaps-rtls/mqtt-migration-guide"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/leaps-rtls/mqtt-migration-guide/"
order: 19
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="mqtt-migration-guide">
<h1>MQTT Migration Guide</h1>
<p>This guide describes the recommended process for migrating MQTT
integrations from the <a class="reference internal" href="/docs/zh/pans-pro-rtls#pans-pro-rtls"><span class="std std-ref">PANS PRO RTLS</span></a> stack to the <a class="reference internal" href="/docs/zh/leaps-rtls#leaps-rtls"><span class="std std-ref">LEAPS RTLS</span></a> stack. Teams
may modernise their existing applications to speak the LEAPS topics
directly or deploy a temporary/permanent bridge that performs the
translation on their behalf. It consolidates the documentation found in:</p>
<ul class="simple">
<li><p>PANS PRO RTLS:</p>
<ul>
<li><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/mqtt-api#pans-mqtt-api"><span class="std std-ref">PANS PRO RTLS MQTT API</span></a></p></li>
<li><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/mqtt-connector#pans-mqtt-connector"><span class="std std-ref">PANS PRO RTLS MQTT Connector</span></a></p></li>
<li><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/mqtt-message-reference#pans-mqtt-message-reference"><span class="std std-ref">PANS PRO RTLS MQTT Message Reference</span></a></p></li>
</ul>
</li>
<li><p>LEAPS RTLS:</p>
<ul>
<li><p><a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/leaps-api/mqtt-api#leaps-mqtt-api"><span class="std std-ref">LEAPS RTLS MQTT API</span></a></p></li>
<li><p><a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/leaps-api/base-mqtt-messages#leaps-base-mqtt-messages"><span class="std std-ref">LEAPS RTLS Base MQTT messages</span></a></p></li>
<li><p><a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/leaps-api/leaps-mqtt-connector#leaps-mqtt-connector"><span class="std std-ref">LEAPS RTLS LEAPS MQTT Connector</span></a></p></li>
<li><p><a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/leaps-api/mqtt-message-reference#leaps-mqtt-message-reference"><span class="std std-ref">LEAPS RTLS MQTT Message Reference</span></a></p></li>
</ul>
</li>
</ul>
<hr class="docutils">
<div class="section" id="scope-inventory">
<h2>1. Scope &amp; Inventory</h2>
<p>The table below consolidates the MQTT traffic described in the PANS PRO
and LEAPS RTLS connector guides. Use it as a baseline when planning
migrations or validating completeness.</p>
<table class="docutils align-default">
<colgroup>
<col style="width: 17%">
<col style="width: 17%">
<col style="width: 17%">
<col style="width: 17%">
<col style="width: 17%">
<col style="width: 17%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Domain</p></th>
<th class="head"><p>PANS PRO topics (QoS / retain)</p></th>
<th class="head"><p>Payload focus</p></th>
<th class="head"><p>LEAPS RTLS topics (QoS / retain)</p></th>
<th class="head"><p>Payload focus</p></th>
<th class="head"><p>Notes</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Server lifecycle</p></td>
<td><ul class="simple">
<li><p><cite>{prefix}/server</cite> server status (QoS 1 / retained ✓)</p></li>
<li><p><cite>{prefix}/server</cite> requests (QoS 1 / retained ✗)</p></li>
</ul>
</td>
<td><ul class="simple">
<li><p>Server status (empty/min JSON)</p></li>
<li><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/mqtt-message-reference#pans-servermessage"><span class="std std-ref">服务器消息</span></a> requests</p></li>
</ul>
</td>
<td><ul class="simple">
<li><p><cite>{prefix}/server/status</cite> (QoS 1 / retained ✗)</p></li>
<li><p><cite>{prefix}/server/request</cite> (QoS 1 / retained ✗)</p></li>
</ul>
</td>
<td><p><a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/leaps-api/mqtt-message-reference#leaps-api-server-request"><span class="std std-ref">leaps_api.server_request</span></a> (state, version, nodeList, request, networks)</p></td>
<td><p>Consumers subscribe to <cite>{prefix}/server/status</cite>; server LWT publishes <cite>{“state”:”DISCONNECTED”}</cite>.</p></td>
</tr>
<tr class="row-odd"><td><p>Gateway status &amp; config</p></td>
<td><ul class="simple">
<li><p><cite>{prefix}/gateway/{deviceId}/uplink</cite> (QoS 1 / retained ✓)</p></li>
<li><p><cite>{prefix}/gateway/{deviceId}/downlink</cite> (QoS 1 / retained ✗)</p></li>
</ul>
</td>
<td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/mqtt-message-reference#pans-gatewaystatusandconfig"><span class="std std-ref">网关状态和配置</span></a> (networkId, bridgeNodeId, configuration)</p></td>
<td><ul class="simple">
<li><p><cite>{prefix}/{networkId}/gateway/uplink/status/{deviceId}</cite> (QoS 1 / retained ✗)</p></li>
<li><p><cite>{prefix}/{networkId}/gateway/uplink/config/{deviceId}</cite> (QoS 1 / retained ✗)</p></li>
<li><p><cite>{prefix}/{networkId}/gateway/downlink/config/{deviceId}</cite> (QoS 1 / retained ✗)</p></li>
</ul>
</td>
<td><ul class="simple">
<li><p><a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/leaps-api/mqtt-message-reference#leaps-api-status"><span class="std std-ref">leaps_api.status</span></a></p></li>
<li><p><a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/leaps-api/mqtt-message-reference#leaps-api-node-config"><span class="std std-ref">leaps_api.node_config</span></a></p></li>
</ul>
</td>
<td><p>Insert <cite>{networkId}</cite> from legacy <cite>networkId</cite>; split status vs configuration topics.</p></td>
</tr>
<tr class="row-even"><td><p>Node status &amp; config</p></td>
<td><ul class="simple">
<li><p><cite>{prefix}/node/{deviceId}/uplink/status</cite> (QoS 1 / retained ✓)</p></li>
<li><p><cite>{prefix}/node/{deviceId}/uplink/config</cite> (QoS 1 / retained ✓)</p></li>
<li><p><cite>{prefix}/node/{deviceId}/downlink/config</cite> (QoS 1 / retained ✗)</p></li>
</ul>
</td>
<td><ul class="simple">
<li><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/mqtt-message-reference#pans-nodestatusuplink"><span class="std std-ref">NodeStatusUplink</span></a></p></li>
<li><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/mqtt-message-reference#pans-nodeconfiguration"><span class="std std-ref">NodeConfiguration</span></a></p></li>
</ul>
</td>
<td><ul class="simple">
<li><p><cite>{prefix}/{networkId}/{nodegateway}/uplink/status/{deviceId}</cite> (QoS 1 / retained ✗)</p></li>
<li><p><cite>{prefix}/{networkId}/{nodegateway}/uplink/config/{deviceId}</cite> (QoS 1 / retained ✗)</p></li>
<li><p><cite>{prefix}/{networkId}/{nodegateway}/downlink/config/{deviceId}</cite> (QoS 1 / retained ✗)</p></li>
</ul>
</td>
<td><ul class="simple">
<li><p><a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/leaps-api/mqtt-message-reference#leaps-api-status"><span class="std std-ref">leaps_api.status</span></a></p></li>
<li><p><a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/leaps-api/mqtt-message-reference#leaps-api-node-config"><span class="std std-ref">leaps_api.node_config</span></a></p></li>
</ul>
</td>
<td><p>Map <cite>nodeType</cite> into <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/leaps-api/mqtt-message-reference#anchor-config"><span class="std std-ref">anchor_config</span></a>/<a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/leaps-api/mqtt-message-reference#tag-config"><span class="std std-ref">tag_config</span></a>; remove redundant <cite>networkId</cite>.</p></td>
</tr>
<tr class="row-odd"><td><p>Data &amp; service channels</p></td>
<td><ul class="simple">
<li><p><cite>{prefix}/node/{deviceId}/uplink/data</cite> (QoS 1 / retained ✗)</p></li>
<li><p><cite>{prefix}/node/{deviceId}/downlink/data</cite> (QoS 1 / retained ✗)</p></li>
<li><p><cite>{prefix}/node/{deviceId}/uplink/service</cite> (QoS 1 / retained ✗)</p></li>
<li><p><cite>{prefix}/node/{deviceId}/downlink/service</cite> (QoS 1 / retained ✗)</p></li>
</ul>
</td>
<td><ul class="simple">
<li><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/mqtt-message-reference#pans-nodedatauplink"><span class="std std-ref">节点数据链接</span></a> with Base64 payloads with optional <cite>superFrameNumber</cite></p></li>
<li><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/mqtt-message-reference#pans-nodedatadownlink"><span class="std std-ref">节点数据下行链路</span></a> with Base64 payloads with optional <cite>overwrite</cite></p></li>
<li><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/mqtt-message-reference#pans-nodeserviceuplink"><span class="std std-ref">NodeServiceUplink</span></a> / <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/mqtt-message-reference#pans-nodeservicedownlink"><span class="std std-ref">NodeServiceDownlink</span></a> TLV messages</p></li>
</ul>
</td>
<td><ul class="simple">
<li><p><cite>{prefix}/{networkId}/{nodegateway}/uplink/data/{deviceId}</cite> (QoS 1 / retained ✗)</p></li>
<li><p><cite>{prefix}/{networkId}/{nodegateway}/downlink/data/{deviceId}</cite> (QoS 1 / retained ✗)</p></li>
<li><p><cite>{prefix}/{networkId}/{nodegateway}/uplink/service/{deviceId}</cite> (QoS 1 / retained ✗)</p></li>
<li><p><cite>{prefix}/{networkId}/{nodegateway}/downlink/service/{deviceId}</cite> (QoS 1 / retained ✗)</p></li>
</ul>
</td>
<td><ul class="simple">
<li><p><a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/leaps-api/mqtt-message-reference#leaps-api-user-data"><span class="std std-ref">leaps_api.user_data</span></a></p></li>
<li><p><a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/leaps-api/mqtt-message-reference#leaps-api-service-data"><span class="std std-ref">leaps_api.service_data</span></a></p></li>
</ul>
</td>
<td><p>LEAPS omits <cite>superFrameNumber</cite>; keep timestamps and <cite>overwrite</cite> flags.</p></td>
</tr>
<tr class="row-even"><td><p>Location streams</p></td>
<td><p><cite>{prefix}/node/{deviceId}/uplink/location</cite> (QoS 0 / retained ✓)</p></td>
<td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/mqtt-message-reference#pans-nodelocationuplink"><span class="std std-ref">节点位置链接</span></a> (<a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/mqtt-message-reference#pans-position"><span class="std std-ref">位置</span></a>, superFrameNumber)</p></td>
<td><p><cite>{prefix}/{networkId}/node/uplink/location/{deviceId}</cite> (QoS 0 / retained ✗)</p></td>
<td><p><a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/leaps-api/mqtt-message-reference#leaps-api-location"><span class="std std-ref">leaps_api.location</span></a> (<a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/leaps-api/mqtt-message-reference#node-location"><span class="std std-ref">节点位置</span></a>, statistics)</p></td>
<td><p>Wrap coordinates inside <cite>location</cite> and drop <cite>superFrameNumber</cite>.</p></td>
</tr>
</tbody>
</table>
</div>
<hr class="docutils">
<div class="section" id="schema-alignment-and-translation-recipes">
<h2>2. Schema Alignment and Translation Recipes</h2>
<p>The following sections document the translation requirements for each
domain. Use them when refactoring publishers/consumers or building an
adapter.</p>
<div class="section" id="server-lifecycle">
<h3>2.1 Server Lifecycle</h3>
<ul>
<li><p><strong>PANS topics:</strong></p>
<ul class="simple">
<li><p>Uplink server status: <code class="docutils literal notranslate"><span class="pre">{prefix}/server</span></code> (retained, QoS 1)
publishing an empty or minimal JSON payload when the server is
online; broker LWT sends the same topic with an empty payload on
disconnect (See <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/mqtt-connector#pp-uplink"><span class="std std-ref">reference</span></a>).</p></li>
<li><p>Downlink commands: <code class="docutils literal notranslate"><span class="pre">{prefix}/server</span></code> carrying <code class="docutils literal notranslate"><span class="pre">ServerMessage</span></code>
requests such as <code class="docutils literal notranslate"><span class="pre">{"request":"REFRESH_TOPICS"}</span></code>
(See <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/mqtt-connector#pp-downlink"><span class="std std-ref">reference</span></a>).</p></li>
</ul>
</li>
<li><p><strong>LEAPS topics:</strong></p>
<ul class="simple">
<li><p>Uplink status: <code class="docutils literal notranslate"><span class="pre">{prefix}/server/status</span></code> (not retained, QoS 1)
conveying <code class="docutils literal notranslate"><span class="pre">leaps_api.server_status</span></code> payloads
(See <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/leaps-api/base-mqtt-messages#lr-uplink"><span class="std std-ref">reference1</span></a>
and <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/leaps-api/mqtt-message-reference#leaps-api-server-status"><span class="std std-ref">reference2</span></a>).</p></li>
<li><p>Downlink requests: <code class="docutils literal notranslate"><span class="pre">{prefix}/server/request</span></code> (not retained, QoS
1) using the same <code class="docutils literal notranslate"><span class="pre">leaps_api.server_status</span></code> schema for requests
(See <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/leaps-api/base-mqtt-messages#lr-downlink"><span class="std std-ref">reference</span></a>).</p></li>
</ul>
</li>
<li><p><strong>Translation steps:</strong></p>
<ol class="arabic simple">
<li><p><strong>Subscriber change:</strong> Update consumers to subscribe to
<code class="docutils literal notranslate"><span class="pre">{prefix}/server/status</span></code> (uplink) instead of
<code class="docutils literal notranslate"><span class="pre">{prefix}/server</span></code>. Expect JSON payloads with at least <code class="docutils literal notranslate"><span class="pre">state</span></code>
and handle disconnect events when <code class="docutils literal notranslate"><span class="pre">{"state":"DISCONNECTED"}</span></code> is
received.</p></li>
<li><p><strong>Publisher change:</strong> Configure the server (or bridge) to emit a
server status payloads such as <code class="docutils literal notranslate"><span class="pre">{"state":"CONNECTED"}</span></code> to
<code class="docutils literal notranslate"><span class="pre">{prefix}/server/status</span></code> and set the broker LWT on that topic to
publish <code class="docutils literal notranslate"><span class="pre">{"state":"DISCONNECTED"}</span></code>.</p></li>
<li><p><strong>Request routing:</strong> Move any command publications to
<code class="docutils literal notranslate"><span class="pre">{prefix}/server/request</span></code> and encode them as
<code class="docutils literal notranslate"><span class="pre">{"request":"PUBLISH_ALL_TOPICS"}</span></code> with optional <code class="docutils literal notranslate"><span class="pre">networks</span></code>
filters.</p></li>
</ol>
</li>
<li><p><strong>Before / After:</strong></p>
<div class="highlight-json notranslate"><div class="highlight"><pre><span></span><span class="c1">// PANS server status</span>
<span class="p">{}</span>

<span class="c1">// LEAPS server status</span>
<span class="p">{</span>
<span class="w">  </span><span class="nt">"state"</span><span class="p">:</span><span class="w"> </span><span class="s2">"CONNECTED"</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"version"</span><span class="p">:</span><span class="w"> </span><span class="s2">"2.2.8"</span>
<span class="p">}</span>
</pre></div>
</div>
</li>
</ul>
</div>
<hr class="docutils">
<div class="section" id="gateway-status-and-configuration">
<h3>2.2 Gateway Status and Configuration</h3>
<ul>
<li><p><strong>PANS topics:</strong></p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">{prefix}/gateway/{deviceId}/uplink</span></code> (retained, QoS 1) reporting
<code class="docutils literal notranslate"><span class="pre">GatewayStatusAndConfig</span></code> payloads with fields such as
<code class="docutils literal notranslate"><span class="pre">networkId</span></code>, <code class="docutils literal notranslate"><span class="pre">bridgeNodeId</span></code>, <code class="docutils literal notranslate"><span class="pre">version</span></code>, <code class="docutils literal notranslate"><span class="pre">uwb</span></code>, and nested
<code class="docutils literal notranslate"><span class="pre">configuration</span></code>
(See <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/mqtt-connector#pp-gatewaystatusandconfig"><span class="std std-ref">reference</span></a>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">{prefix}/gateway/{deviceId}/downlink</span></code> for configuration updates
(See <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/mqtt-connector#pp-downlink"><span class="std std-ref">reference</span></a>).</p></li>
</ul>
</li>
<li><p><strong>LEAPS topics:</strong></p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">{prefix}/{networkId}/gateway/uplink/status/{deviceId}</span></code> (not
retained, QoS 1) carrying <code class="docutils literal notranslate"><span class="pre">leaps_api.status</span></code>
(See <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/leaps-api/leaps-mqtt-connector#lr-uplink-gw"><span class="std std-ref">reference</span></a>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">{prefix}/{networkId}/gateway/uplink/config/{deviceId}</span></code> and
<code class="docutils literal notranslate"><span class="pre">{prefix}/{networkId}/gateway/downlink/config/{deviceId}</span></code> using
<code class="docutils literal notranslate"><span class="pre">leaps_api.node_config</span></code>
(<a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/leaps-api/leaps-mqtt-connector#lr-configuration-message"><span class="std std-ref">reference1</span></a>
and
<a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/leaps-api/mqtt-message-reference#leaps-api-node-config"><span class="std std-ref">reference2</span></a>).</p></li>
</ul>
</li>
<li><p><strong>Translation steps:</strong></p>
<ol class="arabic simple">
<li><p>Introduce the <code class="docutils literal notranslate"><span class="pre">{networkId}</span></code> path segment (using the value
previously found in the PANS <code class="docutils literal notranslate"><span class="pre">networkId</span></code> field). Remove the
now-duplicate <code class="docutils literal notranslate"><span class="pre">networkId</span></code> field from the payload.</p></li>
<li><p>Map gateway health indicators: <code class="docutils literal notranslate"><span class="pre">present</span></code>, <code class="docutils literal notranslate"><span class="pre">downlink</span></code>, <code class="docutils literal notranslate"><span class="pre">uwb</span></code>,
<code class="docutils literal notranslate"><span class="pre">batt</span></code>, and <code class="docutils literal notranslate"><span class="pre">temp</span></code> can be copied directly into
<code class="docutils literal notranslate"><span class="pre">leaps_api.status</span></code>. If PANS included <code class="docutils literal notranslate"><span class="pre">bridgeNodeId</span></code> or routing
diagnostics, log or expose them via observability channels because
LEAPS does not have one-to-one fields.</p></li>
<li><p>Restructure <code class="docutils literal notranslate"><span class="pre">configuration</span></code> into the <code class="docutils literal notranslate"><span class="pre">leaps_api.node_config</span></code>
shape:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">ipAddress[]</span></code>, <code class="docutils literal notranslate"><span class="pre">ipMask[]</span></code>, <code class="docutils literal notranslate"><span class="pre">ipGateway[]</span></code> →
<code class="docutils literal notranslate"><span class="pre">inet.ip[].addr</span></code>, <code class="docutils literal notranslate"><span class="pre">inet.ip[].mask</span></code>, <code class="docutils literal notranslate"><span class="pre">inet.ip[].gateway</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dns[]</span></code> → <code class="docutils literal notranslate"><span class="pre">inet.dns</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">interface</span></code> → <code class="docutils literal notranslate"><span class="pre">inet.iface</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">tls</span></code> → <code class="docutils literal notranslate"><span class="pre">inet.tls</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">server</span></code> / <code class="docutils literal notranslate"><span class="pre">port</span></code> → <code class="docutils literal notranslate"><span class="pre">inet.server.host</span></code> /
<code class="docutils literal notranslate"><span class="pre">inet.server.port</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">dhcp</span></code> → <code class="docutils literal notranslate"><span class="pre">inet.dhcp</span></code></p></li>
<li><p>Optional Wi-Fi fields → <code class="docutils literal notranslate"><span class="pre">wifi</span></code></p></li>
</ul>
</li>
<li><p>If firmware <code class="docutils literal notranslate"><span class="pre">version</span></code> details are required, subscribe them
through <code class="docutils literal notranslate"><span class="pre">{prefix}/server/status</span></code> or a management database; LEAPS
gateway config/topic does not transport release metadata.</p></li>
</ol>
</li>
<li><p><strong>Before / After:</strong></p>
<div class="highlight-json notranslate"><div class="highlight"><pre><span></span><span class="c1">// PANS gateway uplink</span>
<span class="p">{</span>
<span class="w">  </span><span class="nt">"networkId"</span><span class="p">:</span><span class="w"> </span><span class="mi">1</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"uwb"</span><span class="p">:</span><span class="w"> </span><span class="s2">"CONNECTED_BH"</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"configuration"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="nt">"ipAddress"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="s2">"10.0.1.10"</span><span class="p">],</span>
<span class="w">    </span><span class="nt">"ipMask"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="s2">"255.255.255.0"</span><span class="p">],</span>
<span class="w">    </span><span class="nt">"dns"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="s2">"8.8.8.8"</span><span class="p">],</span>
<span class="w">    </span><span class="nt">"interface"</span><span class="p">:</span><span class="w"> </span><span class="s2">"ETHERNET"</span><span class="p">,</span>
<span class="w">    </span><span class="nt">"tls"</span><span class="p">:</span><span class="w"> </span><span class="s2">"OFF"</span><span class="p">,</span>
<span class="w">    </span><span class="nt">"server"</span><span class="p">:</span><span class="w"> </span><span class="s2">"10.0.1.13"</span><span class="p">,</span>
<span class="w">    </span><span class="nt">"port"</span><span class="p">:</span><span class="w"> </span><span class="mi">7777</span>
<span class="w">  </span><span class="p">}</span>
<span class="p">}</span>

<span class="c1">// LEAPS gateway uplink (status + config pair)</span>
<span class="p">{</span>
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

<span class="p">{</span>
<span class="w">  </span><span class="nt">"label"</span><span class="p">:</span><span class="w"> </span><span class="s2">"DW590F-nWIFI"</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"uwb_mode"</span><span class="p">:</span><span class="w"> </span><span class="s2">"UWB_MODE_ACTIVE"</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"fw_update"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"inet"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="nt">"ip"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span>
<span class="w">      </span><span class="p">{</span><span class="nt">"addr"</span><span class="p">:</span><span class="w"> </span><span class="s2">"10.0.1.10"</span><span class="p">,</span><span class="w"> </span><span class="nt">"mask"</span><span class="p">:</span><span class="w"> </span><span class="s2">"255.255.255.0"</span><span class="p">}</span>
<span class="w">    </span><span class="p">],</span>
<span class="w">    </span><span class="nt">"dns"</span><span class="p">:</span><span class="w"> </span><span class="p">[</span><span class="s2">"8.8.8.8"</span><span class="p">],</span>
<span class="w">    </span><span class="nt">"iface"</span><span class="p">:</span><span class="w"> </span><span class="s2">"ETHERNET"</span><span class="p">,</span>
<span class="w">    </span><span class="nt">"tls"</span><span class="p">:</span><span class="w"> </span><span class="s2">"OFF"</span><span class="p">,</span>
<span class="w">    </span><span class="nt">"dhcp"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span><span class="p">,</span>
<span class="w">    </span><span class="nt">"server"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="nt">"host"</span><span class="p">:</span><span class="w"> </span><span class="s2">"10.0.1.13"</span><span class="p">,</span><span class="w"> </span><span class="nt">"port"</span><span class="p">:</span><span class="w"> </span><span class="mi">7777</span><span class="p">}</span>
<span class="w">  </span><span class="p">}</span>
<span class="p">}</span>
</pre></div>
</div>
</li>
</ul>
</div>
<hr class="docutils">
<div class="section" id="node-configuration-and-status">
<h3>2.3 Node Configuration and Status</h3>
<ul>
<li><p><strong>PANS topics:</strong></p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">{prefix}/node/{deviceId}/uplink/status</span></code> (retained, QoS 1) with
<code class="docutils literal notranslate"><span class="pre">NodeStatusUplink</span></code> payloads
(See <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/mqtt-connector#pp-nodestatusuplink"><span class="std std-ref">reference</span></a>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">{prefix}/node/{deviceId}/uplink/config</span></code> and
<code class="docutils literal notranslate"><span class="pre">{prefix}/node/{deviceId}/downlink/config</span></code> sharing
<code class="docutils literal notranslate"><span class="pre">NodeConfiguration</span></code> structures
(See <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/mqtt-connector#pp-nodestatusuplink"><span class="std std-ref">reference1</span></a>
and <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/mqtt-connector#pp-nodeconfigdownlink"><span class="std std-ref">reference2</span></a>).</p></li>
</ul>
</li>
<li><p><strong>LEAPS topics:</strong></p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">{prefix}/{networkId}/{node|gateway}/uplink/status/{deviceId}</span></code>
carrying <code class="docutils literal notranslate"><span class="pre">leaps_api.status</span></code>
(See <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/leaps-api/leaps-mqtt-connector#lr-uplink-gw"><span class="std std-ref">reference</span></a>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">{prefix}/{networkId}/{node|gateway}/{uplink|downlink}/config/{deviceId}</span></code>
using <code class="docutils literal notranslate"><span class="pre">leaps_api.node_config</span></code>
(See <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/leaps-api/leaps-mqtt-connector#lr-configuration-message"><span class="std std-ref">reference</span></a>).</p></li>
</ul>
</li>
<li><p><strong>Translation steps:</strong></p>
<ol class="arabic simple">
<li><p>Insert <code class="docutils literal notranslate"><span class="pre">{networkId}</span></code> and the device role (<code class="docutils literal notranslate"><span class="pre">node</span></code> or
<code class="docutils literal notranslate"><span class="pre">gateway</span></code>) into the topic path; remove redundant <code class="docutils literal notranslate"><span class="pre">networkId</span></code>
or <code class="docutils literal notranslate"><span class="pre">nodeType</span></code> identifiers from the payload.</p></li>
<li><p>Map shared fields directly: <code class="docutils literal notranslate"><span class="pre">present</span></code>, <code class="docutils literal notranslate"><span class="pre">downlink</span></code>, <code class="docutils literal notranslate"><span class="pre">uwb</span></code>,
<code class="docutils literal notranslate"><span class="pre">batt</span></code>, <code class="docutils literal notranslate"><span class="pre">batt_state</span></code>, <code class="docutils literal notranslate"><span class="pre">temp</span></code>, and <code class="docutils literal notranslate"><span class="pre">timestamp</span></code> match
one-to-one in <code class="docutils literal notranslate"><span class="pre">leaps_api.status</span></code>.</p></li>
<li><p>Convert configuration objects:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">configuration.label</span></code> → <code class="docutils literal notranslate"><span class="pre">label</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">nodeType</span></code> → choose between populating <code class="docutils literal notranslate"><span class="pre">anchor</span></code> (for
anchors/gateways) or <code class="docutils literal notranslate"><span class="pre">tag</span></code> (for tags); absence of a section
implies the other role</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">ble</span></code>, <code class="docutils literal notranslate"><span class="pre">leds</span></code>, <code class="docutils literal notranslate"><span class="pre">uwbFirmwareUpdate</span></code> → <code class="docutils literal notranslate"><span class="pre">ble</span></code>, <code class="docutils literal notranslate"><span class="pre">leds</span></code>,
<code class="docutils literal notranslate"><span class="pre">fw_update</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">anchor.position</span></code> (x/y/z/quality) → <code class="docutils literal notranslate"><span class="pre">anchor.location</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">anchor.routingConfig</span></code> (<code class="docutils literal notranslate"><span class="pre">ROUTING_CFG_*</span></code>) →
<code class="docutils literal notranslate"><span class="pre">anchor.routing</span></code> (<code class="docutils literal notranslate"><span class="pre">ROUTING_*</span></code> enum)</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">anchor.routingStatus</span></code> has no LEAPS equivalent; surface via
monitoring or drop</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">anchor.initiator</span></code> → <code class="docutils literal notranslate"><span class="pre">anchor.initiator</span></code></p></li>
<li><p>Tag settings (<code class="docutils literal notranslate"><span class="pre">TagConfiguration</span></code>) → <code class="docutils literal notranslate"><span class="pre">tag</span></code> fields
(<code class="docutils literal notranslate"><span class="pre">location_engine</span></code>, <code class="docutils literal notranslate"><span class="pre">low_power</span></code>, <code class="docutils literal notranslate"><span class="pre">stationary_detection</span></code>,
<code class="docutils literal notranslate"><span class="pre">update_rate_*</span></code>)</p></li>
</ul>
</li>
<li><p>Carry timestamps forward; ensure they are strings or integers
consistent with LEAPS examples (microseconds).</p></li>
</ol>
</li>
<li><p><strong>Before / After:</strong></p>
<div class="highlight-json notranslate"><div class="highlight"><pre><span></span><span class="c1">// PANS node config</span>
<span class="p">{</span>
<span class="w">  </span><span class="nt">"configuration"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="nt">"label"</span><span class="p">:</span><span class="w"> </span><span class="s2">"DW0F07"</span><span class="p">,</span>
<span class="w">    </span><span class="nt">"nodeType"</span><span class="p">:</span><span class="w"> </span><span class="s2">"ANCHOR"</span><span class="p">,</span>
<span class="w">    </span><span class="nt">"ble"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span><span class="p">,</span>
<span class="w">    </span><span class="nt">"leds"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span><span class="p">,</span>
<span class="w">    </span><span class="nt">"uwbFirmwareUpdate"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span><span class="p">,</span>
<span class="w">    </span><span class="nt">"anchor"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">      </span><span class="nt">"initiator"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span><span class="p">,</span>
<span class="w">      </span><span class="nt">"position"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="nt">"x"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span><span class="w"> </span><span class="nt">"y"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span><span class="w"> </span><span class="nt">"z"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span><span class="w"> </span><span class="nt">"quality"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span><span class="p">},</span>
<span class="w">      </span><span class="nt">"routingConfig"</span><span class="p">:</span><span class="w"> </span><span class="s2">"ROUTING_CFG_OFF"</span>
<span class="w">    </span><span class="p">}</span>
<span class="w">  </span><span class="p">}</span>
<span class="p">}</span>
<span class="c1">// PANS node uplink status</span>
<span class="p">{</span>
<span class="w"> </span><span class="nt">"present"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span><span class="p">,</span>
<span class="w"> </span><span class="nt">"downlink"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span><span class="p">,</span>
<span class="w"> </span><span class="nt">"batt"</span><span class="p">:</span><span class="w"> </span><span class="mi">100</span><span class="p">,</span>
<span class="w"> </span><span class="nt">"temp"</span><span class="p">:</span><span class="w"> </span><span class="mi">25</span><span class="p">,</span>
<span class="w"> </span><span class="nt">"batt_state"</span><span class="p">:</span><span class="mi">0</span><span class="p">,</span>
<span class="w"> </span><span class="nt">"timestamp"</span><span class="p">:</span><span class="s2">"1679494411479191"</span>
<span class="p">}</span>

<span class="c1">// LEAPS node config</span>
<span class="p">{</span>
<span class="w">  </span><span class="nt">"label"</span><span class="p">:</span><span class="w"> </span><span class="s2">"DW0F07"</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"uwb_mode"</span><span class="p">:</span><span class="w"> </span><span class="s2">"UWB_MODE_ACTIVE"</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"ble"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"leds"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"fw_update"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"anchor"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="nt">"initiator"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span><span class="p">,</span>
<span class="w">    </span><span class="nt">"location"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span><span class="nt">"x"</span><span class="p">:</span><span class="w"> </span><span class="mf">0.0</span><span class="p">,</span><span class="w"> </span><span class="nt">"y"</span><span class="p">:</span><span class="w"> </span><span class="mf">0.0</span><span class="p">,</span><span class="w"> </span><span class="nt">"z"</span><span class="p">:</span><span class="w"> </span><span class="mf">0.0</span><span class="p">,</span><span class="w"> </span><span class="nt">"quality"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span><span class="p">},</span>
<span class="w">    </span><span class="nt">"routing"</span><span class="p">:</span><span class="w"> </span><span class="s2">"ROUTING_OFF"</span>
<span class="w">  </span><span class="p">}</span>
<span class="p">}</span>
<span class="c1">// LEAPS node uplink status</span>
<span class="p">{</span>
<span class="w">  </span><span class="nt">"present"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"downlink"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"batt"</span><span class="p">:</span><span class="w"> </span><span class="mi">0</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"temp"</span><span class="p">:</span><span class="w"> </span><span class="mi">34</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"batt_state"</span><span class="p">:</span><span class="mi">1</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"timestamp"</span><span class="p">:</span><span class="s2">"1755336445063828"</span>
<span class="p">}</span>
</pre></div>
</div>
</li>
</ul>
</div>
<hr class="docutils">
<div class="section" id="uplink-data-and-service-channels">
<h3>2.4 Uplink Data and Service Channels</h3>
<ul>
<li><p><strong>PANS topics:</strong></p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">{prefix}/node/{deviceId}/uplink/data</span></code> and
<code class="docutils literal notranslate"><span class="pre">{prefix}/node/{deviceId}/downlink/data</span></code> carrying base64
payloads plus <code class="docutils literal notranslate"><span class="pre">superFrameNumber</span></code>
(See <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/mqtt-connector#pp-superframenumber"><span class="std std-ref">reference</span></a>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">{prefix}/node/{deviceId}/uplink/service</span></code> and
<code class="docutils literal notranslate"><span class="pre">{prefix}/node/{deviceId}/downlink/service</span></code> transporting TLV
command acknowledgements
(See <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/mqtt-connector#pp-superframenumber"><span class="std std-ref">reference1</span></a>,
and <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/mqtt-connector#pp-nodeconfigdownlink"><span class="std std-ref">reference2</span></a>).</p></li>
</ul>
</li>
<li><p><strong>LEAPS topics:</strong></p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">{prefix}/{networkId}/{node|gateway}/uplink/data/{deviceId}</span></code>
and corresponding downlink topics for <code class="docutils literal notranslate"><span class="pre">leaps_api.user_data</span></code>
(See <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/leaps-api/leaps-mqtt-connector#lr-data-message-01"><span class="std std-ref">reference1</span></a>
and <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/leaps-api/mqtt-message-reference#leaps-api-user-data"><span class="std std-ref">reference2</span></a>).</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">{prefix}/{networkId}/{node|gateway}/uplink/service/{deviceId}</span></code>
and downlink equivalents for <code class="docutils literal notranslate"><span class="pre">leaps_api.service_data</span></code>
(See <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/leaps-api/leaps-mqtt-connector#lr-service-message-01"><span class="std std-ref">reference</span></a>).</p></li>
</ul>
</li>
<li><p><strong>Translation steps:</strong></p>
<ol class="arabic simple">
<li><p>Add <code class="docutils literal notranslate"><span class="pre">{networkId}</span></code> and the device role to the topic path; drop
<code class="docutils literal notranslate"><span class="pre">superFrameNumber</span></code> unless an application explicitly requires it
(LEAPS does not define this field—store it in analytics or embed
it into <code class="docutils literal notranslate"><span class="pre">service_data</span></code> if necessary).</p></li>
<li><p>Preserve <code class="docutils literal notranslate"><span class="pre">data</span></code> as base64; ensure <code class="docutils literal notranslate"><span class="pre">overwrite</span></code> semantics follow
LEAPS expectations (optional boolean in both uplink and downlink
payloads).</p></li>
<li><p>Translate service message <code class="docutils literal notranslate"><span class="pre">type</span></code> values to the LEAPS enum names:
<code class="docutils literal notranslate"><span class="pre">TLV_API_CMD</span></code>, <code class="docutils literal notranslate"><span class="pre">TLV_API_ACK</span></code>, <code class="docutils literal notranslate"><span class="pre">TLV_API_NACK</span></code>
(See <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/leaps-api/mqtt-message-reference#tag-config"><span class="std std-ref">tag_config</span></a>).</p></li>
<li><p>Ensure timestamps stay in microseconds and remain optional fields
(<code class="docutils literal notranslate"><span class="pre">timestamp</span></code>).</p></li>
</ol>
</li>
<li><p><strong>Before / After:</strong></p>
<div class="highlight-json notranslate"><div class="highlight"><pre><span></span><span class="c1">// PANS uplink data</span>
<span class="p">{</span>
<span class="w">  </span><span class="nt">"data"</span><span class="p">:</span><span class="w"> </span><span class="s2">"ASNFZ4mrze8="</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"superFrameNumber"</span><span class="p">:</span><span class="w"> </span><span class="mi">1028</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"timestamp"</span><span class="p">:</span><span class="w"> </span><span class="s2">"1679495612282922"</span>
<span class="p">}</span>
<span class="c1">// PANS downlink data</span>
<span class="p">{</span>
<span class="w"> </span><span class="nt">"data"</span><span class="p">:</span><span class="w"> </span><span class="s2">"QUJDREVGR0hJSktMTU5PUFFSU1Q="</span><span class="p">,</span>
<span class="w"> </span><span class="nt">"overwrite"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span>
<span class="p">}</span>

<span class="c1">// LEAPS uplink data</span>
<span class="p">{</span>
<span class="w">  </span><span class="nt">"data"</span><span class="p">:</span><span class="w"> </span><span class="s2">"ASNFZ4mrze8="</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"timestamp"</span><span class="p">:</span><span class="w"> </span><span class="s2">"1679495612282922"</span>
<span class="p">}</span>
<span class="c1">// LEAPS downlink data</span>
<span class="p">{</span>
<span class="w">  </span><span class="nt">"data"</span><span class="p">:</span><span class="w"> </span><span class="s2">"QUJDREVGR0hJSktMTU5PUFFSU1Q="</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"overwrite"</span><span class="p">:</span><span class="w"> </span><span class="kc">true</span>
<span class="p">}</span>
</pre></div>
</div>
</li>
</ul>
</div>
<hr class="docutils">
<div class="section" id="location-streams">
<h3>2.5 Location Streams</h3>
<ul>
<li><p><strong>PANS topics:</strong> <code class="docutils literal notranslate"><span class="pre">{prefix}/node/{deviceId}/uplink/location</span></code> with
<code class="docutils literal notranslate"><span class="pre">NodeLocationUplink</span></code> payloads
(See <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/mqtt-connector#pp-uplink-location"><span class="std std-ref">reference</span></a>).</p></li>
<li><p><strong>LEAPS topics:</strong>
<code class="docutils literal notranslate"><span class="pre">{prefix}/{networkId}/node/uplink/location/{deviceId}</span></code> publishing
<code class="docutils literal notranslate"><span class="pre">leaps_api.location</span></code> payloads
(See <a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/leaps-api/leaps-mqtt-connector#lr-uplink-location"><span class="std std-ref">reference</span></a>).</p></li>
<li><p><strong>Translation steps:</strong></p>
<ol class="arabic simple">
<li><p>Add <code class="docutils literal notranslate"><span class="pre">{networkId}</span></code> to the topic and remove <code class="docutils literal notranslate"><span class="pre">networkId</span></code> fields
from the body.</p></li>
<li><p>Nest position coordinates inside the <code class="docutils literal notranslate"><span class="pre">location</span></code> object expected
by LEAPS: <code class="docutils literal notranslate"><span class="pre">position.x</span></code> → <code class="docutils literal notranslate"><span class="pre">location.x</span></code>, etc. If PANS supplied
<code class="docutils literal notranslate"><span class="pre">KernelPosition</span></code> bytes, convert them to floating-point meters
before publishing.</p></li>
<li><p>Move optional quality metrics into LEAPS statistics fields when
available (<code class="docutils literal notranslate"><span class="pre">sd_x</span></code>, <code class="docutils literal notranslate"><span class="pre">sd_y</span></code>, <code class="docutils literal notranslate"><span class="pre">sd_z</span></code>, <code class="docutils literal notranslate"><span class="pre">r95</span></code>, <code class="docutils literal notranslate"><span class="pre">toa</span></code>). Values
without direct equivalents can be stored in application-specific
telemetry streams.</p></li>
<li><p>Drop <code class="docutils literal notranslate"><span class="pre">superFrameNumber</span></code> or repurpose it within analytics; LEAPS
does not define that field in <code class="docutils literal notranslate"><span class="pre">leaps_api.location</span></code>.</p></li>
</ol>
</li>
<li><p><strong>Before / After:</strong></p>
<div class="highlight-json notranslate"><div class="highlight"><pre><span></span><span class="c1">// PANS location</span>
<span class="p">{</span>
<span class="w">  </span><span class="nt">"position"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="nt">"x"</span><span class="p">:</span><span class="w"> </span><span class="mf">3.25238609</span><span class="p">,</span>
<span class="w">    </span><span class="nt">"y"</span><span class="p">:</span><span class="w"> </span><span class="mf">-0.00895162672</span><span class="p">,</span>
<span class="w">    </span><span class="nt">"z"</span><span class="p">:</span><span class="w"> </span><span class="mf">0.42510426</span><span class="p">,</span>
<span class="w">    </span><span class="nt">"quality"</span><span class="p">:</span><span class="w"> </span><span class="mi">21</span>
<span class="w">  </span><span class="p">},</span>
<span class="w">  </span><span class="nt">"superFrameNumber"</span><span class="p">:</span><span class="w"> </span><span class="mi">1144</span><span class="p">,</span>
<span class="w">  </span><span class="nt">"timestamp"</span><span class="p">:</span><span class="w"> </span><span class="s2">"1679495047880989"</span>
<span class="p">}</span>

<span class="c1">// LEAPS location</span>
<span class="p">{</span>
<span class="w">  </span><span class="nt">"location"</span><span class="p">:</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="nt">"x"</span><span class="p">:</span><span class="w"> </span><span class="mf">3.25238609</span><span class="p">,</span>
<span class="w">    </span><span class="nt">"y"</span><span class="p">:</span><span class="w"> </span><span class="mf">-0.00895162672</span><span class="p">,</span>
<span class="w">    </span><span class="nt">"z"</span><span class="p">:</span><span class="w"> </span><span class="mf">0.42510426</span><span class="p">,</span>
<span class="w">    </span><span class="nt">"quality"</span><span class="p">:</span><span class="w"> </span><span class="mi">21</span>
<span class="w">  </span><span class="p">},</span>
<span class="w">  </span><span class="nt">"timestamp"</span><span class="p">:</span><span class="w"> </span><span class="s2">"1679495047880989"</span>
<span class="p">}</span>
</pre></div>
</div>
</li>
</ul>
</div>
</div>
<hr class="docutils">
<div class="section" id="environment-updates">
<h2>3. Environment Updates</h2>
<ul class="simple">
<li><p><strong>Broker configuration:</strong> Update topic ACLs, retained flags, and LWT
settings to accommodate the LEAPS namespace. Ensure
<code class="docutils literal notranslate"><span class="pre">{prefix}/server/status</span></code> and <code class="docutils literal notranslate"><span class="pre">{prefix}/server/request</span></code> are
available and that QoS requirements match the LEAPS documentation.</p></li>
<li><p><strong>Client endpoints:</strong> Point gateways and management tools to the
LEAPS server endpoints. Adjust client-side MQTT settings (QoS,
retain) to match the new specifications.</p></li>
<li><p><strong>Documentation:</strong> Record any broker-level changes so that future
deployments reference the LEAPS expectations instead of the legacy
ones.</p></li>
</ul>
</div>
<hr class="docutils">
<div class="section" id="cutover-validation">
<h2>4. Cutover &amp; Validation</h2>
<ul class="simple">
<li><p><strong>Staging rehearsal:</strong> Run the full traffic set through a staging
LEAPS deployment. Confirm that consumers process the new topics
without schema errors.</p></li>
<li><p><strong>Production cutover:</strong> Schedule the switch once staging passes.
Monitor the broker, adapter logs, and downstream applications for
discrepancies.</p></li>
<li><p><strong>Fallback plan:</strong> Maintain the adapter or dual-publish strategy
until metrics show stable consumption on the LEAPS topics.</p></li>
<li><p><strong>Alerting updates:</strong> Modify monitoring rules to inspect the new
topics (e.g., checking <code class="docutils literal notranslate"><span class="pre">state</span> <span class="pre">!=</span> <span class="pre">"CONNECTED"</span></code> on
<code class="docutils literal notranslate"><span class="pre">{prefix}/server/status</span></code>).</p></li>
</ul>
</div>
<hr class="docutils">
<div class="section" id="post-migration-cleanup">
<h2>5. Post-Migration Cleanup</h2>
<ol class="arabic simple">
<li><p>Retire PANS PRO topic publishers and remove obsolete ACLs from the
broker.</p></li>
<li><p>Decommission temporary adapters once every producer and consumer
speaks native LEAPS.</p></li>
<li><p>Archive the translation recipes and sample payloads. They remain
valuable for onboarding and audits.</p></li>
<li><p>Update team runbooks and diagrams to reflect the LEAPS RTLS
architecture.</p></li>
</ol>
</div>
<hr class="docutils">
<div class="section" id="appendices">
<h2>Appendices</h2>
<div class="section" id="a-reference-tables">
<h3>A. Reference Tables</h3>
<table class="docutils align-default">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Domain</p></th>
<th class="head"><p>Source docs</p></th>
<th class="head"><p>Target docs</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>Server lifecycle</p></td>
<td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/mqtt-connector#pans-mqtt-connector"><span class="std std-ref">MQTT 连接器</span></a></p></td>
<td><p><a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/leaps-api/base-mqtt-messages#leaps-base-mqtt-messages"><span class="std std-ref">基本 MQTT 消息</span></a></p></td>
</tr>
<tr class="row-odd"><td><p>Gateway status/config</p></td>
<td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/mqtt-connector#pans-mqtt-connector"><span class="std std-ref">MQTT 连接器</span></a></p></td>
<td><p><a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/leaps-api/leaps-mqtt-connector#leaps-mqtt-connector"><span class="std std-ref">LEAPS MQTT 连接器</span></a></p></td>
</tr>
<tr class="row-even"><td><p>Node status/config</p></td>
<td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/mqtt-connector#pans-mqtt-connector"><span class="std std-ref">MQTT 连接器</span></a></p></td>
<td><p><a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/leaps-api/leaps-mqtt-connector#leaps-mqtt-connector"><span class="std std-ref">LEAPS MQTT 连接器</span></a></p></td>
</tr>
<tr class="row-odd"><td><p>Data/service</p></td>
<td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/mqtt-connector#pans-mqtt-connector"><span class="std std-ref">MQTT 连接器</span></a></p></td>
<td><p><a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/leaps-api/leaps-mqtt-connector#leaps-mqtt-connector"><span class="std std-ref">LEAPS MQTT 连接器</span></a></p></td>
</tr>
<tr class="row-even"><td><p>Location</p></td>
<td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/mqtt-connector#pans-mqtt-connector"><span class="std std-ref">MQTT 连接器</span></a></p></td>
<td><p><a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/leaps-api/leaps-mqtt-connector#leaps-mqtt-connector"><span class="std std-ref">LEAPS MQTT 连接器</span></a></p></td>
</tr>
</tbody>
</table>
</div>
</div>
</div>


           </div>
