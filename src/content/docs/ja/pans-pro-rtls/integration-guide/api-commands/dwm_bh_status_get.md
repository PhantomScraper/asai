---
title: "dwm_bh_status_get"
lang: ja
slug: "pans-pro-rtls/integration-guide/api-commands/dwm_bh_status_get"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/pans-pro-rtls/integration-guide/api-commands/dwm_bh_status_get/"
order: 164
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-bh-status-get">
<span id="id1"></span><h1>dwm_bh_status_get</h1>
<p>現在のUWBMACバックホールのステータスを取得します。ノードはゲートウェイとして設定されている必要があります。</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_bh_status_get">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_bh_status_get</span></span></span><span class="sig-paren">(</span><span class="kt"><span class="pre">void</span></span><span class="sig-paren">)</span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">パラメータ</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>input</strong> -- (<em>なし</em>)</p></li>
<li><p><strong>output</strong> -- sf_number, bh_seat_map, origin_cnt, {origin_info}</p></li>
<li><p><strong>sf_number</strong> -- 16ビット整数 (<em>現在のスーパーフレーム番号</em>)</p></li>
<li><p><strong>bh_seat_map</strong> -- 32ビット整数(<em>現在のスーパーフレームのシートマップ</em>)</p></li>
<li><p><strong>origin_cnt</strong> -- 8ビット整数 (<em>範囲は0から8</em>)</p></li>
<li><p><strong>origin_info</strong> -- node_id, bh_seat, hop_lvl (<em>起点リストの要素</em>)</p></li>
<li><p><strong>node_id</strong> -- 16ビット整数（<em>オリジン・アドレス</em>）</p></li>
<li><p><strong>bh_seat</strong> -- 8ビットの整数（<em>原点が占める席、範囲は0から8まで</em>）</p></li>
<li><p><strong>hop_lvl</strong> -- 8ビット整数(<em>ホップレベル</em>)</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>Cコード例</strong></p>
<p>モジュール上のユーザーアプリケーションでは利用できません。</p>
<p><strong>SPI/UART 例</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 50%">
<col style="width: 50%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="2"><p>TLV 要求</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>タイプ</p></td>
<td><p>長さ</p></td>
</tr>
<tr class="row-odd"><td><p>0x3A</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x3A は、コマンド dwm_bh_status_get を意味する</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 16%">
<col style="width: 12%">
<col style="width: 12%">
<col style="width: 10%">
<col style="width: 12%">
<col style="width: 39%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="6"><p>TLV 応答</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td rowspan="2"><p>タイプ</p></td>
<td rowspan="2"><p>長さ</p></td>
<td rowspan="2"><p>値</p></td>
<td rowspan="2"><p>タイプ</p></td>
<td rowspan="2"><p>長さ</p></td>
<td><p>値</p></td>
</tr>
<tr class="row-odd"><td><div class="line-block">
<div class="line">(2バイト) sf_number</div>
<div class="line">(4バイト) bh_seat_map</div>
<div class="line">(1バイト) origin_cnt</div>
<div class="line">(N*4バイト) N*origin_info</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
<td><p>0x5D</p></td>
<td><p>0x13</p></td>
<td><p>0x6c 0x00
0x07 0x00
0x00 0x00
0x03
0xf3 0x11
0x00 0x01
0xc3 0x11
0x01 0x01
0x66 0x11
0x02 0x01</p></td>
</tr>
</tbody>
</table>
<div class="line-block">
<div class="line">タイプ0x40は、直前のコマンドの <a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">ステータスコード</span></a> を意味する</div>
<div class="line">タイプ 0x5D は UWBMAC ステータスを意味する</div>
</div>
</div>


           </div>
