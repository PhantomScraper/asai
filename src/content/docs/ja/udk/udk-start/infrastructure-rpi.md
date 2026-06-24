---
title: "LEAPS Raspberry Pi"
lang: ja
slug: "udk/udk-start/infrastructure-rpi"
section: "udk"
sourceUrl: "https://docs.leapslabs.com/ja/udk/udk-start/infrastructure-rpi/"
order: 41
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="leaps-raspberry-pi">
<span id="leaps-raspberrypi"></span><h1>LEAPS Raspberry Pi</h1>
<p>このページには以下が含まれます:</p>
<blockquote>
<div><ul class="simple">
<li><p>LEAPS Raspberry Pi パッケージ。</p></li>
<li><p>システム要件に関する情報。</p></li>
<li><p>LEAPS Raspberry Pi のインストール方法に関する説明。</p></li>
</ul>
</div></blockquote>
<p>インストールは迅速かつ簡単で、一度行うだけで済みます。</p>
<p id="uiraspberrypi"><span class="red-text">開始する前に: フォーマット中にすべてのデータが永久に上書きされるため、保存しておきたい重要なファイルは必ず SD カードからバックアップしてください。</span></p>
<p><strong>システム要件</strong></p>
<blockquote>
<div><ul class="simple">
<li><p>Raspberry Pi 3B 以降。</p></li>
<li><p><em>推奨: UDK のセット (少なくとも 5 つのデバイス) を検証します。</em></p></li>
<li><p><em>推奨: デバイスに電力を供給するためのバッテリーまたは USB-C ケーブル。</em></p></li>
<li><p><em>推奨:</em> <a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> <em>デバイスを構成します。</em></p></li>
</ul>
</div></blockquote>
<p><strong>セットアップ手順</strong></p>
<ol class="arabic simple">
<li><p>LEAPS Raspberry Pi イメージをダウンロードします。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>LEAPS Docker: <a class="reference external" href="https://drive.google.com/file/d/1VmdslvrcuqN7vf6ppKKLfxMA2PENuYtT/view?usp=drive_link">LEAPS-RPI-IMAGE-v1.1.0.zip</a>.</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="2">
<li><p>LEAPS Raspberry Pi アーカイブを抽出します。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>WinZip や 7-Zip などのプログラムを使用して、ダウンロードした LEAPS Raspberry Pi の zip ファイルを抽出します。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="3">
<li><p>Raspberry Pi Imagerを起動しています。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>オペレーティング システムがインストーラーをブロックしようとしている可能性があります。</p></li>
<li><p><em>Windows の場合: 警告メッセージが表示された場合は、</em> <span class="red-text">詳細情報</span> <em>および</em> <span class="red-text">とにかく実行</span> をクリックします。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="4">
<li><p>LEAPS Raspberry Pi イメージをインストールしています。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>SD カードをコンピューターまたはラップトップの SD カード スロットに挿入します。</p></li>
<li><p>Raspberry Pi Imagerを開きます。</p></li>
</ul>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/raspberry_pi_imager.png"><img alt="../../../_images/raspberry_pi_imager.png" src="/docs-assets/ja/_images/raspberry_pi_imager.png" style="width: 541.6px; height: 363.20000000000005px;"></a>
</div>
<ul class="simple">
<li><p>[カスタムを使用] を選択し、インストールしたい LEAPS Raspberry Pi イメージを選択します。</p></li>
</ul>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/raspberry_pi_image_use_custom.png"><img alt="../../../_images/raspberry_pi_image_use_custom.png" src="/docs-assets/ja/_images/raspberry_pi_image_use_custom.png" style="width: 604.8000000000001px; height: 361.6px;"></a>
</div>
<ul class="simple">
<li><p>イメージをインストールする正しい SD カードを選択してください。ドライブはプラットフォームごとに異なって表示される場合があります。</p></li>
</ul>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/choose_the_correct_sd_card.png"><img alt="../../../_images/choose_the_correct_sd_card.png" src="/docs-assets/ja/_images/choose_the_correct_sd_card.png" style="width: 604.8000000000001px; height: 359.20000000000005px;"></a>
</div>
<ul class="simple">
<li><p>メモリ容量に基づいて正しいドライブを選択するように特に注意してください。</p></li>
<li><p>LEAPS Raspberry Pi イメージと SD カードが選択されると、新しい <span class="red-text">WRITE</span> ボタンが表示されます。</p></li>
</ul>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/raspberry_pi_image_write.png"><img alt="../../../_images/raspberry_pi_image_write.png" src="/docs-assets/ja/_images/raspberry_pi_image_write.png" style="width: 607.2px; height: 360.8px;"></a>
</div>
<ul class="simple">
<li><p><span class="red-text">書き込み</span> ボタンをクリックします。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="5">
<li><p>書いて仕上げています。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>Raspberry Pi Imager が書き込みプロセスを完了するまで待ちます。</p></li>
</ul>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/raspberry_pi_image_writing.png"><img alt="../../../_images/raspberry_pi_image_writing.png" src="/docs-assets/ja/_images/raspberry_pi_image_writing.png" style="width: 605.6px; height: 362.40000000000003px;"></a>
</div>
<ul class="simple">
<li><p>確認メッセージが表示されたら、SD カードを安全に取り出すことができます。</p></li>
</ul>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/raspberry_pi_image_confirm.png"><img alt="../../../_images/raspberry_pi_image_confirm.png" src="/docs-assets/ja/_images/raspberry_pi_image_confirm.png" style="width: 604.8000000000001px; height: 362.40000000000003px;"></a>
</div>
</div></blockquote>
<ol class="arabic simple" start="6">
<li><p>LEAPS を始めましょう。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>コンピューターまたはラップトップから SD カードを取り外し、Raspberry Pi に挿入します。</p></li>
<li><p>Raspberry Pi の電源が入っていることを確認してください。</p></li>
<li><p>LEAPS システムがインストールされ、Raspberry Pi で起動するように構成されています。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="7">
<li><p>システムが起動するまで待ちます。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>システム全体の起動が完了するまで数分間お待ちください。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="8">
<li><p>Raspberry Pi がブロードキャストする <code class="docutils literal notranslate"><span class="pre">LEAPS-AP</span></code> ネットワークにパスワード <code class="docutils literal notranslate"><span class="pre">Leaps1234</span></code> で接続します。</p></li>
</ol>
<blockquote>
<div><div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/connect_leaps_udk_network.png"><img alt="../../../_images/connect_leaps_udk_network.png" src="/docs-assets/ja/_images/connect_leaps_udk_network.png" style="width: 234.0px; height: 64.5px;"></a>
</div>
</div></blockquote>
<ol class="arabic simple" start="9">
<li><p>Raspberry Pi に SSH 接続します (オプション)。</p></li>
</ol>
<blockquote>
<div><ul>
<li><p>PC (または別の Raspberry Pi) で PowerShell またはターミナルwindowを開き、次のコマンドを入力して SSH 経由で Raspberry Pi に接続します。</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">ssh</span> <span class="n">leaps</span><span class="o">@</span><span class="mf">192.168.200.1</span>
</pre></div>
</div>
</li>
<li><p>デフォルトでは、アカウントは <code class="docutils literal notranslate"><span class="pre">leaps</span></code> 、パスワードは <code class="docutils literal notranslate"><span class="pre">leaps</span></code> です。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="10">
<li><p><a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> を使用してネットワークを準備します。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>デモを設定します: <a class="reference internal" href="/docs/ja/udk/udk-start/twr-rtls-and-data-telemetry-demo#twr-rtls-and-data-telemetry-demo"><span class="std std-ref">TWR RTLS およびデータ遠隔測定デモ</span></a> または <a class="reference internal" href="/docs/ja/udk/udk-start/uplink-tdoa-rtls-demo#uplink-tdoa-rtls-demo"><span class="std std-ref">アップリンク TDoA RTLS デモ</span></a>。</p></li>
<li><p>デフォルトでは、ネットワーク ID は <code class="docutils literal notranslate"><span class="pre">0x1234</span></code> になります。</p></li>
<li><p>この例では、ゲートウェイ bo に接続する必要があります。</p></li>
</ul>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/raspberry_pi_network_demo01.jpg"><img alt="../../../_images/raspberry_pi_network_demo01.jpg" src="/docs-assets/ja/_images/raspberry_pi_network_demo01.jpg" style="width: 360.0px; height: 800.0px;"></a>
</div>
</div></blockquote>
<ol class="arabic simple" start="11">
<li><p>ゲートウェイ ボードとの接続。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>USB-C データ ケーブルを使用して、ゲートウェイ ボードを Raspberry Pi に接続します。</p></li>
<li><p>USB-C データ ケーブルを PC の <a class="reference internal" href="/docs/ja/udk/udk-start/device-hw-interfaces#hardware-interface"><span class="std std-ref">USB-C データ ポート 1</span></a> に差し込みます。安定した接続を確保してください。</p></li>
<li><p>ゲートウェイ モードで正常に接続された場合は、確認としてビープ音が 2 回聞こえます。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="12">
<li><p>システムのステータスを確認します (オプション)。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p><span class="red-text">mosquitto_sub</span> コマンドを使用して、システムのステータスを確認します。このコマンドは Mosquitto MQTT ブローカーに接続し、受信したすべてのメッセージを表示します。</p></li>
</ul>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">mosquitto_sub</span> <span class="o">-</span><span class="n">p</span> <span class="mi">1883</span> <span class="o">-</span><span class="n">d</span> <span class="o">-</span><span class="n">v</span> <span class="o">-</span><span class="n">t</span> <span class="s1">'#'</span>
</pre></div>
</div>
</div></blockquote>
<ol class="arabic simple" start="13">
<li><p><a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> にアクセスします。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>Web ブラウザで、アドレス <span class="red-text">192.168.200.1/24</span> にアクセスします。 (これは、Raspberry Pi 上で直接開くことも、パスワード <code class="docutils literal notranslate"><span class="pre">Leaps1234</span></code> を使用して Raspberry Pi によってブロードキャストされる <code class="docutils literal notranslate"><span class="pre">LEAPS-AP</span></code> ネットワークに接続されている PC 上で開くこともできます - ステップ 9)</p></li>
<li><p>LAN ネットワーク上にある場合は、別のコンピュータの Web ブラウザを使用して Raspberry Pi の IP アドレスにアクセスします。</p></li>
<li><p><a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> で、接続したゲートウェイ ボードのネットワーク ID と一致するようにネットワーク設定を構成します。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="14">
<li><p><a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> にログインします。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>ユーザー名 <span class="red-text">admin</span>、パスワード <span class="red-text">admin</span> を使用してログインします。</p></li>
</ul>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/raspberry_leaps_center_login.png"><img alt="../../../_images/raspberry_leaps_center_login.png" src="/docs-assets/ja/_images/raspberry_leaps_center_login.png" style="width: 762.4000000000001px; height: 370.8px;"></a>
</div>
</div></blockquote>
<ol class="arabic simple" start="15">
<li><p><a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> でネットワークを構成します。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p><a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> のネットワーク設定を確認して、ネットワーク ID と一致するようにしてください。</p></li>
</ul>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/raspberry_pi_leaps_center_udk.png"><img alt="../../../_images/raspberry_pi_leaps_center_udk.png" src="/docs-assets/ja/_images/raspberry_pi_leaps_center_udk.png" style="width: 764.4000000000001px; height: 373.20000000000005px;"></a>
</div>
<ul class="simple">
<li><p>アプリケーションを使用してノードとネットワークを構成および視覚化する方法の詳細については、<a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> および <a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-manager#leapsmanager"><span class="std std-ref">LEAPS Manager</span></a> を参照してください。</p></li>
</ul>
</div></blockquote>
<p>これで、システムは正常にセットアップされ、構成されました。楽しく使ってください！</p>
<div class="admonition note">
<p class="admonition-title">注釈</p>
<p><strong>任意のネットワークで再構成する方法</strong></p>
<ol class="arabic simple">
<li><p>Raspberry Pi で LEAPS-AP Wi-Fi AP をオフにする</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>まず、Raspberry Pi の Wi-Fi アクセス ポイント (AP) を必ず無効にしてください。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="2">
<li><p>Raspberry Piを目的のネットワークに接続します</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>Raspberry Pi を、使用するイーサネットまたは Wi-Fi ネットワークに接続します。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="3">
<li><p>IP アドレスを確認してください</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>Raspberry Pi でターミナルを開き、<code class="docutils literal notranslate"><span class="pre">ifconfig</span></code> コマンドで IP アドレスを確認します。</p></li>
</ul>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/raspberry_pi_check_ip.png"><img alt="../../../_images/raspberry_pi_check_ip.png" src="/docs-assets/ja/_images/raspberry_pi_check_ip.png" style="width: 413.0px; height: 297.5px;"></a>
</div>
<ul class="simple">
<li><p>IP アドレスをメモします。たとえば、<code class="docutils literal notranslate"><span class="pre">192.168.0.104</span></code> などです。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="4">
<li><p>対応する IP アドレスを更新</p></li>
</ol>
<blockquote>
<div><ul>
<li><p>LEAPS Gatewayの構成ファイルを開きます:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">sudo</span> <span class="n">nano</span> <span class="o">/</span><span class="n">usr</span><span class="o">/</span><span class="n">share</span><span class="o">/</span><span class="n">LEAPS</span><span class="o">-</span><span class="n">DOCKER</span><span class="o">-</span><span class="n">LINUX</span><span class="o">/</span><span class="n">leaps</span><span class="o">-</span><span class="n">gateway</span><span class="o">-</span><span class="n">hub</span><span class="o">/</span><span class="n">data</span><span class="o">/</span><span class="n">leaps</span><span class="o">-</span><span class="n">gateway</span><span class="o">.</span><span class="n">conf</span>
</pre></div>
</div>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/raspberry_pi_leaps_gateway.png"><img alt="../../../_images/raspberry_pi_leaps_gateway.png" src="/docs-assets/ja/_images/raspberry_pi_leaps_gateway.png" style="width: 386.5px; height: 271.0px;"></a>
</div>
</li>
<li><p>IP アドレスを指定している行を探し、それを <code class="docutils literal notranslate"><span class="pre">192.168.0.104</span></code> に変更します。</p></li>
<li><p>次に、LEAPS Serverの構成ファイルを開きます:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">sudo</span> <span class="n">nano</span> <span class="o">/</span><span class="n">usr</span><span class="o">/</span><span class="n">share</span><span class="o">/</span><span class="n">LEAPS</span><span class="o">-</span><span class="n">DOCKER</span><span class="o">-</span><span class="n">LINUX</span><span class="o">/</span><span class="n">leaps</span><span class="o">-</span><span class="n">server</span><span class="o">-</span><span class="n">hub</span><span class="o">/</span><span class="n">data</span><span class="o">/</span><span class="n">leaps</span><span class="o">-</span><span class="n">server</span><span class="o">.</span><span class="n">conf</span>
</pre></div>
</div>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/raspberry_pi_leaps_server.png"><img alt="../../../_images/raspberry_pi_leaps_server.png" src="/docs-assets/ja/_images/raspberry_pi_leaps_server.png" style="width: 387.5px; height: 268.5px;"></a>
</div>
</li>
<li><p>再度、このファイルを更新して、新しい IP アドレス <code class="docutils literal notranslate"><span class="pre">192.168.0.104</span></code> を反映します。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="5">
<li><p>LEAPS Serverと LEAPS Gatewayを再起動します</p></li>
</ol>
<blockquote>
<div><ul>
<li><p>変更を加えた後、両方のサービスを再起動します:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">sudo</span> <span class="n">docker</span> <span class="n">restart</span> <span class="n">leaps_server</span>
</pre></div>
</div>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">sudo</span> <span class="n">docker</span> <span class="n">restart</span> <span class="n">leaps_gateway</span>
</pre></div>
</div>
</li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="6">
<li><p>LEAPS Serverと LEAPS Gatewayが正しく動作していることを確認します</p></li>
</ol>
<blockquote>
<div><ul>
<li><p>実行中の Docker コンテナのステータスを確認します。</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span>leaps@raspberrypi:~ $ sudo docker ps
CONTAINER ID   IMAGE                          COMMAND                  CREATED      STATUS          PORTS                                                                                  NAMES
b5bc1d479a04   leapslabs/leaps_gateway:udk   "/app/leaps-gateway …"   6 days ago   Up 15 minutes                                                                                          leaps_gateway
68c33d70bc07   leapslabs/leaps_server:udk    "/app/leaps-server -…"   6 days ago   Up 15 minutes   0.0.0.0:7777-&gt;7777/tcp, 0.0.0.0:7777-&gt;7777/udp, :::7777-&gt;7777/tcp, :::7777-&gt;7777/udp   leaps_server
38092ca7b1b1   leapslabs/leaps_center:udk    "sh -c 'cd /app &amp;&amp;  …"   6 days ago   Up 15 minutes   80/tcp, 0.0.0.0:80-&gt;8080/tcp, [::]:80-&gt;8080/tcp                                        leaps_center
</pre></div>
</div>
</li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="7">
<li><p>MQTT メッセージを監視する</p></li>
</ol>
<blockquote>
<div><ul>
<li><p>MQTT メッセージを監視するには、次を使用します:</p>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">mosquitto_sub</span> <span class="o">-</span><span class="n">p</span> <span class="mi">1883</span> <span class="o">-</span><span class="n">d</span> <span class="o">-</span><span class="n">v</span> <span class="o">-</span><span class="n">t</span> <span class="s1">'#'</span>
</pre></div>
</div>
</li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="8">
<li><p>LEAPS Centerを開いてホストを更新します</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>LEAPS Centerアプリケーションを起動し、ホスト アドレスを <code class="docutils literal notranslate"><span class="pre">192.168.0.104</span></code> に更新します。</p></li>
<li><p>変更を適用するには、必ずネットワークをリロードしてください。</p></li>
</ul>
</div></blockquote>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/raspberry_pi_leaps_center_reconfig.png"><img alt="../../../_images/raspberry_pi_leaps_center_reconfig.png" src="/docs-assets/ja/_images/raspberry_pi_leaps_center_reconfig.png" style="width: 764.8000000000001px; height: 372.40000000000003px;"></a>
</div>
<div class="line-block">
<div class="line"><br></div>
</div>
</div>
<div class="admonition note">
<p class="admonition-title">注釈</p>
<p><strong>Wi-Fi AP: LEAPS-AP のパスワードを設定する方法</strong></p>
<blockquote>
<div><p>Raspberry Pi OS Bookworm でアクセス ポイントのセキュリティとパスワードを設定します。</p>
<blockquote>
<div><div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">sudo</span> <span class="n">nmcli</span> <span class="n">con</span> <span class="n">modify</span> <span class="n">hotspot</span> <span class="n">wifi</span><span class="o">-</span><span class="n">sec</span><span class="o">.</span><span class="n">key</span><span class="o">-</span><span class="n">mgmt</span> <span class="n">wpa</span><span class="o">-</span><span class="n">psk</span>
<span class="n">sudo</span> <span class="n">nmcli</span> <span class="n">con</span> <span class="n">modify</span> <span class="n">hotspot</span> <span class="n">wifi</span><span class="o">-</span><span class="n">sec</span><span class="o">.</span><span class="n">psk</span> <span class="s2">"Leaps1234"</span>
</pre></div>
</div>
</div></blockquote>
<p>Raspberry Pi OS Bullseye 以前でのアクセス ポイントのセットアップ:</p>
<blockquote>
<div><ol class="arabic simple">
<li><p>Hostapd 構成を編集します。この通信で Hostapd 設定ファイルを開きます:</p></li>
</ol>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">sudo</span> <span class="n">nano</span> <span class="o">/</span><span class="n">etc</span><span class="o">/</span><span class="n">hostapd</span><span class="o">/</span><span class="n">hostapd</span><span class="o">.</span><span class="n">conf</span>
</pre></div>
</div>
<ol class="arabic simple" start="2">
<li><p>ファイルの最後に次のパラメータを追加します:</p></li>
</ol>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">wpa</span><span class="o">=</span><span class="mi">2</span>
<span class="n">wpa_passphrase</span><span class="o">=</span><span class="n">Leaps1234</span>
<span class="n">wpa_key_mgmt</span><span class="o">=</span><span class="n">WPA</span><span class="o">-</span><span class="n">PSK</span>
<span class="n">wpa_pairwise</span><span class="o">=</span><span class="n">TKIP</span>
<span class="n">rsn_pairwise</span><span class="o">=</span><span class="n">CCMP</span>
</pre></div>
</div>
<ol class="arabic simple" start="3">
<li><p>保存して終了</p></li>
</ol>
<blockquote>
<div><p><cite>CTRL + O</cite> を押して保存し、<cite>CTRL + X</cite> を押してエディタを終了します。</p>
</div></blockquote>
<ol class="arabic simple" start="4">
<li><p>Raspberry Pi を再起動します</p></li>
</ol>
<blockquote>
<div><p>変更を適用するには、Raspberry Pi を再起動します。</p>
</div></blockquote>
</div></blockquote>
</div></blockquote>
</div>
<div class="admonition note">
<p class="admonition-title">注釈</p>
<p><strong>Step-by-step instructions to expand the filesystem for LEAPS Raspberry Pi (For versions prior to v1.1.0)</strong></p>
<blockquote>
<div><ol class="arabic simple">
<li><p>Open raspi-config. From a terminal on your Raspberry Pi, run:</p></li>
</ol>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">sudo</span> <span class="n">raspi</span><span class="o">-</span><span class="n">config</span>
</pre></div>
</div>
<ol class="arabic simple" start="2">
<li><p>Navigate to Expand Filesystem. Use the arrow keys and Enter:</p></li>
</ol>
<p><code class="docutils literal notranslate"><span class="pre">Advanced</span> <span class="pre">Options</span></code> -&gt; <code class="docutils literal notranslate"><span class="pre">Expand</span> <span class="pre">Filesystem</span></code></p>
<ol class="arabic simple" start="3">
<li><p>Confirm Expansion. Select <code class="docutils literal notranslate"><span class="pre">OK</span></code> when prompted.</p></li>
</ol>
<p>You’ll see a message saying the root filesystem will be expanded on the next reboot</p>
<ol class="arabic simple" start="4">
<li><p>Reboot. When prompted, choose <code class="docutils literal notranslate"><span class="pre">Yes</span></code> to reboot</p></li>
</ol>
<p>(or manually reboot later with <code class="docutils literal notranslate"><span class="pre">sudo</span> <span class="pre">reboot</span></code>):</p>
<ol class="arabic simple" start="5">
<li><p>Verify (Optional). After reboot, confirm the disk is fully expanded:</p></li>
</ol>
<div class="highlight-default notranslate"><div class="highlight"><pre><span></span><span class="n">df</span> <span class="o">-</span><span class="n">h</span> <span class="o">/</span>
</pre></div>
</div>
</div></blockquote>
</div>
</div>


           </div>
