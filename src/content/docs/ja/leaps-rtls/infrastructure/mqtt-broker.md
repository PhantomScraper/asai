---
title: "MQTT Broker"
lang: ja
slug: "leaps-rtls/infrastructure/mqtt-broker"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/leaps-rtls/infrastructure/mqtt-broker/"
order: 72
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="mqtt-broker">
<span id="id1"></span><h1>MQTT Broker</h1>
<p>MQTTブローカーは、すべてのクライアントメッセージを受信し、適切な宛先クライアントにメッセージをルーティングするサーバーです。MQTTクライアントは、MQTTライブラリを実行し、ネットワーク経由でMQTTブローカーに接続する任意のデバイス（マイクロコントローラーから本格的なサーバーまで）です。</p>
<p>オープンソースのMQTTブローカーであるLEAPS Mosquittoは、Dockerイメージ <a class="reference external" href="https://hub.docker.com/_/eclipse-mosquitto">eclipse-mosquitto:1.5.11</a> のコピーで、カスタムの <code class="docutils literal notranslate"><span class="pre">mosquitto.conf</span></code> ファイルが <code class="docutils literal notranslate"><span class="pre">/mosquitto/config/mosquitto.conf</span></code> に統合されています。詳細については、<a class="reference external" href="https://hub.docker.com/_/eclipse-mosquitto">eclipse-mosquitto</a> を参照してください。</p>
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
<li><p>macOSでは、macOS 10.13以降でDocker Desktopを使用してください。ハードウェア要件としては、最低2GBのRAMに加え、十分なCPUとディスク容量が必要です。</p></li>
</ul>
<p>最新の情報については、<a class="reference external" href="https://docs.docker.com/">Docker</a> 公式ドキュメントを参照してください。</p>
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
<li><p>PCでコマンドプロンプトまたはターミナルウィンドウを開き、LEAPS Mosquitto Dockerパッケージをインストールします。次のコマンドを実行します。</p></li>
</ol>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">docker run -d -p 1883:1883/tcp -p 15675:15675 --name some_name leapslabs/leaps_mosquitto:latest mosquitto ---cfg /mosquitto/config/mosquitto.conf</span>
</pre></div>
</div>
<p><code class="docutils literal notranslate"><span class="pre">some_name</span></code> はコンテナに割り当てる名前、<code class="docutils literal notranslate"><span class="pre">tag</span></code> は必要な <code class="docutils literal notranslate"><span class="pre">leaps-mosquitto</span></code> のバージョンを指定するタグです。</p>
<ul class="simple">
<li><p>推奨される走行オプション</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">--user</span> <span class="pre">$(id</span> <span class="pre">-u):$(id</span> <span class="pre">-g)</span></code> 特定のユーザーとグループの下でインスタンスを実行する。</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">--restart</span> <span class="pre">unless-stopped</span></code> サーバーがクラッシュした場合にインスタンスを自動的に再起動する。</p></li>
</ul>
</li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="3">
<li><p>LEAPS Mosquittoのインストールプロセスが開始されます。</p></li>
</ol>
<blockquote>
<div><p>たとえば、Ubuntu (Linux) の場合:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">docker run -d -p 1883:1883/tcp -p 15675:15675 --name leaps_mosquitto leapslabs/leaps_mosquitto:latest mosquitto ---cfg /mosquitto/config/mosquitto.conf</span>

<span class="go">Unable to find image 'leapslabs/leaps_mosquitto:latest' locally</span>
<span class="go">latest: Pulling from leapslabs/leaps_mosquitto</span>
<span class="go">f7dab3ab2d6e: Already exists</span>
<span class="go">2a0a6c9fa787: Already exists</span>
<span class="go">a211eff771d6: Already exists</span>
<span class="go">d362e2a9c11b: Already exists</span>
<span class="go">Digest: sha256:a97752d6e2d81e2701c7cd5f807eb4256322983f8aa3135da8235b647e6a9b4e</span>
<span class="go">Status: Downloaded newer image for leapslabs/leaps_mosquitto:latest</span>
<span class="go">1f526e755ad9a356c439003b93c200802628ae9bc046827e7327d0334804b565</span>
</pre></div>
</div>
</div></blockquote>
<ol class="arabic simple" start="4">
<li><p>インストールが成功したことを確認し、実行する：</p></li>
</ol>
<blockquote>
<div><p>たとえば、Ubuntu (Linux) の場合:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">docker ps</span>

<span class="go">CONTAINER ID   IMAGE                      COMMAND                  CREATED          STATUS                          PORTS     NAMES</span>
<span class="go">b1145b72db35   leapslabs/leaps_mosquitto:latest  "sh -c 'cd /app &amp;&amp;  …"   37 seconds ago   11 seconds ago                            leaps_mosquitto</span>
</pre></div>
</div>
</div></blockquote>
<p>これで、LEAPS MosquittoがPCにインストールされ、起動しました。</p>
</div>
</div>
<hr class="docutils">
<div class="section" id="getting-started">
<h2>はじめに</h2>
<div class="section" id="leaps-mosquitto-docker">
<h3>LEAPS Mosquitto Docker</h3>
<ul class="simple">
<li><p>LEAPS Mosquittoを起動します。<code class="docutils literal notranslate"><span class="pre">docker</span> <span class="pre">start</span> <span class="pre">leaps_mosquitto</span></code> を実行します。</p></li>
<li><p>LEAPS Mosquittoを停止します。<code class="docutils literal notranslate"><span class="pre">docker</span> <span class="pre">stop</span> <span class="pre">leaps_mosquitto</span></code> を実行します。</p></li>
<li><p>LEAPS Mosquittoを再起動します。<code class="docutils literal notranslate"><span class="pre">docker</span> <span class="pre">restart</span> <span class="pre">leaps_mosquitto</span></code> を実行します。</p></li>
<li><p>LEAPS Mosquittoを削除します。<code class="docutils literal notranslate"><span class="pre">docker</span> <span class="pre">rm</span> <span class="pre">--force</span> <span class="pre">leaps_mosquitto</span></code> を実行します。</p></li>
</ul>
</div>
</div>
<hr class="docutils">
<div class="section" id="customized-options">
<h2>カスタマイズオプション</h2>
<blockquote>
<div><p><strong>必須オプション</strong></p>
<blockquote>
<div><ul class="simple">
<li><p>ポート1883 - デフォルトのリスナーポート</p></li>
<li><p>リスナー1884 - 1884でリスナーを有効化</p></li>
<li><p>リスナー15675 - 15675でリスナーを有効化</p></li>
</ul>
</div></blockquote>
<p><strong>推奨オプション</strong></p>
<blockquote>
<div><ul class="simple">
<li><p>user mosquitto - ルート権限を削除</p></li>
<li><p>max_inflight_messages 200 - 一度に送信できるQoS1の数が少ないため、クライアントあたりのインファイティングQoSメッセージ数を増やします。</p></li>
<li><p>max_queued_messages 1000 - クライアントあたりのキューに保持するQoS1およびQoS2メッセージの最大数を、現在処理中のメッセージ数より増やします。</p></li>
<li><p>allow_zero_length_clientid true - クライアントIDの長さを0にすることを許可</p></li>
<li><p>persistent_client_expiration 14d - 設計が不適切なクライアントからの自動保護</p></li>
</ul>
</div></blockquote>
</div></blockquote>
</div>
<div class="section" id="troubleshooting">
<h2>トラブルシューティング</h2>
<ul class="simple">
<li><p>LEAPS Mosquittoを再起動するには、以下のコマンド``docker restart leaps_mosquitto``を使用します。</p></li>
<li><p>LEAPS Mosquittoの実行中にログを確認し、Dockerデスクトップを開いてleaps_mosquittoコンテナを選択します。</p></li>
</ul>
</div>
</div>


           </div>
