---
title: "dwm_status_get"
lang: ja
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-status-get"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/pans-pro-rtls/integration-guide/api-commands/dwm-status-get/"
order: 210
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-status-get">
<span id="id1"></span><h1>dwm_status_get</h1>
<p>システムステータスを取得します。次のフラグが使用可能です。</p>
<ul class="simple">
<li><p>位置データの準備ができました</p></li>
<li><p>ノードが UWB ネットワークに参加しました</p></li>
<li><p>新しいバックホール データの準備ができました</p></li>
<li><p>バックホールのステータスが変更されました</p></li>
<li><p>バックホールルートが初期化されました</p></li>
<li><p>UWB スキャン結果の準備ができました</p></li>
<li><p>UWB 経由でユーザー データを受信しました</p></li>
<li><p>UWB 経由で送信されたユーザー データ</p></li>
<li><p>ファームウェアのアップデートが進行中です</p></li>
</ul>
<p>以下を除き、フラグは呼び出し後にクリアされます。</p>
<ul class="simple">
<li><p>ノードが UWB ネットワークに参加しました</p></li>
<li><p>バックホールルートが初期化されました</p></li>
<li><p>ファームウェアのアップデートが進行中です</p></li>
</ul>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_status_get">
<span class="kt"><span class="pre">int</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_status_get</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">dwm_status_t</span></span><span class="p"><span class="pre">*</span></span><span class="sig-paren">)</span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">パラメータ</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>input</strong> -- (<em>なし</em>)</p></li>
<li><p><strong>output</strong> -- <a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">ステータスコード</span></a>,ステータス</p></li>
<li><p><strong>status</strong> -- loc_ready, uwbmac_joined, bh_data_ready, bh_initialized, bh_status_changed, uwb_scan_ready, usr_data_ready</p></li>
<li><p><strong>loc_ready</strong> -- '0' | ‘1’ (<em>新しい位置データが準備できました</em>)</p></li>
<li><p><strong>uwbmac_joined</strong> -- '0' | ‘1’ (<em>ノードは UWB ネットワークに接続されています</em>)</p></li>
<li><p><strong>bh_data_ready</strong> -- '0' | ‘1’ (<em>UWB MAC バックホール データ準備完了</em>)</p></li>
<li><p><strong>bh_status_changed</strong> -- '0' | ‘1’ (<em>UWB MAC ステータスが変更され、バックホールで使用されます</em>)</p></li>
<li><p><strong>bh_initialized</strong> -- '0' | ‘1’ (<em>ノードは UWB バックホール経由でルートを初期化しました</em>)</p></li>
<li><p><strong>uwb_scan_ready</strong> -- '0' | ‘1’ (<em>UWB スキャン結果は準備完了</em>)</p></li>
<li><p><strong>usr_data_ready</strong> -- '0' | ‘1’ (<em>UWB 経由で受信したユーザー データ</em>)</p></li>
<li><p><strong>usr_data_sent</strong> -- '0' | ‘1’ (<em>UWB 経由で送信されたユーザー データ</em>)</p></li>
<li><p><strong>fwup_in_progress</strong> -- '0' | ‘1’ (<em>ファームウェアアップデート中</em>)</p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>Cコード例</strong></p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="n">dwm_status_t</span><span class="w"> </span><span class="n">status</span><span class="p">;</span>
<span class="kt">int</span><span class="w"> </span><span class="n">rv</span><span class="p">;</span>
<span class="n">rv</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="n">dwm_status_get</span><span class="p">(</span><span class="o">&amp;</span><span class="n">status</span><span class="p">);</span>
<span class="k">if</span><span class="w"> </span><span class="p">(</span><span class="n">rv</span><span class="w"> </span><span class="o">==</span><span class="w"> </span><span class="n">DWM_OK</span><span class="p">)</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="n">printf</span><span class="p">(</span><span class="s">"loc_data: %d</span><span class="se">\n</span><span class="s">"</span><span class="p">,</span><span class="w"> </span><span class="n">status</span><span class="p">.</span><span class="n">loc_dat1</span><span class="p">);</span>
<span class="w">    </span><span class="n">printf</span><span class="p">(</span><span class="s">"uwbmac_joined: %d</span><span class="se">\n</span><span class="s">"</span><span class="p">,</span><span class="w"> </span><span class="n">status</span><span class="p">.</span><span class="n">uwbmac_joined</span><span class="p">);</span>
<span class="w">    </span><span class="n">printf</span><span class="p">(</span><span class="s">"bh_data_ready: %d</span><span class="se">\n</span><span class="s">"</span><span class="p">,</span><span class="w"> </span><span class="n">status</span><span class="p">.</span><span class="n">bh_data_ready</span><span class="p">);</span>
<span class="w">    </span><span class="n">printf</span><span class="p">(</span><span class="s">"bh_status_changed: %d</span><span class="se">\n</span><span class="s">"</span><span class="p">,</span><span class="w"> </span><span class="n">status</span><span class="p">.</span><span class="n">bh_status_changed</span><span class="p">);</span>
<span class="w">    </span><span class="n">printf</span><span class="p">(</span><span class="s">"bh_initialized: %d</span><span class="se">\n</span><span class="s">"</span><span class="p">,</span><span class="w"> </span><span class="n">status</span><span class="p">.</span><span class="n">bh_initialized</span><span class="p">);</span>
<span class="w">    </span><span class="n">printf</span><span class="p">(</span><span class="s">"uwb_scan_ready: %d</span><span class="se">\n</span><span class="s">"</span><span class="p">,</span><span class="w"> </span><span class="n">status</span><span class="p">.</span><span class="n">uwb_scan_ready</span><span class="p">);</span>
<span class="w">    </span><span class="n">printf</span><span class="p">(</span><span class="s">"usr_data_ready: %d</span><span class="se">\n</span><span class="s">"</span><span class="p">,</span><span class="w"> </span><span class="n">status</span><span class="p">.</span><span class="n">usr_data_ready</span><span class="p">);</span>
<span class="w">    </span><span class="n">printf</span><span class="p">(</span><span class="s">"usr_data_sent: %d</span><span class="se">\n</span><span class="s">"</span><span class="p">,</span><span class="w"> </span><span class="n">status</span><span class="p">.</span><span class="n">usr_data_sent</span><span class="p">);</span>
<span class="w">    </span><span class="n">printf</span><span class="p">(</span><span class="s">"fwup_in_progress: %d</span><span class="se">\n</span><span class="s">"</span><span class="p">,</span><span class="w"> </span><span class="n">status</span><span class="p">.</span><span class="n">fwup_in_progress</span><span class="p">);</span>
<span class="p">}</span>
<span class="k">else</span><span class="w"> </span><span class="p">{</span>
<span class="w">    </span><span class="n">printf</span><span class="p">(</span><span class="s">"error</span><span class="se">\n</span><span class="s">"</span><span class="p">);</span>
<span class="p">}</span>
</pre></div>
</div>
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
<tr class="row-odd"><td><p>0x32</p></td>
<td><p>0x00</p></td>
</tr>
</tbody>
</table>
<p>タイプ 0x32 はコマンド dwm_status_get を意味します</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 14%">
<col style="width: 14%">
<col style="width: 14%">
<col style="width: 14%">
<col style="width: 14%">
<col style="width: 32%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="6"><p>TLV 応答</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p>タイプ</p></td>
<td><p>長さ</p></td>
<td><p>値（エラーコードを参照）</p></td>
<td><p>タイプ</p></td>
<td><p>長さ</p></td>
<td><p>値</p></td>
</tr>
<tr class="row-odd"><td rowspan="2"><p>0x40</p></td>
<td rowspan="2"><p>0x01</p></td>
<td rowspan="2"><p>0x00</p></td>
<td rowspan="2"><p>0x5A</p></td>
<td rowspan="2"><p>0x02</p></td>
<td><p>loc_ready (ビット 0) uwbmac_joined (ビット 1) bh_status_changed (ビット 2) bh_data_ready (ビット 3) bh_initialized (ビット 4) uwb_scan_ready (ビット 5) usr_data_ready (ビット 6) usr_data_sent (ビット 7) fwup_in_progress(ビット 8) 予約済み (ビット 9 ～ 15)</p></td>
</tr>
<tr class="row-even"><td><p>0x01 0x00</p></td>
</tr>
</tbody>
</table>
<div class="line-block">
<div class="line">タイプ 0x5A はステータスを意味します</div>
<div class="line">タイプ0x40は、直前のコマンドの <a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">ステータスコード</span></a> を意味する</div>
</div>
</div>


           </div>
