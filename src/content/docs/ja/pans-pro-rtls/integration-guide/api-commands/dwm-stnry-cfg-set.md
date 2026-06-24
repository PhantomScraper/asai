---
title: "dwm_stnry_cfg_set"
lang: ja
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-stnry-cfg-set"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/pans-pro-rtls/integration-guide/api-commands/dwm-stnry-cfg-set/"
order: 212
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-stnry-cfg-set">
<span id="id1"></span><h1>dwm_stnry_cfg_set</h1>
<p>タグノードが使用する定常モードの設定を書き込む。この設定は、定常検出が無効になっている場合でも保存されます (<a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/api-commands/dwm-cfg-tag-set#dwm-cfg-tag-set"><span class="std std-ref">dwm_cfg_tag_set</span></a> を参照)。これは内部の不揮発性メモリに書き込むので、注意して使用する必要があります。新しい感度設定は、ステーショナリーモードが有効になると即座に有効になる。デフォルトの感度は <code class="docutils literal notranslate"><span class="pre">HIGH</span></code> である。</p>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_stnry_cfg_set">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_stnry_cfg_set</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">uint16_t</span></span><span class="sig-paren">)</span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">パラメータ</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>input</strong> -- 感性</p></li>
<li><p><strong>sensitivity</strong> -- ‘0’ | ‘1’ | ‘2’ (<em>0 - LOW [4064 mg] , 1 - NORMAL [2048 mg], 2 - HIGH [512 mg]</em>)</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>Cコード例</strong></p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="n">dwm_stnry_cfg_set</span><span class="p">(</span><span class="n">DWM_STNRY_SENSITIVITY_HIGH</span><span class="p">);</span>
</pre></div>
</div>
<p><strong>SPI/UART 例</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 33%">
<col style="width: 33%">
<col style="width: 33%">
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
<tr class="row-odd"><td><p>0x11</p></td>
<td><p>0x01</p></td>
<td><p>0x01</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x11 は、コマンド dwm_stnry_cfg_set を意味する</p>
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
<div class="line-block">
<div class="line">タイプ0x40は、直前のコマンドの <a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">ステータスコード</span></a> を意味する</div>
</div>
</div>


           </div>
