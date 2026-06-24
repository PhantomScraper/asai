---
title: "MQTT API"
lang: ja
slug: "leaps-rtls/integration-guide/leaps-api/mqtt-api"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/leaps-rtls/integration-guide/leaps-api/mqtt-api/"
order: 76
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="mqtt-api">
<span id="leaps-mqtt-api"></span><h1>MQTT API</h1>
<p>このページでは、<a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-server#leapsserver"><span class="std std-ref">LEAPS Server</span></a> との通信に使用される MQTT メッセージについて説明します。MQTT インターフェース上のすべてのメッセージは JSON 形式です。<a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-server#leapsserver"><span class="std std-ref">LEAPS Server</span></a> はコネクタを介して世界と通信します。フィルタリング/処理済みのアップリンクデータを世界に向けて送信し、ダウンリンクデータを受信して​​ UWB ネットワークに転送します。</p>
<p>LEAPS ネットワークのコンセプトを示し、MQTT Brokerとネットワークの接続を視覚化します。</p>
<img alt="../../../../_images/leaps-architect-solution.png" class="align-center" src="/docs-assets/ja/_images/leaps-architect-solution.png">
<hr class="docutils">
<p>次のセクションでは、MQTT API の詳細について説明します。</p>
<div class="toctree-wrapper compound">
<ul>
<li class="toctree-l1"><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/leaps-api/base-mqtt-messages">基本 MQTT メッセージ</a></li>
<li class="toctree-l1"><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/leaps-api/leaps-mqtt-connector">LEAPS MQTT コネクタ</a></li>
<li class="toctree-l1"><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/leaps-api/mqtt-message-reference">MQTT メッセージ参照</a></li>
</ul>
</div>
</div>


           </div>
