---
title: "leaps_cfg_anchor_set"
lang: zh
slug: "leaps-rtls/integration-guide/api-commands/leaps-cfg-anchor-set"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/leaps-rtls/integration-guide/api-commands/leaps-cfg-anchor-set/"
order: 224
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-cfg-anchor-set">
<span id="id1"></span><h1>leaps_cfg_anchor_set</h1>
<p>使用给定的选项将节点配置为锚点。 如果未设置加密密钥，则无法启用加密。 此调用需要重置才能使新配置生效(<a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/api-commands/leaps-reset#leaps-reset"><span class="std std-ref">leaps_reset</span></a>)。 在启动器上启用加密将导致自动启用具有相同加密密钥集(<a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/api-commands/leaps-enc-key-set#leaps-enc-key-set"><span class="std std-ref">leaps_enc_key_set</span></a>)的所有节点的加密。 这允许从一个地方远程对具有相同泛ID（网络ID）和相同加密密钥的整个网络进行加密。</p>
<p>在设置新值的情况下，此调用会写入内部闪存，因此不应频繁使用，在最坏的情况下可能需要数百毫秒！</p>
<hr class="docutils">
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
输入</div>
<ul class="simple">
<li><p class="sd-card-text">initiator: 1-bit (<em>‘0’ | ‘1’ - 启动器角色启用</em>)</p></li>
<li><p class="sd-card-text">gateway: 1-bit (<em>‘0’ | ‘1’ - 网关角色启用</em>)</p></li>
<li><p class="sd-card-text">enc_en: 1-bit (<em>‘0’ | ‘1’ - 启用加密</em>)</p></li>
<li><p class="sd-card-text">led_en: 1-bit (<em>‘0’ | ‘1’ - 通用 LED启用</em>)</p></li>
<li><p class="sd-card-text">ble_en: 1-bit (<em>‘0’ | ‘1’ - 启用BLE</em>)</p></li>
<li><p class="sd-card-text">uwb_mode: 2-bits (<em>0-关, 1-被动, 2-主动</em>)</p></li>
<li><p class="sd-card-text">fw_update_en: 1-bit (<em>‘0’ | ‘1’- 固件更新启用</em>)</p></li>
<li><p class="sd-card-text">profile_id: 3-bits (<em>配置文件的ID</em>)</p></li>
<li><p class="sd-card-text">clock_reference: 1-bit (<em>在节点上启用时钟参考</em>)</p></li>
<li><p class="sd-card-text">uwb_act_ble: 1-bit (<em>在节点上通过ble启用uwb激活</em>)</p></li>
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
<blockquote>
<div><div class="admonition note">
<p class="admonition-title">注解</p>
<p><strong>uwb_bh_routing</strong>: 仅在固件编译了 UWB 路由回程时可用：</p>
<p>Value : ‘0’ | ‘1’ | ‘2’</p>
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
<col style="width: 13%">
<col style="width: 8%">
<col style="width: 23%">
<col style="width: 28%">
<col style="width: 29%">
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
<div class="line">(bit 7) 启动器</div>
<div class="line">(bit 6) gateway</div>
<div class="line">(5位) enc_en</div>
<div class="line">(4位) led_en</div>
<div class="line">(3位) ble_en</div>
<div class="line">(2位) fw_update_en</div>
<div class="line">(bits 0-1) uwb_mode</div>
</div>
</td>
<td><div class="line-block">
<div class="line">(bits 2-7) 保留</div>
<div class="line">(bits 0-1) uwb_bh_routing:</div>
<div class="line">0 – 关</div>
<div class="line">1 – 开</div>
<div class="line">2 – 自动</div>
</div>
</td>
<td><div class="line-block">
<div class="line">(bits 0-2) 配置文件id</div>
<div class="line">(bit 3) 时钟基准</div>
<div class="line">(bit 4) uwb激活 ble</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>0x07</p></td>
<td><p>0x03</p></td>
<td><p>0x9C</p></td>
<td><p>0x02</p></td>
<td><p>0x02</p></td>
</tr>
</tbody>
</table>
<p>类型 0x07 表示命令 leaps_cfg_anchor_set</p>
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
