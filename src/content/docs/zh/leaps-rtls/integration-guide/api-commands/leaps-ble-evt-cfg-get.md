---
title: "leaps_ble_evt_cfg_get"
lang: zh
slug: "leaps-rtls/integration-guide/api-commands/leaps-ble-evt-cfg-get"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/leaps-rtls/integration-guide/api-commands/leaps-ble-evt-cfg-get/"
order: 249
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-ble-evt-cfg-get">
<span id="id1"></span><h1>leaps_ble_evt_cfg_get</h1>
<p>读取BLE事件的当前配置。</p>
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
<tr class="row-odd"><td><p>0x22</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>类型 0x22 (34) 表示命令 leaps_ble_evt_cfg_get</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 14%">
<col style="width: 10%">
<col style="width: 10%">
<col style="width: 10%">
<col style="width: 10%">
<col style="width: 47%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="6"><p>TLV 响应</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="2"><p>类型</p></td>
<td rowspan="2"><p>长度</p></td>
<td rowspan="2"><p>价值</p></td>
<td rowspan="2"><p>类型</p></td>
<td rowspan="2"><p>长度</p></td>
<td><p>价值</p></td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line">(bits 1 0-15)保留</div>
<div class="line">(bit 9) 位置就绪事件包括测距节点的位置</div>
<div class="line">(bit 8) 位置就绪事件包括我的位置</div>
<div class="line">(3-7 位)保留</div>
<div class="line">(bit 2) BLE用户数据就绪事件启用</div>
<div class="line">(bit 1)代理位置就绪事件已启用</div>
<div class="line">(bit 0) 位置就绪事件已启用</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
<td><p>0x5E</p></td>
<td><p>0x02</p></td>
<td><p>0x02
0x01</p></td>
</tr>
</tbody>
</table>
<p>类型 0x40 表示状态代码</p>
<p>类型 0x5E (94) 表示 BLE 事件配置</p>
</div>


           </div>
