---
title: "API コマンドリスト"
lang: ja
slug: "leaps-rtls/integration-guide/leaps-api/api-list"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/leaps-rtls/integration-guide/leaps-api/api-list/"
order: 145
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="api-command-list">
<span id="api-commmand-list"></span><h1>API コマンドリスト</h1>
<p>次の表は、SPI/UART/BLE などのインターフェイス上の UWB サブシステム (UWBS) での API コマンドの可用性と、イーサネット ゲートウェイ モジュールでサポートされているかどうかの概要を示しています。</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 48%">
<col style="width: 14%">
<col style="width: 20%">
<col style="width: 18%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>API コマンド</p></th>
<th class="head"><p>UWBS</p></th>
<th class="head"><p>ゲートウェイ</p></th>
<th class="head"><p>(*)</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-gpio-cfg-output#leaps-gpio-cfg-output"><span class="std std-ref">leaps_gpio_cfg_output</span></a></p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-gpio-value-set#leaps-gpio-value-set"><span class="std std-ref">leaps_gpio_value_set</span></a></p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-gpio-value-toggle#leaps-gpio-value-toggle"><span class="std std-ref">leaps_gpio_value_toggle</span></a></p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-gpio-cfg-input#leaps-gpio-cfg-input"><span class="std std-ref">leaps_gpio_cfg_input</span></a></p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-gpio-value-get#leaps-gpio-value-get"><span class="std std-ref">leaps_gpio_value_get</span></a></p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-pos-get#leaps-pos-get"><span class="std std-ref">leaps_pos_get</span></a></p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-pos-set#leaps-pos-set"><span class="std std-ref">leaps_pos_set</span></a></p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-loc-get#leaps-loc-get"><span class="std std-ref">leaps_loc_get</span></a></p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-fw-update-start#leaps-fw-update-start"><span class="std std-ref">leaps_fw_update_start</span></a></p></td>
<td><p>はい</p></td>
<td><p>はい</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-fw-update-xfer#leaps-fw-update-xfer"><span class="std std-ref">leaps_fw_update_xfer</span></a></p></td>
<td><p>はい</p></td>
<td><p>はい</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-autopos-start#leaps-autopos-start"><span class="std std-ref">leaps_autopos_start</span></a></p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-upd-rate-set#leaps-upd-rate-set"><span class="std std-ref">leaps_upd_rate_set</span></a></p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-upd-rate-get#leaps-upd-rate-get"><span class="std std-ref">leaps_upd_rate_get</span></a></p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-upd-trigger#leaps-upd-trigger"><span class="std std-ref">leaps_upd_trigger</span></a></p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-dev-info-get#leaps-dev-info-get"><span class="std std-ref">leaps_dev_info_get</span></a></p></td>
<td><p>はい</p></td>
<td><p>はい</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-cfg-anchor-set#leaps-cfg-anchor-set"><span class="std std-ref">leaps_cfg_anchor_set</span></a></p></td>
<td><p>はい</p></td>
<td><p>はい</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-cfg-tag-set#leaps-cfg-tag-set"><span class="std std-ref">leaps_cfg_tag_set</span></a></p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-cfg-get#leaps-cfg-get"><span class="std std-ref">leaps_cfg_get</span></a></p></td>
<td><p>はい</p></td>
<td><p>はい</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-boot-cfg-set#leaps-boot-cfg-set"><span class="std std-ref">leaps_boot_cfg_set</span></a></p></td>
<td><p>はい</p></td>
<td><p>はい</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-boot-cfg-get#leaps-boot-cfg-get"><span class="std std-ref">leaps_boot_cfg_get</span></a></p></td>
<td><p>はい</p></td>
<td><p>はい</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-ble-evt-cfg-set#leaps-ble-evt-cfg-set"><span class="std std-ref">leaps_ble_evt_cfg_set</span></a></p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-ble-evt-cfg-get#leaps-ble-evt-cfg-get"><span class="std std-ref">leaps_ble_evt_cfg_get</span></a></p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-serial-cfg-set#leaps-serial-cfg-set"><span class="std std-ref">leaps_serial_cfg_set</span></a></p></td>
<td><p>はい</p></td>
<td><p>はい</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-serial-cfg-get#leaps-serial-cfg-get"><span class="std std-ref">leaps_serial_cfg_get</span></a></p></td>
<td><p>はい</p></td>
<td><p>はい</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-dist-alarm-cfg-set#leaps-dist-alarm-cfg-set"><span class="std std-ref">leaps_dist_alarm_cfg_set</span></a></p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-dist-alarm-cfg-get#leaps-dist-alarm-cfg-get"><span class="std std-ref">leaps_dist_alarm_cfg_get</span></a></p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-alarm-start#leaps-alarm-start"><span class="std std-ref">leaps_alarm_start</span></a></p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-filter-cfg-get#leaps-filter-cfg-get"><span class="std std-ref">leaps_filter_cfg_get</span></a></p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-filter-cfg-set#leaps-filter-cfg-set"><span class="std std-ref">leaps_filter_cfg_set</span></a></p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-mac-addr-get#leaps-mac-addr-get"><span class="std std-ref">leaps_mac_addr_get</span></a></p></td>
<td><p>はい</p></td>
<td><p>はい</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-mac-addr-set#leaps-mac-addr-set"><span class="std std-ref">leaps_mac_addr_set</span></a></p></td>
<td><p>はい</p></td>
<td><p>はい</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-mac-addr-set-once#leaps-mac-addr-set-once"><span class="std std-ref">leaps_mac_addr_set_once</span></a></p></td>
<td><p>はい</p></td>
<td><p>はい</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps_api_cmd_an_seat_set#leaps-api-cmd-an-seat-set"><span class="std std-ref">leaps_api_cmd_an_seat_set</span></a></p></td>
<td><p>はい</p></td>
<td><p>はい</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps_api_cmd_an_seat_get#leaps-api-cmd-an-seat-get"><span class="std std-ref">leaps_api_cmd_an_seat_get</span></a></p></td>
<td><p>はい</p></td>
<td><p>はい</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-hw-ver-set-once#leaps-hw-ver-set-once"><span class="std std-ref">leaps_hw_ver_set_once</span></a></p></td>
<td><p>はい</p></td>
<td><p>はい</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-enc-key-set#leaps-enc-key-set"><span class="std std-ref">leaps_enc_key_set</span></a></p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-enc-key-clear#leaps-enc-key-clear"><span class="std std-ref">leaps_enc_key_clear</span></a></p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-anchor-list-get#leaps-anchor-list-get"><span class="std std-ref">leaps_anchor_list_get</span></a></p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-panid-set#leaps-panid-set"><span class="std std-ref">leaps_panid_set</span></a></p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-panid-get#leaps-panid-get"><span class="std std-ref">leaps_panid_get</span></a></p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-panid-profile-set#leaps-panid-profile-set"><span class="std std-ref">leaps_panid_profile_set</span></a></p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-panid-profile-get#leaps-panid-profile-get"><span class="std std-ref">leaps_panid_profile_get</span></a></p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-node-id-get#leaps-node-id-get"><span class="std std-ref">leaps_node_id_get</span></a></p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-reset#leaps-reset"><span class="std std-ref">leaps_reset</span></a></p></td>
<td><p>はい</p></td>
<td><p>はい</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-factory-reset#leaps-factory-reset"><span class="std std-ref">leaps_factory_reset</span></a></p></td>
<td><p>はい</p></td>
<td><p>はい</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-turn-off#leaps-turn-off"><span class="std std-ref">leaps_turn_off</span></a></p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-blink-leds#leaps-blink-leds"><span class="std std-ref">leaps_blink_leds</span></a></p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-int-cfg-set#leaps-int-cfg-set"><span class="std std-ref">leaps_int_cfg_set</span></a></p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-int-cfg-get#leaps-int-cfg-get"><span class="std std-ref">leaps_int_cfg_get</span></a></p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-stnry-cfg-set#leaps-stnry-cfg-set"><span class="std std-ref">leaps_stnry_cfg_set</span></a></p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-stnry-cfg-get#leaps-stnry-cfg-get"><span class="std std-ref">leaps_stnry_cfg_get</span></a></p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-label-read#leaps-label-read"><span class="std std-ref">leaps_label_read</span></a></p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-label-write#leaps-label-write"><span class="std std-ref">leaps_label_write</span></a></p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-usr-data-read#leaps-usr-data-read"><span class="std std-ref">leaps_usr_data_read</span></a></p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-usr-data-write#leaps-usr-data-write"><span class="std std-ref">leaps_usr_data_write</span></a></p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-uwb-rf-cpl-set#leaps-uwb-rf-cpl-set"><span class="std std-ref">leaps_uwb_rf_cpl_set</span></a></p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-uwb-cfg-set#leaps-uwb-cfg-set"><span class="std std-ref">leaps_uwb_cfg_set</span></a></p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-uwb-cfg-get#leaps-uwb-cfg-get"><span class="std std-ref">leaps_uwb_cfg_get</span></a></p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-uwb-profile-get#leaps-uwb-profile-get"><span class="std std-ref">leaps_uwb_profile_get</span></a></p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-status-get#leaps-status-get"><span class="std std-ref">leaps_status_get</span></a></p></td>
<td><p>はい</p></td>
<td><p>はい</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-dev-status-get#leaps-dev-status-get"><span class="std std-ref">leaps_dev_status_get</span></a></p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-sleep#leaps-sleep"><span class="std std-ref">leaps_sleep</span></a></p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-uwbs-set#leaps-uwbs-set"><span class="std std-ref">leaps_uwbs_set</span></a></p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-uwbs-get#leaps-uwbs-get"><span class="std std-ref">leaps_uwbs_get</span></a></p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/leaps-api/leaps-bh-status-get#leaps-bh-status-get"><span class="std std-ref">leaps_bh_status_get</span></a></p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/leaps-api/leaps-bh-xfer#leaps-bh-xfer"><span class="std std-ref">leaps_bh_xfer</span></a></p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-cert-update-start#leaps-cert-update-start"><span class="std std-ref">leaps_cert_update_start</span></a></p></td>
<td><p>いいえ</p></td>
<td><p>はい</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-cert-update-write#leaps-cert-update-write"><span class="std std-ref">leaps_cert_update_write</span></a></p></td>
<td><p>いいえ</p></td>
<td><p>はい</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-stats-clear#leaps-stats-clear"><span class="std std-ref">leaps_stats_clear</span></a></p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-stats-get#leaps-stats-get"><span class="std std-ref">leaps_stats_get</span></a></p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps_inet_cfg_set#leaps-inet-cfg-set"><span class="std std-ref">leaps_inet_cfg_set</span></a></p></td>
<td><p>いいえ</p></td>
<td><p>はい</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps_inet_cfg_get#leaps-inet-cfg-get"><span class="std std-ref">leaps_inet_cfg_get</span></a></p></td>
<td><p>いいえ</p></td>
<td><p>はい</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps_peer_cfg_set#leaps-peer-cfg-set"><span class="std std-ref">leaps_peer_cfg_set</span></a></p></td>
<td><p>いいえ</p></td>
<td><p>はい</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps_peer_cfg_get#leaps-peer-cfg-get"><span class="std std-ref">leaps_peer_cfg_get</span></a></p></td>
<td><p>いいえ</p></td>
<td><p>はい</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps_wifi_cfg_set#leaps-wifi-cfg-set"><span class="std std-ref">leaps_wifi_cfg_set</span></a></p></td>
<td><p>いいえ</p></td>
<td><p>はい</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps_wifi_cfg_get#leaps-wifi-cfg-get"><span class="std std-ref">leaps_wifi_cfg_get</span></a></p></td>
<td><p>いいえ</p></td>
<td><p>はい</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>(*) N: 新規、M: 変更、-: LEAPS RTLS と比較して変更なし</p>
<hr class="docutils">
<div class="toctree-wrapper compound">
</div>
<div class="section" id="backhaul-commands">
<h2>バックホールコマンド</h2>
<p>このセクションでは、DWM モジュールが <code class="docutils literal notranslate"><span class="pre">ゲートウェイ</span></code> として構成されている場合に、SPI インターフェイス経由でデータを定期的に転送するために使用される API コマンドについて説明します (API 呼び出し <a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/api-commands/leaps-cfg-anchor-set#leaps-cfg-anchor-set"><span class="std std-ref">leaps_cfg_anchor_set</span></a> を参照)。</p>
<div class="toctree-wrapper compound">
<ul>
<li class="toctree-l1"><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/leaps-api/leaps-bh-status-get">leaps_bh_status_get</a></li>
<li class="toctree-l1"><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/leaps-api/leaps-bh-config">leaps_bh_config</a></li>
<li class="toctree-l1"><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/leaps-api/leaps-bh-xfer">leaps_bh_xfer</a></li>
<li class="toctree-l1"><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/leaps-api/leaps-bh-xfer#bh-transfer-over-usb">USB 経由の BH 転送</a></li>
</ul>
</div>
</div>
</div>


           </div>
