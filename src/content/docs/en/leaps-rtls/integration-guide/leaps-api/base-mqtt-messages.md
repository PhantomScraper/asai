---
title: "Base MQTT messages"
lang: en
slug: "leaps-rtls/integration-guide/leaps-api/base-mqtt-messages"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/leaps-rtls/integration-guide/leaps-api/base-mqtt-messages/"
order: 77
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="base-mqtt-messages">
<span id="leaps-base-mqtt-messages"></span><h1>Base MQTT messages</h1>
<div class="section" id="uplink">
<span id="lr-uplink"></span><h2>Uplink</h2>
<p>The Uplink messages common to all MQTT connectors.</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 40%">
<col style="width: 60%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>Topic</strong></p></th>
<th class="head"><p><strong>Description</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>{prefix}/server/status</p></td>
<td><div class="line-block">
<div class="line">Status of the LEAPS Server.</div>
<div class="line">Refer to <a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/leaps-api/mqtt-message-reference#leaps-api-server-status"><span class="std std-ref">leaps_api.server_status</span></a>.</div>
</div>
<ul class="simple">
<li><p>retained = false</p></li>
<li><p>qos = 1</p></li>
</ul>
<p>Example:</p>
<div class="highlight-json notranslate"><div class="highlight"><pre><span></span><span class="p">{</span>
<span class="w"> </span><span class="nt">"state"</span><span class="p">:</span><span class="s2">"CONNECTED"</span><span class="p">,</span><span class="nt">"version"</span><span class="p">:</span><span class="s2">"2.2.8"</span>
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
<span id="lr-downlink"></span><h2>Downlink</h2>
<p>The Downlink messages accepted by all MQTT connectors.</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 31%">
<col style="width: 69%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>Topic</strong></p></th>
<th class="head"><p><strong>Description</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>{prefix}/server/request</p></td>
<td><div class="line-block">
<div class="line">Request to the LEAPS Server.</div>
<div class="line">Refer to <a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/leaps-api/mqtt-message-reference#leaps-api-server-request"><span class="std std-ref">leaps_api.server_request</span></a>.</div>
</div>
<p>Example:</p>
<div class="highlight-json notranslate"><div class="highlight"><pre><span></span><span class="p">{</span>
<span class="w">  </span><span class="nt">"request"</span><span class="p">:</span><span class="s2">"PUBLISH_ALL_TOPICS"</span>
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
