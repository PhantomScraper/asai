---
title: "dwm_usr_data_write"
lang: ja
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-usr-data-write"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/pans-pro-rtls/integration-guide/api-commands/dwm-usr-data-write/"
order: 217
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-usr-data-write">
<span id="id1"></span><h1>dwm_usr_data_write</h1>
<p>ユーザー データを UWB ネットワークに送信します。</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_usr_data_write">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_usr_data_write</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">uint8_t</span></span><span class="p"><span class="pre">*</span></span>, <span class="n"><span class="pre">uint8_t</span></span>, <span class="n"><span class="pre">boolean_t</span></span><span class="sig-paren">)</span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">パラメータ</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>input</strong> -- データ、長さ、上書き</p></li>
<li><p><strong>data</strong> -- 最大 34 バイト (<em>書き込まれるユーザーデータ</em>)</p></li>
<li><p><strong>len</strong> -- (<em>データ長、最大 34 バイト</em>)</p></li>
<li><p><strong>overwrite</strong> -- bool (<em>強制書き込み、まだゲートウェイに送信されていないデータを上書きします</em>)</p></li>
<li><p><strong>output</strong> -- <a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">ステータスコード</span></a></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>Cコード例</strong></p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="kt">uint8_t</span><span class="w"> </span><span class="n">len</span><span class="p">,</span><span class="w"> </span><span class="n">data</span><span class="p">[</span><span class="n">DWM_USR_DATA_LEN_MAX</span><span class="p">];</span>
<span class="n">len</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">DWM_USR_DATA_LEN_MAX</span><span class="p">;</span>
<span class="n">dwm_usr_data_write</span><span class="p">(</span><span class="n">data</span><span class="p">,</span><span class="w"> </span><span class="n">len</span><span class="p">,</span><span class="w"> </span><span class="nb">false</span><span class="p">);</span>
</pre></div>
</div>
<p><strong>SPI/UART 例</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 29%">
<col style="width: 29%">
<col style="width: 43%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV 要求</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>タイプ</p></td>
<td><p>長さ</p></td>
<td><p>値</p></td>
</tr>
<tr class="row-odd"><td rowspan="2"><p>0x1A</p></td>
<td rowspan="2"><p>0x23</p></td>
<td><div class="line-block">
<div class="line">バイト 0: フラグ</div>
<div class="line-block">
<div class="line">- overwrite (bit 0)</div>
<div class="line">- reserved (bit 1 - bit 7)</div>
</div>
</div>
<div class="line-block">
<div class="line">バイト 1 - N: ユーザーデータ (2 &lt;= N &lt;= 34)</div>
</div>
</td>
</tr>
<tr class="row-even"><td><p>0x01 0x01 0x02 0x03
…. 0x23 0x22</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x1A はコマンド dwm_usr_data_write を意味します</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="3"><p>TLV 応答</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>タイプ</p></td>
<td><p>長さ</p></td>
<td><p>値（エラーコードを参照）</p></td>
</tr>
<tr class="row-odd"><td><p>0x40</p></td>
<td><p>0x01</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x40 はコマンドの <a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">ステータスコード</span></a> を意味します</p>
</div>


           </div>
