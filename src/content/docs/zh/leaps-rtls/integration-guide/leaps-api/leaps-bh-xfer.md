---
title: "leaps_bh_xfer"
lang: zh
slug: "leaps-rtls/integration-guide/leaps-api/leaps-bh-xfer"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/leaps-rtls/integration-guide/leaps-api/leaps-bh-xfer/"
order: 148
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-bh-xfer">
<span id="id1"></span><h1>leaps_bh_xfer</h1>
<p>写入下行链路数据并读取上行链路数据块。 模块必须配置为关接节点。</p>
<p>通过 SPI 接口传输上行和下行数据时，上行和下行数据都被编码为 tlv 帧，如 <a class="reference external" href="#example-interrupt-leaps_bh_xfer">SPI上的多TVL</a> 所述。</p>
<p>SPI 主站通过 <strong>downlink_byte_cnt</strong> 告诉从站要传输多少个下行链路字节。 从站在第一次 SPI 传输中读取 <strong>下行链路字节数</strong>。 从站在读取下行链路数据时，已经准备好了一些上行链路数据，它希望将这些数据传输给主站。 要同时从主站向从站传输下行链路数据和从站向主站传输上行链路数据，从站必须计算出需要多少字节和多少次 SPI 传输。 主站在第二次 SPI 传输中读取字节数和传输数，详见 <a class="reference external" href="#example-interrupt-leaps_bh_xfer">通过 SPI 传输多个 TVL</a>。 最后，执行传输，并传输上行链路和下行链路。 目前支持的最大传输次数为 5 次，最大有效载荷为 253 字节，即 255 -（TLV 标头）的大小。 一次调用 leaps_bh_xfer 最多支持 5 个上行链路帧和 2 个下行链路帧。</p>
<hr class="docutils">
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-2 sd-row-cols-xs-2 sd-row-cols-sm-2 sd-row-cols-md-2 sd-row-cols-lg-2 docutils">
<div class="sd-col sd-d-flex-row sd-col-11 sd-col-xs-11 sd-col-sm-11 sd-col-md-11 sd-col-lg-11 sd-m-2 docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm docutils">
<div class="sd-card-body docutils">
<div class="sd-card-title sd-font-weight-bold docutils">
输入</div>
<ul class="simple">
<li><p class="sd-card-text">downlink_byte_cnt: 16 位无符号整数（<em>不含 TLV 头的下行链路数据字节数，最多 506 字节</em>）</p></li>
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
<li><p class="sd-card-text">downlink_chunk:最多 253 字节（<em>作为下行链路发送到从属设备的不透明数据</em>）</p></li>
<li><p class="sd-card-text">output: 5 <em>[上行链路_chunk]</em>。</p></li>
<li><p class="sd-card-text">uplink_chunk: 最多 253 字节 (<em>不透明数据作为上行链路发送到主站</em>)</p></li>
</ul>
</div>
</div>
</div>
</div>
</div>
<hr class="docutils">
<p><strong>UART 示例</strong></p>
<p>UART 接口不可用。</p>
<p><strong>SPI示例（关接除外）</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 15%">
<col style="width: 13%">
<col style="width: 72%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV 请求</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>类型</p></td>
<td><p>长度</p></td>
<td><p>价值</p>
<p>downlink_byte_cnt = 下行数据大小 (244 字节)</p>
</td>
</tr>
<tr class="row-odd"><td><p>0x37</p></td>
<td><p>0x02</p></td>
<td><p>0xF4 0x00</p></td>
</tr>
</tbody>
</table>
<div class="line-block">
<div class="line">0x37 表示命令 leaps_bh_xfer</div>
</div>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 34%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>TLV 响应</p></th>
<th class="head"></th>
<th class="head"></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>类型</p></td>
<td><p>长度</p></td>
<td><p>价值</p></td>
</tr>
<tr class="row-odd"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x02</p></td>
</tr>
</tbody>
</table>
<p><strong>SPI 示例关</strong></p>
<div class="line-block">
<div class="line">下行链路字节数:244</div>
<div class="line">上行链路字节数:980</div>
</div>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 15%">
<col style="width: 13%">
<col style="width: 72%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV 请求</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>类型</p></td>
<td><p>长度</p></td>
<td><p>值downlink_byte_cnt = 下行链路数据的大小 (244 字节)</p></td>
</tr>
<tr class="row-odd"><td><p>0x37</p></td>
<td><p>0x02</p></td>
<td><p>0xF4 0x00</p></td>
</tr>
</tbody>
</table>
<div class="line-block">
<div class="line">0x37 表示命令 leaps_bh_xfer</div>
</div>
<p>此调用具有可变的连续传输次数，它遵循 TLV 请求，请参阅 “API over SPI 接口描述 &lt;#example-interrupt-leaps_bh_xfer&gt;”</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 48%">
<col style="width: 15%">
<col style="width: 37%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV 下行链路编号1,2, 3,4,5</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>类型</p></td>
<td><p>长度 (244 字节)</p></td>
<td><p>价值</p></td>
</tr>
<tr class="row-odd"><td><p>0x64</p></td>
<td><p>0xF4
(244)</p></td>
<td><p>下行链路数据块 nr.1</p></td>
</tr>
<tr class="row-even"><td><p>0x65</p></td>
<td><p>0x00</p></td>
<td><p>空</p></td>
</tr>
<tr class="row-odd"><td><p>0x66</p></td>
<td><p>0x00</p></td>
<td><p>空</p></td>
</tr>
<tr class="row-even"><td><p>0x67</p></td>
<td><p>0x00</p></td>
<td><p>空</p></td>
</tr>
<tr class="row-odd"><td><p>0x68</p></td>
<td><p>0x00</p></td>
<td><p>空</p></td>
</tr>
</tbody>
</table>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 48%">
<col style="width: 15%">
<col style="width: 37%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV上行链路编号1,2,3,4,5</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>类型</p></td>
<td><p>长度（980 字节）</p></td>
<td><p>价值</p></td>
</tr>
<tr class="row-odd"><td><p>0x6E</p></td>
<td><p>0xFD
(253)</p></td>
<td><p>上行链路数据块 1</p></td>
</tr>
<tr class="row-even"><td><p>0x6F</p></td>
<td><p>0xFD</p></td>
<td><p>上行链路数据块nr.2</p></td>
</tr>
<tr class="row-odd"><td><p>0x70</p></td>
<td><p>0xFD</p></td>
<td><p>上行链路数据块 nr.3</p></td>
</tr>
<tr class="row-even"><td><p>0x71</p></td>
<td><p>0xDD
(221)</p></td>
<td><p>上行链路数据块 nr.4</p></td>
</tr>
<tr class="row-odd"><td><p>0x72</p></td>
<td><p>0x00</p></td>
<td><p>空</p></td>
</tr>
</tbody>
</table>
<div class="line-block">
<div class="line">类型0x64表示下行链路数据块nr.1</div>
<div class="line">类型0x65表示下行链路数据块nr.2</div>
<div class="line">…</div>
<div class="line">类型 0x68 表示下行链路数据块nr.5</div>
<div class="line">类型0x6E表示上行链路数据块nr.1</div>
<div class="line">类型0x6F表示上行链路数据块nr.2</div>
<div class="line">…</div>
<div class="line">类型0x72表示上行链路数据块nr.5</div>
</div>
</div>
<div class="section" id="bh-transfer-over-usb">
<h1>通过USB进行BH传输</h1>
<p>通过 USB 传输 BH 数据与通过 SPI 传输不同. SPI 数据传输以中断为基础，但 LEAPS RTLS 设备与 PC 之间的 USB 连接无法使用中断线路，因此在 USB 接口上，LEAPS RTLS 设备将主动发送通知（TLV_TYPE_NOTIF_STATUS, TLV_TYPE_NOTIF_BH_STATUS）和上行数据块给网关主控（PC），而不是使用 TLV_TYPE_CMD_BH_XFER TLV 命令的请求-响应方式. 通知和上行链路数据可以启用/禁用，类似于使用 <a class="reference external" href="#leaps_int_cfg_set">leaps_int_cfg_set</a> 的中断。</p>
</div>


           </div>
