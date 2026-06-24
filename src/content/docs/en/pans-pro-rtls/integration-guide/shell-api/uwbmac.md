---
title: "UWBMAC"
lang: en
slug: "pans-pro-rtls/integration-guide/shell-api/uwbmac"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/pans-pro-rtls/integration-guide/shell-api/uwbmac/"
order: 163
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="uwbmac">
<h1>UWBMAC</h1>
<hr class="docutils">
<div class="section" id="nmo">
<span id="pp-nmo"></span><h2>nmo</h2>
<p>Enables passive offline option and resets the node.</p>
<p><strong>Example:</strong></p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">dwm&gt; nmo</span>
<span class="go">/* press enter twice to switch to shell mode after reset */</span>
<span class="go"> PANS PRO Real Time Location System</span>
<span class="go"> Copyright :  2016-2021 LEAPS and Decawave/Qorvo</span>
<span class="go"> License   :  Please visit https://www.leapslabs.com/pans-pro-license</span>
<span class="go"> Compiled  :  Apr 13 2021 14:50:42</span>
<span class="go"> Help      :  ? or help</span>

<span class="go"> dwm&gt; si</span>
<span class="go"> /\*... Look at `mode*/</span>
<span class="go"> [000001.234 INF] mode: tn (off,twr,np,nole)</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="nmp">
<span id="pp-nmp"></span><h2>nmp</h2>
<p>Set UWB mode to passive.</p>
<p><strong>Example:</strong></p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">dwm&gt; nmp</span>
<span class="go">/* press enter twice to switch to shell mode after reset*/</span>
<span class="go"> PANS PRO Real Time Location System</span>
<span class="go"> Copyright :  2016-2021 LEAPS and Decawave/Qorvo</span>
<span class="go"> License   :  Please visit https://www.leapslabs.com/pans-pro-license</span>
<span class="go"> Compiled  :  Apr 13 2021 14:50:42</span>
<span class="go"> Help      :  ? or help</span>
<span class="go">dwm&gt; si</span>
<span class="go">/\*... Look at `mode*/</span>
<span class="go">[000001.234 INF] mode: tn (pasv,twr,np,nole)</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="nma">
<span id="pp-nma"></span><h2>nma</h2>
<p>Configures node to as anchor, active and resets the node.</p>
<p><strong>Example:</strong></p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">dwm&gt; nma</span>
<span class="go">/* press Enter twice */</span>
<span class="go"> PANS PRO Real Time Location System</span>
<span class="go"> Copyright :  2016-2021 LEAPS and Decawave/Qorvo</span>
<span class="go"> License   :  Please visit https://www.leapslabs.com/pans-pro-license</span>
<span class="go"> Compiled  :  Apr 13 2021 14:50:42</span>
<span class="go"> Help      :  ? or help</span>
<span class="go">dwm&gt; si</span>
<span class="go">/\*... Look at `mode*/</span>
<span class="go">[000001.234 INF] mode: an (act,-,-)</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="nmi">
<span id="pp-nmi"></span><h2>nmi</h2>
<p>Configures node to as anchor - initiator, active and resets the node.</p>
<p><strong>Example:</strong></p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">dwm&gt; nmi</span>
<span class="go">/* press enter twice */</span>
<span class="go"> PANS PRO Real Time Location System</span>
<span class="go"> Copyright :  2016-2021 LEAPS and Decawave/Qorvo</span>
<span class="go"> License   :  Please visit https://www.leapslabs.com/pans-pro-license</span>
<span class="go"> Compiled  :  Apr 13 2021 14:50:42</span>
<span class="go"> Help      :  ? or help</span>
<span class="go">dwm&gt; si</span>
<span class="go">/*... Look at `mode*/</span>
<span class="go">[000001.234 INF] mode: ain (act,real,-)</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="nmt">
<span id="pp-nmt"></span><h2>nmt</h2>
<p>Configures node to as tag, active and resets the node.</p>
<p><strong>Example:</strong></p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">dwm&gt; nmt</span>
<span class="go">/* press enter twice */</span>
<span class="go"> PANS PRO Real Time Location System</span>
<span class="go"> Copyright :  2016-2021 LEAPS and Decawave/Qorvo</span>
<span class="go"> License   :  Please visit https://www.leapslabs.com/pans-pro-license</span>
<span class="go"> Compiled  :  Apr 13 2021 14:50:42</span>
<span class="go"> Help      :  ? or help</span>
<span class="go">dwm&gt; si</span>
<span class="go">/*... Look at `mode*/</span>
<span class="go">[000001.234 INF] mode: tn (act,twr,np,le)</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="nmtl">
<span id="pp-nmtl"></span><h2>nmtl</h2>
<p>Configures node to as tag, active, low-power and resets the node.</p>
<p><strong>Example:</strong></p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">dwm&gt; nmtl</span>
<span class="go">/* press enter twice */</span>
<span class="go"> PANS PRO Real Time Location System</span>
<span class="go"> Copyright :  2016-2021 LEAPS and Decawave/Qorvo</span>
<span class="go"> License   :  Please visit https://www.leapslabs.com/pans-pro-license</span>
<span class="go"> Compiled  :  Apr 13 2021 14:50:42</span>
<span class="go"> Help      :  ? or help</span>
<span class="go">dwm&gt; si</span>
<span class="go">/*... Look at `mode*/</span>
<span class="go">[000001.234 INF] mode: tn (act,twr,lp,le)</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="nmg">
<span id="pp-nmg"></span><h2>nmg</h2>
<p>Sets mode to GN</p>
<hr class="docutils">
</div>
<div class="section" id="la">
<span id="pp-la"></span><h2>la</h2>
<p>Shows anchor list (the output can slightly differ based on node type).</p>
<p><strong>Example:</strong></p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">la</span>
<span class="go">[007582.110 INF] AN: cnt=5 seq=x15</span>
<span class="go">[007582.110 INF]    0) id=DECAA6429C750997 seat=0 idl=1 seens=90 rssi=-79 fl=0001</span>
<span class="go">[007582.120 INF]    1) id=DECA5AA932A3D482 seat=1 idl=1 seens=35 rssi=-79 fl=0001</span>
<span class="go">[007582.120 INF]    2) id=DECAA19F7B23CAAB seat=2 idl=1 seens=21 rssi=-79 fl=0001</span>
<span class="go">[007582.130 INF]    3) id=DECA97E24B94C5B7 seat=3 idl=0 seens=254 rssi=-79 fl=0001</span>
<span class="go">[007582.140 INF]    4) id=DECA1DAB42E4C62F seat=4 idl=1 seens=47 rssi=-79 fl=0001</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="lg">
<span id="pp-lg"></span><h2>lg</h2>
<p>Shows GN list</p>
<p><strong>Example:</strong></p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">&gt; lb</span>
<span class="go">[007922.440 INF] GN: cnt=2 seq=x01</span>
<span class="go">[007922.440 INF]     0) id=DECAAE5D14830CB2 seat=1 seens=0 rssi=-127</span>
<span class="go">[007922.450 INF]     1) id=0000000000000D35 seat=2 seens=170 rssi=-82</span>
<span class="go">[007922.450 INF]</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="lr">
<span id="pp-lr"></span><h2>lr</h2>
<p>Lists routes [Available only when the firmware is compiled with UWB routing backhaul]</p>
<p><strong>Example:</strong></p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">lr</span>
<span class="go">[007019.790 INF] bh : cnt=9 sf=259 seq=xBB    gn    |   ul_loc   ul_iot |   dl_iot</span>
<span class="go">[007019.800 INF]  0) x0997 : x0997 -&gt; x0D35 : x0D35 |   544062   545237 |       39</span>
<span class="go">[007019.810 INF]  1) xC5B7 : xC5B7 -&gt; x0D35 : x0D35 |   536665   537756 |        2</span>
<span class="go">[007019.810 INF]  2)   -   :</span>
<span class="go">[007019.820 INF]  3)   -   :</span>
<span class="go">[007019.820 INF]  4)   -   :</span>
<span class="go">[007019.820 INF]  5)   -   :</span>
<span class="go">[007019.820 INF]  6)   -   :</span>
<span class="go">[007019.830 INF]  7)   -   :</span>
<span class="go">[007019.830 INF]  8)   -   :</span>
<span class="go">[007019.830 INF]</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="lrn">
<span id="pp-lrn"></span><h2>lrn</h2>
<p>Lists next routes [Available only when the firmware is compiled with UWB routing backhaul]</p>
<p><strong>Example:</strong></p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">dwm&gt; lrn</span>
<span class="go">[007021.610 INF] bhn: cnt=9 sf=278 seq=xBB    gn    |   ul_loc   ul_iot |   dl_iot</span>
<span class="go">[007021.610 INF]  0) x0997 : x0997 -&gt; x0D35 : x0D35 |        0        0 |        0</span>
<span class="go">[007021.620 INF]  1) xC5B7 : xC5B7 -&gt; x0D35 : x0D35 |        0        0 |        0</span>
<span class="go">[007021.630 INF]  2)   -   :</span>
<span class="go">[007021.630 INF]  3)   -   :</span>
<span class="go">[007021.630 INF]  4)   -   :</span>
<span class="go">[007021.640 INF]  5)   -   :</span>
<span class="go">[007021.640 INF]  6)   -   :</span>
<span class="go">[007021.640 INF]  7)   -   :</span>
<span class="go">[007021.650 INF]  8)   -   :</span>
<span class="go">[007021.650 INF]</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="nis">
<span id="pp-nis"></span><h2>nis</h2>
<p>Set Network ID</p>
<p><strong>Example:</strong></p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">dwm&gt; nis 0xabcd</span>
<span class="go">nis: ok</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="nls">
<span id="pp-nls"></span><h2>nls</h2>
<p>Sets node label</p>
<hr class="docutils">
</div>
<div class="section" id="stg">
<span id="pp-stg"></span><h2>stg</h2>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 30%">
<col style="width: 70%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head" colspan="2"><p><strong>Displays Statistics</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><strong>Statistic</strong></p></td>
<td><p><strong>Description</strong></p></td>
</tr>
<tr class="row-odd"><td><p>uptime</p></td>
<td><p>System time since restart
in seconds</p></td>
</tr>
<tr class="row-even"><td><p>rtc_drift</p></td>
<td><p>Estimated RTC drift against
the UWB network clock (used
during production)</p></td>
</tr>
<tr class="row-odd"><td><p>ble_con_ok</p></td>
<td><p>Each BLE connect event
increments this counter</p></td>
</tr>
<tr class="row-even"><td><p>ble_dis_ok</p></td>
<td><p>Each BLE disconnect event
increments this counter</p></td>
</tr>
<tr class="row-odd"><td><p>ble_err</p></td>
<td><p>Number that identifies the last
internal BLE error</p></td>
</tr>
<tr class="row-even"><td><p>api_err</p></td>
<td><p>Number that identifies the last
internal API error</p></td>
</tr>
<tr class="row-odd"><td><p>api_err_cnt</p></td>
<td><p>Counter of errors on API</p></td>
</tr>
<tr class="row-even"><td><p>api_dl_cnt</p></td>
<td><p>The number of received backhaul
DownLink packets via API
(GN only)</p></td>
</tr>
<tr class="row-odd"><td><p>uwb0_intr</p></td>
<td><p>The number of interrupts from
the DW1000</p></td>
</tr>
<tr class="row-even"><td><p>uwb0_rst</p></td>
<td><p>The number of attempts to reset
the DW1000 to recover from
error</p></td>
</tr>
<tr class="row-odd"><td><p>uwb0_bpc: 1</p></td>
<td><p>The number of
bandwidth/temperature
compensation</p></td>
</tr>
<tr class="row-even"><td><p>rx_ok</p></td>
<td><p>The number of enabling the
reception on time</p></td>
</tr>
<tr class="row-odd"><td><p>rx_err</p></td>
<td><p>The number of failures to
enable the reception on
time</p></td>
</tr>
<tr class="row-even"><td><p>tx_err</p></td>
<td><p>The number of failures to
enable the transmission on
time</p></td>
</tr>
<tr class="row-odd"><td><p>tx_errx</p></td>
<td><p>The number of errors related
to the TX buffer</p></td>
</tr>
<tr class="row-even"><td><p>bcn_tx_ok</p></td>
<td><p>The number of transmitted
beacons</p></td>
</tr>
<tr class="row-odd"><td><p>bcn_tx_err</p></td>
<td><p>The number of failures during
transmission of beacons</p></td>
</tr>
<tr class="row-even"><td><p>bcn_rx_ok</p></td>
<td><p>The number of received beacons</p></td>
</tr>
<tr class="row-odd"><td><p>alma_tx_ok</p></td>
<td><p>The number of transmitted almanacs</p></td>
</tr>
<tr class="row-even"><td><p>alma_tx_err</p></td>
<td><p>The number of failures during transmission of almanacs</p></td>
</tr>
<tr class="row-odd"><td><p>alma_rx_ok</p></td>
<td><p>The number of received almanacs</p></td>
</tr>
<tr class="row-even"><td><p>cl_rx_ok</p></td>
<td><p>The number of received cluster join</p></td>
</tr>
<tr class="row-odd"><td><p>cl_tx_ok</p></td>
<td><p>The number of transmitted cluster join</p></td>
</tr>
<tr class="row-even"><td><p>cl_coll</p></td>
<td><p>The number of detected cluster collisions</p></td>
</tr>
<tr class="row-odd"><td><p>fwup_tx_ok</p></td>
<td><p>The number of transmitted firmware update frames</p></td>
</tr>
<tr class="row-even"><td><p>fwup_tx_err</p></td>
<td><p>The number of failures to transmit firmware update frames</p></td>
</tr>
<tr class="row-odd"><td><p>fwup_rx_ok</p></td>
<td><p>The number of received firmware update frames</p></td>
</tr>
<tr class="row-even"><td><p>svc_tx_ok</p></td>
<td><p>The number of transmitted service frames</p></td>
</tr>
<tr class="row-odd"><td><p>svc_tx_err</p></td>
<td><p>The number of failures to transmit service frames</p></td>
</tr>
<tr class="row-even"><td><p>svc_rx_ok</p></td>
<td><p>The number of received service frames</p></td>
</tr>
<tr class="row-odd"><td><p>clk_sync</p></td>
<td><p>The number of times the node has synchronized</p></td>
</tr>
<tr class="row-even"><td><p>bh_rt</p></td>
<td><p>The number of times the AN was routing during the routing table switch</p></td>
</tr>
<tr class="row-odd"><td><p>bh_nort</p></td>
<td><p>The number of times the AN was not routing during the routing table switch</p></td>
</tr>
<tr class="row-even"><td><p>bh_ev</p></td>
<td><p>The number of events sent to the DWM Kernel Module</p></td>
</tr>
<tr class="row-odd"><td><p>bh_buf_lost[0]</p></td>
<td><p>The number of lost buffers ready for the Kernel Module</p></td>
</tr>
<tr class="row-even"><td><p>bh_buf_lost[1]</p></td>
<td><p>The number of lost buffers ready for the Kernel Module</p></td>
</tr>
<tr class="row-odd"><td><p>bh_tx_err</p></td>
<td><p>The number of failures to transmit backhaul frames</p></td>
</tr>
<tr class="row-even"><td><p>bh_dl_err</p></td>
<td><p>The number of failures during processing of downlink backhaul frames</p></td>
</tr>
<tr class="row-odd"><td><p>bh_dl_ok</p></td>
<td><p>The number of received downlink backhaul frames</p></td>
</tr>
<tr class="row-even"><td><p>bh_ul_err</p></td>
<td><p>The number of failures during processing of uplink backhaul frames</p></td>
</tr>
<tr class="row-odd"><td><p>bh_ul_ok</p></td>
<td><p>The number of received uplink backhaul frames</p></td>
</tr>
<tr class="row-even"><td><p>fw_dl_tx_err</p></td>
<td><p>The number of failures during sending downlink data to the edge nodes</p></td>
</tr>
<tr class="row-odd"><td><p>fw_dl_iot_ok</p></td>
<td><p>The number of sent downlink data to the edge nodes</p></td>
</tr>
<tr class="row-even"><td><p>fw_ul_loc_ok</p></td>
<td><p>The number of received uplink location data from the edge nodes</p></td>
</tr>
<tr class="row-odd"><td><p>fw_ul_iot_ok</p></td>
<td><p>The number of received uplink IoT data from the edge nodes</p></td>
</tr>
<tr class="row-even"><td><p>ul_tx_err</p></td>
<td><p>The number of failures during sending uplink data from the edge node</p></td>
</tr>
<tr class="row-odd"><td><p>dl_iot_ok</p></td>
<td><p>The number of sent downlink data to the edge node</p></td>
</tr>
<tr class="row-even"><td><p>ul_loc_ok</p></td>
<td><p>The number of received uplink location data from the edge node</p></td>
</tr>
<tr class="row-odd"><td><p>ul_iot_ok</p></td>
<td><p>The number of received uplink IoT data from the edge nodes</p></td>
</tr>
<tr class="row-even"><td><p>enc_err</p></td>
<td><p>The number of encryption errors</p></td>
</tr>
<tr class="row-odd"><td><p>reinit</p></td>
<td><p>The number of node reinitialization</p></td>
</tr>
<tr class="row-even"><td><p>twr_ok</p></td>
<td><p>The number of succeeded TWR cycle</p></td>
</tr>
<tr class="row-odd"><td><p>twr_err</p></td>
<td><p>The number of failed TWR cycle</p></td>
</tr>
<tr class="row-even"><td><p>res[0] x00000000</p></td>
<td><p>Reserved</p></td>
</tr>
<tr class="row-odd"><td><p>res[1] x00000000</p></td>
<td><p>Reserved</p></td>
</tr>
<tr class="row-even"><td><p>res[2] x00000000</p></td>
<td><p>Reserved</p></td>
</tr>
<tr class="row-odd"><td><p>res[3] x00000000</p></td>
<td><p>Reserved</p></td>
</tr>
<tr class="row-even"><td><p>res[4] x00000000</p></td>
<td><p>Reserved</p></td>
</tr>
<tr class="row-odd"><td><p>res[5] x00000000</p></td>
<td><p>Reserved</p></td>
</tr>
</tbody>
</table>
<p><strong>Example:</strong></p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">dwm&gt; stg</span>
<span class="go">uptime: 6146</span>
<span class="go">rtc_drift: 0.000000</span>
<span class="go">ble_con_ok: 0</span>
<span class="go">ble_dis_ok: 0</span>
<span class="go">ble_err: 0</span>
<span class="go">api_err: 0</span>
<span class="go">api_err_cnt: 0</span>
<span class="go">api_dl_cnt: 0</span>
<span class="go">uwb0_intr: 3927517</span>
<span class="go">uwb0_rst: 0</span>
<span class="go">uwb0_bpc: 0</span>
<span class="go">rx_ok: 3863996</span>
<span class="go">rx_err: 4</span>
<span class="go">tx_err: 0</span>
<span class="go">tx_errx: 0</span>
<span class="go">bcn_tx_ok: 61332</span>
<span class="go">bcn_tx_err: 0</span>
<span class="go">bcn_rx_ok: 61320</span>
<span class="go">alma_tx_ok: 1095</span>
<span class="go">alma_tx_err: 0</span>
<span class="go">alma_rx_ok: 0</span>
<span class="go">cl_rx_ok: 0</span>
<span class="go">cl_tx_ok: 1</span>
<span class="go">cl_coll: 0</span>
<span class="go">fwup_tx_ok: 0</span>
<span class="go">fwup_tx_err: 0</span>
<span class="go">fwup_rx_ok: 0</span>
<span class="go">svc_tx_ok: 0</span>
<span class="go">svc_tx_err: 0</span>
<span class="go">svc_rx_ok: 0</span>
<span class="go">clk_sync: 0</span>
<span class="go">bh_rt: 0</span>
<span class="go">bh_nort: 0</span>
<span class="go">bh_ev: 0</span>
<span class="go">bh_buf_lost[0]: 0</span>
<span class="go">bh_buf_lost[1]: 0</span>
<span class="go">bh_tx_err: 0</span>
<span class="go">bh_dl_err: 0</span>
<span class="go">bh_dl_ok: 0</span>
<span class="go">bh_ul_err: 0</span>
<span class="go">bh_ul_ok: 0</span>
<span class="go">fw_dl_tx_err: 0</span>
<span class="go">fw_dl_iot_ok: 0</span>
<span class="go">fw_ul_loc_ok: 0</span>
<span class="go">fw_ul_iot_ok: 0</span>
<span class="go">ul_tx_err: 0</span>
<span class="go">dl_iot_ok: 0</span>
<span class="go">ul_loc_ok: 0</span>
<span class="go">ul_iot_ok: 1096</span>
<span class="go">enc_err: 0</span>
<span class="go">reinit: 1</span>
<span class="go">twr_ok: 0</span>
<span class="go">twr_err: 0</span>
<span class="go">res[0]: 0 x00000000</span>
<span class="go">res[1]: 0 x00000000</span>
<span class="go">res[2]: 0 x00000000</span>
<span class="go">res[3]: 0 x00000000</span>
<span class="go">res[4]: 0 x00000000</span>
<span class="go">res[5]: 0 x00000000</span>
<span class="go">tot_err: 4</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="stc">
<span id="pp-stc"></span><h2>stc</h2>
<p>Clears statistics.</p>
<p>Example:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">dwm&gt; stc</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="udi">
<span id="pp-udi"></span><h2>udi</h2>
<p>Toggles displaying of IoT data received via backhaul.</p>
<p>Example:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">dwm&gt; udi</span>
<span class="go">dl: show on</span>
<span class="go">dl: len=8: 01 23 45 67 89 AB CD EF</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="uui">
<span id="pp-uui"></span><h2>uui</h2>
<p>Sends IoT data via backhaul.</p>
<p>Example:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">dwm&gt; uui</span>
<span class="go">usage: uui &lt;hex_string&gt; [cnt]</span>
<span class="go">dwm&gt; uui 11223344 100</span>
<span class="go">ul: len=4 cnt=100 rv=4:  11 22 33 44</span>
</pre></div>
</div>
</div>
</div>


           </div>
