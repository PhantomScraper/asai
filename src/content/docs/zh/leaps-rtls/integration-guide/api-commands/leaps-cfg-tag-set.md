---
title: "leaps_cfg_tag_set"
lang: zh
slug: "leaps-rtls/integration-guide/api-commands/leaps-cfg-tag-set"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/leaps-rtls/integration-guide/api-commands/leaps-cfg-tag-set/"
order: 149
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-cfg-tag-set">
<span id="id1"></span><h1>leaps_cfg_tag_set</h1>
<p>使用给定的选项将节点配置为标签。 如果未设置加密密钥，则无法启用加密。 此调用需要重置才能使新配置生效（leaps_reset）。 在设置新值的情况下，此调用会写入内部闪存，因此不应频繁使用，在最坏的情况下可能需要数百毫秒！</p>
<hr class="docutils">
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
输入</div>
<ul class="simple">
<li><p class="sd-card-text">stnry_en: 1-bit (<em>‘0’ | ‘1’  已启用固定检测，如果已启用，则在节点未移动时使用固定更新率而不是正常更新率</em>)</p></li>
<li><p class="sd-card-text">meas_mode: 2-bits (<em>‘0’ - TWR, 双向测距,  ‘1’ - TDOA,  到达时间差, ‘2’, ‘3’ - 保留</em>)</p></li>
<li><p class="sd-card-text">low_power_en:1位（<em>’0’|’1’低功耗模式启用</em>）</p></li>
<li><p class="sd-card-text">loc_engine_en: 1-bit (<em>‘0’ | ‘1’ 表示不使用内部位置引擎，1表示内部位置引擎</em>)</p></li>
<li><p class="sd-card-text">enc_en: 1-bit (<em>‘0’ | ‘1’ 加密启用</em>)</p></li>
<li><p class="sd-card-text">led_en: 1-bit (<em>‘0’ | ‘1’ 通用LED启用</em>)</p></li>
<li><p class="sd-card-text">ble_en: 1-bit (<em>‘0’ | ‘1’ BLE 启用</em>)</p></li>
<li><p class="sd-card-text">uwb_mode: 2-bits (<em>‘0’ | ‘1’ | ‘2’ 0-关, 1-被动, 2-主动</em>)</p></li>
<li><p class="sd-card-text">fw_update_en: 1-bit (<em>‘0’ | ‘1’ 固件更新启用</em>)</p></li>
<li><p class="sd-card-text">profile_id: 3位无符号整数(<em>配置文件的ID</em>)</p></li>
<li><p class="sd-card-text">uwb_act_ble: 1位无符号整数(<em>通过BLE激活UWB</em>)</p></li>
</ul>
</div>
</div>
</div>
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
输出</div>
<ul class="simple">
<li><p class="sd-card-text"><a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/leaps-api/api-generic-data-types#statuscode"><span class="std std-ref">状态码</span></a></p></li>
</ul>
</div>
</div>
</div>
</div>
</div>
<hr class="docutils">
<p><strong>示例</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 11%">
<col style="width: 9%">
<col style="width: 32%">
<col style="width: 31%">
<col style="width: 16%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="5"><p>TLV 响应</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="2"><p>类型</p></td>
<td rowspan="2"><p>长度</p></td>
<td colspan="3"><p>价值</p></td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line">(7位) low_power_en</div>
<div class="line">(6位) loc_engine_en</div>
<div class="line">(5位) enc_en</div>
<div class="line">(4位) led_en</div>
<div class="line">(3位) ble_en</div>
<div class="line">(2位) fw_update_en</div>
<div class="line">(bits 0-1) uwb_mode</div>
</div>
</td>
<td><div class="line-block">
<div class="line">(bits 4-7) reserved</div>
<div class="line">(bit 3) uwb_act_ble</div>
<div class="line">(2 位) stnry_en</div>
<div class="line">(bits 0-1) meas_mode</div>
</div>
</td>
<td><p>(bits 0-2) 配置文件id</p></td>
</tr>
<tr class="row-even"><td><p>0x05</p></td>
<td><p>0x03</p></td>
<td><p>0x72</p></td>
<td><p>0x04</p></td>
<td><p>0x05</p></td>
</tr>
</tbody>
</table>
<p>类型0x05表示命令leaps_cfg_tag_set</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 34%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV 响应</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>类型</p></td>
<td><p>长度</p></td>
<td><p>价值</p></td>
</tr>
<tr class="row-odd"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>类型 0x40 表示状态代码</p>
</div>


           </div>
