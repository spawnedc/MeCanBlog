var mcb = {

	log: function(message, logtype) {
		if(logtype===undefined) {
			logtype = 'log';
		}
		console[logtype](message);
	},

	info: function(message) {
		mcb.log(message, 'info');
	},

	warn: function(message) {
		mcb.log(message, 'warn');
	},

	error: function(message) {
		mcb.log(message, 'error');
	},

	init: function() {
		mcb.info('Init mcb');
	}

}

mcb.init();
