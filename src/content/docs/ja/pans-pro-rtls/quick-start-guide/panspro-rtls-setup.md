---
title: "PANS PRO デモ"
lang: ja
slug: "pans-pro-rtls/quick-start-guide/panspro-rtls-setup"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/pans-pro-rtls/quick-start-guide/panspro-rtls-setup/"
order: 88
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="pans-pro-demo">
<span id="id1"></span><h1>PANS PRO デモ</h1>
<p><strong>セットアップの準備</strong></p>
<img alt="../../../_images/qsg_set_up.png" class="align-center" src="/docs-assets/ja/_images/qsg_set_up.png">
<ol class="arabic simple">
<li><p><a class="reference internal" href="/docs/ja/pans-pro-rtls/infrastructure/pans-pro-manager#pans-pro-manager"><span class="std std-ref">PANS PRO Manager</span></a> アプリケーションが Android デバイスにインストールされています。</p></li>
<li><p><a class="reference internal" href="/docs/ja/pans-pro-rtls/infrastructure/leaps-center#pans-pro-center"><span class="std std-ref">LEAPS Center</span></a> アプリケーションが PC にインストールされています。</p></li>
<li><p>少なくとも 4 つの LC4 デバイス (アンカー ノード) と 1 つの LC8 デバイス (タグ ノード)。</p></li>
<li><p>1 つの LC5 デバイス (ゲートウェイ ノード)。</p></li>
<li><p>デバイスに電力を供給するためのバッテリーまたは Micro USB ケーブル。</p></li>
<li><p><em>推奨</em>: アンカー デバイスを取り付けるには、カメラ マウントを備えたクランプまたは三脚を使用します。</p></li>
<li><p><em>推奨</em>: Raspberry Pi 3B 以降のバージョン、または PC、データ サーバー、および Web アプリケーションのインストール。</p></li>
<li><p><em>オプション</em>: Putty、Teraterm、minicom、またはコンピューターにインストールされているお気に入りのターミナル アプリケーション。</p></li>
</ol>
<p><strong>セットアップ時間:</strong> 5 分未満</p>
<div class="sd-container-fluid sd-sphinx-override sd-mb-4 docutils">
<div class="sd-row sd-row-cols-3 sd-row-cols-xs-3 sd-row-cols-sm-3 sd-row-cols-md-3 sd-row-cols-lg-3 docutils">
<div class="sd-col sd-d-flex-row docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm sd-card-hover sd-text-center custom-card docutils">
<div class="sd-card-body docutils">
<a class="reference internal image-reference" href="../../../_images/lc4a_front_view.png"><img alt="../../../_images/lc4a_front_view.png" src="/docs-assets/ja/_images/lc4a_front_view.png" style="width: 131.76px; height: 189.26999999999998px;"></a>
<p class="sd-card-text"><span class="red-text">LC4 デバイス</span></p>
</div>
<a class="sd-stretched-link reference internal" href="/docs/ja/pans-pro-rtls/specification/lc4a-specification#lc4a-specification"><span class="std std-ref"></span></a></div>
</div>
<div class="sd-col sd-d-flex-row docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm sd-card-hover sd-text-center custom-card docutils">
<div class="sd-card-body docutils">
<a class="reference internal image-reference" href="../../../_images/lc5.png"><img alt="../../../_images/lc5.png" src="/docs-assets/ja/_images/lc5.png" style="width: 204.8px; height: 184.8px;"></a>
<p class="sd-card-text"><span class="red-text">LC5 デバイス</span></p>
</div>
<a class="sd-stretched-link reference internal" href="/docs/ja/pans-pro-rtls/specification/lc5a-specification#lc5a-specification"><span class="std std-ref"></span></a></div>
</div>
<div class="sd-col sd-d-flex-row docutils">
<div class="sd-card sd-sphinx-override sd-w-100 sd-shadow-sm sd-card-hover sd-text-center custom-card docutils">
<div class="sd-card-body docutils">
<a class="reference internal image-reference" href="../../../_images/lc8.png"><img alt="../../../_images/lc8.png" src="/docs-assets/ja/_images/lc8.png" style="width: 117.2px; height: 182.0px;"></a>
<p class="sd-card-text"><span class="red-text">LC8 デバイス</span></p>
</div>
<a class="sd-stretched-link reference internal" href="/docs/ja/pans-pro-rtls/specification/lc8a-specification#lc8a-specification"><span class="std std-ref"></span></a></div>
</div>
</div>
</div>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-0" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-0">
電話でのクイックスタート</label><div class="sd-tab-content docutils">
<p><strong>概要</strong></p>
<p>このセットアップは、リアルタイム ナビゲーション、追跡、および <span class="red-text">Two Way Ranging (TWR)</span> テクノロジーを使用した両方の方法のデータ テレメトリを示しています。</p>
<p><strong>代表的なアプリケーション</strong>: 屋内ナビゲーション、資産追跡、およびアップリンクとダウンリンクをサポートするリアルタイム データ テレメトリ。</p>
<p><strong>セットアップ手順</strong></p>
<ol class="arabic">
<li><p>最新ファームウェアがすでにフラッシュされているデバイスの電源をオンにします。</p>
<ul class="simple">
<li><p>静的にマウントされたデバイスはアンカーとして機能し、位置情報をタグに提供します。</p></li>
<li><p>移動デバイスは、双方向レンジング測定モードで設定されたタグとして機能します。</p></li>
</ul>
</li>
<li><p><a class="reference internal" href="/docs/ja/pans-pro-rtls/infrastructure/pans-pro-manager#pans-pro-manager"><span class="std std-ref">PANS PRO Manager</span></a> セクションの詳細なガイドラインを参照してください。ここでは簡単な手順を説明します。</p>
<p>2.1。ユーザー名 <code class="docutils literal notranslate"><span class="pre">admin</span></code> とパスワード <code class="docutils literal notranslate"><span class="pre">admin</span></code> を使用してログインします。</p>
<p>2.2。ログインに成功したら、ホームページ上の``デバイス検出の開始``機能をクリックします。</p>
<p>2.3。検出されたデバイスをネットワークに割り当てます。ネットワーク名を入力して続行し、すべてのデバイスをこのネットワークに割り当てます。</p>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/ppm-home-page.jpg"><img alt="../../../_images/ppm-home-page.jpg" src="/docs-assets/ja/_images/ppm-home-page.jpg" style="width: 32%;"></a>
<a class="reference internal image-reference" href="../../../_images/ppm-assign-network6.jpg"><img alt="../../../_images/ppm-assign-network6.jpg" src="/docs-assets/ja/_images/ppm-assign-network6.jpg" style="width: 32%;"></a>
<a class="reference internal image-reference" href="../../../_images/ppm-network-1.jpg"><img alt="../../../_images/ppm-network-1.jpg" src="/docs-assets/ja/_images/ppm-network-1.jpg" style="width: 32%;"></a>
</div></blockquote>
<p>2.4。検出されたデバイスの 1 つをイニシエーター アンカー ノード (ANI) として構成し、イニシエーター モードを有効にします。</p>
<p>2.5。検出されたデバイスのうち 3 つを、イニシエーター モードを有効にせずにアンカー ノード (AN) として構成します。</p>
<p>2.6。 4 つのアンカー ノード (AN) を使用すると、位置を手動で設定できます。</p>
<blockquote>
<div><ul class="simple">
<li><p><a class="reference internal" href="/docs/ja/pans-pro-rtls/infrastructure/pans-pro-manager#pans-pro-manager"><span class="std std-ref">PANS PRO Manager</span></a> でアンカーを簡単に配置できる自動配置機能を確認してください。</p></li>
</ul>
</div></blockquote>
<p>2.7。 1 つのデバイスを、デフォルトの``NORMAL UPDATE RATE``および``STATIONARY UPDATE RATE``を使用してタグ ノード (TN) として設定します。</p>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/ppm-device-configure-b.jpg"><img alt="../../../_images/ppm-device-configure-b.jpg" src="/docs-assets/ja/_images/ppm-device-configure-b.jpg" style="width: 32%;"></a>
<a class="reference internal image-reference" href="../../../_images/anchor-initiator-node-disable.png"><img alt="../../../_images/anchor-initiator-node-disable.png" src="/docs-assets/ja/_images/anchor-initiator-node-disable.png" style="width: 32%;"></a>
<a class="reference internal image-reference" href="../../../_images/ppm-device-configure-a.jpg"><img alt="../../../_images/ppm-device-configure-a.jpg" src="/docs-assets/ja/_images/ppm-device-configure-a.jpg" style="width: 32%;"></a>
</div></blockquote>
<p>2.8。検出と構成が完了すると、<a class="reference internal" href="/docs/ja/pans-pro-rtls/infrastructure/pans-pro-manager#pans-pro-manager"><span class="std std-ref">PANS PRO Manager</span></a> アプリケーション上でネットワークの視覚化を 2D グリッドまたは 3D グリッドで表示できます。</p>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/ppm-grib-2d-0.jpg"><img alt="../../../_images/ppm-grib-2d-0.jpg" src="/docs-assets/ja/_images/ppm-grib-2d-0.jpg" style="width: 40%;"></a>
<a class="reference internal image-reference" href="../../../_images/ppm-grib-3d-0.jpg"><img alt="../../../_images/ppm-grib-3d-0.jpg" src="/docs-assets/ja/_images/ppm-grib-3d-0.jpg" style="width: 40%;"></a>
</div></blockquote>
</li>
</ol>
</div>
<input id="sd-tab-item-1" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-1">
Web のクイック スタート</label><div class="sd-tab-content docutils">
<p><strong>概要</strong></p>
<p>このセクションでは、<a class="reference internal" href="/docs/ja/pans-pro-rtls/infrastructure/leaps-center#pans-pro-center"><span class="std std-ref">LEAPS Center</span></a> に表示するために PANS PRO RTLS ネットワークをセットアップする方法をガイドラインで説明します。 PANS PRO RLTS ネットワークを正常にセットアップするには、必須のハードウェアとソフトウェアを確認してください。</p>
<p><strong>手順</strong>：</p>
<ol class="arabic">
<li><p>ネットワークを準備します:</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">電話によるクイックスタート</span></code> タブの説明に従って、<code class="docutils literal notranslate"><span class="pre">PANS</span> <span class="pre">PRO</span> <span class="pre">Manage</span></code> 経由の設定を使用してネットワークを設定します。</p></li>
</ul>
</li>
<li><p>ゲートウェイ ボードをセットアップします。<code class="docutils literal notranslate"><span class="pre">PANS</span> <span class="pre">PRO</span> <span class="pre">Docker</span></code> または <code class="docutils literal notranslate"><span class="pre">PANS</span> <span class="pre">PRO</span> <span class="pre">Raspberry</span> <span class="pre">Pi</span></code> のいずれかを使用します。</p>
<ul class="simple">
<li><p><cite>注: 最新のファームウェアがボード上でまだ利用できない場合は、それをフラッシュしてください</cite>。</p></li>
</ul>
<p><strong>ゲートウェイ構成</strong></p>
<div class="line-block">
<div class="line">構成は、USB 経由でデバイスを接続し、オンボードのシェル コマンドを使用することで実行できます。</div>
<div class="line">Enter キーを 2 回押して、シェル コマンド モードを有効にします。</div>
</div>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/advanced_001.png"><img alt="../../../_images/advanced_001.png" class="align-center" src="/docs-assets/ja/_images/advanced_001.png" style="width: 303.40000000000003px; height: 320.0px;"></a>
</div></blockquote>
<p>2.1。 UWBネットワーク構成</p>
<blockquote>
<div><ul>
<li><p>ネットワーク ID を設定します</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; nis</span>
<span class="go">usage: nis PANID</span>
</pre></div>
</div>
</div></blockquote>
</li>
<li><p>ゲートウェイになるようにデバイスを構成します</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; nmg</span>
<span class="go">ok</span>
</pre></div>
</div>
</div></blockquote>
</li>
</ul>
<p>または</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; acs leds 1 uwb 2</span>
<span class="go">ok</span>
</pre></div>
</div>
</div></blockquote>
</div></blockquote>
<p>2.2。デバイスのIPアドレス設定</p>
<blockquote>
<div><p>デフォルトは DHCP (動的 IP アドレス) なので、必要がない限り設定する必要はありません。</p>
<ul>
<li><p>使用法</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; ipv4</span>
<span class="go">usage: ipv4 [static|dynamic] [addr STRING] [mask STRING] [gw STRING]</span>
</pre></div>
</div>
<div class="admonition note">
<p class="admonition-title">注釈</p>
<p>構成が成功すると、デバイスはリセットされます。</p>
</div>
</div></blockquote>
</li>
<li><p>静的 IP アドレスの構成</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; ipv4 addr 192.168.1.100 static</span>
<span class="go">ipv4 ok(0)</span>
</pre></div>
</div>
</div></blockquote>
</li>
<li><p>ネットワークマスク設定</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; ipv4 mask 255.255.255.0</span>
<span class="go">ipv4 ok(0)</span>
</pre></div>
</div>
</div></blockquote>
</li>
<li><p>以前に構成された静的 IP アドレスを有効にします</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; ipv4 static</span>
<span class="go">ipv4 ok(0)</span>
</pre></div>
</div>
</div></blockquote>
</li>
<li><p>DHCP を有効にする</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; ipv4 dynamic</span>
<span class="go">ipv4 ok(0)</span>
</pre></div>
</div>
</div></blockquote>
</li>
<li><p>1 つのステップですべてを構成する</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; ipv4 addr 192.168.1.100 mask 255.255.255.0 static ipv4 ok(0)</span>
</pre></div>
</div>
</div></blockquote>
</li>
</ul>
</div></blockquote>
<p>2.3。 LEAPS Server接続の設定</p>
<blockquote>
<div><ul>
<li><p>使用法</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; peer</span>
<span class="go">usage: peer [addr STRING] [port NUM] [tls 0|1]</span>
</pre></div>
</div>
<div class="admonition note">
<p class="admonition-title">注釈</p>
<p>構成が成功すると、デバイスはリセットされます。</p>
</div>
</div></blockquote>
</li>
<li><p>IP アドレス 192.168.200.1 およびポート 7777 で LEAPS Serverとの接続を構成しています</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; peer addr 192.168.200.1 port 7777 tls 0</span>
<span class="go">peer ok(0)</span>
</pre></div>
</div>
</div></blockquote>
</li>
<li><p>TLSを無効にする</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; peer tls 0</span>
<span class="go">peer ok(0)</span>
</pre></div>
</div>
</div></blockquote>
</li>
<li><p>TLS を有効にする</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; peer tls 1</span>
<span class="go">peer ok(0)</span>
</pre></div>
</div>
</div></blockquote>
</li>
<li><p>LEAS サーバーホストと TLS の組み合わせ構成</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; peer host example.com tls 1</span>
<span class="go">peer ok(0)</span>
</pre></div>
</div>
</div></blockquote>
</li>
<li><p>TLS が無効になっている場合のシステムの正しいステータス</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; si</span>
<span class="go">[000081.971 INF] sys: fw1 fw_ver=x01030000 cfg_ver=x00030000</span>
<span class="go">[000081.976 INF] inet: up tls=off addr=192.168.1.100 mask=255.255.255.0 gw=192.168.200.1 (dynamic)</span>
<span class="go">[000081.983 INF] inet: peer=192.168.200.1:7777 (-)</span>
<span class="go">[000081.987 INF] uwb: panid=x0000 addr=xDECA84B1B8544434</span>
<span class="go">[000081.992 INF] uwbmac: connected</span>
<span class="go">[000081.997 INF] mode: gn (act)</span>
<span class="go">[000082.000 INF] cfg: enc=0 ble=1 leds=1 fwup=0 label=ID4434</span>
<span class="go">[000082.005 INF] enc: off (nokey)</span>
<span class="go">[000082.008 INF] gw: connected</span>
</pre></div>
</div>
</div></blockquote>
</li>
<li><p>システムの正しいステータスTLSが有効になっています</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">leaps&gt; si</span>
<span class="go">[000027.316 INF] sys: fw1 fw_ver=x01030000 cfg_ver=x00030000</span>
<span class="go">[000027.321 INF] inet: up tls=on addr=192.168.1.100 mask=255.255.255.0 gw=192.168.200.1 (dynamic)</span>
<span class="go">[000027.328 INF] inet: peer=123.123.123.123:7777(server.example.com)</span>
<span class="go">[000027.332 INF] uwb: panid=x0000 addr=xDECA84B1B8544434</span>
<span class="go">[000027.337 INF] uwbmac: connected</span>
<span class="go">[000027.342 INF] mode: gn (act)</span>
<span class="go">[000027.345 INF] cfg: enc=0 ble=1 leds=1 fwup=0 label=ID4434</span>
<span class="go">[000027.350 INF] enc: off (nokey)</span>
<span class="go">[000027.353 INF] gw: connected</span>
</pre></div>
</div>
</div></blockquote>
</li>
</ul>
</div></blockquote>
</li>
<li><p>LEAPS Centerを開く</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">PANS</span> <span class="pre">PRO</span> <span class="pre">Docker</span></code> または <code class="docutils literal notranslate"><span class="pre">PANS</span> <span class="pre">PRO</span> <span class="pre">Raspberry</span> <span class="pre">Pi</span></code> 経由で起動します。</p></li>
</ul>
</li>
<li><p>ログイン</p>
<ul class="simple">
<li><p>ユーザー名 <code class="docutils literal notranslate"><span class="pre">admin</span></code> とパスワード <code class="docutils literal notranslate"><span class="pre">admin</span></code> を使用します。</p></li>
</ul>
<a class="reference internal image-reference" href="../../../_images/leaps_center_login.png"><img alt="../../../_images/leaps_center_login.png" class="align-center" src="/docs-assets/ja/_images/leaps_center_login.png" style="width: 762.8000000000001px; height: 360.0px;"></a>
</li>
<li><p>ネットワークの選択</p>
<ul class="simple">
<li><p>左側のナビゲーション メニューで [ネットワーク] をクリックします。</p></li>
</ul>
</li>
<li><p>新しいネットワークを追加</p>
<ul class="simple">
<li><p><strong>名前</strong> と <strong>ID</strong> を入力します。</p></li>
<li><p><strong>プロトコル タイプ</strong> を <strong>PANS</strong> として選択します。</p></li>
<li><p><strong>ホスト</strong> と <strong>TCP ポート</strong> を入力します。</p></li>
<li><p><strong>ユーザー名</strong>、<strong>パスワード</strong>、<strong>トピック プレフィックス</strong> を入力します。</p></li>
</ul>
</li>
<li><p>接続をテストします</p>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">テスト</span></code> ボタンを押して接続を確認し、<code class="docutils literal notranslate"><span class="pre">保存</span></code> を押してネットワークを作成します。</p></li>
</ul>
<a class="reference internal image-reference" href="../../../_images/leaps_center_pans.png"><img alt="../../../_images/leaps_center_pans.png" class="align-center" src="/docs-assets/ja/_images/leaps_center_pans.png" style="width: 764.4000000000001px; height: 360.40000000000003px;"></a>
</li>
<li><p>完了すると、ネットワークの視覚化がアプリケーションの 2D グリッド ビューと 3D グリッド ビューの両方に表示されます。詳細については、 <code class="docutils literal notranslate"><span class="pre">LEAPS</span> <span class="pre">Center</span></code> の構成と使用方法を参照してください。</p></li>
</ol>
</div>
<input id="sd-tab-item-2" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-2">
詳細</label><div class="sd-tab-content docutils">
<p><a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/pans-pro-api#pans-pro-api"><span class="std std-ref">PANS PRO API</span></a> への参照。</p>
</div>
<input id="sd-tab-item-3" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-3">
トラブルシューティング</label><div class="sd-tab-content docutils">
<ul class="simple">
<li><p>Bluetooth Low Energy (BLE) と LED が両方ともオフの場合、ユーザーはボードが機能していないと誤って認識する可能性があります。このシナリオでは、ユーザーの唯一の手段は、工場出荷時設定へのリセット (<a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/sys#frst"><span class="std std-ref">frst</span></a>) コマンドを開始することです。</p></li>
<li><p>バージョンを確認してください。最新の正式バージョンを使用することをお勧めします。</p></li>
</ul>
</div>
</div>
<div class="admonition note">
<p class="admonition-title">注釈</p>
<ul class="simple">
<li><p>このデモの威力をさらに詳しく調べるには、ソフトウェア インフラストラクチャを参照してください。私たちのサポートには <a class="reference internal" href="/docs/ja/pans-pro-rtls/quick-start-guide/panspro-docker#panspro-docker"><span class="std std-ref">PANS PRO Docker</span></a> と <a class="reference internal" href="/docs/ja/pans-pro-rtls/quick-start-guide/panspro-rpi#panspro-rpi"><span class="std std-ref">PANS PRO Raspberry Pi</span></a> が含まれます。</p></li>
<li><p>弊社製品に関するご意見やご質問については、<a class="reference external" href="https://forum.leapslabs.com">LEAPS フォーラム</a> にアクセスすることをお勧めします。</p></li>
</ul>
</div>
</div>


           </div>
