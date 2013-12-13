## Usage:

`./pyurtstat.py SERVER[:PORT] -c [OPTIONS]`

    SERVER:		Required, ip or hostname of urbanterror server.
    PORT:		Optional, port of urbanterror server. Default 27960 used if not specified.
    OPTIONS:	Optional, comma separated list of server options you want to retrive and display


## Example:

1. Simple Usages 


        $ python pyurtstat.py 209.190.50.170 
        
        -------------------------
        209.190.50.170:27960
        ------------------------- 

		Name                           	 Ping 	 Kills
		------------------------------ 	 ---- 	 -----
		ng                             	 140  	 35   
		painpain                       	 162  	 2    
		[EH]Doktar                     	 300  	 38   
		Assassin-9mm                   	 200  	 38   
		Stingray76                     	 148  	 28   
		hew_UrT_Player                 	 221  	 1    



2. Empty server


        $ python pyurtstat.py urt.sarimkhan.com:2222

		-------------------------
		urt.sarimkhan.com:2222
		-------------------------
		
		No one is playing on the server at this moment. 
		
3. Querying single config option
		
		$ python pyurtstat.py urtbd.com:2222 -c g_redwave,g_bluewave,Admin
		
		-------------------------
		urtbd.com:2222
		-------------------------
		
		Config                         	 Value                         
		------------------------------ 	 ------------------------------
		g_redwave                      	 15                            
		g_bluewave                     	 15                            
		Admin                          	 MegaMind   
		
4. Querying all options     
		
		$ python pyurtstat.py urtbd.com:2222 -c all
		
		-------------------------
		urtbd.com:2222
		-------------------------
		
		Config                         	 Value                         
		------------------------------ 	 ------------------------------
		protocol                       	 68                            
		g_enableDust                   	 0                             
		g_enableBreath                 	 0                             
		g_followstrict                 	 1                             
		g_respawndelay                 	 7                             
		g_bombdefusetime               	 10                            
		g_cahtime                      	 60                            
		g_survivorrule                 	 0                             
		Email                          	 xxx@xxx.xx                    
		g_gametype                     	 3                             
		g_suddendeath                  	 1                             
		g_redwave                      	 15                            
		g_armbands                     	 2                             
		sv_floodprotect                	 1                             
		sv_minRate                     	 0                             
		gamename                       	 q3ut4                         
		g_swaproles                    	 0                             
		g_maxGameClients               	 0                             
		version                        	 ioq3 1.35urt linux-i386 Jan 28 2009
		g_gear                         	 0                             
		g_modversion                   	 4.1                           
		g_hotpotato                    	 2                             
		g_bluewave                     	 15                            
		g_allowvote                    	 1073741823                    
		sv_minPing                     	 0                             
		Admin                          	 MegaMind                      
		sv_privateClients              	 0                             
		g_roundtime                    	 3                             
		sv_dlURL                       	 fallin-angels.org             
		g_waverespawns                 	 0                             
		g_deadchat                     	 1                             
		sv_maxclients                  	 30                            
		sv_hostname                    	 Urban Terrorists urt server   
		g_needpass                     	 0                             
		fraglimit                      	 0                             
		g_maxrounds                    	 0                             
		mapname                        	 ut4_kingdom                   
		g_warmup                       	 15                            
		g_bombexplodetime              	 40                            
		capturelimit                   	 0                             
		dmflags                        	 0                             
		g_survivor                     	 0                             
		g_matchmode                    	 0                             
		g_enablePrecip                 	 0                             
		timelimit                      	 10                            
		sv_allowdownload               	 0                             
		g_friendlyfire                 	 0                             
		g_antilagvis                   	 0                             
		sv_maxRate                     	 0                             
		sv_maxPing                     	 0                             
