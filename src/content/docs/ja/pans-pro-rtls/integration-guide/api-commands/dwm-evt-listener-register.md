---
title: "dwm_evt_listener_register"
lang: ja
slug: "pans-pro-rtls/integration-guide/api-commands/dwm-evt-listener-register"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/pans-pro-rtls/integration-guide/api-commands/dwm-evt-listener-register/"
order: 180
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="dwm-evt-listener-register">
<span id="id1"></span><h1>dwm_evt_listener_register</h1>
<p>ユーザー・アプリケーションでは、このコマンドは、ファームウェアから来るイベントをリッスン するために登録するために使用される。例えば、LE が位置計算を終了した時や距離が計算された時にイベントをトリガーすることができます。この呼び出しはエンド・ユーザー・アプリケーションにのみ適用され、SPI や UART では使用できません。低消費電力モードでは、イベント・リスナーはスリープから復帰するために登録されなければな りません。そうしないと、ユーザー・アプリケーションはスリープ状態のままになります。</p>
<p>ユーザーがリッスンできるイベント：</p>
<ul class="simple">
<li><p>DWM_EVT_LOC_READY</p></li>
<li><p>DWM_EVT_USR_DATA_READY</p></li>
<li><p>DWM_EVT_USR_DATA_SENT</p></li>
<li><p>DWM_EVT_BH_INITIALIZED</p></li>
<li><p>DWM_EVT_UWBMAC_JOINED_CHANGED</p></li>
<li><p>DWM_EVT_UWB_SCAN_READY</p></li>
</ul>
<dl class="c function">
<dt class="sig sig-object c" id="c.dwm_evt_listener_register">
<span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="sig-name descname"><span class="n"><span class="pre">dwm_evt_listener_register</span></span></span><span class="sig-paren">(</span><span class="n"><span class="pre">uint32_t</span></span><span class="w"> </span><span class="n"><span class="pre">evt_id_map</span></span>, <span class="kt"><span class="pre">void</span></span><span class="w"> </span><span class="p"><span class="pre">*</span></span><span class="n"><span class="pre">context</span></span><span class="sig-paren">)</span><br></dt>
<dd><dl class="field-list simple">
<dt class="field-odd">パラメータ</dt>
<dd class="field-odd"><ul class="simple">
<li><p><strong>input</strong> -- event_id_map, context</p></li>
<li><p><strong>event_id_map</strong> -- 32ビット幅のビットマップ (ユーザーが聞きたい/聞きたくないイベントのフラグをそれぞれ設定/クリアする必要がある。 <a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/api-commands/dwm-evt-wait#dwm-evt-wait"><span class="std std-ref">dwm_evt_wait</span></a> を参照)</p></li>
<li><p><strong>context</strong> -- ユーザーがコールバックコンテキストに渡したいデータ</p></li>
<li><p><strong>output</strong> -- <a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/generic-api-information#pans-statuscode"><span class="std std-ref">ステータスコード</span></a></p></li>
</ul>
</dd>
</dl>
</dd></dl>

<p><strong>Cコード例</strong></p>
<div class="highlight-c notranslate"><div class="highlight"><pre><span></span><span class="n">dwm_evt_listener_register</span><span class="p">(</span><span class="n">DWM_EVT_LOC_READY</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="n">DWM_EVT_USR_DATA_READY</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="n">DWM_EVT_USR_DATA_SENT</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="n">DWM_EVT_UWB_SCAN_READY</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="n">DWM_EVT_BH_INITIALIZED</span><span class="w"> </span><span class="o">|</span><span class="w"> </span><span class="n">DWM_EVT_UWBMAC_JOINED_CHANGED</span><span class="p">,</span><span class="w"> </span><span class="nb">NULL</span><span class="p">);</span>
</pre></div>
</div>
<p><strong>SPI/UART 例</strong></p>
<p>これらのインターフェースでは使用できません</p>
</div>


           </div>
