��    �      T  �   �      `     a  -   y  '   �     �  '   �  "     #   0  )   T  �   ~  �   	  5   �  /   �     �  a        r     �  8   �     �     �     	     #     >  -   U  8   �  .   �  *   �  )     "   @     c     y     �     �     �     �  >   �  Q   �  h   Q     �  �   �     O     a  �   r  1   �  2   /     b  !   v     �     �     �     �  *   �  %        '  >   *  %   i  '   �  C   �    �  w     �   �    <     C  (   O  �   x  !   Y     {  ,   �     �     �     �  %   �     !  �   :     �     	       #   #     G  G   `  +   �     �  .   �     	          &     8     K     \     j     �     �  '   �  (   �     �          )     ;     U     Z     s     �     �  %   �  b   �     "     1  0   F     w      �     �  &   �     �        !      b   @   B   �   �   �   +   k!  �   �!     ("  `   ."     �"  #   �"     �"  Q   �"  &   #     D#     P#  $   g#  4   �#     �#  	   �#     �#     �#  �  �#     �%  %   �%     �%     �%  3   
&  ,   >&  0   k&  4   �&  �   �&  z   ]'  >   �'  <   (  !   T(  X   v(     �(  *   �(  D   )     V)  ,   q)     �)     �)     �)  +   �)  @   *  /   T*  -   �*  3   �*  4   �*      +     <+     Y+     g+     l+     ~+  >   �+  ?   �+     ,  	   �,  �   �,     ^-     x-  �   �-  I   +.  E   u.     �.  (   �.  !   �.     /     8/  	   >/  @   H/  &   �/     �/  (   �/     �/      �/  ;   0  =  W0  }   �1  �   2  f  �2     N5  1   a5    �5  '   �6      �6  >   �6      7     '7     >7  1   Y7      �7  �   �7      �8     �8     �8  0   �8      �8  O   9  /   l9     �9  4   �9     �9  
   �9     �9     :     ,:     >:     L:     e:     n:  .   �:  0   �:     �:  (   
;     3;  $   G;     l;     q;     �;     �;     �;     �;  a   �;     5<     G<  ;   a<     �<     �<     �<  *   �<  +   =  !   H=  (   j=     �=  I   >  �   ]>  4   �>  �    ?     �?  d   �?     /@  3   K@     @  p   �@  2   �@     *A     =A  0   [A  M   �A     �A  
   �A     �A     	B     4      O   c   �       8   ;             &       y          G          $   _   v   ~      x   :   @   �              �                     !   F   I   e   [   U   n   '   Z       ?   =   {           q                   /       3   g   r   H       �       i       b          6   w   +   D      T   
   9   |   �   m   �   t   	      ]      k   5   (   "       L      }      *          B   �   <   -           P   o   d   W       Q       .       Y      M       V      2                   >   1   J   ,   0   a                               `          u   C   )   h   %   X                 A          S   E      f   ^       p               �             N   l   \   R   s   j   K   z   #   7    


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

github update info could not be determined. GithubPluginUpdater GithubPluginUpdater - update info GithubPluginUpdater Setup  Info only on updates Input Message No github update info could be determined. No update info for %s could be found. OK Plugins have been updated!
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


load data ... update-info for  version:  weekly yes Project-Id-Version: GithubPluginUpdater v1.7.0
PO-Revision-Date: 2022-02-26 23:16+0100
Last-Translator: Dario Croci <spaeleus@croci.org>
Language-Team: DREAM-ELITE <https://www.dream-elite.net>
Language: it_IT
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
Plural-Forms: nplurals=2; plural=(n != 1);
X-Generator: Poedit 3.0.1
X-Poedit-Basepath: ../../..
X-Poedit-SearchPath-0: .
 


Tasto "EXIT" per chiudere 

Avviare l'aggiornamento github ora? 

Avviare l'aggiornamento?
 

Tasto "EXIT" per annullare 
Installazione versione github corrente in corso... 
  Versione installata dopo l'aggiornamento: 
  Versione installata prima dell'aggiornamento: 
Caricamento versione corrente da github in corso... 
 = GithubPluginUpdater = 

  >>> Sono presenti aggiornamenti per i seguenti plugin <<<
  %s


  Aprire GithubPluginUpdater per aggiornarli 
 = GithubPluginUpdater = 

  >>> Sono presenti aggiornamenti per i seguenti plugin <<<
  %s


Aprire GithubPluginUpdater? 
 = GithubPluginUpdater = 

  Nessun aggiornamento disponibile 
...info dettagliate nelle info di aggiornamento avanzate... 
È presente una nuova versione.
 
Impossibile caricare info avanzate.
Raggiunto il limite orario per le query su github.
 
Ora corrente:     	   
Errore nella verifica degli aggiornamenti 
Per maggiori info sugli aggiornamenti visitare il sito web github.
 
Ora reset del limite: 	   
Caricamento info aggiornamento in corso...
 
Limite query per ora:	 
Limite query residuo:	 
In attesa di reset: 	          Risposta predefinita alla richiesta:    Info aggiornamento avanzate con richiesta di aprire il plugin    Durata finestra info aggiornamenti (secondi)    Intervallo di AutoUpdateCheck su avvio box    Posizione di archiviazione dei backup dei plugin    Verificare aggiornamenti per %s all'avvio del box  - aggiornamenti non disponibili  - aggiornamenti disponibili  - con errori  min (versione github) (versione locale) (numero query residue: %(limit)s - ora reset limite: %(time)s) Ripristinare il backup successivo per il plugin "%s"?

Backup:
 Ripristino del backup per il plugin "%s" fallito.

Forse non tutti i file dei plugin sono nella seguente directory di backup:

 Annullare Verificare solo la directory src per gli aggiornamenti. Gli aggiornamenti irrilevanti al di fuori di questa directory verranno ignorati, poiché in ogni caso solo la cartella src sarà aggiornata. Selezionare la directory: Selezionare la directory Definire la posizione dei backup dei plugin ("OK" per selezionare). Il percorso verrà completato con il numero di versione locale del plugin e data/ora. Errore.

Impossibile determinare informazioni di aggiornamento su github. Errore

Impossibile determinare informazioni di aggiornamento github. GithubPluginUpdater GithubPluginUpdater - Info aggiornamenti Impostazioni GithubPluginUpdater  Info solo sugli aggiornamenti Input Messaggio Impossibile determinare informazioni di aggiornamento su github. Info aggiornamenti per %s non trovate. OK Plugin aggiornato.
Riavviare la GUI ora? Installare il pacchetto curl? Disinstallare il pacchetto curl? È già in uso l'ultima versione.                        
  Impossibile avviare l'aggiornamento.

È necessario preventivamente installare il pacchetto curl.

Il pacchetto curl può essere installato utilizzando la voce "Installare il pacchetto curl" raggiungibile con il tasto "MENU".


L'installazione è anche possibile via telnet con il seguente comando:

opkg install curl Qui è possibile attivare/disattivare un avviso prima di aggiornamenti github sulle possibili conseguenze di tali operazioni. Sono disponibili 3 opzioni di verifica aggiornamenti. L'opzione più affidabile è la "api-call", con una restrizione di accesso a 60 chiamate/ora. Con le api, è possibile selezionare un'alternativa di ripiego. Non sono disponibili valori di date locali github per tutti i plugin in uso per un confronto delle versioni.
Pertanto questi plugin sono offerti automaticamente come aggiornamento. Sono disponibili le seguenti opzioni per salvare una data locale di GitHub la prima volta :

1. Se tutti i plugin installati sono effettivamente aggiornati, il tasto "MENU" può essere utilizzato per selezionare l'opzione "Impostare la data github corrente per tutti i plugin"

oppure

2. I rispettivi plugin possono essere aggiornati usando il tasto colorato.

In seguito tutti i plugin dovrebbero essere visualizzati come correnti. Info aggiornamento Verificare aggiornamenti e info all'avvio del box Attenzione:

Le versioni presenti su github sono spesso sperimentali e potrebbero provocare problemi dopo l'installazione.

Pertanto solo utenti esperti dovrebbero effettuare l'aggiornamento a una versione github.

Eseguire comunque l'aggiornamento github ora? Info avanzate aggiornamenti github per  Info avanzate aggiornamento per  Informazioni di aggiornamento avanzate per GithubPluginUpdater Sempre api-call/Elenco commit api-call/Sito web standard Backup del database di SerienRecorder in corso... Backup della versione locale in: Verificare ad ogni avvio (compresi riavvi GUI e risvegli da idle) la presenza di aggiornamenti e mostrare un messaggio (mai/solo su aggiornamenti/sempre). Sempre mostrerà un messaggio anche in assenza di aggiornamenti. Verificare solo la directory src Chiudere il plugin Elenco commit Copia del database di SerienRecorder in corso... Copia file di backup in corso... Creare un backup del plugin locale prima di aggiornarlo con la versione github. Creare un backup del plugin prima di aggiornare Giornaliera Rimuovere la data github corrente per tutti i plugin Ogni 12 ore Ogni 6 ore Forzare l'aggiornamento per  Aggiornamento forzato per  Versione github:  data github:  Versione github caricata Ogni ora Installare il pacchetto curl Versione installata dopo il ripristino backup: Versione installata prima del ripristino backup: Ultime info aggiornamenti per  Caricamento versione GitHub in corso...
 Versione locale:    È stata caricata la versione locale Menu Menu GithubPluginUpdater Menu ripristino backup plugin Mensile No Nessun backup trovato per "%s". Nessuno dei plugin previsti risulta installato.
Un ripristino dal backup è pertanto impossibile. Sito web standard Aprire il menu del plugin Opzioni per la verifica di aggiornamenti github/alternative Ricaricare i dati github Disinstallare il pacchetto curl Rirpistinare backup per %s Ripristinare backup di GithubPluginUpdater Ripristino in corso del backup del plugin - Ripristinare un backup dei plugin Selezionare il backup per il plugin "%s" Impostare il ritardo della chiusura automatica della finestra info aggiornamenti (1-20 secondi - 0 = attendere pressione tasto) Impostare una verifica aggiornamenti per questo plugin all'avvio del box. Impostare l'intervallo verifiche di AutoUpdateCheck all'avvio. Durante questo intervallo non verranno ripetute verifiche sugli aggiornamenti. Impostare la data github corrente per tutti i plugin Impostare la risposta predefinita alla richiesta di apertura di GithubPluginUpdaters. "No" non aprirà automaticamente il plugin al timeout della richiesta. Impostazioni Mostrare su info aggiornamenti una richiesta aggiuntiva per aprire direttamente GithubPluginUpdater. Mostrare info aggiornamento Mostrare un avviso prima di un aggiornamento github Stato: Per ricaricare la versione github premere "OK".
Utilizzare i tasti 1-4 per mostrare le ultime info github-update Verificare aggiornamento per GithubPluginUpdater:
 Aggiornamento per  Aggiornare la versione github Verificare aggiornamenti per GithubPluginUpdater Verifica aggiornamenti per GithubPluginUpdater


Caricamento dati in corso... Info aggiornamento per  Versione:  Settimanale Sì 