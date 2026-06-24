---
title: "MQTT API"
lang: en
slug: "leaps-rtls/integration-guide/leaps-api/mqtt-api"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/leaps-rtls/integration-guide/leaps-api/mqtt-api/"
order: 76
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="mqtt-api">
<span id="leaps-mqtt-api"></span><h1>MQTT API</h1>
<p>This page describes the MQTT messages used to communicate with the <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-server#leapsserver"><span class="std std-ref">LEAPS Server</span></a>.
All messages on the MQTT interface are in JSON format.
The <a class="reference internal" href="/docs/en/leaps-rtls/infrastructure/leaps-server#leapsserver"><span class="std std-ref">LEAPS Server</span></a> communicates with the World via connectors. It provides filtered / processed
uplink data to the world and receives and forwards the downlink data toward the UWB network.</p>
<p>Here is the LEAPS Network concept, visualize the connection of network with MQTT Broker</p>
<img alt="../../../../_images/leaps-architect-solution.png" class="align-center" src="/docs-assets/_images/leaps-architect-solution.png">
<hr class="docutils">
<p>Following section describe detail of MQTT API:</p>
<div class="toctree-wrapper compound">
<ul>
<li class="toctree-l1"><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/leaps-api/base-mqtt-messages">Base MQTT messages</a></li>
<li class="toctree-l1"><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/leaps-api/leaps-mqtt-connector">LEAPS MQTT Connector</a></li>
<li class="toctree-l1"><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/leaps-api/mqtt-message-reference">MQTT Message Reference</a></li>
</ul>
</div>
</div>


           </div>
