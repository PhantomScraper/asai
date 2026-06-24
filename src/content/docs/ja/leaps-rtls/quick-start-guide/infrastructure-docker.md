---
title: "LEAPS ドッカー"
lang: ja
slug: "leaps-rtls/quick-start-guide/infrastructure-docker"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/leaps-rtls/quick-start-guide/infrastructure-docker/"
order: 64
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-docker">
<span id="leaps-qsg-infrastructure-docker"></span><h1>LEAPS ドッカー</h1>
<p>このページには以下が含まれます:</p>
<blockquote>
<div><ul class="simple">
<li><p>LEAPS Docker パッケージ。</p></li>
<li><p>システム要件に関する情報。</p></li>
<li><p>LEAPS Docker のインストール方法に関する説明。</p></li>
</ul>
</div></blockquote>
<p>インストールは迅速かつ簡単で、一度行うだけで済みます。</p>
<p><a class="reference external" href="https://docs.docker.com/">Docker</a> の詳細については、公式 Docker にアクセスしてください。</p>
<p><strong>システム要件</strong></p>
<blockquote>
<div><ul class="simple">
<li><p>システム要件は、 <a class="reference external" href="https://docs.docker.com/desktop/install/windows-install/#system-requirements">Linux 上の Docker デスクトップ</a> または <a class="reference external" href="https://docs.docker.com/desktop/install/windows-install/#system-requirements">Windows 上の Docker デスクトップ</a> に従います。</p></li>
<li><p>デスクトップ デバイス: <strong>2 GB の空きメモリが必要です</strong>。</p></li>
<li><p>Windows では、WSL のインストールにより 2GB の RAM が永続的に消費されます。これは Ubuntu WSL に割り当てられます。</p></li>
<li><p><em>推奨: UDK のセット (少なくとも 5 つのデバイス) を検証します。</em></p></li>
<li><p><em>推奨: デバイスに電力を供給するためのバッテリーまたは USB-C ケーブル。</em></p></li>
<li><p><em>推奨:</em> <a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> <em>デバイスを構成します。</em></p></li>
</ul>
</div></blockquote>
<p id="uidocker"><strong>セットアップ手順</strong></p>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-0" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-0">
Linux</label><div class="sd-tab-content docutils">
<p>このシステムは、AMD64、ARM64、および ARM32 アーキテクチャと互換性があります。</p>
<ol class="arabic simple">
<li><p>LEAPS Docker をダウンロード</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>LEAPS Docker <a class="reference download internal" download="" href="../../../_downloads/ae97200ed08d464a52759cdc643e7c12/LEAPS-DOCKER-LINUX-v1.1.0.zip"><code class="xref download docutils literal notranslate"><span class="pre">LEAPS-DOCKER-LINUX-v1.1.0.zip</span></code></a>.</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="2">
<li><p>LEAPS Docker アーカイブを抽出します</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>ターミナルに次のように入力します: <span class="red-text">$ unzip LEAPS-DOCKER-LINUX-v1.1.0.zip -d /path/to/directory</span></p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="3">
<li><p>オペレーティング システムに Docker をインストールします。</p></li>
</ol>
<blockquote>
<div><ul>
<li><p><span class="red-text">leaps_docker_install.sh</span> スクリプトを実行して、オペレーティング システムに Docker をインストールします。たとえば、Ubuntu (Linux) の場合:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">source</span> <span class="n">leaps_docker_install</span><span class="o">.</span><span class="n">sh</span>
</pre></div>
</div>
</li>
<li><p>インストール後、OS を再起動して、Docker が正しく構成されていることを確認します。</p></li>
<li><p>詳細な手順については、公式の <a class="reference external" href="https://docs.docker.com/get-docker/">Docker ドキュメント</a> を参照してください。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="4">
<li><p>IP アドレスを使用して正しい構成を更新します。</p></li>
</ol>
<blockquote>
<div><ul>
<li><p><span class="red-text">update_configuration_ip.sh</span> スクリプトを使用して、PC の IP アドレスでシステムの構成を更新します。たとえば、Ubuntu (Linux) の場合:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">source</span> <span class="n">update_configuration_ip</span><span class="o">.</span><span class="n">sh</span>
</pre></div>
</div>
</li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="5">
<li><p>すべての LEAPS Docker コンテナを実行します。</p></li>
</ol>
<blockquote>
<div><ul>
<li><p><span class="red-text">leaps_docker_run_all.sh</span> スクリプトを実行します。これにより、<a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a>、<a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-server#leapsserver"><span class="std std-ref">LEAPS Server</span></a>、<a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-gateway#leapsgateway"><span class="std std-ref">LEAPS Gateway</span></a>、および Mosquitto (MQTT Broker) に必要な Docker コンテナがプルされて実行されます。たとえば、Ubuntu (Linux) の場合:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">source</span> <span class="n">leaps_docker_run_all</span><span class="o">.</span><span class="n">sh</span>
</pre></div>
</div>
</li>
<li><p><span class="red-text">docker ps</span> コマンドを実行し、すべてのコンテナが正常に起動し、使用できる状態になっていることを確認します。たとえば、Ubuntu (Linux) の場合:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">docker</span> <span class="n">ps</span>

<span class="n">CONTAINER</span> <span class="n">ID</span>   <span class="n">IMAGE</span>                       <span class="n">COMMAND</span>                  <span class="n">CREATED</span>          <span class="n">STATUS</span>          <span class="n">PORTS</span>                                              <span class="n">NAMES</span>
<span class="mi">6</span><span class="n">f2ae0c87d65</span>   <span class="n">leapslabs</span><span class="o">/</span><span class="n">leaps_mosquitto</span><span class="p">:</span><span class="n">udk</span>   <span class="s2">"/docker-entrypoint.…"</span>   <span class="mi">9</span> <span class="n">seconds</span> <span class="n">ago</span>    <span class="n">Up</span> <span class="mi">9</span> <span class="n">seconds</span>    <span class="mf">0.0.0.0</span><span class="p">:</span><span class="mi">1883</span><span class="o">-&gt;</span><span class="mi">1883</span><span class="o">/</span><span class="n">tcp</span><span class="p">,</span> <span class="mf">0.0.0.0</span><span class="p">:</span><span class="mi">15675</span><span class="o">-&gt;</span><span class="mi">15675</span><span class="o">/</span><span class="n">tcp</span>   <span class="n">leaps_mosquitto</span>
<span class="mi">3</span><span class="n">d84cad7a913</span>   <span class="n">leapslabs</span><span class="o">/</span><span class="n">leaps_server</span><span class="p">:</span><span class="n">udk</span>      <span class="s2">"/app/leaps-server -…"</span>   <span class="mi">10</span> <span class="n">seconds</span> <span class="n">ago</span>   <span class="n">Up</span> <span class="mi">9</span> <span class="n">seconds</span>    <span class="mf">0.0.0.0</span><span class="p">:</span><span class="mi">7777</span><span class="o">-&gt;</span><span class="mi">7777</span><span class="o">/</span><span class="n">tcp</span><span class="p">,</span> <span class="mf">0.0.0.0</span><span class="p">:</span><span class="mi">7777</span><span class="o">-&gt;</span><span class="mi">7777</span><span class="o">/</span><span class="n">udp</span>     <span class="n">leaps_server</span>
<span class="mi">633</span><span class="n">c97e96f6e</span>   <span class="n">leapslabs</span><span class="o">/</span><span class="n">leaps_center</span><span class="p">:</span><span class="n">udk</span>      <span class="s2">"sh -c 'cd /app &amp;&amp;  …"</span>   <span class="mi">10</span> <span class="n">seconds</span> <span class="n">ago</span>   <span class="n">Up</span> <span class="mi">10</span> <span class="n">seconds</span>   <span class="mi">80</span><span class="o">/</span><span class="n">tcp</span><span class="p">,</span> <span class="mf">0.0.0.0</span><span class="p">:</span><span class="mi">80</span><span class="o">-&gt;</span><span class="mi">8080</span><span class="o">/</span><span class="n">tcp</span>                       <span class="n">leaps_center</span>
</pre></div>
</div>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">sudo</span> <span class="n">docker</span> <span class="n">ps</span>

<span class="n">CONTAINER</span> <span class="n">ID</span>   <span class="n">IMAGE</span>                     <span class="n">COMMAND</span>                  <span class="n">CREATED</span>              <span class="n">STATUS</span>                          <span class="n">PORTS</span>     <span class="n">NAMES</span>
<span class="mi">6</span><span class="n">bb3bf42cb63</span>   <span class="n">leapslabs</span><span class="o">/</span><span class="n">leaps_gateway</span><span class="p">:</span><span class="n">udk</span>   <span class="s2">"/app/leaps-gateway …"</span>   <span class="n">About</span> <span class="n">a</span> <span class="n">minute</span> <span class="n">ago</span>   <span class="n">Up</span> <span class="n">About</span> <span class="n">a</span> <span class="n">minute</span>                         <span class="n">leaps_gateway</span>
</pre></div>
</div>
</li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="6">
<li><p>USB-C データ ケーブルを使用して、ゲートウェイ ボードを PC に接続します。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>USB-C データ ケーブルを PC の <a class="reference internal" href="/docs/ja/udk/udk-start/device-hw-interfaces#hardware-interface"><span class="std std-ref">USB-C データ ポート 1</span></a> に差し込みます。安定した接続を確保してください。</p></li>
</ul>
<img alt="../../../_images/leaps-connect-usb-port1.gif" class="align-center" src="/docs-assets/ja/_images/leaps-connect-usb-port1.gif">
</div></blockquote>
<ol class="arabic simple" start="7">
<li><p>Mosquitto およびチェックメッセージ (オプション)</p></li>
</ol>
<blockquote>
<div><ul>
<li><p>システムで mosquitto_sub を使用します。メッセージを確認するには、ターミナルで次のコマンドを使用します</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">mosquitto_sub</span> <span class="o">-</span><span class="n">p</span> <span class="mi">1883</span> <span class="o">-</span><span class="n">d</span> <span class="o">-</span><span class="n">v</span> <span class="o">-</span><span class="n">t</span> <span class="s1">'#'</span>
</pre></div>
</div>
</li>
<li><p>このコマンドは Mosquitto MQTT ブローカーに接続し、受信したすべてのメッセージを表示します)。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="8">
<li><p>IP アドレス経由で <a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> にアクセスします。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>コンピュータの Web ブラウザを使用します。</p></li>
<li><p><a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> にアクセスするには、IP アドレスまたは <span class="red-text">localhost</span> を入力します。</p></li>
</ul>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/docker_leaps_center_login.png"><img alt="../../../_images/docker_leaps_center_login.png" src="/docs-assets/ja/_images/docker_leaps_center_login.png" style="width: 762.4000000000001px; height: 370.8px;"></a>
</div>
</div></blockquote>
<ol class="arabic simple" start="9">
<li><p><a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> にログインします。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>ユーザー名 <span class="red-text">admin</span>、パスワード <span class="red-text">admin</span> を使用してログインします。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="10">
<li><p><a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> を使用してネットワークを準備します。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>デモを設定します: <a class="reference internal" href="/docs/ja/udk/udk-start/twr-rtls-and-data-telemetry-demo#twr-rtls-and-data-telemetry-demo"><span class="std std-ref">TWR RTLS およびデータ遠隔測定デモ</span></a> または <a class="reference internal" href="/docs/ja/udk/udk-start/uplink-tdoa-rtls-demo#uplink-tdoa-rtls-demo"><span class="std std-ref">アップリンク TDoA RTLS デモ</span></a>。</p></li>
<li><p>デフォルトでは、ネットワーク ID は <code class="docutils literal notranslate"><span class="pre">0x1234</span></code> になります。</p></li>
<li><p>この例では、ID <code class="docutils literal notranslate"><span class="pre">0x83A2</span></code> のゲートウェイ ボードを接続する必要があります。</p></li>
</ul>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/docker_network_demo01.jpg"><img alt="../../../_images/docker_network_demo01.jpg" src="/docs-assets/ja/_images/docker_network_demo01.jpg" style="width: 360.0px; height: 800.0px;"></a>
</div>
</div></blockquote>
<ol class="arabic simple" start="11">
<li><p><a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> でネットワークを構成します。</p></li>
</ol>
<blockquote>
<div><ul>
<li><p><a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> のネットワーク設定を確認して、ネットワーク ID と一致するようにしてください。</p></li>
<li><p>PC の IP アドレスとして構成された正しいホストを確認してください。</p></li>
<li><p>この例では、ネットワーク ID は <code class="docutils literal notranslate"><span class="pre">0x1234</span></code>、ホストは <code class="docutils literal notranslate"><span class="pre">192.168.1.12</span></code> です。</p>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/docker_leaps_center_config_network.png"><img alt="../../../_images/docker_leaps_center_config_network.png" src="/docs-assets/ja/_images/docker_leaps_center_config_network.png" style="width: 626.4000000000001px; height: 409.6px;"></a>
</div>
</li>
<li><p>アプリケーションを使用してノードとネットワークを構成および視覚化する方法の詳細については、<a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> および <a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> を参照してください。</p></li>
</ul>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/docker_leaps_center_network.png"><img alt="../../../_images/docker_leaps_center_network.png" src="/docs-assets/ja/_images/docker_leaps_center_network.png" style="width: 764.4000000000001px; height: 373.20000000000005px;"></a>
</div>
</div></blockquote>
<p>これで、システムは正常にセットアップされ、構成されました。楽しく使ってください！</p>
</div>
<input id="sd-tab-item-1" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-1">
Windows</label><div class="sd-tab-content docutils">
<ol class="arabic simple">
<li><p>LEAPS Docker をダウンロードします。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>LEAPS Docker <a class="reference download internal" download="" href="../../../_downloads/0bfac2c46fb0b9265d7f58941736f12a/LEAPS-DOCKER-WINDOWS-v1.1.0.zip"><code class="xref download docutils literal notranslate"><span class="pre">LEAPS-DOCKER-WINDOWS-v1.1.0.zip</span></code></a>。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="2">
<li><p>LEAPS Docker アーカイブを抽出します。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>WinZip や 7-Zip などのプログラムを使用して、ダウンロードした LEAPS Docker zip ファイルを解凍します。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="3">
<li><p>Windows に Docker デスクトップをインストールします。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>Docker ドキュメントの <a class="reference external" href="https://docs.docker.com/desktop/install/windows-install/">Docker Windows インストール</a> の手順に従ってください。</p></li>
<li><p>インストールが完了したら、Windows システムを再起動して、すべての変更が有効になっていることを確認します。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="4">
<li><p>PowerShell を使用して、IP アドレスを含む正しい構成を更新します。</p></li>
</ol>
<blockquote>
<div><ul>
<li><p><span class="red-text">update_configuration_ip.bat</span> スクリプトを使用して、PC の IP アドレスでシステムの構成を更新します。</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">./</span><span class="n">update_configuration_ip</span><span class="o">.</span><span class="n">bat</span>
</pre></div>
</div>
</li>
<li><p>For this example, the leaps-server configuration is updated with the current IP address: <code class="docutils literal notranslate"><span class="pre">192.168.1.12</span></code>.</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="5">
<li><p>PowerShell を使用してすべての LEAPS Docker コンテナを実行します。</p></li>
</ol>
<blockquote>
<div><ul>
<li><p><span class="red-text">leaps_docker_run_all.bat</span> スクリプトを実行します。これにより、<a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a>、LEAPS Server、および Mosquitto (MQTT Broker) に必要な Docker コンテナがプルされて実行されます。</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="o">./</span><span class="n">leaps_docker_run_all</span><span class="o">.</span><span class="n">bat</span>
</pre></div>
</div>
</li>
<li><p>すべてのコンテナが正常に起動し、使用できる状態になっていることを確認してください。</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">CONTAINER</span> <span class="n">ID</span>   <span class="n">IMAGE</span>                       <span class="n">COMMAND</span>                  <span class="n">CREATED</span>          <span class="n">STATUS</span>          <span class="n">PORTS</span>                                              <span class="n">NAMES</span>
<span class="mi">6</span><span class="n">f2ae0c87d65</span>   <span class="n">leapslabs</span><span class="o">/</span><span class="n">leaps_mosquitto</span><span class="p">:</span><span class="n">udk</span>   <span class="s2">"/docker-entrypoint.…"</span>   <span class="mi">9</span> <span class="n">seconds</span> <span class="n">ago</span>    <span class="n">Up</span> <span class="mi">9</span> <span class="n">seconds</span>    <span class="mf">0.0.0.0</span><span class="p">:</span><span class="mi">1883</span><span class="o">-&gt;</span><span class="mi">1883</span><span class="o">/</span><span class="n">tcp</span><span class="p">,</span> <span class="mf">0.0.0.0</span><span class="p">:</span><span class="mi">15675</span><span class="o">-&gt;</span><span class="mi">15675</span><span class="o">/</span><span class="n">tcp</span>   <span class="n">leaps_mosquitto</span>
<span class="mi">3</span><span class="n">d84cad7a913</span>   <span class="n">leapslabs</span><span class="o">/</span><span class="n">leaps_server</span><span class="p">:</span><span class="n">udk</span>      <span class="s2">"/app/leaps-server -…"</span>   <span class="mi">11</span> <span class="n">seconds</span> <span class="n">ago</span>   <span class="n">Up</span> <span class="mi">11</span> <span class="n">seconds</span>    <span class="mf">0.0.0.0</span><span class="p">:</span><span class="mi">7777</span><span class="o">-&gt;</span><span class="mi">7777</span><span class="o">/</span><span class="n">tcp</span><span class="p">,</span> <span class="mf">0.0.0.0</span><span class="p">:</span><span class="mi">7777</span><span class="o">-&gt;</span><span class="mi">7777</span><span class="o">/</span><span class="n">udp</span>    <span class="n">leaps_server</span>
<span class="mi">633</span><span class="n">c97e96f6e</span>   <span class="n">leapslabs</span><span class="o">/</span><span class="n">leaps_center</span><span class="p">:</span><span class="n">udk</span>      <span class="s2">"sh -c 'cd /app &amp;&amp;  …"</span>   <span class="mi">12</span> <span class="n">seconds</span> <span class="n">ago</span>   <span class="n">Up</span> <span class="mi">12</span> <span class="n">seconds</span>   <span class="mi">80</span><span class="o">/</span><span class="n">tcp</span><span class="p">,</span> <span class="mf">0.0.0.0</span><span class="p">:</span><span class="mi">80</span><span class="o">-&gt;</span><span class="mi">8080</span><span class="o">/</span><span class="n">tcp</span>                       <span class="n">leaps_center</span>
</pre></div>
</div>
</li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="6">
<li><p>Connect the <a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-gateway#leapsgateway"><span class="std std-ref">LEAPS Gateway</span></a> use <code class="docutils literal notranslate"><span class="pre">Linux</span></code> or <code class="docutils literal notranslate"><span class="pre">Raspberry</span> <span class="pre">Pi</span></code>.</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>Make sure there is a connection to Windows.</p></li>
<li><p>Refer to <a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-gateway#leapsgateway"><span class="std std-ref">LEAPS Gateway</span></a> setup on <code class="docutils literal notranslate"><span class="pre">Linux</span></code> or <code class="docutils literal notranslate"><span class="pre">Raspberry</span> <span class="pre">Pi</span></code> and, update the IP address accordingly. For example, <code class="docutils literal notranslate"><span class="pre">leaps-server-host</span></code> will be updated to <code class="docutils literal notranslate"><span class="pre">192.168.1.12</span></code>.</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="7">
<li><p>Mosquitto およびチェックメッセージ (オプション)</p></li>
</ol>
<blockquote>
<div><ul>
<li><p>システムで mosquitto_sub を使用します。メッセージを確認するには、ターミナルで次のコマンドを使用します</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">mosquitto_sub</span> <span class="o">-</span><span class="n">p</span> <span class="mi">1883</span> <span class="o">-</span><span class="n">d</span> <span class="o">-</span><span class="n">v</span> <span class="o">-</span><span class="n">t</span> <span class="s1">'#'</span>
</pre></div>
</div>
</li>
<li><p>このコマンドは Mosquitto MQTT ブローカーに接続し、受信したすべてのメッセージを表示します)。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="8">
<li><p>IP アドレス経由で <a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> にアクセスします。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>コンピュータの Web ブラウザを使用します。</p></li>
<li><p><a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> にアクセスするには、IP アドレスまたは <span class="red-text">localhost</span> を入力します。</p></li>
</ul>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/docker_leaps_center_login.png"><img alt="../../../_images/docker_leaps_center_login.png" src="/docs-assets/ja/_images/docker_leaps_center_login.png" style="width: 762.4000000000001px; height: 370.8px;"></a>
</div>
</div></blockquote>
<ol class="arabic simple" start="9">
<li><p><a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> にログインします。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>ユーザー名 <span class="red-text">admin</span>、パスワード <span class="red-text">admin</span> を使用してログインします。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="10">
<li><p><a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> を使用してネットワークを準備します。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>デモを設定します: <a class="reference internal" href="/docs/ja/udk/udk-start/twr-rtls-and-data-telemetry-demo#twr-rtls-and-data-telemetry-demo"><span class="std std-ref">TWR RTLS およびデータ遠隔測定デモ</span></a> または <a class="reference internal" href="/docs/ja/udk/udk-start/uplink-tdoa-rtls-demo#uplink-tdoa-rtls-demo"><span class="std std-ref">アップリンク TDoA RTLS デモ</span></a>。</p></li>
<li><p>デフォルトでは、ネットワーク ID は <code class="docutils literal notranslate"><span class="pre">0x1234</span></code> になります。</p></li>
</ul>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/docker_network_demo01.jpg"><img alt="../../../_images/docker_network_demo01.jpg" src="/docs-assets/ja/_images/docker_network_demo01.jpg" style="width: 360.0px; height: 800.0px;"></a>
</div>
</div></blockquote>
<ol class="arabic simple" start="11">
<li><p><a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> でネットワークを構成します。</p></li>
</ol>
<blockquote>
<div><ul>
<li><p><a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> のネットワーク設定を確認して、ネットワーク ID と一致するようにしてください。</p></li>
<li><p>PC の IP アドレスとして構成された正しいホストを確認してください。</p></li>
<li><p>この例では、ネットワーク ID は <code class="docutils literal notranslate"><span class="pre">0x1234</span></code>、ホストは <code class="docutils literal notranslate"><span class="pre">192.168.1.12</span></code> です。</p>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/docker_leaps_center_config_network.png"><img alt="../../../_images/docker_leaps_center_config_network.png" src="/docs-assets/ja/_images/docker_leaps_center_config_network.png" style="width: 626.4000000000001px; height: 409.6px;"></a>
</div>
<ul class="simple">
<li><p>アプリケーションを使用してノードとネットワークを構成および視覚化する方法の詳細については、<a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> および <a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> を参照してください。</p></li>
</ul>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/docker_leaps_center_network.png"><img alt="../../../_images/docker_leaps_center_network.png" src="/docs-assets/ja/_images/docker_leaps_center_network.png" style="width: 764.4000000000001px; height: 373.20000000000005px;"></a>
</div>
</li>
</ul>
</div></blockquote>
<p>これで、システムは正常にセットアップされ、構成されました。楽しく使ってください！</p>
</div>
</div>
</div>


           </div>
