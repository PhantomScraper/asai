---
title: "dwm_cfg_tag_set"
lang: ja
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-cfg-tag-set"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/pans-pro-rtls/integration-guide/api-commands/dwm-cfg-tag-set/"
order: 175
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-cfg-tag-set">
<span id="id1"></span><h1>dwm_cfg_tag_set</h1>
<p>指定されたオプションでノードをタグとして設定します。BLEオプションは暗号化とともに有効にすることはできません。そうでない場合、設定は無効とみなされ、使用されません。暗号化キーが設定されていない場合、暗号化は有効にできません。この呼び出しでは、新しい設定を有効にするためにリセットが必要です (<a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/api-commands/dwm-reset#dwm-reset"><span class="std std-ref">dwm_reset</span></a>)。</p>
<div class="admonition caution">
<p class="admonition-title">注意</p>
<p>通常、この呼び出しは新しい値を設定するときに内部フラッシュに書き込む。したがって、頻繁に使うべきものではなく、最悪の場合数百ミリ秒かかることもある！</p>
</div>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_cfg_tag_set">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_cfg_tag_set</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">dwm_cfg_tag_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n"><span class="pre">cfg_tag</span></span><span class="sig-paren">)</span><span class="p"><span class="pre">;</span></span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">パラメータ</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>input</strong> -- cfg_tag</p></li>
<li><p><strong>cfg_tag</strong> -- stnry_en, low_power_en, meas_mode, loc_engine_en, led_en, ble_en, uwb_mode, fw_update_en, enc_en</p></li>
<li><p><strong>stnry_en</strong> -- '0' | '1' (<em>有効な場合、ノードが:param移動していない場合、通常の更新レートの代わりに静止更新レートが使用されます。</em>)</p></li>
<li><p><strong>meas_mode</strong> -- '0' | '1' | '2' | '3' (<em>0 - 双方向レンジング、1,2,3 - 予約済み</em>)</p></li>
<li><p><strong>low_power_en</strong> -- '0' | '1' (* 低消費電力モードイネーブル*)</p></li>
<li><p><strong>loc_engine_en</strong> -- '0' | '1' (<em>0 は内部 Location Engine を使用しないことを意味し、1 は内部 Location Engine を意味する。</em>)</p></li>
<li><p><strong>enc_en</strong> -- '0' | '1' (* 暗号化有効*)</p></li>
<li><p><strong>led_en</strong> -- '0' | '1' (* 汎用LEDを使用可能*)</p></li>
<li><p><strong>ble_en</strong> -- '0' | '1' (<em>BLEイネーブル</em>)</p></li>
<li><p><strong>uwb_mode</strong> -- '0' | '1' | '2' (<em>0オフ、1パッシブ、2アクティブ</em>)</p></li>
<li><p><strong>fw_update_en</strong> -- '0' | '1' (* ファームウェア・アップデート有効*)</p></li>
<li><p><strong>output</strong> -- <a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">ステータスコード</span></a></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>Cコード例</strong></p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="n">dwm_cfg_tag_t</span><span class="w"> </span><span class="n">cfg</span><span class="p">;</span>
<span class="n">cfg</span><span class="p">.</span><span class="n">stnry_en</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1</span><span class="p">;</span>
<span class="n">cfg</span><span class="p">.</span><span class="n">meas_mode</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">DWM_MEAS_MODE_TWR</span><span class="p">;</span>
<span class="n">cfg</span><span class="p">.</span><span class="n">low_power_en</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
<span class="n">cfg</span><span class="p">.</span><span class="n">loc_engine_en</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1</span><span class="p">;</span>
<span class="n">cfg</span><span class="p">.</span><span class="n">common</span><span class="p">.</span><span class="n">enc_en</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1</span><span class="p">;</span>
<span class="n">cfg</span><span class="p">.</span><span class="n">common</span><span class="p">.</span><span class="n">led_en</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1</span><span class="p">;</span>
<span class="n">cfg</span><span class="p">.</span><span class="n">common</span><span class="p">.</span><span class="n">ble_en</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
<span class="n">cfg</span><span class="p">.</span><span class="n">common</span><span class="p">.</span><span class="n">fw_update_en</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
<span class="n">cfg</span><span class="p">.</span><span class="n">common</span><span class="p">.</span><span class="n">uwb_mode</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">DWM_UWB_MODE_ACTIVE</span><span class="p">;</span>
<span class="n">dwm_cfg_tag_set</span><span class="p">(</span><span class="o">&amp;</span><span class="n">cfg</span><span class="p">);</span>
</pre></div>
</div>
<p><strong>SPI/UART 例</strong></p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 25%">
<col style="width: 25%">
<col style="width: 50%">
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
<tr class="row-odd"><td rowspan="2"><p>0x05</p></td>
<td rowspan="2"><p>0x02</p></td>
<td><p><em>BYTE 1:</em></p>
<ul class="simple">
<li><p>ビット3-7:予約済み</p></li>
<li><p>ビット2:stnry_en</p></li>
<li><p>ビット 0-#. meas_mode： 0 -TWR、1-3予約</p></li>
</ul>
<p><em>BYTE 0:</em></p>
<ul class="simple">
<li><p>ビット7: low_power_en</p></li>
<li><p>ビット6: loc_engine_en</p></li>
<li><p>ビット5: enc_en</p></li>
<li><p>ビット4: led_en</p></li>
<li><p>ビット3: ble_en</p></li>
<li><p>ビット2: fw_update_en</p></li>
<li><p>ビット0-#.uwb_mode</p></li>
</ul>
</td>
</tr>
<tr class="row-even"><td><p>0x72 0x04</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x05 は、コマンド <a class="reference internal" href="#dwm-cfg-tag-set"><span class="std std-ref">dwm_cfg_tag_set</span></a> を意味する</p>
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
