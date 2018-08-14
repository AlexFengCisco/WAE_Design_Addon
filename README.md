# WAE_Design_Addon Integration with 3rd party Applications

## Addon sample format and sample code for reference 

---- 
>Sample code to make WAE Design addon integration,
> addon.txt design format and style for addon,
 valid_options is variable constrain ,
 python code to handle options and design content , you may integrate WAE Design addon to any 3rd party applications ,NSO or other auyonation tools

 >Exec python code by invoke WAE Design addon options , observe the result from WAE log window.
----

## Result From WAE log window as following
    
    14:44:26 Notice [30]: Run Scripts started.
    14:44:51 Notice [30]: -mate-version*****
    14:44:51 Notice [30]: -out-file*****
    14:44:51 Notice [30]: -pdf-report-file*****
    14:44:51 Notice [30]: -plan-file*****
    14:44:51 Notice [30]: -report-dir*****
    14:44:51 Notice [30]: -report-file*****
    14:44:51 Notice [30]: -return-config-file*****
    14:44:51 Notice [30]: -Option3*****
    14:44:51 Notice [30]: -Option1*****
    14:44:51 Notice [30]: -Option2*****
    14:44:51 Notice [30]: ----------PRINT OPTIONS FROM ADDON__________________________________________________________
    14:44:51 Notice [30]: report-dir :/var/folders/35/vkjljcjn5t994nllqfv_7mm80000gn/T/run_script_report_dir_30628/PushLSPSIDListtoNSO
    14:44:51 Notice [30]: pdf-report-file :/private/var/folders/35/vkjljcjn5t994nllqfv_7mm80000gn/T/addonPdfDir_alfeng/runscript_report_f30628.pdf
    14:44:51 Notice [30]: report-file :/private/var/folders/35/vkjljcjn5t994nllqfv_7mm80000gn/T/runscript_report.30628.txt
    14:44:51 Notice [30]: mate-version :7.1
    14:44:51 Notice [30]: return-config-file :/private/var/folders/35/vkjljcjn5t994nllqfv_7mm80000gn/T/run_script_gui_config.30628.txt
    14:44:51 Notice [30]: plan-file :/private/var/folders/35/vkjljcjn5t994nllqfv_7mm80000gn/T/runscript_input.30628.pln
    14:44:51 Notice [30]: out-file :/var/folders/35/vkjljcjn5t994nllqfv_7mm80000gn/T/DARE-DSJopt-out.txt
    14:44:51 Notice [30]: Option1 :/var/folders/35/vkjljcjn5t994nllqfv_7mm80000gn/T/e30628.txt
    14:44:51 Notice [30]: Option2 :/var/folders/35/vkjljcjn5t994nllqfv_7mm80000gn/T/F30628.txt
    14:44:51 Notice [30]: Option3 :true
    14:44:51 Notice [30]: ____________PRINT OPTION1 TAB CONTENT _______________________________________________________
    14:44:51 Notice [30]: <Nodes>
    14:44:51 Notice [30]: Name  Site    Function    Protected   Active  Type    ISISArea    AS  BGPID   SID AvoidTransit    TotalTraffSim   SrcTraffSim DestTraffSim    TransitTraffSim SrcTraffMeas    DestTraffMeas   LSPCount    ECMPMax FailureImpact   FIInterface IPAddress   SiteLongitude   SiteLatitude    X   Y   SiteX   SiteY   Shown   InterfaceCount  Description UUID    Vendor  Model   OS  IPManage    CostInitial CostPerPeriod   LastTemplateUpdate  Longitude   Latitude    Failed  Operational Tags    SiteTags    ASTags  NetIntSNMP_Error    NetIntSource    NetIntRE0CPU1m  NetIntRE0CPU5m  NetIntRE0Mem    NetIntRE1CPU1m  NetIntRE1CPU5m  NetIntRE1Mem
    14:44:51 Notice [30]: R3        core    F   T   physical        1   8.8.8.3 16043   No  0.00    0.00    0.00    0.00            1   1           8.8.8.3         -50.00  50.00           T   2           Cisco       IOS 6.4.1   8.8.8.3 0.00    0.00                F   T                                           
    14:44:51 Notice [30]: R4        core    F   T   physical        1   8.8.8.4 16044   No  0.00    0.00    0.00    0.00                0           8.8.8.4         50.00   -50.00          T   2           Cisco       IOS 6.4.1   8.8.8.4 0.00    0.00                F   T                                           
    14:44:51 Notice [30]: R2        core    F   T   physical        1   8.8.8.2 16042   No  0.00    0.00    0.00    0.00            1   0           8.8.8.2         -50.00  -50.00          T   2           Cisco       IOS 6.4.1   8.8.8.2 0.00    0.00                F   T                                           
    14:44:51 Notice [30]: R5        core    F   T   physical        1   8.8.8.5 16045   No  0.00    0.00    0.00    0.00                            8.8.8.5         50.00   50.00           T   2           Cisco       IOS 6.4.1   8.8.8.5 0.00    0.00                F   T                                           
    14:44:51 Notice [30]: ____________PRINT OPTIN 2 TAB CONTENT _______________________________________________________
    14:44:51 Notice [30]: <SegmentLists>
    14:44:51 Notice [30]: Source    Name
    14:44:51 Notice [30]: R3    SL
    14:44:51 Notice [30]: _____________________PRINT R3 INTERFACES FROM CURRENT ACTIVE PLAN FILE__________________________________________
    14:44:51 Notice [30]: interface GigabitEthernet0/0/0/3 on node R3
    14:44:51 Notice [30]: ------------------------
    14:44:51 Notice [30]: interface GigabitEthernet0/0/0/2 on node R3
    14:44:51 Notice [30]: ------------------------
    14:44:51 Notice [30]: _____________________PRINT SEGMENT LIST FORM CURRENT ACTICE PLAN FILE________________________________________
    14:44:51 Notice [30]: SegmentListManager[sl{sl_R3_t200_1|R3}, sl{SL|R3}]
    14:44:51 Notice [30]:  THIS IS A DRY RUN
    14:44:51 Notice [30]: No text output from running   /Users/alfeng/Documents/Cisco_Products/NSO/WAE/WAE-Design-k9-7.1.1-MacOSX-x86_64/addons/CCBAddon/PushLSPSIDListtoNSO
    14:44:51 Notice [30]: Run Scripts finished.
