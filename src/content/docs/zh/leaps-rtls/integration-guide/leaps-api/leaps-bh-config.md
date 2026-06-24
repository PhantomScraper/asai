---
title: "leaps_bh_config"
lang: zh
slug: "leaps-rtls/integration-guide/leaps-api/leaps-bh-config"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/leaps-rtls/integration-guide/leaps-api/leaps-bh-config/"
order: 291
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-bh-config">
<span id="id1"></span><h1>leaps_bh_config</h1>
<p><strong>先决条件</strong></p>
<ul class="simple">
<li><p>在主机MCU和Leaps板之间设置SPI。</p></li>
<li><p>连接到Leap api_irq引脚（这是接收每个TLV响应数据的中断）。</p></li>
</ul>
<p><strong>将Leaps板初始化为网关节点的步骤</strong></p>
<p><a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/api-commands/leaps-int-cfg-set#leaps-int-cfg-set"><span class="std std-ref">leaps_int_cfg_set</span></a></p>
<ul class="simple">
<li><p>发送3402000e</p></li>
</ul>
<p><a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/api-commands/leaps-serial-cfg-get#leaps-serial-cfg-get"><span class="std std-ref">leaps_serial_cfg_get</span></a></p>
<ul class="simple">
<li><p>发送3900</p></li>
<li><p>复制接收到的配置</p></li>
<li><p>将USB回程启用设置为0（用于SPI接口）</p></li>
</ul>
<p><a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/api-commands/leaps-serial-cfg-set#leaps-serial-cfg-set"><span class="std std-ref">leaps_serial_cfg_set</span></a> - 示例：发送380400000000（USB回程启用=0）</p>
<p><a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/api-commands/leaps-cfg-get#leaps-cfg-get"><span class="std std-ref">leaps_cfg_get</span></a></p>
<ul class="simple">
<li><p>发送0800</p></li>
<li><p>复制启动器、网关、 enc_en, led_en, ble_en, fw_update_en, uwb_mode, profile_id, clock_reference, uwb_activation_ble</p></li>
<li><p>将uwb_bh_route设置为ON</p></li>
</ul>
<p><a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/api-commands/leaps-cfg-anchor-set#leaps-cfg-anchor-set"><span class="std std-ref">leaps_cfg_anchor_set</span></a></p>
<ul class="simple">
<li><p>示例:发送07039e0110</p></li>
</ul>
<p><a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/api-commands/leaps-reset#leaps-reset"><span class="std std-ref">leaps_reset</span></a></p>
<ul class="simple">
<li><p>发送1400</p></li>
</ul>
</div>


           </div>
