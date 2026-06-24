---
title: "ダウンリンク TDoA RTLS デモ"
lang: ja
slug: "udk/udk-start/downlink-tdoa-rtls-demo"
section: "udk"
sourceUrl: "https://docs.leapslabs.com/ja/udk/udk-start/downlink-tdoa-rtls-demo/"
order: 109
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="downlink-tdoa-rtls-demo">
<span id="anchor-dtdoa"></span><h1>ダウンリンク TDoA RTLS デモ</h1>
<a class="reference internal image-reference" href="../../../_images/downlink_tdoa_rtls_demo.png"><img alt="../../../_images/downlink_tdoa_rtls_demo.png" class="align-right" src="/docs-assets/ja/_images/downlink_tdoa_rtls_demo.png" style="width: 216.0px; height: 245.88px;"></a>
<p><strong>セットアップの準備</strong></p>
<ol class="arabic simple">
<li><p><a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> アプリケーションがインストールされました。</p></li>
<li><p>少なくとも 5 つの LC14 デバイス。</p></li>
<li><p>デバイスに電力を供給するためのバッテリーまたは USB-C ケーブル。</p></li>
<li><p><em>推奨: アンカー デバイスの取り付けにはカメラ マウントを備えたクランプまたは三脚を使用します。</em></p></li>
<li><p><em>オプション: Putty、Teraterm、minicom、またはコンピュータにインストールされているお気に入りのターミナル アプリケーション。</em></p></li>
</ol>
<p><strong>セットアップ時間:</strong> 5 分未満</p>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-0" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-0">
クイックスタート</label><div class="sd-tab-content docutils">
<p><strong>概要</strong></p>
<p>このセットアップは、<span class="red-text">ダウンリンク到着時間差 (DL-TDoA)</span> テクノロジーを使用した、完全なプライバシーを備えた受信専用モードでの無制限の量のタグのリアルタイム ナビゲーションを示し、タグ位置ナビゲーションを備えた LEAPS Manager アプリケーションを示します。</p>
<p><strong>代表的なアプリケーション</strong>: マッピングを使用した屋内ナビゲーション、自律ロボットおよび車両ナビゲーション、別の通信チャネルを通じて送信される位置データを使用した資産追跡。</p>
<p><strong>セットアップ手順</strong></p>
<ol class="arabic simple">
<li><p>デバイスの電源を <span class="red-text">ON</span> にします。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>静的にマウントされたデバイスはアンカーとして機能し、位置情報をタグに提供します。</p></li>
<li><p>移動デバイスは、ナビゲーション モードで構成されたタグとして、受信モードのみで機能し、送信は行われません (GNSS のようなモード)。</p></li>
<li><p>タグの数に制限はありません。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="2">
<li><p><a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> のデモ セレクターを使用して設定します。</p></li>
</ol>
<blockquote>
<div><p>2.1。 LEAPS Manager を開き、メイン ページから <span class="red-text">Demo Selector</span> を選択します。</p>
<p>2.2。 <span class="red-text">ダウンリンク TDoA RTLS</span> を選択します。</p>
<p>2.3。 Bluetooth 経由で検出されたデバイスのリストがリストに表示されます。必要に応じて、下にスワイプしてリストを更新します。</p>
<p>2.4。デモに使用するデバイスを選択します。上部の <span class="red-text">アンカー</span> と <span class="red-text">タグ</span> は、デモに必要なデバイスの数を示します。</p>
<p>2.5。 <span class="red-text">SAVE</span> を押して、デバイスを LEAPS RTLS モード、ネットワーク <span class="red-text">プロファイル 2 (TWR+UL / DL-Data、DL-TDoA をサポート)</span> に設定します。</p>
<p>2.6。 [アンカー設定] ポップアップ ウィンドウが表示され、アンカーの位置を設定するオプションが提供されます。必要に応じて、 <span class="red-text">手動</span>、<span class="red-text">自動位置決め</span>、または <span class="red-text">現在位置を維持</span> を選択し、<span class="red-text">OK</span> を押します。</p>
<p>2.7。デバイスが起動すると、<span class="red-text">赤い LED</span> が点滅することを目視で確認してください。</p>
<img alt="../../../_images/downlinktdoartlsdemo-manual.gif" class="align-center" src="/docs-assets/ja/_images/downlinktdoartlsdemo-manual.gif">
</div></blockquote>
<ol class="arabic simple" start="3">
<li><p>デバイスが正常に構成されると、LEAPS Demo Network ウィンドウが構成されたノードのリストとともに表示されます。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p><em>推奨: アラーム機能を使用してデバイスを識別し、正しい物理的な場所に移動します。</em></p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="4">
<li><p>上部のドロップダウン メニューにある <span class="red-text">グリッド</span> を開くか、位置アイコンをタップしてデバイスとその位置を視覚化します。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p><a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> は <span class="red-text">プロファイル 2 (TWR+UL / DL-Data、DL-TDoA をサポート)</span> に設定されていますが、自動状態です。したがって、地図上でタグの座標を確認できます。</p></li>
</ul>
<img alt="../../../_images/downlinktdoartlsdemo-2d.gif" class="align-center" src="/docs-assets/ja/_images/downlinktdoartlsdemo-2d.gif">
<p><em>(GIF 画像では、アンカーポイントが設定され、1 メートル離れて配置されます)</em></p>
<ul class="simple">
<li><p>アプリケーションを使用してノードとネットワークを構成および視覚化する方法の詳細については、<a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> を参照してください。</p></li>
</ul>
</div></blockquote>
</div>
<input id="sd-tab-item-1" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-1">
詳細</label><div class="sd-tab-content docutils">
<p><strong>高度なセットアップ</strong></p>
<p>高度なセットアップの準備をしてください。ターミナルの能力を活用して、プロのようにデバイスを設定できるようにお手伝いします。以下の手順に従うだけで準備は完了です。</p>
<ol class="arabic simple">
<li><p>USB-C データ ケーブルを使用して、デバイスの <a class="reference internal" href="/docs/ja/udk/udk-start/device-hw-interfaces#hardware-interface"><span class="std std-ref">USB-C データ ポート 1</span></a> または <a class="reference internal" href="/docs/ja/udk/udk-start/device-hw-interfaces#hardware-interface"><span class="std std-ref">USB-C データ ポート 2</span></a> を PC に接続します。</p></li>
</ol>
<blockquote>
<div><img alt="../../../_images/leaps-connect-usb-port1.gif" class="align-center" src="/docs-assets/ja/_images/leaps-connect-usb-port1.gif">
</div></blockquote>
<ol class="arabic simple" start="2">
<li><p>Putty、Teraterm、Minicom などの希望のターミナル アプリケーション、またはお気に入りのターミナル アプリケーションを使用してシリアル ポートに接続します。ボーレートを <span class="red-text">115200</span> に設定する必要があります。</p></li>
</ol>
<blockquote>
<div><p>たとえば、Ubuntu (Linux) で Minicom を使用します。</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">minicom</span> <span class="o">-</span><span class="n">b</span> <span class="mi">115200</span> <span class="o">-</span><span class="n">D</span> <span class="o">/</span><span class="n">dev</span><span class="o">/</span><span class="n">ttyACM0</span>
</pre></div>
</div>
</div></blockquote>
<ol class="arabic simple" start="3">
<li><p>シェル コンソールで <span class="red-text">ダブル Enter</span> を押して、コマンド ライン制御システムにアクセスします。</p></li>
</ol>
<blockquote>
<div><p>たとえば、Ubuntu (Linux) では、<span class="red-text">/dev/ttyACM0</span> を開き、<span class="red-text">double Enter</span> を押します。</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>minicom -b 115200 -D /dev/ttyACM0

  Welcome to minicom 2.7.1

  OPTIONS: I18n
  Compiled on Dec 23 2019, 02:06:26.
  Port /dev/ttyACM0, 16:02:57

  Press CTRL-A Z for help on special keys



  Low Energy Accurate Positioning System

  FOR DEMO PURPOSE ONLY, NOT FOR SALE.

  Copyright :  2016-2023 LEAPS
  License   :  Please visit https://www.leapslabs.com/leaps-rtls-license
  Compiled  :  Jan  6 2024 09:38:07 (v0.15.0-ab84fb)

  Help      :  ? or help

  leaps&gt;
</pre></div>
</div>
</div></blockquote>
<ol class="arabic simple" start="4">
<li><p>デバイスごとに構成するには、次の手順を実行します。</p></li>
</ol>
<blockquote>
<div><ol class="loweralpha simple">
<li><p>デバイスをデフォルトにリセットし、<span class="red-text">frst</span> コマンドを実行します。 (オプション)</p></li>
</ol>
<blockquote>
<div><div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ leaps&gt; frst
frst ok
</pre></div>
</div>
</div></blockquote>
<img alt="../../../_images/reset-command.gif" class="align-center" src="/docs-assets/ja/_images/reset-command.gif">
<p><em>(デバイスが正常にリセットされるまで監視して待ちます。その後、 :red:`ダブル Enter` を押してコマンド ライン制御システムにアクセスします。)</em></p>
<ol class="loweralpha simple" start="2">
<li><p>コマンド <span class="red-text">nps 2</span> を使用して、各デバイスの <span class="red-text">プロファイル 2 (TWR+UL / DL-Data、DL-TDoA をサポート)</span> を設定します。</p></li>
</ol>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ leaps&gt; nps 2
nps: ok
</pre></div>
</div>
<ol class="loweralpha simple" start="3">
<li><p><span class="red-text">nis</span> コマンドを使用して、ネットワーク内のすべてのデバイスを設定します。</p></li>
</ol>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ leaps&gt; nis 0x1234
nis: ok
</pre></div>
</div>
<ul class="simple">
<li><p><strong>その後、デバイスをリセットする必要があります。設定を更新するにはデバイスをリセットする必要があります</strong>。 <span class="red-text">reset</span> コマンドを使用してデバイスをリセットします。</p></li>
</ul>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ leaps&gt; reset
reset ok
</pre></div>
</div>
</div></blockquote>
<div class="admonition note">
<p class="admonition-title">注釈</p>
<p>この例では、 <strong>イニシエーターを有効にしたアンカー</strong>、 <strong>3 つのアンカー</strong>、 <strong>タグ</strong> を構成します。</p>
</div>
<ol class="arabic simple" start="5">
<li><p>各アンカーとタグのモードを設定します。</p></li>
</ol>
<blockquote>
<div><ul>
<li><p>イニシエータを有効にして <span class="red-text">アンカーを設定するには、コマンド</span>  <span class="red-text">nmi</span> を使用してデバイスを設定します。</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ leaps&gt; nmi
</pre></div>
</div>
<p><em>その後、デバイスがリセットされ、コマンド ライン制御システムに再度アクセスするには、Enter キーを 2 回押します。</em></p>
</li>
<li><p><span class="red-text">3 アンカー</span> を設定するには、コマンド <span class="red-text">nma</span> を使用して 3 つのデバイスをアンカー モードに設定しますが、イニシエーターは有効にしません。</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ leaps&gt; nma
</pre></div>
</div>
<p><em>その後、デバイスがリセットされ、コマンド ライン制御システムに再度アクセスするには、Enter キーを 2 回押します。</em></p>
</li>
<li><p><span class="red-text">a tag</span> を設定するには、コマンド <span class="red-text">nmt</span> を使用してデバイスをタグ モードに設定します</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ leaps&gt; nmt
</pre></div>
</div>
<p><em>その後、デバイスがリセットされ、コマンド ライン制御システムに再度アクセスするには、Enter キーを 2 回押します。</em></p>
</li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="6">
<li><p>いずれかのアンカーのクロック基準を設定します。</p></li>
</ol>
<blockquote>
<div><ul>
<li><p>少なくとも 1 つのアンカーが構成されています。</p></li>
<li><p><span class="red-text">クロック参照を有効にしてアンカー</span> を設定するには、コマンド <span class="red-text">acs cr</span> を使用してデバイスを設定します。</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ leaps&gt; acs cr 1
</pre></div>
</div>
</li>
<li><p><strong>その後、デバイスをリセットする必要があります。設定を更新するにはデバイスをリセットする必要があります</strong>。 <span class="red-text">reset</span> コマンドを使用してデバイスをリセットします。</p></li>
</ul>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ leaps&gt; reset
reset ok
</pre></div>
</div>
</div></blockquote>
<ol class="arabic simple" start="7">
<li><p>各アンカーの実際の位置を設定します。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>位置を取得するには、アンカーごとに <span class="red-text">pg</span> コマンドを使用し、位置を設定するには、<span class="red-text">ps</span> コマンドを使用します。</p></li>
<li><p>この例では、4 つのアンカーが 1 メートル間隔で配置され、正方形に配置されるように設定します。</p></li>
</ul>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-3" name="sd-tab-set-1" type="radio">
<label class="sd-tab-label" for="sd-tab-item-3">
アンカー 1 (イニシエーターを有効にする)</label><div class="sd-tab-content docutils">
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">leaps</span><span class="o">&gt;</span> <span class="n">ps</span> <span class="mi">1000</span> <span class="mi">1000</span> <span class="mi">0</span>
<span class="n">ps</span><span class="p">:</span> <span class="n">ok</span>
<span class="n">leaps</span><span class="o">&gt;</span> <span class="n">pg</span>
<span class="n">pg</span><span class="p">:</span> <span class="n">x</span><span class="p">:</span><span class="mi">1000</span> <span class="n">y</span><span class="p">:</span><span class="mi">1000</span> <span class="n">z</span><span class="p">:</span><span class="mi">0</span> <span class="n">qf</span><span class="p">:</span><span class="mi">100</span>
<span class="n">leaps</span><span class="o">&gt;</span>
</pre></div>
</div>
</div>
<input id="sd-tab-item-4" name="sd-tab-set-1" type="radio">
<label class="sd-tab-label" for="sd-tab-item-4">
アンカー 2</label><div class="sd-tab-content docutils">
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">leaps</span><span class="o">&gt;</span> <span class="n">ps</span> <span class="mi">0</span> <span class="mi">0</span> <span class="mi">0</span>
<span class="n">ps</span><span class="p">:</span> <span class="n">ok</span>
<span class="n">leaps</span><span class="o">&gt;</span> <span class="n">pg</span>
<span class="n">pg</span><span class="p">:</span> <span class="n">x</span><span class="p">:</span><span class="mi">0</span> <span class="n">y</span><span class="p">:</span><span class="mi">0</span> <span class="n">z</span><span class="p">:</span><span class="mi">0</span> <span class="n">qf</span><span class="p">:</span><span class="mi">100</span>
<span class="n">leaps</span><span class="o">&gt;</span>
</pre></div>
</div>
</div>
<input id="sd-tab-item-5" name="sd-tab-set-1" type="radio">
<label class="sd-tab-label" for="sd-tab-item-5">
アンカー 3</label><div class="sd-tab-content docutils">
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">leaps</span><span class="o">&gt;</span> <span class="n">ps</span> <span class="mi">1000</span> <span class="mi">0</span> <span class="mi">0</span>
<span class="n">ps</span><span class="p">:</span> <span class="n">ok</span>
<span class="n">leaps</span><span class="o">&gt;</span> <span class="n">pg</span>
<span class="n">pg</span><span class="p">:</span> <span class="n">x</span><span class="p">:</span><span class="mi">1000</span> <span class="n">y</span><span class="p">:</span><span class="mi">0</span> <span class="n">z</span><span class="p">:</span><span class="mi">0</span> <span class="n">qf</span><span class="p">:</span><span class="mi">100</span>
<span class="n">leaps</span><span class="o">&gt;</span>
</pre></div>
</div>
</div>
<input id="sd-tab-item-6" name="sd-tab-set-1" type="radio">
<label class="sd-tab-label" for="sd-tab-item-6">
アンカー4</label><div class="sd-tab-content docutils">
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">leaps</span><span class="o">&gt;</span> <span class="n">ps</span> <span class="mi">0</span> <span class="mi">1000</span> <span class="mi">0</span>
<span class="n">ps</span><span class="p">:</span> <span class="n">ok</span>
<span class="n">leaps</span><span class="o">&gt;</span> <span class="n">pg</span>
<span class="n">pg</span><span class="p">:</span> <span class="n">x</span><span class="p">:</span><span class="mi">0</span> <span class="n">y</span><span class="p">:</span><span class="mi">1000</span> <span class="n">z</span><span class="p">:</span><span class="mi">0</span> <span class="n">qf</span><span class="p">:</span><span class="mi">100</span>
<span class="n">leaps</span><span class="o">&gt;</span>
</pre></div>
</div>
</div>
</div>
<ul class="simple">
<li><p>アンカーの構成が正常に完了したら、アンカーを物理的な正しい位置は 1 メートル離れています。</p></li>
<li><p>さらに、 <a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> を使用して、デバイスとその位置を視覚化することもできます。</p></li>
</ul>
<a class="reference internal image-reference" href="../../../_images/downlinktdoartlsdemo-anchors.jpeg"><img alt="../../../_images/downlinktdoartlsdemo-anchors.jpeg" class="align-center" src="/docs-assets/ja/_images/downlinktdoartlsdemo-anchors.jpeg" style="width: 80%;"></a>
</div></blockquote>
<ol class="arabic simple" start="8">
<li><p>各タグの設定により、測定に <span class="red-text">DL-TDoA</span> テクノロジーを使用できるようになります。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>設定するには、タグに対して <span class="red-text">tcs mode 2</span> コマンドを使用します。</p></li>
</ul>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ leaps&gt; tcs mode 2
tcs: ok
</pre></div>
</div>
<ul class="simple">
<li><p><strong>その後、構成を更新するにはデバイスをリセットする必要があります</strong>。 <span class="red-text">reset</span> コマンドを使用してデバイスをリセットします。</p></li>
</ul>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ leaps&gt; reset
reset ok
</pre></div>
</div>
</div></blockquote>
<ol class="arabic simple" start="9">
<li><p>デフォルトでは、<span class="red-text">通常の更新レート</span> は 0.1 秒/10Hz、<span class="red-text">定常的な更新レート</span> は 5.0 秒/0.2Hz です。速度を上げるには、<span class="red-text">urs</span> コマンドを使用します。</p></li>
</ol>
<blockquote>
<div><p>たとえば、<span class="red-text">通常の更新レート</span> を 0.1 秒/ 10Hz に設定し、<span class="red-text">定常的な更新レート</span> を 0.1 秒 / 10Hz に設定します。次のコマンドを実行します。</p>
<blockquote>
<div><div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ leaps&gt; urs 1 1
urs: ok
</pre></div>
</div>
</div></blockquote>
</div></blockquote>
<ol class="arabic simple" start="10">
<li><p>ステップ 5、6、7、および 8 では、<span class="red-text">si</span> コマンドを使用して、モード、プロファイル、およびネットワーク構成が正しいかどうかを確認できます。 (オプション)</p></li>
</ol>
<blockquote>
<div><p>たとえば、4 つのアンカーと 1 つのタグの場合:</p>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-7" name="sd-tab-set-2" type="radio">
<label class="sd-tab-label" for="sd-tab-item-7">
アンカー 1 (イニシエーターを有効にする)</label><div class="sd-tab-content docutils">
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">mode:</span> <span class="pre">ani</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">panid=x1234</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prof=2</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">cr=1</span></code></p></li>
</ul>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>leaps&gt; nps 2
nps: ok
leaps&gt; nis 0x1234
nis: ok
leaps&gt; acs cr 1
nis: ok
leaps&gt; nmi


Low Energy Accurate Positioning System

FOR DEMO PURPOSE ONLY, NOT FOR SALE.

Copyright :  2016-2023 LEAPS
License   :  Please visit https://www.leapslabs.com/leaps-rtls-license
Compiled  :  Jan  6 2024 09:38:07 (v0.15.0-ab84fb)

Help      :  ? or help

leaps&gt; si
[000008.695 INF] release: LEAPS RTLS v0.15.0-ab84fb
[000008.696 INF] sys: main main_ver=x02000001 cfg_ver=x01040000 batt=none board=LC14_B
[000008.696 INF] uwb: ch9 prf64 plen128 pac8 txcode9 rxcode9 baud6800 phrmodeext phrratestd sfdtypeieee4a sfdto129 stsmodeoff stslen64 pdoamodem0
[000008.696 INF] uwb: tx_pwr=x34/xFAFAFAFA sts:shr:phr:data=27.7:27.7:27.7:27.7[dB] cpl=FCC/ETSI pgcnt=5
[000008.697 INF] uwb: lna=1 pa=0 rf1=1 rf2=0 xtaltrim=27 tx_delay=16438 rx_delay=16438
[000008.697 INF] uwb: panid=x1234 addr=xDECA0E27530083A2
[000008.700 INF] mode: ani (act,-)
[000008.715 INF] uwbmac: disconnected prof=2 (manual)
[000008.715 INF] uwbmac: bh disconnected
[000008.716 INF] cfg: sync=0 fwup=1 ble=1 leds=1 init=1 uab=1 bh=auto bh_stat=off cr=1 upd_rate_stat=30 label=ID83A2
[000008.744 INF] enc: off
[000008.744 INF] ble: addr=F8:64:22:75:6C:F7
leaps&gt;
</pre></div>
</div>
</div>
<input id="sd-tab-item-8" name="sd-tab-set-2" type="radio">
<label class="sd-tab-label" for="sd-tab-item-8">
アンカー 2</label><div class="sd-tab-content docutils">
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">mode:</span> <span class="pre">an</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">panid=x1234</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prof=2</span></code></p></li>
</ul>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>leaps&gt; nps 2
nps: ok
leaps&gt; nis 0x1234
nis: ok
leaps&gt; nma


Low Energy Accurate Positioning System

FOR DEMO PURPOSE ONLY, NOT FOR SALE.

Copyright :  2016-2023 LEAPS
License   :  Please visit https://www.leapslabs.com/leaps-rtls-license
Compiled  :  Jan  6 2024 09:38:07 (v0.15.0-ab84fb)

Help      :  ? or help

leaps&gt; [000004.252 INF] uwbmac: connected

leaps&gt; si
[000073.748 INF] release: LEAPS RTLS v0.15.0-ab84fb
[000073.748 INF] sys: main main_ver=x02000001 cfg_ver=x01040000 batt=none board=LC14_B
[000073.748 INF] uwb: ch9 prf64 plen128 pac8 txcode9 rxcode9 baud6800 phrmodeext phrratestd sfdtypeieee4a sfdto129 stsmodeoff stslen64 pdoamodem0
[000073.749 INF] uwb: tx_pwr=x34/xE6E6E6E6 sts:shr:phr:data=25.8:25.8:25.8:25.8[dB] cpl=FCC/ETSI pgcnt=25
[000073.749 INF] uwb: lna=1 pa=0 rf1=1 rf2=0 xtaltrim=32 tx_delay=16438 rx_delay=16438
[000073.750 INF] uwb: panid=x1234 addr=xDECA9DD29FD0CBBB
[000073.753 INF] mode: an (act,-)
[000073.764 INF] uwbmac: connected prof=2 (manual)
[000073.764 INF] uwbmac: bh disconnected
[000073.764 INF] cfg: sync=0 fwup=1 ble=1 leds=1 init=0 uab=1 bh=auto bh_stat=off cr=0 upd_rate_stat=30 label=IDCBBB
[000073.796 INF] enc: off
[000073.796 INF] ble: addr=E6:92:A3:6B:05:21
leaps&gt;
</pre></div>
</div>
</div>
<input id="sd-tab-item-9" name="sd-tab-set-2" type="radio">
<label class="sd-tab-label" for="sd-tab-item-9">
アンカー 3</label><div class="sd-tab-content docutils">
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">mode:</span> <span class="pre">an</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">panid=x1234</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prof=2</span></code></p></li>
</ul>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>leaps&gt; nps 2
nps: ok
leaps&gt; nis 0x1234
nis: ok
leaps&gt; nma


Low Energy Accurate Positioning System

FOR DEMO PURPOSE ONLY, NOT FOR SALE.

Copyright :  2016-2023 LEAPS
License   :  Please visit https://www.leapslabs.com/leaps-rtls-license
Compiled  :  Jan  6 2024 09:38:07 (v0.15.0-ab84fb)

Help      :  ? or help

leaps&gt; si
[000031.142 INF] release: LEAPS RTLS v0.15.0-ab84fb
[000031.142 INF] sys: main main_ver=x02000001 cfg_ver=x01040000 batt=none board=LC14_B
[000031.143 INF] uwb: ch9 prf64 plen128 pac8 txcode9 rxcode9 baud6800 phrmodeext phrratestd sfdtypeieee4a sfdto129 stsmodeoff stslen64 pdoamodem0
[000031.143 INF] uwb: tx_pwr=x34/xEEEEEEEE sts:shr:phr:data=26.5:26.5:26.5:26.5[dB] cpl=FCC/ETS5
[000031.144 INF] uwb: lna=1 pa=0 rf1=1 rf2=0 xtaltrim=32 tx_delay=16436 rx_delay=16436
[000031.144 INF] uwb: panid=x1234 addr=xDECA7A20DFE04F2E
[000031.148 INF] mode: an (act,-)
[000031.163 INF] uwbmac: connected prof=2 (manual)
[000031.163 INF] uwbmac: bh disconnected
[000031.163 INF] cfg: sync=0 fwup=1 ble=1 leds=1 init=0 uab=1 bh=auto bh_stat=off cr=0 upd_rate_stat=30 label=ID4F2E
[000031.190 INF] enc: off
[000031.190 INF] ble: addr=C8:D9:F3:F1:7D:CE
leaps&gt;
</pre></div>
</div>
</div>
<input id="sd-tab-item-10" name="sd-tab-set-2" type="radio">
<label class="sd-tab-label" for="sd-tab-item-10">
アンカー4</label><div class="sd-tab-content docutils">
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">mode:</span> <span class="pre">an</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">panid=x1234</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prof=2</span></code></p></li>
</ul>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>leaps&gt; nps 2
nps: ok
leaps&gt; nis 0x1234
nis: ok
leaps&gt; nma


Low Energy Accurate Positioning System

FOR DEMO PURPOSE ONLY, NOT FOR SALE.

Copyright :  2016-2023 LEAPS
License   :  Please visit https://www.leapslabs.com/leaps-rtls-license
Compiled  :  Jan  6 2024 09:38:07 (v0.15.0-ab84fb)

Help      :  ? or help

leaps&gt; si
[000004.702 INF] release: LEAPS RTLS v0.15.0-ab84fb
[000004.703 INF] sys: main main_ver=x02000001 cfg_ver=x01040000 batt=none board=LC14_B
[000004.703 INF] uwb: ch9 prf64 plen128 pac8 txcode9 rxcode9 baud6800 phrmodeext phrratestd sfdtypeieee4a sfdto129 stsmodeoff stslen64 pdoamodem0
[000004.703 INF] uwb: tx_pwr=x34/xC6C6C6C6 sts:shr:phr:data=22.6:22.6:22.6:22.6[dB] cpl=FCC/ETSI pgcnt=2365
[000004.704 INF] uwb: lna=1 pa=0 rf1=1 rf2=0 xtaltrim=32 tx_delay=16431 rx_delay=16431
[000004.704 INF] uwb: panid=x1234 addr=xDECAED5BC8B1468D
[000004.707 INF] mode: an (act,-)
[000004.720 INF] uwbmac: connected prof=2 (manual)
[000004.720 INF] uwbmac: bh disconnected
[000004.720 INF] cfg: sync=0 fwup=1 ble=1 leds=1 init=0 uab=1 bh=auto bh_stat=off cr=0 upd_rate_stat=30 label=ID468D
[000004.751 INF] enc: off
[000004.752 INF] ble: addr=F3:D9:66:75:93:EB
leaps&gt;
</pre></div>
</div>
</div>
<input id="sd-tab-item-11" name="sd-tab-set-2" type="radio">
<label class="sd-tab-label" for="sd-tab-item-11">
タグ</label><div class="sd-tab-content docutils">
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">mode:</span> <span class="pre">tn</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">panid=x1234</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prof=2</span></code></p></li>
</ul>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>leaps&gt; nps 2
nps: ok
leaps&gt; nis 0x1234
nis: ok
leaps&gt; nmt


Low Energy Accurate Positioning System

FOR DEMO PURPOSE ONLY, NOT FOR SALE.

Copyright :  2016-2023 LEAPS
License   :  Please visit https://www.leapslabs.com/leaps-rtls-license
Compiled  :  Jan  6 2024 09:38:07 (v0.15.0-ab84fb)

Help      :  ? or help

leaps&gt; tcs mode 2
tcs: ok
leaps&gt; urs 1 1
urs: ok
leaps&gt; reset
reset ok


Low Energy Accurate Positioning System

FOR DEMO PURPOSE ONLY, NOT FOR SALE.

Copyright :  2016-2023 LEAPS
License   :  Please visit https://www.leapslabs.com/leaps-rtls-license
Compiled  :  Jan  6 2024 09:38:07 (v0.15.0-ab84fb)

Help      :  ? or help

leaps&gt; si
[000006.325 INF] release: LEAPS RTLS v0.15.0-ab84fb
[000006.325 INF] sys: main main_ver=x02000001 cfg_ver=x01040000 batt=none board=LC14_B
[000006.326 INF] uwb: ch9 prf64 plen128 pac8 txcode9 rxcode9 baud6800 phrmodeext phrratestd sfdtypeieee4a sfdto129 stsmodeoff stslen64 pdoamodem0
[000006.326 INF] uwb: tx_pwr=x34/xB6B6B6B6 sts:shr:phr:data=21.1:21.1:21.1:21.1[dB] cpl=FCC/ETSI pgcnt=231 temp=25
[000006.327 INF] uwb: lna=1 pa=0 rf1=1 rf2=0 xtaltrim=43 tx_delay=16434 rx_delay=16434
[000006.327 INF] uwb: panid=x1234 addr=xDECA80CB2C558A11
[000006.330 INF] mode: tn (act,rtdoa,np,le)
[000006.346 INF] uwbmac: connected prof=2 (manual)
[000006.346 INF] uwbmac: bh disconnected
[000006.347 INF] cfg: sync=0 fwup=1 ble=1 leds=1 le=1 lp=0 uab=1 stat_det=1 (sens=2) mode=2 upd_rate_norm=1 upd_rate_stat=1 label=ID8A11
[000006.374 INF] enc: off
[000006.374 INF] ble: addr=E8:BB:0A:C9:93:4E
leaps&gt;
</pre></div>
</div>
</div>
</div>
</div></blockquote>
<ol class="arabic simple" start="11">
<li><p>範囲内にあり、デバイス自体に接続されているアンカーのリストを表示するには、<span class="red-text">la</span> コマンドを使用します。 (オプション)</p></li>
</ol>
<blockquote>
<div><p>たとえば、アンカー 1 (イニシエーターを有効にする) では次のようになります:</p>
<blockquote>
<div><div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">leaps</span><span class="o">&gt;</span> <span class="n">la</span>
<span class="p">[</span><span class="mf">001330.813</span> <span class="n">INF</span><span class="p">]</span> <span class="n">AN</span><span class="p">:</span> <span class="n">cnt</span><span class="o">=</span><span class="mi">4</span> <span class="n">seq</span><span class="o">=</span><span class="n">x03</span>
<span class="p">[</span><span class="mf">001330.813</span> <span class="n">INF</span><span class="p">]</span>     <span class="mi">0</span><span class="p">)</span> <span class="nb">id</span><span class="o">=</span><span class="mi">83</span><span class="n">A2</span> <span class="n">seat</span><span class="o">=</span><span class="mi">0</span> <span class="n">clk_lvl</span><span class="o">=</span><span class="mi">0</span> <span class="n">seens</span><span class="o">=</span><span class="mi">0</span> <span class="n">rssi</span><span class="o">=-</span><span class="mi">127</span> <span class="n">cl</span><span class="o">=</span><span class="mi">0000000</span><span class="n">F</span> <span class="n">nbr</span><span class="o">=</span><span class="mi">0000000</span><span class="n">F</span> <span class="n">pos</span><span class="o">=</span><span class="mf">1.00</span><span class="p">:</span><span class="mf">1.00</span><span class="p">:</span><span class="mf">0.00</span>
<span class="p">[</span><span class="mf">001330.814</span> <span class="n">INF</span><span class="p">]</span>     <span class="mi">1</span><span class="p">)</span> <span class="nb">id</span><span class="o">=</span><span class="mi">4</span><span class="n">F2E</span> <span class="n">seat</span><span class="o">=</span><span class="mi">2</span> <span class="n">clk_lvl</span><span class="o">=</span><span class="mi">1</span> <span class="n">seens</span><span class="o">=</span><span class="mi">205</span> <span class="n">rssi</span><span class="o">=-</span><span class="mi">55</span> <span class="n">cl</span><span class="o">=</span><span class="mi">0000000</span><span class="n">F</span> <span class="n">nbr</span><span class="o">=</span><span class="mi">00000000</span> <span class="n">pos</span><span class="o">=</span><span class="mf">1.00</span><span class="p">:</span><span class="mf">0.00</span><span class="p">:</span><span class="mf">0.00</span>
<span class="p">[</span><span class="mf">001330.814</span> <span class="n">INF</span><span class="p">]</span>     <span class="mi">2</span><span class="p">)</span> <span class="nb">id</span><span class="o">=</span><span class="mi">468</span><span class="n">D</span> <span class="n">seat</span><span class="o">=</span><span class="mi">3</span> <span class="n">clk_lvl</span><span class="o">=</span><span class="mi">1</span> <span class="n">seens</span><span class="o">=</span><span class="mi">223</span> <span class="n">rssi</span><span class="o">=-</span><span class="mi">55</span> <span class="n">cl</span><span class="o">=</span><span class="mi">0000000</span><span class="n">F</span> <span class="n">nbr</span><span class="o">=</span><span class="mi">00000000</span> <span class="n">pos</span><span class="o">=</span><span class="mf">0.00</span><span class="p">:</span><span class="mf">1.00</span><span class="p">:</span><span class="mf">0.00</span>
<span class="p">[</span><span class="mf">001330.814</span> <span class="n">INF</span><span class="p">]</span>     <span class="mi">3</span><span class="p">)</span> <span class="nb">id</span><span class="o">=</span><span class="n">CBBB</span> <span class="n">seat</span><span class="o">=</span><span class="mi">1</span> <span class="n">clk_lvl</span><span class="o">=</span><span class="mi">1</span> <span class="n">seens</span><span class="o">=</span><span class="mi">224</span> <span class="n">rssi</span><span class="o">=-</span><span class="mi">55</span> <span class="n">cl</span><span class="o">=</span><span class="mi">0000000</span><span class="n">F</span> <span class="n">nbr</span><span class="o">=</span><span class="mi">00000000</span> <span class="n">pos</span><span class="o">=</span><span class="mf">0.00</span><span class="p">:</span><span class="mf">0.00</span><span class="p">:</span><span class="mf">0.00</span>
<span class="p">[</span><span class="mf">001330.815</span> <span class="n">INF</span><span class="p">]</span>
<span class="n">leaps</span><span class="o">&gt;</span>
</pre></div>
</div>
</div></blockquote>
</div></blockquote>
<p>これで、システムは正常にセットアップされ、構成されました。楽しく使ってください！</p>
</div>
<input id="sd-tab-item-2" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-2">
トラブルシューティング</label><div class="sd-tab-content docutils">
<ol class="arabic">
<li><p>Bluetooth Low Energy (BLE) と LED が両方ともオフの場合、ユーザーはボードが機能していないと誤って認識する可能性があります。このシナリオでは、ユーザーの唯一の手段は、工場出荷時設定へのリセット (<a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/sys#frst"><span class="std std-ref">frst</span></a>) コマンドを開始することです。</p></li>
<li><p>インストールプロセスに関連するいくつかの問題を修正するためのヒントをいくつか紹介します。</p>
<ul class="simple">
<li><p>バージョンを確認してください。最新の正式バージョンを使用することをお勧めします。</p></li>
<li><p>デバイスの現在の状態がわからない場合は、<a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> のデモ セレクターの <span class="red-text">デバイスをデフォルトにリセット</span> 機能を使用します。次のGIF画像を参照してください。</p></li>
</ul>
<img alt="../../../_images/reset-devices-to-defaul-x2.gif" class="align-center" src="/docs-assets/ja/_images/reset-devices-to-defaul-x2.gif">
</li>
</ol>
</div>
</div>
<div class="admonition note">
<p class="admonition-title">注釈</p>
<ul class="simple">
<li><p>ダウンリンク TDoA RTLS デモの位置データは、別の通信チャネルを通じて送信されます。</p></li>
<li><p>弊社製品に関するご意見やご質問については、<a class="reference external" href="https://forum.leapslabs.com">LEAPS フォーラム</a> にアクセスすることをお勧めします。</p></li>
<li><p>既知の制限と問題リストの詳細については、セクション <a class="reference internal" href="/docs/ja/udk/release#udk-releases"><span class="std std-ref">リリース</span></a> を参照してください。</p></li>
</ul>
</div>
</div>


           </div>
