---
title: "dwm_upd_rate_set"
lang: ja
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-upd-rate-set"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/pans-pro-rtls/integration-guide/api-commands/dwm-upd-rate-set/"
order: 215
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-upd-rate-set">
<span id="id1"></span><h1>dwm_upd_rate_set</h1>
<p>位置更新レートと静止更新レートを数百ミリ秒単位で設定する。この呼び出しは通常、新しい値が設定されると内部フラッシュに書き込まれる。したがって、頻繁に呼び出すべきではありません。応答には、最悪の場合数百ミリ秒かかることがある。</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_upd_rate_set">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_upd_rate_set</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">uint8_t</span></span><span class="w"> </span><span class="n"><span class="pre">update_rate</span></span>, <span class="n"><span class="pre">uint8_t</span></span><span class="w"> </span><span class="n"><span class="pre">update_rate_stationary</span></span><span class="sig-paren">)</span><span class="p"><span class="pre">;</span></span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">パラメータ</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>update_rate</strong> -- 16ビット整数（<em>100ミリ秒の倍数での位置公表レート、最大は1分、最小は100ミリ秒</em>)</p></li>
<li><p><strong>update_rate_stationary</strong> -- 16ビット整数（<em>ノードが100ミリ秒の倍数で移動していないときの位置公開レート、最大は1分、最小は100ミリ秒</em>）</p></li>
<li><p><strong>output</strong> -- <a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">ステータスコード</span></a></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>Cコード例</strong></p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="n">dwm_upd_rate_set</span><span class="p">(</span><span class="mi">10</span><span class="p">,</span><span class="w"> </span><span class="mi">50</span><span class="p">);</span><span class="w"> </span><span class="cm">/* update rate 1 second. 5 seconds stationary */</span>
<span class="n">dwm_upd_rate_set</span><span class="p">(</span><span class="mi">10</span><span class="p">,</span><span class="w"> </span><span class="mi">0</span><span class="p">);</span><span class="w"> </span><span class="cm">/* ERROR - must not be a zero */</span>
</pre></div>
</div>
<p><strong>SPI/UART 例</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 32%">
<col style="width: 32%">
<col style="width: 37%">
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
<tr class="row-odd"><td><p>0x03</p></td>
<td><p>0x04</p></td>
<td><p>最初の2バイトはリトルエンディアンの16ビット値で、更新レートは100msの倍数（例えば、0x0A 0x00は10を意味する）、2番目の2バイトはリトルエンディアンの16ビット値で、定常更新レートは100msの倍数。</p></td>
</tr>
<tr class="row-even"><td></td>
<td></td>
<td><p>0x0A 0x00 0x014 0x00</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x03 は、コマンド dwm_upd_rate_set を意味する</p>
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
<p>タイプ0x40は、直前のコマンドの <a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">ステータスコード</span></a> を意味する</p>
</div>


           </div>
