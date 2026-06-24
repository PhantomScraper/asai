---
title: "leaps_bh_config"
lang: en
slug: "leaps-rtls/integration-guide/leaps-api/leaps-bh-config"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/leaps-rtls/integration-guide/leaps-api/leaps-bh-config/"
order: 292
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-bh-config">
<span id="id1"></span><h1>leaps_bh_config</h1>
<p><strong>Prerequisites</strong></p>
<ul class="simple">
<li><p>Setup SPI between host MCU and Leaps board.</p></li>
<li><p>Connect to Leap api_irq pin (this is the interrupt to receive data for each TLV response).</p></li>
</ul>
<p><strong>Steps to initialize Leaps board as a gateway node</strong></p>
<p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/api-commands/leaps-int-cfg-set#leaps-int-cfg-set"><span class="std std-ref">leaps_int_cfg_set</span></a></p>
<ul class="simple">
<li><p>Send 3402000e</p></li>
</ul>
<p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/api-commands/leaps-serial-cfg-get#leaps-serial-cfg-get"><span class="std std-ref">leaps_serial_cfg_get</span></a></p>
<ul class="simple">
<li><p>Send 3900</p></li>
<li><p>Copy received configuration</p></li>
<li><p>Set USB backhaul enable to 0 (for SPI interface)</p></li>
</ul>
<p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/api-commands/leaps-serial-cfg-set#leaps-serial-cfg-set"><span class="std std-ref">leaps_serial_cfg_set</span></a>
- Example: send 380400000000 (USB backhaul enable = 0)</p>
<p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/api-commands/leaps-cfg-get#leaps-cfg-get"><span class="std std-ref">leaps_cfg_get</span></a></p>
<ul class="simple">
<li><p>Send 0800</p></li>
<li><p>Copy initiator, gateway, enc_en, led_en, ble_en, fw_update_en, uwb_mode, profile_id, clock_reference, uwb_activation_ble</p></li>
<li><p>Set uwb_bh_routing to ON</p></li>
</ul>
<p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/api-commands/leaps-cfg-anchor-set#leaps-cfg-anchor-set"><span class="std std-ref">leaps_cfg_anchor_set</span></a></p>
<ul class="simple">
<li><p>Example: send 07039e0110</p></li>
</ul>
<p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/api-commands/leaps-reset#leaps-reset"><span class="std std-ref">leaps_reset</span></a></p>
<ul class="simple">
<li><p>Send 1400</p></li>
</ul>
</div>


           </div>
