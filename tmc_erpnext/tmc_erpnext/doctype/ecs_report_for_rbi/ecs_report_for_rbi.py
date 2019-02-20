# -*- coding: utf-8 -*-
# Copyright (c) 2018, Frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import cint,cstr
import datetime

class ECSReportForRBI(Document):
	def create_rbi_ecs_record(self):
		month = datetime.datetime.strptime(self.month, '%B').strftime("%m")
		salary_date = self.year+"-"+month+"-%"
		employee_details = frappe.db.sql("""
				select emp.employee, emp.employee_name, emp.ifsc_code, emp.micr, 
					sal.branch, sal.bank_account_no, sal.gross_pay
				from `tabSalary Slip` sal, `tabEmployee` emp
				where emp.employee = sal.employee
				and emp.status = "Active"
				and sal.start_date LIKE %s
				and sal.bank_account_no IS NOT NULL
				and emp.ifsc_code NOT LIKE "MAHB"
				and sal.docstatus = 1 
				""", (salary_date), as_dict = 1)	
		emp_ecs_details = []
		max_pay = 0
		total_pay = 0
		for e in employee_details:
			emp_ecs_record = ("22"+cstr(e.micr)+cstr(e.bank_ac_no)).ljust(31)[:31] 
			emp_name = e.employee_name.ljust(40)[:40]
			company_code = "4000141034005034T.M.C. ".ljust(23)[:23]
			branch = cstr(e.branch).ljust(13)[:13]     
			emp_code = cstr(e.employee).ljust(13)[:13]
			emp_pay = "{0:013}".format(cint(employee_details[0].get("gross_pay")*100))[:13]
			max_pay = max(max_pay, cint(emp_pay))
			total_pay += cint(emp_pay)
			emp_ecs_record = emp_ecs_record + emp_name + company_code + branch + emp_code + emp_pay
			emp_ecs_details.append(emp_ecs_record.ljust(155))	
		
		max_pay = "{0:016}".format(max_pay)[:16]
		total_pay = "{0:015}".format(total_pay)[:15]
		payment_date = datetime.datetime.strptime(self.payment_date, '%Y-%m-%d').strftime("%m%d%y")
		ecs_id = max_pay+total_pay + payment_date
		ecs_header = ("114005034THANE MUNICIPAL CORPORATION,THANE".ljust(49)+"SALARY-SEP201800000000040001410320010700535".ljust(47)+ecs_id).ljust(155) 
		
		return {"emp_ecs_details" : emp_ecs_details,
			"ecs_header" : ecs_header}

	def generate_report_and_get_url(self):
		data = self.create_rbi_ecs_record()
		ecs_report = data["ecs_header"]+"\n"
		ecs_report += "\n".join(data["emp_ecs_details"])
		f = frappe.get_doc({
			'doctype': 'File',
			'file_name': 'ecs-report-'+self.payment_date+'.txt',
			'content': ecs_report,
			'is_private': True
		})
		f.save()
		return f.file_url