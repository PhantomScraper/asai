---
title: "dwm_backhaul_xfer"
lang: zh
slug: "pans-pro-rtls/integration-guide/api-commands/dwm_backhaul_xfer"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/pans-pro-rtls/integration-guide/api-commands/dwm_backhaul_xfer/"
order: 222
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-backhaul-xfer">
<span id="id1"></span><h1>dwm_backhaul_xfer</h1>
<p>写入下行链路数据并读取上行链路数据块。 DWM 模块必须配置为网关。 上行链路数据和下行链路数据被编码为 TLV 帧，并通过 SPI 接口进行传输，如上文所述。 SPI 主站通过 <strong>downlink_byte_cnt</strong> 告诉从站要传输多少个下行链路字节。 从站在第一次 SPI 传输中读取 <strong>downlink_byte_cnt</strong>。 从站在读取下行链路数据时，已经准备好向主站传输一些上行链路数据。 要同时从主站向从站传输下行链路数据和从站向主站传输上行链路数据，从站必须计算出需要多少字节和 SPI 传输量。 主站在第二次 SPI 传输中读取字节数和传输数。 最后，执行传输，同时传输上行链路和下行链路。 目前支持的最大传输次数为 5 次，最大有效载荷为 253 字节，即 255 -（TLV 标头的大小）。 一次调用 <a class="reference internal" href="#dwm-backhaul-xfer"><span class="std std-ref">dwm_backhaul_xfer</span></a> 最多支持 5 个上行帧和 2 个下行帧。</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_backhaul_xfer">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_backhaul_xfer</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">uint16_t</span></span>, <span class="n"><span class="pre">uint8_t</span></span><span class="p"><span class="pre">*</span></span><span class="sig-paren">)</span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">参数</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>input</strong> – downlink_byte_cnt, {downlink_chunk}</p></li>
<li><p><strong>downlink_byte_cnt</strong> – 16 位无符号整数(<em>不含 TLV 标头的下行链路数据字节数，最大 506 字节</em>)</p></li>
<li><p><strong>downlink_chunk</strong> – 最大 253 字节（<em>作为下行链路发送到从属设备的不透明数据，最多 2 个数据块</em>）</p></li>
<li><p><strong>output</strong> – {uplink_chunk} (<em>最多 5 个上行链路数据块</em>)</p></li>
<li><p><strong>uplink_chunk</strong> – 最大253字节(<em>不透明数据作为上行链路发送到主站</em>)</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>C代码示例</strong></p>
<p>用户应用程序不可用。</p>
<p><strong>UART 示例</strong></p>
<p>UART 接口不可用。</p>
<p><strong>SPI示例（关接除外）</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV 请求</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>类型</p></td>
<td><p>长度</p></td>
<td><p>价值</p></td>
</tr>
<tr class="row-odd"><td rowspan="2"><p>0x37</p></td>
<td rowspan="2"><p>0x02</p></td>
<td><p>downlink_byte_cnt = 下行数据大小 (244 字节)</p></td>
</tr>
<tr class="row-even"><td><p>0xF4 0x00</p></td>
</tr>
</tbody>
</table>
<p>类型0x37 表示指令 dwm_backhaul_xfer</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV 响应</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>类型</p></td>
<td><p>长度</p></td>
<td><p>价值（参见错误代码）</p></td>
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
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV 请求</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>类型</p></td>
<td><p>长度</p></td>
<td><p>价值</p></td>
</tr>
<tr class="row-odd"><td rowspan="2"><p>0x37</p></td>
<td rowspan="2"><p>0x02</p></td>
<td><p>downlink_byte_cnt = 下行数据大小 (244 字节)</p></td>
</tr>
<tr class="row-even"><td><p>0xF4 0x00</p></td>
</tr>
</tbody>
</table>
<div class="line-block">
<div class="line">类型0x37 表示指令 dwm_backhaul_xfer</div>
</div>
<p>此调用在 TLV 请求之后，有数量不定的连续传输。 请参阅 SPI 接口上的 API 描述。。</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p><strong>TLV下行链路编号1,2,3,4,5</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>类型</p></td>
<td><p>长度**（244字节）**</p></td>
<td><p>价值</p></td>
</tr>
<tr class="row-odd"><td><p>0x64</p></td>
<td><p>0xF4 (244)</p></td>
<td><p>下行数据块 1</p></td>
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
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p><strong>TLV 上行链路编号 1,2,3,4,5</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>类型</p></td>
<td><p>长度 <strong>(980 字节)</strong></p></td>
<td><p>价值</p></td>
</tr>
<tr class="row-odd"><td><p>0x6E</p></td>
<td><p>0xFD (253)</p></td>
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
<td><p>0xDD (22#.</p></td>
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


           </div>
