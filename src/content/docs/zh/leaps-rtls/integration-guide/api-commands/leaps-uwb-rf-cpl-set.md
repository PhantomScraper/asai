---
title: "leaps_uwb_rf_cpl_set"
lang: zh
slug: "leaps-rtls/integration-guide/api-commands/leaps-uwb-rf-cpl-set"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/leaps-rtls/integration-guide/api-commands/leaps-uwb-rf-cpl-set/"
order: 272
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-uwb-rf-cpl-set">
<span id="id1"></span><h1>leaps_uwb_rf_cpl_set</h1>
<p>与 UWB 信道一起设置 UWB 射频合规性. 如果使用 <a class="reference external" href="#leaps_uwb_cfg_set">leaps_uwb_cfg_set</a> 设置了 UWB 配置参数（如 Tx 功率等），则 UWB 射频符合性会自动设置为 “自定义”. 配置生效需要重置. 配置存储在非易失性存储器中. 并非所有板卡都支持所有通道. 仅 UWB 频道 9 支持 ARIB 射频合规性。</p>
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
输入</div>
<ul class="simple">
<li><p class="sd-card-text">uwb_channel: ‘2’ | ‘3’ | ‘5’ | ‘9’ (<em>UWB 信道 2, 3, 5 仅支持 DW1000 板，UWB 信道 5, 9 仅支持 DW3000 板</em>)</p></li>
<li><p class="sd-card-text">rf_compliance: ‘0’ | ‘1’ | ‘2’ (<em>RF 合规选项, 0 = FCC/ETSI, 1 = ETSI + 10dB, 2 = ARIB</em>)</p></li>
<li><p class="sd-card-text">pcode: ‘9’ | ‘10’ | ‘11’ | ‘12’ (<em>Tx/Rx 前置码，这是可选项。 如果用户不输入，则使用下面指定的默认值。</em>)</p>
<ul>
<li><p class="sd-card-text">Channel 2: Tx/Rx Preamble Code = 11</p></li>
<li><p class="sd-card-text">Channel 3: Tx/Rx Preamble Code = 12</p></li>
<li><p class="sd-card-text">Channel 5: Tx/Rx Preamble Code = 9</p></li>
<li><p class="sd-card-text">Channel 9: Tx/Rx Preamble Code = 11</p></li>
</ul>
</li>
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
<div class="admonition note">
<p class="admonition-title">注解</p>
<ul class="simple">
<li><p>通道 2 和通道 3 仅支持 ‘0 = FCC/ETSI’</p></li>
<li><p>只有频道9支持ARIB。</p></li>
</ul>
</div>
<hr class="docutils">
<p><strong>示例</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 15%">
<col style="width: 15%">
<col style="width: 70%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV 请求</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="2"><p>类型</p></td>
<td rowspan="2"><p>长度</p></td>
<td><p>价值</p></td>
</tr>
<tr class="row-odd"><td><p>字节 0:</p>
<blockquote>
<div><ul class="simple">
<li><p>Bits [7:4]: rf_compliance</p></li>
<li><p>Bits [3:0]: uwb_channel</p></li>
</ul>
</div></blockquote>
<p>byte 1: pcode</p>
</td>
</tr>
<tr class="row-even"><td><p>0x8A</p></td>
<td><p>0x02</p></td>
<td><p>0x29 0x0B</p></td>
</tr>
</tbody>
</table>
<p>类型 0x8A（138 dec）表示命令 <a class="reference internal" href="#leaps-uwb-rf-cpl-set"><span class="std std-ref">leaps_uwb_rf_cpl_set</span></a></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 34%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV回复</p></th>
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
</div>


           </div>
