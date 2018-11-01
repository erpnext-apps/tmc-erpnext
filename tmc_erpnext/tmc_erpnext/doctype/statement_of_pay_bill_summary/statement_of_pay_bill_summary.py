# -*- coding: utf-8 -*-
# Copyright (c) 2018, Frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.utils import flt

class StatementOfPayBillSummary(Document):
	pass

@frappe.whitelist()
def get_data(company = None, department = None, branch = None, period = None):

	conditions = get_conditions(company, department, branch, period)

	entry = frappe.db.sql(""" select sal.department, sum(sal.gross_pay) as gross, sum(sal.total_deduction) as deduction, sum(sal.net_pay) as net_pay
		from `tabSalary Slip` sal
		where sal.docstatus = 1 %s
		group by sal.department
	""" % (conditions), as_dict=1)

	data = frappe.db.sql(""" select sal.department, ded.short_name, sum(ded.amount) as amount
		from `tabSalary Slip` sal, `tabSalary Detail` ded
		where sal.name = ded.parent
		and ded.parentfield = 'deductions'
		and ded.parenttype = 'Salary Slip'
		and sal.docstatus = 1 %s
		group by sal.department,ded.short_name
	""" % (conditions ), as_dict=1)

	data_dict = {}

	for d in data:
		if data_dict.get(d.department):
			data_dict[d.department]["short_name"] = d.short_name
			data_dict[d.department][d.short_name] = d.amount
		else:
			data_dict.setdefault(
				d.department,{
					"short_name" : d.short_name,
					d.short_name: d.amount
				}
			)

	result = []

	sr_no = 1

	total = [[ 0 for i in range(1,20) ] for i in range(1,4) ]

	for d in entry:
		row = [[ 0 for i in range(1,20) ] for i in range(1,4,) ]

		row[0][0] = sr_no
		row[0][1] = d.department
		row[0][2] = d.gross
		row[0][18] = d.net_pay
		total[0][1] = "<b>Zone Total<b>"
		total[0][2] += row[0][2]

		row[1][2] = d.deduction
		total[1][2] += row[1][2]

		row, total = get_row(row, total, data_dict, d.department, 3, "RD", "IT", "PF Loan")

		row, total = get_row(row, total, data_dict, d.department, 4, "PF", "ADD PF", "DCPS")

		row, total = get_row(row, total, data_dict, d.department, 5, "DCPS R", "LEVY", "CCTD")

		row, total = get_row(row, total, data_dict, d.department, 6, "SOCIETY", "TEACH SOC", "HBA1")

		row, total = get_row(row, total, data_dict, d.department, 7, "HBA2", "HBA3", "HBA4")

		row, total = get_row(row, total, data_dict, d.department, 8, "SCOOT ADV", "FEST", "COMP ADV")

		row, total = get_row(row, total, data_dict, d.department, 9, "OTH ADV", "LIC", "BANK L")

		row, total = get_row(row, total, data_dict, d.department, 10, "POTAGI", "GIS", "Serv Chg")

		row, total = get_row(row, total, data_dict, d.department, 11, "AUDIT R", "FINE REC", "LWP")

		row, total = get_row(row, total, data_dict, d.department, 12, "EXTRA REC", "FLAG DAY", "ADHOC")

		row, total = get_row(row, total, data_dict, d.department, 13, "1 DAY", "MAHASANG", "LABW")

		row, total = get_row(row, total, data_dict, d.department, 14, "MAHAR", "LABW ADV", "MOB ADV")

		row, total = get_row(row, total, data_dict, d.department, 15, "PST1", "DED OTH", "OOD")

		row, total = get_row(row, total, data_dict, d.department, 16, "PT REC", "MEDI ADV", "LAP ADV")

		row, total = get_row(row, total, data_dict, d.department, 17, "CA ADV", "PTAX STAMP", "TMCFUND")

		result += row
		sr_no += 1

	result += total

	return result

def get_row(row, total, data_dict, department, index, short_name1, short_name2, short_name3):

	row[0][index] = flt(data_dict.get(department).get(short_name1)) if data_dict.get(department).get(short_name1) else 0
	row[1][index] = flt(data_dict.get(department).get(short_name2)) if data_dict.get(department).get(short_name2) else 0
	row[2][index] = flt(data_dict.get(department).get(short_name3)) if data_dict.get(department).get(short_name3) else 0

	total[0][index] += row[0][index] 
	total[1][index] += row[1][index]
	total[2][index] += row[2][index]

	return row,total


def get_conditions(company, department, branch, period):

	conditions = [""]

	if company:
		conditions.append("sal.company = '%s' " % (company) )

	if department:

		if department != "ALL":
			department_dict = frappe._dict(frappe.db.sql(""" select department_type,name from `tabDepartment`"""))
			conditions.append("sal.department = '%s' " % (department_dict.get(department)) )

	if branch:
		conditions.append("sal.branch = '%s' " % (branch) )

	if period:

		month = {
			"January":1,
			"February":2,
			"March":3,
			"April":4,
			"May":5,
			"June":6,
			"July":7,
			"August":8,
			"September":9,
			"October":10,
			"November":11,
			"December":12
		}

		conditions.append("month(sal.start_date) = '%s' " % (month.get(period)))

	return " and ".join(conditions)





