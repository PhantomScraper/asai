---
title: "API 命令列表"
lang: zh
slug: "pans-pro-rtls/integration-guide/api-command-list"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/pans-pro-rtls/integration-guide/api-command-list/"
order: 155
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="api-command-list">
<h1>API 命令列表</h1>
<p>下表概括说明 API 命令在 SPI/UART 等接口, 板载 C 代码应用程序上的可用性，以及是否支持以太网网关模块。</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 28%">
<col style="width: 11%">
<col style="width: 11%">
<col style="width: 15%">
<col style="width: 22%">
<col style="width: 14%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>应用程序接口指令</p></th>
<th class="head"><p>SPI DWM1001</p></th>
<th class="head"><p>UART DWM1001</p></th>
<th class="head"><p>UART/USB 网关</p></th>
<th class="head"><p>板载用户应用程序 DWM1001</p></th>
<th class="head"><p>PANS PRO(*)</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm-pos-set#dwm-pos-set"><span class="std std-ref">dwm_pos_set</span></a></p></td>
<td><p>是</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
<td><p>是</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm-pos-get#dwm-pos-get"><span class="std std-ref">dwm_pos_get</span></a></p></td>
<td><p>是</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
<td><p>是</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm-upd-rate-set#dwm-upd-rate-set"><span class="std std-ref">dwm_upd_rate_set</span></a></p></td>
<td><p>是</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
<td><p>是</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm-upd-rate-get#dwm-upd-rate-get"><span class="std std-ref">dwm_upd_rate_get</span></a></p></td>
<td><p>是</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
<td><p>是</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm-cfg-tag-set#dwm-cfg-tag-set"><span class="std std-ref">dwm_cfg_tag_set</span></a></p></td>
<td><p>是</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
<td><p>是</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm-cfg-anchor-set#dwm-cfg-anchor-set"><span class="std std-ref">dwm_cfg_anchor_set</span></a></p></td>
<td><p>是</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
<td><p>是</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm-cfg-get#dwm-cfg-get"><span class="std std-ref">dwm_cfg_get</span></a></p></td>
<td><p>是</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
<td><p>是</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm-sleep#dwm-sleep"><span class="std std-ref">dwm_sleep</span></a></p></td>
<td><p>是</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
<td><p>是</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm-anchor-list-get#dwm-anchor-list-get"><span class="std std-ref">dwm_anchor_list_get</span></a></p></td>
<td><p>是</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
<td><p>是</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm-loc-get#dwm-loc-get"><span class="std std-ref">dwm_loc_get</span></a></p></td>
<td><p>是</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
<td><p>是</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm-baddr-get#dwm-baddr-get"><span class="std std-ref">dwm_baddr_get</span></a></p></td>
<td><p>是</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
<td><p>是</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm-stnry-cfg-set#dwm-stnry-cfg-set"><span class="std std-ref">dwm_stnry_cfg_set</span></a></p></td>
<td><p>是</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
<td><p>是</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm-stnry-cfg-get#dwm-stnry-cfg-get"><span class="std std-ref">dwm_stnry_cfg_get</span></a></p></td>
<td><p>是</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
<td><p>是</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm-factory-reset#dwm-factory-reset"><span class="std std-ref">dwm_factory_reset</span></a></p></td>
<td><p>是</p></td>
<td><p>是</p></td>
<td><p>是</p></td>
<td><p>是</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm-reset#dwm-reset"><span class="std std-ref">dwm_reset</span></a></p></td>
<td><p>是</p></td>
<td><p>是</p></td>
<td><p>是</p></td>
<td><p>是</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm-dev-info-get#dwm-dev-info-get"><span class="std std-ref">dwm_dev_info_get</span></a></p></td>
<td><p>是</p></td>
<td><p>是</p></td>
<td><p>是</p></td>
<td><p>是</p></td>
<td><p>M</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm-dev-status-get#dwm-dev-status-get"><span class="std std-ref">dwm_dev_status_get</span></a></p></td>
<td><p>是</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
<td><p>是</p></td>
<td><p>N</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm-uwb-cfg-set#dwm-uwb-cfg-set"><span class="std std-ref">dwm_uwb_cfg_set</span></a></p></td>
<td><p>是</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
<td><p>是</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm-uwb-cfg-get#dwm-uwb-cfg-get"><span class="std std-ref">dwm_uwb_cfg_get</span></a></p></td>
<td><p>是</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
<td><p>是</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm-usr-data-read#dwm-usr-data-read"><span class="std std-ref">dwm_usr_data_read</span></a></p></td>
<td><p>是</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
<td><p>是</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm-usr-data-write#dwm-usr-data-write"><span class="std std-ref">dwm_usr_data_write</span></a></p></td>
<td><p>是</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
<td><p>是</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm-label-read#dwm-label-read"><span class="std std-ref">dwm_label_read</span></a></p></td>
<td><p>是</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
<td><p>是</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm-label-write#dwm-label-write"><span class="std std-ref">dwm_label_write</span></a></p></td>
<td><p>是</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
<td><p>是</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm-status-get#dwm-status-get"><span class="std std-ref">dwm_status_get</span></a></p></td>
<td><p>是</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
<td><p>是</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm-gpio-cfg-output#dwm-gpio-cfg-output"><span class="std std-ref">dwm_gpio_cfg_output</span></a></p></td>
<td><p>是</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
<td><p>是</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm-gpio-value-set#dwm-gpio-value-set"><span class="std std-ref">dwm_gpio_value_set</span></a></p></td>
<td><p>是</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
<td><p>是</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm-gpio-value-get#dwm-gpio-value-get"><span class="std std-ref">dwm_gpio_value_get</span></a></p></td>
<td><p>是</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
<td><p>是</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm-gpio-value-get#dwm-gpio-value-get"><span class="std std-ref">dwm_gpio_value_get</span></a></p></td>
<td><p>是</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
<td><p>是</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm-gpio-value-toggle#dwm-gpio-value-toggle"><span class="std std-ref">dwm_gpio_value_toggle</span></a></p></td>
<td><p>是</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
<td><p>是</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm-node-id-get#dwm-node-id-get"><span class="std std-ref">dwm_node_id_get</span></a></p></td>
<td><p>是</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
<td><p>是</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm-panid-set#dwm-panid-set"><span class="std std-ref">dwm_panid_set</span></a></p></td>
<td><p>是</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
<td><p>是</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm-panid-get#dwm-panid-get"><span class="std std-ref">dwm_panid_get</span></a></p></td>
<td><p>是</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
<td><p>是</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm-status-get#dwm-status-get"><span class="std std-ref">dwm_status_get</span></a></p></td>
<td><p>是</p></td>
<td><p>是</p></td>
<td><p>是</p></td>
<td><p>是</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm-int-cfg-set#dwm-int-cfg-set"><span class="std std-ref">dwm_int_cfg_set</span></a></p></td>
<td><p>是</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
<td><p>是</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm-int-cfg-get#dwm-int-cfg-get"><span class="std std-ref">dwm_int_cfg_get</span></a></p></td>
<td><p>是</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
<td><p>是</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm_backhaul_xfer#dwm-backhaul-xfer"><span class="std std-ref">dwm_backhaul_xfer</span></a></p></td>
<td><p>是</p></td>
<td><p>否</p></td>
<td><p>否</p></td>
<td><p>否</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm_bh_status_get#dwm-bh-status-get"><span class="std std-ref">dwm_bh_status_get</span></a></p></td>
<td><p>是</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
<td><p>否</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm-enc-key-set#dwm-enc-key-set"><span class="std std-ref">dwm_enc_key_set</span></a></p></td>
<td><p>是</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
<td><p>是</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm-turn-off#dwm-turn-off"><span class="std std-ref">dwm_turn_off</span></a></p></td>
<td><p>是</p></td>
<td><p>是</p></td>
<td><p>是</p></td>
<td><p>是</p></td>
<td><p>N</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm-enc-key-clear#dwm-enc-key-clear"><span class="std std-ref">dwm_enc_key_clear</span></a></p></td>
<td><p>是</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
<td><p>是</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm-mac-addr-get#dwm-mac-addr-get"><span class="std std-ref">dwm_mac_addr_get</span></a></p></td>
<td><p>是</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
<td><p>是</p></td>
<td><p>N</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm-mac-addr-set-once#dwm-mac-addr-set-once"><span class="std std-ref">dwm_mac_addr_set_once</span></a></p></td>
<td><p>是</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
<td><p>是</p></td>
<td><p>N</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm-hw-ver-set-once#dwm-hw-ver-set-once"><span class="std std-ref">dwm_hw_ver_set_once</span></a></p></td>
<td><p>是</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
<td><p>否</p></td>
<td><p>N</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm-alarm-start#dwm-alarm-start"><span class="std std-ref">dwm_alarm_start</span></a></p></td>
<td><p>是</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
<td><p>是</p></td>
<td><p>N</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm-cert-update-start#dwm-cert-update-start"><span class="std std-ref">dwm_cert_update_start</span></a></p></td>
<td><p>否</p></td>
<td><p>否</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
<td><p>N</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm-cert-update-write#dwm-cert-update-write"><span class="std std-ref">dwm_cert_update_write</span></a></p></td>
<td><p>否</p></td>
<td><p>否</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
<td><p>N</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm-boot-cfg-set#dwm-boot-cfg-set"><span class="std std-ref">dwm_boot_cfg_set</span></a></p></td>
<td><p>否</p></td>
<td><p>否</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
<td><p>N</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm-boot-cfg-get#dwm-boot-cfg-get"><span class="std std-ref">dwm_boot_cfg_get</span></a></p></td>
<td><p>否</p></td>
<td><p>否</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
<td><p>N</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm-fw-update-start#dwm-fw-update-start"><span class="std std-ref">dwm_fw_update_start</span></a></p></td>
<td><p>否</p></td>
<td><p>否</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
<td><p>N</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm-fw-update-xfer#dwm-fw-update-xfer"><span class="std std-ref">dwm_fw_update_xfer</span></a></p></td>
<td><p>否</p></td>
<td><p>否</p></td>
<td><p>是</p></td>
<td><p>否</p></td>
<td><p>N</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm-i2c-write#dwm-i2c-write"><span class="std std-ref">dwm_i2c_write</span></a></p></td>
<td><p>否</p></td>
<td><p>否</p></td>
<td><p>否</p></td>
<td><p>是</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm-i2c-read#dwm-i2c-read"><span class="std std-ref">dwm_i2c_read</span></a></p></td>
<td><p>否</p></td>
<td><p>否</p></td>
<td><p>否</p></td>
<td><p>是</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm-evt-wait#dwm-evt-wait"><span class="std std-ref">dwm_evt_wait</span></a></p></td>
<td><p>否</p></td>
<td><p>否</p></td>
<td><p>否</p></td>
<td><p>是</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm-wake-up#dwm-wake-up"><span class="std std-ref">dwm_wake_up</span></a></p></td>
<td><p>否</p></td>
<td><p>否</p></td>
<td><p>否</p></td>
<td><p>是</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm-wake-up#dwm-wake-up"><span class="std std-ref">dwm_wake_up</span></a></p></td>
<td><p>否</p></td>
<td><p>否</p></td>
<td><p>否</p></td>
<td><p>是</p></td>
<td><ul class="simple">
<li></li>
</ul>
</td>
</tr>
</tbody>
</table>
<p>(*) N:新增，M:修改，-：与 PANS 2.0 相比没有变化</p>
<hr class="docutils">
<div class="toctree-wrapper compound">
</div>
<div class="section" id="backhaul-commands">
<h2>回程命令</h2>
<p>本节描述当 DWM 模块被配置为 “关接”（参见 API 调用 <a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm-cfg-anchor-set#dwm-cfg-anchor-set"><span class="std std-ref">dwm_cfg_anchor_set</span></a>）时，用于通过 SPI 接口定期传输数据的 API 命令。</p>
<div class="toctree-wrapper compound">
<ul>
<li class="toctree-l1"><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm_backhaul_xfer">dwm_backhaul_xfer</a></li>
<li class="toctree-l1"><a class="reference internal" href="/docs/zh/pans-pro-rtls/integration-guide/api-commands/dwm_bh_status_get">dwm_bh_status_get</a></li>
</ul>
</div>
</div>
</div>


           </div>
