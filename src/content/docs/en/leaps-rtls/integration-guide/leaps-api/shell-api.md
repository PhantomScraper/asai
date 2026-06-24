---
title: "Shell API"
lang: en
slug: "leaps-rtls/integration-guide/leaps-api/shell-api"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/leaps-rtls/integration-guide/leaps-api/shell-api/"
order: 115
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="shell-api">
<span id="leaps-shell-api"></span><h1>Shell API</h1>
<p><strong>UART Interface</strong></p>
<p>Shell uses the UART interface, which can also work in binary mode. The binary
mode is used to read API commands in TLV format. The module starts by
default in binary mode after reset. The shell mode can be entered by
pressing ENTER twice within one second. The binary mode can be entered by
executing command <a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/base#quit"><span class="std std-ref">quit</span></a> in shell mode. The shell mode and the
binary mode can be switched back and forth.</p>
<p><strong>Supported Commands</strong></p>
<div class="admonition tip">
<p class="admonition-title">Tip</p>
<p>Press Enter to repeat the last command</p>
</div>
<hr class="docutils">
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 15%">
<col style="width: 63%">
<col style="width: 21%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>Command</strong></p></th>
<th class="head"><p><strong>Description</strong></p></th>
<th class="head"><p><strong>Example</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td colspan="3"><p>Command group: <strong>Base</strong></p></td>
</tr>
<tr class="row-odd"><td><p>?</p></td>
<td><p>this help</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/base#helpm"><span class="std std-ref">?</span></a></p></td>
</tr>
<tr class="row-even"><td><p>help</p></td>
<td><p>this help</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/base#id1"><span class="std std-ref">help</span></a></p></td>
</tr>
<tr class="row-odd"><td><p>quit</p></td>
<td><p>quit</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/base#quit"><span class="std std-ref">quit</span></a></p></td>
</tr>
<tr class="row-even"><td colspan="3"><p>Command group: <strong>SYS</strong></p></td>
</tr>
<tr class="row-odd"><td><p>reset</p></td>
<td><p>Reboot the system</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/sys#reset"><span class="std std-ref">reset</span></a></p></td>
</tr>
<tr class="row-even"><td><p>frst</p></td>
<td><p>Factory reset</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/sys#frst"><span class="std std-ref">frst</span></a></p></td>
</tr>
<tr class="row-odd"><td><p>si</p></td>
<td><p>System info</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/sys#si"><span class="std std-ref">si</span></a></p></td>
</tr>
<tr class="row-even"><td><p>f</p></td>
<td><p>Show free memory on the heap</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/sys#f"><span class="std std-ref">f</span></a></p></td>
</tr>
<tr class="row-odd"><td><p>stg</p></td>
<td><p>Get stats</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/sys#stg"><span class="std std-ref">stg</span></a></p></td>
</tr>
<tr class="row-even"><td><p>stc</p></td>
<td><p>Clear stats</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/sys#stc"><span class="std std-ref">stc</span></a></p></td>
</tr>
<tr class="row-odd"><td><p>rbv</p></td>
<td><p>Read battery voltage</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/sys#rbv"><span class="std std-ref">rbv</span></a></p></td>
</tr>
<tr class="row-even"><td><p>rcs</p></td>
<td><p>Read charger status</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/sys#rcs"><span class="std std-ref">rcs</span></a></p></td>
</tr>
<tr class="row-odd"><td><p>ut</p></td>
<td><p>Show device uptime</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/sys#ut"><span class="std std-ref">ut</span></a></p></td>
</tr>
<tr class="row-even"><td><p>sbl</p></td>
<td><p>Set the battery voltage level</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/sys#sbl"><span class="std std-ref">sbl</span></a></p></td>
</tr>
<tr class="row-odd"><td colspan="3"><p>Command group: <strong>SYS</strong></p></td>
</tr>
<tr class="row-even"><td><p>gc</p></td>
<td><p>GPIO clear</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/gpio#gc"><span class="std std-ref">gc</span></a></p></td>
</tr>
<tr class="row-odd"><td><p>gg</p></td>
<td><p>GPIO get</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/gpio#gg"><span class="std std-ref">gg</span></a></p></td>
</tr>
<tr class="row-even"><td><p>gs</p></td>
<td><p>GPIO set</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/gpio#gs"><span class="std std-ref">gs</span></a></p></td>
</tr>
<tr class="row-odd"><td><p>gt</p></td>
<td><p>GPIO toggle</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/gpio#gt"><span class="std std-ref">gt</span></a></p></td>
</tr>
<tr class="row-even"><td colspan="3"><p>Command group: <strong>SENS</strong></p></td>
</tr>
<tr class="row-odd"><td><p>twi</p></td>
<td><p>General purpose TWI read</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/sens#twi"><span class="std std-ref">twi</span></a></p></td>
</tr>
<tr class="row-even"><td><p>aid</p></td>
<td><p>Read ACC device ID</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/sens#aid"><span class="std std-ref">aid</span></a></p></td>
</tr>
<tr class="row-odd"><td><p>av</p></td>
<td><p>Read ACC values</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/sens#av"><span class="std std-ref">av</span></a></p></td>
</tr>
<tr class="row-even"><td><p>scs</p></td>
<td><p>Stationary config set</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/sens#scs"><span class="std std-ref">scs</span></a></p></td>
</tr>
<tr class="row-odd"><td><p>scg</p></td>
<td><p>Stationary config get</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/sens#scg"><span class="std std-ref">scg</span></a></p></td>
</tr>
<tr class="row-even"><td colspan="3"><p>Command group: <strong>LE</strong></p></td>
</tr>
<tr class="row-odd"><td><p>les</p></td>
<td><p>Show meas. and pos.</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/le#les"><span class="std std-ref">les</span></a></p></td>
</tr>
<tr class="row-even"><td><p>lec</p></td>
<td><p>Show meas. and pos. in CSV</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/le#lec"><span class="std std-ref">lec</span></a></p></td>
</tr>
<tr class="row-odd"><td><p>lep</p></td>
<td><p>Show pos. in CSV</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/le#lep"><span class="std std-ref">lep</span></a></p></td>
</tr>
<tr class="row-even"><td><p>lej</p></td>
<td><p>Show pos. in JSON</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/le#lej"><span class="std std-ref">lej</span></a></p></td>
</tr>
<tr class="row-odd"><td><p>lea</p></td>
<td><p>how meas., pos. and pdoa</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/le#lea"><span class="std std-ref">lea</span></a></p></td>
</tr>
<tr class="row-even"><td colspan="3"><p>Command group: <strong>UWB</strong></p></td>
</tr>
<tr class="row-odd"><td><p>ucs</p></td>
<td><p>Set UWB channel and compliance</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/uwb#ucs"><span class="std std-ref">ucs</span></a></p></td>
</tr>
<tr class="row-even"><td><p>utpg</p></td>
<td><p>Get TxPwr</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/uwb#utpg"><span class="std std-ref">utpg</span></a></p></td>
</tr>
<tr class="row-odd"><td><p>utps</p></td>
<td><p>Set TxPwr</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/uwb#utps"><span class="std std-ref">utps</span></a></p></td>
</tr>
<tr class="row-even"><td><p>ufs</p></td>
<td><p>UWB Frontend Set</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/uwb#ufs"><span class="std std-ref">ufs</span></a></p></td>
</tr>
<tr class="row-odd"><td><p>ucls</p></td>
<td><p>Set BLE Adv UWB counter low water mark</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/uwb#ucls"><span class="std std-ref">ucls</span></a></p></td>
</tr>
<tr class="row-even"><td><p>uclg</p></td>
<td><p>Get BLE Adv UWB counter low water mark</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/uwb#uclg"><span class="std std-ref">uclg</span></a></p></td>
</tr>
<tr class="row-odd"><td colspan="3"><p>Command group: <strong>UWBMAC</strong></p></td>
</tr>
<tr class="row-even"><td><p>nmo</p></td>
<td><p>Set UWB mode to off</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/uwbmac#nmo"><span class="std std-ref">nmo</span></a></p></td>
</tr>
<tr class="row-odd"><td><p>nmp</p></td>
<td><p>Set UWB mode to passive</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/uwbmac#nmp"><span class="std std-ref">nmp</span></a></p></td>
</tr>
<tr class="row-even"><td><p>nma</p></td>
<td><p>Set mode to AN</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/uwbmac#nma"><span class="std std-ref">nma</span></a></p></td>
</tr>
<tr class="row-odd"><td><p>nmi</p></td>
<td><p>Set mode to ANI</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/uwbmac#nmi"><span class="std std-ref">nmi</span></a></p></td>
</tr>
<tr class="row-even"><td><p>nmt</p></td>
<td><p>Set mode to TN</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/uwbmac#nmt"><span class="std std-ref">nmt</span></a></p></td>
</tr>
<tr class="row-odd"><td><p>nmtl</p></td>
<td><p>Set mode to TN-LP</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/uwbmac#nmtl"><span class="std std-ref">nmtl</span></a></p></td>
</tr>
<tr class="row-even"><td><p>nmg</p></td>
<td><p>Set mode to GN</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/uwbmac#nmg"><span class="std std-ref">nmg</span></a></p></td>
</tr>
<tr class="row-odd"><td><p>ln</p></td>
<td><p>Show node list</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/uwbmac#ln"><span class="std std-ref">ln</span></a></p></td>
</tr>
<tr class="row-even"><td><p>la</p></td>
<td><p>Show AN list</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/uwbmac#la"><span class="std std-ref">la</span></a></p></td>
</tr>
<tr class="row-odd"><td><p>nis</p></td>
<td><p>Set Network ID</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/uwbmac#nis"><span class="std std-ref">nis</span></a></p></td>
</tr>
<tr class="row-even"><td><p>nls</p></td>
<td><p>Set node label</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/uwbmac#nls"><span class="std std-ref">nls</span></a></p></td>
</tr>
<tr class="row-odd"><td><p>nps</p></td>
<td><p>Set network profile</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/uwbmac#nps"><span class="std std-ref">nps</span></a></p></td>
</tr>
<tr class="row-even"><td><p>udi</p></td>
<td><p>Show incoming IoT data</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/uwbmac#udi"><span class="std std-ref">udi</span></a></p></td>
</tr>
<tr class="row-odd"><td><p>uui</p></td>
<td><p>Send IoT data</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/uwbmac#uui"><span class="std std-ref">uui</span></a></p></td>
</tr>
<tr class="row-even"><td><p>usps</p></td>
<td><p>Set pulse per superframe cycle. Example: 50 means 1
pulse per 50 superframe</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/uwbmac#usps"><span class="std std-ref">usps</span></a></p></td>
</tr>
<tr class="row-odd"><td><p>uspg</p></td>
<td><p>Get pulse per superframe cycle.</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/uwbmac#uspg"><span class="std std-ref">uspg</span></a></p></td>
</tr>
<tr class="row-even"><td colspan="3"><p>Command group: <strong>API</strong></p></td>
</tr>
<tr class="row-odd"><td><p>urs</p></td>
<td><p>Set update rate</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/api#urs"><span class="std std-ref">urs</span></a></p></td>
</tr>
<tr class="row-even"><td><p>urg</p></td>
<td><p>Get update rate</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/api#urg"><span class="std std-ref">urg</span></a></p></td>
</tr>
<tr class="row-odd"><td><p>tcs</p></td>
<td><p>Set tag config</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/api#tcs"><span class="std std-ref">tcs</span></a></p></td>
</tr>
<tr class="row-even"><td><p>tlv</p></td>
<td><p>Send TLV frame</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/api#tlv"><span class="std std-ref">tlv</span></a></p></td>
</tr>
<tr class="row-odd"><td><p>tlvr</p></td>
<td><p>Cmd as TLV frame with manual CRC</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/api#tlvr"><span class="std std-ref">tlvr</span></a></p></td>
</tr>
<tr class="row-even"><td><p>ums</p></td>
<td><p>Set default UART mode</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/api#ums"><span class="std std-ref">ums</span></a></p></td>
</tr>
<tr class="row-odd"><td><p>ana</p></td>
<td><p>Set MAC address</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/api#ana"><span class="std std-ref">ana</span></a></p></td>
</tr>
<tr class="row-even"><td><p>amlg</p></td>
<td><p>Get MAC address list.</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/api#amlg"><span class="std std-ref">amlg</span></a></p></td>
</tr>
<tr class="row-odd"><td><p>mrs</p></td>
<td><p>Set mesh random timing</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/api#mrs"><span class="std std-ref">mrs</span></a></p></td>
</tr>
<tr class="row-even"><td><p>mrg</p></td>
<td><p>Get mesh random timing</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/api#mrg"><span class="std std-ref">mrg</span></a></p></td>
</tr>
<tr class="row-odd"><td><p>dacs</p></td>
<td><p>Distance alarm set</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/api#dacs"><span class="std std-ref">dacs</span></a></p></td>
</tr>
<tr class="row-even"><td><p>dacg</p></td>
<td><p>Distance alarm get</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/api#dacg"><span class="std std-ref">dacg</span></a></p></td>
</tr>
<tr class="row-odd"><td><p>acs</p></td>
<td><p>Configure node</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/api#acs"><span class="std std-ref">acs</span></a></p></td>
</tr>
<tr class="row-even"><td><p>pg</p></td>
<td><p>Get the position</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/api#pg"><span class="std std-ref">pg</span></a></p></td>
</tr>
<tr class="row-odd"><td><p>ps</p></td>
<td><p>Set the position</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/api#ps"><span class="std std-ref">ps</span></a></p></td>
</tr>
<tr class="row-even"><td><p>fls</p></td>
<td><p>Filter config set</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/api#fls"><span class="std std-ref">fls</span></a></p></td>
</tr>
<tr class="row-odd"><td><p>flg</p></td>
<td><p>Get filters</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/api#flg"><span class="std std-ref">flg</span></a></p></td>
</tr>
<tr class="row-even"><td><p>ahs</p></td>
<td><p>Set HW version once</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/api#ahs"><span class="std std-ref">ahs</span></a></p></td>
</tr>
<tr class="row-odd"><td><p>eks</p></td>
<td><p>Set encryption key</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/api#eks"><span class="std std-ref">eks</span></a></p></td>
</tr>
<tr class="row-even"><td><p>ekc</p></td>
<td><p>Clear encryption key</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/api#ekc"><span class="std std-ref">ekc</span></a></p></td>
</tr>
<tr class="row-odd"><td><p>amls</p></td>
<td><p>Set MAC addr list once</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/api#amls"><span class="std std-ref">amls</span></a></p></td>
</tr>
<tr class="row-even"><td colspan="3"><p>Command group: <strong>INET</strong></p></td>
</tr>
<tr class="row-odd"><td><p>ipv4</p></td>
<td><p>Set local IPv4</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/inet#ipv4"><span class="std std-ref">ipv4</span></a></p></td>
</tr>
<tr class="row-even"><td><p>peer</p></td>
<td><p>Set server IPv4</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/inet#peer"><span class="std std-ref">peer</span></a></p></td>
</tr>
<tr class="row-odd"><td><p>wifi</p></td>
<td><p>Set WIFI configuration</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/inet#wifi"><span class="std std-ref">wifi</span></a></p></td>
</tr>
<tr class="row-even"><td><p>dns</p></td>
<td><p>Set DNS server IP address list</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/inet#dns"><span class="std std-ref">dns</span></a></p></td>
</tr>
<tr class="row-odd"><td><p>switch</p></td>
<td><p>Set net switch configuration</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/inet#switch"><span class="std std-ref">switch</span></a></p></td>
</tr>
<tr class="row-even"><td colspan="3"><p>Command group: <strong>HAWKBIT</strong></p></td>
</tr>
<tr class="row-odd"><td><p>hb_peer</p></td>
<td><p>Set Hawkbit server IPv4</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/hawkbit#hb-peer"><span class="std std-ref">hb_peer</span></a></p></td>
</tr>
<tr class="row-even"><td><p>hb_token</p></td>
<td><p>Set Hawkbit auth token</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/hawkbit#hb-token"><span class="std std-ref">hb_token</span></a></p></td>
</tr>
<tr class="row-odd"><td colspan="3"><p>Command group: <strong>BDG</strong></p></td>
</tr>
<tr class="row-even"><td><p>utlv</p></td>
<td><p>Cmd as TLV frame for UWB Subsystem</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/bdg#utlv"><span class="std std-ref">utlv</span></a></p></td>
</tr>
<tr class="row-odd"><td colspan="3"><p>Command group: <strong>FiRa</strong></p></td>
</tr>
<tr class="row-even"><td><p>fniq</p></td>
<td><p>Configure the device to FiRa UWB Sub-System Nearby Interaction mode.</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/fira#fniq"><span class="std std-ref">fniq</span></a></p></td>
</tr>
<tr class="row-odd"><td><p>fuci</p></td>
<td><p>Configure the device to FiRa UWB Sub-System UCI mode.</p></td>
<td><p><a class="reference internal" href="/docs/en/leaps-rtls/integration-guide/shell-api/fira#fuci"><span class="std std-ref">fuci</span></a></p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
<div class="toctree-wrapper compound">
</div>
</div>


           </div>
