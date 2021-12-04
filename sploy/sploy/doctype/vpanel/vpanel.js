// Copyright (c) 2021, gross innovate and contributors and contributors
// For license information, please see license.txt

frappe.ui.form.on('VPanel', {
	setup: function (frm){
		frm.disable_save();
	},
	onload_post_render: function (frm){
		frm.disable_save();
		frm.call('get_usage_info').then( r => {
			frm.refresh();
		})
	},
	refresh: function(frm) {
		frm.disable_save();
		
	}
});
