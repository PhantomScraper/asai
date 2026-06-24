---
title: "leaps_bh_config"
lang: ja
slug: "leaps-rtls/integration-guide/leaps-api/leaps-bh-config"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/leaps-rtls/integration-guide/leaps-api/leaps-bh-config/"
order: 291
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-bh-config">
<span id="id1"></span><h1>leaps_bh_config</h1>
<p><strong>前提条件</strong></p>
<ul class="simple">
<li><p>ホストMCUとLeapボード間のSPIをセットアップする。</p></li>
<li><p>Leap api_irq pin（TLV応答ごとにデータを受信するための割り込み）に接続する。</p></li>
</ul>
<p><strong>ゲートウェイノードとしてLeapsボードを初期化するためのステップ</strong></p>
<p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-int-cfg-set#leaps-int-cfg-set"><span class="std std-ref">leaps_int_cfg_set</span></a></p>
<ul class="simple">
<li><p>3402000eを送信します</p></li>
</ul>
<p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-serial-cfg-get#leaps-serial-cfg-get"><span class="std std-ref">leaps_serial_cfg_get</span></a></p>
<ul class="simple">
<li><p>3900を送信します</p></li>
<li><p>受信したコンフィギュレーションをコピー</p></li>
<li><p>USBバックホールイネーブルを0に設定する（SPIインターフェース用）</p></li>
</ul>
<p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-serial-cfg-set#leaps-serial-cfg-set"><span class="std std-ref">leaps_serial_cfg_set</span></a> - 例:380400000000 を送信 (USB バックホールイネーブル = 0)</p>
<p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-cfg-get#leaps-cfg-get"><span class="std std-ref">leaps_cfg_get</span></a></p>
<ul class="simple">
<li><p>0800を送信します</p></li>
<li><p>イニシエータ、ゲートウェイ、 enc_en, led_en, ble_en, fw_update_en, uwb_mode, profile_id, clock_reference, uwb_activation_bleをコピー</p></li>
<li><p>uwb_bh_routingをONに設定</p></li>
</ul>
<p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-cfg-anchor-set#leaps-cfg-anchor-set"><span class="std std-ref">leaps_cfg_anchor_set</span></a></p>
<ul class="simple">
<li><p>例:07039e0110を送信します</p></li>
</ul>
<p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-reset#leaps-reset"><span class="std std-ref">leaps_reset</span></a></p>
<ul class="simple">
<li><p>1400を送信します</p></li>
</ul>
</div>


           </div>
