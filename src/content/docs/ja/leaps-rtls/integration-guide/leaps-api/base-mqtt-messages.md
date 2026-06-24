---
title: "基本 MQTT メッセージ"
lang: ja
slug: "leaps-rtls/integration-guide/leaps-api/base-mqtt-messages"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/leaps-rtls/integration-guide/leaps-api/base-mqtt-messages/"
order: 77
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="base-mqtt-messages">
<span id="leaps-base-mqtt-messages"></span><h1>基本 MQTT メッセージ</h1>
<div class="section" id="uplink">
<span id="lr-uplink"></span><h2>アップリンク</h2>
<p>すべての MQTT コネクタに共通のアップリンク メッセージ。</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 40%">
<col style="width: 60%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>トピック</strong></p></th>
<th class="head"><p><strong>説明</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>{prefix}/server/status</p></td>
<td><div class="line-block">
<div class="line">LEAPS Serverのステータス。</div>
<div class="line">Refer to <a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/leaps-api/mqtt-message-reference#leaps-api-server-status"><span class="std std-ref">leaps_api.server_status</span></a>。</div>
</div>
<ul class="simple">
<li><p>保持 = 偽</p></li>
<li><p>qos = 1</p></li>
</ul>
<p>例:</p>
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
<span id="lr-downlink"></span><h2>ダウンリンク</h2>
<p>すべての MQTT コネクタによって受け入れられるダウンリンク メッセージ。</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 31%">
<col style="width: 69%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>トピック</strong></p></th>
<th class="head"><p><strong>説明</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>{prefix}/server/request</p></td>
<td><div class="line-block">
<div class="line">LEAPS Serverへのリクエスト。</div>
<div class="line">Refer to <a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/leaps-api/mqtt-message-reference#leaps-api-server-request"><span class="std std-ref">leaps_api.server_request</span></a>.</div>
</div>
<p>例:</p>
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
