#! /usr/bin/env python

import sys
sys.path[:0] = [ "/opt/mx/lib/mp" ]

import Mp
import MpCa

input_signal_name = "i0"
output_pv_name    = "ID18:SteeringGoodness"
timer_name        = "joerger_timer"

measurement_time = 1.0		# in seconds

print "Setting up.  Please wait..."

mx_database = Mp.setup_database( "/opt/mx/etc/mxmotor.dat" )

input_signal = mx_database.get_record( input_signal_name )

output_pv    = MpCa.PV( output_pv_name )

timer        = mx_database.get_record( timer_name )

print "Copying steering signal from '%s' to '%s' using timer '%s'" % \
	( input_signal_name, output_pv_name, timer_name )

while 1:
	timer.clear()

	timer.start( measurement_time )

	while 1:
		busy = timer.is_busy()

		if ( busy == 0 ):
			break
	
	input = input_signal.read()

	print "%f" % (input)

	output_pv.caput( input )
