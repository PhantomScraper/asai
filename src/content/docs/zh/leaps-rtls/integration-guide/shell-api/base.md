---
title: "基地"
lang: zh
slug: "leaps-rtls/integration-guide/shell-api/base"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/zh-cn/leaps-rtls/integration-guide/shell-api/base/"
order: 134
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="base">
<h1>基地</h1>
<hr class="docutils">
<div class="section" id="help">
<span id="helpm"></span><h2>?(帮助)</h2>
<p>显示帮助。</p>
<p>示例:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; ?</span>
<span class="go">Usage: &lt;command&gt; [arg0] [arg1] ...</span>
<span class="go">Build-in commands:</span>

<span class="go">** Command group: Base **</span>
<span class="go">?: this help</span>
<span class="go">help: this help</span>
<span class="go">quit: quit</span>

<span class="go">** Command group: SYS **</span>
<span class="go">reset: Reboot the system</span>
<span class="go">frst: Factory reset</span>
<span class="go">si: System info</span>
<span class="go">f: Show free memory on the heap</span>
<span class="go">stg: Get stats</span>
<span class="go">stc: Clear stats</span>
<span class="go">rbv: Read battery voltage</span>
<span class="go">rcs: Read charger status</span>
<span class="go">sbl: Set the battery levels</span>
<span class="go">ut: Show device uptime</span>

<span class="go">** Command group: GPIO **</span>
<span class="go">gc: GPIO clear</span>
<span class="go">gg: GPIO get</span>
<span class="go">gs: GPIO set</span>
<span class="go">gt: GPIO toggle</span>

<span class="go">** Command group: SENS **</span>
<span class="go">twi: General purpose TWI read</span>
<span class="go">aid: Read ACC device ID</span>
<span class="go">av: Read ACC values</span>
<span class="go">scs: Stationary config set</span>
<span class="go">scg: Stationary config get</span>

<span class="go">** Command group: LE **</span>
<span class="go">les: Show meas. and pos.</span>
<span class="go">lec: Show meas. and pos. in CSV</span>
<span class="go">lep: Show pos. in CSV</span>
<span class="go">lej: Show pos. in JSON</span>
<span class="go">lea: Show meas., pos. and pdoa</span>

<span class="go">** Command group: UWB **</span>
<span class="go">ucs: Set UWB channel and compliance</span>
<span class="go">utpg: Get TxPwr</span>
<span class="go">utps: Set TxPwr</span>
<span class="go">ufs: UWB Frontend Set</span>
<span class="go">ucls: Set BLE Adv UWB counter low water mark</span>
<span class="go">uclg: Get BLE Adv UWB counter low water mark</span>

<span class="go">** Command group: UWBMAC **</span>
<span class="go">nmo: Set UWB mode to off</span>
<span class="go">nmp: Set UWB mode to passive</span>
<span class="go">nma: Set mode to AN</span>
<span class="go">nmi: Set mode to ANI</span>
<span class="go">nmt: Set mode to TN</span>
<span class="go">nmtl: Set mode to TN-LP</span>
<span class="go">nmg: Set mode to GN</span>
<span class="go">ln: Show node list</span>
<span class="go">la: Show AN list</span>
<span class="go">nis: Set network ID</span>
<span class="go">nls: Set node label</span>
<span class="go">nps: Set network profile</span>
<span class="go">udi: Show incoming IoT data</span>
<span class="go">uui: Send IoT data</span>
<span class="go">usps: Set pulse per superframe cycle. Example: 50 means 1 pulse per 50 superframe</span>
<span class="go">uspg: Get pulse per superframe cycle.</span>

<span class="go">** Command group: API **</span>
<span class="go">urs: Set update rate</span>
<span class="go">urg: Get update rate</span>
<span class="go">tcs: Set tag config</span>
<span class="go">tlv: Cmd as TLV frame</span>
<span class="go">tlvr: Cmd as TLV frame with manual CRC</span>
<span class="go">ums: Set default UART mode</span>
<span class="go">ana: Set MAC address</span>
<span class="go">amlg: Get MAC address list</span>
<span class="go">mrs: Set mesh random timing</span>
<span class="go">mrg: Get mesh random timing</span>
<span class="go">dacs: Distance alarm set</span>
<span class="go">dacg: Distance alarm get</span>
<span class="go">acs: Set anchor config</span>
<span class="go">pg: Get position</span>
<span class="go">ps: Set position</span>
<span class="go">fls: Filter config set</span>
<span class="go">flg: Filter config get</span>
<span class="go">ahs: Set HW version once</span>
<span class="go">eks: Set encryption key</span>
<span class="go">ekc: Clear encryption key</span>
<span class="go">amls: Set MAC addr list once</span>

<span class="go">** Command group: FiRa **</span>
<span class="go">fniq: Set mode to Nearby Interaction</span>
<span class="go">fuci: Set mode to FiRa UCI</span>

<span class="go">** Tips **</span>
<span class="go">Press Enter to repeat the last command</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="id1">
<span id="id2"></span><h2>帮助</h2>
<p>显示帮助，与命令“?”。</p>
<p>示例:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; help</span>

<span class="go">/*same output as command ?*/</span>
</pre></div>
</div>
<hr class="docutils">
</div>
<div class="section" id="quit">
<span id="id3"></span><h2>退出</h2>
<p>关闭 shell 并将 UART 切换到 API 模式（如果已编译）。</p>
<p>示例:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; quit</span>

<span class="go">/\* press enter twice to switch to shell mode again*/</span>
</pre></div>
</div>
</div>
</div>


           </div>
