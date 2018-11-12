// Copyright (c) 2018, Frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on('ECS Report For RBI', {
	onload : function(frm){
		frm.disable_save();
	},
	payment_date: (frm) => {
		frm.add_custom_button("Print Report", function() {
			frm.call({
				method: "generate_report_and_get_url",
				doc: frm.doc,
				callback: function(r) {
					const a = document.createElement('a');
					a.href = r.message;
					a.target = '_blank'
					a.download = "ecs-report-"+frm.doc.payment_date	
					a.click();
				}
			});
		});
	},
	refresh: function(frm) {
	}
});
