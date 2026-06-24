---
title: "Shell API"
lang: en
slug: "pans-pro-rtls/integration-guide/shell-api"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/pans-pro-rtls/integration-guide/shell-api/"
order: 123
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="shell-api">
<h1>Shell API</h1>
<p>Shell uses a UART interface that can also work in binary mode. The binary mode is used to read API commands in TLV format.
DWM starts by default in binary mode after reset. The shell mode can be switched to by pressing ENTER twice within 1 second.
The binary mode can be switched to by executing the command “quit” in shell mode.
The shell mode and the binary mode can be switched back and forth.
Press Enter in shell mode to repeat the last command. The following text provides an overview of the shell commands.</p>
<hr class="docutils">
<p>The following table gives an overview of the availability of the shell commands on the ethernet gateway and the edge node.</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 27%">
<col style="width: 46%">
<col style="width: 13%">
<col style="width: 13%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>Command</strong></p></th>
<th class="head"><p><strong>Description</strong></p></th>
<th class="head"><p><strong>DWM1001</strong></p></th>
<th class="head"><p><strong>Gateway</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/shell-api/base#pp-helpm"><span class="std std-ref">?</span></a></p></td>
<td><p>this help</p></td>
<td><p>YES</p></td>
<td><p>YES</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/shell-api/base#pp-help"><span class="std std-ref">help</span></a></p></td>
<td><p>this help</p></td>
<td><p>YES</p></td>
<td><p>YES</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/shell-api/base#pp-quit"><span class="std std-ref">quit</span></a></p></td>
<td><p>quit</p></td>
<td><p>YES</p></td>
<td><p>YES</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/shell-api/gpio#pp-gc"><span class="std std-ref">gc</span></a></p></td>
<td><p>GPIO clear</p></td>
<td><p>YES</p></td>
<td><p>YES</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/shell-api/gpio#pp-gg"><span class="std std-ref">gg</span></a></p></td>
<td><p>GPIO get</p></td>
<td><p>YES</p></td>
<td><p>YES</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/shell-api/gpio#pp-gs"><span class="std std-ref">gs</span></a></p></td>
<td><p>GPIO set</p></td>
<td><p>YES</p></td>
<td><p>YES</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/shell-api/gpio#pp-gt"><span class="std std-ref">gt</span></a></p></td>
<td><p>GPIO toggle</p></td>
<td><p>YES</p></td>
<td><p>YES</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/shell-api/sys#pp-f"><span class="std std-ref">f</span></a></p></td>
<td><p>Show free memory on the heap</p></td>
<td><p>YES</p></td>
<td><p>YES</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/shell-api/sys#pp-reset"><span class="std std-ref">reset</span></a></p></td>
<td><p>Reboot the system</p></td>
<td><p>YES</p></td>
<td><p>YES</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/shell-api/sys#pp-si"><span class="std std-ref">si</span></a></p></td>
<td><p>System info</p></td>
<td><p>YES</p></td>
<td><p>YES</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/shell-api/sys#pp-ut"><span class="std std-ref">ut</span></a></p></td>
<td><p>Show device uptime</p></td>
<td><p>YES</p></td>
<td><p>YES</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/shell-api/sys#pp-sbl"><span class="std std-ref">sbl</span></a></p></td>
<td><p>Set the battery voltage level</p></td>
<td><p>YES</p></td>
<td><p>YES</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/shell-api/sys#pp-frst"><span class="std std-ref">frst</span></a></p></td>
<td><p>Factory reset</p></td>
<td><p>YES</p></td>
<td><p>YES</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/shell-api/sens#pp-twi"><span class="std std-ref">twi</span></a></p></td>
<td><p>General purpose TWI read</p></td>
<td><p>YES</p></td>
<td><p>NO</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/shell-api/sens#pp-aid"><span class="std std-ref">aid</span></a></p></td>
<td><p>Read ACC device ID</p></td>
<td><p>YES</p></td>
<td><p>NO</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/shell-api/sens#pp-av"><span class="std std-ref">av</span></a></p></td>
<td><p>Read ACC values</p></td>
<td><p>YES</p></td>
<td><p>NO</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/shell-api/sens#pp-scs"><span class="std std-ref">scs</span></a></p></td>
<td><p>Stationary config set</p></td>
<td><p>YES</p></td>
<td><p>NO</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/shell-api/sens#pp-scg"><span class="std std-ref">scg</span></a></p></td>
<td><p>Stationary config get</p></td>
<td><p>YES</p></td>
<td><p>NO</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/shell-api/le#pp-les"><span class="std std-ref">les</span></a></p></td>
<td><p>Show meas. and pos.</p></td>
<td><p>YES</p></td>
<td><p>NO</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/shell-api/le#pp-lec"><span class="std std-ref">lec</span></a></p></td>
<td><p>Show meas. and pos. in CSV</p></td>
<td><p>YES</p></td>
<td><p>NO</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/shell-api/le#pp-lep"><span class="std std-ref">lep</span></a></p></td>
<td><p>Show pos. in CSV</p></td>
<td><p>YES</p></td>
<td><p>NO</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/shell-api/uwb#pp-utpg"><span class="std std-ref">utpg</span></a></p></td>
<td><p>Get TxPwr</p></td>
<td><p>YES</p></td>
<td><p>NO</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/shell-api/uwb#pp-utps"><span class="std std-ref">utps</span></a></p></td>
<td><p>Set TxPwr</p></td>
<td><p>YES</p></td>
<td><p>NO</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/shell-api/uwbmac#pp-nmp"><span class="std std-ref">nmp</span></a></p></td>
<td><p>Set UWB mode to passive</p></td>
<td><p>YES</p></td>
<td><p>NO</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/shell-api/uwbmac#pp-nmo"><span class="std std-ref">nmo</span></a></p></td>
<td><p>Set UWB mode to off</p></td>
<td><p>YES</p></td>
<td><p>YES</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/shell-api/uwbmac#pp-nma"><span class="std std-ref">nma</span></a></p></td>
<td><p>Set mode to AN</p></td>
<td><p>YES</p></td>
<td><p>NO</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/shell-api/uwbmac#pp-nmi"><span class="std std-ref">nmi</span></a></p></td>
<td><p>Set mode to ANI</p></td>
<td><p>YES</p></td>
<td><p>NO</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/shell-api/uwbmac#pp-nmt"><span class="std std-ref">nmt</span></a></p></td>
<td><p>Set mode to TN</p></td>
<td><p>YES</p></td>
<td><p>NO</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/shell-api/uwbmac#pp-nmtl"><span class="std std-ref">nmtl</span></a></p></td>
<td><p>Set mode to TN-LP</p></td>
<td><p>YES</p></td>
<td><p>NO</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/shell-api/uwbmac#pp-nmg"><span class="std std-ref">nmg</span></a></p></td>
<td><p>Set mode to GN</p></td>
<td><p>YES</p></td>
<td><p>YES</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/shell-api/uwbmac#pp-la"><span class="std std-ref">la</span></a></p></td>
<td><p>Show AN list</p></td>
<td><p>YES</p></td>
<td><p>NO</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/shell-api/uwbmac#pp-lg"><span class="std std-ref">lg</span></a></p></td>
<td><p>Show GN list</p></td>
<td><p>YES</p></td>
<td><p>NO</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/shell-api/uwbmac#pp-nis"><span class="std std-ref">nis</span></a></p></td>
<td><p>Set Network ID</p></td>
<td><p>YES</p></td>
<td><p>YES</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/shell-api/uwbmac#pp-nls"><span class="std std-ref">nls</span></a></p></td>
<td><p>Set node label</p></td>
<td><p>YES</p></td>
<td><p>YES</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/shell-api/uwbmac#pp-udi"><span class="std std-ref">udi</span></a></p></td>
<td><p>Show incoming IoT data</p></td>
<td><p>YES</p></td>
<td><p>NO</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/shell-api/uwbmac#pp-uui"><span class="std std-ref">uui</span></a></p></td>
<td><p>Send IoT data</p></td>
<td><p>YES</p></td>
<td><p>NO</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/shell-api/uwbmac#pp-stg"><span class="std std-ref">stg</span></a></p></td>
<td><p>Get stats</p></td>
<td><p>YES</p></td>
<td><p>YES</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/shell-api/uwbmac#pp-stc"><span class="std std-ref">stc</span></a></p></td>
<td><p>Clear stats</p></td>
<td><p>YES</p></td>
<td><p>YES</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/shell-api/api#pp-tlv"><span class="std std-ref">tlv</span></a></p></td>
<td><p>Send TLV frame</p></td>
<td><p>YES</p></td>
<td><p>YES</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/shell-api/api#pp-aurs"><span class="std std-ref">aurs</span></a></p></td>
<td><p>Set upd rate</p></td>
<td><p>YES</p></td>
<td><p>NO</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/shell-api/api#pp-aurg"><span class="std std-ref">aurg</span></a></p></td>
<td><p>Get upd rate</p></td>
<td><p>YES</p></td>
<td><p>NO</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/shell-api/api#pp-apg"><span class="std std-ref">apg</span></a></p></td>
<td><p>Get pos</p></td>
<td><p>YES</p></td>
<td><p>NO</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/shell-api/api#pp-aps"><span class="std std-ref">aps</span></a></p></td>
<td><p>Set pos</p></td>
<td><p>YES</p></td>
<td><p>NO</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/shell-api/api#pp-acas"><span class="std std-ref">acas</span></a></p></td>
<td><p>Set anchor
config</p></td>
<td><p>YES</p></td>
<td><p>NO</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/shell-api/api#pp-acts"><span class="std std-ref">acts</span></a></p></td>
<td><p>Set tag config</p></td>
<td><p>YES</p></td>
<td><p>NO</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/shell-api/api#pp-aks"><span class="std std-ref">aks</span></a></p></td>
<td><p>Set encryption
key</p></td>
<td><p>YES</p></td>
<td><p>NO</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/shell-api/api#pp-akc"><span class="std std-ref">akc</span></a></p></td>
<td><p>Clear
encryption key</p></td>
<td><p>YES</p></td>
<td><p>NO</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/shell-api/api#pp-ans"><span class="std std-ref">ans</span></a></p></td>
<td><p>Set NVM usr
data</p></td>
<td><p>YES</p></td>
<td><p>NO</p></td>
</tr>
<tr class="row-even"><td><p>anc (not found example)</p></td>
<td><p>Clear NVM usr
data</p></td>
<td><p>YES</p></td>
<td><p>NO</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/shell-api/api#pp-ang"><span class="std std-ref">ang</span></a></p></td>
<td><p>Get NVM usr
data</p></td>
<td><p>YES</p></td>
<td><p>NO</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/shell-api/gateway#pp-amls"><span class="std std-ref">amls</span></a></p></td>
<td><p>Set MAC addr
list once</p></td>
<td><p>YES</p></td>
<td><p>NO</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/shell-api/gateway#pp-amlg"><span class="std std-ref">amlg</span></a></p></td>
<td><p>Get MAC addr
list</p></td>
<td><p>YES</p></td>
<td><p>NO</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/shell-api/gateway#pp-ahs"><span class="std std-ref">ahs</span></a></p></td>
<td><p>Set HW version
once</p></td>
<td><p>YES</p></td>
<td><p>NO</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/shell-api/gateway#pp-ana"><span class="std std-ref">ana</span></a></p></td>
<td><p>Set MAC address</p></td>
<td><p>YES</p></td>
<td><p>NO</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/shell-api/gateway#pp-acs"><span class="std std-ref">acs</span></a></p></td>
<td><p>Configure node</p></td>
<td><p>NO</p></td>
<td><p>YES</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/shell-api/gateway#pp-ums"><span class="std std-ref">ums</span></a></p></td>
<td><p>Set default
UART mode</p></td>
<td><p>NO</p></td>
<td><p>YES</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/shell-api/gateway#pp-ipv4"><span class="std std-ref">ipv4</span></a></p></td>
<td><p>Set local IPv4</p></td>
<td><p>NO</p></td>
<td><p>YES</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/en/pans-pro-rtls/integration-guide/shell-api/gateway#pp-dns"><span class="std std-ref">dns</span></a></p></td>
<td><p>Set DNS server
IP address list</p></td>
<td><p>NO</p></td>
<td><p>YES</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
<div class="toctree-wrapper compound">
</div>
</div>


           </div>
