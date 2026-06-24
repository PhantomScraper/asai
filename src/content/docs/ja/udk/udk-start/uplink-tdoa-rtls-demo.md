---
title: "アップリンク TDoA RTLS デモ"
lang: ja
slug: "udk/udk-start/uplink-tdoa-rtls-demo"
section: "udk"
sourceUrl: "https://docs.leapslabs.com/ja/udk/udk-start/uplink-tdoa-rtls-demo/"
order: 43
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="uplink-tdoa-rtls-demo">
<span id="id1"></span><h1>アップリンク TDoA RTLS デモ</h1>
<a class="reference internal image-reference" href="../../../_images/uplink_tdoa_rtls_demo.png"><img alt="../../../_images/uplink_tdoa_rtls_demo.png" class="align-right" src="/docs-assets/ja/_images/uplink_tdoa_rtls_demo.png" style="width: 252.00000000000003px; height: 278.04px;"></a>
<p><strong>セットアップの準備</strong></p>
<ol class="arabic simple">
<li><p><a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> アプリケーションがインストールされました。</p></li>
<li><p>Raspberry Pi 3B 以降のバージョン、またはデータ サーバーおよび Web アプリケーションのインストール用の PC。</p></li>
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
<p>このセットアップは、<span class="red-text">アップリンク到達時間差 (UL-TDoA)</span> テクノロジーを使用した、高精度でのタグのリアルタイム追跡を示します。</p>
<p><strong>典型的なアプリケーション</strong>: 資産と人物の追跡。</p>
<p><strong>セットアップ手順</strong></p>
<ol class="arabic simple">
<li><p>デバイスの電源を <span class="red-text">ON</span> にします。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>静的にマウントされたデバイスはアンカーとして機能し、位置情報をタグに提供します。</p></li>
<li><p>移動デバイスは、アップリンク TDoA 測定モードで設定されたタグとして機能します。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="2">
<li><p><a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> のデモ セレクターを使用して設定します。</p></li>
</ol>
<blockquote>
<div><p>2.1。 LEAPS Manager を開き、メイン ページから <span class="red-text">Demo Selector</span> を選択します。</p>
<p>2.2。 <span class="red-text">アップリンク TDoA RTLS</span> を選択します。</p>
<p>2.3。 Bluetooth 経由で検出されたデバイスのリストがリストに表示されます。必要に応じて、下にスワイプしてリストを更新します。</p>
<p>2.4。デモに使用するデバイスを選択します。上部の <span class="red-text">アンカー</span> と <span class="red-text">タグ</span> は、デモに必要なデバイスの数を示します。</p>
<p>2.5。 <span class="red-text">SAVE</span> を押して、デバイスを LEAPS RTLS モード、ネットワーキング <span class="red-text">プロファイル 5 (UL-TDoA をサポート)</span> に設定します。</p>
<p>2.6。 [アンカー設定] ポップアップ ウィンドウが表示され、アンカーの位置を設定するオプションが提供されます。必要に応じて <span class="red-text">手動</span> または <span class="red-text">現在位置を維持</span> を選択し、<span class="red-text">OK</span> を押します。</p>
<ul class="simple">
<li><p><em>現在、プロファイル 5 では自動位置決めは利用できません。</em></p></li>
</ul>
<p>2.7。デバイスが起動すると、<span class="red-text">赤い LED</span> が点滅することを目視で確認してください。</p>
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
<li><p>上部のドロップダウン メニューにある <span class="red-text">グリッド</span> を開き、デバイスとその位置を視覚化します。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
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

  Copyright :  2016-2024 LEAPS
  License   :  Please visit https://www.leapslabs.com/leaps-rtls-licee
  Compiled  :  Nov  4 2024 12:30:29 (v0.16.4-a916a6

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
<p><em>(デバイスが正常にリセットされるまで監視して待ちます。その後、Enter キーを 2 回押してコマンド ライン制御システムにアクセスします。)</em></p>
<ol class="loweralpha simple" start="2">
<li><p>コマンド <span class="red-text">nps 5</span> を使用して、各デバイスの <span class="red-text">プロファイル 5 (UL-TDoA をサポート)</span> を設定します。</p></li>
</ol>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ leaps&gt; nps 5
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
<li><p><strong>その後、構成を更新するにはデバイスをリセットする必要があります</strong>。 <span class="red-text">reset</span> コマンドを使用してデバイスをリセットします。</p></li>
</ul>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ leaps&gt; reset
reset ok
</pre></div>
</div>
</div></blockquote>
<div class="admonition note">
<p class="admonition-title">注釈</p>
<p>この例では、<em>イニシエーターを有効にしたアンカー</em>、 <strong>3 つのアンカー</strong>、 <strong>タグ</strong> を構成します。</p>
</div>
<ol class="arabic simple" start="5">
<li><p>各アンカーとタグのモードを設定します。</p></li>
</ol>
<blockquote>
<div><ul>
<li><p>イニシエータを有効にして <span class="red-text">アンカーを設定するには、コマンド</span> <span class="red-text">nmi</span> を使用してデバイスを設定します。</p>
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
<li><p>この例では、4 つのアンカーが 3 メートル離れて正方形に配置されるように設定します。</p></li>
</ul>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-3" name="sd-tab-set-1" type="radio">
<label class="sd-tab-label" for="sd-tab-item-3">
アンカー 1 (イニシエーターを有効にする)</label><div class="sd-tab-content docutils">
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">leaps</span><span class="o">&gt;</span> <span class="n">ps</span> <span class="mi">3000</span> <span class="mi">3000</span> <span class="mi">0</span>
<span class="n">ps</span><span class="p">:</span> <span class="n">ok</span>
<span class="n">leaps</span><span class="o">&gt;</span> <span class="n">pg</span>
<span class="n">pg</span><span class="p">:</span> <span class="n">x</span><span class="p">:</span><span class="mi">5000</span> <span class="n">y</span><span class="p">:</span><span class="mi">5000</span> <span class="n">z</span><span class="p">:</span><span class="mi">0</span> <span class="n">qf</span><span class="p">:</span><span class="mi">100</span>
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
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">leaps</span><span class="o">&gt;</span> <span class="n">ps</span> <span class="mi">3000</span> <span class="mi">0</span> <span class="mi">0</span>
<span class="n">ps</span><span class="p">:</span> <span class="n">ok</span>
<span class="n">leaps</span><span class="o">&gt;</span> <span class="n">pg</span>
<span class="n">pg</span><span class="p">:</span> <span class="n">x</span><span class="p">:</span><span class="mi">3000</span> <span class="n">y</span><span class="p">:</span><span class="mi">0</span> <span class="n">z</span><span class="p">:</span><span class="mi">0</span> <span class="n">qf</span><span class="p">:</span><span class="mi">100</span>
<span class="n">leaps</span><span class="o">&gt;</span>
</pre></div>
</div>
</div>
<input id="sd-tab-item-6" name="sd-tab-set-1" type="radio">
<label class="sd-tab-label" for="sd-tab-item-6">
アンカー4</label><div class="sd-tab-content docutils">
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">leaps</span><span class="o">&gt;</span> <span class="n">ps</span> <span class="mi">0</span> <span class="mi">3000</span> <span class="mi">0</span>
<span class="n">ps</span><span class="p">:</span> <span class="n">ok</span>
<span class="n">leaps</span><span class="o">&gt;</span> <span class="n">pg</span>
<span class="n">pg</span><span class="p">:</span> <span class="n">x</span><span class="p">:</span><span class="mi">0</span> <span class="n">y</span><span class="p">:</span><span class="mi">3000</span> <span class="n">z</span><span class="p">:</span><span class="mi">0</span> <span class="n">qf</span><span class="p">:</span><span class="mi">100</span>
<span class="n">leaps</span><span class="o">&gt;</span>
</pre></div>
</div>
</div>
</div>
<ul class="simple">
<li><p>アンカーの構成が正常に完了したら、アンカーを物理的な正しい位置は 1 メートル離れています。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="8">
<li><p>各タグの設定により、測定に <span class="red-text">UL-TDoA</span> テクノロジーを使用できるようになります。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>設定するには、タグに対して <span class="red-text">tcs mode 1</span> コマンドを使用します。</p></li>
</ul>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ leaps&gt; tcs mode 1
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
<li><p>手順 5、7、および 8 では、<span class="red-text">si</span> コマンドを使用して、モード、プロファイル、およびネットワーク構成が正しいかどうかを確認できます。 (オプション)</p></li>
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
<li><p><code class="docutils literal notranslate"><span class="pre">prof=5</span></code></p></li>
</ul>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>leaps&gt; nps 5
nps: ok
leaps&gt; nis 0x1234
nis: ok
leaps&gt; nmi


Low Energy Accurate Positioning System

FOR DEMO PURPOSE ONLY, NOT FOR SALE.

Copyright :  2016-2024 LEAPS
License   :  Please visit https://www.leapslabs.com/leaps-rtls-licee
Compiled  :  Nov  4 2024 12:30:29 (v0.16.4-a916a6

Help      :  ? or help

leaps&gt;si
[000412.823 INF] release: LEAPS RTLS v0.16.4-a916a6
[000412.824 INF] sys: main main_ver=x02040001 cfg_ver=x01040000 batt=none board=LC14_B
[000412.824 INF] uwb: ch9 prf64 plen128 pac8 txcode9 rxcode9 baud6800 phrmodeext phrratestd sfdtypeieee4a sfdto129 stsmodeoff stslen64 pdoamodem0
[000412.825 INF] uwb: tx_pwr=x34/xD6D6D6D6 sts:shr:phr:data=24.2:24.2:24.2:24.2[dB] cpl=FCC/ETSI pgcnt=232 temp=25
[000412.826 INF] uwb: lna=1 pa=0 rf1=1 rf2=0 xtaltrim=37 tx_delay=16436 rx_delay=16436
[000412.827 INF] uwb: panid=x1234 addr=xDECAD674FD208EAA
[000412.828 INF] mode: ani (act,real)
[000412.851 INF] uwbmac: connected prof=5 (manual)
[000412.851 INF] uwbmac: bh disconnected
[000412.852 INF] cfg: sync=0 fwup=1 ble=1 leds=1 init=1 uab=1 bh=auto bh_stat=off cr=0 upd_rate_stat=30 label=ID8EAA
[000412.852 INF] enc: off
[000412.872 INF] ble: addr=F0:26:43:8B:52:4A
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
<li><p><code class="docutils literal notranslate"><span class="pre">prof=5</span></code></p></li>
</ul>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>leaps&gt; nps 5
nps: ok
leaps&gt; nis 0x1234
nis: ok
leaps&gt; nma


Low Energy Accurate Positioning System

FOR DEMO PURPOSE ONLY, NOT FOR SALE.

Copyright :  2016-2024 LEAPS
License   :  Please visit https://www.leapslabs.com/leaps-rtls-licee
Compiled  :  Nov  4 2024 12:30:29 (v0.16.4-a916a6

Help      :  ? or help

leaps&gt;si
[000454.748 INF] release: LEAPS RTLS v0.16.4-a916a6
[000454.749 INF] sys: main main_ver=x02040001 cfg_ver=x01040000 batt=none board=LC14_B
[000454.749 INF] uwb: ch9 prf64 plen128 pac8 txcode9 rxcode9 baud6800 phrmodeext phrratestd sfdtypeieee4a sfdto129 stsmodeoff stslen64 pdoamodem0
[000454.750 INF] uwb: tx_pwr=x34/xCECECECE sts:shr:phr:data=23.4:23.4:23.4:23.4[dB] cpl=FCC/ETSI pgcnt=238 temp=25
[000454.751 INF] uwb: lna=1 pa=0 rf1=1 rf2=0 xtaltrim=32 tx_delay=16426 rx_delay=16426
[000454.752 INF] uwb: panid=x1234 addr=xDECA229121E05886
[000454.753 INF] mode: an (act,-)
[000454.766 INF] uwbmac: connected prof=5 (manual)
[000454.766 INF] uwbmac: bh disconnected
[000454.767 INF] cfg: sync=0 fwup=1 ble=1 leds=1 init=0 uab=1 bh=auto bh_stat=off cr=0 upd_rate_stat=30 label=ID5886
[000454.797 INF] enc: off
[000454.798 INF] ble: addr=FD:3F:4A:2F:BD:F0
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
<li><p><code class="docutils literal notranslate"><span class="pre">prof=5</span></code></p></li>
</ul>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>leaps&gt; nps 5
nps: ok
leaps&gt; nis 0x1234
nis: ok
leaps&gt; nma


Low Energy Accurate Positioning System

FOR DEMO PURPOSE ONLY, NOT FOR SALE.

Copyright :  2016-2024 LEAPS
License   :  Please visit https://www.leapslabs.com/leaps-rtls-licee
Compiled  :  Nov  4 2024 12:30:29 (v0.16.4-a916a6

Help      :  ? or help

leaps&gt; si
[000496.390 INF] release: LEAPS RTLS v0.16.4-a916a6
[000496.390 INF] sys: main main_ver=x02040001 cfg_ver=x01040000 batt=none board=LC14_B
[000496.390 INF] uwb: ch9 prf64 plen128 pac8 txcode9 rxcode9 baud6800 phrmodeext phrratestd sfdtypeieee4a sfdto129 stsmodeoff stslen64 pdoamodem0
[000496.391 INF] uwb: tx_pwr=x34/xC6C6C6C6 sts:shr:phr:data=22.6:22.6:22.6:22.6[dB] cpl=FCC/ETSI pgcnt=236 temp=25
[000496.392 INF] uwb: lna=1 pa=0 rf1=1 rf2=0 xtaltrim=32 tx_delay=16431 rx_delay=16431
[000496.393 INF] uwb: panid=x1234 addr=xDECAED5BC8B1468D
[000496.394 INF] mode: an (act,-)
[000496.413 INF] uwbmac: connected prof=5 (manual)
[000496.414 INF] uwbmac: bh disconnected
[000496.414 INF] cfg: sync=0 fwup=1 ble=1 leds=1 init=0 uab=1 bh=auto bh_stat=off cr=0 upd_rate_stat=30 label=ID468D
[000496.438 INF] enc: off
[000496.439 INF] ble: addr=F3:D9:66:75:93:EB
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
<li><p><code class="docutils literal notranslate"><span class="pre">prof=5</span></code></p></li>
</ul>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>leaps&gt; nps 5
nps: ok
leaps&gt; nis 0x1234
nis: ok
leaps&gt; nma


Low Energy Accurate Positioning System

FOR DEMO PURPOSE ONLY, NOT FOR SALE.

Copyright :  2016-2024 LEAPS
License   :  Please visit https://www.leapslabs.com/leaps-rtls-licee
Compiled  :  Nov  4 2024 12:30:29 (v0.16.4-a916a6

Help      :  ? or help

leaps&gt; si
[000535.583 INF] release: LEAPS RTLS v0.16.4-a916a6
[000535.583 INF] sys: main main_ver=x02040001 cfg_ver=x01040000 batt=none board=LC14_B
[000535.584 INF] uwb: ch9 prf64 plen128 pac8 txcode9 rxcode9 baud6800 phrmodeext phrratestd sfdtypeieee4a sfdto129 stsmodeoff stslen64 pdoamodem0
[000535.585 INF] uwb: tx_pwr=x34/xEEEEEEEE sts:shr:phr:data=26.5:26.5:26.5:26.5[dB] cpl=FCC/ETSI pgcnt=245 temp=25
[000535.586 INF] uwb: lna=1 pa=0 rf1=1 rf2=0 xtaltrim=32 tx_delay=16436 rx_delay=16436
[000535.587 INF] uwb: panid=x1234 addr=xDECA7A20DFE04F2E
[000535.588 INF] mode: an (act,-)
[000535.599 INF] uwbmac: connected prof=5 (manual)
[000535.599 INF] uwbmac: bh disconnected
[000535.632 INF] cfg: sync=0 fwup=1 ble=1 leds=1 init=0 uab=1 bh=auto bh_stat=off cr=0 upd_rate_stat=30 label=ID4F2E
[000535.632 INF] enc: off
[000535.633 INF] ble: addr=C8:D9:F3:F1:7D:CE
leaps&gt;
</pre></div>
</div>
</div>
<input id="sd-tab-item-11" name="sd-tab-set-2" type="radio">
<label class="sd-tab-label" for="sd-tab-item-11">
タグ</label><div class="sd-tab-content docutils">
<ul class="simple">
<li><p>デフォルトの設定では、デバイスは <span class="red-text">TWR モード</span> になります。別のモードの場合は、<span class="red-text">tcs mode 0</span> コマンドを使用します。</p></li>
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

Copyright :  2016-2024 LEAPS
License   :  Please visit https://www.leapslabs.com/leaps-rtls-licee
Compiled  :  Nov  4 2024 12:30:29 (v0.16.4-a916a6

Help      :  ? or help

leaps&gt; urs 1 1
urs: ok
leaps&gt; si
[000248.294 INF] release: LEAPS RTLS v0.16.4-a916a6
[000248.294 INF] sys: main main_ver=x02040001 cfg_ver=x01040000 batt=none board=LC13_B
[000248.294 INF] uwb: ch9 prf64 plen128 pac8 txcode9 rxcode9 baud6800 phrmodeext phrratestd sfdtypeieee4a sfdto129 stsmodeoff stslen64 pdoamodem0
[000248.295 INF] uwb: tx_pwr=x34/xCDCDCDCD sts:shr:phr:data=21.7:21.7:21.7:21.7[dB] cpl=FCC/ETSI pgcnt=234 temp=25
[000248.295 INF] uwb: lna=1 pa=0 rf1=1 rf2=1 xtaltrim=13 tx_delay=16443 rx_delay=16443
[000248.295 INF] uwb: panid=x1234 addr=xDECA2B16DD209705
[000248.299 INF] mode: tn (act,tdoa,np,le)
[000248.314 INF] uwbmac: disconnected prof=5 (manual)
[000248.314 INF] uwbmac: bh disconnected
[000248.314 INF] cfg: sync=0 fwup=1 ble=1 leds=1 le=1 lp=0 uab=1 stat_det=1 (sens=2) mode=1 upd_rate_norm=1 upd_rate_stat=1 label=ID9705
[000248.342 INF] enc: off
[000248.342 INF] ble: addr=E0:2C:84:68:AD:16
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
<span class="p">[</span><span class="mf">000414.009</span> <span class="n">INF</span><span class="p">]</span> <span class="n">AN</span><span class="p">:</span> <span class="n">cnt</span><span class="o">=</span><span class="mi">4</span> <span class="n">seq</span><span class="o">=</span><span class="n">x03</span>
<span class="p">[</span><span class="mf">000414.009</span> <span class="n">INF</span><span class="p">]</span>     <span class="mi">0</span><span class="p">)</span> <span class="nb">id</span><span class="o">=</span><span class="mi">8</span><span class="n">EAA</span> <span class="n">seat</span><span class="o">=</span><span class="mi">0</span> <span class="n">clk_lvl</span><span class="o">=</span><span class="mi">0</span> <span class="n">seens</span><span class="o">=</span><span class="mi">0</span> <span class="n">rssi</span><span class="o">=-</span><span class="mi">127</span> <span class="n">cl</span><span class="o">=</span><span class="mi">00000039</span> <span class="n">nbr</span><span class="o">=</span><span class="mi">00000039</span> <span class="n">pos</span><span class="o">=</span><span class="mf">3.00</span><span class="p">:</span><span class="mf">3.00</span><span class="p">:</span><span class="mf">0.00</span>
<span class="p">[</span><span class="mf">000414.010</span> <span class="n">INF</span><span class="p">]</span>     <span class="mi">1</span><span class="p">)</span> <span class="nb">id</span><span class="o">=</span><span class="mi">4</span><span class="n">F2E</span> <span class="n">seat</span><span class="o">=</span><span class="mi">4</span> <span class="n">clk_lvl</span><span class="o">=</span><span class="mi">1</span> <span class="n">seens</span><span class="o">=</span><span class="mi">212</span> <span class="n">rssi</span><span class="o">=-</span><span class="mi">127</span> <span class="n">cl</span><span class="o">=</span><span class="mi">00000039</span> <span class="n">nbr</span><span class="o">=</span><span class="mi">00000000</span> <span class="n">pos</span><span class="o">=</span><span class="mf">0.00</span><span class="p">:</span><span class="mf">3.00</span><span class="p">:</span><span class="mf">0.00</span>
<span class="p">[</span><span class="mf">000414.011</span> <span class="n">INF</span><span class="p">]</span>     <span class="mi">2</span><span class="p">)</span> <span class="nb">id</span><span class="o">=</span><span class="mi">5886</span> <span class="n">seat</span><span class="o">=</span><span class="mi">5</span> <span class="n">clk_lvl</span><span class="o">=</span><span class="mi">1</span> <span class="n">seens</span><span class="o">=</span><span class="mi">178</span> <span class="n">rssi</span><span class="o">=-</span><span class="mi">127</span> <span class="n">cl</span><span class="o">=</span><span class="mi">00000039</span> <span class="n">nbr</span><span class="o">=</span><span class="mi">00000000</span> <span class="n">pos</span><span class="o">=</span><span class="mf">3.00</span><span class="p">:</span><span class="mf">0.00</span><span class="p">:</span><span class="mf">0.00</span>
<span class="p">[</span><span class="mf">000414.012</span> <span class="n">INF</span><span class="p">]</span>     <span class="mi">3</span><span class="p">)</span> <span class="nb">id</span><span class="o">=</span><span class="mi">468</span><span class="n">D</span> <span class="n">seat</span><span class="o">=</span><span class="mi">3</span> <span class="n">clk_lvl</span><span class="o">=</span><span class="mi">1</span> <span class="n">seens</span><span class="o">=</span><span class="mi">145</span> <span class="n">rssi</span><span class="o">=-</span><span class="mi">127</span> <span class="n">cl</span><span class="o">=</span><span class="mi">00000039</span> <span class="n">nbr</span><span class="o">=</span><span class="mi">00000000</span> <span class="n">pos</span><span class="o">=</span><span class="mf">0.00</span><span class="p">:</span><span class="mf">0.00</span><span class="p">:</span><span class="mf">0.00</span>
<span class="p">[</span><span class="mf">000414.012</span> <span class="n">INF</span><span class="p">]</span>
<span class="n">leaps</span><span class="o">&gt;</span>
</pre></div>
</div>
</div></blockquote>
</div></blockquote>
<ol class="arabic" start="12">
<li><p>すべての設定が完了した後。 <a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> を使用して、デバイスとその位置を視覚化できます。</p>
<a class="reference internal image-reference" href="../../../_images/twrrtlsanddatatelemetrydemo-advanced-01.jpeg"><img alt="../../../_images/twrrtlsanddatatelemetrydemo-advanced-01.jpeg" src="/docs-assets/ja/_images/twrrtlsanddatatelemetrydemo-advanced-01.jpeg" style="width: 32%;"></a>
<a class="reference internal image-reference" href="../../../_images/twrrtlsanddatatelemetrydemo-advanced-02.jpeg"><img alt="../../../_images/twrrtlsanddatatelemetrydemo-advanced-02.jpeg" src="/docs-assets/ja/_images/twrrtlsanddatatelemetrydemo-advanced-02.jpeg" style="width: 32%;"></a>
<a class="reference internal image-reference" href="../../../_images/twrrtlsanddatatelemetrydemo-advanced-03.jpeg"><img alt="../../../_images/twrrtlsanddatatelemetrydemo-advanced-03.jpeg" src="/docs-assets/ja/_images/twrrtlsanddatatelemetrydemo-advanced-03.jpeg" style="width: 32%;"></a>
</li>
</ol>
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
<p><strong>データ フロー</strong>: タグが点滅すると、アンカーは点滅を受信し、点滅の TX/RX タイムスタンプを LEAPS Gateway経由で LEAPS Serverーに送信します。</p>
<blockquote>
<div><a class="reference internal image-reference" href="../../../_images/uplink_tdoa_rtls_demo.png"><img alt="../../../_images/uplink_tdoa_rtls_demo.png" class="align-right" src="/docs-assets/ja/_images/uplink_tdoa_rtls_demo.png" style="width: 360.0px; height: 397.20000000000005px;"></a>
</div></blockquote>
<p><strong>インフラストラクチャのセットアップ</strong></p>
<blockquote>
<div><ol class="arabic simple">
<li><p>デバイス構成</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>上記と同様に、クイック スタートで LM を使用するか、アドバンストでシェルを使用してデバイスを設定します。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="2">
<li><p>Raspberry Pi のセットアップ</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>LEAPS-RPI-IMAGE を使用してすべての Raspberry Pi をインストールします。</p></li>
<li><p>対応する各アンカーは Raspberry Pi に接続するため、少なくとも 4 つの Raspberry Pi が必要です。</p></li>
<li><p>イメージには、 <code class="docutils literal notranslate"><span class="pre">LEAPS</span> <span class="pre">Gateway</span></code>、 <code class="docutils literal notranslate"><span class="pre">LEAPS</span> <span class="pre">Server</span></code>、 <code class="docutils literal notranslate"><span class="pre">LEAPS</span> <span class="pre">Center</span></code>、 <code class="docutils literal notranslate"><span class="pre">Mosquitto</span> <span class="pre">MQTT</span> <span class="pre">Broker</span></code> のセットアップと構成が含まれています。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="3">
<li><p>Raspberry Pi の接続</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>すべての Raspberry Pi をルーターに接続して、それらが同じ LAN 上にあることを確認します。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="4">
<li><p>LEAPS Serverのセットアップ</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">LEAPS</span> <span class="pre">Server</span></code> を実行する任意の Raspberry Pi を選択し、その IP アドレスを確認します。 IP アドレスを取得するには、ifconfig コマンドを使用します。</p></li>
</ul>
<img alt="../../../_images/uplinktdoartlsdemo-ip-address.png" class="align-center" src="/docs-assets/ja/_images/uplinktdoartlsdemo-ip-address.png">
</div></blockquote>
<ol class="arabic simple" start="5">
<li><p>構成を更新しています</p></li>
</ol>
<blockquote>
<div><ul>
<li><p>選択した Raspberry Pi の IP アドレスを使用して、すべての Raspberry Pi 上のすべての LEAPS Gatewayの <code class="docutils literal notranslate"><span class="pre">/usr/share/LEAPS-DOCKER-LINUX/leaps-gateway-hub/data/leaps-gateway.conf</span></code> 内の <code class="docutils literal notranslate"><span class="pre">leaps-server-host</span></code> 設定を更新します。</p>
<ul class="simple">
<li><p>たとえば:</p></li>
</ul>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">leaps</span><span class="o">-</span><span class="n">server</span><span class="o">-</span><span class="n">host</span> <span class="o">=</span> <span class="mf">192.168.1.8</span>
</pre></div>
</div>
</li>
</ul>
<img alt="../../../_images/uplinktdoartlsdemo-leaps-gateway.png" class="align-center" src="/docs-assets/ja/_images/uplinktdoartlsdemo-leaps-gateway.png">
<img alt="../../../_images/uplinktdoartlsdemo-leaps-gateway.png" class="align-center" src="/docs-assets/ja/_images/uplinktdoartlsdemo-leaps-gateway.png">
<ul class="simple">
<li><p>設定を保存し、次のコマンドで <code class="docutils literal notranslate"><span class="pre">LEAPS</span> <span class="pre">Gateway</span></code> を再起動します：</p></li>
</ul>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">sudo</span> <span class="n">docker</span> <span class="n">restart</span> <span class="n">leaps_gateway</span>
</pre></div>
</div>
<ul class="simple">
<li><p>次に、次のコマンドを使用して <code class="docutils literal notranslate"><span class="pre">LEAPS</span> <span class="pre">Server</span></code> を再起動します：</p></li>
</ul>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">sudo</span> <span class="n">service</span> <span class="n">leaps</span><span class="o">-</span><span class="n">server</span> <span class="n">restart</span>
</pre></div>
</div>
</div></blockquote>
<ol class="arabic simple" start="6">
<li><p>システムの監視</p></li>
</ol>
<blockquote>
<div><ul>
<li><p>ゲートウェイの準備ができたら、以下を使用してシステムのステータスを監視します。</p></li>
<li><p>たとえば:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">mosquitto_sub</span> <span class="o">-</span><span class="n">h</span> <span class="mf">192.168.1.8</span> <span class="o">-</span><span class="n">p</span> <span class="mi">1883</span> <span class="o">-</span><span class="n">t</span> <span class="s1">'#'</span> <span class="o">-</span><span class="n">v</span>
</pre></div>
</div>
</li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="7">
<li><p>LEAPS Centerの構成</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>例: Web ブラウザを開いて: <code class="docutils literal notranslate"><span class="pre">192.168.1.8/2</span></code> に移動します</p></li>
<li><p>これには、Raspberry Pi 上で直接アクセスするか、パスワード <code class="docutils literal notranslate"><span class="pre">Leaps1234</span></code> を使用して Raspberry Pi によってブロードキャストされる LEAPS-AP ネットワークに接続されている PC 上でアクセスできます。</p></li>
<li><p>LAN ネットワーク上の場合は、別のコンピュータの Web ブラウザを使用して Raspberry Pi の IP アドレスにアクセスすることもできます。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="8">
<li><p>ネットワーク構成</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">LEAPS</span> <span class="pre">Center</span></code> で、接続しているゲートウェイ ボードのネットワーク ID と一致するようにネットワーク設定を構成します。</p></li>
</ul>
<img alt="../../../_images/uplinktdoartlsdemo-leaps-center.png" class="align-center" src="/docs-assets/ja/_images/uplinktdoartlsdemo-leaps-center.png">
</div></blockquote>
<p>これで、システムは正常にセットアップされ、構成されました。楽しく使ってください！</p>
</div></blockquote>
<div class="admonition note">
<p class="admonition-title">注釈</p>
<ul class="simple">
<li><p>このデモの威力をさらに詳しく調べるには、ソフトウェア インフラストラクチャを参照してください。私たちのサポートには、<a class="reference internal" href="/docs/ja/udk/udk-start/infrastructure-docker#leaps-docker"><span class="std std-ref">LEAPS ドッカー</span></a>、<a class="reference internal" href="/docs/ja/udk/udk-start/infrastructure-vmware#leaps-vmware"><span class="std std-ref">LEAPS VMWare</span></a>、および <a class="reference internal" href="/docs/ja/udk/udk-start/infrastructure-rpi#leaps-raspberrypi"><span class="std std-ref">LEAPS Raspberry Pi</span></a> が含まれます。</p></li>
<li><p>弊社製品に関するご意見やご質問については、<a class="reference external" href="https://forum.leapslabs.com">LEAPS フォーラム</a> にアクセスすることをお勧めします。</p></li>
<li><p>既知の制限と問題リストの詳細については、セクション <a class="reference internal" href="/docs/ja/udk/release#udk-releases"><span class="std std-ref">リリース</span></a> を参照してください。</p></li>
</ul>
</div>
</div>


           </div>
