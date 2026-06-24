---
title: "インフラレス近接デモ"
lang: ja
slug: "udk/udk-start/infrastructure-less-proximity-demo"
section: "udk"
sourceUrl: "https://docs.leapslabs.com/ja/udk/udk-start/infrastructure-less-proximity-demo/"
order: 108
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="infrastructure-less-proximity-demo">
<span id="anchor-ilp"></span><h1>インフラレス近接デモ</h1>
<a class="reference internal image-reference" href="../../../_images/infrastructure-less_proximity_demo.png"><img alt="../../../_images/infrastructure-less_proximity_demo.png" class="align-right" src="/docs-assets/ja/_images/infrastructure-less_proximity_demo.png" style="width: 180.0px; height: 204.9px;"></a>
<p><strong>セットアップの準備</strong></p>
<ol class="arabic simple">
<li><p><a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> アプリケーションがインストールされました。</p></li>
<li><p>少なくとも 2 つの LC14 または LC13 デバイス。</p></li>
<li><p>デバイスに電力を供給するためのバッテリーまたは USB-C ケーブル。</p></li>
<li><p><em>オプション: Putty、Teraterm、minicom、またはコンピュータにインストールされているお気に入りのターミナル アプリケーション。</em></p></li>
</ol>
<p><strong>セットアップ時間:</strong> 2 分未満</p>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-0" name="sd-tab-set-0" type="radio">
<label class="sd-tab-label" for="sd-tab-item-0">
クイックスタート</label><div class="sd-tab-content docutils">
<p><strong>概要</strong></p>
<p>このデモは、<span class="red-text">Two Way Ranging (TWR)</span> 測定技術に基づいた、インフラストラクチャを使用しないノード間の近接検出を示します。ノードが近接している場合、すべてのノードによってアラームがトリガーされます。アラームは LED、ハプティック モーター、またはブザーを使用し、しきい値は設定可能です。</p>
<p><strong>典型的なアプリケーション</strong>: 衝突回避、社会的距離、群の調整。</p>
<p><strong>セットアップ手順</strong></p>
<ol class="arabic simple">
<li><p>デバイスの電源を <span class="red-text">ON</span> にします。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>デバイスは、Bluetooth を使用して周囲のデバイスを検出し、UWB を使用して検出されたデバイスまでの距離を測定する独立したタグとして機能します。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="2">
<li><p><a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> のデモ セレクターを使用して設定します。</p></li>
</ol>
<blockquote>
<div><p>2.1。 LEAPS Manager を開き、メイン ページから <span class="red-text">Demo Selector</span> を選択します。</p>
<p>2.2。 <span class="red-text">インフラストラクチャのない近接性</span> を選択します。</p>
<p>2.3。 Bluetooth 経由で検出されたデバイスのリストがリストに表示されます。必要に応じて、下にスワイプしてリストを更新します。</p>
<p>2.4。デモに使用するデバイスを選択します。上側の``ノード``は、デモに必要なデバイスの数を示します。</p>
<p>2.5。 <span class="red-text">SAVE</span> を押して、デバイスを LEAPS RTLS モード、タグメッシュ ネットワーク プロファイルに設定します。</p>
<p>2.6。デバイスが起動すると、<span class="red-text">赤い LED</span> が点滅することを目視で確認してください。</p>
<img alt="../../../_images/infrastructure-less-proximity-demo.gif" class="align-center" src="/docs-assets/ja/_images/infrastructure-less-proximity-demo.gif">
</div></blockquote>
<ol class="arabic simple" start="3">
<li><p>デバイスは <a class="reference internal" href="#anchor-ilp"><span class="std std-ref">インフラレス近接デモ</span></a> 用に構成されています。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>デフォルトでは、デバイスが互いに 2.5 メートル以内に近づくと、アラームが作動します (赤色の LED とブザーで示されます)。デバイスが近づくにつれて、アラームの強度が増加します。</p></li>
<li><p>最初に、デバイスは低強度のビープ音を発し、赤色 LED が点滅します。上(<a class="reference internal" href="/docs/ja/udk/udk-start/device-hw-interfaces#uihwinterfaces"><span class="std std-ref">ボタン B</span></a>)下(<a class="reference internal" href="/docs/ja/udk/udk-start/device-hw-interfaces#uihwinterfaces"><span class="std std-ref">ボタン A</span></a>)ボタンでビープ音の音量を調整でき、バイブレーションも有効になります。</p></li>
<li><p>以下に概説するデモでは、デバイスには 2 つの近接しきい値があります。最初のしきい値は 0.2 メートルに設定され、2 番目のしきい値は 0.5 メートルに設定されています。</p></li>
</ul>
<img alt="../../../_images/infrastructure-less-proximity-demo-01.gif" class="align-center" src="/docs-assets/ja/_images/infrastructure-less-proximity-demo-01.gif">
</div></blockquote>
<p>アプリケーションを使用してノードとネットワークを構成および視覚化する方法の詳細については、<a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> を参照してください。</p>
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
<li><p>Putty、Teraterm、Minicom などの任意のターミナル アプリケーション、またはお気に入りのターミナル アプリケーションを使用してシリアル ポートに接続します。ボーレートを <span class="red-text">115200</span> に設定する必要があります。</p></li>
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
<li><p>次の手順に従って各デバイスを構成します。</p></li>
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
<li><p>コマンド <span class="red-text">nps 4</span> を使用して、各デバイスの <span class="red-text">プロファイル 4 (タグ メッシュ プロキシミティをサポート)</span> を設定します。</p></li>
</ol>
<blockquote>
<div><div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ leaps&gt; nps 4
nps: ok
</pre></div>
</div>
</div></blockquote>
<ol class="loweralpha simple" start="3">
<li><p><span class="red-text">nis</span> コマンドを使用して、ネットワーク内のすべてのデバイスを設定します。</p></li>
</ol>
<blockquote>
<div><div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ leaps&gt; nis 0x1234
nis: ok
</pre></div>
</div>
</div></blockquote>
<ol class="loweralpha simple" start="4">
<li><p>コマンド <span class="red-text">nmt</span> を使用して、タグ モードを更新します。</p></li>
</ol>
<blockquote>
<div><div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ leaps&gt; nmt
</pre></div>
</div>
</div></blockquote>
<p><em>(次に、デバイスが正常に設定されるまで監視して待ちます。その後、Enter キーを 2 回押して、コマンド ライン制御システムに再度アクセスします。)</em></p>
<ol class="loweralpha simple" start="5">
<li><p><span class="red-text">si</span> コマンドを使用して、モード、プロファイル、ネットワークなどの構成を確認します。</p></li>
</ol>
<blockquote>
<div><div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">leaps</span><span class="o">&gt;</span> <span class="n">si</span>
<span class="p">[</span><span class="mf">000028.754</span> <span class="n">INF</span><span class="p">]</span> <span class="n">release</span><span class="p">:</span> <span class="n">LEAPS</span> <span class="n">RTLS</span> <span class="n">v0</span><span class="mf">.15.0</span><span class="o">-</span><span class="n">ab84fb</span>
<span class="p">[</span><span class="mf">000028.754</span> <span class="n">INF</span><span class="p">]</span> <span class="n">sys</span><span class="p">:</span> <span class="n">main</span> <span class="n">main_ver</span><span class="o">=</span><span class="n">x02000001</span> <span class="n">cfg_ver</span><span class="o">=</span><span class="n">x01040000</span> <span class="n">batt</span><span class="o">=</span><span class="n">none</span> <span class="n">board</span><span class="o">=</span><span class="n">LC14_B</span>
<span class="p">[</span><span class="mf">000028.754</span> <span class="n">INF</span><span class="p">]</span> <span class="n">uwb</span><span class="p">:</span> <span class="n">ch9</span> <span class="n">prf64</span> <span class="n">plen128</span> <span class="n">pac8</span> <span class="n">txcode9</span> <span class="n">rxcode9</span> <span class="n">baud6800</span> <span class="n">phrmodeext</span> <span class="n">phrratestd</span> <span class="n">sfdtypeieee4a</span> <span class="n">sfdto10</span>
<span class="p">[</span><span class="mf">000028.754</span> <span class="n">INF</span><span class="p">]</span> <span class="n">uwb</span><span class="p">:</span> <span class="n">tx_pwr</span><span class="o">=</span><span class="n">x34</span><span class="o">/</span><span class="n">xC6C6C6C6</span> <span class="n">sts</span><span class="p">:</span><span class="n">shr</span><span class="p">:</span><span class="n">phr</span><span class="p">:</span><span class="n">data</span><span class="o">=</span><span class="mf">22.6</span><span class="p">:</span><span class="mf">22.6</span><span class="p">:</span><span class="mf">22.6</span><span class="p">:</span><span class="mf">22.6</span><span class="p">[</span><span class="n">dB</span><span class="p">]</span> <span class="n">cpl</span><span class="o">=</span><span class="n">FCC</span><span class="o">/</span><span class="n">ETSI</span> <span class="n">pgcnt</span><span class="o">=</span><span class="mi">236</span> <span class="n">temp</span><span class="o">=</span><span class="mi">5</span>
<span class="p">[</span><span class="mf">000028.755</span> <span class="n">INF</span><span class="p">]</span> <span class="n">uwb</span><span class="p">:</span> <span class="n">lna</span><span class="o">=</span><span class="mi">1</span> <span class="n">pa</span><span class="o">=</span><span class="mi">0</span> <span class="n">rf1</span><span class="o">=</span><span class="mi">1</span> <span class="n">rf2</span><span class="o">=</span><span class="mi">0</span> <span class="n">xtaltrim</span><span class="o">=</span><span class="mi">32</span> <span class="n">tx_delay</span><span class="o">=</span><span class="mi">16431</span> <span class="n">rx_delay</span><span class="o">=</span><span class="mi">16431</span>
<span class="p">[</span><span class="mf">000028.755</span> <span class="n">INF</span><span class="p">]</span> <span class="n">uwb</span><span class="p">:</span> <span class="n">panid</span><span class="o">=</span><span class="n">x1234</span> <span class="n">addr</span><span class="o">=</span><span class="n">xDECAED5BC8B1468D</span>
<span class="p">[</span><span class="mf">000028.758</span> <span class="n">INF</span><span class="p">]</span> <span class="n">mode</span><span class="p">:</span> <span class="n">tn</span> <span class="p">(</span><span class="n">act</span><span class="p">,</span><span class="n">twr</span><span class="p">,</span><span class="n">np</span><span class="p">,</span><span class="n">le</span><span class="p">)</span>
<span class="p">[</span><span class="mf">000028.774</span> <span class="n">INF</span><span class="p">]</span> <span class="n">uwbmac</span><span class="p">:</span> <span class="n">connected</span> <span class="n">prof</span><span class="o">=</span><span class="mi">4</span> <span class="p">(</span><span class="n">manual</span><span class="p">)</span>
<span class="p">[</span><span class="mf">000028.774</span> <span class="n">INF</span><span class="p">]</span> <span class="n">uwbmac</span><span class="p">:</span> <span class="n">bh</span> <span class="n">disconnected</span>
<span class="p">[</span><span class="mf">000028.774</span> <span class="n">INF</span><span class="p">]</span> <span class="n">cfg</span><span class="p">:</span> <span class="n">sync</span><span class="o">=</span><span class="mi">0</span> <span class="n">fwup</span><span class="o">=</span><span class="mi">1</span> <span class="n">ble</span><span class="o">=</span><span class="mi">1</span> <span class="n">leds</span><span class="o">=</span><span class="mi">1</span> <span class="n">le</span><span class="o">=</span><span class="mi">1</span> <span class="n">lp</span><span class="o">=</span><span class="mi">0</span> <span class="n">uab</span><span class="o">=</span><span class="mi">1</span> <span class="n">stat_det</span><span class="o">=</span><span class="mi">1</span> <span class="p">(</span><span class="n">sens</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span> <span class="n">mode</span><span class="o">=</span><span class="mi">0</span> <span class="n">upd_rate_norm</span><span class="o">=</span><span class="mi">1</span> <span class="n">upd_D</span>
<span class="p">[</span><span class="mf">000028.802</span> <span class="n">INF</span><span class="p">]</span> <span class="n">enc</span><span class="p">:</span> <span class="n">off</span>
<span class="p">[</span><span class="mf">000028.802</span> <span class="n">INF</span><span class="p">]</span> <span class="n">ble</span><span class="p">:</span> <span class="n">addr</span><span class="o">=</span><span class="n">F3</span><span class="p">:</span><span class="n">D9</span><span class="p">:</span><span class="mi">66</span><span class="p">:</span><span class="mi">75</span><span class="p">:</span><span class="mi">93</span><span class="p">:</span><span class="n">EB</span>
<span class="n">leaps</span><span class="o">&gt;</span>
</pre></div>
</div>
</div></blockquote>
<ul class="simple">
<li><p><code class="docutils literal notranslate"><span class="pre">mode:</span> <span class="pre">tn</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">panid=x1234</span></code></p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">prof=4</span></code></p></li>
</ul>
<ol class="loweralpha simple" start="6">
<li><p>デバイスの起動時に <span class="red-text">赤い LED</span> が点滅することを目視で確認してください。</p></li>
</ol>
</div></blockquote>
<div class="admonition note">
<p class="admonition-title">注釈</p>
<p>この例では、<strong>2 つのタグ</strong> を構成します。</p>
</div>
<ol class="arabic simple" start="5">
<li><p>デバイスを構成した後、BLE 経由ですべてのデバイスをスキャンします。デバイスが許容距離内にある場合、自動的に UWB が再アクティブ化され、互いの距離が測定されます。</p></li>
</ol>
<blockquote>
<div><p>すべてのデバイスを表示するには、<span class="red-text">ln</span> コマンドを使用します。これはすべての UDK デバイスで使用できます。</p>
<div class="sd-tab-set docutils">
<input checked="checked" id="sd-tab-item-3" name="sd-tab-set-1" type="radio">
<label class="sd-tab-label" for="sd-tab-item-3">
タグ1</label><div class="sd-tab-content docutils">
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ leaps&gt; ln
[000005.713 INF] TN: cnt=2 size=100
[000005.713 INF]   0) id=468D dist=0.40,xDD
[000005.713 INF]   1) id=4F2E dist=0.00,xBD
[000005.713 INF]
</pre></div>
</div>
</div>
<input id="sd-tab-item-4" name="sd-tab-set-1" type="radio">
<label class="sd-tab-label" for="sd-tab-item-4">
タグ2</label><div class="sd-tab-content docutils">
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ leaps&gt; ln
[000033.319 INF] TN: cnt=2 size=100
[000033.319 INF]   0) id=468D dist=0.00,x00
[000033.320 INF]   1) id=4F2E dist=0.44,x66
[000033.320 INF]
</pre></div>
</div>
</div>
</div>
</div></blockquote>
<ol class="arabic simple" start="6">
<li><p><a class="reference internal" href="#anchor-ilp"><span class="std std-ref">インフラレス近接デモ</span></a> 内。</p></li>
</ol>
<blockquote>
<div><ul>
<li><p>デフォルトでは、デバイスが互いに 2.5 メートル以内に近づくと、アラームが作動します (赤色の LED とブザーで示されます)。デバイスが近づくにつれて、アラームの強度が増加します。</p></li>
<li><p>最初に、デバイスは低強度のビープ音を発し、赤色 LED が点滅します。上(<a class="reference internal" href="/docs/ja/udk/udk-start/device-hw-interfaces#uihwinterfaces"><span class="std std-ref">ボタン B</span></a>)下(<a class="reference internal" href="/docs/ja/udk/udk-start/device-hw-interfaces#uihwinterfaces"><span class="std std-ref">ボタン A</span></a>)ボタンでビープ音の音量を調整でき、バイブレーションも有効になります。</p></li>
<li><p>ユーザーは、<span class="red-text">dacg</span> コマンドと <span class="red-text">dacs</span> コマンドの 2 つのコマンドを使用して、この距離を表示および構成できます。</p>
<p>たとえば、0.2 メートルと 0.5 メートルの 2 つのしきい値を表示および設定します。次のコマンドを実行します。</p>
<blockquote>
<div><ul class="simple">
<li><p>表示するには:</p></li>
</ul>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ leaps&gt; dacg
dacg: thold_1=200 thold_2=500 mincon=2 minnocon=2 opt=7
</pre></div>
</div>
<ul class="simple">
<li><p>設定するには:</p></li>
</ul>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ leaps&gt; dacs 200 500 2 2 7
dacs: ok
</pre></div>
</div>
</div></blockquote>
<p>以下の GIF 画像では、デバイスはしきい値 1 が 0.2 メートル、しきい値 2 が 0.5 メートルで構成されています。</p>
<img alt="../../../_images/infrastructure-less-proximity-demo-01.gif" class="align-center" src="/docs-assets/ja/_images/infrastructure-less-proximity-demo-01.gif">
</li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="7">
<li><p>設定後、タグのシェル コンソールを開いて、<span class="red-text">les</span> コマンドを使用してタグの位置を表示できます。</p></li>
</ol>
<blockquote>
<div><div class="highlight-default notranslate"><div class="highlight"><pre><span></span>$ leaps&gt; les
  leaps&gt; POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.54
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.57
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.58
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.59
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.51
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.47
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.43
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.40
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.35
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.32
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.31
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.29
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.27
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.22
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.19
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.16
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.14
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.12
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.09
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.08
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.05
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.09
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.11
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.13
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.15
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.17
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.19
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.21
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.23
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.42
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.51
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.56
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.60
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.62
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.64
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.67
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.69
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.71
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.73
  POS[NaN,NaN,Nan,0] 4F2E[0.00,0.00,0.00,100]=0.73
</pre></div>
</div>
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
<div class="admonition caution">
<p class="admonition-title">注意</p>
<p><strong>Related to Profile 4 (support Tag Mesh Proximity)</strong></p>
<ul class="simple">
<li><p>デバイスがアンカー モードまたはイニシエーター モードの場合、ユーザーはプロファイル 4 (タグ メッシュ プロキシミティをサポート) に切り替えることはできません。</p></li>
<li><p>設定された更新レートの値は x1 以内に制限する必要があります。 x10。</p></li>
</ul>
</div>
<div class="admonition note">
<p class="admonition-title">注釈</p>
<ul class="simple">
<li><p>距離のしきい値は API 経由で構成できます。</p></li>
<li><p>弊社製品に関するご意見やご質問については、<a class="reference external" href="https://forum.leapslabs.com">LEAPS フォーラム</a> にアクセスすることをお勧めします。</p></li>
<li><p>既知の制限と問題リストの詳細については、セクション <a class="reference internal" href="/docs/ja/udk/release#udk-releases"><span class="std std-ref">リリース</span></a> を参照してください。</p></li>
</ul>
</div>
</div>


           </div>
