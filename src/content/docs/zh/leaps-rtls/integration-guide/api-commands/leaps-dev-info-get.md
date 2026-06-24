---
title: "leaps_dev_info_get"
lang: zh
slug: "leaps-rtls/integration-guide/api-commands/leaps-dev-info-get"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/leaps-rtls/integration-guide/api-commands/leaps-dev-info-get/"
order: 233
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-dev-info-get">
<span id="id1"></span><h1>leaps_dev_info_get</h1>
<p>获取有关模块固件和硬件的信息。</p>
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
<li><p class="sd-card-text">fw_id: 32位整数(<em>固件id. 可能的值为BLDR的“0”, ELDR-扩展加载器的“1”或主固件的“2”. 主固件是默认值. ELDR是主固件和服务器的有限版本，主要在固件更新期间作为备份. 并非所有硬件都支持ELDR.</em>)</p></li>
<li><p class="sd-card-text">bldr_version: 32位整数(<em>maj, min, patch, res, var</em>)</p></li>
<li><p class="sd-card-text">eldr_version: 32位整数(<em>maj，min，patch，res，var，值0xFFFFFFFF表示硬件不支持eldr</em>)</p></li>
<li><p class="sd-card-text">fw_version: 32位整数(<em>maj, min, patch, res, var</em>)</p></li>
<li><p class="sd-card-text">bldr_checksum: 32位整数</p></li>
<li><p class="sd-card-text">eldr_checksum: 32位整数(<em>价值0xFFFFFFFF 表示硬件不支持ELDR</em>)</p></li>
<li><p class="sd-card-text">fw_checksum: 32位整数</p></li>
<li><p class="sd-card-text">cfg_version: 32位整数</p></li>
<li><p class="sd-card-text">hw_version: 32位整数</p></li>
</ul>
</div>
</div>
</div>
</div>
</div>
<hr class="docutils">
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 20%">
<col style="width: 18%">
<col style="width: 18%">
<col style="width: 22%">
<col style="width: 22%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="5"><p>固件版本编码</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>maj = bits
24 - 31</p>
<p>(MAJOR)</p>
</td>
<td><p>min = bits
16 - 23</p>
<p>(MINOR)</p>
</td>
<td><p>patch = bits
8 - 15</p>
<p>(补丁)</p>
</td>
<td><p>res = bits
4 - 7</p>
<p>(保留)</p>
</td>
<td><p>var = bits
0 - 3</p>
<p>(VARIANT)</p>
</td>
</tr>
</tbody>
</table>
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
<tr class="row-odd"><td><p>0x15</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>类型0x15表示命令leaps_dev_info_get</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 11%">
<col style="width: 8%">
<col style="width: 7%">
<col style="width: 6%">
<col style="width: 8%">
<col style="width: 8%">
<col style="width: 24%">
<col style="width: 14%">
<col style="width: 13%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="9"><p>TLV 响应</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="2"><p>类型</p></td>
<td rowspan="2"><p>长度</p></td>
<td rowspan="2"><p>价值</p></td>
<td rowspan="2"><p>类型</p></td>
<td rowspan="2"><p>长度</p></td>
<td colspan="4"><p>价值</p></td>
</tr>
<tr class="row-odd"><td><p>fw_id</p></td>
<td><p>bldr_version
eldr_version
fw_version
bldr_checksum
eldr_checksum
fw_checksum</p></td>
<td><p>cfg_version</p></td>
<td><p>hw_version</p></td>
</tr>
<tr class="row-even"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
<td><p>0x50</p></td>
<td><p>0x24</p></td>
<td><p>0x00
0x00
0x00
0x01</p></td>
<td><p>0x00 0x00 0x03 0x01
0xff 0xff 0xff 0xff
0x01 0x00 0x03 0x01
0xd2 0x81 0x9d 0x59
0xff 0xff 0xff 0xff
0xa7 0x34 0x01 0xcd</p></td>
<td><p>0x00
0x07
0x01
0x00</p></td>
<td><p>0x00
0x01
0x41
0xDE</p></td>
</tr>
</tbody>
</table>
<p>类型 0x40 表示状态代码</p>
<p>类型0x50表示设备信息</p>
</div>


           </div>
