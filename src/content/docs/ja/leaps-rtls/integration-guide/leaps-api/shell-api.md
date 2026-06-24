---
title: "シェルAPI"
lang: ja
slug: "leaps-rtls/integration-guide/leaps-api/shell-api"
section: "leaps-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/leaps-rtls/integration-guide/leaps-api/shell-api/"
order: 115
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="shell-api">
<span id="leaps-shell-api"></span><h1>シェルAPI</h1>
<p><strong>UART インターフェース</strong></p>
<p>シェルはUARTインターフェースを使用します。UARTインターフェースはバイナリモードでも動作します。バイナリモードは、TLV形式のAPIコマンドの読み取りに使用されます。モジュールはリセット後、デフォルトでバイナリモードで起動します。シェルモードに入るには、1秒以内にEnterキーを2回押します。バイナリモードに入るには、シェルモードでコマンド <a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/base#quit"><span class="std std-ref">終了</span></a> を実行します。シェルモードとバイナリモードは切り替え可能です。</p>
<p><strong>サポートされているコマンド</strong></p>
<div class="admonition tip">
<p class="admonition-title">ちなみに</p>
<p>Enterキーを押すと、直前のコマンドを繰り返します。</p>
</div>
<hr class="docutils">
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 15%">
<col style="width: 63%">
<col style="width: 21%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>コマンド</strong></p></th>
<th class="head"><p><strong>説明</strong></p></th>
<th class="head"><p><strong>例</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td colspan="3"><p>Command group: <strong>Base</strong></p></td>
</tr>
<tr class="row-odd"><td><p>?</p></td>
<td><p>このヘルプ</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/base#helpm"><span class="std std-ref">?</span></a></p></td>
</tr>
<tr class="row-even"><td><p>ヘルプ</p></td>
<td><p>このヘルプ</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/base#id1"><span class="std std-ref">ヘルプ</span></a></p></td>
</tr>
<tr class="row-odd"><td><p>終了</p></td>
<td><p>終了</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/base#quit"><span class="std std-ref">終了</span></a></p></td>
</tr>
<tr class="row-even"><td colspan="3"><p>Command group: <strong>SYS</strong></p></td>
</tr>
<tr class="row-odd"><td><p>リセット</p></td>
<td><p>システムを再起動します</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/sys#reset"><span class="std std-ref">リセット</span></a></p></td>
</tr>
<tr class="row-even"><td><p>frst</p></td>
<td><p>出荷時設定にリセット</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/sys#frst"><span class="std std-ref">frst</span></a></p></td>
</tr>
<tr class="row-odd"><td><p>si</p></td>
<td><p>システム情報</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/sys#si"><span class="std std-ref">si</span></a></p></td>
</tr>
<tr class="row-even"><td><p>f</p></td>
<td><p>ヒープ上の空きメモリを表示</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/sys#f"><span class="std std-ref">f</span></a></p></td>
</tr>
<tr class="row-odd"><td><p>stg</p></td>
<td><p>統計情報の取得</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/sys#stg"><span class="std std-ref">stg</span></a></p></td>
</tr>
<tr class="row-even"><td><p>stc</p></td>
<td><p>統計情報をクリア</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/sys#stc"><span class="std std-ref">stc</span></a></p></td>
</tr>
<tr class="row-odd"><td><p>rbv</p></td>
<td><p>バッテリー電圧の読み取り</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/sys#rbv"><span class="std std-ref">rbv</span></a></p></td>
</tr>
<tr class="row-even"><td><p>rcs</p></td>
<td><p>充電器の状態の読み取り</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/sys#rcs"><span class="std std-ref">rcs</span></a></p></td>
</tr>
<tr class="row-odd"><td><p>ut</p></td>
<td><p>デバイスの稼働時間を表示</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/sys#ut"><span class="std std-ref">ut</span></a></p></td>
</tr>
<tr class="row-even"><td><p>sbl</p></td>
<td><p>Set the battery voltage level</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/sys#sbl"><span class="std std-ref">sbl</span></a></p></td>
</tr>
<tr class="row-odd"><td colspan="3"><p>Command group: <strong>SYS</strong></p></td>
</tr>
<tr class="row-even"><td><p>gc</p></td>
<td><p>GPIO クリア</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/gpio#gc"><span class="std std-ref">gc</span></a></p></td>
</tr>
<tr class="row-odd"><td><p>gg</p></td>
<td><p>GPIO 获取</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/gpio#gg"><span class="std std-ref">gg</span></a></p></td>
</tr>
<tr class="row-even"><td><p>gs</p></td>
<td><p>GPIO セット</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/gpio#gs"><span class="std std-ref">gs</span></a></p></td>
</tr>
<tr class="row-odd"><td><p>gt</p></td>
<td><p>GPIOトグル</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/gpio#gt"><span class="std std-ref">gt</span></a></p></td>
</tr>
<tr class="row-even"><td colspan="3"><p>Command group: <strong>SENS</strong></p></td>
</tr>
<tr class="row-odd"><td><p>twi</p></td>
<td><p>汎用 TWI 読み取り</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/sens#twi"><span class="std std-ref">twi</span></a></p></td>
</tr>
<tr class="row-even"><td><p>aid</p></td>
<td><p>ACC デバイス ID を読み取ります</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/sens#aid"><span class="std std-ref">aid</span></a></p></td>
</tr>
<tr class="row-odd"><td><p>av</p></td>
<td><p>ACC 値の読み取り</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/sens#av"><span class="std std-ref">av</span></a></p></td>
</tr>
<tr class="row-even"><td><p>scs</p></td>
<td><p>固定構成セット</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/sens#scs"><span class="std std-ref">scs</span></a></p></td>
</tr>
<tr class="row-odd"><td><p>scg</p></td>
<td><p>固定構成の取得</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/sens#scg"><span class="std std-ref">scg</span></a></p></td>
</tr>
<tr class="row-even"><td colspan="3"><p>Command group: <strong>LE</strong></p></td>
</tr>
<tr class="row-odd"><td><p>les</p></td>
<td><p>測定値と位置の表示</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/le#les"><span class="std std-ref">les</span></a></p></td>
</tr>
<tr class="row-even"><td><p>lec</p></td>
<td><p>測定値と位置をCSVで表示</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/le#lec"><span class="std std-ref">lec</span></a></p></td>
</tr>
<tr class="row-odd"><td><p>lep</p></td>
<td><p>位置をCSVで表示</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/le#lep"><span class="std std-ref">lep</span></a></p></td>
</tr>
<tr class="row-even"><td><p>lej</p></td>
<td><p>位置をJSONで表示</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/le#lej"><span class="std std-ref">lej</span></a></p></td>
</tr>
<tr class="row-odd"><td><p>lea</p></td>
<td><p>測定値、位置、PDOAの情報</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/le#lea"><span class="std std-ref">lea</span></a></p></td>
</tr>
<tr class="row-even"><td colspan="3"><p>Command group: <strong>UWB</strong></p></td>
</tr>
<tr class="row-odd"><td><p>ucs</p></td>
<td><p>UWBチャンネルとコンプライアンスの設定</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/uwb#ucs"><span class="std std-ref">ucs</span></a></p></td>
</tr>
<tr class="row-even"><td><p>utpg</p></td>
<td><p>TxPwr を取得</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/uwb#utpg"><span class="std std-ref">utpg</span></a></p></td>
</tr>
<tr class="row-odd"><td><p>utps</p></td>
<td><p>TxPwr を設定する</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/uwb#utps"><span class="std std-ref">utps</span></a></p></td>
</tr>
<tr class="row-even"><td><p>ufs</p></td>
<td><p>UWBフロントエンドの設定</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/uwb#ufs"><span class="std std-ref">ufs</span></a></p></td>
</tr>
<tr class="row-odd"><td><p>ucls</p></td>
<td><p>BLE Adv UWBカウンターの下限値の設定</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/uwb#ucls"><span class="std std-ref">ucls</span></a></p></td>
</tr>
<tr class="row-even"><td><p>uclg</p></td>
<td><p>BLE Adv UWBカウンターの下限値を取得</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/uwb#uclg"><span class="std std-ref">uclg</span></a></p></td>
</tr>
<tr class="row-odd"><td colspan="3"><p>Command group: <strong>UWBMAC</strong></p></td>
</tr>
<tr class="row-even"><td><p>nmo</p></td>
<td><p>UWB モードをオフに設定します</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/uwbmac#nmo"><span class="std std-ref">nmo</span></a></p></td>
</tr>
<tr class="row-odd"><td><p>nmp</p></td>
<td><p>UWB モードをパッシブに設定します</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/uwbmac#nmp"><span class="std std-ref">nmp</span></a></p></td>
</tr>
<tr class="row-even"><td><p>nma</p></td>
<td><p>モードを AN に設定します</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/uwbmac#nma"><span class="std std-ref">nma</span></a></p></td>
</tr>
<tr class="row-odd"><td><p>nmi</p></td>
<td><p>モードを ANI に設定します</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/uwbmac#nmi"><span class="std std-ref">nmi</span></a></p></td>
</tr>
<tr class="row-even"><td><p>nmt</p></td>
<td><p>モードを TN に設定します</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/uwbmac#nmt"><span class="std std-ref">nmt</span></a></p></td>
</tr>
<tr class="row-odd"><td><p>nmtl</p></td>
<td><p>モードを TN-LP に設定します。</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/uwbmac#nmtl"><span class="std std-ref">nmtl</span></a></p></td>
</tr>
<tr class="row-even"><td><p>nmg</p></td>
<td><p>モードを GN に設定します</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/uwbmac#nmg"><span class="std std-ref">nmg</span></a></p></td>
</tr>
<tr class="row-odd"><td><p>ln</p></td>
<td><p>ノードリストを表示</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/uwbmac#ln"><span class="std std-ref">ln</span></a></p></td>
</tr>
<tr class="row-even"><td><p>la</p></td>
<td><p>AN リストを表示</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/uwbmac#la"><span class="std std-ref">la</span></a></p></td>
</tr>
<tr class="row-odd"><td><p>nis</p></td>
<td><p>ネットワーク ID を設定します</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/uwbmac#nis"><span class="std std-ref">nis</span></a></p></td>
</tr>
<tr class="row-even"><td><p>nls</p></td>
<td><p>ノードラベルを設定します</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/uwbmac#nls"><span class="std std-ref">nls</span></a></p></td>
</tr>
<tr class="row-odd"><td><p>nps</p></td>
<td><p>ネットワークプロファイルを設定</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/uwbmac#nps"><span class="std std-ref">nps</span></a></p></td>
</tr>
<tr class="row-even"><td><p>udi</p></td>
<td><p>受信した IoT データを表示</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/uwbmac#udi"><span class="std std-ref">udi</span></a></p></td>
</tr>
<tr class="row-odd"><td><p>uui</p></td>
<td><p>IoT データを送信する</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/uwbmac#uui"><span class="std std-ref">uui</span></a></p></td>
</tr>
<tr class="row-even"><td><p>usps</p></td>
<td><p>スーパーフレームサイクルごとのパルス数を設定。例：50は50スーパーフレームに1パルスを意味します。</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/uwbmac#usps"><span class="std std-ref">usps</span></a></p></td>
</tr>
<tr class="row-odd"><td><p>uspg</p></td>
<td><p>スーパーフレームサイクルごとのパルス数を取得。</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/uwbmac#uspg"><span class="std std-ref">uspg</span></a></p></td>
</tr>
<tr class="row-even"><td colspan="3"><p>Command group: <strong>API</strong></p></td>
</tr>
<tr class="row-odd"><td><p>urs</p></td>
<td><p>更新レートを設定</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/api#urs"><span class="std std-ref">urs</span></a></p></td>
</tr>
<tr class="row-even"><td><p>urg</p></td>
<td><p>更新レートを取得</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/api#urg"><span class="std std-ref">urg</span></a></p></td>
</tr>
<tr class="row-odd"><td><p>tcs</p></td>
<td><p>タグ構成を設定します</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/api#tcs"><span class="std std-ref">tcs</span></a></p></td>
</tr>
<tr class="row-even"><td><p>tlv</p></td>
<td><p>TLV フレームを送信</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/api#tlv"><span class="std std-ref">tlv</span></a></p></td>
</tr>
<tr class="row-odd"><td><p>tlvr</p></td>
<td><p>手動CRC付きTLVフレームとしてコマンドを送信</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/api#tlvr"><span class="std std-ref">tlvr</span></a></p></td>
</tr>
<tr class="row-even"><td><p>ums</p></td>
<td><p>デフォルトの UART モードを設定します</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/api#ums"><span class="std std-ref">ums</span></a></p></td>
</tr>
<tr class="row-odd"><td><p>ana</p></td>
<td><p>MAC アドレスを設定</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/api#ana"><span class="std std-ref">ana</span></a></p></td>
</tr>
<tr class="row-even"><td><p>amlg</p></td>
<td><p>MACアドレスリストを取得</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/api#amlg"><span class="std std-ref">amlg</span></a></p></td>
</tr>
<tr class="row-odd"><td><p>mrs</p></td>
<td><p>メッシュランダムタイミングを設定</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/api#mrs"><span class="std std-ref">mrs</span></a></p></td>
</tr>
<tr class="row-even"><td><p>mrg</p></td>
<td><p>メッシュランダムタイミングを取得</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/api#mrg"><span class="std std-ref">mrg</span></a></p></td>
</tr>
<tr class="row-odd"><td><p>dacs</p></td>
<td><p>距離アラーム設定</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/api#dacs"><span class="std std-ref">dacs</span></a></p></td>
</tr>
<tr class="row-even"><td><p>dacg</p></td>
<td><p>距離アラーム取得</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/api#dacg"><span class="std std-ref">dacg</span></a></p></td>
</tr>
<tr class="row-odd"><td><p>acs</p></td>
<td><p>ノードの構成</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/api#acs"><span class="std std-ref">acs</span></a></p></td>
</tr>
<tr class="row-even"><td><p>pg</p></td>
<td><p>ポジションを取得する</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/api#pg"><span class="std std-ref">pg</span></a></p></td>
</tr>
<tr class="row-odd"><td><p>ps</p></td>
<td><p>ポジションの設定</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/api#ps"><span class="std std-ref">ps</span></a></p></td>
</tr>
<tr class="row-even"><td><p>fls</p></td>
<td><p>フィルター設定設定</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/api#fls"><span class="std std-ref">fls</span></a></p></td>
</tr>
<tr class="row-odd"><td><p>flg</p></td>
<td><p>フィルター取得</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/api#flg"><span class="std std-ref">flg</span></a></p></td>
</tr>
<tr class="row-even"><td><p>ahs</p></td>
<td><p>HW バージョンを 1 回設定します</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/api#ahs"><span class="std std-ref">ahs</span></a></p></td>
</tr>
<tr class="row-odd"><td><p>eks</p></td>
<td><p>暗号化キーを設定します</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/api#eks"><span class="std std-ref">eks</span></a></p></td>
</tr>
<tr class="row-even"><td><p>ekc</p></td>
<td><p>暗号化キーをクリアします</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/api#ekc"><span class="std std-ref">ekc</span></a></p></td>
</tr>
<tr class="row-odd"><td><p>amls</p></td>
<td><p>MAC アドレスリストを 1 回設定します</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/api#amls"><span class="std std-ref">amls</span></a></p></td>
</tr>
<tr class="row-even"><td colspan="3"><p>Command group: <strong>INET</strong></p></td>
</tr>
<tr class="row-odd"><td><p>ipv4</p></td>
<td><p>Set local IPv4</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/inet#ipv4"><span class="std std-ref">ipv4</span></a></p></td>
</tr>
<tr class="row-even"><td><p>peer</p></td>
<td><p>Set server IPv4</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/inet#peer"><span class="std std-ref">peer</span></a></p></td>
</tr>
<tr class="row-odd"><td><p>wifi</p></td>
<td><p>Set WIFI configuration</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/inet#wifi"><span class="std std-ref">wifi</span></a></p></td>
</tr>
<tr class="row-even"><td><p>dns</p></td>
<td><p>Set DNS server IP address list</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/inet#dns"><span class="std std-ref">dns</span></a></p></td>
</tr>
<tr class="row-odd"><td><p>switch</p></td>
<td><p>Set net switch configuration</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/inet#switch"><span class="std std-ref">switch</span></a></p></td>
</tr>
<tr class="row-even"><td colspan="3"><p>Command group: <strong>HAWKBIT</strong></p></td>
</tr>
<tr class="row-odd"><td><p>hb_peer</p></td>
<td><p>Set Hawkbit server IPv4</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/hawkbit#hb-peer"><span class="std std-ref">hb_peer</span></a></p></td>
</tr>
<tr class="row-even"><td><p>hb_token</p></td>
<td><p>Set Hawkbit auth token</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/hawkbit#hb-token"><span class="std std-ref">hb_token</span></a></p></td>
</tr>
<tr class="row-odd"><td colspan="3"><p>Command group: <strong>BDG</strong></p></td>
</tr>
<tr class="row-even"><td><p>utlv</p></td>
<td><p>Cmd as TLV frame for UWB Subsystem</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/bdg#utlv"><span class="std std-ref">utlv</span></a></p></td>
</tr>
<tr class="row-odd"><td colspan="3"><p>Command group: <strong>FiRa</strong></p></td>
</tr>
<tr class="row-even"><td><p>fniq</p></td>
<td><p>デバイスをFiRa UWBサブシステム近傍インタラクションモードに設定します。</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/fira#fniq"><span class="std std-ref">fniq</span></a></p></td>
</tr>
<tr class="row-odd"><td><p>fuci</p></td>
<td><p>デバイスをFiRa UWBサブシステムUCIモードに設定します。</p></td>
<td><p><a class="reference internal" href="/docs/ja/leaps-rtls/integration-guide/shell-api/fira#fuci"><span class="std std-ref">fuci</span></a></p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
<div class="toctree-wrapper compound">
</div>
</div>


           </div>
