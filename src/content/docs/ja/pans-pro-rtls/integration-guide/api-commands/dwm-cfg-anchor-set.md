---
title: "dwm_cfg_anchor_set"
lang: ja
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-cfg-anchor-set"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/pans-pro-rtls/integration-guide/api-commands/dwm-cfg-anchor-set/"
order: 173
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-cfg-anchor-set">
<span id="id1"></span><h1>dwm_cfg_anchor_set</h1>
<p>指定されたオプションでノードをアンカーとして設定する。BLEオプションは暗号化とともに有効にすることはできない。そうでない場合、設定は無効とみなされ、使用されません。暗号化キーが設定されていない場合、暗号化は有効にできない。このコールは、新しいコンフィギュレーションを有効にするためにリセットを必要とする(<a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/api-commands/dwm-reset#dwm-reset"><span class="std std-ref">dwm_reset</span></a>)。イニシエータで暗号化を有効にすると、同じ暗号化キーが設定されたすべてのノードの暗号化が自動的に有効になります()。これにより、同じパンID(ネットワークID)と暗号化キーを持つネットワーク全体の暗号化が1箇所からリモートで可能になります。</p>
<div class="admonition caution">
<p class="admonition-title">注意</p>
<p>通常、この呼び出しは新しい値を設定するときに内部フラッシュに書き込む。したがって、頻繁に使うべきものではなく、最悪の場合数百ミリ秒かかることもある！</p>
</div>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_cfg_anchor_set">
<span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_cfg_anchor_set</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">dwm_cfg_anchor_t</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n"><span class="pre">cfg_anchor</span></span><span class="sig-paren">)</span><span class="p"><span class="pre">;</span></span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">パラメータ</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>input</strong> -- cfg_anchor</p></li>
<li><p><strong>cfg_anchor</strong> -- initiator, gateway, led_en, ble_en, uwb_mode, fw_update_en, enc_en</p></li>
<li><p><strong>initiator</strong> -- '0' | '1' (<em>イニシエーターの役割を有効にする</em>)</p></li>
<li><p><strong>gateway</strong> -- '0' | '1' (<em>ゲートウェイの役割を有効にする</em>)</p></li>
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

<div class="admonition note">
<p class="admonition-title">注釈</p>
<div class="line-block">
<div class="line">ファームウェアがUWBルーティング・バックホール用にコンパイルされている場合のみ利用可能：</div>
<div class="line">uwb_bh_routing: '0' | '1' | '2' (<em>0(OFF) - アンカーはルーティング・アンカーにならない、1(ON) - アンカーはルーティング・アルゴリズムによって優先的にルーティング・アンカーとして選ばれる、2(AUTO) - アンカーがルーティングになるかどうかは、完全にルーティング・アルゴリズムに依存する</em>)</div>
</div>
</div>
<p><strong>Cコード例</strong></p>
<div class="highlight-cpp notranslate"><div class="highlight"><pre><span></span><span class="n">dwm_cfg_anchor_t</span><span class="w"> </span><span class="n">cfg</span><span class="p">;</span>
<span class="kt">int</span><span class="w"> </span><span class="n">rv</span><span class="p">;</span>
<span class="n">cfg</span><span class="p">.</span><span class="n">initiator</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1</span><span class="p">;</span>
<span class="n">cfg</span><span class="p">.</span><span class="n">gateway</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">0</span><span class="p">;</span>
<span class="cm">/* [Available only when the firmware is compiled with UWB routing backhaul: cfg.uwb_bh_routing: DWM_UWB_BH_ROUTING_AUTO;] */</span>
<span class="n">cfg</span><span class="p">.</span><span class="n">common</span><span class="p">.</span><span class="n">enc_en</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1</span><span class="p">;</span>
<span class="n">cfg</span><span class="p">.</span><span class="n">common</span><span class="p">.</span><span class="n">led_en</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1</span><span class="p">;</span>
<span class="n">cfg</span><span class="p">.</span><span class="n">common</span><span class="p">.</span><span class="n">ble_en</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1</span><span class="p">;</span>
<span class="n">cfg</span><span class="p">.</span><span class="n">common</span><span class="p">.</span><span class="n">fw_update_en</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="mi">1</span><span class="p">;</span>
<span class="n">cfg</span><span class="p">.</span><span class="n">common</span><span class="p">.</span><span class="n">uwb_mode</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">DWM_UWB_MODE_OFF</span><span class="p">;</span>
<span class="n">rv</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">dwm_cfg_anchor_set</span><span class="p">(</span><span class="o">&amp;</span><span class="n">cfg</span><span class="p">);</span>
<span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">rv</span><span class="w"> </span><span class="o">==</span><span class="w"> </span><span class="n">DWM_ERR_PERM</span><span class="p">)</span>
<span class="p">{</span>
<span class="w">  </span><span class="n">printf</span><span class="p">(</span><span class="s">"Error: either encryption or BLE can be enabled, encryption can be enabled only if encryption key is set</span><span class="se">\n</span><span class="s">”);</span>
<span class="p">}</span>
<span class="n">dwm_reset</span><span class="p">();</span>
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
<tr class="row-even"><td rowspan="2"><p>0x07</p></td>
<td rowspan="2"><p>0x02</p></td>
<td><ul class="simple">
<li><p>(ビット0-#) uwb_mode</p></li>
<li><p>(ビット2) fw_update_en</p></li>
<li><p>(ビット3) ble_en</p></li>
<li><p>(ビット4) led_en</p></li>
<li><p>(ビット5) enc_en</p></li>
</ul>
</td>
</tr>
<tr class="row-odd"><td><p>0x9C 0x02</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x07 は、コマンド <a class="reference internal" href="#dwm-cfg-anchor-set"><span class="std std-ref">dwm_cfg_anchor_set</span></a> を意味する</p>
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
