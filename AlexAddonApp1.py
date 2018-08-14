'''

Sample code to make WAE Design addon integration,
addon.txt design format and style for addon,
valid_options is variable constrain ,
python code to handle options and design content , you may integrate WAE Design addon to any 3rd party applications ,NSO or other auyonation tools

Exec python code by invoke WAE Design addon options , observe the result from WAE log window.


Result From WAE log window as following

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
14:44:51 Notice [30]: Name	Site	Function	Protected	Active	Type	ISISArea	AS	BGPID	SID	AvoidTransit	TotalTraffSim	SrcTraffSim	DestTraffSim	TransitTraffSim	SrcTraffMeas	DestTraffMeas	LSPCount	ECMPMax	FailureImpact	FIInterface	IPAddress	SiteLongitude	SiteLatitude	X	Y	SiteX	SiteY	Shown	InterfaceCount	Description	UUID	Vendor	Model	OS	IPManage	CostInitial	CostPerPeriod	LastTemplateUpdate	Longitude	Latitude	Failed	Operational	Tags	SiteTags	ASTags	NetIntSNMP_Error	NetIntSource	NetIntRE0CPU1m	NetIntRE0CPU5m	NetIntRE0Mem	NetIntRE1CPU1m	NetIntRE1CPU5m	NetIntRE1Mem
14:44:51 Notice [30]: R3		core	F	T	physical		1	8.8.8.3	16043	No	0.00	0.00	0.00	0.00			1	1			8.8.8.3			-50.00	50.00			T	2			Cisco		IOS 6.4.1	8.8.8.3	0.00	0.00				F	T											
14:44:51 Notice [30]: R4		core	F	T	physical		1	8.8.8.4	16044	No	0.00	0.00	0.00	0.00				0			8.8.8.4			50.00	-50.00			T	2			Cisco		IOS 6.4.1	8.8.8.4	0.00	0.00				F	T											
14:44:51 Notice [30]: R2		core	F	T	physical		1	8.8.8.2	16042	No	0.00	0.00	0.00	0.00			1	0			8.8.8.2			-50.00	-50.00			T	2			Cisco		IOS 6.4.1	8.8.8.2	0.00	0.00				F	T											
14:44:51 Notice [30]: R5		core	F	T	physical		1	8.8.8.5	16045	No	0.00	0.00	0.00	0.00							8.8.8.5			50.00	50.00			T	2			Cisco		IOS 6.4.1	8.8.8.5	0.00	0.00				F	T											
14:44:51 Notice [30]: ____________PRINT OPTIN 2 TAB CONTENT _______________________________________________________
14:44:51 Notice [30]: <SegmentLists>
14:44:51 Notice [30]: Source	Name
14:44:51 Notice [30]: R3	SL
14:44:51 Notice [30]: _____________________PRINT R3 INTERFACES FROM CURRENT ACTIVE PLAN FILE__________________________________________
14:44:51 Notice [30]: interface GigabitEthernet0/0/0/3 on node R3
14:44:51 Notice [30]: ------------------------
14:44:51 Notice [30]: interface GigabitEthernet0/0/0/2 on node R3
14:44:51 Notice [30]: ------------------------
14:44:51 Notice [30]: _____________________PRINT SEGMENT LIST FORM CURRENT ACTICE PLAN FILE________________________________________
14:44:51 Notice [30]: SegmentListManager[sl{sl_R3_t200_1|R3}, sl{SL|R3}]
14:44:51 Notice [30]:  THIS IS A DRY RUN
14:44:51 Notice [30]: No text output from running
/Users/alfeng/Documents/Cisco_Products/NSO/WAE/WAE-Design-k9-7.1.1-MacOSX-x86_64/addons/CCBAddon/PushLSPSIDListtoNSO
14:44:51 Notice [30]: Run Scripts finished.


Created on Aug 7, 2018

@author: Alex Feng 

alfeng@cisco.com
'''

import sys
import re
import os
from com.cisco.wae.opm.network import open_plan
import Ice
from alex_input_options import VALID_OPTIONS as valid_options


ADDON_NAME = 'Alex Addon Application 1'
VERSION = '0.0.8'
_FLAG_RE = re.compile(r'\A--?([-\w]+)\Z')
_HELP_RE = re.compile(r'\A-h(?:elp)?\Z', re.IGNORECASE)
_VERSION_RE = re.compile(r'\A-v(?:ersion)?\Z', re.IGNORECASE)

p1 = re.compile(r'<NetIntPrefixSIDs>') 
p11 = re.compile("<ColumnData>")
p2 = re.compile(r'<SegmentListHops>')
p22 = re.compile(r'<TrafficLevels>')

def main():
	'''
	main()
	'''
	# Start by parsing the options
	options = get_cli_options()

	#get options variable 
	print "----------PRINT OPTIONS FROM ADDON__________________________________________________________"
	print "report-dir :"+options['report-dir']
	print "pdf-report-file :"+options['pdf-report-file']
	print "report-file :"+options['report-file']
	print "mate-version :"+options['mate-version']
	print "return-config-file :"+options['return-config-file']
	print "plan-file :"+options['plan-file']
	print "out-file :"+options['out-file']
	print "Option1 :"+options["Option1"]
	print "Option2 :"+options["Option2"]
	print "Option3 :"+options["Option3"]

	#get option 1 content from selected current table 
	print "____________PRINT OPTION1 TAB CONTENT _______________________________________________________"
	f_option1=open(options['Option1'])
	print f_option1.read()
	f_option1.close()
	
	#get option 2 content from seleted current table
	print "____________PRINT OPTIN 2 TAB CONTENT _______________________________________________________"
	f_option2=open(options['Option2'])
	print f_option2.read()
	f_option2.close()
    
    #open current plan file and fetch content
	with open_plan(options['plan-file']) as network:
		model = network.model
		# Do stuff with the network model ...
		node = model.nodes['R3']
		print "_____________________PRINT R3 INTERFACES FROM CURRENT ACTIVE PLAN FILE__________________________________________"
		for interface in node.interfaces:
			print 'interface %s on node %s'%(interface.name,node.name)
			print '------------------------'
		
		print "_____________________PRINT SEGMENT LIST FORM CURRENT ACTICE PLAN FILE________________________________________"
		Segment_list=model.segment_lists
		print Segment_list
	
	'''
	Do what you want to handle current plan file and 
	push the result as json content to call NSO RESP API
	
	'''	
	if options['Option3']=='true':
		print " THIS IS A DRY RUN"
	
	return 0


def get_cli_options():
	'''
		Captures and validates the CLI options
	'''
	options = process_argv()
	#options = validate_options(options)
	return options

def process_argv():
	'''
		Returns the cli arguments in a dictionary
	'''
	argv = list(sys.argv)
	options = {}
	argv.pop(0)
	while len(argv) > 0:
		item = argv.pop(0)
		print item+"*****"
		next_item = argv.pop(0)
		options[re.sub(r'^-', '', item)] = next_item
		'''
		if item in valid_options:
			if _VERSION_RE.match(item):
				print VERSION
				sys.exit()
			if _HELP_RE.match(item) is not None:
				do_help()
			if _FLAG_RE.match(item):
				try:
					next_item = argv.pop(0)
				except Exception:
					do_help()
				if next_item is not None:
					if _FLAG_RE.match(next_item) is None:
						options[re.sub(r'^-', '', item)] = next_item
					else:
						do_help()
		else:
			print "Warning[20]: "+item+" is not a valid option"
			do_help()
        '''
	return options

def validate_options(options):
	'''
		Validates the CLI options
	'''
	# Ensure we fill out any defined defaults
	for option in valid_options.keys():
		if 'default' in valid_options[option]:
			default = valid_options[option]['default']
			option = re.sub(r'^-', '', option)
			if option not in options:
				options[option] = default

	# Ensure we check our allowed values
	for option in valid_options.keys():
		if 'allowed' in valid_options[option]:
			allowed_values = valid_options[option]['allowed']
			option = re.sub(r'^-', '', option)
			if option in options:
				if options[option] not in allowed_values:
					do_help()

	# Ensure we have our required options
	for option in valid_options.keys():
		if 'REQUIRED' in valid_options[option]:
			if valid_options[option]['REQUIRED'] == 1:
				option = re.sub(r'^-', '', option)
				if option not in options:
					do_help()

	return options



def do_help():
	'''
		Shows a help screen
	'''
	program_name = os.path.basename(sys.argv[0])
	print program_name + " (" + VERSION +")"
	print "Usage"
	print "\t" + program_name + " [general flags] <required flags> [optional flags]"
	print ""
	print ADDON_NAME
	print "Required Flags:"
	print_flags(valid_options, 1)
	print "Optional Flags:"
	print_flags(valid_options, 0)
	sys.exit()

def print_flags(print_options, required_flag):
	'''
		Prints option flags
	'''
	for option in print_options.keys():
		if 'hidden' in print_options[option]:
			continue
		if print_options[option]['REQUIRED'] == required_flag:
			buf = "%20s %10s                    :  %s" % (option, print_options[option]['type'], print_options[option]['description'])
			print buf
			if 'allowed' in print_options[option]:
				allow = ", ".join(print_options[option]['allowed'])
				buf = "%20s %10s                    :      Allowed values: %s" % (" ", " ", allow)
				print buf
	return

if __name__ == '__main__':
	try:
		sys.exit(main())
	except Exception as exception:
		import traceback
		print traceback.print_exc()
		sys.stderr.write('Fatal [0]: '+str(exception)+'\n')
