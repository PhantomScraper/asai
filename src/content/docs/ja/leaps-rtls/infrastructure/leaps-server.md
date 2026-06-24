---
title: "LEAPS Server"
lang: ja
slug: "leaps-rtls/infrastructure/leaps-server"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/leaps-rtls/infrastructure/leaps-server/"
order: 70
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-server">
<span id="leapsserver"></span><h1>LEAPS Server</h1>
<p>LEAPS ServerはUWBネットワークの中央データハブです。すべての <a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-gateway#leapsgateway"><span class="std std-ref">LEAPS Gateway</span></a> デバイスを、<a class="reference external" href="https://mosquitto.org/">MQTT Broker</a> を介して世界と相互接続します。</p>
<hr class="docutils">
<div class="section" id="key-features">
<h2>主な機能</h2>
<ul class="simple">
<li><p>アップリンクデータコンセントレータ、ダウンリンクデータルータ、データプロセッサ、位置情報エンジン、デバイス管理、デバイスアクセス制御、そしてQoS（Quality of Service）として機能します。</p></li>
<li><p>コネクタを介して世界と通信します。現在サポートされているコネクタは、AWSを含むMQTTです。</p></li>
<li><p><a class="reference internal" href="#leapsserver"><span class="std std-ref">LEAPS Server</span></a> は、Linuxプラットフォーム上でデーモンサービスとして動作します。</p></li>
</ul>
</div>
<hr class="docutils">
<div class="section" id="installation">
<h2>インストール</h2>
<div class="section" id="system-requirements">
<h3>システム要件</h3>
<div class="admonition note">
<p class="admonition-title">注釈</p>
<p>Dockerのシステム要件は、オペレーティングシステムによって異なります。</p>
<ul class="simple">
<li><p>Linuxの場合、64ビットアーキテクチャ、互換性のあるカーネルバージョン、および特定のカーネル機能が必要です。</p></li>
<li><p>Windowsでは、仮想化を有効にしたWindows 10でDocker Desktopを使用してください。</p></li>
<li><p>macOSでは、macOS 10.13以降でDocker Desktopを使用してください。ハードウェアに関しては、最低2GBのRAMに加え、十分なCPUとディスク容量が推奨されます。</p></li>
</ul>
<p>最新の詳細については、<a class="reference external" href="https://docs.docker.com/">Docker</a> 公式ドキュメントを参照してください。</p>
</div>
</div>
<hr class="docutils">
<div class="section" id="instructions">
<h3>使用方法</h3>
<ol class="arabic simple">
<li><p>PCにDockerをインストールする</p></li>
</ol>
<blockquote>
<div><div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-0" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-0">
Linux の場合</label><div class="sd-tab-content docutils">
<p><a class="reference external" href="https://docs.docker.com/desktop/install/linux-install/">LinuxにDocker Desktopをインストールする</a></p>
<p>さらに、以下のコマンドを参考にしてインストールすることもできる：</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">curl -fsSL https://get.docker.com -o get-docker.sh</span>
<span class="go">sudo sh ./get-docker.sh</span>
<span class="go">sudo usermod -aG docker $USER</span>
</pre></div>
</div>
</div>
<input id="sd-tab-item-1" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-1">
Windows の場合</label><div class="sd-tab-content docutils">
<p><a class="reference external" href="https://docs.docker.com/desktop/install/windows-install/">WindowsにDocker Desktopをインストールする</a></p>
</div>
<input id="sd-tab-item-2" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-2">
macOS の場合</label><div class="sd-tab-content docutils">
<p><a class="reference external" href="https://docs.docker.com/desktop/install/mac-install/">にDocker Desktopをインストールする</a></p>
</div>
</div>
</div></blockquote>
<ol class="arabic simple" start="2">
<li><p><cite>leaps_server_hub</cite> フォルダとサブフォルダ <code class="docutils literal notranslate"><span class="pre">data</span></code> を作成します。次に、<code class="docutils literal notranslate"><span class="pre">leaps_server_hub/data</span></code> に <code class="docutils literal notranslate"><span class="pre">leaps-server.conf</span></code> 設定ファイルを追加します。</p></li>
</ol>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">#</span><span class="c1">######################################################################</span>
<span class="gp"># </span>LEAPS<span class="w"> </span>Server<span class="w"> </span>settings
<span class="gp">#</span>

<span class="gp"># </span>-----------------------------------------------------------------
<span class="gp"># </span>Logging
<span class="gp"># </span>-----------------------------------------------------------------
<span class="go">log_level = 0 #  Logging level, default is 0 (0=none, 1=fatal, 2=error, 3=warning, 4=info, 5=debug, 6=verbose)</span>

<span class="gp"># </span>Path<span class="w"> </span>to<span class="w"> </span>log<span class="w"> </span>file.<span class="w"> </span>Comment<span class="w"> </span>out<span class="w"> </span>to<span class="w"> </span>disable<span class="w"> </span>logging<span class="w"> </span>to<span class="w"> </span>file<span class="w"> </span><span class="o">(</span>log<span class="w"> </span>to<span class="w"> </span>stdio<span class="w"> </span>instead<span class="o">)</span>.
<span class="gp"># </span><span class="nv">log</span><span class="w"> </span><span class="o">=</span><span class="w"> </span>leaps-server.log

<span class="gp"># </span>-----------------------------------------------------------------
<span class="gp"># </span>Certificate<span class="w"> </span>based<span class="w"> </span>SSL/TLS<span class="w"> </span>support
<span class="gp"># </span>-----------------------------------------------------------------
<span class="gp">#</span>
<span class="gp"># </span>cafile<span class="w"> </span>-<span class="w"> </span>Authority<span class="w"> </span>certificates<span class="w"> </span>that<span class="w"> </span>have<span class="w"> </span>signed<span class="w"> </span>your<span class="w"> </span>server<span class="w"> </span>certificate.
<span class="gp"># </span>certfile<span class="w"> </span>-<span class="w"> </span>Path<span class="w"> </span>to<span class="w"> </span>the<span class="w"> </span>PEM<span class="w"> </span>encoded<span class="w"> </span>server<span class="w"> </span>certificate.
<span class="gp"># </span>keyfile<span class="w"> </span>-<span class="w"> </span>Path<span class="w"> </span>to<span class="w"> </span>the<span class="w"> </span>PEM<span class="w"> </span>encoded<span class="w"> </span>keyfile.
<span class="gp"># </span>gw_auth<span class="w"> </span>-<span class="w"> </span>When<span class="w"> </span>using<span class="w"> </span>TLS<span class="w"> </span>on<span class="w"> </span>the<span class="w"> </span>interface<span class="w"> </span>with<span class="w"> </span>the<span class="w"> </span>gateways,<span class="w"> </span>this<span class="w"> </span>parameter<span class="w"> </span>configures<span class="w"> </span>TLS<span class="w"> </span>authentication<span class="w"> </span>between<span class="w"> </span>server<span class="w"> </span>and<span class="w"> </span>the<span class="w"> </span>gateway<span class="w"> </span><span class="o">(</span><span class="nv">0</span><span class="o">=</span>server<span class="w"> </span><span class="nv">1</span><span class="o">=</span>mutual<span class="o">)</span>.
<span class="gp">#</span>
<span class="gp"># </span><span class="nv">cafile</span><span class="w"> </span><span class="o">=</span><span class="w"> </span>/etc/leaps-server/cacert.pem
<span class="gp"># </span><span class="nv">certfile</span><span class="w"> </span><span class="o">=</span><span class="w"> </span>/etc/leaps-server/servercert.pem
<span class="gp"># </span><span class="nv">keyfile</span><span class="w"> </span><span class="o">=</span><span class="w"> </span>/etc/leaps-server/serverkey.pem
<span class="gp"># </span><span class="nv">gw_auth</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="m">0</span>

<span class="gp"># </span>Optional<span class="w"> </span>AES<span class="w"> </span><span class="m">128</span>-bit<span class="w"> </span>private<span class="w"> </span>key<span class="w"> </span>as<span class="w"> </span>hexadecimal<span class="w"> </span>number.<span class="w"> </span>If<span class="w"> </span>specified,<span class="w"> </span>the<span class="w"> </span>key<span class="w"> </span>is<span class="w"> </span>used<span class="w"> </span>to<span class="w"> </span>encrypt<span class="w"> </span>sensitive<span class="w"> </span>data
<span class="gp"># </span><span class="k">for</span><span class="w"> </span>example<span class="w"> </span>the<span class="w"> </span>WiFi<span class="w"> </span>password<span class="w"> </span>published<span class="w"> </span>on<span class="w"> </span>the<span class="w"> </span>MQTT<span class="w"> </span>interface.
<span class="gp"># </span><span class="nv">aes_128_key</span><span class="w"> </span><span class="o">=</span><span class="w"> </span>00112233445566778899aabbccddeeff

<span class="gp"># </span>-----------------------------------------------------------------
<span class="gp"># </span>MQTT<span class="w"> </span>Broker
<span class="gp"># </span>-----------------------------------------------------------------
<span class="gp"># </span>MQTT<span class="w"> </span>API<span class="w"> </span>variant<span class="w"> </span><span class="s2">"pans"</span><span class="w"> </span>or<span class="w"> </span><span class="s2">"leaps"</span>
<span class="go">mqtt_api = leaps</span>

<span class="gp"># </span>include<span class="w"> </span>network<span class="w"> </span>ID<span class="w"> </span><span class="o">(</span>panid<span class="o">)</span><span class="w"> </span><span class="k">in</span><span class="w"> </span>the<span class="w"> </span>MQTT<span class="w"> </span>topics
<span class="go">mqtt_with_panid = true</span>

<span class="gp"># </span>Specifies<span class="w"> </span>an<span class="w"> </span><span class="nb">alias</span><span class="w"> </span><span class="k">for</span><span class="w"> </span>particular<span class="w"> </span>UWB<span class="w"> </span>network<span class="w"> </span>that<span class="w"> </span>is<span class="w"> </span><span class="k">then</span><span class="w"> </span>used<span class="w"> </span><span class="k">in</span><span class="w"> </span>the<span class="w"> </span>MQTT<span class="w"> </span>topic<span class="w"> </span>instead<span class="w"> </span>of<span class="w"> </span>the<span class="w"> </span>network<span class="w"> </span>ID<span class="w"> </span><span class="o">(</span>pan<span class="w"> </span>ID<span class="o">)</span><span class="w"> </span>.
<span class="gp"># </span>Parameter<span class="w"> </span>can<span class="w"> </span>be<span class="w"> </span>used<span class="w"> </span>multiple<span class="w"> </span><span class="nb">times</span><span class="w"> </span>and<span class="w"> </span>there<span class="w"> </span>might<span class="w"> </span>be<span class="w"> </span>multiple<span class="w"> </span>definitions<span class="w"> </span>separated<span class="w"> </span>by<span class="w"> </span>spaces<span class="w"> </span>which<span class="w"> </span>are<span class="w"> </span><span class="k">then</span><span class="w"> </span>added<span class="w"> </span>to<span class="w"> </span>the<span class="w"> </span>list<span class="w"> </span>of<span class="w"> </span>known<span class="w"> </span>aliases.
<span class="gp"># </span>Alias<span class="w"> </span>definitions<span class="w"> </span>must<span class="w"> </span>follow<span class="w"> </span>format<span class="w"> </span>&lt;ID&gt;:&lt;ALIAS_STRING&gt;.<span class="w"> </span>Multiple<span class="w"> </span>definitions<span class="w"> </span>must<span class="w"> </span>be<span class="w"> </span>separated<span class="w"> </span>with<span class="w"> </span>spaces.
<span class="gp"># </span>Network<span class="w"> </span>ID<span class="w"> </span><span class="o">(</span>PAN<span class="w"> </span>ID<span class="o">)</span><span class="w"> </span>can<span class="w"> </span>be<span class="w"> </span>hexadecimal<span class="w"> </span>number<span class="w"> </span><span class="o">(</span>withe<span class="w"> </span>prefix<span class="w"> </span><span class="se">\"</span>0x<span class="se">\"</span><span class="o">)</span><span class="w"> </span>or<span class="w"> </span>decimal<span class="w"> </span>number.
<span class="gp"># </span><span class="nv">mqtt_panid_alias</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="o">[</span><span class="m">123</span>:NetworkA<span class="o">]</span><span class="w"> </span><span class="o">[</span>0x0002:Net<span class="w"> </span>B<span class="o">]</span>
<span class="gp"># </span><span class="nv">mqtt_panid_alias</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="o">[</span>0XABCD:Network_C<span class="o">]</span>

<span class="go">mqtt_clid = 1</span>
<span class="go">mqtt_port = 1883</span>
<span class="go">mqtt_host = localhost # Or your Computer's IP Address</span>

<span class="gp"># </span>For<span class="w"> </span>LEAPS<span class="w"> </span>RTLS
<span class="go">mqtt_user = leaps</span>
<span class="go">mqtt_password = leapspass</span>
<span class="go">mqtt_topic_prefix = leaps</span>

<span class="gp"># </span>For<span class="w"> </span>PANS<span class="w"> </span>PRO<span class="w"> </span>RTLS
<span class="gp"># </span><span class="nv">mqtt_user</span><span class="w"> </span><span class="o">=</span><span class="w"> </span>dwmuser
<span class="gp"># </span><span class="nv">mqtt_password</span><span class="w"> </span><span class="o">=</span><span class="w"> </span>dwmpass
<span class="gp"># </span><span class="nv">mqtt_topic_prefix</span><span class="w"> </span><span class="o">=</span><span class="w"> </span>dwm

<span class="gp"># </span>Certificates<span class="w"> </span>used<span class="w"> </span>on<span class="w"> </span>MQTT<span class="w"> </span>interface
<span class="gp"># </span><span class="nv">mqtt_cafile</span><span class="w"> </span><span class="o">=</span><span class="w"> </span>/etc/leaps-server/cacert.pem
<span class="gp"># </span><span class="nv">mqtt_certfile</span><span class="w"> </span><span class="o">=</span><span class="w"> </span>/etc/leaps-server/servercert.pem
<span class="gp"># </span><span class="nv">mqtt_keyfile</span><span class="w"> </span><span class="o">=</span><span class="w"> </span>/etc/leaps-server/serverkey.pem

<span class="gp"># </span>Period<span class="w"> </span><span class="k">in</span><span class="w"> </span>seconds<span class="w"> </span>after<span class="w"> </span>which<span class="w"> </span>all<span class="w"> </span>retained<span class="w"> </span>topics<span class="w"> </span>are<span class="w"> </span>published<span class="w"> </span>regardless
<span class="gp"># </span>whether<span class="w"> </span>the<span class="w"> </span>content<span class="w"> </span>has<span class="w"> </span>changed<span class="w"> </span>or<span class="w"> </span>not.<span class="w"> </span>Disabled<span class="w"> </span>when<span class="w"> </span><span class="nb">set</span><span class="w"> </span>to<span class="w"> </span><span class="m">0</span>.<span class="w"> </span>Disabled<span class="w"> </span>by<span class="w"> </span>default.
<span class="gp">#</span><span class="nv">mqtt_refresh</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="m">0</span>

<span class="gp"># </span>-----------------------------------------------------------------
<span class="gp"># </span>Secondary<span class="w"> </span>MQTT<span class="w"> </span>Broker
<span class="gp"># </span>-----------------------------------------------------------------
<span class="gp">#</span>
<span class="gp"># </span><span class="nv">mqtt_clid_sec</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="m">2</span>
<span class="gp"># </span><span class="nv">mqtt_port_sec</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="m">1883</span>
<span class="gp"># </span><span class="nv">mqtt_host_sec</span><span class="w"> </span><span class="o">=</span>

<span class="gp"># </span>For<span class="w"> </span>PANS<span class="w"> </span>PRO<span class="w"> </span>RTLS
<span class="gp"># </span><span class="nv">mqtt_user_sec</span><span class="w"> </span><span class="o">=</span><span class="w"> </span>dwmuser
<span class="gp"># </span><span class="nv">mqtt_password_sec</span><span class="w"> </span><span class="o">=</span><span class="w"> </span>dwmpass

<span class="gp"># </span>Certificates<span class="w"> </span>used<span class="w"> </span>on<span class="w"> </span>MQTT<span class="w"> </span>interface
<span class="gp"># </span><span class="nv">mqtt_cafile_sec</span><span class="w"> </span><span class="o">=</span><span class="w"> </span>/etc/leaps-server/cacert.pem
<span class="gp"># </span><span class="nv">mqtt_certfile_sec</span><span class="w"> </span><span class="o">=</span><span class="w"> </span>/etc/leaps-server/servercert.pem
<span class="gp"># </span><span class="nv">mqtt_keyfile_sec</span><span class="w"> </span><span class="o">=</span><span class="w"> </span>/etc/leaps-server/serverkey.pem

<span class="gp"># </span>-----------------------------------------------------------------
<span class="gp"># </span>TCP
<span class="gp"># </span>-----------------------------------------------------------------
<span class="gp">#</span>
<span class="go">tcp_port = 7777</span>

<span class="gp"># </span>-----------------------------------------------------------------
<span class="gp"># </span>Tag<span class="w"> </span>location<span class="w"> </span>statistics
<span class="gp"># </span>-----------------------------------------------------------------
<span class="gp"># </span>Enable<span class="w"> </span>calculation<span class="w"> </span>of<span class="w"> </span>tag<span class="w"> </span>location<span class="w"> </span>statistics.<span class="w"> </span>Default<span class="w"> </span>is<span class="w"> </span>false.
<span class="gp"># </span><span class="nv">loc_stats_enable</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="nb">true</span>

<span class="gp"># </span>History<span class="w"> </span>window<span class="w"> </span><span class="k">for</span><span class="w"> </span>calculation<span class="w"> </span>of<span class="w"> </span>tag<span class="w"> </span>location<span class="w"> </span>statistics.<span class="w"> </span>Default<span class="w"> </span>is<span class="w"> </span><span class="m">100</span>.
<span class="gp"># </span><span class="nv">loc_stats_history_window</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="m">100</span>

<span class="gp"># </span>-----------------------------------------------------------------
<span class="gp"># </span>Other
<span class="gp"># </span>-----------------------------------------------------------------
<span class="gp"># </span>maximum<span class="w"> </span>number<span class="w"> </span>of<span class="w"> </span>attempts<span class="w"> </span>of<span class="w"> </span>configuration<span class="w"> </span>and<span class="w"> </span>service<span class="w"> </span>commands
<span class="gp"># </span><span class="nv">cmd_att</span><span class="w"> </span><span class="o">=</span><span class="w"> </span><span class="m">3</span>
</pre></div>
</div>
</div></blockquote>
<ol class="arabic simple" start="3">
<li><p>PCでコマンドプロンプトまたはターミナルウィンドウを開く。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>設定ファイルを作成したフォルダに移動します。</p></li>
</ul>
<p>たとえば、Ubuntu (Linux) の場合:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">cd leaps_server_hub/</span>
</pre></div>
</div>
</div></blockquote>
<ol class="arabic simple" start="4">
<li><p>LEAPS Server Dockerパッケージをインストールします。</p></li>
</ol>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">docker run -d -p 7777:7777/tcp -p 7777:7777/udp --name some_name -v /path/to/data/data/:/app/data/ leapslabs/leaps_server:tag /app/leaps-server --cfg /app/data/leaps-server.conf</span>
</pre></div>
</div>
<p>ここで、<code class="docutils literal notranslate"><span class="pre">some_name</span></code> はコンテナに割り当てる名前、<code class="docutils literal notranslate"><span class="pre">tag</span></code> は必要な <code class="docutils literal notranslate"><span class="pre">leaps-server</span></code> のバージョンを指定するタグです。</p>
<p>leaps_server インスタンスは、<a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-gateway#leapsgateway"><span class="std std-ref">LEAPS Gateway</span></a> との <code class="docutils literal notranslate"><span class="pre">TCP</span></code> および <code class="docutils literal notranslate"><span class="pre">UDP</span></code> 通信にポート <code class="docutils literal notranslate"><span class="pre">7777</span></code> を使用しているため、コマンド <code class="docutils literal notranslate"><span class="pre">-p</span> <span class="pre">7777:7777/tcp</span> <span class="pre">-p</span> <span class="pre">7777:7777/udp</span></code> を使用して、これらのポートをホストから leaps_server インスタンスに再マッピングする必要があります。</p>
<p>必要がない限り、ポート番号を変更することは推奨されません。変更が必要な場合は、<a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-gateway#leapsgateway"><span class="std std-ref">LEAPS Gateway</span></a> のポート設定を適宜調整してください。</p>
<ul class="simple">
<li><p>推奨される走行オプション</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">--user</span> <span class="pre">$(id</span> <span class="pre">-u):$(id</span> <span class="pre">-g)</span></code> 特定のユーザーとグループの下でインスタンスを実行する。</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">--restart</span> <span class="pre">unless-stopped</span></code> は、サーバーがクラッシュした場合に備えて、インスタンスを自動的に再起動します。</p></li>
</ul>
</li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="5">
<li><p>LEAPS Serverのインストールプロセスが開始されます。</p></li>
</ol>
<blockquote>
<div><p>たとえば、Ubuntu (Linux) の場合:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">docker run -d -p 7777:7777/tcp -p 7777:7777/udp --name leaps_server -v "$(pwd)"/data/:/app/data leapslabs/leaps_server:latest /app/leaps-server --cfg /app/data/leaps-server.conf</span>

<span class="go">Unable to find image 'leapslabs/leaps_server:latest' locally</span>
<span class="go">latest: Pulling from leapslabs/leaps_server</span>
<span class="go">a458657ccc71: Pull complete</span>
<span class="go">Digest: sha256:a19b127656d41d8607f043c2c83924e5b9a5cbd4dc23cfbed070be3b9cfc6b9a</span>
<span class="go">Status: Downloaded newer image for leapslabs/leaps_server:latest</span>
<span class="go">320d3768289874e063619f75faca7a24dd75a08884df8cd8fb2cc9b54c6f0a46</span>
</pre></div>
</div>
</div></blockquote>
<ol class="arabic simple" start="6">
<li><p>インストールが成功したことを確認し、実行する：</p></li>
</ol>
<blockquote>
<div><p>たとえば、Ubuntu (Linux) の場合:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">docker ps</span>

<span class="go">CONTAINER ID   IMAGE                    COMMAND                  CREATED          STATUS                          PORTS     NAMES</span>
<span class="go">b1145b72db35   leapslabs/leaps_server:latest   "sh -c 'cd /app &amp;&amp;  …"   37 seconds ago   11 seconds ago                            leaps_server</span>
</pre></div>
</div>
</div></blockquote>
<p>これで、PC上の LEAPS Server が正常にインストールされ、起動しました。</p>
</div>
</div>
<hr class="docutils">
<div class="section" id="getting-started">
<h2>はじめに</h2>
<div class="section" id="leaps-server-docker">
<h3>LEAPS ServerDocker</h3>
<ul class="simple">
<li><p>LEAPS Serverを起動するには、<code class="docutils literal notranslate"><span class="pre">docker</span> <span class="pre">start</span> <span class="pre">leaps_server</span></code> を実行します。</p></li>
<li><p>LEAPS Serverを停止するには、<code class="docutils literal notranslate"><span class="pre">docker</span> <span class="pre">stop</span> <span class="pre">leaps_server</span></code> を実行します。</p></li>
<li><p>LEAPS Serverを再起動するには、<code class="docutils literal notranslate"><span class="pre">docker</span> <span class="pre">restart</span> <span class="pre">leaps_server</span></code> を実行します。</p></li>
<li><p>LEAPS Serverを削除するには、<code class="docutils literal notranslate"><span class="pre">docker</span> <span class="pre">rm</span> <span class="pre">--force</span> <span class="pre">leaps_server</span></code> を実行します。</p></li>
</ul>
</div>
<hr class="docutils">
<div class="section" id="network-configuration">
<h3>ネットワーク構成</h3>
<ul>
<li><p>MQTT APIバリアント "pans" または "leaps"</p></li>
<li><p>公開トピックにLEAPS IDを追加します。</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">mqtt_with_panid = true</span>

<span class="go">mqtt_clid = 1</span>
<span class="go">mqtt_port = 1883</span>
<span class="go">mqtt_host = localhost # Or your Computer's IP Address</span>
</pre></div>
</div>
</li>
<li><p>LEAPS RTLS アカウントの設定</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">mqtt_user = leapsuser</span>
<span class="go">mqtt_password = leapspass</span>
<span class="go">mqtt_topic_prefix = leaps</span>
</pre></div>
</div>
</li>
<li><p>TCP ポートは 7777 です。</p></li>
</ul>
</div>
</div>
<div class="section" id="troubleshooting">
<h2>トラブルシューティング</h2>
<ul class="simple">
<li><p>LEAPS Serverを再起動するには、以下のコマンド <code class="docutils literal notranslate"><span class="pre">docker</span> <span class="pre">restart</span> <span class="pre">leaps_server</span></code> を使用します。</p></li>
<li><p><a class="reference internal" href="#leapsserver"><span class="std std-ref">LEAPS Server</span></a> 実行中のログを確認し、Docker デスクトップを開いて leaps_server コンテナを選択します。</p></li>
</ul>
</div>
</div>


           </div>
