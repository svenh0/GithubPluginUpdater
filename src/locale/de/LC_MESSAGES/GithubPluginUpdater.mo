��    �      D  �   l      8     9  -   Q  '        �  '   �  "   �  #     )   ,  �   V  �   �  5   h  /   �     �  a   �     J     a  8   x     �     �     �     �       -   -  8   [  .   �  *   �  )   �  "        ;     Q     d     r     w     �  >   �  Q   �  h   )     �  �   �     '     9  �   J  1   �  2        :  !   N     p     �  *   �  %   �     �  >   �  %   3  '   Y  C   �    �  w   �  �   N           (     �   B  !   #     E  ,   _     �     �     �  %   �     �  �        �     �     �  #   �       G   *  +   r     �  .   �     �     �     �               &     4     K     R  '   r  (   �     �     �     �               $     =     X     `  %   c  b   �     �     �  0        A      T     u  &   �     �     �  !   �  b   
   B   m   �   �   +   5!  �   a!     �!  `   �!     Y"  #   j"     �"  Q   �"  &   �"     #     #  $   1#  4   V#     �#  	   �#     �#     �#  h  �#     %  0   4%  *   e%     �%  ,   �%  (   �%  '   &  )   )&  �   S&  �   �&  ;   i'  3   �'  #   �'  u   �'     s(     �(  >   �(     �(      )     )     4)     R)  4   l)  ;   �)  1   �)  4   *  %   D*  %   j*     �*     �*     �*     �*     �*     �*  ;   �*  ^   1+  �   �+  	   0,  �   :,     �,     �,  �   -  ;   �-  ;   �-     .      .     =.     X.  4   m.  3   �.     �.  Q   �.  '   +/  )   S/  I   }/    �/  �   �0  �   e1  %  ;2     a4  '   m4    �4  #   �5     �5  /   �5     6     6     76  '   S6     {6  �   �6     f7     �7     �7  '   �7     �7  I   �7  -   -8     [8  3   d8     �8     �8     �8     �8     �8     �8     9  
   9  #   %9  7   I9  6   �9     �9     �9     �9     �9     :     $:  $   >:  	   c:     m:  -   r:  t   �:     ;     %;  5   :;     p;  %   �;     �;  0   �;  *   <     ,<  &   K<  }   r<  \   �<  �   M=  1   �=  �   >     �>  o   �>     _?  ,   p?     �?  e   �?  )   @     5@     B@  '   [@  8   �@     �@  	   �@     �@     �@         @          (   J      4   �   1       |       F   r   [       -   w   %   O   q      !   f   a   I                                6   y       *       S           C   �   9   '   n   3       �   &   )   B   k           E   T   c          ?   �   	   7   `              V   v   P   U      =   ;   ^   �       e         0   5                  s   \       :   N          2                   m          "   x       X      z   o       G      u   M       <              i               ~   >   ,   �   d   K             h   l              +   _   8   A   R   g   {   
       #      Z   j   ]   .   /           Q       D          H   }      b   t   L   p   Y          $       W           


Exit-button to close 

Do you want to start the github update now? 

Do you want to start the update now?
 

exit-key for cancel 
  install current github version...... 
  installed version after update: 
  installed version before update: 
  load current version from github...... 
 = GithubPluginUpdater = 

  >>> there are updates for the following plugins !!! <<<
  %s


  open the GithubPluginUpdater for the update 
 = GithubPluginUpdater = 

  >>> there are updates for the following plugins !!! <<<
  %s


Should the GithubPluginUpdater be opened? 
 = GithubPluginUpdater = 

  no plugin updates found 
... more infos in the advanced update-info ... 
A newer version exists!
 
The advanced update info could not be loaded.
The hourly limit for github queries was reached!!
 
current time:     	   
error on update-check 
for more update-infos please visit the github-website.
 
limit reset time: 	   
loading update info...
 
query limit per hour:	   
remaining query limit:	   
waiting to reset: 	          answer for question is default set to:    advanced update-info with question to open the plugin    duration of update-info-window (in seconds)    interval of AutoUpdateCheck on boxstart    storage location for the plugin backup    update-check for %s on boxstart  - no updates avaible  - updates avaible  - with error  min (github version) (local version) (remaining query-limit: %(limit)s, limit-reset-time: %(time)s) Are you sure you want to restore the subsequent backup for plugin '%s'?

backup:
 Backup restore for plugin '%s' failed.

Maybe not all plugin files are in the following backup folder:

 Cancel Checks only the src folder for an update. Irrelevant updates outside of this folder are ignored, since only the src folder is updated anyway. Choose Directory: Choose directory Defines the location for the plugin backup (selection with OK). The path is supplemented by the local plugin version number and date/time. Error

No github update info could be determined. Error

github update info could not be determined. GithubPluginUpdater GithubPluginUpdater - update info GithubPluginUpdater Setup  Info only on updates No github update info could be determined. No update info for %s could be found. OK Plugins have been updated!
Do you want to restart the GUI now? Should the curl package be installed? Should the curl package be uninstalled? The latest version is already being used!                        
  The update could not be started!

The curl package must first be installed.

The curl package can be installed in the plug-in using the menu button via the entry 'Install curl package on the box'!


it is possible via telnet with the following command:

 opkg install curl The warning before a github update on the possible consequences of such an update can be activated or deactivated here. There are 3 options for the update check. The most reliable option is the 'api call', which has an access restriction of 60 calls per hour. A relapse alternative can be chosen at api. There are not local github date values for all plugins that are used for version comparison.
Therefore, these plugins are automatically offered as an update. There are the following options for the first time to save a local github date:

1. if all plugins on the box are actually up to date, then the menu button can be used to select the option 'set the current github date for all plugins'

or

2. the respective plugins can be updated using the color button.

Afterwards all plugins should be displayed as current. Update-Info Updatecheck and Info on starting the box Warning:

Plugin versions in github are often still test versions and can cause certain problems after installation!

Therefore, only experienced users should update to a github version.

Should the github -Update start now? advanced github-update-infos for  advanced update-info for  advanced update-info for GithubPluginUpdater always api-call / commits-list api-call / normal website backup SerienRecorder database ...... backup local version to: check on boxstart (also on GUI-Restart and start from Idle) for updates and show a message (none/only on updates/always). On 'always' show a message also if is not updates avaible. check only the src-folder close plugin commits-list copy SerienRecorder database ...... copy backup files ...... create a backup from the local plugin before update the guthub-version. create a backup of the plugin before update daily delete the current github date for all plugins every 12 hours every 6 hours force update for  forced update for  github version:  github-date:  github-versions loaded hourly install curl-package on the box installed version after restore backup: installed version before restore backup: last update-info for  load github-versions ...
 local version:    local versions was loaded menu menu GithubPluginUpdater menu restore plugin backup monthly no no backups found for the plugin '%s'. none of the possible plugins are installed on the box.
a backup restore is therefore not possible. normal website open the plugin-menu option to check for github-updates / alternative reload github-data remove curl-package from the box restore backup for %s restore backup for GithubPluginUpdater restore backup for the plugin - restore plugin backup select backup for the plugin '%s' set after how many seconds the update-info-window is closed (1-20 seconds, 0 = wait for key-press) set if you want to check for updates for this plugin on box-start. set the check-interval of AutoUpdateCheck on boxstart. Within the interval there is no renewed update check when the box is started. set the current github date for all plugins set the default answer to the question to open the GithubPluginUpdaters. on 'no' the plugin is not open automaically on timeout of the question. setup show on update-info an additioal question, if you want to open directly the GithubPluginUpdater. show update info show warning before a github update state: to reload the github-versions press 'OK'
Keys 1-4 to show last github-update-info update check for GithubPluginUpdater:
 update for  update github-versions update-check for GithubPluginUpdater update-check for GithubPluginUpdater


load data ... update-info for  version:  weekly yes Project-Id-Version: Enigma2 GithubPluginUpdater
Report-Msgid-Bugs-To: 
PO-Revision-Date: 2022-02-26 19:47+0100
Last-Translator: 
Language-Team: 
Language: de_DE
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
X-Poedit-Basepath: ../../..
X-Poedit-SourceCharset: UTF-8
X-Generator: Poedit 2.4.3
X-Poedit-SearchPath-0: .
 


Exit-Taste zum Beenden 

Soll das github-Update jetzt gestartet werden? 

Soll das Update jetzt gestartet werden?
 

Exit-Taste zum Abbrechen 
  installiere aktuelle Github-Version...... 
  installierte Version nach dem Update: 
  installierte Version vor dem Update: 
  lade aktuelle Version von Github...... 
 = GithubPluginUpdater = 

  >>> es liegen für folgende Plugins Updates vor !!! <<<
  %s


  zum Update den GithubPluginUpdater öffnen 
 = GithubPluginUpdater = 

  >>> es liegen für folgende Plugins Updates vor !!! <<<
  %s


Soll der GithubPluginUpdater geöffnet werden? 
 = GithubPluginUpdater = 

  keine Plugin-Updates gefunden 
... weitere Infos in der erweiterten Updatinfo ... 
Es existiert eine neuere Version!
 
Die erweiterte Update-Info konnte nicht geladen werden.
Das stündliche Limit für github-Abfragen wurde erreicht!!
 
aktuelle Zeit:     	   
Fehler bei der Updateprüfung 
für weitere Update-Infos bitte die github-Website besuchen.
 
Limit-Reset-Zeit: 	   
Lade Update-Info...
 
Abfrage-Limit pro Stunde:	   
Restliches Abfrage-Limit:	   
Wartezeit bis Reset: 	          Antwort für Frage steht standardmäßig auf:    erweiterte Update-Info mit Frage zum Öffnen des Plugins    Anzeigedauer für Update-Info-Fenster (in Sek)    Intervall für AutoUpdateCheck beim Start der Box    Speicherort für das Plugin-Backup    Update-Check für %s bei Box-Start  - keine Updates vorhanden  - Updates vorhanden  - mit Fehler  min (github Version) (lokale Version) (Rest Abfrage-Limit: %(limit)s, Limit-Reset-Time: %(time)s) Soll das nachfolgende Backup für das Plugin '%s' wirklich wiederhergestellt werden?

Backup:
 Die Backup-Wiederherstellung für das Plugin '%s' ist fehlgeschlagen

Möglicherweise befinden sich nicht alle Plugin-Dateien im nachfolgenden Backup-Ordner:

 Abbrechen Prüft nur den src-Ordner auf ein Update. Dabei werden unrelevante Updates außerhalb dieses Ordners ignoriert, da eh nur der src-Ordner geupdatet wird. wähle das Verzeichnis: wähle das Verzeichnis Legt den Ort für das Plugin-Backup fest (Auswahl mit OK). Der Pfad wird noch durch die lokale Plugin-Versionsnummer und Datum/Zeit ergänzt. Error

Es konnte keine github-Update-Info ermittelt werden. Error

Es konnte keine github-Update-Info ermittelt werden. GithubPluginUpdater GithubPluginUpdater - Updateinfo GithubPluginUpdater Setup  Info nur bei Updates Es konnte keine github-Update-Info ermittelt werden. Es konnte keine Updateinfo für %s gefunden werden. OK Es wurden Plugins aktualisiert!
Soll jetzt ein GUI-Neustart durchgeführt werden? Soll das curl-Paket installiert werden? Soll das curl-Paket deinstalliert werden? Es wird bereits die aktuellste Version genutzt!                        
  Das Update konnte nicht gestartet werden!

Es muss erst das curl-Paket installiert werden.

Das curl-Paket kann im Plugin per Menü-Taste über den Eintrag 'curl-Paket auf der Box installieren' installiert werden!


per Telnet geht es z.B. mit folgendem Befehl:

 opkg install curl Der Warnhinweis vor einem github-Update zu den möglichen Folgen eines solchen Updates kann hier aktiviert bzw. deaktiviert werden. Es gibt 3 Varianten zur Update-Prüfung. Am zuverlässigstens ist die Variante 'api-Abruf', welche eine Zugriffsbeschränkung von 60 Abrufen pro Stunde hat. Bei api kann eine Rückfall-Alternative gewählt werden. Es existieren nicht für alle Plugins lokale github-Datumswerte, die zum Versionsvergleich genutzt werden.
Daher werden diese Plugins automatisch als Update angeboten. Es gibt folgende Möglichkeiten erstmals ein lokales github-Datum zu speichern:

1. wenn alle Plugins auf der Box tatsächlich aktuell sind, dann kann per Menü-Taste die Option 'setze für alle Plugins das aktuelle github-Datum' gewählt werden

oder

2. die jeweiligen Plugins können per Farb-Taste aktualisiert werden.

Danach sollten alle Plugins als aktuell angezeigt werden. Update-Info Updatecheck und Info beim Start der Box Warnhinweis:

Plugin-Versionen im github sind oft noch Test-Versionen und können gewisse Probleme nach der Installation verursachen!

Daher sollten nur erfahrene User ein solches Update auf eine github-Version durchführen.

Soll das github-Update jetzt gestartet werden? erweiterte github-Update-Info für  erweiterte Update-Info für  erweiterte Update-Info für GithubPluginUpdater immer api-Abruf / commits-Liste api-Abruf / normale Website sichere SerienRecorder Datenbank ...... sichere lokale Version in: Prüft beim Box-Start (auch GUI-Neustart und Start aus dem Idle) auf Updates und gibt eine Meldung aus (nein/nur bei Updates/immer). Bei 'immer' kommt auch eine Info-Meldung, dass kein Update verfügbar ist. Prüfe nur den src-Ordner Plugin beenden commits-Liste kopiere SerienRecorder-Datenbank ...... kopiere Backup-Dateien ...... Legt vor dem Update der Github-Version ein Backup des lokalen Plugins an. erzeuge ein Backup des Plugins vor dem Update täglich lösche für alle Plugins das aktuelle github-Datum alle 12 Stunden alle 6 Stunden Erzwinge Update für  Zwangs-Update für  github Version:  github-Datum:  github-Versionen geladen stündlich curl-Paket auf der Box installieren installierte Version nach der Backup-Wiederherstellung: installierte Version vor der Backup-Wiederherstellung: letzte Update-Info für  lade github-Versionen ...
 lokale Version:   lokale Versionen wurden geladen Menü Menü GithubPluginUpdater Menü Plugin-Backup wiederherstellen monatlich nein keine Backups für das Plugins '%s' gefunden. keines der möglichen Plugins ist auf der Box installiert.
Eine Backup-Wiederherstellung ist dadurch nicht möglich. normale Website Plugin-Menü öffnen Variante zum Prüfen auf github-Updates / Alternative Neuladen der github-Daten curl-Paket auf der Box deinstallieren Backup für %s wiederherstellen Backup für GithubPluginUpdater wiederherstellen Backup-Wiederherstellung für das Plugin - Plugin-Backup wiederherstellen Backup für das Plugin '%s' auswählen Legt fest, nach wieviel Sekunden das Update-Info-Fenster automatisch geschlossen wird (1-20 Sek., 0 = wartet auf Tastendruck) Legt fest, ob für das Plugin beim Box-Start eine Update-Prüfung durchgeführt werden soll. Legt den Prüf-Intervall für den AutoUpdateCheck beim Start der Box fest. Innerhalb des Intervalls erfolgt kein erneuter Update-Check beim Start der Box. setze für alle Plugins das aktuelle github-Datum Legt fest, welche Antwort für die Frage zum Öffnen des GithubPluginUpdaters standardmäßig vorausgewählt sein soll. Bei 'nein' öffnet sich das Plugin bei Zeitablauf der Frage nicht automatisch. Einstellungen Zeigt beim Update-Hinweis zusätzlich eine Frage, ob man den GithubPluginUpdater direkt direkt öffnen möchte. Show Update-Info Warnhinweis vor einem github-Update anzeigen Status: zum Neuladen der github-Versionen 'OK' drücken
Tasten 1-4 zur Anzeige der letzten Github-Update-Info Updateprüfung für GithubPluginUpdater:
 Update für  github-Versionen updaten Updateprüfung für GithubPluginUpdater Updateprüfung für GithubPluginUpdater


lade Daten ... Update-Info für  Version:  wöchentlich ja 