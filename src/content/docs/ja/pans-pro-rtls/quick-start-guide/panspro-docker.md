---
title: "PANS PRO Docker"
lang: ja
slug: "pans-pro-rtls/quick-start-guide/panspro-docker"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/pans-pro-rtls/quick-start-guide/panspro-docker/"
order: 90
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="pans-pro-docker">
<span id="panspro-docker"></span><h1>PANS PRO Docker</h1>
<p>このページには以下が含まれます:</p>
<blockquote>
<div><ul class="simple">
<li><p>PANS PRO Docker パッケージ。</p></li>
<li><p>システム要件に関する情報。</p></li>
<li><p>PANS PRO Docker のインストール方法に関する説明。</p></li>
</ul>
</div></blockquote>
<p>インストールは迅速かつ簡単で、一度行うだけで済みます。</p>
<div class="admonition-disclaimer admonition">
<p class="admonition-title">免責事項</p>
<p><a class="reference internal" href="#panspro-docker"><span class="std std-ref">PANS PRO Docker</span></a> のインストールは専門家のみを対象としています。デモ目的の場合は、 <a class="reference internal" href="/docs/ja/pans-pro-rtls/quick-start-guide/panspro-rpi#panspro-rpi"><span class="std std-ref">PANS PRO Raspberry Pi</span></a> の方がはるかに優れたオプションです。</p>
</div>
<p><a class="reference external" href="https://docs.docker.com/">Docker</a> の詳細については、公式 Docker にアクセスしてください。</p>
<p><strong>システム要件</strong></p>
<blockquote>
<div><ul class="simple">
<li><p>システム要件は、<a class="reference external" href="https://docs.docker.com/desktop/install/windows-install/#system-requirements">Linux 上の Docker デスクトップ</a> または <a class="reference external" href="https://docs.docker.com/desktop/install/windows-install/#system-requirements">Windows 上の Docker デスクトップ</a> に従います。</p></li>
<li><p>デスクトップ デバイス: <strong>2 GB の空きメモリが必要です</strong>。</p></li>
<li><p>Windows では、WSL のインストールにより 2GB の RAM が永続的に消費されます。これは Ubuntu WSL に割り当てられます。</p></li>
<li><p><em>推奨: 検証するセット (少なくとも 5 台のデバイス)。</em></p></li>
<li><p><em>推奨: デバイスに電力を供給するためのバッテリーまたは Micro USB ケーブル。</em></p></li>
<li><p><em>推奨:</em> <a class="reference internal" href="/docs/ja/pans-pro-rtls/infrastructure/pans-pro-manager#pans-pro-manager"><span class="std std-ref">PANS PRO Manager</span></a> <em>デバイスを構成します。</em></p></li>
</ul>
</div></blockquote>
<p id="uidocker"><strong>セットアップ手順</strong></p>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-0" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-0">
Linux</label><div class="sd-tab-content docutils">
<p>このシステムは、AMD64、ARM64、および ARM32 アーキテクチャと互換性があります。</p>
<ol class="arabic simple">
<li><p>PANS PRO Docker をダウンロード</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>ダウンロード パッケージについては、<a class="reference external" href="mailto:apps-support%40leapslabs.com">apps-support<span>@</span>leapslabs<span>.</span>com</a> までお問い合わせください。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="2">
<li><p>PANS PRO Docker アーカイブを抽出します</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>ターミナルに次のように入力します: <span class="red-text">$ unzip PANS-PRO-DOCKER-LINUX.zip -d /path/to/directory</span></p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="3">
<li><p>オペレーティング システムに Docker をインストールします。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p><span class="red-text">leaps_docker_install.sh</span> スクリプトを実行して、オペレーティング システムに Docker をインストールします。</p></li>
</ul>
<p>たとえば、Ubuntu (Linux) の場合:</p>
<blockquote>
<div><div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">source</span> <span class="n">leaps_docker_install</span><span class="o">.</span><span class="n">sh</span>
</pre></div>
</div>
</div></blockquote>
<ul class="simple">
<li><p>インストール後、OS を再起動して、Docker が正しく構成されていることを確認します。</p></li>
<li><p>詳細な手順については、公式の <a class="reference external" href="https://docs.docker.com/get-docker/">Docker ドキュメント</a> を参照してください。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="4">
<li><p>IP アドレスを使用して正しい構成を更新します。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>ゲートウェイ ボードの IP アドレスを指すように、 <code class="docutils literal notranslate"><span class="pre">leaps-server.conf</span></code> の <code class="docutils literal notranslate"><span class="pre">mqtt_host</span></code> を更新します。シェル経由でアドレスを取得します。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="5">
<li><p>すべての LEAPS Docker コンテナを実行します。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p><span class="red-text">leaps_docker_run_all.sh</span> スクリプトを実行します。これにより、<a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a>、<a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-server#leapsserver"><span class="std std-ref">LEAPS Server</span></a>、および Mosquitto (MQTT ブローカー) に必要な Docker コンテナがプルされて実行されます。</p></li>
</ul>
<p>たとえば、Ubuntu (Linux) の場合:</p>
<blockquote>
<div><div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">source</span> <span class="n">leaps_docker_run_all</span><span class="o">.</span><span class="n">sh</span>
</pre></div>
</div>
</div></blockquote>
<ul class="simple">
<li><p><span class="red-text">docker ps</span> コマンドを実行し、すべてのコンテナが正常に起動し、使用できる状態になっていることを確認します。</p></li>
</ul>
<p>たとえば、Ubuntu (Linux) の場合:</p>
<blockquote>
<div><div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">docker</span> <span class="n">ps</span>

<span class="n">CONTAINER</span> <span class="n">ID</span>   <span class="n">IMAGE</span>                       <span class="n">COMMAND</span>                  <span class="n">CREATED</span>          <span class="n">STATUS</span>          <span class="n">PORTS</span>                                              <span class="n">NAMES</span>
<span class="mi">6</span><span class="n">f2ae0c87d65</span>   <span class="n">leapslabs</span><span class="o">/</span><span class="n">leaps_mosquitto</span><span class="p">:</span><span class="n">latest</span>   <span class="s2">"/docker-entrypoint.…"</span>   <span class="mi">9</span> <span class="n">seconds</span> <span class="n">ago</span>    <span class="n">Up</span> <span class="mi">9</span> <span class="n">seconds</span>    <span class="mf">0.0.0.0</span><span class="p">:</span><span class="mi">1883</span><span class="o">-&gt;</span><span class="mi">1883</span><span class="o">/</span><span class="n">tcp</span><span class="p">,</span> <span class="mf">0.0.0.0</span><span class="p">:</span><span class="mi">15675</span><span class="o">-&gt;</span><span class="mi">15675</span><span class="o">/</span><span class="n">tcp</span>   <span class="n">leaps_mosquitto</span>
<span class="mi">3</span><span class="n">d84cad7a913</span>   <span class="n">leapslabs</span><span class="o">/</span><span class="n">leaps_server</span><span class="p">:</span><span class="n">latest</span>      <span class="s2">"/app/leaps-server -…"</span>   <span class="mi">10</span> <span class="n">seconds</span> <span class="n">ago</span>   <span class="n">Up</span> <span class="mi">9</span> <span class="n">seconds</span>    <span class="mf">0.0.0.0</span><span class="p">:</span><span class="mi">7777</span><span class="o">-&gt;</span><span class="mi">7777</span><span class="o">/</span><span class="n">tcp</span><span class="p">,</span> <span class="mf">0.0.0.0</span><span class="p">:</span><span class="mi">7777</span><span class="o">-&gt;</span><span class="mi">7777</span><span class="o">/</span><span class="n">udp</span>     <span class="n">leaps_server</span>
<span class="mi">633</span><span class="n">c97e96f6e</span>   <span class="n">leapslabs</span><span class="o">/</span><span class="n">leaps_center</span><span class="p">:</span><span class="n">latest</span>      <span class="s2">"sh -c 'cd /app &amp;&amp;  …"</span>   <span class="mi">10</span> <span class="n">seconds</span> <span class="n">ago</span>   <span class="n">Up</span> <span class="mi">10</span> <span class="n">seconds</span>   <span class="mi">80</span><span class="o">/</span><span class="n">tcp</span><span class="p">,</span> <span class="mf">0.0.0.0</span><span class="p">:</span><span class="mi">80</span><span class="o">-&gt;</span><span class="mi">8080</span><span class="o">/</span><span class="n">tcp</span>                       <span class="n">leaps_center</span>
</pre></div>
</div>
</div></blockquote>
</div></blockquote>
<ol class="arabic simple" start="6">
<li><p><a class="reference internal" href="/docs/ja/pans-pro-rtls/quick-start-guide/panspro-rtls-setup#pans-pro-demo"><span class="std std-ref">PANS PRO デモ</span></a> のようにネットワークを準備し、ゲートウェイ ボードを接続します。</p></li>
<li><p>Mosquitto およびチェックメッセージ (オプション)</p></li>
</ol>
<blockquote>
<div><ul>
<li><p>システムで mosquitto_sub を使用します。</p></li>
<li><p>メッセージを確認するには、ターミナルで次のコマンドを使用します (このコマンドは Mosquitto MQTT ブローカーに接続し、受信したすべてのメッセージを表示します)。</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">mosquitto_sub</span> <span class="o">-</span><span class="n">p</span> <span class="mi">1883</span> <span class="o">-</span><span class="n">d</span> <span class="o">-</span><span class="n">v</span> <span class="o">-</span><span class="n">t</span> <span class="s1">'#'</span>
</pre></div>
</div>
</li>
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
<a class="reference internal image-reference" href="../../../_images/leaps_center_login.png"><img alt="../../../_images/leaps_center_login.png" src="/docs-assets/ja/_images/leaps_center_login.png" style="width: 667.4499999999999px; height: 315.0px;"></a>
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
<li><p><a class="reference internal" href="/docs/ja/pans-pro-rtls/infrastructure/pans-pro-manager#pans-pro-manager"><span class="std std-ref">PANS PRO Manager</span></a> を使用してネットワークを準備します。</p></li>
<li><p><a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> でネットワークを構成します。</p></li>
</ol>
<blockquote>
<div><ul>
<li><p><a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> のネットワーク設定を確認して、ネットワーク ID と一致するようにしてください。</p></li>
<li><p>PC の IP アドレスとして構成された正しいホストを確認してください。</p>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/leaps_center_pans.png"><img alt="../../../_images/leaps_center_pans.png" class="align-center" src="/docs-assets/ja/_images/leaps_center_pans.png" style="width: 764.4000000000001px; height: 360.40000000000003px;"></a>
</div></blockquote>
</li>
<li><p>アプリケーションを使用してノードとネットワークを構成および視覚化する方法の詳細については、<a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> および <a class="reference internal" href="/docs/ja/pans-pro-rtls/infrastructure/pans-pro-manager#pans-pro-manager"><span class="std std-ref">PANS PRO Manager</span></a> を参照してください。</p></li>
</ul>
</div></blockquote>
<p>これで、システムは正常にセットアップされ、構成されました。楽しく使ってください！</p>
</div>
<input id="sd-tab-item-1" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-1">
Windows</label><div class="sd-tab-content docutils">
<ol class="arabic simple">
<li><p>PANS PRO Docker をダウンロードします。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>ダウンロード パッケージについては、<a class="reference external" href="mailto:apps-support%40leapslabs.com">apps-support<span>@</span>leapslabs<span>.</span>com</a> までお問い合わせください。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="2">
<li><p>PANS PRO Docker アーカイブを抽出します。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>WinZip や 7-Zip などのプログラムを使用して、ダウンロードした PANS PRO Docker zip ファイルを解凍します。</p></li>
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
<span class="mi">6</span><span class="n">f2ae0c87d65</span>   <span class="n">leapslabs</span><span class="o">/</span><span class="n">leaps_mosquitto</span><span class="p">:</span><span class="n">latest</span>   <span class="s2">"/docker-entrypoint.…"</span>   <span class="mi">9</span> <span class="n">seconds</span> <span class="n">ago</span>    <span class="n">Up</span> <span class="mi">9</span> <span class="n">seconds</span>    <span class="mf">0.0.0.0</span><span class="p">:</span><span class="mi">1883</span><span class="o">-&gt;</span><span class="mi">1883</span><span class="o">/</span><span class="n">tcp</span><span class="p">,</span> <span class="mf">0.0.0.0</span><span class="p">:</span><span class="mi">15675</span><span class="o">-&gt;</span><span class="mi">15675</span><span class="o">/</span><span class="n">tcp</span>   <span class="n">leaps_mosquitto</span>
<span class="mi">3</span><span class="n">d84cad7a913</span>   <span class="n">leapslabs</span><span class="o">/</span><span class="n">leaps_server</span><span class="p">:</span><span class="n">latest</span>      <span class="s2">"/app/leaps-server -…"</span>   <span class="mi">11</span> <span class="n">seconds</span> <span class="n">ago</span>   <span class="n">Up</span> <span class="mi">11</span> <span class="n">seconds</span>    <span class="mf">0.0.0.0</span><span class="p">:</span><span class="mi">7777</span><span class="o">-&gt;</span><span class="mi">7777</span><span class="o">/</span><span class="n">tcp</span><span class="p">,</span> <span class="mf">0.0.0.0</span><span class="p">:</span><span class="mi">7777</span><span class="o">-&gt;</span><span class="mi">7777</span><span class="o">/</span><span class="n">udp</span>    <span class="n">leaps_server</span>
<span class="mi">633</span><span class="n">c97e96f6e</span>   <span class="n">leapslabs</span><span class="o">/</span><span class="n">leaps_center</span><span class="p">:</span><span class="n">latest</span>      <span class="s2">"sh -c 'cd /app &amp;&amp;  …"</span>   <span class="mi">12</span> <span class="n">seconds</span> <span class="n">ago</span>   <span class="n">Up</span> <span class="mi">12</span> <span class="n">seconds</span>   <span class="mi">80</span><span class="o">/</span><span class="n">tcp</span><span class="p">,</span> <span class="mf">0.0.0.0</span><span class="p">:</span><span class="mi">80</span><span class="o">-&gt;</span><span class="mi">8080</span><span class="o">/</span><span class="n">tcp</span>                       <span class="n">leaps_center</span>
</pre></div>
</div>
</li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="6">
<li><p><a class="reference internal" href="/docs/ja/pans-pro-rtls/quick-start-guide/panspro-rtls-setup#pans-pro-demo"><span class="std std-ref">PANS PRO デモ</span></a> のようにネットワークを準備し、ゲートウェイ ボードを接続します。</p></li>
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
<ol class="arabic simple" start="8">
<li><p><a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> にログインします。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>ユーザー名 <span class="red-text">admin</span>、パスワード <span class="red-text">admin</span> を使用してログインします。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="9">
<li><p><a class="reference internal" href="/docs/ja/pans-pro-rtls/infrastructure/pans-pro-manager#pans-pro-manager"><span class="std std-ref">PANS PRO Manager</span></a> を使用してネットワークを準備します。</p></li>
<li><p><a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> でネットワークを構成します。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p><a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> のネットワーク設定を確認して、ネットワーク ID と一致するようにしてください。</p></li>
<li><p>PC の IP アドレスとして構成された正しいホストを確認してください。</p></li>
</ul>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/leaps_center_pans.png"><img alt="../../../_images/leaps_center_pans.png" src="/docs-assets/ja/_images/leaps_center_pans.png" style="width: 764.4000000000001px; height: 360.40000000000003px;"></a>
</div>
<ul class="simple">
<li><p>アプリケーションを使用してノードとネットワークを構成および視覚化する方法の詳細については、<a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> および <a class="reference internal" href="/docs/ja/pans-pro-rtls/infrastructure/pans-pro-manager#pans-pro-manager"><span class="std std-ref">PANS PRO Manager</span></a> を参照してください。</p></li>
</ul>
</div></blockquote>
<p>これで、システムは正常にセットアップされ、構成されました。楽しく使ってください！</p>
</div>
</div>
</div>


           </div>
