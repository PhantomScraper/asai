---
title: "leaps_ble_evt_cfg_set"
lang: zh
slug: "leaps-rtls/integration-guide/api-commands/leaps-ble-evt-cfg-set"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/leaps-rtls/integration-guide/api-commands/leaps-ble-evt-cfg-set/"
order: 223
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-ble-evt-cfg-set">
<span id="id1"></span><h1>leaps_ble_evt_cfg_set</h1>
<p>启用/禁用BLE接口上的事件。 在设置新值的情况下，此调用会写入内部非易失性存储器，因此不应频繁使用，在最坏的情况下可能需要数百毫秒！</p>
<hr class="docutils">
<p><strong>示例</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 11%">
<col style="width: 11%">
<col style="width: 78%">
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
<tr class="row-odd"><td><div class="line-block">
<div class="line">(bits 10-15) 保留</div>
<div class="line">(bit 9) 位置就绪事件包括测距节点的位置</div>
<div class="line">(bit 8) 位置就绪事件包括我的位置</div>
<div class="line">(3-7 位)保留</div>
<div class="line">(bit 2) BLE用户数据就绪事件启用</div>
<div class="line">(bit 1)代理位置就绪事件已启用</div>
<div class="line">(bit 0) 位置就绪事件已启用</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>0x21</p></td>
<td><p>0x02</p></td>
<td><p>0x02 0x01</p></td>
</tr>
</tbody>
</table>
<p>类型0x21 (33)表示命令 leaps_ble_evt_cfg_set</p>
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
