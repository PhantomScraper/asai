---
title: "leaps_cfg_get"
lang: zh
slug: "leaps-rtls/integration-guide/api-commands/leaps-cfg-get"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/leaps-rtls/integration-guide/api-commands/leaps-cfg-get/"
order: 152
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-cfg-get">
<span id="id1"></span><h1>leaps_cfg_get</h1>
<p>获取节点的当前配置选项。</p>
<hr class="docutils">
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
输入</div>
<ul class="simple">
<li><p class="sd-card-text">(<em>无</em>)</p></li>
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
<li><p class="sd-card-text">initiator: 1-bit (<em>‘0’ | ‘1’ - 启动器角色启用</em>)</p></li>
<li><p class="sd-card-text">gateway: 1-bit (<em>‘0’ | ‘1’ - 网关角色启用</em>)</p></li>
<li><p class="sd-card-text">enc_en: 1-bit (<em>‘0’ | ‘1’ - 启用加密</em>)</p></li>
<li><p class="sd-card-text">led_en: 1-bit (<em>‘0’ | ‘1’ - 通用 LED启用</em>)</p></li>
<li><p class="sd-card-text">ble_en: 1-bit (<em>‘0’ | ‘1’ - 启用BLE</em>)</p></li>
<li><p class="sd-card-text">uwb_mode: 2-bits (<em>0-关, 1-被动, 2-主动</em>)</p></li>
<li><p class="sd-card-text">fw_update_en: 1-bit (<em>‘0’ | ‘1’- 固件更新启用</em>)</p></li>
<li><p class="sd-card-text">stnry_en: 1-bit (<em>‘0’ | ‘1’  已启用固定检测，如果已启用，则在节点未移动时使用固定更新率而不是正常更新率</em>)</p></li>
<li><p class="sd-card-text">meas_mode: 2位(<em>‘0’ | ‘1’ | ‘2’ | ‘3’ , 0 - 双向测距, 1 - UL-TDoA, 2 - DL-TDoA, 3 - 保留</em>)</p></li>
<li><p class="sd-card-text">low_power_en:1位（<em>’0’|’1’低功耗模式启用</em>）</p></li>
<li><p class="sd-card-text">loc_engine_en: 1-bit (<em>‘0’ | ‘1’ 表示不使用内部位置引擎，1表示内部位置引擎</em>)</p></li>
<li><p class="sd-card-text">profile_id: 3-bits (<em>配置文件的ID</em>)</p></li>
<li><p class="sd-card-text">clock_reference: 1-bit (<em>在节点上启用时钟参考</em>)</p></li>
<li><p class="sd-card-text">uwb_act_ble:1 位（<em>节点上的 uwb 激活超过 ble 状态</em>）</p></li>
</ul>
</div>
</div>
</div>
</div>
</div>
<hr class="docutils">
<blockquote>
<div><div class="admonition note">
<p class="admonition-title">注解</p>
<p><strong>uwb_bh_routing</strong>: 仅在固件编译了 UWB 路由回程时可用：</p>
<p>价值: ‘0’ | ‘1’ | ‘2’:</p>
<ul class="simple">
<li><p>0- 关 - 锚点不会成为路由锚点</p></li>
<li><p>1- 开 - 路由算法会优先选择锚点作为路由锚点</p></li>
<li><p>2- 自动- 锚点是否成为路由锚点，完全取决于路由算法</p></li>
</ul>
</div>
</div></blockquote>
<hr class="docutils">
<p><strong>示例</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 53%">
<col style="width: 47%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="2"><p>TLV 请求</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>类型</p></td>
<td><p>长度</p></td>
</tr>
<tr class="row-odd"><td><p>0x08</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>类型0x08表示命令leaps_cfg_get</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 5%">
<col style="width: 6%">
<col style="width: 5%">
<col style="width: 4%">
<col style="width: 6%">
<col style="width: 20%">
<col style="width: 30%">
<col style="width: 26%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="8"><p>TLV 响应</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="2"><p>类型</p></td>
<td rowspan="2"><p>长度</p></td>
<td rowspan="2"><p>价值</p></td>
<td rowspan="2"><p>类型</p></td>
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
<div class="line">(bits 0-1) uwb_mode:</div>
<div class="line">0 - 脱机,</div>
<div class="line">1 - 被动,</div>
<div class="line">2 - 有效</div>
</div>
</td>
<td><div class="line-block">
<div class="line">(bits 6-7) uwb_bh_routing:</div>
<div class="line">0 - 关,</div>
<div class="line">1 – 开,</div>
<div class="line">2 - 自动</div>
<div class="line">(bit 5) 模式:</div>
<div class="line">0 - 标记</div>
<div class="line">1 - 锚点</div>
<div class="line">(bit 4) 启动程序</div>
<div class="line">(bit 3) 关接</div>
<div class="line">(2 位) stnry_en</div>
<div class="line">(bits 0-1) meas_mode:</div>
<div class="line">0 - TWR,</div>
<div class="line">1 - UL-TDoA</div>
<div class="line">2 - DL-TDoA</div>
<div class="line">3保留</div>
</div>
</td>
<td><div class="line-block">
<div class="line">(bits 0-2) 配置文件id</div>
<div class="line">(bit 3) 时钟基准</div>
<div class="line">(bit 4) uwb_act_ble</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
<td><p>0x46</p></td>
<td><p>0x03</p></td>
<td><p>0x1C</p></td>
<td><p>0x20</p></td>
<td><p>0x02</p></td>
</tr>
</tbody>
</table>
<p>类型 0x40 表示状态代码</p>
<p>类型0x46表示节点配置</p>
</div>


           </div>
