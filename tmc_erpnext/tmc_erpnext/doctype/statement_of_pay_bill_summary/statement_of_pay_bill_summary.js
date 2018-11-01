// Copyright (c) 2018, Frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on('Statement Of Pay Bill Summary', {

	onload : function(frm){
		frm.disable_save();
		frm.trigger('set_print_button');
	},

	set_print_button : frm => {

		const print_wrapper = frm.fields_dict.print.$wrapper;

		var print_button = $('<div>\
			<button class="btn btn-primary btn-print-report">Print</button>\
			</div>').appendTo(print_wrapper);

		frappe.query_report = new frappe.views.QueryReport({
			parent: print_wrapper,
		});

		print_button.find(".btn-print-report")
		.on("click",function() {

			frappe.call({
				"method" : "tmc_erpnext.tmc_erpnext.doctype.statement_of_pay_bill_summary.statement_of_pay_bill_summary.get_data",
				"args" : {
					company : frm.doc.company,
					department : frm.doc.department,
					branch : frm.doc.branch,
					period : frm.doc.period
				},
				"callback" : function(r){

					let data = r.message

					frappe.ui.get_print_settings(false, print_settings => {

						frappe.render_grid({
							template: 'statement_of_pay_bill_summary',
							title: __(this.doctype),
							print_settings: print_settings,
							data: data,
							columns: ["Sr_No","Sub<br>Department<br>Bill_Number", "Gross<br>Deduction", "RD<br>IT<br>PF_Loan",
							"PF<br>ADD_PF<br>DCPS", "DCPS_R<br>LEVY<br>CCTD", "SOCIETY<br>TEACH_SOC<br>HBA1",
							"HBA2<br>HBA3<br>HBA4","Scoot_ADV<br>FESTIVAL<br>Comp_ADV","OTH_ADV<br>LIC<br>BANK_L",
							"POTAGI<br>GIS<br>Serv_Chg","AUDIT_R<br>FINE<br>REC_LWP","EXTRA_REC<br>FLAG_DAY<br>ADHOC",
							"1_DAY<br>MAHASANG<br>LABW","MAHAR<br>LABW_ADV<br>MOB_ADV","PST1<br>DED_OTH<br>OOD",
							"PT_REC<br>MEDI_ADV<br>LAP_ADV","CA_ADV<br>PTAX_STAMP<br>TMCFUND","NET_PAY"]
						});
					});
				}
			});
		});
	}

});
