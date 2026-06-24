---
title: "leaps_uwb_profile_get"
lang: zh
slug: "leaps-rtls/integration-guide/api-commands/leaps-uwb-profile-get"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/leaps-rtls/integration-guide/api-commands/leaps-uwb-profile-get/"
order: 275
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-uwb-profile-get">
<span id="id1"></span><h1>leaps_uwb_profile_get</h1>
<p>读取当前激活的 UWB 配置文件的信息。 如果因为没有 UWB 连接而无法读取信息，则返回 “不允许”。</p>
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
<li><p class="sd-card-text"><a class="reference internal" href="/docs/zh/leaps-rtls/integration-guide/leaps-api/api-generic-data-types#statuscode"><span class="std std-ref">状态码</span></a></p></li>
<li><p class="sd-card-text">sf_period_us: 32 位无符号整数（<em>超帧周期，微秒</em>）</p></li>
<li><p class="sd-card-text">slot_period_us: 16 位无符号整数 (<em>插槽周期，以微秒为单位</em>)</p></li>
<li><p class="sd-card-text">sf_num_max: 16 位无符号整数 (<em>超帧数最大值</em>)</p></li>
<li><p class="sd-card-text">anchor_upd_rate: 16 位无符号整数（<em>超帧周期乘以锚点的更新率</em>）</p></li>
<li><p class="sd-card-text">active_profile_id: ‘1’|’2’|’3’|’4’|’5’|’6’ (<em>当前配置文件 ID/编号，数值 0 表示自动配置文件</em>）。</p></li>
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
<col style="width: 52%">
<col style="width: 48%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="2"><p>TLV 请求</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>类型</p></td>
<td><p>长度</p></td>
</tr>
<tr class="row-odd"><td><p>0x1F</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>键入0x1F（12月31日）表示命令leaps_uwb_profile_get</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 4%">
<col style="width: 6%">
<col style="width: 5%">
<col style="width: 4%">
<col style="width: 6%">
<col style="width: 15%">
<col style="width: 14%">
<col style="width: 14%">
<col style="width: 13%">
<col style="width: 11%">
<col style="width: 8%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="11"><p>TLV 响应</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="2"><p>类型</p></td>
<td rowspan="2"><p>长度</p></td>
<td rowspan="2"><p>价值</p></td>
<td rowspan="2"><p>类型</p></td>
<td rowspan="2"><p>长度</p></td>
<td colspan="6"><p>价值</p></td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line">(字节0-3)</div>
<div class="line">超帧周期</div>
<div class="line">以微秒为单位</div>
</div>
</td>
<td><div class="line-block">
<div class="line">(字节4-5)</div>
<div class="line">插槽周期</div>
<div class="line">微秒</div>
</div>
</td>
<td><div class="line-block">
<div class="line">(字节6-7)</div>
<div class="line">超帧</div>
<div class="line">最大数量</div>
</div>
</td>
<td><div class="line-block">
<div class="line">(字节8-9)</div>
<div class="line">锚点更新</div>
<div class="line">费率</div>
</div>
</td>
<td><div class="line-block">
<div class="line">(字节10)</div>
<div class="line">活动</div>
<div class="line">配置文件ID</div>
</div>
</td>
<td><p>(字节11)保留</p></td>
</tr>
<tr class="row-even"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
<td><p>0x5B</p></td>
<td><p>0x0C</p></td>
<td><p>0xA0 0x86
0x01 0x00</p></td>
<td><p>0xF4
0x01</p></td>
<td><p>0xa0
0x05</p></td>
<td><p>0x1E
0x00</p></td>
<td><p>0x02</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>类型0x5B(91 dec)表示UWB配置文件信息</p>
</div>


           </div>
