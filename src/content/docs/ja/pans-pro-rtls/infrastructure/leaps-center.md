---
title: "LEAPS Center"
lang: ja
slug: "pans-pro-rtls/infrastructure/leaps-center"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/pans-pro-rtls/infrastructure/leaps-center/"
order: 98
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-center">
<span id="pans-pro-center"></span><h1>LEAPS Center</h1>
<p><a class="reference internal" href="#pans-pro-center"><span class="std std-ref">LEAPS Center</span></a> は、デバイス管理、ネットワーク管理、ネットワーク全体の位置情報と遠隔測定データの可視化を提供するウェブアプリケーションです。</p>
<div class="section" id="key-features">
<h2>主な機能</h2>
<ul class="simple">
<li><p>2Dと3Dのグリッドはリアルタイムで位置を更新し、ネットワーク内のデバイスを視覚化します。</p></li>
<li><p>その他の便利な機能には、ユーザー管理、ゾーン管理、ゾーン履歴、フロアプラン管理、ポジション履歴、ポジションヒートマップがあります。</p></li>
<li><p>The <a class="reference internal" href="#pans-pro-center"><span class="std std-ref">LEAPS Center</span></a> は <a class="reference external" href="https://mosquitto.org/">MQTT Broker</a> を介して <a class="reference internal" href="/docs/ja/pans-pro-rtls/infrastructure/leaps-server#pans-pro-server"><span class="std std-ref">LEAPS Server</span></a> と相互接続します。LinuxとWindowsのプラットフォーム上でサービスとして動作する。</p></li>
</ul>
</div>
<div class="section" id="installation">
<h2>インストール</h2>
<div class="section" id="system-requirements">
<h3>システム要件</h3>
<p>Dockerのシステム要件はOSによって異なります。</p>
<ul class="simple">
<li><p>Linuxの場合、64ビット・アーキテクチャ、互換性のあるカーネル・バージョン、特定のカーネル機能が必要だ。</p></li>
<li><p>Windowsでは、仮想化を有効にしたWindows 10上でDocker Desktopを使用します</p></li>
<li><p>macOSの場合は、macOS 10.13以降のDocker Desktopを使用してください。ハードウェアに関しては、最低2GBのRAMと十分なCPUとディスク容量を推奨します。</p></li>
</ul>
<div class="admonition note">
<p class="admonition-title">注釈</p>
<p>最新の詳細については <a class="reference external" href="https://docs.docker.com/">Docker</a> 公式ドキュメントを参照してください。</p>
</div>
</div>
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
<li><p>コンフィギュレーション・パッケージを準備する。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p><a class="reference internal" href="#pans-configuration-files"><span class="std std-ref">設定ファイル</span></a> を含むleaps_centerディレクトリを作成します。</p>
<ul>
<li><p>leaps-center-web.conf</p></li>
<li><p>アプリケーション.特性</p></li>
<li><p>leaps-center-history.properties</p></li>
<li><p>leaps-center-web.properties</p></li>
</ul>
</li>
<li><p>または、LEAPS Center設定パッケージをダウンロードすることもできます(<a class="reference external" href="https://drive.google.com/file/d/1T-TECozBs9O87w4sCUHM1bXtLkd6jvHM/view?usp=drive_link">LEAPS_CENTER_DOCKER.zip</a>)。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="3">
<li><p>PCでコマンドプロンプトまたはターミナルウィンドウを開く。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>LEAPS Center構成パッケージを解凍したディレクトリに移動します。</p></li>
</ul>
<p>たとえば、Ubuntu (Linux) の場合:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">cd LEAPS_CENTER_DOCKER/</span>
</pre></div>
</div>
</div></blockquote>
<ol class="arabic simple" start="4">
<li><p>LEAPS Center Dockerパッケージをインストールし、実行します：</p></li>
</ol>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">docker run -d -p 80:8080/tcp --name some_name -v /path/to/data/data/:/app/data/ -e LEAPS_CENTER_HOME=/app/data/ leapslabs/leaps_center:tag sh -c "cd /app &amp;&amp;  java -jar leaps-center-web.jar"</span>
</pre></div>
</div>
<p>ここで、<code class="docutils literal notranslate"><span class="pre">some_name</span></code> はコンテナに割り当てたい名前であり、<code class="docutils literal notranslate"><span class="pre">tag</span></code> は希望する <code class="docutils literal notranslate"><span class="pre">leaps-center-web</span></code> バージョンを指定するタグである。</p>
<p>leaps_centerイメージは、設定ファイル、アプリケーションログ、設定/ノード履歴データベースを格納する外部マウントフォルダと共に動作する必要があります。</p>
<p>オプション <code class="docutils literal notranslate"><span class="pre">-v</span> <span class="pre">/path/to/data/:/app/data/</span></code> は <code class="docutils literal notranslate"><span class="pre">/path/to/data/</span></code> にあるフォルダを内部の <code class="docutils literal notranslate"><span class="pre">/app/data</span></code> フォルダにマウントします。データフォルダには以下のファイルが必要です。</p>
<ul class="simple">
<li><p>推奨される走行オプション</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">--user</span> <span class="pre">$(id</span> <span class="pre">-u):$(id</span> <span class="pre">-g)</span></code> 特定のユーザーとグループの下でインスタンスを実行する。</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">--restart</span> <span class="pre">unless-stopped</span></code> サーバーがクラッシュした場合にインスタンスを自動的に再起動する。</p></li>
</ul>
</li>
<li><p>走行オプション</p>
<ul>
<li><p><code class="docutils literal notranslate"><span class="pre">--security-opt</span> <span class="pre">seccomp=unconfined</span></code> このオプションは32ビットのRaspberry Piイメージ（Raspbian）で必要です。なぜなら、Dockerイメージに悪影響を与える（MQTTサーバーに接続できない）バグのある旧式のseccompライブラリが含まれているからです。このオプションにより、この問題を上書きすることができます。</p></li>
</ul>
</li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="5">
<li><p>LEAPS Centerのインストール処理が開始されます。</p></li>
</ol>
<blockquote>
<div><p>たとえば、Ubuntu (Linux) の場合:</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">docker run -d -p 80:8080/tcp --name leaps_center -v $PWD/leaps_center/:/app/data/ -e LEAPS_CENTER_HOME=/app/data/ leapslabs/leaps_center:latest sh -c "cd /app &amp;&amp;  java -jar leaps-center-web.jar"</span>

<span class="go">Unable to find image 'leapslabs/leaps_center:latest' locally</span>
<span class="go">latest: Pulling from leapslabs/leaps_center</span>
<span class="go">a458657ccc71: Pull complete</span>
<span class="go">Digest: sha256:a19b127656d41d8607f043c2c83924e5b9a5cbd4dc23cfbed070be3b9cfc6b9a</span>
<span class="go">Status: Downloaded newer image for leapslabs/leaps_center:latest</span>
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
<span class="go">b1145b72db35   leapslabs/leaps_center:latest   "sh -c 'cd /app &amp;&amp;  …"   37 seconds ago   11 seconds ago                            leaps_center</span>
</pre></div>
</div>
</div></blockquote>
<ol class="arabic simple" start="7">
<li><p>ウェブブラウザを開き、次の <a class="reference external" href="http://localhost:80">http://localhost:80</a>；LEAPS Centerアプリケーションがウェブブラウザにロードされます。</p></li>
</ol>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/lc_login.png"><img alt="../../../_images/lc_login.png" class="align-center" src="/docs-assets/ja/_images/lc_login.png" style="width: 716.4px; height: 520.2px;"></a>
</div></blockquote>
<p>これでLEAPS CenterのPCへのインストールと起動は完了です。</p>
</div>
</div>
<div class="section" id="configuration-files">
<span id="pans-configuration-files"></span><h2>設定ファイル</h2>
<ul>
<li><p>leaps-center-web.conf</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">JAVA_OPTS="-Xms256m -Xmx512m -Xss256k"</span>
</pre></div>
</div>
</li>
<li><p>アプリケーション.特性</p></li>
<li><p>leaps-center-history.properties</p></li>
<li><p>leaps-center-web.properties</p>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-3" name="sd-tab-set-1" type="radio">
<label class="sd-tab-label" for="sd-tab-item-3">
アプリケーション.特性</label><div class="sd-tab-content docutils">
<p>この設定ファイルは、アプリケーションのロギングを制御する。</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">spring.main.banner-mode=OFF</span>

<span class="go">logging.level.root=OFF</span>
<span class="go">logging.level.global.leaps.center.mqtt=OFF</span>
<span class="go">logging.level.global.leaps.center.init=OFF</span>
<span class="go">logging.level.global.leaps.center.service=OFF</span>
<span class="go">logging.level.global.leaps.center.history.filter=OFF</span>
<span class="go">logging.level.global.leaps.center.history.service=OFF</span>
<span class="go">logging.level.global.leaps.center.history=OFF</span>
<span class="go">logging.level.global.leaps.center.web.component=OFF</span>
<span class="go">logging.level.global.leaps.center.web.rest=OFF</span>
<span class="go">logging.level.global.leaps.center.web.sse=OFF</span>
<span class="go">logging.level.global.leaps.center.web=OFF</span>
<span class="go">logging.level.global.leaps.center=OFF</span>
</pre></div>
</div>
</div>
<input id="sd-tab-item-4" name="sd-tab-set-1" type="radio">
<label class="sd-tab-label" for="sd-tab-item-4">
leaps-center-history.properties</label><div class="sd-tab-content docutils">
<p>この設定ファイルはノードの位置履歴ロギングを制御します。</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">#</span>
<span class="gp">#       </span>LEAPS<span class="w"> </span>-<span class="w"> </span>Low<span class="w"> </span>Energy<span class="w"> </span>Accurate<span class="w"> </span>Positioning<span class="w"> </span>System<span class="w"> </span>-<span class="w"> </span>LEAPS<span class="w"> </span>Center.
<span class="gp">#</span>
<span class="gp">#       </span>Copyright<span class="w"> </span><span class="o">(</span>c<span class="o">)</span><span class="w"> </span><span class="m">2016</span>-2021,<span class="w"> </span>LEAPS.
<span class="gp">#</span>
<span class="gp">#       </span>Licensed<span class="w"> </span>under<span class="w"> </span>the<span class="w"> </span>Apache<span class="w"> </span>License,<span class="w"> </span>Version<span class="w"> </span><span class="m">2</span>.0<span class="w"> </span><span class="o">(</span>the<span class="w"> </span><span class="s2">"License"</span><span class="o">)</span><span class="p">;</span>
<span class="gp">#       </span>You<span class="w"> </span>may<span class="w"> </span>not<span class="w"> </span>use<span class="w"> </span>this<span class="w"> </span>file<span class="w"> </span>except<span class="w"> </span><span class="k">in</span><span class="w"> </span>compliance<span class="w"> </span>with<span class="w"> </span>the<span class="w"> </span>License.
<span class="gp">#       </span>You<span class="w"> </span>may<span class="w"> </span>obtain<span class="w"> </span>a<span class="w"> </span>copy<span class="w"> </span>of<span class="w"> </span>the<span class="w"> </span>License<span class="w"> </span>at
<span class="gp">#</span>
<span class="gp">#       </span>http://www.apache.org/licenses/LICENSE-2.0
<span class="gp">#</span>
<span class="gp">#       </span>Unless<span class="w"> </span>required<span class="w"> </span>by<span class="w"> </span>applicable<span class="w"> </span>law<span class="w"> </span>or<span class="w"> </span>agreed<span class="w"> </span>to<span class="w"> </span><span class="k">in</span><span class="w"> </span>writing,<span class="w"> </span>software
<span class="gp">#       </span>distributed<span class="w"> </span>under<span class="w"> </span>the<span class="w"> </span>License<span class="w"> </span>is<span class="w"> </span>distributed<span class="w"> </span>on<span class="w"> </span>an<span class="w"> </span><span class="s2">"AS IS"</span><span class="w"> </span>BASIS,
<span class="gp">#       </span>WITHOUT<span class="w"> </span>WARRANTIES<span class="w"> </span>OR<span class="w"> </span>CONDITIONS<span class="w"> </span>OF<span class="w"> </span>ANY<span class="w"> </span>KIND,<span class="w"> </span>either<span class="w"> </span>express<span class="w"> </span>or<span class="w"> </span>implied.
<span class="gp">#       </span>See<span class="w"> </span>the<span class="w"> </span>License<span class="w"> </span><span class="k">for</span><span class="w"> </span>the<span class="w"> </span>specific<span class="w"> </span>language<span class="w"> </span>governing<span class="w"> </span>permissions<span class="w"> </span>and
<span class="gp">#       </span>limitations<span class="w"> </span>under<span class="w"> </span>the<span class="w"> </span>License.
<span class="gp">#</span>

<span class="gp"># </span><span class="nb">history</span><span class="w"> </span>enabled<span class="w"> </span><span class="o">(</span>default<span class="w"> </span><span class="nb">false</span><span class="o">)</span>
<span class="go">history.enabled=false</span>
<span class="go">history.position.enabled=true</span>
<span class="go">history.zone.enabled=true</span>

<span class="gp"># </span>use<span class="w"> </span>node<span class="w"> </span>position<span class="w"> </span>message<span class="w"> </span>timestamp<span class="w"> </span><span class="o">(</span>default<span class="w"> </span><span class="nb">true</span><span class="o">)</span>
<span class="go">history.use.position.timestamp=false</span>

<span class="gp"># </span><span class="o">=======================================================================================================</span>
<span class="gp"># </span>Export<span class="w"> </span><span class="nv">Options</span>
<span class="gp"># </span><span class="o">=======================================================================================================</span>

<span class="gp"># </span>add<span class="w"> </span>headers<span class="w"> </span><span class="o">(</span>default<span class="w"> </span><span class="nb">false</span><span class="o">)</span>
<span class="go">history.export.headers=false</span>

<span class="gp"># </span>maximum<span class="w"> </span>number<span class="w"> </span>of<span class="w"> </span>records<span class="w"> </span><span class="o">(</span>default<span class="w"> </span><span class="m">1000000</span><span class="o">)</span>
<span class="go">history.export.max.lines=1000000</span>

<span class="gp"># </span>compress<span class="w"> </span><span class="nb">export</span><span class="w"> </span>file<span class="w"> </span><span class="o">(</span>default<span class="w"> </span><span class="nb">true</span><span class="o">)</span>
<span class="go">history.export.compress=true</span>

<span class="gp"># </span>number<span class="w"> </span>of<span class="w"> </span>decimal<span class="w"> </span>places<span class="w"> </span><span class="k">for</span><span class="w"> </span>x,<span class="w"> </span>y,<span class="w"> </span>z<span class="w"> </span>values<span class="w"> </span><span class="o">(</span>default<span class="w"> </span><span class="m">4</span><span class="o">)</span>
<span class="go">history.export.position.decimal.places=2</span>

<span class="gp"># </span>format<span class="w"> </span>network<span class="w"> </span>id<span class="w"> </span>to<span class="w"> </span>hex<span class="w"> </span>value<span class="w"> </span><span class="o">(</span>default<span class="w"> </span><span class="nb">true</span><span class="o">)</span>
<span class="go">history.export.hex.network.id=true</span>

<span class="gp"># </span>format<span class="w"> </span>node<span class="w">  </span>ID<span class="w"> </span>to<span class="w"> </span>hex<span class="w"> </span>value<span class="w"> </span><span class="o">(</span>default<span class="w"> </span><span class="nb">true</span><span class="o">)</span>
<span class="go">history.export.hex.node.id=true</span>

<span class="gp"># </span><span class="o">=======================================================================================================</span>
<span class="gp"># </span>Position<span class="w"> </span>History<span class="w"> </span><span class="nv">Options</span>
<span class="gp"># </span><span class="o">=======================================================================================================</span>

<span class="gp"># </span>interval<span class="w"> </span><span class="nb">time</span><span class="w"> </span>to<span class="w"> </span>add<span class="w"> </span>a<span class="w"> </span><span class="nb">history</span><span class="w"> </span>record<span class="w"> </span><span class="o">(</span>default<span class="w"> </span><span class="m">10000</span><span class="o">)</span>
<span class="go">history.node.position.interval.time=10000</span>

<span class="gp"># </span>minimun<span class="w"> </span>quality<span class="w"> </span>value<span class="w"> </span><span class="o">(</span>default<span class="w"> </span><span class="m">0</span><span class="o">)</span>
<span class="go">history.node.position.min.quality=0</span>

<span class="gp"># </span><span class="o">=======================================================================================================</span>
<span class="gp"># </span>Heatmap<span class="w"> </span><span class="nv">Options</span>
<span class="gp"># </span><span class="o">=======================================================================================================</span>
<span class="gp"># </span>maximum<span class="w"> </span>number<span class="w"> </span>of<span class="w"> </span>records<span class="w"> </span><span class="k">for</span><span class="w"> </span>heatmap<span class="w"> </span><span class="o">(</span>default<span class="w"> </span><span class="m">100000</span><span class="o">)</span>
<span class="go">heatmap.max.results=100000</span>

<span class="gp"># </span><span class="o">=======================================================================================================</span>
<span class="gp"># </span>Purge<span class="w"> </span><span class="nv">Options</span>
<span class="gp"># </span><span class="o">=======================================================================================================</span>

<span class="gp"># </span><span class="nb">time</span><span class="w"> </span>to<span class="w"> </span>purge<span class="w"> </span>database<span class="w"> </span>records<span class="w"> </span><span class="k">in</span><span class="w"> </span>days<span class="w"> </span><span class="o">(</span>default<span class="w"> </span><span class="m">30</span><span class="w"> </span>days<span class="o">)</span>
<span class="go">history.purge.time=30</span>

<span class="gp"># </span>backup<span class="w"> </span>purged<span class="w"> </span>records<span class="w"> </span>to<span class="w"> </span>a<span class="w"> </span>file<span class="w"> </span><span class="k">in</span><span class="w"> </span>/history<span class="w"> </span>folder<span class="w"> </span><span class="o">(</span>default<span class="w"> </span><span class="nb">false</span><span class="o">)</span>
<span class="go">history.purge.backup.records=true</span>

<span class="gp"># </span>max<span class="w"> </span>number<span class="w"> </span>of<span class="w"> </span>backup<span class="w"> </span>files<span class="w"> </span><span class="o">(</span>default<span class="w"> </span><span class="m">10</span><span class="o">)</span>
<span class="go">history.purge.max.backup.files=5</span>

<span class="gp"># </span><span class="o">=======================================================================================================</span>
<span class="gp"># </span>DBMS<span class="w"> </span><span class="o">(</span>SQLITE,<span class="w"> </span>POSTGRESQL,<span class="w"> </span>MY_SQL,<span class="w"> </span>ORACLE,<span class="w"> </span>SQL_SERVER<span class="w"> </span>or<span class="w"> </span>CUSTOM<span class="o">)</span>
<span class="gp"># </span><span class="o">=======================================================================================================</span>

<span class="gp"># </span>History<span class="w"> </span>-<span class="w"> </span>SQLite<span class="w"> </span>Database<span class="w"> </span>Example<span class="w"> </span><span class="o">(</span>default<span class="o">)</span>.
<span class="gp"># </span>history.dbms<span class="o">=</span>SQLITE
<span class="gp"># </span>history.db.jdbc.url<span class="o">=</span>jdbc:sqlite:leaps-center-history.db
<span class="gp"># </span>history.db.username<span class="o">=</span>
<span class="gp"># </span>history.db.password<span class="o">=</span>

<span class="gp"># </span>History<span class="w"> </span>-<span class="w"> </span>PostgreSQL<span class="w"> </span>Database<span class="w"> </span>Example
<span class="gp"># </span>history.dbms<span class="o">=</span>POSTGRESQL
<span class="gp"># </span>history.db.jdbc.url<span class="o">=</span>jdbc:postgresql://localhost:5432/leaps_center_history
<span class="gp"># </span>history.db.username<span class="o">=</span>leaps_center
<span class="gp"># </span>history.db.password<span class="o">=</span><span class="nb">pwd</span>

<span class="gp"># </span>History<span class="w"> </span>-<span class="w"> </span>Oracle<span class="w"> </span>Database<span class="w"> </span>Example
<span class="gp"># </span>Important!<span class="w"> </span>To<span class="w"> </span>use<span class="w"> </span>Oracle<span class="w"> </span>DBMS<span class="w"> </span>is<span class="w"> </span>mandatory<span class="w"> </span>to<span class="w"> </span>change<span class="w"> </span>global.leaps.center.history.entity.NetworkNodeHistory.id<span class="w"> </span>@Id<span class="w"> </span>generation<span class="w"> </span>strategy<span class="w"> </span>to<span class="w"> </span>GenerationType.AUTO<span class="w"> </span>or<span class="w"> </span>GenerationType.SEQUENCE.<span class="w"> </span>Oracle<span class="w"> </span>does<span class="w"> </span>not<span class="w"> </span>support<span class="w"> </span>GenerationType.IDENTITY.
<span class="gp"># </span>history.dbms<span class="o">=</span>ORACLE
<span class="gp"># </span>history.db.hibernate.dialect<span class="o">=</span>org.hibernate.dialect.Oracle10gDialect
<span class="gp"># </span>history.db.jdbc.url<span class="o">=</span>jdbc:oracle:thin:@127.0.0.1:1521/XE
<span class="gp"># </span>history.db.username<span class="o">=</span>leaps_center
<span class="gp"># </span>history.db.password<span class="o">=</span><span class="nb">pwd</span>

<span class="gp"># </span>History<span class="w"> </span>-<span class="w"> </span>MySQL<span class="w"> </span>Database<span class="w"> </span>Example
<span class="gp"># </span>history.dbms<span class="o">=</span>MY_SQL
<span class="gp"># </span>history.db.jdbc.url<span class="o">=</span>jdbc:mysql://localhost:3306/leaps_center
<span class="gp"># </span>history.db.username<span class="o">=</span>leaps_center
<span class="gp"># </span>history.db.password<span class="o">=</span><span class="nb">pwd</span>

<span class="gp"># </span>History<span class="w"> </span>-<span class="w"> </span>SQL<span class="w"> </span>Server<span class="w"> </span>Database<span class="w"> </span>Example
<span class="gp"># </span>TODO:<span class="w"> </span>It<span class="w"> </span>needs<span class="w"> </span>to<span class="w"> </span>be<span class="w"> </span>tested.
<span class="gp"># </span>history.dbms<span class="o">=</span>SQL_SERVER
<span class="gp"># </span>history.db.jdbc.url<span class="o">=</span>jdbc:sqlserver://localhost:1433<span class="p">;</span><span class="nv">databaseName</span><span class="o">=</span>leaps_center_history<span class="p">;</span><span class="nv">integratedSecurity</span><span class="o">=</span><span class="nb">true</span>
<span class="gp"># </span>history.db.jdbc.url<span class="o">=</span>jdbc:jtds:sqlserver://localhost:1433/leaps_center_history<span class="p">;</span><span class="nv">instance</span><span class="o">=</span>SQLEXPRESS<span class="p">;</span>
<span class="gp"># </span>history.db.username<span class="o">=</span>leaps_center
<span class="gp"># </span>history.db.password<span class="o">=</span><span class="nb">pwd</span>

<span class="gp"># </span>History<span class="w"> </span>-<span class="w"> </span>Custom<span class="w"> </span>Database
<span class="gp"># </span>history.dbms<span class="o">=</span>CUSTOM

<span class="gp"># </span>Hibernate<span class="w"> </span>Dialect
<span class="gp"># </span>history.db.hibernate.dialect<span class="o">=</span>org.hibernate.dialect.PostgreSQLDialect

<span class="gp"># </span>JDBC<span class="w"> </span>driver<span class="w"> </span>class
<span class="gp"># </span>history.db.jdbc.driver.class<span class="o">=</span>org.postgresql.Driver
</pre></div>
</div>
</div>
<input id="sd-tab-item-5" name="sd-tab-set-1" type="radio">
<label class="sd-tab-label" for="sd-tab-item-5">
leaps-center-web.properties</label><div class="sd-tab-content docutils">
<p>この設定ファイルはleaps_centerアプリケーションをコントロールします。</p>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">#</span>
<span class="gp">#       </span>LEAPS<span class="w"> </span>-<span class="w"> </span>Low<span class="w"> </span>Energy<span class="w"> </span>Accurate<span class="w"> </span>Positioning<span class="w"> </span>System<span class="w"> </span>-<span class="w"> </span>LEAPS<span class="w"> </span>Center.
<span class="gp">#</span>
<span class="gp">#       </span>Copyright<span class="w"> </span><span class="o">(</span>c<span class="o">)</span><span class="w"> </span><span class="m">2016</span>-2021,<span class="w"> </span>LEAPS.
<span class="gp">#</span>
<span class="gp">#       </span>Licensed<span class="w"> </span>under<span class="w"> </span>the<span class="w"> </span>Apache<span class="w"> </span>License,<span class="w"> </span>Version<span class="w"> </span><span class="m">2</span>.0<span class="w"> </span><span class="o">(</span>the<span class="w"> </span><span class="s2">"License"</span><span class="o">)</span><span class="p">;</span>
<span class="gp">#       </span>you<span class="w"> </span>may<span class="w"> </span>not<span class="w"> </span>use<span class="w"> </span>this<span class="w"> </span>file<span class="w"> </span>except<span class="w"> </span><span class="k">in</span><span class="w"> </span>compliance<span class="w"> </span>with<span class="w"> </span>the<span class="w"> </span>License.
<span class="gp">#       </span>You<span class="w"> </span>may<span class="w"> </span>obtain<span class="w"> </span>a<span class="w"> </span>copy<span class="w"> </span>of<span class="w"> </span>the<span class="w"> </span>License<span class="w"> </span>at
<span class="gp">#</span>
<span class="gp">#       </span>http://www.apache.org/licenses/LICENSE-2.0
<span class="gp">#</span>
<span class="gp">#       </span>Unless<span class="w"> </span>required<span class="w"> </span>by<span class="w"> </span>applicable<span class="w"> </span>law<span class="w"> </span>or<span class="w"> </span>agreed<span class="w"> </span>to<span class="w"> </span><span class="k">in</span><span class="w"> </span>writing,<span class="w"> </span>software
<span class="gp">#       </span>distributed<span class="w"> </span>under<span class="w"> </span>the<span class="w"> </span>License<span class="w"> </span>is<span class="w"> </span>distributed<span class="w"> </span>on<span class="w"> </span>an<span class="w"> </span><span class="s2">"AS IS"</span><span class="w"> </span>BASIS,
<span class="gp">#       </span>WITHOUT<span class="w"> </span>WARRANTIES<span class="w"> </span>OR<span class="w"> </span>CONDITIONS<span class="w"> </span>OF<span class="w"> </span>ANY<span class="w"> </span>KIND,<span class="w"> </span>either<span class="w"> </span>express<span class="w"> </span>or<span class="w"> </span>implied.
<span class="gp">#       </span>See<span class="w"> </span>the<span class="w"> </span>License<span class="w"> </span><span class="k">for</span><span class="w"> </span>the<span class="w"> </span>specific<span class="w"> </span>language<span class="w"> </span>governing<span class="w"> </span>permissions<span class="w"> </span>and
<span class="gp">#       </span>limitations<span class="w"> </span>under<span class="w"> </span>the<span class="w"> </span>License.
<span class="gp">#</span>

<span class="gp"># </span>database<span class="w"> </span><span class="o">(</span>SQLITE,<span class="w"> </span>POSTGRESQL,<span class="w"> </span>MY_SQL,<span class="w"> </span>ORACLE,<span class="w"> </span>SQL_SERVER<span class="w"> </span>or<span class="w"> </span>CUSTOM<span class="o">)</span>
<span class="go">db.dbms=SQLITE</span>

<span class="gp"># </span>History<span class="w"> </span>-<span class="w"> </span>SQLite<span class="w"> </span>Database<span class="w"> </span>Example.
<span class="gp"># </span><span class="nv">dbms</span><span class="o">=</span>SQLITE
<span class="gp"># </span>db.jdbc.url<span class="o">=</span>jdbc:sqlite:leaps-center-db
<span class="gp"># </span>db.username<span class="o">=</span>
<span class="gp"># </span>db.password<span class="o">=</span>

<span class="gp"># </span>History<span class="w"> </span>-<span class="w"> </span>PostgreSQL<span class="w"> </span>Database<span class="w"> </span>Example
<span class="gp"># </span>db.dbms<span class="o">=</span>POSTGRESQL
<span class="gp"># </span>db.jdbc.url<span class="o">=</span>jdbc:postgresql://localhost:5432/leaps_center
<span class="gp"># </span>db.username<span class="o">=</span>postgres
<span class="gp"># </span>db.password<span class="o">=</span>qwe123

<span class="gp"># </span>History<span class="w"> </span>-<span class="w"> </span>Oracle<span class="w"> </span>Database<span class="w"> </span>Example
<span class="gp"># </span>Important!<span class="w"> </span>To<span class="w"> </span>use<span class="w"> </span>Oracle<span class="w"> </span>DBMS<span class="w"> </span>is<span class="w"> </span>mandatory<span class="w"> </span>to<span class="w"> </span>change<span class="w"> </span>global.leaps.center.entity.NetworkNodeHistory.id<span class="w"> </span>@Id<span class="w"> </span>generation<span class="w"> </span>strategy<span class="w"> </span>to<span class="w"> </span>GenerationType.AUTO<span class="w"> </span>or<span class="w"> </span>GenerationType.SEQUENCE.<span class="w"> </span>Oracle<span class="w"> </span>does<span class="w"> </span>not<span class="w"> </span>support<span class="w"> </span>GenerationType.IDENTITY.
<span class="gp"># </span>db.dbms<span class="o">=</span>ORACLE
<span class="gp"># </span>db.hibernate.dialect<span class="o">=</span>org.hibernate.dialect.Oracle10gDialect
<span class="gp"># </span>db.jdbc.url<span class="o">=</span>jdbc:oracle:thin:@127.0.0.1:1521/XE
<span class="gp"># </span>db.username<span class="o">=</span>leaps_center
<span class="gp"># </span>db.password<span class="o">=</span>q1w2e3r4t5

<span class="gp"># </span>History<span class="w"> </span>-<span class="w"> </span>MySQL<span class="w"> </span>Database<span class="w"> </span>Example
<span class="gp"># </span>db.dbms<span class="o">=</span>MY_SQL
<span class="gp"># </span>db.jdbc.url<span class="o">=</span>jdbc:mysql://localhost:3306/leaps_center
<span class="gp"># </span>db.username<span class="o">=</span>root
<span class="gp"># </span>db.password<span class="o">=</span>qwe123

<span class="gp"># </span>History<span class="w"> </span>-<span class="w"> </span>SQL<span class="w"> </span>Server<span class="w"> </span>Database<span class="w"> </span>Example
<span class="gp"># </span>db.dbms<span class="o">=</span>SQL_SERVER
<span class="gp"># </span>db.jdbc.url<span class="o">=</span>jdbc:sqlserver://localhost:1433<span class="p">;</span><span class="nv">databaseName</span><span class="o">=</span>leaps_center_history<span class="p">;</span><span class="nv">integratedSecurity</span><span class="o">=</span><span class="nb">true</span>
<span class="gp"># </span>db.jdbc.url<span class="o">=</span>jdbc:jtds:sqlserver://localhost:1433/leaps_center_history<span class="p">;</span><span class="nv">instance</span><span class="o">=</span>SQLEXPRESS<span class="p">;</span>
<span class="gp"># </span>db.username<span class="o">=</span>leaps_center
<span class="gp"># </span>db.password<span class="o">=</span>qwe123

<span class="gp"># </span>History<span class="w"> </span>-<span class="w"> </span>Custom<span class="w"> </span>Database
<span class="gp"># </span>db.dbms<span class="o">=</span>CUSTOM

<span class="gp"># </span>Hibernate<span class="w"> </span>Dialect
<span class="gp"># </span>db.hibernate.dialect<span class="o">=</span>org.hibernate.dialect.PostgreSQLDialect

<span class="gp"># </span>JDBC<span class="w"> </span>driver<span class="w"> </span>class
<span class="gp"># </span>history.db.jdbc.driver.class<span class="o">=</span>org.postgresql.Driver
<span class="gp"># </span>db.jdbc.url<span class="o">=</span>jdbc:postgresql://localhost:5432/leaps_center
<span class="gp"># </span>db.username<span class="o">=</span>postgres
<span class="gp"># </span>db.password<span class="o">=</span>qwe123
<span class="gp"># </span>db.jdbc.driver.class<span class="o">=</span>
<span class="gp"># </span>db.hibernate.dialect<span class="o">=</span>

<span class="gp"># </span>show<span class="w"> </span>sql<span class="w"> </span><span class="o">(</span>default<span class="w"> </span><span class="nb">false</span><span class="o">)</span>
<span class="gp"># </span>db.jpa.show-sql<span class="o">=</span><span class="nb">false</span>

<span class="gp"># </span>format<span class="w"> </span>sql<span class="w"> </span><span class="o">(</span>default<span class="w"> </span><span class="nb">false</span><span class="o">)</span>
<span class="gp"># </span>db.jpa.format-sql<span class="o">=</span><span class="nb">false</span>

<span class="gp"># </span><span class="o">=======================================================================================================</span>
<span class="gp"># </span><span class="nv">network</span>
<span class="gp"># </span><span class="o">=======================================================================================================</span>

<span class="gp"># </span><span class="nb">enable</span><span class="w"> </span>the<span class="w"> </span>registration<span class="w"> </span>of<span class="w"> </span>networks<span class="w"> </span>with<span class="w"> </span>mqtt<span class="w"> </span>connection<span class="w"> </span><span class="nb">type</span><span class="w"> </span><span class="o">=</span><span class="w"> </span>HOST.<span class="w"> </span><span class="o">(</span>default<span class="w"> </span><span class="nb">true</span><span class="o">)</span>
<span class="go">network.mqtt.connection.by.host.enabled=true</span>

<span class="gp"># </span><span class="nb">enable</span><span class="w"> </span>the<span class="w"> </span>registration<span class="w"> </span>of<span class="w"> </span>networks<span class="w"> </span>with<span class="w"> </span>mqtt<span class="w"> </span>connection<span class="w"> </span><span class="nb">type</span><span class="w"> </span><span class="o">=</span><span class="w"> </span>PAN_ID.<span class="w"> </span><span class="o">(</span>default<span class="w"> </span><span class="nb">false</span><span class="o">)</span>
<span class="go">network.mqtt.connection.by.network.id.enable=false</span>

<span class="gp"># </span><span class="nb">enable</span><span class="w"> </span>the<span class="w"> </span>registration<span class="w"> </span>of<span class="w"> </span>networks<span class="w"> </span>with<span class="w"> </span>web<span class="w"> </span>client<span class="w"> </span>connection<span class="w"> </span>by<span class="w"> </span>websocket.<span class="w"> </span><span class="o">(</span>default<span class="w"> </span><span class="nb">false</span><span class="o">)</span>
<span class="go">network.web.client.connection.by.web.socket=false</span>

<span class="gp"># </span>create<span class="w"> </span>the<span class="w"> </span>default<span class="w"> </span>network<span class="w"> </span><span class="k">if</span><span class="w"> </span>it<span class="w"> </span>does<span class="w"> </span>not<span class="w"> </span>exist<span class="w"> </span>when<span class="w"> </span>starting.<span class="w"> </span><span class="o">(</span>default<span class="w"> </span><span class="nb">true</span><span class="o">)</span>
<span class="go">network.create.default.network=true</span>
<span class="gp"># </span>network.create.default.floor.plan<span class="o">=</span><span class="nb">true</span>

<span class="go">network.default.id=</span>
<span class="go">network.default.name=Default</span>

<span class="gp"># </span>PAN_ID<span class="w"> </span>or<span class="w"> </span>HOST
<span class="go">network.default.mqtt.connection.type=HOST</span>

<span class="gp"># </span>WS<span class="w"> </span>or<span class="w"> </span>SSE
<span class="go">network.default.web.client.connection.type=SSE</span>

<span class="gp"># </span>MQTT
<span class="go">mqtt.host=</span>
<span class="go">mqtt.ws.port=15675</span>
<span class="go">mqtt.tcp.port=1883</span>
<span class="go">mqtt.username=dwmuser</span>
<span class="go">mqtt.password=dwmuser</span>
<span class="gp"># </span>Enable/Disable<span class="w"> </span>TLS
<span class="gp">#</span>mqtt.tls<span class="o">=</span>
<span class="gp"># </span>CA_SIGNED_CERTIFICATE<span class="w"> </span><span class="o">(</span>signed<span class="w"> </span>by<span class="w"> </span>a<span class="w"> </span>publicly<span class="w"> </span>trusted<span class="w"> </span>CA<span class="o">)</span>,<span class="w"> </span>CA_FILE_CERTIFICATE<span class="w"> </span><span class="o">(</span>file<span class="w"> </span>certificate<span class="o">)</span><span class="p">;</span>
<span class="gp">#</span>mqtt.tls.certificate.type<span class="o">=</span>CA_SIGNED_CERTIFICATE
<span class="gp"># </span>TLS<span class="w"> </span>Protocol:<span class="w"> </span>TLS_V1<span class="w"> </span><span class="o">(</span>TLSv1<span class="o">)</span>,<span class="w"> </span>TLS_V1_1<span class="w"> </span><span class="o">(</span>TLSv1.1<span class="o">)</span>,<span class="w"> </span>TLS_V1_2<span class="w"> </span><span class="o">(</span>TLSv1.2<span class="o">)</span>,<span class="w"> </span>TLS_V1_3<span class="o">(</span>TLSv1.3<span class="o">)</span><span class="p">;</span>
<span class="gp">#</span>mqtt.tls.protocol<span class="o">=</span>TLS_V1_2
<span class="gp">#</span>mqtt.tls.certificate.file<span class="o">=</span>/user/.../leaps-center.crt
<span class="go">mqtt.topic.prefix=dwm</span>
<span class="go">mqtt.tag.topic.prefix=node</span>
<span class="go">mqtt.anchor.topic.prefix=node</span>

<span class="gp"># </span><span class="o">=======================================================================================================</span>
<span class="gp"># </span>floorplan<span class="w"> </span><span class="nv">settings</span>
<span class="gp"># </span><span class="o">=======================================================================================================</span>
<span class="gp"># </span>size<span class="w"> </span><span class="k">in</span><span class="w"> </span>pixels<span class="w"> </span><span class="o">(</span>default<span class="w"> </span><span class="m">2048</span><span class="o">)</span>
<span class="go">floorplan.max.image.dimension.size=2048</span>

<span class="gp"># </span><span class="o">=======================================================================================================</span>
<span class="gp"># </span>scene<span class="w"> </span><span class="nv">settings</span>
<span class="gp"># </span><span class="o">=======================================================================================================</span>
<span class="gp"># </span>size<span class="w"> </span><span class="k">in</span><span class="w"> </span>cm<span class="w"> </span><span class="o">(</span>default<span class="w"> </span>50cm<span class="o">)</span>
<span class="go">scene.grid.size=50</span>
<span class="gp"># </span>color<span class="w"> </span><span class="k">in</span><span class="w"> </span>int<span class="w"> </span><span class="o">(</span>default<span class="w"> </span>0xD8D8D8<span class="o">)</span>
<span class="go">scene.grid.color=0xD8D8D8</span>
<span class="gp"># </span>max<span class="w"> </span>grid<span class="w"> </span>visibility<span class="w"> </span>distance<span class="w"> </span><span class="k">in</span><span class="w"> </span>meters<span class="w"> </span><span class="o">(</span>default<span class="w"> </span><span class="m">100</span><span class="o">)</span>
<span class="go">scene.grid.max.visibility.distance=100</span>
<span class="gp"># </span>zoom<span class="w"> </span>min<span class="w"> </span><span class="k">in</span><span class="w"> </span>meters<span class="w"> </span><span class="o">(</span>default<span class="w"> </span><span class="m">2</span><span class="o">)</span>
<span class="go">scene.zoom.min=2</span>
<span class="gp"># </span>zoom<span class="w"> </span>max<span class="w"> </span><span class="k">in</span><span class="w"> </span>meters<span class="w"> </span><span class="o">(</span>default<span class="w"> </span><span class="m">100</span><span class="o">)</span>
<span class="go">scene.zoom.max=100</span>

<span class="gp"># </span><span class="o">=======================================================================================================</span>
<span class="gp"># </span>web<span class="w"> </span>server<span class="w"> </span><span class="nv">settings</span>
<span class="gp"># </span><span class="o">=======================================================================================================</span>

<span class="gp"># </span>http<span class="w"> </span>session<span class="w"> </span>timeout
<span class="go">server.servlet.session.timeout=120m</span>

<span class="gp"># </span>maximum<span class="w"> </span>number<span class="w"> </span>of<span class="w"> </span>http<span class="w"> </span>sessions<span class="w"> </span>per<span class="w"> </span>user<span class="w"> </span><span class="o">(</span>-1<span class="w"> </span>is<span class="w"> </span>unlimited<span class="o">)</span>
<span class="go">server.max.sessions.per.user=-1</span>

<span class="gp"># </span>mod-jk/ajp<span class="w"> </span>connector<span class="w"> </span>configuration
<span class="go">tomcat.ajp.enabled=false</span>
<span class="gp"># </span>tomcat.ajp.port<span class="o">=</span><span class="m">8009</span>
<span class="gp"># </span>tomcat.ajp.secret.required<span class="o">=</span><span class="nb">false</span>
<span class="gp"># </span>tomcat.apr.enabled<span class="o">=</span><span class="nb">false</span>

<span class="gp"># </span>server<span class="w"> </span>port<span class="w"> </span><span class="o">(</span><span class="m">2</span>-65535<span class="o">)</span>
<span class="go">server.port=8080</span>

<span class="gp"># </span><span class="nb">enable</span><span class="w"> </span>/<span class="w"> </span>disable<span class="w"> </span>https
<span class="go">server.ssl.enabled=false</span>
<span class="gp"># </span>keystore<span class="w"> </span>format
<span class="gp"># </span>server.ssl.key-store-type<span class="o">=</span>PKCS12
<span class="gp"># </span>keystore<span class="w"> </span>location
<span class="gp"># </span>server.ssl.key-store<span class="o">=</span>D:<span class="se">\\</span>Leaps<span class="se">\\</span>tls<span class="se">\\</span>springboot.p12
<span class="gp"># </span>keystore<span class="w"> </span><span class="nb">alias</span>
<span class="gp"># </span>server.ssl.key-alias<span class="o">=</span>springboot
<span class="gp"># </span>keystore<span class="w"> </span>password
<span class="gp"># </span>server.ssl.key-store-password<span class="o">=</span>password
<span class="gp"># </span>SSL<span class="w"> </span>protocol<span class="w"> </span>to<span class="w"> </span>use
<span class="gp"># </span>server.ssl.protocol<span class="o">=</span>TLS
<span class="gp"># </span>Enabled<span class="w"> </span>SSL<span class="w"> </span>protocols
<span class="gp"># </span>server.ssl.enabled-protocols<span class="o">=</span>TLSv1.2
</pre></div>
</div>
</div>
</div>
</li>
</ul>
</div>
<div class="section" id="getting-started">
<h2>はじめに</h2>
<blockquote>
<div><p>デフォルトでは、ユーザー名は <span class="red-text">admin</span>、パスワードは <span class="red-text">admin</span> です。</p>
</div></blockquote>
<div class="section" id="leaps-server-docker">
<h3>LEAPS Server Docker</h3>
<ul class="simple">
<li><p>LEAPS Centerを起動します： <code class="docutils literal notranslate"><span class="pre">docker</span> <span class="pre">start</span> <span class="pre">leaps_center</span></code> を実行します。</p></li>
<li><p>LEAPS Centerを停止します：<code class="docutils literal notranslate"><span class="pre">docker</span> <span class="pre">stop</span> <span class="pre">leaps_center</span></code> を実行します。</p></li>
<li><p>LEAPS Centerを再起動します：<code class="docutils literal notranslate"><span class="pre">docker</span> <span class="pre">restart</span> <span class="pre">leaps_center</span></code> を実行します。</p></li>
<li><p>LEAPS Centerを削除するには、<code class="docutils literal notranslate"><span class="pre">docker</span> <span class="pre">rm</span> <span class="pre">--force</span> <span class="pre">leaps_center</span></code> を実行します。</p></li>
</ul>
</div>
<div class="section" id="network-configurations">
<h3>ネットワーク構成</h3>
<blockquote>
<div><p>ネットワークを設定するには、メニューから <span class="red-text">Networks</span> を選択する。</p>
<a class="reference internal image-reference" href="../../../_images/lc_select_networks.png"><img alt="../../../_images/lc_select_networks.png" class="align-center" src="/docs-assets/ja/_images/lc_select_networks.png" style="width: 720.0px; height: 564.3000000000001px;"></a>
<p>ネットワーク管理ダイアログがポップアップします。デフォルトでローカルホストネットワークがネットワークID 0x1234で設定されています。</p>
<a class="reference internal image-reference" href="../../../_images/lc_list_networks.png"><img alt="../../../_images/lc_list_networks.png" class="align-center" src="/docs-assets/ja/_images/lc_list_networks.png" style="width: 1023.3000000000001px; height: 333.0px;"></a>
<p>新しいネットワークを作成するには、右下の <span class="red-text">Add</span> ボタンをクリックします。</p>
<p>次に、必要な設定パラメータを入力する：</p>
<blockquote>
<div><blockquote>
<div><ul class="simple">
<li><p>名前</p></li>
<li><p>ネットワークタイプ</p></li>
<li><p>ホスト</p></li>
<li><p>TCPポート</p></li>
<li><p>ユーザー名</p></li>
<li><p>トピックのプレフィックス</p></li>
</ul>
</div></blockquote>
<p>すべて入力したら、<span class="red-text">Save</span> ボタンをクリックして接続し、ネットワークIDを受け取ります。</p>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/lc_config_networks_1234.png"><img alt="../../../_images/lc_config_networks_1234.png" class="align-center" src="/docs-assets/ja/_images/lc_config_networks_1234.png" style="width: 704.7px; height: 763.2px;"></a>
</div></blockquote>
</div></blockquote>
<p>ネットワークIDがわからない場合は、<a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> やShellを使って見つけることができる。</p>
<p>最後に <span class="red-text">Test</span> ボタンをクリックして接続を確認し、 <span class="red-text">Save</span> ボタンをクリックして設定を保存します。</p>
</div></blockquote>
</div>
<div class="section" id="node-configurations">
<h3>ノード構成</h3>
<p>ノードを設定するには、あらかじめノードを特定のネットワークに割り当てる必要があります。</p>
<p>指定したノードのあるネットワークを選択すると、ネットワークの詳細が表示されます。次に、ノードの設定を開始します。</p>
<p>ゲートウェイ・ノード、アンカー・ノード、タグ・ノードとして設定可能なノードについては、以下を参照してください</p>
<blockquote>
<div><div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-6" name="sd-tab-set-2" type="radio">
<label class="sd-tab-label" for="sd-tab-item-6">
ゲートウェイ</label><div class="sd-tab-content docutils">
<a class="reference internal image-reference" href="../../../_images/lc_config_gateway.png"><img alt="../../../_images/lc_config_gateway.png" class="align-center" src="/docs-assets/ja/_images/lc_config_gateway.png" style="width: 702.0px; height: 738.9px;"></a>
</div>
<input id="sd-tab-item-7" name="sd-tab-set-2" type="radio">
<label class="sd-tab-label" for="sd-tab-item-7">
アンカー</label><div class="sd-tab-content docutils">
<a class="reference internal image-reference" href="../../../_images/lc_config_anchor.png"><img alt="../../../_images/lc_config_anchor.png" class="align-center" src="/docs-assets/ja/_images/lc_config_anchor.png" style="width: 712.8000000000001px; height: 512.1px;"></a>
</div>
<input id="sd-tab-item-8" name="sd-tab-set-2" type="radio">
<label class="sd-tab-label" for="sd-tab-item-8">
タグ</label><div class="sd-tab-content docutils">
<a class="reference internal image-reference" href="../../../_images/lc_config_tag.png"><img alt="../../../_images/lc_config_tag.png" class="align-center" src="/docs-assets/ja/_images/lc_config_tag.png" style="width: 712.8000000000001px; height: 540.9px;"></a>
</div>
</div>
</div></blockquote>
</div>
<div class="section" id="floor-plans">
<h3>フロアプラン</h3>
<blockquote>
<div><p>フロアプランを設定するには、メニューから <span class="red-text">Floor Plans</span> を選択してください。</p>
<a class="reference internal image-reference" href="../../../_images/lc_menu.png"><img alt="../../../_images/lc_menu.png" class="align-center" src="/docs-assets/ja/_images/lc_menu.png" style="width: 218.70000000000002px; height: 392.40000000000003px;"></a>
<p>右下の <span class="red-text">Add</span> ボタンをクリックしてください。</p>
<a class="reference internal image-reference" href="../../../_images/lc_floor_plans_add.png"><img alt="../../../_images/lc_floor_plans_add.png" class="align-center" src="/docs-assets/ja/_images/lc_floor_plans_add.png" style="width: 1020.6px; height: 331.2px;"></a>
<p>次に、設定したいフロアプランをインポートし、対応するパラメータを入力します。</p>
<a class="reference internal image-reference" href="../../../_images/lc_floor_plans_create.png"><img alt="../../../_images/lc_floor_plans_create.png" class="align-center" src="/docs-assets/ja/_images/lc_floor_plans_create.png" style="width: 444.6px; height: 456.3px;"></a>
<p>入力が終わったら <span class="red-text">Save</span> ボタンをクリックして設定を保存します。 <span class="red-text">Visible</span> チェックボックスを使用すると、マップ上で可視性を有効にすることができます。</p>
<a class="reference internal image-reference" href="../../../_images/lc_floor_plans_udk.png"><img alt="../../../_images/lc_floor_plans_udk.png" class="align-center" src="/docs-assets/ja/_images/lc_floor_plans_udk.png" style="width: 1020.6px; height: 331.2px;"></a>
</div></blockquote>
</div>
<div class="section" id="zones">
<h3>ゾーン</h3>
<blockquote>
<div><p>ゾーンを設定するには、メニューから <span class="red-text">Zones</span> を選択してください。</p>
<a class="reference internal image-reference" href="../../../_images/lc_menu.png"><img alt="../../../_images/lc_menu.png" class="align-center" src="/docs-assets/ja/_images/lc_menu.png" style="width: 218.70000000000002px; height: 392.40000000000003px;"></a>
<p>右下の <span class="red-text">Add</span> ボタンをクリックしてください。</p>
<a class="reference internal image-reference" href="../../../_images/lc_floor_plans_add.png"><img alt="../../../_images/lc_floor_plans_add.png" class="align-center" src="/docs-assets/ja/_images/lc_floor_plans_add.png" style="width: 1020.6px; height: 331.2px;"></a>
<p>それから対応するパラメータを入力し、<span class="red-text">Save</span> の設定を追加します。</p>
</div></blockquote>
</div>
<div class="section" id="users">
<h3>ユーザー</h3>
<blockquote>
<div><p>ユーザーを設定するには、メニューから <span class="red-text">Users</span> を選択してください。</p>
<a class="reference internal image-reference" href="../../../_images/lc_menu.png"><img alt="../../../_images/lc_menu.png" class="align-center" src="/docs-assets/ja/_images/lc_menu.png" style="width: 218.70000000000002px; height: 392.40000000000003px;"></a>
<p>デフォルトでは、アプリケーションは管理者アカウントと共通アカウントをあらかじめ設定しています。</p>
<a class="reference internal image-reference" href="../../../_images/lc_user_list.png"><img alt="../../../_images/lc_user_list.png" class="align-center" src="/docs-assets/ja/_images/lc_user_list.png" style="width: 714.6px; height: 367.2px;"></a>
<p>管理者または共通アカウントの場合。</p>
<blockquote>
<div><div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-9" name="sd-tab-set-3" type="radio">
<label class="sd-tab-label" for="sd-tab-item-9">
管理者</label><div class="sd-tab-content docutils">
<a class="reference internal image-reference" href="../../../_images/lc_user_admin.png"><img alt="../../../_images/lc_user_admin.png" class="align-center" src="/docs-assets/ja/_images/lc_user_admin.png" style="width: 443.7px; height: 486.0px;"></a>
</div>
<input id="sd-tab-item-10" name="sd-tab-set-3" type="radio">
<label class="sd-tab-label" for="sd-tab-item-10">
共通</label><div class="sd-tab-content docutils">
<a class="reference internal image-reference" href="../../../_images/lc_user_common.png"><img alt="../../../_images/lc_user_common.png" class="align-center" src="/docs-assets/ja/_images/lc_user_common.png" style="width: 440.1px; height: 689.4px;"></a>
</div>
</div>
</div></blockquote>
</div></blockquote>
</div>
</div>
<hr class="docutils">
<div class="section" id="api-authorization">
<h2>API 認証</h2>
<ol class="arabic">
<li><p>ユーザは /login に以下のパラメータを渡すシンプルな HTTP POST を行う必要があります (admin:admin を例にしています)。</p>
<ul class="simple">
<li><p>ユーザー名: admin</p></li>
<li><p>パスワード: admin</p></li>
<li><p>remember-me: on</p></li>
</ul>
</li>
<li><p>ログイン後、JSESSIONIDクッキーが生成され、ユーザはそれ以降のリクエストでそれを使用する必要があります。</p>
<div class="admonition note">
<p class="admonition-title">注釈</p>
<ol class="arabic simple">
<li><p>これは必須ではありません。もしユーザがこれを使うと、レスポンスとして別のクッキー (クッキー REMEMBERME) が追加され、ユーザはそれ以降のリクエストでそれを使うことができます。</p></li>
<li><p>LEAPS Centerでは、ログイン後およびユーザが認証されていない場合にリダイレクトを実行するため、ユーザのクライアントで <code class="docutils literal notranslate"><span class="pre">follow</span> <span class="pre">redirects</span></code> パラメータを適切に設定する必要がある。ログイン後のレスポンスコードは302であるが、ユーザが認証されていない場合のステータスコードも302であるため、ユーザはそれを手動で処理する必要がある。ユーザは、例えばRESTサービスに対してどのようなリクエストを行っても、レスポンスのステータスコードが200でなければ、ユーザは認証されません。</p></li>
</ol>
</div>
</li>
</ol>
<p>以下は、リクエストとネットワークへの問い合わせを行うJavaのコード例である：</p>
<a class="reference internal image-reference" href="../../../_images/api-authorization.png"><img alt="../../../_images/api-authorization.png" class="align-center" src="/docs-assets/ja/_images/api-authorization.png" style="width: 505.4px; height: 591.5px;"></a>
<p>詳細については、以下の2つのビデオを参照してください。1つはPostmanを使用し、もう1つはJavaコードを使用します。</p>
<div style="text-align: center; max-width: 100%;">
    <video controls="" src="../../../_static/video/postman.mp4" style="width: 100%; height: auto;"></video>
    <h2 style="margin-top: 0; margin-bottom: 10px; font-size: 1rem;">Postman</h2> <!-- Adjusted font-size -->
</div><hr class="docutils">
<div style="text-align: center; max-width: 100%;">
    <video controls="" src="../../../_static/video/java_client.mp4" style="width: 100%; height: auto;"></video>
    <h2 style="margin-top: 0; margin-bottom: 10px; font-size: 1rem;">Java Client</h2> <!-- Adjusted font-size -->
</div></div>
<hr class="docutils">
<div class="section" id="troubleshooting">
<h2>トラブルシューティング</h2>
<ul class="simple">
<li><p>次のコマンド <code class="docutils literal notranslate"><span class="pre">docker</span> <span class="pre">restart</span> <span class="pre">leaps_center</span></code> を使って LEAPS Centerを再起動してください。</p></li>
<li><p>LEAPS Centerが起動しているときにログをチェックし、docker デスクトップを開いて leaps_center コンテナを選択してください。</p></li>
<li><p>Open via Safari: If the interactive floor plan fails to load when you open the app, a Safari experimental feature is likely causing a conflict. Go to Settings &gt; Safari &gt; Advanced &gt; Experimental Features and disable ‘requestIdleCallback’.</p></li>
</ul>
</div>
</div>


           </div>
