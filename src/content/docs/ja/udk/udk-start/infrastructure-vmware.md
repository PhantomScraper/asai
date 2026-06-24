---
title: "LEAPS VMWare"
lang: ja
slug: "udk/udk-start/infrastructure-vmware"
section: "udk"
sourceUrl: "https://docs.leapslabs.com/ja/udk/udk-start/infrastructure-vmware/"
order: 39
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-vmware">
<span id="id1"></span><h1>LEAPS VMWare</h1>
<blockquote>
<div><p>このページには以下が含まれます:</p>
<blockquote>
<div><ul class="simple">
<li><p>LEAPS VMWare パッケージ。</p></li>
<li><p>システム要件に関する情報。</p></li>
<li><p>LEAPS VMWare のインストール方法に関する説明。</p></li>
</ul>
</div></blockquote>
</div></blockquote>
<p>インストールは迅速かつ簡単で、一度行うだけで済みます。</p>
<p id="uivmware"><strong>システム要件</strong></p>
<blockquote>
<div><ul class="simple">
<li><p>デスクトップデバイス。</p></li>
<li><p><em>推奨: UDK のセット (少なくとも 5 つのデバイス) を検証します。</em></p></li>
<li><p><em>推奨: デバイスに電力を供給するためのバッテリーまたは USB-C ケーブル。</em></p></li>
<li><p><em>推奨:</em> <a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> <em>デバイスを構成します。</em></p></li>
</ul>
</div></blockquote>
<p><strong>セットアップ手順</strong></p>
<ol class="arabic simple">
<li><p>ダウンロードとインストールVMware Player または VMware Workstation。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>次のリンクにアクセスして、必要なソフトウェアをダウンロードします。</p>
<ul>
<li><p><a class="reference external" href="https://www.vmware.com/uk/products/workstation-player.html">VMware Workstation Player</a>。</p></li>
<li><p><a class="reference external" href="https://www.vmware.com/products/workstation-pro/workstation-pro-evaluation.html">VMware Workstation Pro</a>。</p></li>
</ul>
</li>
<li><p>オペレーティング システムと互換性のあるバージョンを選択し、表示されるインストール手順に従ってください。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="2">
<li><p>LEAPS VMWare をダウンロードします。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>LEAPS VMWare: <a class="reference external" href="https://drive.google.com/file/d/1By5GRLJCnKrMETvIk7INXXEKKhFTtli4/view?usp=drive_link">LEAPS-VMM-IMAGE-v1.1.0.zip</a>.</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="3">
<li><p>VMWare アーカイブを抽出します。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>WinZip や 7-Zip などのプログラムを使用して、ダウンロードした LEAPS VMWare zip ファイルを解凍します。</p></li>
</ul>
</div></blockquote>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/extract_the_vmware_archive.png"><img alt="../../../_images/extract_the_vmware_archive.png" src="/docs-assets/ja/_images/extract_the_vmware_archive.png" style="width: 463.0px; height: 262.0px;"></a>
</div>
<ol class="arabic simple" start="4">
<li><p>アプライアンスをインポートします。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>抽出されたファイルに移動し、.ova ファイルを見つけます。</p></li>
<li><p>VMware アプリケーションを開き、<span class="red-text">File</span> » <span class="red-text">Import Appliance</span> に移動します。</p></li>
<li><p>.ova ファイルを参照し、開くをクリックします。</p></li>
<li><p>仮想マシンの名前を入力し、仮想マシン ファイルのディレクトリを入力するか参照して、[インポート] をクリックします。</p></li>
<li><p><span class="red-text">インポート</span> ボタンをクリックして、インポート プロセスを開始します。インポートが失敗した場合は、<code class="docutils literal notranslate"><span class="pre">再試行</span></code> をクリックして再試行するか、<code class="docutils literal notranslate"><span class="pre">キャンセル</span></code> をクリックしてインポートをキャンセルします。</p></li>
</ul>
</div></blockquote>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/import_the_appliance.png"><img alt="../../../_images/import_the_appliance.png" src="/docs-assets/ja/_images/import_the_appliance.png" style="width: 697.9px; height: 477.4px;"></a>
</div>
<ol class="arabic simple" start="5">
<li><p>VMWare を起動します。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>インポートが完了したら、インポートされた仮想マシンを選択し、red:<cite>開始</cite> ボタンをクリックして起動します。</p></li>
</ul>
</div></blockquote>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/start_the_vmware.png"><img alt="../../../_images/start_the_vmware.png" src="/docs-assets/ja/_images/start_the_vmware.png" style="width: 760.9px; height: 476.7px;"></a>
</div>
<ol class="arabic simple" start="6">
<li><p>システムが起動するまで待ちます。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>システム全体の起動が完了するまで数分間お待ちください。</p></li>
<li><p>デフォルトでは、アカウントは <code class="docutils literal notranslate"><span class="pre">leaps</span></code> 、パスワードは <code class="docutils literal notranslate"><span class="pre">leaps</span></code> です。</p></li>
</ul>
</div></blockquote>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/windows_vmware.png"><img alt="../../../_images/windows_vmware.png" src="/docs-assets/ja/_images/windows_vmware.png" style="width: 600.5999999999999px; height: 487.2px;"></a>
</div>
<ol class="arabic simple" start="7">
<li><p><a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> を使用してネットワークを準備します。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>デモを設定します: <a class="reference internal" href="/docs/ja/udk/udk-start/twr-rtls-and-data-telemetry-demo#twr-rtls-and-data-telemetry-demo"><span class="std std-ref">TWR RTLS およびデータ遠隔測定デモ</span></a> または <a class="reference internal" href="/docs/ja/udk/udk-start/uplink-tdoa-rtls-demo#uplink-tdoa-rtls-demo"><span class="std std-ref">アップリンク TDoA RTLS デモ</span></a>。</p></li>
<li><p>デフォルトでは、ネットワーク ID は <code class="docutils literal notranslate"><span class="pre">0x1234</span></code> になります。</p></li>
<li><p>この例では、ID <code class="docutils literal notranslate"><span class="pre">0x83A2</span></code> のゲートウェイ ボードを接続する必要があります。</p></li>
</ul>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/vmware_network_demo01.jpg"><img alt="../../../_images/vmware_network_demo01.jpg" src="/docs-assets/ja/_images/vmware_network_demo01.jpg" style="width: 360.0px; height: 800.0px;"></a>
</div>
</div></blockquote>
<ol class="arabic simple" start="8">
<li><p>USB-C データ ケーブルを使用して、ゲートウェイ ボードを PC に接続します。</p></li>
</ol>
<blockquote>
<div><ul>
<li><p>USB-C データ ケーブルを PC の <a class="reference internal" href="/docs/ja/udk/udk-start/device-hw-interfaces#hardware-interface"><span class="std std-ref">USB-C データ ポート 1</span></a> に差し込みます。安定した接続を確保してください。</p>
<img alt="../../../_images/leaps-connect-usb-port1.gif" class="align-center" src="/docs-assets/ja/_images/leaps-connect-usb-port1.gif">
</li>
<li><p>実行中の VMWare で、<span class="red-text">仮想マシン</span> » <span class="red-text">リムーバブル デバイス</span> に移動します。</p></li>
<li><p>ゲートウェイ モードで正常に接続された場合は、確認としてビープ音が 2 回聞こえます。</p></li>
</ul>
</div></blockquote>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/connect_the_gateway_board.png"><img alt="../../../_images/connect_the_gateway_board.png" src="/docs-assets/ja/_images/connect_the_gateway_board.png" style="width: 718.1999999999999px; height: 488.59999999999997px;"></a>
</div>
<ol class="arabic simple" start="9">
<li><p>システムステータスを確認してください。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>VMWare 内でターミナルまたはコマンド プロンプトを開きます。</p></li>
<li><p><span class="red-text">mosquitto_sub</span> コマンドを使用して、システムのステータスを確認します。このコマンドは Mosquitto MQTT ブローカーに接続し、受信したすべてのメッセージを表示します。</p></li>
</ul>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">mosquitto_sub</span> <span class="o">-</span><span class="n">p</span> <span class="mi">1883</span> <span class="o">-</span><span class="n">d</span> <span class="o">-</span><span class="n">v</span> <span class="o">-</span><span class="n">t</span> <span class="s1">'#'</span>
</pre></div>
</div>
</div></blockquote>
<ol class="arabic simple" start="10">
<li><p>IP アドレスを確認してください。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>ステップ 6 の IP アドレス。表示されていない場合。コマンド <code class="docutils literal notranslate"><span class="pre">sudo</span> <span class="pre">ifconfig</span></code> を使用して確認してください。</p>
<ul>
<li><p>この例では、<code class="docutils literal notranslate"><span class="pre">192.168.26.151</span></code> です。</p></li>
</ul>
</li>
</ul>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/windows_vmware_ip_address.png"><img alt="../../../_images/windows_vmware_ip_address.png" src="/docs-assets/ja/_images/windows_vmware_ip_address.png" style="width: 600.5999999999999px; height: 487.2px;"></a>
</div>
<ul>
<li><p>IP アドレスが確認できない場合は、次のように設定を変更することもできます。</p>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/vmware-set-nat.png"><img alt="../../../_images/vmware-set-nat.png" src="/docs-assets/ja/_images/vmware-set-nat.png" style="width: 525.6999999999999px; height: 510.29999999999995px;"></a>
</div>
<ul class="simple">
<li><p>次に、コマンド <code class="docutils literal notranslate"><span class="pre">sudo</span> <span class="pre">ifconfig</span></code> を使用して確認します。この例では <code class="docutils literal notranslate"><span class="pre">192.168.146.145</span></code> です。</p></li>
</ul>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/vmware-sudo-ipconfig.png"><img alt="../../../_images/vmware-sudo-ipconfig.png" src="/docs-assets/ja/_images/vmware-sudo-ipconfig.png" style="width: 557.1999999999999px; height: 457.79999999999995px;"></a>
</div>
</li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="10">
<li><p><a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> にアクセスします。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>コンピュータの Web ブラウザを使用します。</p></li>
<li><p><a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> にアクセスするための LEAPS VMware の IP アドレスを入力します。</p></li>
</ul>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/vmware_leaps_center_login.png"><img alt="../../../_images/vmware_leaps_center_login.png" src="/docs-assets/ja/_images/vmware_leaps_center_login.png" style="width: 762.4000000000001px; height: 370.8px;"></a>
</div>
</div></blockquote>
<ol class="arabic simple" start="11">
<li><p><a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> にログインします。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>ユーザー名 <span class="red-text">admin</span>、パスワード <span class="red-text">admin</span> を使用してログインします。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="12">
<li><p><a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> 上のネットワーク。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p><a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> のネットワーク設定を確認して、ネットワーク ID と一致するようにしてください。</p></li>
</ul>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/vmware_leaps_center_network.png"><img alt="../../../_images/vmware_leaps_center_network.png" src="/docs-assets/ja/_images/vmware_leaps_center_network.png" style="width: 764.4000000000001px; height: 373.20000000000005px;"></a>
</div>
<ul class="simple">
<li><p>アプリケーションを使用してノードとネットワークを構成および視覚化する方法の詳細については、<a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> および <a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> を参照してください。</p></li>
</ul>
</div></blockquote>
<p>これで、システムは正常にセットアップされ、構成されました。楽しく使ってください！</p>
</div>


           </div>
