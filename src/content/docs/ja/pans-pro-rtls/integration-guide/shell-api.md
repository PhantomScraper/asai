---
title: "シェルAPI"
lang: ja
slug: "pans-pro-rtls/integration-guide/shell-api"
section: "pans-pro-rtls"
sourceUrl: "https://docs.leapslabs.com/ja/pans-pro-rtls/integration-guide/shell-api/"
order: 122
---

<!-- <div class="wy-alert wy-alert-warning">
    Please note that the Chinese and Japanese versions are currently being updated and are not yet complete. Stay tuned for the final versions!
  </div> -->

  
           <div itemprop="articleBody">
             
  <div class="section" id="shell-api">
<h1>シェルAPI</h1>
<p>Shell は、バイナリ モードでも動作できる UART インターフェイスを使用します。バイナリ モードは、TLV 形式の API コマンドを読み取るために使用されます。DWM は、リセット後、デフォルトでバイナリ モードで起動します。シェル モードに切り替えるには、1 秒以内に ENTER キーを 2 回押します。バイナリ モードに切り替えるには、シェル モードでコマンド``quit``を実行します。シェル モードとバイナリ モードは、切り替えることができます。シェル モードで Enter キーを押すと、最後のコマンドが繰り返されます。次のテキストは、シェル コマンドの概要を示しています。</p>
<hr class="docutils">
<p>次の表は、イーサネット ゲートウェイとエッジ ノードでのシェル コマンドの利用可能性の概要を示しています。</p>
<table class="custom-table docutils align-default">
<colgroup>
<col style="width: 27%">
<col style="width: 46%">
<col style="width: 13%">
<col style="width: 13%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p><strong>コマンド</strong></p></th>
<th class="head"><p><strong>説明</strong></p></th>
<th class="head"><p><strong>DWM1001</strong></p></th>
<th class="head"><p><strong>ゲートウェイ</strong></p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/shell-api/base#pp-helpm"><span class="std std-ref">?</span></a></p></td>
<td><p>このヘルプ</p></td>
<td><p>はい</p></td>
<td><p>はい</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/shell-api/base#pp-help"><span class="std std-ref">ヘルプ</span></a></p></td>
<td><p>このヘルプ</p></td>
<td><p>はい</p></td>
<td><p>はい</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/shell-api/base#pp-quit"><span class="std std-ref">終了</span></a></p></td>
<td><p>終了</p></td>
<td><p>はい</p></td>
<td><p>はい</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/shell-api/gpio#pp-gc"><span class="std std-ref">gc</span></a></p></td>
<td><p>GPIO クリア</p></td>
<td><p>はい</p></td>
<td><p>はい</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/shell-api/gpio#pp-gg"><span class="std std-ref">gg</span></a></p></td>
<td><p>GPIO 获取</p></td>
<td><p>はい</p></td>
<td><p>はい</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/shell-api/gpio#pp-gs"><span class="std std-ref">gs</span></a></p></td>
<td><p>GPIO セット</p></td>
<td><p>はい</p></td>
<td><p>はい</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/shell-api/gpio#pp-gt"><span class="std std-ref">gt</span></a></p></td>
<td><p>GPIOの切り替え</p></td>
<td><p>はい</p></td>
<td><p>はい</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/shell-api/sys#pp-f"><span class="std std-ref">f</span></a></p></td>
<td><p>ヒープ上の空きメモリを表示</p></td>
<td><p>はい</p></td>
<td><p>はい</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/shell-api/sys#pp-reset"><span class="std std-ref">リセット</span></a></p></td>
<td><p>システムを再起動します</p></td>
<td><p>はい</p></td>
<td><p>はい</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/shell-api/sys#pp-si"><span class="std std-ref">si</span></a></p></td>
<td><p>システム情報</p></td>
<td><p>はい</p></td>
<td><p>はい</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/shell-api/sys#pp-ut"><span class="std std-ref">ut</span></a></p></td>
<td><p>デバイスの稼働時間を表示</p></td>
<td><p>はい</p></td>
<td><p>はい</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/shell-api/sys#pp-sbl"><span class="std std-ref">sbl</span></a></p></td>
<td><p>Set the battery voltage level</p></td>
<td><p>はい</p></td>
<td><p>はい</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/shell-api/sys#pp-frst"><span class="std std-ref">frst</span></a></p></td>
<td><p>出荷時設定にリセット</p></td>
<td><p>はい</p></td>
<td><p>はい</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/shell-api/sens#pp-twi"><span class="std std-ref">twi</span></a></p></td>
<td><p>汎用 TWI 読み取り</p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/shell-api/sens#pp-aid"><span class="std std-ref">aid</span></a></p></td>
<td><p>ACC デバイス ID を読み取ります</p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/shell-api/sens#pp-av"><span class="std std-ref">av</span></a></p></td>
<td><p>ACC 値の読み取り</p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/shell-api/sens#pp-scs"><span class="std std-ref">scs</span></a></p></td>
<td><p>固定構成セット</p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/shell-api/sens#pp-scg"><span class="std std-ref">scg</span></a></p></td>
<td><p>固定構成の取得</p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/shell-api/le#pp-les"><span class="std std-ref">les</span></a></p></td>
<td><p>測定値を表示します。そしてポス。</p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/shell-api/le#pp-lec"><span class="std std-ref">lec</span></a></p></td>
<td><p>CSV で測定値と位置を表示</p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/shell-api/le#pp-lep"><span class="std std-ref">lep</span></a></p></td>
<td><p>CSV で位置を表示</p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/shell-api/uwb#pp-utpg"><span class="std std-ref">utpg</span></a></p></td>
<td><p>TxPwr を取得</p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/shell-api/uwb#pp-utps"><span class="std std-ref">utps</span></a></p></td>
<td><p>TxPwr を設定する</p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/shell-api/uwbmac#pp-nmp"><span class="std std-ref">nmp</span></a></p></td>
<td><p>UWB モードをパッシブに設定します</p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/shell-api/uwbmac#pp-nmo"><span class="std std-ref">nmo</span></a></p></td>
<td><p>UWB モードをオフに設定します</p></td>
<td><p>はい</p></td>
<td><p>はい</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/shell-api/uwbmac#pp-nma"><span class="std std-ref">nma</span></a></p></td>
<td><p>モードを AN に設定します</p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/shell-api/uwbmac#pp-nmi"><span class="std std-ref">nmi</span></a></p></td>
<td><p>モードを ANI に設定します</p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/shell-api/uwbmac#pp-nmt"><span class="std std-ref">nmt</span></a></p></td>
<td><p>モードを TN に設定します</p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/shell-api/uwbmac#pp-nmtl"><span class="std std-ref">nmtl</span></a></p></td>
<td><p>モードを TN-LP に設定します。</p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/shell-api/uwbmac#pp-nmg"><span class="std std-ref">nmg</span></a></p></td>
<td><p>モードを GN に設定します</p></td>
<td><p>はい</p></td>
<td><p>はい</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/shell-api/uwbmac#pp-la"><span class="std std-ref">la</span></a></p></td>
<td><p>AN リストを表示</p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/shell-api/uwbmac#pp-lg"><span class="std std-ref">lg</span></a></p></td>
<td><p>GN リストを表示</p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/shell-api/uwbmac#pp-nis"><span class="std std-ref">nis</span></a></p></td>
<td><p>ネットワーク ID を設定します</p></td>
<td><p>はい</p></td>
<td><p>はい</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/shell-api/uwbmac#pp-nls"><span class="std std-ref">nls</span></a></p></td>
<td><p>ノードラベルを設定します</p></td>
<td><p>はい</p></td>
<td><p>はい</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/shell-api/uwbmac#pp-udi"><span class="std std-ref">udi</span></a></p></td>
<td><p>受信した IoT データを表示</p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/shell-api/uwbmac#pp-uui"><span class="std std-ref">uui</span></a></p></td>
<td><p>IoT データを送信する</p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/shell-api/uwbmac#pp-stg"><span class="std std-ref">stg</span></a></p></td>
<td><p>統計情報の取得</p></td>
<td><p>はい</p></td>
<td><p>はい</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/shell-api/uwbmac#pp-stc"><span class="std std-ref">stc</span></a></p></td>
<td><p>統計情報をクリア</p></td>
<td><p>はい</p></td>
<td><p>はい</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/shell-api/api#pp-tlv"><span class="std std-ref">tlv</span></a></p></td>
<td><p>TLV フレームを送信</p></td>
<td><p>はい</p></td>
<td><p>はい</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/shell-api/api#pp-aurs"><span class="std std-ref">aurs</span></a></p></td>
<td><p>アップレートを設定します</p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/shell-api/api#pp-aurg"><span class="std std-ref">aurg</span></a></p></td>
<td><p>アップレートを取得</p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/shell-api/api#pp-apg"><span class="std std-ref">apg</span></a></p></td>
<td><p>位置情報を取得</p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/shell-api/api#pp-aps"><span class="std std-ref">aps</span></a></p></td>
<td><p>位置を設定</p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/shell-api/api#pp-acas"><span class="std std-ref">acas</span></a></p></td>
<td><p>アンカー構成を設定します</p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/shell-api/api#pp-acts"><span class="std std-ref">acts</span></a></p></td>
<td><p>タグ構成を設定します</p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/shell-api/api#pp-aks"><span class="std std-ref">aks</span></a></p></td>
<td><p>暗号化キーを設定します</p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/shell-api/api#pp-akc"><span class="std std-ref">akc</span></a></p></td>
<td><p>暗号化キーをクリアします</p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/shell-api/api#pp-ans"><span class="std std-ref">ans</span></a></p></td>
<td><p>NVM ユーザーデータを設定します</p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
</tr>
<tr class="row-even"><td><p>anc (例が見つかりません)</p></td>
<td><p>NVM ユーザーデータをクリア</p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/shell-api/api#pp-ang"><span class="std std-ref">ang</span></a></p></td>
<td><p>NVM ユーザーデータを取得</p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/shell-api/gateway#pp-amls"><span class="std std-ref">amls</span></a></p></td>
<td><p>MAC アドレスリストを 1 回設定します</p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/shell-api/gateway#pp-amlg"><span class="std std-ref">amlg</span></a></p></td>
<td><p>MAC アドレスリストを取得</p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/shell-api/gateway#pp-ahs"><span class="std std-ref">ahs</span></a></p></td>
<td><p>HW バージョンを 1 回設定します</p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/shell-api/gateway#pp-ana"><span class="std std-ref">ana</span></a></p></td>
<td><p>MAC アドレスを設定</p></td>
<td><p>はい</p></td>
<td><p>いいえ</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/shell-api/gateway#pp-acs"><span class="std std-ref">acs</span></a></p></td>
<td><p>ノードの構成</p></td>
<td><p>いいえ</p></td>
<td><p>はい</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/shell-api/gateway#pp-ums"><span class="std std-ref">ums</span></a></p></td>
<td><p>デフォルトの UART モードを設定します</p></td>
<td><p>いいえ</p></td>
<td><p>はい</p></td>
</tr>
<tr class="row-even"><td><p><a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/shell-api/gateway#pp-ipv4"><span class="std std-ref">ipv4</span></a></p></td>
<td><p>ローカル IPv4 を設定します</p></td>
<td><p>いいえ</p></td>
<td><p>はい</p></td>
</tr>
<tr class="row-odd"><td><p><a class="reference internal" href="/docs/ja/pans-pro-rtls/integration-guide/shell-api/gateway#pp-dns"><span class="std std-ref">dns</span></a></p></td>
<td><p>DNS サーバーの IP アドレスリストを設定します</p></td>
<td><p>いいえ</p></td>
<td><p>はい</p></td>
</tr>
</tbody>
</table>
<hr class="docutils">
<div class="toctree-wrapper compound">
</div>
</div>


           </div>
