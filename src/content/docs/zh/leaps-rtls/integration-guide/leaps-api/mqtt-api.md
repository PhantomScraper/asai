---
title: "MQTT API"
lang: zh
slug: "leaps-rtls/integration-guide/leaps-api/mqtt-api"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/leaps-rtls/integration-guide/leaps-api/mqtt-api/"
order: 76
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="mqtt-api">
<span id="leaps-mqtt-api"></span><h1>MQTT API</h1>
<p>此页面描述了用于与 <a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-server#leapsserver"><span class="std std-ref">LEAPS Server</span></a> 通信的MQTT消息。MQTT接口上的所有消息都是JSON格式的。<a class="reference internal" href="/docs/zh/leaps-rtls/infrastructure/leaps-server#leapsserver"><span class="std std-ref">LEAPS Server</span></a> 通过连接器与World通信。它向世界提供经过滤波/处理的上行链路数据，并接收下行链路数据并将其转发到UWB网络。</p>
<p>这是LEAPS网络概念，可视化网络与MQTT Broker的连接</p>
<img alt="../../../../_images/leaps-architect-solution.png" class="align-center" src="/docs-assets/zh-cn/_images/leaps-architect-solution.png">
<hr class="docutils">
<p>以下部分描述了MQTT API的详细信息:</p>
<div class="toctree-wrapper compound">
<ul>
<li class="toctree-l1"><a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/leaps-api/base-mqtt-messages">基本 MQTT 消息</a></li>
<li class="toctree-l1"><a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/leaps-api/leaps-mqtt-connector">LEAPS MQTT 连接器</a></li>
<li class="toctree-l1"><a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/leaps-api/mqtt-message-reference">MQTT 消息参考</a></li>
</ul>
</div>
</div>


           </div>
