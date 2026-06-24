---
title: "PANS PRO Raspberry Pi"
lang: ja
slug: "pans-pro-rtls/quick-start-guide/panspro-rpi"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/pans-pro-rtls/quick-start-guide/panspro-rpi/"
order: 91
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="pans-pro-raspberry-pi">
<span id="panspro-rpi"></span><h1>PANS PRO Raspberry Pi</h1>
<p>このページには以下が含まれます:</p>
<blockquote>
<div><ul class="simple">
<li><p>PANS PRO Raspberry Pi パッケージ。</p></li>
<li><p>システム要件に関する情報。</p></li>
<li><p>PANS PRO Raspberry Pi のインストール方法に関する説明。</p></li>
</ul>
</div></blockquote>
<p>インストールは迅速かつ簡単で、一度行うだけで済みます。</p>
<p id="uiraspberrypi"><span class="red-text">開始する前に: フォーマット中にすべてのデータが永久に上書きされるため、保存しておきたい重要なファイルは必ず SD カードからバックアップしてください。</span></p>
<p><strong>システム要件</strong></p>
<blockquote>
<div><ul class="simple">
<li><p>Raspberry Pi 3B 以降。</p></li>
<li><p><em>推奨: 検証するセット (少なくとも 5 台のデバイス)。</em></p></li>
<li><p><em>推奨: デバイスに電力を供給するためのバッテリーまたは Micro USB ケーブル。</em></p></li>
<li><p><em>推奨:</em> <a class="reference internal" href="/docs/ja/pans-pro-rtls/infrastructure/pans-pro-manager#pans-pro-manager"><span class="std std-ref">PANS PRO Manager</span></a> <em>デバイスを構成します。</em></p></li>
</ul>
</div></blockquote>
<p><strong>セットアップ手順</strong></p>
<ol class="arabic simple">
<li><p>ダウンロードPANS PRO Raspberry Pi のイメージ。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>ダウンロード パッケージについては、<a class="reference external" href="mailto:apps-support%40leapslabs.com">apps-support<span>@</span>leapslabs<span>.</span>com</a> までお問い合わせください。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="2">
<li><p>PANS PRO Raspberry Pi アーカイブを抽出します。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>WinZip や 7-Zip などのプログラムを使用して、ダウンロードした PANS PRO Raspberry Pi zip ファイルを解凍します。</p></li>
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
<li><p>PANS PRO Raspberry Pi イメージをインストールしています。</p></li>
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
<li><p>[カスタムを使用] を選択し、インストールしたい PANS PRO Raspberry Pi イメージを選択します。</p></li>
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
<li><p>PANS PRO Raspberry Pi イメージと SD カードが選択されると、新しい <span class="red-text">WRITE</span> ボタンが表示されます。</p></li>
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
<li><p>PANS PRO を始めましょう。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>コンピューターまたはラップトップから SD カードを取り外し、Raspberry Pi に挿入します。</p></li>
<li><p>Raspberry Pi の電源が入っていることを確認してください。</p></li>
<li><p>PANS PRO システムがインストールされ、Raspberry Pi で起動するように構成されています。</p></li>
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
<li><p><a class="reference internal" href="/docs/ja/pans-pro-rtls/infrastructure/pans-pro-manager#pans-pro-manager"><span class="std std-ref">PANS PRO Manager</span></a> を使用してネットワークを準備し、<cite>ネットワーク ID</cite> を決定します。</p></li>
<li><p>ゲートウェイ ボードの設定と接続。</p></li>
</ol>
<blockquote>
<div><p>11.1。設定ファイルを開きます。</p>
<blockquote>
<div><div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">sudo nano /usr/share/LEAPS-DOCKER-LINUX/leaps-server-hub/data/leaps-server.conf</span>
</pre></div>
</div>
</div></blockquote>
<p>11.2。 LEAPS Serverの構成を更新します。</p>
<blockquote>
<div><ul class="simple">
<li><p>MQTT API バリアントを次のいずれかの``pans``に変更します。</p></li>
</ul>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">mqtt_api = pans</span>
</pre></div>
</div>
</div></blockquote>
<p>11.3。 LEAPS Serverを再起動します。</p>
<blockquote>
<div><ul class="simple">
<li><p>変更を保存した後、サービスを再起動します。</p></li>
</ul>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="go">sudo docker restart leaps_server</span>
</pre></div>
</div>
</div></blockquote>
<p>11.4。 LEAPS Serverの状態を確認します。</p>
<blockquote>
<div><ul class="simple">
<li><p>実行中の Docker コンテナのステータスを確認します。</p></li>
</ul>
<div class="highlight-console notranslate"><div class="highlight"><pre><span></span><span class="gp">leaps@raspberrypi:~ $ </span>sudo<span class="w"> </span>docker<span class="w"> </span>ps
<span class="go">CONTAINER ID        IMAGE                           COMMAND                  CREATED        STATUS              PORTS                                                  NAMES</span>
<span class="go">68c33d70bc07        leapslabs/leaps_server:udk    "/app/leaps-server -..." 6 days ago     Up 15 minutes       0.0.0.0:7777-&gt;7777/tcp, 0.0.0.0:7777-&gt;7777/udp, :::7777-&gt;7777/tcp, :::7777-&gt;7777/udp   leaps_server</span>
<span class="go">38092ca7b1b1        leapslabs/leaps_center:udk     "sh -c 'cd /app &amp;&amp; ..." 6 days ago     Up 15 minutes       80/tcp, 0.0.0.0:80-&gt;8080/tcp, [::]:80-&gt;8080/tcp                    leaps_center</span>
</pre></div>
</div>
</div></blockquote>
<p>11.5。 Raspberry PI Ethernet をゲートウェイ ボードに直接接続するか、ゲートウェイ ボードを備えた別のスイッチに接続します。</p>
<blockquote>
<div><ul class="simple">
<li><p>IP アドレス: 192.168.200.1</p></li>
<li><p>ネットワークマスク: 255.255.255.0</p></li>
</ul>
<p>注: 一般的なスイッチ/ルーターに接続できますが、IP アドレスが競合する可能性があります。 Raspberry PI のイーサネット構成は次のように静的です。</p>
</div></blockquote>
<p>11.6。ゲートウェイ ボードのネットワーク ID が UWB ネットワークと一致していることを確認します。詳細については、<code class="docutils literal notranslate"><span class="pre">Web</span> <span class="pre">によるクイック</span> <span class="pre">スタート</span></code> の <code class="docutils literal notranslate"><span class="pre">ゲートウェイ構成</span></code> を参照してください。</p>
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
<li><p>Web ブラウザで、アドレス <span class="red-text">192.168.200.1/24</span> にアクセスします。 (これは、Raspberry Pi 上で直接開くことも、パスワード <code class="docutils literal notranslate"><span class="pre">Leaps1234</span></code>  Raspberry Pi によってブロードキャストされる``LEAPS-AP``ネットワークに接続されている PC 上で開くこともできます - ステップ 9)</p></li>
<li><p>LAN ネットワーク上にある場合は、別のコンピュータの Web ブラウザを使用して Raspberry Pi の IP アドレスにアクセスします。</p></li>
<li><p><a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> で、接続したゲートウェイ ボードのネットワーク ID と一致するようにネットワーク設定を構成します。</p></li>
</ul>
<div class="figure align-center">
<a class="reference internal image-reference" href="../../../_images/leaps_center_login.png"><img alt="../../../_images/leaps_center_login.png" src="/docs-assets/ja/_images/leaps_center_login.png" style="width: 762.8000000000001px; height: 360.0px;"></a>
</div>
</div></blockquote>
<ol class="arabic simple" start="14">
<li><p><a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> にログインします。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p>ユーザー名 <span class="red-text">admin</span>、パスワード <span class="red-text">admin</span> を使用してログインします。</p></li>
</ul>
</div></blockquote>
<ol class="arabic simple" start="15">
<li><p><a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> でネットワークを構成します。</p></li>
</ol>
<blockquote>
<div><ul class="simple">
<li><p><a class="reference internal" href="/docs/ja/leaps-rtls/infrastructure/leaps-center#leapscenter"><span class="std std-ref">LEAPS Center</span></a> のネットワーク設定を確認して、ネットワーク ID と一致するようにしてください。</p></li>
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
